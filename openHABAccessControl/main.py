from flask import Flask, render_template, request
from operations.json_file_operations import delete_json_files
from operations.url_actions import process_url_form_data, process_oauth_form_data

app = Flask(__name__)


@app.route('/smart_home', methods=['GET'])
def serve_first_ui():
    return render_template('main.html')


@app.route('/smart_home_proxy', methods=['POST'])
def serve_proxy_data_ui():
    if request.method == 'POST':
        # Delete any .json file because user has to manually upload json file from UI
        delete_json_files()
        # process form data and then create http request to Proxy Server
        result_dict = process_url_form_data(request)
        return render_template("response.html", result=result_dict["status"], cont=result_dict["content"])


@app.route('/smart_home_oauth', methods=['GET'])
def serve_oauth_ui():
    return render_template('oauth.html')


@app.route('/smart_home_token_request_oauth', methods=['POST'])
def serve_oauth_token_request_ui():
    return process_oauth_form_data(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
