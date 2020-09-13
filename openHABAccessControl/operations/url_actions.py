import json
from flask import send_from_directory, render_template
import requests
from operations.json_file_operations import store_token_to_file_system


def process_url_form_data(request_from_webpage):
    flag = False
    # first see if user wants to cause action
    # method: GET and URL value and file. Rest form variables are null-empty-default.
    res = request_from_webpage.form
    # if checkbox of body is default
    try:
        print(res['addBodyId'])
        flag = True
    except Exception:
        flag = False

    # common variables for both cases
    url = res['urlId']
    method_req = res['methodId']
    file = request_from_webpage.files['fileToUploadId']
    access_token_var = json.loads(file.read())['access_token']
    # save json file in order to open it and read token
    # file.save(secure_filename(file.filename))

    if flag:
        # Now take values from form
        body = res['dataId']
        # check for each method and act:
        if method_req == 'POST':
            w = 3
        elif method_req == 'PUT':
            t = 1
        elif method_req == 'DELETE':
            s = 0
    elif not flag:
        # create header and load json to read access token
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token_var + ''
        }
        # http request to Proxy Server
        response = requests.get('http://proxy-node:9000' + url, headers=headers)
        return response


def process_oauth_form_data(request_from_webpage):
    res = request_from_webpage.form
    # cause http to ControlThings Server
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': res['c_id'],
        'client_secret': res['c_sec']
    }
    response = requests.post('https://as.controlthings.gr/oauth2/token/stefanos2',
                             headers=headers, data=data, verify=False)
    if response.status_code == 200:
        json_web_token = response.json()
        # store token as json
        store_token_to_file_system(res['c_id'], json_web_token)
        return send_from_directory(directory="", filename=res['c_id'] + '.json', as_attachment=True)
    else:
        return render_template("response.html", result='Error occurred../Wrong Client Credentials')
