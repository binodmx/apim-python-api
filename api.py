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


def get_consumer_credentials(client_name):
    url = config.host + config.client_register_path
    headers = {
        'Authorization': 'Basic %s' % base64.b64encode(
            str(config.current_user['username'] + ':' + config.current_user['password']).encode()).decode('utf-8'),
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        'callbackUrl': 'www.google.lk',
        'clientName': client_name,
        'owner': config.current_user['username'],
        'grantType': 'password refresh_token',
        'saasApp': True
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()


def get_access_token(client_name, scopes):
    consumer_credentials = get_consumer_credentials(client_name)
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
# Admin API
########################################################################################################################


def add_advanced_throttling_policy(body):
    url = config.host + config.admin_path + '/throttling/policies/advanced'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_application_throttling_policy(body):
    url = config.host + config.admin_path + '/throttling/policies/application'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_subscription_throttling_policy(body):
    url = config.host + config.admin_path + '/throttling/policies/subscription'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_custom_throttling_policy(body):
    url = config.host + config.admin_path + '/throttling/policies/custom'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_role_alias_mapping(body):
    url = config.host + config.admin_path + '/system-scopes/role-aliases'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:admin_operations'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.put(url, headers=headers, data=data, verify=False)
    return response


def add_api_category(body):
    url = config.host + config.admin_path + '/api-categories'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:admin_operations'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


########################################################################################################################
# Publisher API
########################################################################################################################


def create_api(body):
    url = config.host + config.publisher_path + '/apis'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def update_api(api_id, body):
    url = config.host + config.publisher_path + '/apis/' + api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.put(url, headers=headers, data=data, verify=False)
    return response


def import_api_from_oas(file_path='', file_url='', additional_properties={}, inline_api_definition=''):
    url = config.host + config.publisher_path + '/apis/import-openapi'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
    }
    files = {
        'file': open(file_path, 'rb'),
        'url': file_url,
        'additionalProperties': json.dumps(additional_properties),
        'inlineAPIDefinition': inline_api_definition
    }
    print(files)
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def import_api_from_wsdl_definition(file_path=None, file_url=None, additional_properties=None, implementation_type=None):
    url = config.host + config.publisher_path + '/apis/import-wsdl'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
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
    url = config.host + config.publisher_path + '/apis/import-graphql-schema'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
    }
    files = {
        'type': definition_type,
        'file': open(file_path, 'rb'),
        'additionalProperties': additional_properties
    }
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def create_new_api_version(api_id, new_version, default_version=False):
    url = config.host + config.publisher_path + '/apis/copy-api'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
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


def create_application(body):
    url = config.host + config.devportal_path + '/applications'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_devportal', 'apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def generate_application_keys(application_id, body):
    url = config.host + config.devportal_path + '/applications/' + application_id + "/generate-keys"
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_devportal', 'apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def generate_application_token(application_id, key_mapping_id, body):
    url = config.host + config.devportal_path + '/applications/' + application_id \
          + "/oauth-keys/" + key_mapping_id + "/generate-token"
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_devportal', 'apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response
