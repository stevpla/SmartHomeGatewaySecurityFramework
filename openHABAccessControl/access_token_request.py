#!/usr/bin/python

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
import json

# curl command which creates the request
# curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d
# "grant_type=client_credentials&client_id=8S0di1q1RoHn11tdENVUEw==&client_secret=myClientPassword"
# https://as.controlthings.gr/oauth2/token/stefanos2
# -----------------------------------------------------
# sys.argv[1] --> client_id
# sys.argv[2] --> client_secret
# -----------------------------------------------------


def request_jwt():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': str(sys.argv[1]),
        'client_secret': str(sys.argv[2])
    }
    # InsecureRequestWarning: Unverified HTTPS request is being made to host 'as.controlthings.gr'.
    # Adding certificate verification is strongly advised.
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    response = requests.post('https://as.controlthings.gr/oauth2/token/stefanos2',
                             headers=headers, data=data, verify=False)
    if response.status_code == 200:
        # store token as json
        json_web_token = response.json()
        store_token_to_file_system(json_web_token)
        return print('Server returned JWT: ' + str(json_web_token) + '\n')
    else:
        return print('Error: ' + response.status_code + ' status code.\n')


def store_token_to_file_system(token):
    # store token as json format to local fs
    with open(str(sys.argv[1]) + '.json', 'w', encoding='utf-8') as f:
        json.dump(token, f, ensure_ascii=False, indent=4)


def check_arguments():
    if len(sys.argv) != 3:
        return False
    else:
        return True


def main():
    print("Requesting JsonWebToken from Authorization Server..")
    if check_arguments():
        request_jwt()
    else:
        print('Error: Give all arguments.\n')


if __name__ == "__main__":
    main()
