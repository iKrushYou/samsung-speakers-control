from flask import Flask
import samsungctl
import time

app = Flask(__name__)

keys = [
    ["KEY_HOME", 1, 0.5],
    ["KEY_LEFT", 5, 0.2],
    ["KEY_UP", 1, 0.1],
    ["KEY_RIGHT", 2, 0.1],
    ["KEY_ENTER", 1, 0.1],
    ["KEY_HOME", 1, 0.1],
]


@app.route('/')
def hello_world():
    return 'Hello, World!'


def send_key(remote, key, sleep):
    print('sending command ' + key)
    remote.control(key)
    time.sleep(sleep)


@app.route('/speakers-on')
def speakers_on():
    config = samsungctl.Config.load('/home/pi/speakers_on/samsung.conf')(
        name='samsungctl'
    )

    with samsungctl.Remote(config) as remote:
        for key in keys:
            for i in range(key[1]):
                send_key(remote, key[0], key[2])

    return "on"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

