import api
import data
import utils

for tenant in data.tenants:
    # Add tenant
    tenant_domain = tenant[tenant.index('<xsd:tenantDomain>') + 18:tenant.index('</xsd:tenantDomain>')]
    if tenant_domain != 'carbon.super':
        tenant_response = api.add_tenant(tenant)
        utils.validate_response(tenant_response, 200, 'adding tenant ' + tenant_domain)
        utils.login('admin@' + tenant_domain, 'admin')
    else:
        utils.login('admin', 'admin')
    # Add roles
    for role in data.roles:
        role_name = role[role.index('<xsd:roleName>') + 14:role.index('</xsd:roleName>')]
        role_response = api.add_role(role)
        utils.validate_response(role_response, 200, 'adding role ' + role_name)
    # Add users
    for user in data.users:
        user_name = user[user.index('<xsd:userName>') + 14:user.index('</xsd:userName>')]
        user_response = api.add_user(user)
        utils.validate_response(user_response, 200, 'adding user ' + user_name)
    # Add role alias mapping (scope assignment)
    role_alias_mapping_response = api.add_role_alias_mapping(data.aliases)
    utils.validate_response(role_alias_mapping_response, 200, 'adding role alias mapping')
    # Add api categories
    for api_category in data.api_categories:
        api_category_response = api.add_api_category(api_category)
        utils.validate_response(api_category_response, 201, 'adding api category ' + api_category['name'])
    # Add rate limiting policies (throttling policies)
    adv_tp_response = api.add_advanced_throttling_policy(data.advanced_throttling_policy)
    utils.validate_response(adv_tp_response, 201, 'adding advanced throttling policy')
    app_tp_response = api.add_application_throttling_policy(data.application_throttling_policy)
    utils.validate_response(app_tp_response, 201, 'adding application throttling policy')
    sub_tp_response = api.add_subscription_throttling_policy(data.subscription_throttling_policy)
    utils.validate_response(sub_tp_response, 201, 'adding subscription throttling policy')
    # Add shared scopes (global scopes)
    for shared_scope in data.shared_scopes:
        shared_scope_response = api.add_shared_scope(shared_scope)
        utils.validate_response(shared_scope_response, 201, 'adding shared scope ' + shared_scope['name'])
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Create rest api from scratch
    create_api_response = api.create_api(data.api_to_add_rest)
    utils.validate_response(create_api_response, 201, 'adding rest api')
    rest_api_id = create_api_response.json()['id']
    # Add documents
    for document in data.documents:
        add_document_response = api.add_document(rest_api_id, document)
        utils.validate_response(add_document_response, 201, 'adding document ' + document['name'])
        document_id = add_document_response.json()['documentId']
        if document['name'] in data.document_contents.keys():
            add_document_content_response = api.add_document_content(rest_api_id, document_id,
                                                                     data.document_contents[document['name']])
            utils.validate_response(add_document_content_response, 201, 'adding document content')
    # Add comment
    add_comment_response = api.add_comment(rest_api_id, data.comment)
    # Add mediation policy
    in_mediation_policy = None
    try:
        add_mediation_policy_response = api.add_mediation_policy(rest_api_id, data.mediation_policy)
        utils.validate_response(add_mediation_policy_response, 201, 'adding custom mediation policy')
        in_mediation_policy = add_mediation_policy_response.json()
    except:
        print('hence, default mediation policy will be added')
    # Get mediation policies
    get_mediation_policies_response = api.get_mediation_policies()
    utils.validate_response(get_mediation_policies_response, 200, 'getting mediation policies')
    if in_mediation_policy is None:
        in_mediation_policy = get_mediation_policies_response.json()['list'][6]
    out_mediation_policy = get_mediation_policies_response.json()['list'][11]
    fault_mediation_policy = get_mediation_policies_response.json()['list'][15]
    # Update api
    api_to_update = data.api_to_update_rest.copy()
    api_to_update['mediationPolicies'] = [in_mediation_policy, out_mediation_policy, fault_mediation_policy]
    update_api_response = api.update_api(rest_api_id, api_to_update)
    utils.validate_response(update_api_response, 200, 'updating rest api')
    # Create new version
    create_new_version_response = api.create_new_api_version(rest_api_id, '2.0.0')
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(rest_api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(rest_api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(rest_api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Import rest api from oas3
    try:
        import_api_response = api.import_api_from_oas(data.api_to_import_oas3)
        utils.validate_response(import_api_response, 201, 'importing oas3 api')
        api_id = import_api_response.json()['id']
    except:
        print('hence, not importing apis')
        continue
    # Update api
    update_api_response = api.update_api(api_id, data.api_to_update_oas3)
    utils.validate_response(update_api_response, 200, 'updating oas3 api')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0')
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    api_id_2 = create_new_version_response.json()['id']
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    # Block api 2.0.0
    create_revision_response = api.create_api_revision(api_id_2, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id_2 = create_revision_response.json()['id']
    deploy_revision_response = api.deploy_api_revision(api_id_2, revision_id_2, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    publish_api_response = api.change_api_status(api_id_2, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    block_api_response = api.change_api_status(api_id_2, 'Block')
    utils.validate_response(block_api_response, 200, 'blocking api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Import rest api from oas2
    try:
        import_api_response = api.import_api_from_oas(data.api_to_import_oas2)
        utils.validate_response(import_api_response, 201, 'importing oas2 api')
        api_id = import_api_response.json()['id']
    except:
        print('hence, not importing oas2 api')
        continue
    # Update api
    update_api_response = api.update_api(api_id, data.api_to_update_oas2)
    utils.validate_response(update_api_response, 200, 'updating oas2 api')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0', True)
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Import wsdl api
    import_wsdl_api_response = api.import_api_from_wsdl_definition(data.api_to_import_wsdl)
    utils.validate_response(import_wsdl_api_response, 201, 'importing wsdl api')
    api_id = import_wsdl_api_response.json()['id']
    # Update api
    update_wsdl_api_response = api.update_api(api_id, data.api_to_update_wsdl)
    utils.validate_response(update_wsdl_api_response, 200, 'updating wsdl api')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0', True)
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Import graphql api
    import_graphql_api_response = api.import_api_from_graphql_schema(data.api_to_import_graphql)
    utils.validate_response(import_graphql_api_response, 201, 'importing graphql api')
    api_id = import_graphql_api_response.json()['id']
    # Update api
    update_graphql_api_response = api.update_api(api_id, data.api_to_update_graphql)
    utils.validate_response(update_graphql_api_response, 200, 'updating graphql api')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0', True)
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Create websocket api
    create_websocket_api_response = api.create_api(data.api_to_add_websocket)
    utils.validate_response(create_websocket_api_response, 201, 'adding websocket api ')
    api_id = create_websocket_api_response.json()['id']
    # Update api definition
    update_api_definition_response = api.update_async_api_definition(api_id, data.api_definition_websocket)
    utils.validate_response(update_api_definition_response, 200, 'updating api definition')
    # Update api
    update_websocket_api_response = api.update_api(api_id, data.api_to_update_websocket)
    utils.validate_response(update_websocket_api_response, 200, 'updating websocket api ')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0')
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Create websub api
    create_websub_api_response = api.create_api(data.api_to_add_websub)
    utils.validate_response(create_websub_api_response, 201, 'adding websub api ')
    api_id = create_websub_api_response.json()['id']
    # Update api definition
    update_api_definition_response = api.update_async_api_definition(api_id, data.api_definition_websub)
    utils.validate_response(update_api_definition_response, 200, 'updating api definition')
    # Update api
    update_websub_api_response = api.update_api(api_id, data.api_to_update_websub)
    utils.validate_response(update_websub_api_response, 200, 'updating websub api ')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0')
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_crt_user@' + tenant_domain, 'adp_crt_user')
    # Create sse api
    create_sse_api_response = api.create_api(data.api_to_add_sse)
    utils.validate_response(create_sse_api_response, 201, 'adding sse api ')
    api_id = create_sse_api_response.json()['id']
    # Update api
    update_sse_api_response = api.update_api(api_id, data.api_to_update_sse)
    utils.validate_response(update_sse_api_response, 200, 'updating sse api ')
    # Create new version
    create_new_version_response = api.create_new_api_version(api_id, '2.0.0')
    utils.validate_response(create_new_version_response, 201, 'creating new version 2.0.0')
    # Create revision
    create_revision_response = api.create_api_revision(api_id, {'description': 'adp revision description'})
    utils.validate_response(create_revision_response, 201, 'creating revision')
    revision_id = create_revision_response.json()['id']
    # Deploy revision
    deploy_revision_response = api.deploy_api_revision(api_id, revision_id, data.revision)
    utils.validate_response(deploy_revision_response, 201, 'deploying revision')
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Publish api
    publish_api_response = api.change_api_status(api_id, 'Publish')
    utils.validate_response(publish_api_response, 200, 'publishing api')
    ####################################################################################################################
    utils.login('adp_pub_user@' + tenant_domain, 'adp_pub_user')
    # Create api product
    api_product_to_add = data.api_product_to_add.copy()
    api_product_to_add['apis'][0]['apiId'] = rest_api_id
    create_api_product_response = api.create_api_product(api_product_to_add)
    utils.validate_response(create_api_product_response, 201, 'adding api product')
    api_product_id = create_api_product_response.json()['id']
    # Update api product
    api_product_to_update = data.api_product_to_update.copy()
    api_product_to_update['apis'][0]['apiId'] = rest_api_id
    update_api_product_response = api.update_api_product(api_product_id, api_product_to_update)
    utils.validate_response(update_api_product_response, 200, 'updating api product')
    # Add documents
    for document in data.documents:
        add_document_response = api.add_document_to_api_product(api_product_id, document)
        utils.validate_response(add_document_response, 201, 'adding document ' + document['name'])
        document_id = add_document_response.json()['documentId']
        if document['name'] in data.document_contents.keys():
            add_document_content_response = api.add_document_content_to_api_product(
                api_product_id, document_id, data.document_contents[document['name']])
            utils.validate_response(add_document_content_response, 201, 'adding document content')
    ####################################################################################################################
