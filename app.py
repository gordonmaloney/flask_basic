from flask import *
import json, time
import ssl
from pyngrok import ngrok, conf, installer

pyngrok_config = conf.get_default()

if not os.path.exists(pyngrok_config.ngrok_path):
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    installer.install_ngrok(pyngrok_config.ngrok_path, context=context)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))    #/user/?user=gfengr

    data_set = {'Page': 'Request', 'Message': f'Successfully requested {user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777)
