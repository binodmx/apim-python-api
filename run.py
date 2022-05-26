import api
import data
import utils

for tenant in data.tenants:
    # Add tenant
    tenant_domain = tenant[tenant.index('<xsd:tenantDomain>')+18:tenant.index('</xsd:tenantDomain>')]
    if tenant_domain != 'carbon.super':
        tenant_response = api.add_tenant(tenant)
        utils.validate_response(tenant_response, 200, 'adding tenant ' + tenant_domain)
        utils.login('admin@' + tenant_domain, 'admin')
    else:
        utils.login('admin', 'admin')
    # Add roles
    for role in data.roles:
        role_name = role[role.index('<xsd:roleName>')+14:role.index('</xsd:roleName>')]
        role_response = api.add_role(role)
        utils.validate_response(role_response, 200, 'adding role ' + role_name)
    # Add users
    for user in data.users:
        user_name = user[user.index('<xsd:userName>')+14:user.index('</xsd:userName>')]
        user = user.replace(user_name, user_name + '@' + tenant_domain)
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
