import api
import data

# Create REST APIs
for rest_api in data.rest_apis:
    response = api.create_api(rest_api)
    if response.status_code == 201:
        print("REST API created successfully")
    else:
        print("Error while creating REST API")




