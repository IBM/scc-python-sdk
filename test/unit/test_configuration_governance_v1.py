# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for ConfigurationGovernanceV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_scc.configuration_governance_v1 import *


_service = ConfigurationGovernanceV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://us.compliance.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Rules
##############################################################################
# region

class TestCreateRules():
    """
    Test Class for create_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_rules_all_params(self):
        """
        create_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules')
        mock_response = '{"rules": [{"request_id": "3cebc877-58e7-44a5-a292-32114fa73558", "status_code": 201, "rule": {"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}, "errors": [{"code": "bad_request", "message": "The rule is missing an account ID"}], "trace": "861263b4-cee3-4514-8d8c-05d17308e6eb"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {}
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a dict representation of a TargetResource model
        target_resource_model = {}
        target_resource_model['service_name'] = 'iam-groups'
        target_resource_model['resource_kind'] = 'service'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {}
        rule_required_config_model['description'] = 'Public access check'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {}
        enforcement_action_model['action'] = 'disallow'

        # Construct a dict representation of a RuleRequest model
        rule_request_model = {}
        rule_request_model['account_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_request_model['name'] = 'Disable public access'
        rule_request_model['description'] = 'Ensure that public access to account resources is disabled.'
        rule_request_model['rule_type'] = 'user_defined'
        rule_request_model['target'] = target_resource_model
        rule_request_model['required_config'] = rule_required_config_model
        rule_request_model['enforcement_actions'] = [enforcement_action_model]
        rule_request_model['labels'] = ['Access', 'IAM']

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {}
        create_rule_request_model['request_id'] = '3cebc877-58e7-44a5-a292-32114fa73558'
        create_rule_request_model['rule'] = rule_request_model

        # Set up parameter values
        rules = [create_rule_request_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_rules(
            rules,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['rules'] == [create_rule_request_model]


    @responses.activate
    def test_create_rules_required_params(self):
        """
        test_create_rules_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules')
        mock_response = '{"rules": [{"request_id": "3cebc877-58e7-44a5-a292-32114fa73558", "status_code": 201, "rule": {"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}, "errors": [{"code": "bad_request", "message": "The rule is missing an account ID"}], "trace": "861263b4-cee3-4514-8d8c-05d17308e6eb"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {}
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a dict representation of a TargetResource model
        target_resource_model = {}
        target_resource_model['service_name'] = 'iam-groups'
        target_resource_model['resource_kind'] = 'service'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {}
        rule_required_config_model['description'] = 'Public access check'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {}
        enforcement_action_model['action'] = 'disallow'

        # Construct a dict representation of a RuleRequest model
        rule_request_model = {}
        rule_request_model['account_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_request_model['name'] = 'Disable public access'
        rule_request_model['description'] = 'Ensure that public access to account resources is disabled.'
        rule_request_model['rule_type'] = 'user_defined'
        rule_request_model['target'] = target_resource_model
        rule_request_model['required_config'] = rule_required_config_model
        rule_request_model['enforcement_actions'] = [enforcement_action_model]
        rule_request_model['labels'] = ['Access', 'IAM']

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {}
        create_rule_request_model['request_id'] = '3cebc877-58e7-44a5-a292-32114fa73558'
        create_rule_request_model['rule'] = rule_request_model

        # Set up parameter values
        rules = [create_rule_request_model]

        # Invoke method
        response = _service.create_rules(
            rules,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['rules'] == [create_rule_request_model]


    @responses.activate
    def test_create_rules_value_error(self):
        """
        test_create_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules')
        mock_response = '{"rules": [{"request_id": "3cebc877-58e7-44a5-a292-32114fa73558", "status_code": 201, "rule": {"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}, "errors": [{"code": "bad_request", "message": "The rule is missing an account ID"}], "trace": "861263b4-cee3-4514-8d8c-05d17308e6eb"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {}
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a dict representation of a TargetResource model
        target_resource_model = {}
        target_resource_model['service_name'] = 'iam-groups'
        target_resource_model['resource_kind'] = 'service'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {}
        rule_required_config_model['description'] = 'Public access check'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {}
        enforcement_action_model['action'] = 'disallow'

        # Construct a dict representation of a RuleRequest model
        rule_request_model = {}
        rule_request_model['account_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_request_model['name'] = 'Disable public access'
        rule_request_model['description'] = 'Ensure that public access to account resources is disabled.'
        rule_request_model['rule_type'] = 'user_defined'
        rule_request_model['target'] = target_resource_model
        rule_request_model['required_config'] = rule_required_config_model
        rule_request_model['enforcement_actions'] = [enforcement_action_model]
        rule_request_model['labels'] = ['Access', 'IAM']

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {}
        create_rule_request_model['request_id'] = '3cebc877-58e7-44a5-a292-32114fa73558'
        create_rule_request_model['rule'] = rule_request_model

        # Set up parameter values
        rules = [create_rule_request_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rules": rules,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_rules(**req_copy)



class TestListRules():
    """
    Test Class for list_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_rules_all_params(self):
        """
        list_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules')
        mock_response = '{"offset": 6, "limit": 1000, "total_count": 11, "first": {"href": "href"}, "last": {"href": "href"}, "rules": [{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        transaction_id = 'testString'
        attached = True
        labels = 'SOC2,ITCS300'
        scopes = 'scope_id'
        limit = 1000
        offset = 38

        # Invoke method
        response = _service.list_rules(
            account_id,
            transaction_id=transaction_id,
            attached=attached,
            labels=labels,
            scopes=scopes,
            limit=limit,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string
        assert 'attached={}'.format('true' if attached else 'false') in query_string
        assert 'labels={}'.format(labels) in query_string
        assert 'scopes={}'.format(scopes) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_list_rules_required_params(self):
        """
        test_list_rules_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules')
        mock_response = '{"offset": 6, "limit": 1000, "total_count": 11, "first": {"href": "href"}, "last": {"href": "href"}, "rules": [{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'

        # Invoke method
        response = _service.list_rules(
            account_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'account_id={}'.format(account_id) in query_string


    @responses.activate
    def test_list_rules_value_error(self):
        """
        test_list_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules')
        mock_response = '{"offset": 6, "limit": 1000, "total_count": 11, "first": {"href": "href"}, "last": {"href": "href"}, "rules": [{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "account_id": account_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_rules(**req_copy)



class TestGetRule():
    """
    Test Class for get_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_rule_all_params(self):
        """
        get_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        mock_response = '{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            rule_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_rule_required_params(self):
        """
        test_get_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        mock_response = '{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.get_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_rule_value_error(self):
        """
        test_get_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        mock_response = '{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_rule(**req_copy)



class TestUpdateRule():
    """
    Test Class for update_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_rule_all_params(self):
        """
        update_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        mock_response = '{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {}
        target_resource_additional_target_attributes_item_model['name'] = 'testString'
        target_resource_additional_target_attributes_item_model['value'] = 'testString'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a dict representation of a TargetResource model
        target_resource_model = {}
        target_resource_model['service_name'] = 'iam-groups'
        target_resource_model['resource_kind'] = 'service'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {}
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_false'
        rule_required_config_model['value'] = 'testString'

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {}
        enforcement_action_model['action'] = 'audit_log'

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        name = 'Disable public access'
        description = 'Ensure that public access to account resources is disabled.'
        target = target_resource_model
        required_config = rule_required_config_model
        enforcement_actions = [enforcement_action_model]
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_type = 'user_defined'
        labels = ['SOC2', 'ITCS300']
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_rule(
            rule_id,
            if_match,
            name,
            description,
            target,
            required_config,
            enforcement_actions,
            account_id=account_id,
            rule_type=rule_type,
            labels=labels,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Disable public access'
        assert req_body['description'] == 'Ensure that public access to account resources is disabled.'
        assert req_body['target'] == target_resource_model
        assert req_body['required_config'] == rule_required_config_model
        assert req_body['enforcement_actions'] == [enforcement_action_model]
        assert req_body['account_id'] == '531fc3e28bfc43c5a2cea07786d93f5c'
        assert req_body['rule_type'] == 'user_defined'
        assert req_body['labels'] == ['SOC2', 'ITCS300']


    @responses.activate
    def test_update_rule_required_params(self):
        """
        test_update_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        mock_response = '{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {}
        target_resource_additional_target_attributes_item_model['name'] = 'testString'
        target_resource_additional_target_attributes_item_model['value'] = 'testString'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a dict representation of a TargetResource model
        target_resource_model = {}
        target_resource_model['service_name'] = 'iam-groups'
        target_resource_model['resource_kind'] = 'service'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {}
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_false'
        rule_required_config_model['value'] = 'testString'

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {}
        enforcement_action_model['action'] = 'audit_log'

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        name = 'Disable public access'
        description = 'Ensure that public access to account resources is disabled.'
        target = target_resource_model
        required_config = rule_required_config_model
        enforcement_actions = [enforcement_action_model]
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_type = 'user_defined'
        labels = ['SOC2', 'ITCS300']

        # Invoke method
        response = _service.update_rule(
            rule_id,
            if_match,
            name,
            description,
            target,
            required_config,
            enforcement_actions,
            account_id=account_id,
            rule_type=rule_type,
            labels=labels,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Disable public access'
        assert req_body['description'] == 'Ensure that public access to account resources is disabled.'
        assert req_body['target'] == target_resource_model
        assert req_body['required_config'] == rule_required_config_model
        assert req_body['enforcement_actions'] == [enforcement_action_model]
        assert req_body['account_id'] == '531fc3e28bfc43c5a2cea07786d93f5c'
        assert req_body['rule_type'] == 'user_defined'
        assert req_body['labels'] == ['SOC2', 'ITCS300']


    @responses.activate
    def test_update_rule_value_error(self):
        """
        test_update_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        mock_response = '{"account_id": "account_id", "name": "name", "description": "description", "rule_type": "user_defined", "target": {"service_name": "cloud-object-storage", "resource_kind": "bucket", "additional_target_attributes": [{"name": "name", "value": "value", "operator": "string_equals"}]}, "required_config": {"description": "description", "property": "public_access_enabled", "operator": "is_true", "value": "value"}, "enforcement_actions": [{"action": "audit_log"}], "labels": ["label"], "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "creation_date": "2020-01-10T05:23:19.000Z", "created_by": "created_by", "modification_date": "2020-01-10T05:23:19.000Z", "modified_by": "modified_by", "number_of_attachments": 3}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {}
        target_resource_additional_target_attributes_item_model['name'] = 'testString'
        target_resource_additional_target_attributes_item_model['value'] = 'testString'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a dict representation of a TargetResource model
        target_resource_model = {}
        target_resource_model['service_name'] = 'iam-groups'
        target_resource_model['resource_kind'] = 'service'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {}
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_false'
        rule_required_config_model['value'] = 'testString'

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {}
        enforcement_action_model['action'] = 'audit_log'

        # Set up parameter values
        rule_id = 'testString'
        if_match = 'testString'
        name = 'Disable public access'
        description = 'Ensure that public access to account resources is disabled.'
        target = target_resource_model
        required_config = rule_required_config_model
        enforcement_actions = [enforcement_action_model]
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_type = 'user_defined'
        labels = ['SOC2', 'ITCS300']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
            "if_match": if_match,
            "name": name,
            "description": description,
            "target": target,
            "required_config": required_config,
            "enforcement_actions": enforcement_actions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_rule(**req_copy)



class TestDeleteRule():
    """
    Test Class for delete_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_rule_all_params(self):
        """
        delete_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            rule_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_rule_required_params(self):
        """
        test_delete_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_rule_value_error(self):
        """
        test_delete_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_rule(**req_copy)



class TestCreateRuleAttachments():
    """
    Test Class for create_rule_attachments
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_rule_attachments_all_params(self):
        """
        create_rule_attachments()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments')
        mock_response = '{"attachments": [{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {}
        rule_scope_model['note'] = 'My enterprise'
        rule_scope_model['scope_id'] = '282cf433ac91493ba860480d92519990'
        rule_scope_model['scope_type'] = 'enterprise'

        # Construct a dict representation of a RuleAttachmentRequest model
        rule_attachment_request_model = {}
        rule_attachment_request_model['account_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_attachment_request_model['included_scope'] = rule_scope_model
        rule_attachment_request_model['excluded_scopes'] = [rule_scope_model]

        # Set up parameter values
        rule_id = 'testString'
        attachments = [rule_attachment_request_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_rule_attachments(
            rule_id,
            attachments,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [rule_attachment_request_model]


    @responses.activate
    def test_create_rule_attachments_required_params(self):
        """
        test_create_rule_attachments_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments')
        mock_response = '{"attachments": [{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {}
        rule_scope_model['note'] = 'My enterprise'
        rule_scope_model['scope_id'] = '282cf433ac91493ba860480d92519990'
        rule_scope_model['scope_type'] = 'enterprise'

        # Construct a dict representation of a RuleAttachmentRequest model
        rule_attachment_request_model = {}
        rule_attachment_request_model['account_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_attachment_request_model['included_scope'] = rule_scope_model
        rule_attachment_request_model['excluded_scopes'] = [rule_scope_model]

        # Set up parameter values
        rule_id = 'testString'
        attachments = [rule_attachment_request_model]

        # Invoke method
        response = _service.create_rule_attachments(
            rule_id,
            attachments,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [rule_attachment_request_model]


    @responses.activate
    def test_create_rule_attachments_value_error(self):
        """
        test_create_rule_attachments_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments')
        mock_response = '{"attachments": [{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {}
        rule_scope_model['note'] = 'My enterprise'
        rule_scope_model['scope_id'] = '282cf433ac91493ba860480d92519990'
        rule_scope_model['scope_type'] = 'enterprise'

        # Construct a dict representation of a RuleAttachmentRequest model
        rule_attachment_request_model = {}
        rule_attachment_request_model['account_id'] = '531fc3e28bfc43c5a2cea07786d93f5c'
        rule_attachment_request_model['included_scope'] = rule_scope_model
        rule_attachment_request_model['excluded_scopes'] = [rule_scope_model]

        # Set up parameter values
        rule_id = 'testString'
        attachments = [rule_attachment_request_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
            "attachments": attachments,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_rule_attachments(**req_copy)



class TestListRuleAttachments():
    """
    Test Class for list_rule_attachments
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_rule_attachments_all_params(self):
        """
        list_rule_attachments()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments')
        mock_response = '{"offset": 6, "limit": 1000, "total_count": 11, "first": {"href": "href"}, "last": {"href": "href"}, "attachments": [{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        transaction_id = 'testString'
        limit = 1000
        offset = 38

        # Invoke method
        response = _service.list_rule_attachments(
            rule_id,
            transaction_id=transaction_id,
            limit=limit,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string


    @responses.activate
    def test_list_rule_attachments_required_params(self):
        """
        test_list_rule_attachments_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments')
        mock_response = '{"offset": 6, "limit": 1000, "total_count": 11, "first": {"href": "href"}, "last": {"href": "href"}, "attachments": [{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = _service.list_rule_attachments(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_rule_attachments_value_error(self):
        """
        test_list_rule_attachments_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments')
        mock_response = '{"offset": 6, "limit": 1000, "total_count": 11, "first": {"href": "href"}, "last": {"href": "href"}, "attachments": [{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_rule_attachments(**req_copy)



class TestGetRuleAttachment():
    """
    Test Class for get_rule_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_rule_attachment_all_params(self):
        """
        get_rule_attachment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        mock_response = '{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_rule_attachment(
            rule_id,
            attachment_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_rule_attachment_required_params(self):
        """
        test_get_rule_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        mock_response = '{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'

        # Invoke method
        response = _service.get_rule_attachment(
            rule_id,
            attachment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_rule_attachment_value_error(self):
        """
        test_get_rule_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        mock_response = '{"attachment_id": "attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2", "rule_id": "rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
            "attachment_id": attachment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_rule_attachment(**req_copy)



class TestUpdateRuleAttachment():
    """
    Test Class for update_rule_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_rule_attachment_all_params(self):
        """
        update_rule_attachment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        mock_response = '{"attachment_id": "attachment_id", "template_id": "template_id", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {}
        rule_scope_model['note'] = 'My enterprise'
        rule_scope_model['scope_id'] = '282cf433ac91493ba860480d92519990'
        rule_scope_model['scope_type'] = 'enterprise'

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'
        if_match = 'testString'
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        included_scope = rule_scope_model
        excluded_scopes = [rule_scope_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_rule_attachment(
            rule_id,
            attachment_id,
            if_match,
            account_id,
            included_scope,
            excluded_scopes=excluded_scopes,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == '531fc3e28bfc43c5a2cea07786d93f5c'
        assert req_body['included_scope'] == rule_scope_model
        assert req_body['excluded_scopes'] == [rule_scope_model]


    @responses.activate
    def test_update_rule_attachment_required_params(self):
        """
        test_update_rule_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        mock_response = '{"attachment_id": "attachment_id", "template_id": "template_id", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {}
        rule_scope_model['note'] = 'My enterprise'
        rule_scope_model['scope_id'] = '282cf433ac91493ba860480d92519990'
        rule_scope_model['scope_type'] = 'enterprise'

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'
        if_match = 'testString'
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        included_scope = rule_scope_model
        excluded_scopes = [rule_scope_model]

        # Invoke method
        response = _service.update_rule_attachment(
            rule_id,
            attachment_id,
            if_match,
            account_id,
            included_scope,
            excluded_scopes=excluded_scopes,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['account_id'] == '531fc3e28bfc43c5a2cea07786d93f5c'
        assert req_body['included_scope'] == rule_scope_model
        assert req_body['excluded_scopes'] == [rule_scope_model]


    @responses.activate
    def test_update_rule_attachment_value_error(self):
        """
        test_update_rule_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        mock_response = '{"attachment_id": "attachment_id", "template_id": "template_id", "account_id": "account_id", "included_scope": {"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}, "excluded_scopes": [{"note": "note", "scope_id": "scope_id", "scope_type": "enterprise"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {}
        rule_scope_model['note'] = 'My enterprise'
        rule_scope_model['scope_id'] = '282cf433ac91493ba860480d92519990'
        rule_scope_model['scope_type'] = 'enterprise'

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'
        if_match = 'testString'
        account_id = '531fc3e28bfc43c5a2cea07786d93f5c'
        included_scope = rule_scope_model
        excluded_scopes = [rule_scope_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
            "attachment_id": attachment_id,
            "if_match": if_match,
            "account_id": account_id,
            "included_scope": included_scope,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_rule_attachment(**req_copy)



class TestDeleteRuleAttachment():
    """
    Test Class for delete_rule_attachment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_rule_attachment_all_params(self):
        """
        delete_rule_attachment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_rule_attachment(
            rule_id,
            attachment_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_rule_attachment_required_params(self):
        """
        test_delete_rule_attachment_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'

        # Invoke method
        response = _service.delete_rule_attachment(
            rule_id,
            attachment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_rule_attachment_value_error(self):
        """
        test_delete_rule_attachment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/config/v1/rules/testString/attachments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        rule_id = 'testString'
        attachment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
            "attachment_id": attachment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_rule_attachment(**req_copy)



# endregion
##############################################################################
# End of Service: Rules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestCreateRuleAttachmentsResponse():
    """
    Test Class for CreateRuleAttachmentsResponse
    """

    def test_create_rule_attachments_response_serialization(self):
        """
        Test serialization/deserialization for CreateRuleAttachmentsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_scope_model = {} # RuleScope
        rule_scope_model['note'] = 'testString'
        rule_scope_model['scope_id'] = 'testString'
        rule_scope_model['scope_type'] = 'enterprise'

        rule_attachment_model = {} # RuleAttachment
        rule_attachment_model['attachment_id'] = 'attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2'
        rule_attachment_model['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_attachment_model['account_id'] = 'testString'
        rule_attachment_model['included_scope'] = rule_scope_model
        rule_attachment_model['excluded_scopes'] = [rule_scope_model]

        # Construct a json representation of a CreateRuleAttachmentsResponse model
        create_rule_attachments_response_model_json = {}
        create_rule_attachments_response_model_json['attachments'] = [rule_attachment_model]

        # Construct a model instance of CreateRuleAttachmentsResponse by calling from_dict on the json representation
        create_rule_attachments_response_model = CreateRuleAttachmentsResponse.from_dict(create_rule_attachments_response_model_json)
        assert create_rule_attachments_response_model != False

        # Construct a model instance of CreateRuleAttachmentsResponse by calling from_dict on the json representation
        create_rule_attachments_response_model_dict = CreateRuleAttachmentsResponse.from_dict(create_rule_attachments_response_model_json).__dict__
        create_rule_attachments_response_model2 = CreateRuleAttachmentsResponse(**create_rule_attachments_response_model_dict)

        # Verify the model instances are equivalent
        assert create_rule_attachments_response_model == create_rule_attachments_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_rule_attachments_response_model_json2 = create_rule_attachments_response_model.to_dict()
        assert create_rule_attachments_response_model_json2 == create_rule_attachments_response_model_json

class TestCreateRuleRequest():
    """
    Test Class for CreateRuleRequest
    """

    def test_create_rule_request_serialization(self):
        """
        Test serialization/deserialization for CreateRuleRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        target_resource_model = {} # TargetResource
        target_resource_model['service_name'] = 'cloud-object-storage'
        target_resource_model['resource_kind'] = 'bucket'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        rule_required_config_model = {} # RuleRequiredConfigSingleProperty
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        enforcement_action_model = {} # EnforcementAction
        enforcement_action_model['action'] = 'disallow'

        rule_request_model = {} # RuleRequest
        rule_request_model['account_id'] = 'testString'
        rule_request_model['name'] = 'testString'
        rule_request_model['description'] = 'testString'
        rule_request_model['rule_type'] = 'user_defined'
        rule_request_model['target'] = target_resource_model
        rule_request_model['required_config'] = rule_required_config_model
        rule_request_model['enforcement_actions'] = [enforcement_action_model]
        rule_request_model['labels'] = ['SOC2', 'ITCS300']

        # Construct a json representation of a CreateRuleRequest model
        create_rule_request_model_json = {}
        create_rule_request_model_json['request_id'] = '3cebc877-58e7-44a5-a292-32114fa73558'
        create_rule_request_model_json['rule'] = rule_request_model

        # Construct a model instance of CreateRuleRequest by calling from_dict on the json representation
        create_rule_request_model = CreateRuleRequest.from_dict(create_rule_request_model_json)
        assert create_rule_request_model != False

        # Construct a model instance of CreateRuleRequest by calling from_dict on the json representation
        create_rule_request_model_dict = CreateRuleRequest.from_dict(create_rule_request_model_json).__dict__
        create_rule_request_model2 = CreateRuleRequest(**create_rule_request_model_dict)

        # Verify the model instances are equivalent
        assert create_rule_request_model == create_rule_request_model2

        # Convert model instance back to dict and verify no loss of data
        create_rule_request_model_json2 = create_rule_request_model.to_dict()
        assert create_rule_request_model_json2 == create_rule_request_model_json

class TestCreateRuleResponse():
    """
    Test Class for CreateRuleResponse
    """

    def test_create_rule_response_serialization(self):
        """
        Test serialization/deserialization for CreateRuleResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        target_resource_model = {} # TargetResource
        target_resource_model['service_name'] = 'cloud-object-storage'
        target_resource_model['resource_kind'] = 'bucket'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        rule_required_config_model = {} # RuleRequiredConfigSingleProperty
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        enforcement_action_model = {} # EnforcementAction
        enforcement_action_model['action'] = 'disallow'

        rule_model = {} # Rule
        rule_model['account_id'] = 'testString'
        rule_model['name'] = 'testString'
        rule_model['description'] = 'testString'
        rule_model['rule_type'] = 'user_defined'
        rule_model['target'] = target_resource_model
        rule_model['required_config'] = rule_required_config_model
        rule_model['enforcement_actions'] = [enforcement_action_model]
        rule_model['labels'] = ['SOC2', 'ITCS300']
        rule_model['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_model['creation_date'] = "2020-01-10T05:23:19Z"
        rule_model['created_by'] = 'testString'
        rule_model['modification_date'] = "2020-01-10T05:23:19Z"
        rule_model['modified_by'] = 'testString'
        rule_model['number_of_attachments'] = 3

        rule_response_error_model = {} # RuleResponseError
        rule_response_error_model['code'] = 'bad_request'
        rule_response_error_model['message'] = 'The rule is missing an account ID'

        # Construct a json representation of a CreateRuleResponse model
        create_rule_response_model_json = {}
        create_rule_response_model_json['request_id'] = '3cebc877-58e7-44a5-a292-32114fa73558'
        create_rule_response_model_json['status_code'] = 201
        create_rule_response_model_json['rule'] = rule_model
        create_rule_response_model_json['errors'] = [rule_response_error_model]
        create_rule_response_model_json['trace'] = '861263b4-cee3-4514-8d8c-05d17308e6eb'

        # Construct a model instance of CreateRuleResponse by calling from_dict on the json representation
        create_rule_response_model = CreateRuleResponse.from_dict(create_rule_response_model_json)
        assert create_rule_response_model != False

        # Construct a model instance of CreateRuleResponse by calling from_dict on the json representation
        create_rule_response_model_dict = CreateRuleResponse.from_dict(create_rule_response_model_json).__dict__
        create_rule_response_model2 = CreateRuleResponse(**create_rule_response_model_dict)

        # Verify the model instances are equivalent
        assert create_rule_response_model == create_rule_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_rule_response_model_json2 = create_rule_response_model.to_dict()
        assert create_rule_response_model_json2 == create_rule_response_model_json

class TestCreateRulesResponse():
    """
    Test Class for CreateRulesResponse
    """

    def test_create_rules_response_serialization(self):
        """
        Test serialization/deserialization for CreateRulesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        target_resource_model = {} # TargetResource
        target_resource_model['service_name'] = 'cloud-object-storage'
        target_resource_model['resource_kind'] = 'bucket'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        rule_required_config_model = {} # RuleRequiredConfigSingleProperty
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        enforcement_action_model = {} # EnforcementAction
        enforcement_action_model['action'] = 'disallow'

        rule_model = {} # Rule
        rule_model['account_id'] = 'testString'
        rule_model['name'] = 'testString'
        rule_model['description'] = 'testString'
        rule_model['rule_type'] = 'user_defined'
        rule_model['target'] = target_resource_model
        rule_model['required_config'] = rule_required_config_model
        rule_model['enforcement_actions'] = [enforcement_action_model]
        rule_model['labels'] = ['SOC2', 'ITCS300']
        rule_model['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_model['creation_date'] = "2020-01-10T05:23:19Z"
        rule_model['created_by'] = 'testString'
        rule_model['modification_date'] = "2020-01-10T05:23:19Z"
        rule_model['modified_by'] = 'testString'
        rule_model['number_of_attachments'] = 3

        rule_response_error_model = {} # RuleResponseError
        rule_response_error_model['code'] = 'bad_request'
        rule_response_error_model['message'] = 'The rule is missing an account ID'

        create_rule_response_model = {} # CreateRuleResponse
        create_rule_response_model['request_id'] = '3cebc877-58e7-44a5-a292-32114fa73558'
        create_rule_response_model['status_code'] = 201
        create_rule_response_model['rule'] = rule_model
        create_rule_response_model['errors'] = [rule_response_error_model]
        create_rule_response_model['trace'] = '861263b4-cee3-4514-8d8c-05d17308e6eb'

        # Construct a json representation of a CreateRulesResponse model
        create_rules_response_model_json = {}
        create_rules_response_model_json['rules'] = [create_rule_response_model]

        # Construct a model instance of CreateRulesResponse by calling from_dict on the json representation
        create_rules_response_model = CreateRulesResponse.from_dict(create_rules_response_model_json)
        assert create_rules_response_model != False

        # Construct a model instance of CreateRulesResponse by calling from_dict on the json representation
        create_rules_response_model_dict = CreateRulesResponse.from_dict(create_rules_response_model_json).__dict__
        create_rules_response_model2 = CreateRulesResponse(**create_rules_response_model_dict)

        # Verify the model instances are equivalent
        assert create_rules_response_model == create_rules_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_rules_response_model_json2 = create_rules_response_model.to_dict()
        assert create_rules_response_model_json2 == create_rules_response_model_json

class TestEnforcementAction():
    """
    Test Class for EnforcementAction
    """

    def test_enforcement_action_serialization(self):
        """
        Test serialization/deserialization for EnforcementAction
        """

        # Construct a json representation of a EnforcementAction model
        enforcement_action_model_json = {}
        enforcement_action_model_json['action'] = 'audit_log'

        # Construct a model instance of EnforcementAction by calling from_dict on the json representation
        enforcement_action_model = EnforcementAction.from_dict(enforcement_action_model_json)
        assert enforcement_action_model != False

        # Construct a model instance of EnforcementAction by calling from_dict on the json representation
        enforcement_action_model_dict = EnforcementAction.from_dict(enforcement_action_model_json).__dict__
        enforcement_action_model2 = EnforcementAction(**enforcement_action_model_dict)

        # Verify the model instances are equivalent
        assert enforcement_action_model == enforcement_action_model2

        # Convert model instance back to dict and verify no loss of data
        enforcement_action_model_json2 = enforcement_action_model.to_dict()
        assert enforcement_action_model_json2 == enforcement_action_model_json

class TestLink():
    """
    Test Class for Link
    """

    def test_link_serialization(self):
        """
        Test serialization/deserialization for Link
        """

        # Construct a json representation of a Link model
        link_model_json = {}
        link_model_json['href'] = 'testString'

        # Construct a model instance of Link by calling from_dict on the json representation
        link_model = Link.from_dict(link_model_json)
        assert link_model != False

        # Construct a model instance of Link by calling from_dict on the json representation
        link_model_dict = Link.from_dict(link_model_json).__dict__
        link_model2 = Link(**link_model_dict)

        # Verify the model instances are equivalent
        assert link_model == link_model2

        # Convert model instance back to dict and verify no loss of data
        link_model_json2 = link_model.to_dict()
        assert link_model_json2 == link_model_json

class TestRule():
    """
    Test Class for Rule
    """

    def test_rule_serialization(self):
        """
        Test serialization/deserialization for Rule
        """

        # Construct dict forms of any model objects needed in order to build this model.

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        target_resource_model = {} # TargetResource
        target_resource_model['service_name'] = 'cloud-object-storage'
        target_resource_model['resource_kind'] = 'bucket'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        rule_required_config_model = {} # RuleRequiredConfigSingleProperty
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        enforcement_action_model = {} # EnforcementAction
        enforcement_action_model['action'] = 'disallow'

        # Construct a json representation of a Rule model
        rule_model_json = {}
        rule_model_json['account_id'] = 'testString'
        rule_model_json['name'] = 'testString'
        rule_model_json['description'] = 'testString'
        rule_model_json['rule_type'] = 'user_defined'
        rule_model_json['target'] = target_resource_model
        rule_model_json['required_config'] = rule_required_config_model
        rule_model_json['enforcement_actions'] = [enforcement_action_model]
        rule_model_json['labels'] = ['SOC2', 'ITCS300']
        rule_model_json['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_model_json['creation_date'] = "2020-01-10T05:23:19Z"
        rule_model_json['created_by'] = 'testString'
        rule_model_json['modification_date'] = "2020-01-10T05:23:19Z"
        rule_model_json['modified_by'] = 'testString'
        rule_model_json['number_of_attachments'] = 3

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model = Rule.from_dict(rule_model_json)
        assert rule_model != False

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model_dict = Rule.from_dict(rule_model_json).__dict__
        rule_model2 = Rule(**rule_model_dict)

        # Verify the model instances are equivalent
        assert rule_model == rule_model2

        # Convert model instance back to dict and verify no loss of data
        rule_model_json2 = rule_model.to_dict()
        assert rule_model_json2 == rule_model_json

class TestRuleAttachment():
    """
    Test Class for RuleAttachment
    """

    def test_rule_attachment_serialization(self):
        """
        Test serialization/deserialization for RuleAttachment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_scope_model = {} # RuleScope
        rule_scope_model['note'] = 'testString'
        rule_scope_model['scope_id'] = 'testString'
        rule_scope_model['scope_type'] = 'enterprise'

        # Construct a json representation of a RuleAttachment model
        rule_attachment_model_json = {}
        rule_attachment_model_json['attachment_id'] = 'attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2'
        rule_attachment_model_json['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_attachment_model_json['account_id'] = 'testString'
        rule_attachment_model_json['included_scope'] = rule_scope_model
        rule_attachment_model_json['excluded_scopes'] = [rule_scope_model]

        # Construct a model instance of RuleAttachment by calling from_dict on the json representation
        rule_attachment_model = RuleAttachment.from_dict(rule_attachment_model_json)
        assert rule_attachment_model != False

        # Construct a model instance of RuleAttachment by calling from_dict on the json representation
        rule_attachment_model_dict = RuleAttachment.from_dict(rule_attachment_model_json).__dict__
        rule_attachment_model2 = RuleAttachment(**rule_attachment_model_dict)

        # Verify the model instances are equivalent
        assert rule_attachment_model == rule_attachment_model2

        # Convert model instance back to dict and verify no loss of data
        rule_attachment_model_json2 = rule_attachment_model.to_dict()
        assert rule_attachment_model_json2 == rule_attachment_model_json

class TestRuleAttachmentList():
    """
    Test Class for RuleAttachmentList
    """

    def test_rule_attachment_list_serialization(self):
        """
        Test serialization/deserialization for RuleAttachmentList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        link_model = {} # Link
        link_model['href'] = 'testString'

        rule_scope_model = {} # RuleScope
        rule_scope_model['note'] = 'testString'
        rule_scope_model['scope_id'] = 'testString'
        rule_scope_model['scope_type'] = 'enterprise'

        rule_attachment_model = {} # RuleAttachment
        rule_attachment_model['attachment_id'] = 'attachment-fc7b9a77-1c85-406c-b346-f3f5bb9aa7e2'
        rule_attachment_model['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_attachment_model['account_id'] = 'testString'
        rule_attachment_model['included_scope'] = rule_scope_model
        rule_attachment_model['excluded_scopes'] = [rule_scope_model]

        # Construct a json representation of a RuleAttachmentList model
        rule_attachment_list_model_json = {}
        rule_attachment_list_model_json['offset'] = 38
        rule_attachment_list_model_json['limit'] = 1000
        rule_attachment_list_model_json['total_count'] = 38
        rule_attachment_list_model_json['first'] = link_model
        rule_attachment_list_model_json['last'] = link_model
        rule_attachment_list_model_json['attachments'] = [rule_attachment_model]

        # Construct a model instance of RuleAttachmentList by calling from_dict on the json representation
        rule_attachment_list_model = RuleAttachmentList.from_dict(rule_attachment_list_model_json)
        assert rule_attachment_list_model != False

        # Construct a model instance of RuleAttachmentList by calling from_dict on the json representation
        rule_attachment_list_model_dict = RuleAttachmentList.from_dict(rule_attachment_list_model_json).__dict__
        rule_attachment_list_model2 = RuleAttachmentList(**rule_attachment_list_model_dict)

        # Verify the model instances are equivalent
        assert rule_attachment_list_model == rule_attachment_list_model2

        # Convert model instance back to dict and verify no loss of data
        rule_attachment_list_model_json2 = rule_attachment_list_model.to_dict()
        assert rule_attachment_list_model_json2 == rule_attachment_list_model_json

class TestRuleAttachmentRequest():
    """
    Test Class for RuleAttachmentRequest
    """

    def test_rule_attachment_request_serialization(self):
        """
        Test serialization/deserialization for RuleAttachmentRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_scope_model = {} # RuleScope
        rule_scope_model['note'] = 'testString'
        rule_scope_model['scope_id'] = 'testString'
        rule_scope_model['scope_type'] = 'enterprise'

        # Construct a json representation of a RuleAttachmentRequest model
        rule_attachment_request_model_json = {}
        rule_attachment_request_model_json['account_id'] = 'testString'
        rule_attachment_request_model_json['included_scope'] = rule_scope_model
        rule_attachment_request_model_json['excluded_scopes'] = [rule_scope_model]

        # Construct a model instance of RuleAttachmentRequest by calling from_dict on the json representation
        rule_attachment_request_model = RuleAttachmentRequest.from_dict(rule_attachment_request_model_json)
        assert rule_attachment_request_model != False

        # Construct a model instance of RuleAttachmentRequest by calling from_dict on the json representation
        rule_attachment_request_model_dict = RuleAttachmentRequest.from_dict(rule_attachment_request_model_json).__dict__
        rule_attachment_request_model2 = RuleAttachmentRequest(**rule_attachment_request_model_dict)

        # Verify the model instances are equivalent
        assert rule_attachment_request_model == rule_attachment_request_model2

        # Convert model instance back to dict and verify no loss of data
        rule_attachment_request_model_json2 = rule_attachment_request_model.to_dict()
        assert rule_attachment_request_model_json2 == rule_attachment_request_model_json

class TestRuleList():
    """
    Test Class for RuleList
    """

    def test_rule_list_serialization(self):
        """
        Test serialization/deserialization for RuleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        link_model = {} # Link
        link_model['href'] = 'testString'

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        target_resource_model = {} # TargetResource
        target_resource_model['service_name'] = 'cloud-object-storage'
        target_resource_model['resource_kind'] = 'bucket'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        rule_required_config_model = {} # RuleRequiredConfigSingleProperty
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        enforcement_action_model = {} # EnforcementAction
        enforcement_action_model['action'] = 'disallow'

        rule_model = {} # Rule
        rule_model['account_id'] = 'testString'
        rule_model['name'] = 'testString'
        rule_model['description'] = 'testString'
        rule_model['rule_type'] = 'user_defined'
        rule_model['target'] = target_resource_model
        rule_model['required_config'] = rule_required_config_model
        rule_model['enforcement_actions'] = [enforcement_action_model]
        rule_model['labels'] = ['SOC2', 'ITCS300']
        rule_model['rule_id'] = 'rule-81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        rule_model['creation_date'] = "2020-01-10T05:23:19Z"
        rule_model['created_by'] = 'testString'
        rule_model['modification_date'] = "2020-01-10T05:23:19Z"
        rule_model['modified_by'] = 'testString'
        rule_model['number_of_attachments'] = 3

        # Construct a json representation of a RuleList model
        rule_list_model_json = {}
        rule_list_model_json['offset'] = 38
        rule_list_model_json['limit'] = 1000
        rule_list_model_json['total_count'] = 38
        rule_list_model_json['first'] = link_model
        rule_list_model_json['last'] = link_model
        rule_list_model_json['rules'] = [rule_model]

        # Construct a model instance of RuleList by calling from_dict on the json representation
        rule_list_model = RuleList.from_dict(rule_list_model_json)
        assert rule_list_model != False

        # Construct a model instance of RuleList by calling from_dict on the json representation
        rule_list_model_dict = RuleList.from_dict(rule_list_model_json).__dict__
        rule_list_model2 = RuleList(**rule_list_model_dict)

        # Verify the model instances are equivalent
        assert rule_list_model == rule_list_model2

        # Convert model instance back to dict and verify no loss of data
        rule_list_model_json2 = rule_list_model.to_dict()
        assert rule_list_model_json2 == rule_list_model_json

class TestRuleRequest():
    """
    Test Class for RuleRequest
    """

    def test_rule_request_serialization(self):
        """
        Test serialization/deserialization for RuleRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        target_resource_model = {} # TargetResource
        target_resource_model['service_name'] = 'cloud-object-storage'
        target_resource_model['resource_kind'] = 'bucket'
        target_resource_model['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        rule_required_config_model = {} # RuleRequiredConfigSingleProperty
        rule_required_config_model['description'] = 'testString'
        rule_required_config_model['property'] = 'public_access_enabled'
        rule_required_config_model['operator'] = 'is_true'
        rule_required_config_model['value'] = 'testString'

        enforcement_action_model = {} # EnforcementAction
        enforcement_action_model['action'] = 'disallow'

        # Construct a json representation of a RuleRequest model
        rule_request_model_json = {}
        rule_request_model_json['account_id'] = 'testString'
        rule_request_model_json['name'] = 'testString'
        rule_request_model_json['description'] = 'testString'
        rule_request_model_json['rule_type'] = 'user_defined'
        rule_request_model_json['target'] = target_resource_model
        rule_request_model_json['required_config'] = rule_required_config_model
        rule_request_model_json['enforcement_actions'] = [enforcement_action_model]
        rule_request_model_json['labels'] = ['SOC2', 'ITCS300']

        # Construct a model instance of RuleRequest by calling from_dict on the json representation
        rule_request_model = RuleRequest.from_dict(rule_request_model_json)
        assert rule_request_model != False

        # Construct a model instance of RuleRequest by calling from_dict on the json representation
        rule_request_model_dict = RuleRequest.from_dict(rule_request_model_json).__dict__
        rule_request_model2 = RuleRequest(**rule_request_model_dict)

        # Verify the model instances are equivalent
        assert rule_request_model == rule_request_model2

        # Convert model instance back to dict and verify no loss of data
        rule_request_model_json2 = rule_request_model.to_dict()
        assert rule_request_model_json2 == rule_request_model_json

class TestRuleResponseError():
    """
    Test Class for RuleResponseError
    """

    def test_rule_response_error_serialization(self):
        """
        Test serialization/deserialization for RuleResponseError
        """

        # Construct a json representation of a RuleResponseError model
        rule_response_error_model_json = {}
        rule_response_error_model_json['code'] = 'bad_request'
        rule_response_error_model_json['message'] = 'The rule is missing an account ID'

        # Construct a model instance of RuleResponseError by calling from_dict on the json representation
        rule_response_error_model = RuleResponseError.from_dict(rule_response_error_model_json)
        assert rule_response_error_model != False

        # Construct a model instance of RuleResponseError by calling from_dict on the json representation
        rule_response_error_model_dict = RuleResponseError.from_dict(rule_response_error_model_json).__dict__
        rule_response_error_model2 = RuleResponseError(**rule_response_error_model_dict)

        # Verify the model instances are equivalent
        assert rule_response_error_model == rule_response_error_model2

        # Convert model instance back to dict and verify no loss of data
        rule_response_error_model_json2 = rule_response_error_model.to_dict()
        assert rule_response_error_model_json2 == rule_response_error_model_json

class TestRuleScope():
    """
    Test Class for RuleScope
    """

    def test_rule_scope_serialization(self):
        """
        Test serialization/deserialization for RuleScope
        """

        # Construct a json representation of a RuleScope model
        rule_scope_model_json = {}
        rule_scope_model_json['note'] = 'testString'
        rule_scope_model_json['scope_id'] = 'testString'
        rule_scope_model_json['scope_type'] = 'enterprise'

        # Construct a model instance of RuleScope by calling from_dict on the json representation
        rule_scope_model = RuleScope.from_dict(rule_scope_model_json)
        assert rule_scope_model != False

        # Construct a model instance of RuleScope by calling from_dict on the json representation
        rule_scope_model_dict = RuleScope.from_dict(rule_scope_model_json).__dict__
        rule_scope_model2 = RuleScope(**rule_scope_model_dict)

        # Verify the model instances are equivalent
        assert rule_scope_model == rule_scope_model2

        # Convert model instance back to dict and verify no loss of data
        rule_scope_model_json2 = rule_scope_model.to_dict()
        assert rule_scope_model_json2 == rule_scope_model_json

class TestRuleSingleProperty():
    """
    Test Class for RuleSingleProperty
    """

    def test_rule_single_property_serialization(self):
        """
        Test serialization/deserialization for RuleSingleProperty
        """

        # Construct a json representation of a RuleSingleProperty model
        rule_single_property_model_json = {}
        rule_single_property_model_json['description'] = 'testString'
        rule_single_property_model_json['property'] = 'public_access_enabled'
        rule_single_property_model_json['operator'] = 'is_true'
        rule_single_property_model_json['value'] = 'testString'

        # Construct a model instance of RuleSingleProperty by calling from_dict on the json representation
        rule_single_property_model = RuleSingleProperty.from_dict(rule_single_property_model_json)
        assert rule_single_property_model != False

        # Construct a model instance of RuleSingleProperty by calling from_dict on the json representation
        rule_single_property_model_dict = RuleSingleProperty.from_dict(rule_single_property_model_json).__dict__
        rule_single_property_model2 = RuleSingleProperty(**rule_single_property_model_dict)

        # Verify the model instances are equivalent
        assert rule_single_property_model == rule_single_property_model2

        # Convert model instance back to dict and verify no loss of data
        rule_single_property_model_json2 = rule_single_property_model.to_dict()
        assert rule_single_property_model_json2 == rule_single_property_model_json

class TestTargetResource():
    """
    Test Class for TargetResource
    """

    def test_target_resource_serialization(self):
        """
        Test serialization/deserialization for TargetResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        target_resource_additional_target_attributes_item_model = {} # TargetResourceAdditionalTargetAttributesItem
        target_resource_additional_target_attributes_item_model['name'] = 'resource_id'
        target_resource_additional_target_attributes_item_model['value'] = '81f3db5e-f9db-4c46-9de3-a4a76e66adbf'
        target_resource_additional_target_attributes_item_model['operator'] = 'string_equals'

        # Construct a json representation of a TargetResource model
        target_resource_model_json = {}
        target_resource_model_json['service_name'] = 'cloud-object-storage'
        target_resource_model_json['resource_kind'] = 'bucket'
        target_resource_model_json['additional_target_attributes'] = [target_resource_additional_target_attributes_item_model]

        # Construct a model instance of TargetResource by calling from_dict on the json representation
        target_resource_model = TargetResource.from_dict(target_resource_model_json)
        assert target_resource_model != False

        # Construct a model instance of TargetResource by calling from_dict on the json representation
        target_resource_model_dict = TargetResource.from_dict(target_resource_model_json).__dict__
        target_resource_model2 = TargetResource(**target_resource_model_dict)

        # Verify the model instances are equivalent
        assert target_resource_model == target_resource_model2

        # Convert model instance back to dict and verify no loss of data
        target_resource_model_json2 = target_resource_model.to_dict()
        assert target_resource_model_json2 == target_resource_model_json

class TestTargetResourceAdditionalTargetAttributesItem():
    """
    Test Class for TargetResourceAdditionalTargetAttributesItem
    """

    def test_target_resource_additional_target_attributes_item_serialization(self):
        """
        Test serialization/deserialization for TargetResourceAdditionalTargetAttributesItem
        """

        # Construct a json representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model_json = {}
        target_resource_additional_target_attributes_item_model_json['name'] = 'testString'
        target_resource_additional_target_attributes_item_model_json['value'] = 'testString'
        target_resource_additional_target_attributes_item_model_json['operator'] = 'string_equals'

        # Construct a model instance of TargetResourceAdditionalTargetAttributesItem by calling from_dict on the json representation
        target_resource_additional_target_attributes_item_model = TargetResourceAdditionalTargetAttributesItem.from_dict(target_resource_additional_target_attributes_item_model_json)
        assert target_resource_additional_target_attributes_item_model != False

        # Construct a model instance of TargetResourceAdditionalTargetAttributesItem by calling from_dict on the json representation
        target_resource_additional_target_attributes_item_model_dict = TargetResourceAdditionalTargetAttributesItem.from_dict(target_resource_additional_target_attributes_item_model_json).__dict__
        target_resource_additional_target_attributes_item_model2 = TargetResourceAdditionalTargetAttributesItem(**target_resource_additional_target_attributes_item_model_dict)

        # Verify the model instances are equivalent
        assert target_resource_additional_target_attributes_item_model == target_resource_additional_target_attributes_item_model2

        # Convert model instance back to dict and verify no loss of data
        target_resource_additional_target_attributes_item_model_json2 = target_resource_additional_target_attributes_item_model.to_dict()
        assert target_resource_additional_target_attributes_item_model_json2 == target_resource_additional_target_attributes_item_model_json

class TestTemplateAttachment():
    """
    Test Class for TemplateAttachment
    """

    def test_template_attachment_serialization(self):
        """
        Test serialization/deserialization for TemplateAttachment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_scope_model = {} # TemplateScope
        template_scope_model['note'] = 'testString'
        template_scope_model['scope_id'] = 'testString'
        template_scope_model['scope_type'] = 'enterprise'

        # Construct a json representation of a TemplateAttachment model
        template_attachment_model_json = {}
        template_attachment_model_json['attachment_id'] = 'testString'
        template_attachment_model_json['template_id'] = 'testString'
        template_attachment_model_json['account_id'] = 'testString'
        template_attachment_model_json['included_scope'] = template_scope_model
        template_attachment_model_json['excluded_scopes'] = [template_scope_model]

        # Construct a model instance of TemplateAttachment by calling from_dict on the json representation
        template_attachment_model = TemplateAttachment.from_dict(template_attachment_model_json)
        assert template_attachment_model != False

        # Construct a model instance of TemplateAttachment by calling from_dict on the json representation
        template_attachment_model_dict = TemplateAttachment.from_dict(template_attachment_model_json).__dict__
        template_attachment_model2 = TemplateAttachment(**template_attachment_model_dict)

        # Verify the model instances are equivalent
        assert template_attachment_model == template_attachment_model2

        # Convert model instance back to dict and verify no loss of data
        template_attachment_model_json2 = template_attachment_model.to_dict()
        assert template_attachment_model_json2 == template_attachment_model_json

class TestTemplateScope():
    """
    Test Class for TemplateScope
    """

    def test_template_scope_serialization(self):
        """
        Test serialization/deserialization for TemplateScope
        """

        # Construct a json representation of a TemplateScope model
        template_scope_model_json = {}
        template_scope_model_json['note'] = 'testString'
        template_scope_model_json['scope_id'] = 'testString'
        template_scope_model_json['scope_type'] = 'enterprise'

        # Construct a model instance of TemplateScope by calling from_dict on the json representation
        template_scope_model = TemplateScope.from_dict(template_scope_model_json)
        assert template_scope_model != False

        # Construct a model instance of TemplateScope by calling from_dict on the json representation
        template_scope_model_dict = TemplateScope.from_dict(template_scope_model_json).__dict__
        template_scope_model2 = TemplateScope(**template_scope_model_dict)

        # Verify the model instances are equivalent
        assert template_scope_model == template_scope_model2

        # Convert model instance back to dict and verify no loss of data
        template_scope_model_json2 = template_scope_model.to_dict()
        assert template_scope_model_json2 == template_scope_model_json

class TestRuleConditionAndLvl2():
    """
    Test Class for RuleConditionAndLvl2
    """

    def test_rule_condition_and_lvl2_serialization(self):
        """
        Test serialization/deserialization for RuleConditionAndLvl2
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_single_property_model = {} # RuleSingleProperty
        rule_single_property_model['description'] = 'testString'
        rule_single_property_model['property'] = 'public_access_enabled'
        rule_single_property_model['operator'] = 'is_true'
        rule_single_property_model['value'] = 'testString'

        # Construct a json representation of a RuleConditionAndLvl2 model
        rule_condition_and_lvl2_model_json = {}
        rule_condition_and_lvl2_model_json['description'] = 'testString'
        rule_condition_and_lvl2_model_json['and'] = [rule_single_property_model]

        # Construct a model instance of RuleConditionAndLvl2 by calling from_dict on the json representation
        rule_condition_and_lvl2_model = RuleConditionAndLvl2.from_dict(rule_condition_and_lvl2_model_json)
        assert rule_condition_and_lvl2_model != False

        # Construct a model instance of RuleConditionAndLvl2 by calling from_dict on the json representation
        rule_condition_and_lvl2_model_dict = RuleConditionAndLvl2.from_dict(rule_condition_and_lvl2_model_json).__dict__
        rule_condition_and_lvl2_model2 = RuleConditionAndLvl2(**rule_condition_and_lvl2_model_dict)

        # Verify the model instances are equivalent
        assert rule_condition_and_lvl2_model == rule_condition_and_lvl2_model2

        # Convert model instance back to dict and verify no loss of data
        rule_condition_and_lvl2_model_json2 = rule_condition_and_lvl2_model.to_dict()
        assert rule_condition_and_lvl2_model_json2 == rule_condition_and_lvl2_model_json

class TestRuleConditionOrLvl2():
    """
    Test Class for RuleConditionOrLvl2
    """

    def test_rule_condition_or_lvl2_serialization(self):
        """
        Test serialization/deserialization for RuleConditionOrLvl2
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_single_property_model = {} # RuleSingleProperty
        rule_single_property_model['description'] = 'testString'
        rule_single_property_model['property'] = 'public_access_enabled'
        rule_single_property_model['operator'] = 'is_true'
        rule_single_property_model['value'] = 'testString'

        # Construct a json representation of a RuleConditionOrLvl2 model
        rule_condition_or_lvl2_model_json = {}
        rule_condition_or_lvl2_model_json['description'] = 'testString'
        rule_condition_or_lvl2_model_json['or'] = [rule_single_property_model]

        # Construct a model instance of RuleConditionOrLvl2 by calling from_dict on the json representation
        rule_condition_or_lvl2_model = RuleConditionOrLvl2.from_dict(rule_condition_or_lvl2_model_json)
        assert rule_condition_or_lvl2_model != False

        # Construct a model instance of RuleConditionOrLvl2 by calling from_dict on the json representation
        rule_condition_or_lvl2_model_dict = RuleConditionOrLvl2.from_dict(rule_condition_or_lvl2_model_json).__dict__
        rule_condition_or_lvl2_model2 = RuleConditionOrLvl2(**rule_condition_or_lvl2_model_dict)

        # Verify the model instances are equivalent
        assert rule_condition_or_lvl2_model == rule_condition_or_lvl2_model2

        # Convert model instance back to dict and verify no loss of data
        rule_condition_or_lvl2_model_json2 = rule_condition_or_lvl2_model.to_dict()
        assert rule_condition_or_lvl2_model_json2 == rule_condition_or_lvl2_model_json

class TestRuleConditionSingleProperty():
    """
    Test Class for RuleConditionSingleProperty
    """

    def test_rule_condition_single_property_serialization(self):
        """
        Test serialization/deserialization for RuleConditionSingleProperty
        """

        # Construct a json representation of a RuleConditionSingleProperty model
        rule_condition_single_property_model_json = {}
        rule_condition_single_property_model_json['description'] = 'testString'
        rule_condition_single_property_model_json['property'] = 'public_access_enabled'
        rule_condition_single_property_model_json['operator'] = 'is_true'
        rule_condition_single_property_model_json['value'] = 'testString'

        # Construct a model instance of RuleConditionSingleProperty by calling from_dict on the json representation
        rule_condition_single_property_model = RuleConditionSingleProperty.from_dict(rule_condition_single_property_model_json)
        assert rule_condition_single_property_model != False

        # Construct a model instance of RuleConditionSingleProperty by calling from_dict on the json representation
        rule_condition_single_property_model_dict = RuleConditionSingleProperty.from_dict(rule_condition_single_property_model_json).__dict__
        rule_condition_single_property_model2 = RuleConditionSingleProperty(**rule_condition_single_property_model_dict)

        # Verify the model instances are equivalent
        assert rule_condition_single_property_model == rule_condition_single_property_model2

        # Convert model instance back to dict and verify no loss of data
        rule_condition_single_property_model_json2 = rule_condition_single_property_model.to_dict()
        assert rule_condition_single_property_model_json2 == rule_condition_single_property_model_json

class TestRuleRequiredConfigSingleProperty():
    """
    Test Class for RuleRequiredConfigSingleProperty
    """

    def test_rule_required_config_single_property_serialization(self):
        """
        Test serialization/deserialization for RuleRequiredConfigSingleProperty
        """

        # Construct a json representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_single_property_model_json = {}
        rule_required_config_single_property_model_json['description'] = 'testString'
        rule_required_config_single_property_model_json['property'] = 'public_access_enabled'
        rule_required_config_single_property_model_json['operator'] = 'is_true'
        rule_required_config_single_property_model_json['value'] = 'testString'

        # Construct a model instance of RuleRequiredConfigSingleProperty by calling from_dict on the json representation
        rule_required_config_single_property_model = RuleRequiredConfigSingleProperty.from_dict(rule_required_config_single_property_model_json)
        assert rule_required_config_single_property_model != False

        # Construct a model instance of RuleRequiredConfigSingleProperty by calling from_dict on the json representation
        rule_required_config_single_property_model_dict = RuleRequiredConfigSingleProperty.from_dict(rule_required_config_single_property_model_json).__dict__
        rule_required_config_single_property_model2 = RuleRequiredConfigSingleProperty(**rule_required_config_single_property_model_dict)

        # Verify the model instances are equivalent
        assert rule_required_config_single_property_model == rule_required_config_single_property_model2

        # Convert model instance back to dict and verify no loss of data
        rule_required_config_single_property_model_json2 = rule_required_config_single_property_model.to_dict()
        assert rule_required_config_single_property_model_json2 == rule_required_config_single_property_model_json

class TestRuleRequiredConfigMultiplePropertiesConditionAnd():
    """
    Test Class for RuleRequiredConfigMultiplePropertiesConditionAnd
    """

    def test_rule_required_config_multiple_properties_condition_and_serialization(self):
        """
        Test serialization/deserialization for RuleRequiredConfigMultiplePropertiesConditionAnd
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_condition_model = {} # RuleConditionSingleProperty
        rule_condition_model['description'] = 'testString'
        rule_condition_model['property'] = 'public_access_enabled'
        rule_condition_model['operator'] = 'is_true'
        rule_condition_model['value'] = 'testString'

        # Construct a json representation of a RuleRequiredConfigMultiplePropertiesConditionAnd model
        rule_required_config_multiple_properties_condition_and_model_json = {}
        rule_required_config_multiple_properties_condition_and_model_json['description'] = 'testString'
        rule_required_config_multiple_properties_condition_and_model_json['and'] = [rule_condition_model]

        # Construct a model instance of RuleRequiredConfigMultiplePropertiesConditionAnd by calling from_dict on the json representation
        rule_required_config_multiple_properties_condition_and_model = RuleRequiredConfigMultiplePropertiesConditionAnd.from_dict(rule_required_config_multiple_properties_condition_and_model_json)
        assert rule_required_config_multiple_properties_condition_and_model != False

        # Construct a model instance of RuleRequiredConfigMultiplePropertiesConditionAnd by calling from_dict on the json representation
        rule_required_config_multiple_properties_condition_and_model_dict = RuleRequiredConfigMultiplePropertiesConditionAnd.from_dict(rule_required_config_multiple_properties_condition_and_model_json).__dict__
        rule_required_config_multiple_properties_condition_and_model2 = RuleRequiredConfigMultiplePropertiesConditionAnd(**rule_required_config_multiple_properties_condition_and_model_dict)

        # Verify the model instances are equivalent
        assert rule_required_config_multiple_properties_condition_and_model == rule_required_config_multiple_properties_condition_and_model2

        # Convert model instance back to dict and verify no loss of data
        rule_required_config_multiple_properties_condition_and_model_json2 = rule_required_config_multiple_properties_condition_and_model.to_dict()
        assert rule_required_config_multiple_properties_condition_and_model_json2 == rule_required_config_multiple_properties_condition_and_model_json

class TestRuleRequiredConfigMultiplePropertiesConditionOr():
    """
    Test Class for RuleRequiredConfigMultiplePropertiesConditionOr
    """

    def test_rule_required_config_multiple_properties_condition_or_serialization(self):
        """
        Test serialization/deserialization for RuleRequiredConfigMultiplePropertiesConditionOr
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rule_condition_model = {} # RuleConditionSingleProperty
        rule_condition_model['description'] = 'testString'
        rule_condition_model['property'] = 'public_access_enabled'
        rule_condition_model['operator'] = 'is_true'
        rule_condition_model['value'] = 'testString'

        # Construct a json representation of a RuleRequiredConfigMultiplePropertiesConditionOr model
        rule_required_config_multiple_properties_condition_or_model_json = {}
        rule_required_config_multiple_properties_condition_or_model_json['description'] = 'testString'
        rule_required_config_multiple_properties_condition_or_model_json['or'] = [rule_condition_model]

        # Construct a model instance of RuleRequiredConfigMultiplePropertiesConditionOr by calling from_dict on the json representation
        rule_required_config_multiple_properties_condition_or_model = RuleRequiredConfigMultiplePropertiesConditionOr.from_dict(rule_required_config_multiple_properties_condition_or_model_json)
        assert rule_required_config_multiple_properties_condition_or_model != False

        # Construct a model instance of RuleRequiredConfigMultiplePropertiesConditionOr by calling from_dict on the json representation
        rule_required_config_multiple_properties_condition_or_model_dict = RuleRequiredConfigMultiplePropertiesConditionOr.from_dict(rule_required_config_multiple_properties_condition_or_model_json).__dict__
        rule_required_config_multiple_properties_condition_or_model2 = RuleRequiredConfigMultiplePropertiesConditionOr(**rule_required_config_multiple_properties_condition_or_model_dict)

        # Verify the model instances are equivalent
        assert rule_required_config_multiple_properties_condition_or_model == rule_required_config_multiple_properties_condition_or_model2

        # Convert model instance back to dict and verify no loss of data
        rule_required_config_multiple_properties_condition_or_model_json2 = rule_required_config_multiple_properties_condition_or_model.to_dict()
        assert rule_required_config_multiple_properties_condition_or_model_json2 == rule_required_config_multiple_properties_condition_or_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
