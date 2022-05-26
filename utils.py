import config


def login(username, password):
    config.current_user['username'] = username
    config.current_user['password'] = password


def validate_response(response, status_code, task):
    if response.status_code == status_code:
        print('Completed ' + task)
        return True
    else:
        print('Error while ' + task)
        return False
