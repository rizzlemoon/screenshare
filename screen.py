import pyscreenshot
import flask
import io
import argparse

app = flask.Flask(__name__)
default_interval = 500


@app.route('/screen.png')
def serve_pil_image():
    img_buffer = io.BytesIO()
    pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')


@app.route('/')
def serve_img():
    input_interval = flask.request.args.get("interval")
    if input_interval:
        try:
            int(input_interval)
        except:
            input_interval = None    
    return flask.render_template('screen.html', interval = input_interval or default_interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, dest='port', default=5000, required=False)
    parser.add_argument('-i', '--interval', type=int, dest='interval', default=500, required=False)
    args = parser.parse_args()

    default_interval = args.interval
    app.run(host='0.0.0.0', port=args.port, debug=True)
