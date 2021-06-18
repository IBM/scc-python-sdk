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
import time
from ibm_cloud_sdk_core import *
from ibm_scc.configuration_governance_v1 import *

# Config file name
config_file = 'configuration_governance_v1.env'

# Variables to hold link values
account_id = os.getenv("ACCOUNT_ID")
rule_label = os.getenv("RULE_LABEL") or "sdk-it"
resource_group_id = os.getenv("RESOURCE_GROUP_ID")
identifier = "py-{0}".format(str(time.time()).split(".")[0])

rule_attachment_id_link = None
rule_id_link = None

rule_etag = None
rule_attachment_etag = None

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

    @classmethod
    def teardown_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.configuration_governance_service = ConfigurationGovernanceV1.new_instance(
                )
            assert cls.configuration_governance_service is not None

            cls.config = read_external_sources(
                ConfigurationGovernanceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')
        print(f'cleaning up account: {account_id} with rules labelled {rule_label}-{identifier}\n')
        list_rules_response = cls.configuration_governance_service.list_rules(
            account_id=account_id,
            labels=[f"{rule_label}-{identifier}"],
        )
        for rule in list_rules_response.get_result()['rules']:
            cls.configuration_governance_service.delete_rule(
                rule_id=rule['rule_id']
            )
        print("cleanup was successful\n")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_rules(self):

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': 'cloud-object-storage',
            'resource_kind': 'bucket',
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {
            'description': 'Public access check',
            'property': 'location',
            'operator': 'string_equals',
            'value': 'us-south',
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': 'disallow',
        }

        # Construct a dict representation of a RuleRequest model
        rule_request_model = {
            'account_id': account_id,
            'name': 'Disable public access',
            'description': 'Ensure that public access to account resources is disabled.',
            'rule_type': 'user_defined',
            'target': target_resource_model,
            'required_config': rule_required_config_model,
            'enforcement_actions': [enforcement_action_model],
            'labels': [f"{rule_label}-{identifier}"],
        }

        # Construct a dict representation of a CreateRuleRequest model
        create_rule_request_model = {
            'request_id': '3cebc877-58e7-44a5-a292-32114fa73558',
            'rule': rule_request_model,
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
            'note': 'My account',
            'scope_id': account_id,
            'scope_type': 'account',
        }

        rule_excluded_scope_model = {
            'note': 'My account resource group',
            'scope_id': resource_group_id,
            'scope_type': 'account.resource_group',
        }

        # Construct a dict representation of a RuleAttachmentRequest model
        rule_attachment_request_model = {
            'account_id': account_id,
            'included_scope': rule_scope_model,
            'excluded_scopes': [rule_excluded_scope_model],
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
            account_id=account_id,
            transaction_id='testString',
            attached=True,
            labels=[f"{rule_label}-{identifier}"],
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

        global rule_etag
        rule_etag = get_rule_response.headers['etag']

    @needscredentials
    def test_update_rule(self):

        # Construct a dict representation of a TargetResource model
        target_resource_model = {
            'service_name': 'cloud-object-storage',
            'resource_kind': 'bucket',
        }

        # Construct a dict representation of a RuleRequiredConfigSingleProperty model
        rule_required_config_model = {
            'description': 'testString',
            'property': 'location',
            'operator': 'string_equals',
            'value': 'us-south',
        }

        # Construct a dict representation of a EnforcementAction model
        enforcement_action_model = {
            'action': 'disallow',
        }

        update_rule_response = self.configuration_governance_service.update_rule(
            rule_id=rule_id_link,
            if_match=rule_etag,
            name='Disable public access',
            description='Ensure that public access to account resources is disabled.',
            target=target_resource_model,
            required_config=rule_required_config_model,
            enforcement_actions=[enforcement_action_model],
            account_id=account_id,
            rule_type='user_defined',
            labels=[f"{rule_label}-{identifier}"],
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

        global rule_attachment_etag
        rule_attachment_etag = get_rule_attachment_response.headers['etag']

    @needscredentials
    def test_update_rule_attachment(self):

        # Construct a dict representation of a RuleScope model
        rule_scope_model = {
            'note': 'My account',
            'scope_id': account_id,
            'scope_type': 'account',
        }

        excluded_scope_model = {
            'note': 'My account resource group',
            'scope_id': resource_group_id,
            'scope_type': 'account.resource_group',
        }

        update_rule_attachment_response = self.configuration_governance_service.update_rule_attachment(
            rule_id=rule_id_link,
            attachment_id=rule_attachment_id_link,
            if_match=rule_attachment_etag,
            account_id=account_id,
            included_scope=rule_scope_model,
            excluded_scopes=[excluded_scope_model],
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

