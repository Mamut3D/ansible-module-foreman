# -*- coding: utf-8 -*-
# (c) Radim Janča (Cesnet) 2018

try:
    from foreman.foreman import ForemanError
except ImportError:
    module.fail_json(msg='python-foreman module is required. See https://github.com/Nosmoht/python-foreman.')


def get_organization_ids(module, theforeman, organizations):
    result = []
    for i in range(0, len(organizations)):
        try:
            organization = theforeman.search_organization(data={'name': organizations[i]})
            if not organization:
                module.fail_json(msg='Could not find Organization {0}'.format(organizations[i]))
            result.append(organization.get('id'))
        except ForemanError as e:
            module.fail_json(msg='Search for Organization \'{loc}\' throws an Error: {err}'.format(loc=locations[i],err=e.message))
    return result

def get_location_ids(module, theforeman, locations):
    result = []
    for i in range(0, len(locations)):
        try:
            location = theforeman.search_location(data={'name':locations[i]})
            if not location:
                module.fail_json(msg='Could not find Location {0}'.format(locations[i]))
            result.append(location.get('id'))
        except ForemanError as e:
            module.fail_json(msg='Search for Location \'{loc}\' throws an Error: {err}'.format(loc=locations[i],err=e.message))
    return result
