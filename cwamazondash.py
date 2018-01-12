'''
Created on 11.01.2018

@author: Sebastian.Thiems
'''

from flask import Flask, render_template, send_from_directory, jsonify, make_response

from ConfigurationService import ConfigurationService
from DashJSONEncoder import DashJSONEncoder

app = Flask(__name__, template_folder='html/')
app.json_encoder = DashJSONEncoder
configuration_service = ConfigurationService()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/js/<path:path>')
def get_javascript_files(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def get_css_files(path):
    return send_from_directory('css', path)


@app.route('/rest/v1/groups', methods=['GET'])
def get_groups():
    return make_response(jsonify(configuration_service.get_groups()), 200)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
