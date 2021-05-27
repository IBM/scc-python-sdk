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
Integration Tests for ConfigurationGovernanceV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_scc.configuration_governance_v1 import *

# Config file name
config_file = 'configuration_governance_v1.env'

# Variables to hold link values
rule_attachment_id_link = None
rule_id_link = None

class TestConfigurationGovernanceV1():
    """
    Integration Test Class for ConfigurationGovernanceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.configuration_governance_service = ConfigurationGovernanceV1.new_instance(
                )
            assert cls.configuration_governance_service is not None

            cls.config = read_external_sources(
                ConfigurationGovernanceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_rules(self):

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {
            'name': 'resource_id',
            'value': '81f3db5e-f9db-4c46-9de3-a4a76e66adbf',
            'operator': 'string_equals',
        }

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': 'iam-groups',
            'resource_kind': 'service',
            'additional_target_attributes': [target_resource_additional_target_attributes_item_model],
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {
            'description': 'Public access check',
            'property': 'public_access_enabled',
            'operator': 'is_true',
            'value': 'testString',
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': 'disallow',
        }

        # Construct a dict representation of a RuleRequest model
        rule_request_model = {
            'account_id': '531fc3e28bfc43c5a2cea07786d93f5c',
            'name': 'Disable public access',
            'description': 'Ensure that public access to account resources is disabled.',
            'rule_type': 'user_defined',
            'target': {'service_name':'iam-groups','resource_kind':'service'},
            'required_config': {'description':'Public access check','and':[{'property':'public_access_enabled','operator':'is_false'}]},
            'enforcement_actions': [enforcement_action_model],
            'labels': ['Access', 'IAM'],
        }

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {
            'request_id': '3cebc877-58e7-44a5-a292-32114fa73558',
            'rule': {'account_id':'531fc3e28bfc43c5a2cea07786d93f5c','name':'Disable public access','description':'Ensure that public access to account resources is disabled.','labels':['Access','IAM'],'target':{'service_name':'iam-groups','resource_kind':'service'},'required_config':{'description':'Public access check','and':[{'property':'public_access_enabled','operator':'is_false'}]},'enforcement_actions':[{'action':'disallow'},{'action':'audit_log'}]},
        }

        create_rules_response = self.configuration_governance_service.create_rules(
            rules=[create_rule_request_model],
            transaction_id='testString'
        )

        assert create_rules_response.get_status_code() == 201
        create_rules_response = create_rules_response.get_result()
        assert create_rules_response is not None

        # Store rule_id_link value for later test cases
        global rule_id_link
        rule_id_link = create_rules_response['rules'][0]['rule']['rule_id']

    @needscredentials
    def test_create_rule_attachments(self):

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {
            'note': 'My enterprise',
            'scope_id': '282cf433ac91493ba860480d92519990',
            'scope_type': 'enterprise',
        }

        # Construct a dict representation of a RuleAttachmentRequest model
        rule_attachment_request_model = {
            'account_id': '531fc3e28bfc43c5a2cea07786d93f5c',
            'included_scope': {'note':'My enterprise','scope_id':'282cf433ac91493ba860480d92519990','scope_type':'enterprise'},
            'excluded_scopes': [rule_scope_model],
        }

        create_rule_attachments_response = self.configuration_governance_service.create_rule_attachments(
            rule_id=rule_id_link,
            attachments=[rule_attachment_request_model],
            transaction_id='testString'
        )

        assert create_rule_attachments_response.get_status_code() == 201
        create_rule_attachments_response = create_rule_attachments_response.get_result()
        assert create_rule_attachments_response is not None

        # Store rule_attachment_id_link value for later test cases
        global rule_attachment_id_link
        rule_attachment_id_link = create_rule_attachments_response['attachments'][0]['attachment_id']

    @needscredentials
    def test_list_rules(self):

        list_rules_response = self.configuration_governance_service.list_rules(
            account_id='531fc3e28bfc43c5a2cea07786d93f5c',
            transaction_id='testString',
            attached=True,
            labels='SOC2,ITCS300',
            scopes='scope_id',
            limit=1000,
            offset=38
        )

        assert list_rules_response.get_status_code() == 200
        rule_list = list_rules_response.get_result()
        assert rule_list is not None

    @needscredentials
    def test_get_rule(self):

        get_rule_response = self.configuration_governance_service.get_rule(
            rule_id=rule_id_link,
            transaction_id='testString'
        )

        assert get_rule_response.get_status_code() == 200
        rule = get_rule_response.get_result()
        assert rule is not None

    @needscredentials
    def test_update_rule(self):

        # Construct a dict representation of a TargetResourceAdditionalTargetAttributesItem model
        target_resource_additional_target_attributes_item_model = {
            'name': 'testString',
            'value': 'testString',
            'operator': 'string_equals',
        }

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': 'iam-groups',
            'resource_kind': 'service',
            'additional_target_attributes': [target_resource_additional_target_attributes_item_model],
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {
            'description': 'testString',
            'property': 'public_access_enabled',
            'operator': 'is_false',
            'value': 'testString',
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': 'audit_log',
        }

        update_rule_response = self.configuration_governance_service.update_rule(
            rule_id=rule_id_link,
            if_match='testString',
            name='Disable public access',
            description='Ensure that public access to account resources is disabled.',
            target={'service_name':'iam-groups','resource_kind':'service','additional_target_attributes':[]},
            required_config={'property':'public_access_enabled','operator':'is_false'},
            enforcement_actions=[enforcement_action_model],
            account_id='531fc3e28bfc43c5a2cea07786d93f5c',
            rule_type='user_defined',
            labels=['SOC2', 'ITCS300'],
            transaction_id='testString'
        )

        assert update_rule_response.get_status_code() == 200
        rule = update_rule_response.get_result()
        assert rule is not None

    @needscredentials
    def test_list_rule_attachments(self):

        list_rule_attachments_response = self.configuration_governance_service.list_rule_attachments(
            rule_id=rule_id_link,
            transaction_id='testString',
            limit=1000,
            offset=38
        )

        assert list_rule_attachments_response.get_status_code() == 200
        rule_attachment_list = list_rule_attachments_response.get_result()
        assert rule_attachment_list is not None

    @needscredentials
    def test_get_rule_attachment(self):

        get_rule_attachment_response = self.configuration_governance_service.get_rule_attachment(
            rule_id=rule_id_link,
            attachment_id=rule_attachment_id_link,
            transaction_id='testString'
        )

        assert get_rule_attachment_response.get_status_code() == 200
        rule_attachment = get_rule_attachment_response.get_result()
        assert rule_attachment is not None

    @needscredentials
    def test_update_rule_attachment(self):

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {
            'note': 'My enterprise',
            'scope_id': '282cf433ac91493ba860480d92519990',
            'scope_type': 'enterprise',
        }

        update_rule_attachment_response = self.configuration_governance_service.update_rule_attachment(
            rule_id=rule_id_link,
            attachment_id=rule_attachment_id_link,
            if_match='testString',
            account_id='531fc3e28bfc43c5a2cea07786d93f5c',
            included_scope={'note':'My enterprise','scope_id':'282cf433ac91493ba860480d92519990','scope_type':'enterprise'},
            excluded_scopes=[rule_scope_model],
            transaction_id='testString'
        )

        assert update_rule_attachment_response.get_status_code() == 200
        template_attachment = update_rule_attachment_response.get_result()
        assert template_attachment is not None

    @needscredentials
    def test_delete_rule_attachment(self):

        delete_rule_attachment_response = self.configuration_governance_service.delete_rule_attachment(
            rule_id=rule_id_link,
            attachment_id=rule_attachment_id_link,
            transaction_id='testString'
        )

        assert delete_rule_attachment_response.get_status_code() == 204

    @needscredentials
    def test_delete_rule(self):

        delete_rule_response = self.configuration_governance_service.delete_rule(
            rule_id=rule_id_link,
            transaction_id='testString'
        )

        assert delete_rule_response.get_status_code() == 204

