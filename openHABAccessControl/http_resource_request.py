#!/usr/bin/python

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
import json
# import webbrowser

# curl command which creates the request
# curl -X GET -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJFUzI1N
# iIsInR5cCI6IkpXVCIsImtpZCI6ImNjNTIxZDQzLWE3YzEtNDUzOS04ODY2LWRlMmEyNDQyNDU5OSJ9.eyJjbGllbnRfaWQiOiJ
# sb2NhbC10b2tlbiIsInJvbGUiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZSI6Ii90aGluZ3M6cmVhZHdyaXRlIiwiaWF0IjoxNTk0OT
# kxOTUxLCJpc3MiOiJOb3Qgc2V0LiJ9.Q4X5Z4u2sE_Wq0aggkXnL95EoceJHY4UZjmdKkIFrp28-Cp1sK7tuQ6IdwqhesnAJVDB
# ASvR3UOF3Y8oXSBBUw" http://proxy-node:9000/URL_WHICH_DO_SOMETHING_TURN_ON
# -----------------------------------------------------
# sys.argv[1] --> json_path
# sys.argv[2] --> URL_WHICH_DOES_SMTHING
# -----------------------------------------------------


def request_resource():
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + load_access_token_from_json_file() + ''
    }

    # InsecureRequestWarning: Unverified HTTPS request is being made to host 'as.controlthings.gr'.
    # Adding certificate verification is strongly advised.
    # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    response = requests.get('http://proxy-node:9000/' + str(sys.argv[2]), headers=headers)
    if response.status_code == 200:
        # open html content in a firefox UI
        # json_web_token = response.json()
        # url = 'http://www.icsd.aegean.gr'
        # webbrowser.get('firefox').open_new_tab(url)
        return print('HTTP RESOURCE executed! \n')
    else:
        return print('Error: ' + response.status_code + ' status code.\n')


def load_access_token_from_json_file():
    # load access token from a json object
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        json_object = json.load(f)
    return json_object['access_token']


def check_arguments():
    if len(sys.argv) != 3:
        return False
    else:
        return True


def main():
    print("Requesting HTTP Resource From Proxy Server..")
    if check_arguments():
        request_resource()
    else:
        print('Error: Give all arguments.\n')


if __name__ == "__main__":
    main()

