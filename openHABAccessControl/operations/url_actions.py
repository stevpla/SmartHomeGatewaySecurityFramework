import json
from flask import send_from_directory, render_template, jsonify
import requests
from operations.json_file_operations import store_token_to_file_system


def process_url_form_data(request_from_webpage):
    flag_body = False
    flag_response = False
    # first see if user wants to cause action
    # method: GET or DELETE and URL value and file. Rest form variables are null-empty-default.
    res = request_from_webpage.form
    # if checkbox of body is default
    try:
        print(res['addBodyId'])
        flag_body = True
    except Exception:
        flag_body = False

    # common variables for both cases
    url = res['urlId']
    method_req = res['methodId']
    file = request_from_webpage.files['fileToUploadId']
    access_token_var = json.loads(file.read())['access_token']
    # create header and load json to read access token
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token_var + ''
    }

    if flag_body:
        # Now take body from form
        body = res['dataId']
        # check for each method and act:
        if method_req == 'POST':
            response = requests.post('http://proxy-node:9000' + url, headers=headers, data=body)
        elif method_req == 'PUT':
            response = requests.put('http://proxy-node:9000' + url, headers=headers, data=body)
    elif not flag_body:
        # http request to Proxy Server
        if method_req == 'GET':
            response = requests.get('http://proxy-node:9000' + url, headers=headers)
        elif method_req == 'DELETE':
            response = requests.delete('http://proxy-node:9000' + url, headers=headers)
    # now check if response has json response. If no, put None
    try:
        print(response.json())
        flag_response = True
    except Exception:
        flag_response = False

    if flag_response:
        return {"status": response, "content": response.json()}
    elif not flag_response:
        return {"status": response, "content": []}


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
