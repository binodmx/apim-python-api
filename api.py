import json
import base64
import requests
import config


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


########################################################################################################################
# Admin Services API
########################################################################################################################


def add_tenant(tenant):
    url = config.host + '/services/TenantMgtAdminService'
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(config.admin_username + ':' + config.admin_password).encode()).decode('utf-8'),
        'Content-Type': 'text/xml',
        'SOAPAction': 'urn:addTenant'
    }
    data = tenant
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_role(tenant_username, tenant_password, role):
    url = config.host + '/services/UserAdmin'
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(tenant_username + ':' + tenant_password).encode()).decode('utf-8'),
        'Content-Type': 'text/xml',
        'SOAPAction': 'urn:addRole'
    }
    data = role
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_user(tenant_username, tenant_password, user):
    url = config.host + '/services/UserAdmin'
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(tenant_username + ':' + tenant_password).encode()).decode('utf-8'),
        'Content-Type': 'text/xml',
        'SOAPAction': 'urn:addUser'
    }
    data = user
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


########################################################################################################################
# Publisher API
########################################################################################################################


def get_consumer_credentials(username, password):
    url = config.host + config.client_register_path
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(username + ':' + password).encode()).decode('utf-8'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'callbackUrl': 'www.google.lk',
        'clientName': 'rest_api_publisher',
        'owner': username,
        'grantType': 'password refresh_token',
        'saasApp': True
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()


def get_access_token(user, scopes):
    consumer_credentials = get_consumer_credentials(user['username'], user['password'])
    url = config.host + config.token_path
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(
            str(consumer_credentials['clientId'] + ':' + consumer_credentials['clientSecret']).encode()).decode('utf-8'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'grant_type': 'password',
        'username': config.admin_username,
        'password': config.admin_password,
        'scope': scopes
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()['access_token']


def create_api(user, api):
    url = config.host + '/api/am/publisher/v2/apis'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token(user, 'apim:api_create'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(api)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def update_api(user, api_id, api):
    url = config.host + '/api/am/publisher/v2/apis/' + api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token(user, 'apim:api_create apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = api
    response = requests.put(url, headers=headers, data=data, verify=False)
    return response


def import_api_from_oas(file_path=None, file_url=None, additional_properties=None, inline_api_definition=None):
    url = config.host + '/api/am/publisher/v2/import-openapi/'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:api_create')
    }
    files = {
        'file': open(file_path, 'rb'),
        'url': file_url,
        'additionalProperties': additional_properties,
        'inline_api_definition': inline_api_definition
    }
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def import_api_from_graphql_schema(definition_type=None, file_path=None, additional_properties=None):
    url = config.host + '/api/am/publisher/v2/import-graphql-schema/'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:api_create')
    }
    files = {
        'type': definition_type,
        'file': open(file_path, 'rb'),
        'additionalProperties': additional_properties
    }
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


########################################################################################################################
# Developer Portal API
########################################################################################################################
