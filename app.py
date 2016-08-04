########################################################################

#Machine learning app as API, 
#	submit one set of parameters at a time and return json

########################################################################

from flask import Flask, render_template, url_for, redirect, Response
import json

app = Flask(__name__)

j = {
  "type": "service_account",
  "project_id": {"private_key_id": "some_number"}
}

@app.route('/')
def index():
	json_output = json.dumps(j)
	resp = Response(json_output, status=200, mimetype='application/json')
	resp.headers['Link'] = 'http://adampilz.com'
	#return render_template('index.html', json_output=resp)
	return resp



########################################################
# Shutting down flask server
########################################################
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


# run the app
app.run(host='0.0.0.0')


