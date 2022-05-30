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
        'grantType': 'client_credentials password refresh_token',
        'saasApp': True
    })
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()


def get_access_token(client_name, scopes):
    consumer_credentials = get_consumer_credentials(client_name)
    url = config.host + config.token_path
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(
            str(consumer_credentials['clientId'] + ':' + consumer_credentials['clientSecret']).encode()).decode(
            'utf-8'),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = 'grant_type=password&username=%s&password=%s&scope=%s' % (config.current_user['username'],
                                                                     config.current_user['password'], scopes)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.json()['access_token']


########################################################################################################################
# Admin API
########################################################################################################################


def add_advanced_throttling_policy(data):
    url = config.host + config.admin_path + '/throttling/policies/advanced'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_application_throttling_policy(data):
    url = config.host + config.admin_path + '/throttling/policies/application'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_subscription_throttling_policy(data):
    url = config.host + config.admin_path + '/throttling/policies/subscription'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_custom_throttling_policy(data):
    url = config.host + config.admin_path + '/throttling/policies/custom'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:tier_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_role_alias_mapping(data):
    url = config.host + config.admin_path + '/system-scopes/role-aliases'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:admin_operations'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.put(url, headers=headers, data=data, verify=False)
    return response


def add_api_category(data):
    url = config.host + config.admin_path + '/api-categories'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_admin', 'apim:admin apim:admin_operations'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


########################################################################################################################
# Publisher API
########################################################################################################################


def create_api(data):
    url = config.host + config.publisher_path + '/apis'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def update_api(api_id, data):
    url = config.host + config.publisher_path + '/apis/%s' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.put(url, headers=headers, data=data, verify=False)
    return response


def import_api_from_oas(files):
    url = config.host + config.publisher_path + '/apis/import-openapi'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
    }
    files = files
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


def import_api_from_wsdl_definition(files):
    url = config.host + config.publisher_path + '/apis/import-wsdl'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
    }
    files = files
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


def import_api_from_graphql_schema(files):
    url = config.host + config.publisher_path + '/apis/import-graphql-schema'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create')
    }
    files = files
    response = requests.post(url, headers=headers, files=files, verify=False)
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


def add_document(api_id, data):
    url = config.host + config.publisher_path + '/apis/%s/documents' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create apim:document_create'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_document_content(api_id, document_id, files):
    url = config.host + config.publisher_path + '/apis/%s/documents/%s/content' % (api_id, document_id)
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create apim:document_create')
    }
    files = files
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


def add_comment(api_id, data):
    url = config.host + config.publisher_path + '/apis/%s/comments' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:comment_write'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_mediation_policy(api_id, files):
    url = config.host + config.publisher_path + '/apis/%s/mediation-policies' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher',
                                                        'apim:api_create apim:mediation_policy_create'),
        'Content-Type': 'multipart/form-data'
    }
    files = files
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


def update_async_api_definition(api_id, files):
    url = config.host + config.publisher_path + '/apis/%s/asyncapi' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create'),
        'Content-Type': 'multipart/form-data'
    }
    files = files
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def create_api_revision(api_id, data):
    url = config.host + config.publisher_path + '/apis/%s/revisions' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher',
                                                        'apim:api_create apim:api_publish apim:api_import_export'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def deploy_api_revision(api_id, revision_id, data):
    url = config.host + config.publisher_path + '/apis/%s/deploy-revision' % api_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_create apim:api_publish'),
        'Content-Type': 'application/json'
    }
    params = {
        'revisionId': revision_id
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, params=params, data=data, verify=False)
    return response


def change_api_status(api_id, action):
    url = config.host + config.publisher_path + '/apis/change-lifecycle'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher',
                                                        'apim:api_publish apim:api_import_export'),
        'Content-Type': 'application/json'
    }
    params = {
        'apiId': api_id,
        'action': action
    }
    response = requests.post(url, headers=headers, params=params, verify=False)
    return response


def create_api_product(data):
    url = config.host + config.publisher_path + '/api-products'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def update_api_product(api_product_id, data):
    url = config.host + config.publisher_path + '/api-products/%s' % api_product_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.put(url, headers=headers, data=data, verify=False)
    return response


def add_document_to_api_product(api_product_id, data):
    url = config.host + config.publisher_path + '/api-products/%s/documents' % api_product_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_publish'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def add_document_content_to_api_product(api_product_id, document_id, files):
    url = config.host + config.publisher_path + '/api-products/%s/documents/%s/content' % (api_product_id, document_id)
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:api_publish')
    }
    files = files
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


def add_shared_scope(data):
    url = config.host + config.publisher_path + '/scopes'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher', 'apim:shared_scope_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def get_mediation_policies():
    url = config.host + config.publisher_path + '/mediation-policies'
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_publisher',
                                                        'apim:api_view apim:mediation_policy_view'),
    }
    response = requests.get(url, headers=headers, verify=False)
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
    url = config.host + config.devportal_path + '/applications/%s/generate-keys' % application_id
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_devportal', 'apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response


def generate_application_token(application_id, key_mapping_id, body):
    url = config.host + config.devportal_path + '/applications/%s/oauth-keys/%s/generate-token' \
          % (application_id, key_mapping_id)
    headers = {
        'Authorization': 'Bearer %s' % get_access_token('rest_api_devportal', 'apim:subscribe apim:app_manage'),
        'Content-Type': 'application/json'
    }
    data = json.dumps(body)
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response
