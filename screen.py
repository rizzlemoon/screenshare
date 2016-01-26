import pyscreenshot
import flask
import io
import argparse

app = flask.Flask(__name__)
conf = {
    'interval': 500,
    'prefix': ''
}

@app.route('/screen.png')
def serve_pil_image():
    img_buffer = io.BytesIO()
    pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')


@app.route('/')
def serve_img():
    interval = flask.request.args.get('interval') or conf['interval']
    return flask.render_template('screen.html', interval = interval, prefix = conf['prefix'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, dest='port', default=5000, required=False)
    parser.add_argument('-i', '--interval', type=int, dest='interval', default=500, required=False)
    parser.add_argument('-P', '--prefix', type=str, dest='prefix', default='', required=False)
    args = parser.parse_args()

    conf['interval'] = args.interval
    conf['prefix'] = args.prefix
    if args.prefix:
        app.config['APPLICATION_ROOT'] = args.prefix
    app.run(host='0.0.0.0', port=args.port, debug=True)
