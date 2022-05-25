import api
import data


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
for role in data.roles:
    response = api.add_role('admin@example.com', 'admin', role)
    validate_response(response, 200, 'adding role')

# Add users for tenant1
for user in data.users:
    response = api.add_user('admin@example.com', 'admin', user)
    validate_response(response, 200, 'adding user')

# Create REST APIs
for rest_api in data.rest_apis:
    response = api.create_api(user1, rest_api)
    if response.status_code == 201:
        print('REST API created successfully')
    else:
        print('Error while creating REST API')




