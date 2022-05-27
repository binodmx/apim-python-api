tenants = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:tenantDomain>carbon.super</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:active>true</xsd:active><xsd:admin>admin</xsd:admin><xsd:adminPassword>admin</xsd:adminPassword><xsd:email>john.doe@adp-example.com</xsd:email><xsd:firstname>John</xsd:firstname><xsd:lastname>Doe</xsd:lastname><xsd:tenantDomain>adp-example.com</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://services.mgt.tenant.carbon.wso2.org" xmlns:xsd="http://beans.common.stratos.carbon.wso2.org/xsd"><soapenv:Header/><soapenv:Body><ser:addTenant><ser:tenantInfoBean><xsd:active>true</xsd:active><xsd:admin>admin</xsd:admin><xsd:adminPassword>admin</xsd:adminPassword><xsd:email>tom.henry@adp-sample.com</xsd:email><xsd:firstname>Tom</xsd:firstname><xsd:lastname>Henry</xsd:lastname><xsd:tenantDomain>adp-sample.com</xsd:tenantDomain></ser:tenantInfoBean></ser:addTenant></soapenv:Body></soapenv:Envelope>'
]

roles = [
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_CREATOR</xsd:roleName><xsd:permissions>/permission/admin/login</xsd:permissions><xsd:permissions>/permission/admin/manage/api/create</xsd:permissions><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_PUBLISHER</xsd:roleName><xsd:permissions>/permission/admin/login</xsd:permissions><xsd:permissions>/permission/admin/manage/api/publish</xsd:permissions><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://org.apache.axis2/xsd"><soapenv:Header/><soapenv:Body><xsd:addRole><xsd:roleName>ADP_SUBSCRIBER</xsd:roleName><xsd:permissions>/permission/admin/login</xsd:permissions><xsd:permissions>/permission/admin/manage/api/subscribe</xsd:permissions><xsd:isSharedRole>false</xsd:isSharedRole></xsd:addRole></soapenv:Body></soapenv:Envelope>',
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
    'policyName': 'ADPBrass',
    'description': 'Allows 20 requests per minute',
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

shared_scopes = [
    {
        'name': 'adp-shared-scope-with-roles',
        'displayName': 'ADP Shared Scope with Roles',
        'description': 'Shared scope with role mapping',
        'bindings': ['ADP_CREATOR', 'ADP_PUBLISHER']
    },
    {
        'name': 'adp-shared-scope-without-roles',
        'displayName': 'ADP Shared Scope without Roles',
        'description': 'Shared scope without role mapping'
    }
]

api_to_add = {
    'name': 'ADP_REST_API_SCRATCH',
    'description': 'adp api description',
    'context': '/adp-rest-api-scratch',
    'version': '1.0.0',
    'provider': 'admin',
    'lifeCycleStatus': 'CREATED',
    'responseCachingEnabled': False,
    'cacheTimeout': 300,
    'hasThumbnail': False,
    'isDefaultVersion': False,
    'isRevision': False,
    'revisionId': 0,
    'enableSchemaValidation': True,
    'type': 'HTTP',
    'transport': [
        'http',
        'https'
    ],
    'tags': [
        'adp-tag'
    ],
    'policies': [
        'ADPBrass'
    ],
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory',
        'api_key'
    ],
    'visibility': 'PUBLIC',
    'subscriptionAvailability': 'CURRENT_TENANT',
    'additionalProperties': [
        {
            'name': 'adp-property',
            'value': 'adp-property-value',
            'display': True
        }
    ],
    'accessControl': 'NONE',
    'businessInformation': {
        'businessOwner': 'ADP Business Owner',
        'businessOwnerEmail': 'adp.bo@gmail.com',
        'technicalOwner': 'ADO Technical Owner',
        'technicalOwnerEmail': 'adp.to@gmail.com'
    },
    'corsConfiguration': {
        'corsConfigurationEnabled': False,
        'accessControlAllowCredentials': False,
        'accessControlAllowOrigins': [
            '*'
        ],
        'accessControlAllowHeaders': [
            'authorization',
            'Access-Control-Allow-Origin',
            'Content-Type',
            'SOAPAction',
            'apikey',
            'Internal-Key'
        ],
        'accessControlAllowMethods': [
            'GET',
            'PUT',
            'POST',
            'DELETE',
            'PATCH',
            'OPTIONS'
        ]
    },
    'websubSubscriptionConfiguration': {
        'enable': False,
        'secret': '',
        'signingAlgorithm': 'SHA1',
        'signatureHeader': 'x-hub-signature'
    },
    'endpointConfig': {
        'endpoint_type': 'http',
        'sandbox_endpoints': {
            'url': 'https: //reqres.in/api'
        },
        'production_endpoints': {
            'url': 'https: //reqres.in/api'
        }
    },
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [
        {
            'scope': {
                'id': None,
                'name': 'adp-local-scope-without-roles',
                'displayName': 'adp-local-scope-without-roles',
                'description': 'Local scope without role mapping',
                'bindings': [

                ],
                'usageCount': None
            },
            'shared': False
        },
        {
            'scope': {
                'id': None,
                'name': 'adp-shared-scope-with-roles',
                'displayName': 'adp-shared-scope-with-roles',
                'description': 'Shared scope with role mapping',
                'bindings': [
                    'ADP_CREATOR',
                    'ADP_PUBLISHER'
                ],
                'usageCount': None
            },
            'shared': True
        },
        {
            'scope': {
                'id': None,
                'name': 'adp-shared-scope-without-roles',
                'displayName': 'adp-shared-scope-without-roles',
                'description': 'Shared scope without role mapping',
                'bindings': [

                ],
                'usageCount': None
            },
            'shared': True
        }
    ],
    'operations': [
        {
            'id': '',
            'target': '/users/{id}',
            'verb': 'GET',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-local-scope-without-roles',
                'adp-shared-scope-without-roles'
            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/users/{id}',
            'verb': 'DELETE',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'ADP10PerMin',
            'scopes': [

            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/users',
            'verb': 'GET',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-local-scope-without-roles'
            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/users',
            'verb': 'POST',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-shared-scope-with-roles'
            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/login',
            'verb': 'POST',
            'authType': 'None',
            'throttlingPolicy': 'Unlimited',
            'scopes': [

            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        }
    ],
    'categories': [
        'adp-rest'
    ],
    'keyManagers': [
        'all'
    ],
    'advertiseInfo': {
        'advertised': False,
        'originalDevPortalUrl': None,
        'apiOwner': 'admin',
        'vendor': 'WSO2'
    }
}

api_to_update = {
    'name': 'ADP_REST_API_SCRATCH',
    'description': 'adp api description',
    'context': '/adp-rest-api-scratch',
    'version': '1.0.0',
    'provider': 'admin',
    'lifeCycleStatus': 'CREATED',
    'responseCachingEnabled': False,
    'cacheTimeout': 300,
    'hasThumbnail': False,
    'isDefaultVersion': False,
    'isRevision': False,
    'revisionedApiId': None,
    'revisionId': 0,
    'enableSchemaValidation': True,
    'type': 'HTTP',
    'transport': [
        'http',
        'https'
    ],
    'tags': [
        'adp-tag'
    ],
    'policies': [
        'ADPBrass'
    ],
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory',
        'api_key'
    ],
    'visibility': 'PUBLIC',
    'mediationPolicies': [],
    'subscriptionAvailability': 'CURRENT_TENANT',
    'additionalProperties': [
        {
            'name': 'adp-property',
            'value': 'adp-property-value',
            'display': True
        }
    ],
    'monetization': None,
    'accessControl': 'NONE',
    'businessInformation': {
        'businessOwner': 'ADP Business Owner',
        'businessOwnerEmail': 'adp.bo@gmail.com',
        'technicalOwner': 'ADO Technical Owner',
        'technicalOwnerEmail': 'adp.to@gmail.com'
    },
    'corsConfiguration': {
        'corsConfigurationEnabled': False,
        'accessControlAllowOrigins': [
            '*'
        ],
        'accessControlAllowCredentials': False,
        'accessControlAllowHeaders': [
            'authorization',
            'Access-Control-Allow-Origin',
            'Content-Type',
            'SOAPAction',
            'apikey',
            'Internal-Key'
        ],
        'accessControlAllowMethods': [
            'GET',
            'PUT',
            'POST',
            'DELETE',
            'PATCH',
            'OPTIONS'
        ]
    },
    'websubSubscriptionConfiguration': {
        'enable': False,
        'secret': '',
        'signingAlgorithm': 'SHA1',
        'signatureHeader': 'x-hub-signature'
    },
    'workflowStatus': None,
    'endpointConfig': {
        'endpoint_type': 'http',
        'sandbox_endpoints': {
            'url': 'https: //reqres.in/api'
        },
        'production_endpoints': {
            'url': 'https: //reqres.in/api'
        }
    },
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [
        {
            'scope': {
                'id': None,
                'name': 'adp-local-scope-without-roles',
                'displayName': 'adp-local-scope-without-roles',
                'description': 'Local scope without role mapping',
                'bindings': [

                ],
                'usageCount': None
            },
            'shared': False
        },
        {
            'scope': {
                'id': None,
                'name': 'adp-shared-scope-with-roles',
                'displayName': 'adp-shared-scope-with-roles',
                'description': 'Shared scope with role mapping',
                'bindings': [
                    'ADP_CREATOR',
                    'ADP_PUBLISHER'
                ],
                'usageCount': None
            },
            'shared': True
        },
        {
            'scope': {
                'id': None,
                'name': 'adp-shared-scope-without-roles',
                'displayName': 'adp-shared-scope-without-roles',
                'description': 'Shared scope without role mapping',
                'bindings': [

                ],
                'usageCount': None
            },
            'shared': True
        }
    ],
    'operations': [
        {
            'id': '',
            'target': '/users/{id}',
            'verb': 'GET',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-local-scope-without-roles',
                'adp-shared-scope-without-roles'
            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/users/{id}',
            'verb': 'DELETE',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'ADP10PerMin',
            'scopes': [

            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/users',
            'verb': 'GET',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-local-scope-without-roles'
            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/users',
            'verb': 'POST',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-shared-scope-with-roles'
            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        },
        {
            'id': '',
            'target': '/login',
            'verb': 'POST',
            'authType': 'None',
            'throttlingPolicy': 'Unlimited',
            'scopes': [

            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        }
    ],
    'threatProtectionPolicies': None,
    'categories': [
        'adp-rest'
    ],
    'keyManagers': [
        'all'
    ],
    'serviceInfo': None,
    'advertiseInfo': {
        'advertised': False,
        'originalDevPortalUrl': None,
        'apiOwner': 'admin',
        'vendor': 'WSO2'
    }
}

documents = [
    {
        'name': 'adp-inline-doc',
        'type': 'HOWTO',
        'summary': 'ADP inline doc summary',
        'sourceType': 'INLINE',
        'visibility': 'API_LEVEL',
        'sourceUrl': '',
        'otherTypeName': None,
        'inlineContent': ''
    },
    {
        'name': 'adp-markdown-doc',
        'type': 'HOWTO',
        'summary': 'ADP markdown doc summary',
        'sourceType': 'MARKDOWN',
        'visibility': 'API_LEVEL',
        'sourceUrl': '',
        'otherTypeName': None,
        'inlineContent': ''
    },
    {
        'name': 'adp-url-doc',
        'type': 'PUBLIC_FORUM',
        'summary': 'ADP url doc summary',
        'sourceType': 'URL',
        'visibility': 'API_LEVEL',
        'sourceUrl': 'https://apim.docs.wso2.com/en/latest/',
        'otherTypeName': None,
        'inlineContent': ''
    },
    {
        'name': 'adp-file-doc',
        'type': 'OTHER',
        'summary': 'ADP file doc summary',
        'sourceType': 'FILE',
        'visibility': 'API_LEVEL',
        'sourceUrl': '',
        'otherTypeName': 'TXT',
        'inlineContent': ''
    }
]

document_contents = {
    'adp-inline-doc': {
        'inlineContent': "<p>ADP inline doc content</p>"
    },
    'adp-markdown-doc': {
        'inlineContent': "#ADP markdown doc content"
    },
    'adp-file-doc': {
        'file': open('./resources/adp-file-doc-content.txt', 'rb')
    }
}

comment = {
    'content': 'adp-comment',
    'category': 'general'
}

mediation_policy = {
    'type': 'in',
    'mediationPolicyFile': open('./resources/log_in_message.xml', 'rb')
}

revision = [{
    'name': 'Default',
    'vhost': 'localhost',
    'displayOnDevportal': True
}]

api_to_import_oas2 = {
    'file': open('./resources/oas_v2.json', 'rb'),
    'additionalProperties': '{"name": "ADP_REST_API_IMPORTED_OAS2", "version": "1.0.0", "context": "adp-rest-api-imported-oas2"}'
}

api_to_import_oas3 = {
    'file': open('./resources/oas_v3.json', 'rb'),
    'additionalProperties': '{"name": "ADP_REST_API_IMPORTED_OAS3", "version": "1.0.0", "context": "adp-rest-api-imported-oas3"}'
}

imported_api_to_update_oas2 = {
    'name': 'ADP_REST_API_IMPORTED_OAS2',
    'description': None,
    'context': '/adp-rest-api-imported-oas2',
    'version': '1.0.0',
    'provider': 'admin',
    'lifeCycleStatus': 'CREATED',
    'wsdlInfo': None,
    'wsdlUrl': None,
    'responseCachingEnabled': False,
    'cacheTimeout': 300,
    'hasThumbnail': False,
    'isDefaultVersion': False,
    'isRevision': False,
    'revisionedApiId': None,
    'revisionId': 0,
    'enableSchemaValidation': False,
    'type': 'HTTP',
    'transport': [
        'http',
        'https'
    ],
    'tags': [

    ],
    'policies': [
        'Unlimited'
    ],
    'apiThrottlingPolicy': None,
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory'
    ],
    'maxTps': {
        'production': 100,
        'sandbox': 10
    },
    'visibility': 'PUBLIC',
    'visibleRoles': [

    ],
    'visibleTenants': [

    ],
    'mediationPolicies': [

    ],
    'subscriptionAvailability': 'CURRENT_TENANT',
    'subscriptionAvailableTenants': [

    ],
    'additionalProperties': [
        {
            'name': 'adp-property',
            'value': 'adp-property-value',
            'display': True
        }
    ],
    'monetization': None,
    'accessControl': 'NONE',
    'accessControlRoles': [

    ],
    'businessInformation': {
        'businessOwner': None,
        'businessOwnerEmail': None,
        'technicalOwner': None,
        'technicalOwnerEmail': None
    },
    'corsConfiguration': {
        'corsConfigurationEnabled': True,
        'accessControlAllowOrigins': [
            '*'
        ],
        'accessControlAllowCredentials': False,
        'accessControlAllowHeaders': [
            'authorization',
            'Access-Control-Allow-Origin',
            'Content-Type',
            'SOAPAction',
            'apikey',
            'Internal-Key'
        ],
        'accessControlAllowMethods': [
            'GET',
            'PUT',
            'POST',
            'DELETE',
            'PATCH',
            'OPTIONS'
        ]
    },
    'websubSubscriptionConfiguration': {
        'enable': False,
        'secret': '',
        'signingAlgorithm': 'SHA1',
        'signatureHeader': 'x-hub-signature'
    },
    'workflowStatus': None,
    'createdTime': '2022-05-27 17:27:49.905',
    'lastUpdatedTime': '2022-05-27 17:31:00.013',
    'endpointConfig': {
        'endpoint_type': 'http',
        'sandbox_endpoints': {
            'template_not_supported': False,
            'url': 'https://run.mocky.io/v3/da0f0326-d549-4735-839a-250b6cfd0067'
        },
        'failOver': False,
        'production_endpoints': {
            'template_not_supported': False,
            'url': 'https://run.mocky.io/v3/da0f0326-d549-4735-839a-250b6cfd0067'
        }
    },
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [

    ],
    'operations': [
        {
            'id': '',
            'target': '/hello',
            'verb': 'GET',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [

            ],
            'usedProductIds': [

            ],
            'amznResourceName': None,
            'amznResourceTimeout': None,
            'payloadSchema': None,
            'uriMapping': None
        }
    ],
    'threatProtectionPolicies': None,
    'categories': [
        'adp-imported',
        'adp-rest'
    ],
    'keyManagers': [
        'all'
    ],
    'serviceInfo': None,
    'advertiseInfo': {
        'advertised': False,
        'originalDevPortalUrl': None,
        'apiOwner': 'admin',
        'vendor': 'WSO2'
    }
}

imported_api_to_update_oas3 = {
   'name': 'ADP_REST_API_IMPORTED_OAS2',
   'description': None,
   'context': '/adp_rest_api_imported_oas2',
   'version': '1.0.0',
   'provider': 'admin',
   'lifeCycleStatus': 'CREATED',
   'wsdlInfo': None,
   'wsdlUrl': None,
   'responseCachingEnabled': True,
   'cacheTimeout': 300,
   'hasThumbnail': False,
   'isDefaultVersion': True,
   'isRevision': False,
   'revisionedApiId': None,
   'revisionId': 0,
   'enableSchemaValidation': False,
   'type': 'HTTP',
   'transport': [
      'http',
      'https'
   ],
   'tags': [

   ],
   'policies': [
      'Unlimited'
   ],
   'apiThrottlingPolicy': 'ADP10PerMin',
   'authorizationHeader': 'Authorization',
   'securityScheme': [
      'oauth2',
      'oauth_basic_auth_api_key_mandatory',
      'basic_auth',
      'api_key'
   ],
   'maxTps': None,
   'visibility': 'PUBLIC',
   'visibleRoles': [

   ],
   'visibleTenants': [

   ],
   'mediationPolicies': [

   ],
   'subscriptionAvailability': 'CURRENT_TENANT',
   'subscriptionAvailableTenants': [

   ],
   'additionalProperties': [

   ],
   'monetization': None,
   'accessControl': 'NONE',
   'accessControlRoles': [

   ],
   'businessInformation': {
      'businessOwner': None,
      'businessOwnerEmail': None,
      'technicalOwner': None,
      'technicalOwnerEmail': None
   },
   'corsConfiguration': {
      'corsConfigurationEnabled': False,
      'accessControlAllowOrigins': [
         '*'
      ],
      'accessControlAllowCredentials': False,
      'accessControlAllowHeaders': [
         'authorization',
         'Access-Control-Allow-Origin',
         'Content-Type',
         'SOAPAction',
         'apikey',
         'Internal-Key'
      ],
      'accessControlAllowMethods': [
         'GET',
         'PUT',
         'POST',
         'DELETE',
         'PATCH',
         'OPTIONS'
      ]
   },
   'websubSubscriptionConfiguration': {
      'enable': False,
      'secret': '',
      'signingAlgorithm': 'SHA1',
      'signatureHeader': 'x-hub-signature'
   },
   'workflowStatus': None,
   'endpointConfig': {
      'endpoint_type': 'http',
      'sandbox_endpoints': {
         'url': 'https://run.mocky.io/v3/da0f0326-d549-4735-839a-250b6cfd0067'
      },
      'production_endpoints': {
         'url': 'https://run.mocky.io/v3/da0f0326-d549-4735-839a-250b6cfd0067'
      }
   },
   'endpointImplementationType': 'ENDPOINT',
   'scopes': [
      {
         'scope': {
            'id': None,
            'name': 'adp-local-scope-with-roles',
            'displayName': 'adp-local-scope-with-roles',
            'description': 'Local scope with role mapping',
            'bindings': [
               'ADP_PUBLISHER'
            ],
            'usageCount': None
         },
         'shared': False
      }
   ],
   'operations': [
      {
         'id': '',
         'target': '/hello',
         'verb': 'GET',
         'authType': 'Application & Application User',
         'throttlingPolicy': 'ADP10PerMin',
         'scopes': [
            'adp-local-scope-with-roles'
         ],
         'usedProductIds': [

         ],
         'amznResourceName': None,
         'amznResourceTimeout': None,
         'payloadSchema': None,
         'uriMapping': None
      }
   ],
   'threatProtectionPolicies': None,
   'categories': [
      'adp-imported',
      'adp-rest'
   ],
   'keyManagers': [
      'all'
   ],
   'serviceInfo': None,
   'advertiseInfo': {
      'advertised': False,
      'originalDevPortalUrl': None,
      'apiOwner': 'admin',
      'vendor': 'WSO2'
   }
}
