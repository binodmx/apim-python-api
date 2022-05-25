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
            str(config.admin_user['username'] + ':' + config.admin_user['password']).encode()).decode('utf-8'),
        'Content-Type': 'text/xml',
        'SOAPAction': 'urn:addTenant'
    }
    data = tenant
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_role(role):
    url = config.host + '/services/UserAdmin'
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(config.current_user['username'] + ':' + config.current_user['password']).encode()).decode('utf-8'),
        'Content-Type': 'text/xml',
        'SOAPAction': 'urn:addRole'
    }
    data = role
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_user(user):
    url = config.host + '/services/UserAdmin'
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(config.current_user['username'] + ':' + config.current_user['password']).encode()).decode('utf-8'),
        'Content-Type': 'text/xml',
        'SOAPAction': 'urn:addUser'
    }
    data = user
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


########################################################################################################################
# Token API
########################################################################################################################


def get_consumer_credentials():
    url = config.host + config.client_register_path
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(config.current_user['username'] + ':' + config.current_user['password']).encode()).decode('utf-8'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'callbackUrl': 'www.google.lk',
        'clientName': 'rest_api_publisher',
        'owner': config.current_user['username'],
        'grantType': 'password refresh_token',
        'saasApp': True
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()


def get_access_token(scopes):
    consumer_credentials = get_consumer_credentials()
    url = config.host + config.token_path
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(
            str(consumer_credentials['clientId'] + ':' + consumer_credentials['clientSecret']).encode()).decode('utf-8'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'grant_type': 'password',
        'username': config.current_user['username'],
        'password': config.current_user['password'],
        'scope': scopes
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()['access_token']


########################################################################################################################
# Publisher API
########################################################################################################################


def create_api(api):
    url = config.host + '/api/am/publisher/v2/apis'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:api_create'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(api)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def update_api(api_id, api):
    url = config.host + '/api/am/publisher/v2/apis/' + api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:api_create apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(api)
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
        'inlineAPIDefinition': inline_api_definition
    }
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def import_api_from_wsdl_definition(file_path=None, file_url=None, additional_properties=None, implementation_type=None):
    url = config.host + '/api/am/publisher/v2/import-wsdl/'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:api_create')
    }
    files = {
        'file': open(file_path, 'rb'),
        'url': file_url,
        'additionalProperties': additional_properties,
        'implementationType': implementation_type
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


def create_new_api_version(api_id, new_version, default_version=False):
    url = config.host + '/api/am/publisher/v2/apis/copy-api'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:api_create')
    }
    params = {
        'apiId': api_id,
        'newVersion': new_version,
        'defaultVersion': default_version,
    }
    response = requests.post(url, headers=headers, params=params, verify=False)
    return response


########################################################################################################################
# Developer Portal API
########################################################################################################################


def create_application(application):
    url = config.host + '/api/am/devportal/v2/applications'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(application)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def generate_application_keys(application_id, key_type, grant_types_to_be_supported):
    url = config.host + '/api/am/devportal/v2/applications/' + application_id + "/generate-keys"
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'keyType': key_type,
        'grantTypesToBeSupported': grant_types_to_be_supported
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def generate_application_token(application_id, key_mapping_id, consumer_secret, validity_period, scopes):
    url = config.host + '/api/am/devportal/v2/applications/' + application_id \
          + "/oauth-keys/" + key_mapping_id + "/generate-token"
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'consumerSecret': consumer_secret,
        'validityPeriod': validity_period,
        'scopes': scopes,
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response

