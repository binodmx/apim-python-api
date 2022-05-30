import api
import data
import utils

utils.login('admin', 'admin')
response = api.create_api(data.api_to_add_rest)
print(response.json())
