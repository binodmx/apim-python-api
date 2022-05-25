import api
import data
import config


def login(username, password):
    config.current_user['username'] = username
    config.current_user['password'] = password


def validate_response(response, status_code, task):
    if response.status_code == status_code:
        print(task + ': done')
    else:
        print('error while ' + task)


user1 = {'username': 'admin@example.com', 'password': 'admin'}


# Add tenants
for tenant in data.tenants:
    response = api.add_tenant(tenant)
    validate_response(response, 200, 'adding tenant')

# Add roles for tenant1
login('admin@example.com', 'admin')
for role in data.roles:
    response = api.add_role(role)
    validate_response(response, 200, 'adding role')

# Add users for tenant1
login('admin@example.com', 'admin')
for user in data.users:
    response = api.add_user('admin@example.com', 'admin', user)
    validate_response(response, 200, 'adding user')

# Create REST APIs
login('admin@example.com', 'admin')
for rest_api in data.rest_apis:
    response = api.create_api(user1, rest_api)
    if response.status_code == 201:
        print('REST API created successfully')
    else:
        print('Error while creating REST API')




