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

api_definition_websocket = {
    'apiDefinition': '{"asyncapi":"2.0.0","info":{"title":"ADPChatsAPI","version":"1.0.0"},"servers":{"production":{"url":"ws://localhost:8080","protocol":"ws"}},"channels":{"/notifications":{"parameters":{},"publish":{"x-uri-mapping":"/notifications"},"subscribe":{"x-uri-mapping":"/notifications"}},"/rooms/{roomID}":{"parameters":{"roomID":{"description":"","schema":{"type":"string"}}},"publish":{"x-uri-mapping":"/rooms?room={uri.var.roomID}"},"subscribe":{"x-uri-mapping":"/rooms?room={uri.var.roomID}"}}},"components":{"securitySchemes":{"oauth2":{"type":"oauth2","flows":{"implicit":{"authorizationUrl":"http://localhost:9999","scopes":{},"x-scopes-bindings":{}}}}}}}'
}

api_definition_websub = {
    'apiDefinition': '{"asyncapi":"2.0.0","info":{"title":"ADPRepoWatcherAPI","version":"1.0.0"},"channels":{"/issues":{"parameters":{},"subscribe":{}}},"components":{"securitySchemes":{"oauth2":{"type":"oauth2","flows":{"implicit":{"scopes":{}}}}}}}'
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

########################################################################################################################

api_to_add_rest = {
    'name': 'ADPRestAPI',
    'description': 'adp api description',
    'context': '/adp-rest',
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
            'name': 'adp-property-name',
            'value': 'adp-property-value',
            'display': True
        }
    ],
    'accessControl': 'NONE',
    'businessInformation': {
        'businessOwner': 'ADP Business Owner',
        'businessOwnerEmail': 'adp.bo@gmail.com',
        'technicalOwner': 'ADP Technical Owner',
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

api_to_import_oas2 = {
    'file': open('./resources/oas_v2.json', 'rb'),
    'additionalProperties': '{"name": "ADPOAS2RestAPI", "version": "1.0.0", "context": "adp-oas2-rest"}'
}

api_to_import_oas3 = {
    'file': open('./resources/oas_v3.json', 'rb'),
    'additionalProperties': '{"name": "ADPOAS3RestAPI", "version": "1.0.0", "context": "adp-oas3-rest"}'
}

api_to_import_wsdl = {
    'url': 'http://ws.cdyne.com/phoneverify/phoneverify.asmx?wsdl',
    'additionalProperties': '{"name":"ADPPhoneVerificationAPI","version":"1.0.0","context":"adp-phoneverify","policies":["Unlimited"],"endpointConfig":{"endpoint_type":"http","sandbox_endpoints":{"url":"http://ws.cdyne.com/phoneverify/phoneverify.asmx"},"production_endpoints":{"url":"http://ws.cdyne.com/phoneverify/phoneverify.asmx"}}}',
    'implementationType': 'SOAP'
}

api_to_import_graphql = {
    'type': 'GraphQL',
    'file': open('./resources/schema_graphql.graphql', 'rb'),
    'additionalProperties': '{"name":"ADPStarWarsAPI","version":"1.0.0","context":"adp-swapi","policies":["Unlimited"],"operations":[{"id":"0","target":"hero","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"1","target":"reviews","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"2","target":"search","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"3","target":"character","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"4","target":"droid","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"5","target":"human","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"6","target":"allHumans","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"7","target":"allDroids","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"8","target":"allCharacters","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"9","target":"starship","verb":"QUERY","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"10","target":"createReview","verb":"MUTATION","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null},{"id":"11","target":"reviewAdded","verb":"SUBSCRIPTION","authType":"Any","throttlingPolicy":null,"scopes":[],"usedProductIds":[],"amznResourceName":null,"amznResourceTimeout":null,"payloadSchema":null,"uriMapping":null}],"endpointConfig":{"endpoint_type":"http","sandbox_endpoints":{"url":"http://localhost:8080/graphql"},"production_endpoints":{"url":"http://localhost:8080/graphql"}}}'
}

api_to_add_websocket = {
   'name': 'ADPChatsAPI',
   'version': '1.0.0',
   'context': 'adp-chats',
   'type': 'WS',
   'policies': [
      'AsyncUnlimited'
   ],
   'endpointConfig': {
      'endpoint_type': 'ws',
      'sandbox_endpoints': {
         'url': 'ws://localhost:8080'
      },
      'production_endpoints': {
         'url': 'ws://localhost:8080'
      }
   }
}

api_to_add_websub = {
   'name': 'ADPRepoWatcherAPI',
   'version': '1.0.0',
   'context': 'adp-repo-watcher',
   'type': 'WEBSUB',
   'policies': [
      'AsyncWHUnlimited'
   ]
}

api_to_add_sse = {
   'name': 'ADPObserverAPI',
   'version': '1.0.0',
   'context': 'adp-observer',
   'type': 'SSE',
   'policies': [
      'AsyncUnlimited'
   ],
   'endpointConfig': {
      'endpoint_type': 'http',
      'sandbox_endpoints': {
         'url': 'http://localhost:8080'
      },
      'production_endpoints': {
         'url': 'http://localhost:8080'
      }
   }
}

api_product_to_add = {
    'name': 'ADPAPIProductAPI',
    'context': 'adp-api-product',
    'policies': [
        'Unlimited'
    ],
    'apis': [
        {
            'name': 'ADPRestAPI',
            'apiId': '4b7fb027-b5cb-47d3-b74a-028a2a7ef388',
            'operations': [
                {
                    'id': None,
                    'target': '/users/{id}',
                    'verb': 'GET',
                    'authType': None,
                    'throttlingPolicy': None,
                    'scopes': [

                    ]
                },
                {
                    'id': None,
                    'target': '/users',
                    'verb': 'GET',
                    'authType': None,
                    'throttlingPolicy': None,
                    'scopes': [

                    ]
                }
            ],
            'version': '1.0.0'
        }
    ],
    'transport': [
        'http',
        'https'
    ]
}

########################################################################################################################

api_to_update_rest = {
    'name': 'ADPRestAPI',
    'description': 'adp api description',
    'context': '/adp-rest',
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
            'name': 'adp-property-name',
            'value': 'adp-property-value',
            'display': True
        }
    ],
    'monetization': None,
    'accessControl': 'NONE',
    'businessInformation': {
        'businessOwner': 'ADP Business Owner',
        'businessOwnerEmail': 'adp.bo@gmail.com',
        'technicalOwner': 'ADP Technical Owner',
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

api_to_update_oas2 = {
    'name': 'ADPOAS2RestAPI',
    'description': None,
    'context': '/adp-oas2-rest',
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
            'name': 'adp-property-name',
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

api_to_update_oas3 = {
   'name': 'ADPOAS3RestAPI',
   'description': None,
   'context': '/adp-oas3-rest',
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

api_to_update_wsdl = {
    'name': 'ADPPhoneVerificationAPI',
    'description': None,
    'context': '/adp-phoneverify',
    'version': '1.0.0',
    'provider': 'admin',
    'lifeCycleStatus': 'CREATED',
    'wsdlInfo': {
        'type': 'WSDL'
    },
    'wsdlUrl': '/registry/resource/_system/governance/apimgt/applicationdata/provider/admin/ADPPhoneVerification/1.0.0/admin--ADPPhoneVerification1.0.0.wsdl',
    'responseCachingEnabled': False,
    'cacheTimeout': 300,
    'hasThumbnail': False,
    'isDefaultVersion': False,
    'isRevision': False,
    'revisionedApiId': None,
    'revisionId': 0,
    'enableSchemaValidation': False,
    'type': 'SOAP',
    'transport': [
        'http',
        'https'
    ],
    'tags': [
        'wsdl'
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
    'maxTps': None,
    'visibility': 'PUBLIC',
    'visibleRoles': [

    ],
    'visibleTenants': [

    ],
    'mediationPolicies': [
        {
            'id': 'b91ee57a-9c53-4b24-b354-ab39ff79dae3',
            'name': 'log_in_message',
            'type': 'IN',
            'shared': True
        },
        {
            'id': '145b7589-cb4d-472e-bab0-180e0b3db713',
            'name': 'log_out_message',
            'type': 'OUT',
            'shared': True
        }
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
            'url': 'http://ws.cdyne.com/phoneverify/phoneverify.asmx'
        },
        'production_endpoints': {
            'url': 'http://ws.cdyne.com/phoneverify/phoneverify.asmx'
        }
    },
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [

    ],
    'operations': [
        {
            'id': '',
            'target': '/*',
            'verb': 'POST',
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
        'adp-imported'
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

api_to_update_graphql = {
    'name': 'ADPStarWarsAPI',
    'description': None,
    'context': '/adp-swapi',
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
    'type': 'GRAPHQL',
    'transport': [
        'http',
        'https'
    ],
    'tags': [

    ],
    'policies': [
        'Bronze',
        'Gold',
        'Silver',
        'ADPBrass'
    ],
    'apiThrottlingPolicy': None,
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory'
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
        'businessOwner': 'ADP Business Owner',
        'businessOwnerEmail': 'adp.bo@gmail.com',
        'technicalOwner': 'ADP Technical Owner',
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
            'url': 'http://localhost:8080/graphql'
        },
        'production_endpoints': {
            'url': 'http://localhost:8080/graphql'
        }
    },
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [
        {
            'scope': {
                'id': None,
                'name': 'adp-admin',
                'displayName': 'adp-admin',
                'description': 'Local scope with role mapping',
                'bindings': [
                    'admin'
                ],
                'usageCount': None
            },
            'shared': False
        },
        {
            'scope': {
                'id': None,
                'name': 'adp-film-subscriber',
                'displayName': 'adp-film-subscriber',
                'description': 'Local scope without role mapping',
                'bindings': [

                ],
                'usageCount': None
            },
            'shared': False
        }
    ],
    'operations': [
        {
            'id': '',
            'target': 'allCharacters',
            'verb': 'QUERY',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-admin'
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
            'target': 'allDroids',
            'verb': 'QUERY',
            'authType': 'Application & Application User',
            'throttlingPolicy': 'Unlimited',
            'scopes': [
                'adp-film-subscriber'
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
            'target': 'allHumans',
            'verb': 'QUERY',
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
            'target': 'character',
            'verb': 'QUERY',
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
        },
        {
            'id': '',
            'target': 'createReview',
            'verb': 'MUTATION',
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
        },
        {
            'id': '',
            'target': 'droid',
            'verb': 'QUERY',
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
        },
        {
            'id': '',
            'target': 'hero',
            'verb': 'QUERY',
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
        },
        {
            'id': '',
            'target': 'human',
            'verb': 'QUERY',
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
        },
        {
            'id': '',
            'target': 'reviewAdded',
            'verb': 'SUBSCRIPTION',
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
        },
        {
            'id': '',
            'target': 'reviews',
            'verb': 'QUERY',
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
        },
        {
            'id': '',
            'target': 'search',
            'verb': 'QUERY',
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
        },
        {
            'id': '',
            'target': 'starship',
            'verb': 'QUERY',
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
        'adp-imported'
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

api_to_update_websocket = {
   'name': 'ADPChatsAPI',
   'description': None,
   'context': '/adp-chats',
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
   'type': 'WS',
   'transport': [

   ],
   'tags': [

   ],
   'policies': [
      'AsyncGold'
   ],
   'apiThrottlingPolicy': None,
   'authorizationHeader': 'Authorization',
   'securityScheme': [
      'oauth2',
      'oauth_basic_auth_api_key_mandatory'
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
      'endpoint_type': 'ws',
      'sandbox_endpoints': {
         'url': 'ws://localhost:8080'
      },
      'production_endpoints': {
         'url': 'ws://localhost:8080'
      }
   },
   'endpointImplementationType': 'ENDPOINT',
   'scopes': [

   ],
   'operations': [
      {
         'id': '',
         'target': '/rooms/{roomID}',
         'verb': 'PUBLISH',
         'authType': 'Application & Application User',
         'throttlingPolicy': 'Unlimited',
         'scopes': [

         ],
         'usedProductIds': [

         ],
         'amznResourceName': None,
         'amznResourceTimeout': None,
         'payloadSchema': None,
         'uriMapping': '/rooms?room={uri.var.roomID}'
      },
      {
         'id': '',
         'target': '/notifications',
         'verb': 'PUBLISH',
         'authType': 'Application & Application User',
         'throttlingPolicy': 'Unlimited',
         'scopes': [

         ],
         'usedProductIds': [

         ],
         'amznResourceName': None,
         'amznResourceTimeout': None,
         'payloadSchema': None,
         'uriMapping': '/notifications'
      },
      {
         'id': '',
         'target': '/notifications',
         'verb': 'SUBSCRIBE',
         'authType': 'Application & Application User',
         'throttlingPolicy': 'Unlimited',
         'scopes': [

         ],
         'usedProductIds': [

         ],
         'amznResourceName': None,
         'amznResourceTimeout': None,
         'payloadSchema': None,
         'uriMapping': '/notifications'
      },
      {
         'id': '',
         'target': '/rooms/{roomID}',
         'verb': 'SUBSCRIBE',
         'authType': 'Application & Application User',
         'throttlingPolicy': 'Unlimited',
         'scopes': [

         ],
         'usedProductIds': [

         ],
         'amznResourceName': None,
         'amznResourceTimeout': None,
         'payloadSchema': None,
         'uriMapping': '/rooms?room={uri.var.roomID}'
      }
   ],
   'threatProtectionPolicies': None,
   'categories': [

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

api_to_update_websub = {
    'name': 'ADPRepoWatcherAPI',
    'description': None,
    'context': '/adp-repo-watcher',
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
    'type': 'WEBSUB',
    'transport': [
        'http',
        'https'
    ],
    'tags': [

    ],
    'policies': [
        'AsyncWHGold'
    ],
    'apiThrottlingPolicy': None,
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory'
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
        'enable': True,
        'secret': '41e661da5bab63b24d672365f387af36',
        'signingAlgorithm': 'SHA1',
        'signatureHeader': 'x-hub-signature'
    },
    'workflowStatus': None,
    'endpointConfig': None,
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [

    ],
    'operations': [
        {
            'id': '',
            'target': '/issues',
            'verb': 'SUBSCRIBE',
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

api_to_update_sse = {
    'name': 'ADPObserverAPI',
    'description': None,
    'context': '/adp-observer',
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
    'type': 'SSE',
    'transport': [
        'http',
        'https'
    ],
    'tags': [

    ],
    'policies': [
        'AsyncGold'
    ],
    'apiThrottlingPolicy': None,
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory'
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
            'url': 'http://localhost:8080'
        },
        'production_endpoints': {
            'url': 'http://localhost:8080'
        }
    },
    'endpointImplementationType': 'ENDPOINT',
    'scopes': [

    ],
    'operations': [
        {
            'id': '',
            'target': '/*',
            'verb': 'SUBSCRIBE',
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

api_product_to_update = {
    'name': 'ADPAPIProductAPI',
    'context': '/adp-api-product',
    'description': None,
    'provider': 'admin',
    'hasThumbnail': None,
    'state': 'PUBLISHED',
    'enableSchemaValidation': False,
    'isRevision': False,
    'revisionedApiProductId': None,
    'revisionId': 0,
    'responseCachingEnabled': False,
    'cacheTimeout': 300,
    'visibility': 'PUBLIC',
    'visibleRoles': [

    ],
    'visibleTenants': [

    ],
    'accessControl': 'NONE',
    'accessControlRoles': [

    ],
    'apiType': None,
    'transport': [
        'http',
        'https'
    ],
    'tags': [

    ],
    'policies': [
        'ADPBrass'
    ],
    'apiThrottlingPolicy': None,
    'authorizationHeader': 'Authorization',
    'securityScheme': [
        'oauth2',
        'oauth_basic_auth_api_key_mandatory',
        'basic_auth',
        'api_key'
    ],
    'subscriptionAvailability': 'ALL_TENANTS',
    'subscriptionAvailableTenants': [

    ],
    'additionalProperties': [
        {
            'name': 'adp-property-name',
            'value': 'adp-property-value',
            'display': True
        }
    ],
    'monetization': None,
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
    'apis': [
        {
            'name': 'ADPRestAPI',
            'apiId': '4b7fb027-b5cb-47d3-b74a-028a2a7ef388',
            'version': '1.0.0',
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
                }
            ]
        }
    ],
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
    'categories': [

    ]
}

########################################################################################################################
