tenants = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:active>true</xsd:active><xsd:admin>admin</xsd:admin><xsd:adminPassword>admin</xsd:adminPassword><xsd:email>john.doe@example.com</xsd:email><xsd:firstname>John</xsd:firstname><xsd:lastname>Doe</xsd:lastname><xsd:tenantDomain>example.com</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>'
]

roles = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>CUSTOM_ROLE1</xsd:roleName><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>CUSTOM_ROLE2</xsd:roleName><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
]

users = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd" xmlns:xsd1="http://common.mgt.user.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><xsd:addUser><xsd:userName>user1</xsd:userName><xsd:password>user1</xsd:password><xsd:roles>CUSTOM_ROLE1</xsd:roles><xsd:roles>CUSTOM_ROLE2</xsd:roles></xsd:addUser></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd" xmlns:xsd1="http://common.mgt.user.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><xsd:addUser><xsd:userName>user2</xsd:userName><xsd:password>user2</xsd:password><xsd:roles>CUSTOM_ROLE1</xsd:roles><xsd:roles>CUSTOM_ROLE2</xsd:roles></xsd:addUser></soapenv:Body></soapenv:Envelope>'
]

rest_apis = [
    {
        'name': 'TestAPI1',
        'version': '1.0.0',
        'context': 'test1',
        'policies': ['Unlimited'],
        'endpointConfig': {
            'endpoint_type': 'http',
            'sandbox_endpoints': {'url': 'http://localhost:3000/'},
            'production_endpoints': {'url': 'http://localhost:3000/'}
        }
    },
    {
        'name': 'TestAPI2',
        'version': '1.0.0',
        'context': 'test2',
        'policies': ['Unlimited'],
        'endpointConfig': {
            'endpoint_type': 'http',
            'sandbox_endpoints': {'url': 'http://localhost:3000/'},
            'production_endpoints': {'url': 'http://localhost:3000/'}
        }
    }
]

graphql_schema_file_path = './resources/schema_graphql.graphql'


applications = [
    {
        'name': 'CalculatorApp',
        'throttlingPolicy': 'Unlimited',
        "description": "Sample calculator application"
    }
]

