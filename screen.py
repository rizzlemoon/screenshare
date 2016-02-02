import io

import argparse
import flask
import pyscreenshot


bp = flask.Blueprint('app', __name__)

@bp.route('/screen.png')
def serve_pil_image():
    img_buffer = io.BytesIO()
    pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')

@bp.route('/')
def serve_img():
    val = flask.request.args.get('interval') or flask.current_app.config['interval']
    return flask.render_template('screen.html', interval=val)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, dest='host', default='0.0.0.0', required=False)
    parser.add_argument('-p', '--port', type=int, dest='port', default=5000, required=False)
    parser.add_argument('-i', '--interval', type=int, dest='interval', default=500, required=False)
    parser.add_argument('-P', '--prefix', type=str, dest='prefix', default=None, required=False)
    args = parser.parse_args()
    
    app = flask.Flask(__name__)
    app.register_blueprint(bp, url_prefix=args.prefix)
    app.config['interval'] = args.interval
    app.run(host=args.host, port=args.port, debug=True)
