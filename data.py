tenants = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:tenantDomain>carbon.super</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:active>true</xsd:active><xsd:admin>admin</xsd:admin><xsd:adminPassword>admin</xsd:adminPassword><xsd:email>john.doe@adp-example.com</xsd:email><xsd:firstname>John</xsd:firstname><xsd:lastname>Doe</xsd:lastname><xsd:tenantDomain>adp-example.com</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:active>true</xsd:active><xsd:admin>admin</xsd:admin><xsd:adminPassword>admin</xsd:adminPassword><xsd:email>tom.henry@adp-sample.com</xsd:email><xsd:firstname>Tom</xsd:firstname><xsd:lastname>Henry</xsd:lastname><xsd:tenantDomain>adp-sample.com</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>'
]

roles = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_CREATOR</xsd:roleName><xsd:permissions>/permission/admin/login</xsd:permissions><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_PUBLISHER</xsd:roleName><xsd:permissions>/permission/admin/login</xsd:permissions><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_SUBSCRIBER</xsd:roleName><xsd:permissions>/permission/admin/login</xsd:permissions><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_COMMON</xsd:roleName><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>'
]

users = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd" xmlns:xsd1="http://common.mgt.user.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><xsd:addUser><xsd:userName>adp_crt_user</xsd:userName><xsd:password>adp_crt_user</xsd:password><xsd:roles>ADP_CREATOR</xsd:roles><xsd:roles>ADP_COMMON</xsd:roles></xsd:addUser></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd" xmlns:xsd1="http://common.mgt.user.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><xsd:addUser><xsd:userName>adp_pub_user</xsd:userName><xsd:password>adp_pub_user</xsd:password><xsd:roles>ADP_PUBLISHER</xsd:roles><xsd:roles>ADP_COMMON</xsd:roles></xsd:addUser></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd" xmlns:xsd1="http://common.mgt.user.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><xsd:addUser><xsd:userName>adp_sub_user</xsd:userName><xsd:password>adp_sub_user</xsd:password><xsd:roles>ADP_SUBSCRIBER</xsd:roles><xsd:roles>ADP_COMMON</xsd:roles></xsd:addUser></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd" xmlns:xsd1="http://common.mgt.user.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><xsd:addUser><xsd:userName>adp_nul_user</xsd:userName><xsd:password>adp_nul_user</xsd:password><xsd:roles>ADP_COMMON</xsd:roles></xsd:addUser></soapenv:Body></soapenv:Envelope>'
]

aliases = {
    'count': 3,
    'list': [
        {
            'role': 'Internal/creator',
            'aliases': ['ADP_CREATOR']
        },
        {
            'role': 'Internal/publisher',
            'aliases': ['ADP_PUBLISHER']
        },
        {
            'role': 'Internal/subscriber',
            'aliases': ['ADP_SUBSCRIBER']
        }
    ]
}

api_categories = [
    {
        'name': 'adp-imported'
    },
    {
        'name': 'adp-rest'
    }
]

advanced_throttling_policy = {
    'policyName': 'ADP10PerMin',
    'description': '10PerMinute',
    'conditionalGroups': [],
    'defaultLimit': {
        'type': 'REQUESTCOUNTLIMIT',
        'requestCount': {
            'timeUnit': 'min',
            'unitTime': '1',
            'requestCount': '10'
        },
        'bandwidth': None
    }
}

application_throttling_policy = {
    'policyName': 'ADP5PerMin',
    'description': '5PerMinute',
    'defaultLimit': {
        'type': 'REQUESTCOUNTLIMIT',
        'requestCount': {
            'requestCount': '5',
            'timeUnit': 'min',
            'unitTime': '1'
        }
    }
}

subscription_throttling_policy = {
    'policyName': 'ADPPlatinum',
    'description': 'Platinum',
    'defaultLimit': {
        'type': 'REQUESTCOUNTLIMIT',
        'requestCount': {
            'requestCount': '20',
            'timeUnit': 'min',
            'unitTime': '1'
        }
    },
    'subscriberCount': '5',
    'rateLimitCount': '5',
    'rateLimitTimeUnit': 'sec',
    'billingPlan': 'FREE',
    'stopOnQuotaReach': True,
    'customAttributes': [],
    'graphQLMaxComplexity': '10',
    'graphQLMaxDepth': '5',
    'monetization': {
        'monetizationPlan': 'FIXEDRATE',
        'properties': {
            'fixedPrice': '',
            'pricePerRequest': '',
            'currencyType': '',
            'billingCycle': 'week'
        }
    },
    'permissions': None
}

custom_throttling_policy = {
    'policyName': 'ADP_Custom',
    'description': 'Custom',
    'keyTemplate': '$userId',
    'siddhiQuery': "FROM   RequestStream SELECT   userId,   (userId = = 'admin@carbon.super') AS isEligible,   "
                   "str: concat('admin@carbon.super', '') as throttleKey INSERT INTO   EligibilityStream; FROM   "
                   "EligibilityStream [ isEligible = = true ] # throttler: timeBatch(1 min) SELECT   throttleKey,   "
                   "(count(userId) >= 5) as isThrottled,   expiryTimeStamp group by   throttleKey INSERT ALL EVENTS "
                   "into ResultStream; "
}
