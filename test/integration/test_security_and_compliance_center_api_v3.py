# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.
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
Integration Tests for SecurityAndComplianceCenterApiV3
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_scc.security_and_compliance_center_api_v3 import *
from datetime import datetime, timezone

# Config file name
config_file = 'security_and_compliance_center_api_v3.env'

# Variables to hold link values
account_id_for_report_link = None
attachment_id_for_report_link = None
attachment_id_link = None
control_library_id_link = None
e_tag_link = None
event_notifications_crn_for_update_settings_link = None
group_id_for_report_link = None
object_storage_bucket_for_update_settings_link = None
object_storage_crn_for_update_settings_link = None
object_storage_location_for_update_settings_link = None
profile_id_for_report_link = None
profile_id_link = None
provider_type_instance_id_link = None
report_id_for_report_link = None
rule_id_link = None
scan_id_for_scan_report_link = None
scope_id_link = None
sub_scope_id_link = None
target_id_link = None
type_for_report_link = None


class TestSecurityAndComplianceCenterApiV3:
    """
    Integration Test Class for SecurityAndComplianceCenterApiV3
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.security_and_compliance_center_api_service = SecurityAndComplianceCenterApiV3.new_instance(
            )
            assert cls.security_and_compliance_center_api_service is not None

            cls.config = read_external_sources(SecurityAndComplianceCenterApiV3.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.security_and_compliance_center_api_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_settings(self):
        global event_notifications_crn_for_update_settings_link
        global object_storage_crn_for_update_settings_link
        global object_storage_bucket_for_update_settings_link
        global object_storage_location_for_update_settings_link

        response = self.security_and_compliance_center_api_service.get_settings(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
        )

        assert response.get_status_code() == 200
        settings = response.get_result()
        assert settings is not None

        event_notifications_crn_for_update_settings_link = settings['event_notifications']['instance_crn']
        object_storage_crn_for_update_settings_link = settings['object_storage']['instance_crn']
        object_storage_bucket_for_update_settings_link = settings['object_storage']['bucket']
        object_storage_location_for_update_settings_link = settings['object_storage']['bucket_location']

    @needscredentials
    def test_update_settings(self):
        # Construct a dict representation of a ObjectStoragePrototype model
        object_storage_prototype_model = {
            'bucket': 'px-scan-results',
            'instance_crn': 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::',
        }
        # Construct a dict representation of a EventNotificationsPrototype model
        event_notifications_prototype_model = {
            'instance_crn': 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::',
            'source_description': 'This source is used for integration with IBM Cloud Security and Compliance Center.',
            'source_name': 'scc-sdk-integration',
        }

        response = self.security_and_compliance_center_api_service.update_settings(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            object_storage=object_storage_prototype_model,
            event_notifications=event_notifications_prototype_model,
        )

        assert response.get_status_code() == 200
        settings = response.get_result()
        assert settings is not None

    @needscredentials
    def test_post_test_event(self):
        response = self.security_and_compliance_center_api_service.post_test_event(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
        )

        assert response.get_status_code() == 202
        test_event = response.get_result()
        assert test_event is not None

    @needscredentials
    def test_list_instance_attachments(self):
        response = self.security_and_compliance_center_api_service.list_instance_attachments(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            version_group_label='6702d85a-6437-4d6f-8701-c0146648787b',
            limit=25,
            sort='created_on',
            direction='desc',
        )

        assert response.get_status_code() == 200
        profile_attachment_collection = response.get_result()
        assert profile_attachment_collection is not None

    @needscredentials
    def test_list_instance_attachments_with_pager(self):
        all_results = []

        # Test get_next().
        pager = InstanceAttachmentsPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            version_group_label='6702d85a-6437-4d6f-8701-c0146648787b',
            limit=10,
            sort='created_on',
            direction='desc',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = InstanceAttachmentsPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            version_group_label='6702d85a-6437-4d6f-8701-c0146648787b',
            limit=10,
            sort='created_on',
            direction='desc',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_instance_attachments() returned a total of {len(all_results)} items(s) using InstanceAttachmentsPager.')

    @needscredentials
    def test_create_profile_attachment(self):
        global attachment_id_link

        # Construct a dict representation of a Parameter model
        parameter_list = [
            {
                'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
                'parameter_name': 'tls_version',
                'parameter_display_name': 'IBM Cloud Internet Services TLS version',
                'parameter_type': 'string_list',
                'parameter_value': "['1.2', '1.3']",
            },
            {
                'assessment_id': 'rule-f9137be8-2490-4afb-8cd5-a201cb167eb2',
                'parameter_name': 'ssh_port',
                'parameter_display_name': 'Network ACL rule for allowed IPs to SSH port',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-9653d2c7-6290-4128-a5a3-65487ba40370',
                'parameter_name': 'rdp_port',
                'parameter_display_name': 'Security group rule RDP allow port number',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-7c5f6385-67e4-4edf-bec8-c722558b2dec',
                'parameter_name': 'ssh_port',
                'parameter_display_name': 'Security group rule SSH allow port number',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-f1e80ee7-88d5-4bf2-b42f-c863bb24601c',
                'parameter_name': 'rdp_port',
                'parameter_display_name': 'Disallowed IPs for ingress to RDP port',
                'parameter_type': 'numeric',
                'parameter_value': '3389',
            },
            {
                'assessment_id': 'rule-96527f89-1867-4581-b923-1400e04661e0',
                'parameter_name': 'exclude_default_security_groups',
                'parameter_display_name': 'Exclude the default security groups',
                'parameter_type': 'string_list',
                'parameter_value': "['Default']",
            },
        ]

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {
            'threshold_limit': 15,
            'failed_control_ids': [],
        }
        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {
            'enabled': True,
            'controls': attachment_notifications_controls_model,
        }
        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {
            'id': '8baad3b5-2e69-4027-9967-efac19508e1c',
        }
        # Construct a dict representation of a DateRange model
        end_date = datetime.now(timezone.utc).isoformat()
        date_range_model = {
            'start_date': '2025-02-28T05:42:58.000Z',
            'end_date': end_date,
        }
        # Construct a dict representation of a ProfileAttachmentBase model
        profile_attachment_base_model = {
            'attachment_parameters': parameter_list,
            'description': 'This is a profile attachment targeting IBM CIS Foundation using a SDK',
            'name': 'Profile Attachment for IBM CIS Foundation SDK test',
            'notifications': attachment_notifications_model,
            'schedule': 'daily',
            'scope': [multi_cloud_scope_payload_model],
            'status': 'disabled',
            'data_selection_range': date_range_model,
        }

        response = self.security_and_compliance_center_api_service.create_profile_attachment(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            new_attachments=[profile_attachment_base_model],
            new_profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3',
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 201
        profile_attachment_response = response.get_result()
        assert profile_attachment_response is not None

        attachment_id_link = profile_attachment_response['attachments'][0]['id']

    @needscredentials
    def test_get_profile_attachment(self):
        response = self.security_and_compliance_center_api_service.get_profile_attachment(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            attachment_id=attachment_id_link,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile_attachment = response.get_result()
        assert profile_attachment is not None

    @needscredentials
    def test_replace_profile_attachment(self):
        # Construct a dict representation of a Parameter model
        parameter_list = [
            {
                'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
                'parameter_name': 'tls_version',
                'parameter_display_name': 'IBM Cloud Internet Services TLS version',
                'parameter_type': 'string_list',
                'parameter_value': "['1.2', '1.3']",
            },
            {
                'assessment_id': 'rule-f9137be8-2490-4afb-8cd5-a201cb167eb2',
                'parameter_name': 'ssh_port',
                'parameter_display_name': 'Network ACL rule for allowed IPs to SSH port',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-9653d2c7-6290-4128-a5a3-65487ba40370',
                'parameter_name': 'rdp_port',
                'parameter_display_name': 'Security group rule RDP allow port number',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-7c5f6385-67e4-4edf-bec8-c722558b2dec',
                'parameter_name': 'ssh_port',
                'parameter_display_name': 'Security group rule SSH allow port number',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-f1e80ee7-88d5-4bf2-b42f-c863bb24601c',
                'parameter_name': 'rdp_port',
                'parameter_display_name': 'Disallowed IPs for ingress to RDP port',
                'parameter_type': 'numeric',
                'parameter_value': '3389',
            },
            {
                'assessment_id': 'rule-96527f89-1867-4581-b923-1400e04661e0',
                'parameter_name': 'exclude_default_security_groups',
                'parameter_display_name': 'Exclude the default security groups',
                'parameter_type': 'string_list',
                'parameter_value': "['Default']",
            },
        ]

        # Construct a dict representation of a AttachmentNotificationsControls model
        attachment_notifications_controls_model = {
            'threshold_limit': 15,
            'failed_control_ids': [],
        }
        # Construct a dict representation of a AttachmentNotifications model
        attachment_notifications_model = {
            'enabled': True,
            'controls': attachment_notifications_controls_model,
        }
        # Construct a dict representation of a MultiCloudScopePayloadById model
        multi_cloud_scope_payload_model = {
            'id': '8baad3b5-2e69-4027-9967-efac19508e1c',
        }
        # Construct a dict representation of a DateRange model
        end_date = datetime.now(timezone.utc).isoformat()
        date_range_model = {
            'start_date': '2025-02-28T05:42:58.000Z',
            'end_date': end_date,
        }

        response = self.security_and_compliance_center_api_service.replace_profile_attachment(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            attachment_id=attachment_id_link,
            attachment_parameters=parameter_list,
            description='New Profile Attachment',
            name='SDK Updated Test',
            notifications=attachment_notifications_model,
            schedule='daily',
            scope=[multi_cloud_scope_payload_model],
            status='disabled',
            data_selection_range=date_range_model,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile_attachment = response.get_result()
        assert profile_attachment is not None

    @needscredentials
    def test_upgrade_attachment(self):
        # Construct a dict representation of a Parameter model
        parameter_list = [
            {
                'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
                'parameter_name': 'tls_version',
                'parameter_display_name': 'IBM Cloud Internet Services TLS version',
                'parameter_type': 'string_list',
                'parameter_value': "['1.2', '1.3']",
            },
            {
                'assessment_id': 'rule-f9137be8-2490-4afb-8cd5-a201cb167eb2',
                'parameter_name': 'ssh_port',
                'parameter_display_name': 'Network ACL rule for allowed IPs to SSH port',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-9653d2c7-6290-4128-a5a3-65487ba40370',
                'parameter_name': 'rdp_port',
                'parameter_display_name': 'Security group rule RDP allow port number',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-7c5f6385-67e4-4edf-bec8-c722558b2dec',
                'parameter_name': 'ssh_port',
                'parameter_display_name': 'Security group rule SSH allow port number',
                'parameter_type': 'numeric',
                'parameter_value': '22',
            },
            {
                'assessment_id': 'rule-f1e80ee7-88d5-4bf2-b42f-c863bb24601c',
                'parameter_name': 'rdp_port',
                'parameter_display_name': 'Disallowed IPs for ingress to RDP port',
                'parameter_type': 'numeric',
                'parameter_value': '3389',
            },
            {
                'assessment_id': 'rule-96527f89-1867-4581-b923-1400e04661e0',
                'parameter_name': 'exclude_default_security_groups',
                'parameter_display_name': 'Exclude the default security groups',
                'parameter_type': 'string_list',
                'parameter_value': "['Default']",
            },
        ]

        response = self.security_and_compliance_center_api_service.upgrade_attachment(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            attachment_id=attachment_id_link,
            attachment_parameters=parameter_list,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile_attachment = response.get_result()
        assert profile_attachment is not None

    @needscredentials
    def test_create_scan(self):
        response = self.security_and_compliance_center_api_service.create_scan(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            attachment_id='4deb572c-9f37-4126-9cc0-d550672533cb',
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 201
        create_scan_response = response.get_result()
        assert create_scan_response is not None

    @needscredentials
    def test_create_control_library(self):
        global control_library_id_link

        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {
            'assessment_id': 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e',
            'assessment_description': 'This rule will check on regulation',
        }
        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {
            'component_id': 'apprapp',
            'environment': 'ibm-cloud',
            'control_specification_description': 'This field is used to describe a control specification',
            'assessments': [assessment_prototype_model],
        }
        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {
            'control_name': 'security',
            'control_description': 'This is a description of a control',
            'control_category': 'test-control',
            'control_requirement': True,
            'control_specifications': [control_specification_prototype_model],
            'status': 'disabled',
        }

        response = self.security_and_compliance_center_api_service.create_control_library(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            control_library_name='custom control library from SDK',
            control_library_description='This is a custom control library made from the SDK test framework',
            control_library_type='custom',
            control_library_version='0.0.1',
            controls=[control_prototype_model],
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 201
        control_library = response.get_result()
        assert control_library is not None

        control_library_id_link = control_library['id']

    @needscredentials
    def test_list_control_libraries(self):
        response = self.security_and_compliance_center_api_service.list_control_libraries(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            limit=10,
        )

        assert response.get_status_code() == 200
        control_library_collection = response.get_result()
        assert control_library_collection is not None

    @needscredentials
    def test_list_control_libraries_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ControlLibrariesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ControlLibrariesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_control_libraries() returned a total of {len(all_results)} items(s) using ControlLibrariesPager.')

    @needscredentials
    def test_replace_custom_control_library(self):
        # Construct a dict representation of a AssessmentPrototype model
        assessment_prototype_model = {
            'assessment_id': 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e',
            'assessment_description': 'This rule will check on regulation',
        }
        # Construct a dict representation of a ControlSpecificationPrototype model
        control_specification_prototype_model = {
            'component_id': 'apprapp',
            'environment': 'ibm-cloud',
            'control_specification_description': 'This field is used to describe a control specification',
            'assessments': [assessment_prototype_model],
        }
        # Construct a dict representation of a ControlDoc model
        control_doc_model = {
            'control_docs_id': 'testString',
            'control_docs_type': 'testString',
        }
        # Construct a dict representation of a ControlPrototype model
        control_prototype_model = {
            'control_name': 'security',
            'control_description': 'This is a description of a control',
            'control_category': 'test-control',
            'control_requirement': True,
            'control_parent': '',
            'control_specifications': [control_specification_prototype_model],
            'control_docs': control_doc_model,
            'status': 'enabled',
        }

        response = self.security_and_compliance_center_api_service.replace_custom_control_library(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            control_library_id=control_library_id_link,
            control_library_name='custom control library update from SDK',
            control_library_description='This is a custom control library made from the SDK test framework',
            control_library_type='custom',
            control_library_version='0.0.2',
            controls=[control_prototype_model],
        )

        assert response.get_status_code() == 200
        control_library = response.get_result()
        assert control_library is not None

    @needscredentials
    def test_get_control_library(self):
        response = self.security_and_compliance_center_api_service.get_control_library(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            control_library_id=control_library_id_link,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        control_library = response.get_result()
        assert control_library is not None

    @needscredentials
    def test_create_profile(self):
        global profile_id_link

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {
            'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
            'control_id': '60dae3b5-6104-4b3e-bac7-26cc7b741aca',
        }
        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {
            'assessment_type': 'automated',
            'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
            'parameter_name': 'tls_version',
            'parameter_default_value': '["1.2","1.3"]',
            'parameter_display_name': 'IBM Cloud Internet Services TLS version',
            'parameter_type': 'string_list',
        }

        response = self.security_and_compliance_center_api_service.create_profile(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_name='Example Profile',
            profile_version='0.0.1',
            controls=[profile_controls_prototype_model],
            default_parameters=[default_parameters_model],
            profile_description='This profile is created as an example of the SDK gen',
            latest=True,
            version_group_label='testString',
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 201
        profile = response.get_result()
        assert profile is not None

        profile_id_link = profile['id']

    @needscredentials
    def test_list_profiles(self):
        response = self.security_and_compliance_center_api_service.list_profiles(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            limit=50,
            start='testString',
        )

        assert response.get_status_code() == 200
        profile_collection = response.get_result()
        assert profile_collection is not None

    @needscredentials
    def test_list_profiles_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ProfilesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ProfilesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id=account_id_for_report_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_profiles() returned a total of {len(all_results)} items(s) using ProfilesPager.')

    @needscredentials
    def test_replace_profile(self):
        # Construct a dict representation of a ControlDoc model
        control_doc_model = {
            'control_docs_id': 'testString',
            'control_docs_type': 'testString',
        }
        # Construct a dict representation of a Parameter model
        parameter_model = {
            'assessment_type': 'testString',
            'assessment_id': 'testString',
            'parameter_name': 'location',
            'parameter_display_name': 'Location',
            'parameter_type': 'string',
            'parameter_value': 'testString',
        }
        # Construct a dict representation of a Assessment model
        assessment_model = {
            'assessment_id': '382c2b06-e6b2-43ee-b189-c1c7743b67ee',
            'assessment_type': 'ibm-cloud-rule',
            'assessment_method': 'ibm-cloud-rule',
            'assessment_description': 'Check whether Cloud Object Storage is accessible only by using private endpoints',
            'parameter_count': 1,
            'parameters': [parameter_model],
        }
        # Construct a dict representation of a ControlSpecification model
        control_specification_model = {
            'id': 'testString',
            'responsibility': 'testString',
            'component_id': 'testString',
            'component_name': 'testString',
            'component_type': 'testString',
            'environment': 'testString',
            'description': 'testString',
            'assessments_count': 38,
            'assessments': [assessment_model],
        }
        # Construct a dict representation of a ProfileControls model
        profile_controls_model = {
            'control_requirement': True,
            'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
            'control_id': '60dae3b5-6104-4b3e-bac7-26cc7b741aca',
            'control_library_version': 'testString',
            'control_name': 'testString',
            'control_description': 'testString',
            'control_severity': 'testString',
            'control_category': 'testString',
            'control_parent': 'testString',
            'control_docs': control_doc_model,
            'control_specifications': [control_specification_model],
        }
        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {
            'assessment_type': 'automated',
            'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
            'parameter_name': 'tls_version',
            'parameter_default_value': '["1.2","1.3"]',
            'parameter_display_name': 'IBM Cloud Internet Services TLS version',
            'parameter_type': 'string_list',
        }

        response = self.security_and_compliance_center_api_service.replace_profile(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id=profile_id_link,
            new_profile_type='custom',
            new_controls=[profile_controls_model],
            new_default_parameters=[default_parameters_model],
            new_id='testString',
            new_profile_name='Example Profile Updated',
            new_instance_id='testString',
            new_hierarchy_enabled=True,
            new_profile_description='This profile has been updated',
            new_profile_version='0.0.2',
            new_version_group_label='testString',
            new_latest=True,
            new_created_by='testString',
            new_created_on=string_to_datetime('2019-01-01T12:00:00.000Z'),
            new_updated_by='testString',
            new_updated_on=string_to_datetime('2019-01-01T12:00:00.000Z'),
            new_controls_count=38,
            new_attachments_count=38,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile = response.get_result()
        assert profile is not None

    @needscredentials
    def test_get_profile(self):
        response = self.security_and_compliance_center_api_service.get_profile(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id=profile_id_link,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile = response.get_result()
        assert profile is not None

    @needscredentials
    def test_replace_profile_parameters(self):
        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {
            'assessment_type': 'testString',
            'assessment_id': 'testString',
            'parameter_name': 'testString',
            'parameter_default_value': 'testString',
            'parameter_display_name': 'testString',
            'parameter_type': 'testString',
        }

        response = self.security_and_compliance_center_api_service.replace_profile_parameters(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id=profile_id_link,
            default_parameters=[default_parameters_model],
            id='testString',
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile_default_parameters_response = response.get_result()
        assert profile_default_parameters_response is not None

    @needscredentials
    def test_list_profile_parameters(self):
        response = self.security_and_compliance_center_api_service.list_profile_parameters(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id=profile_id_link,
        )

        assert response.get_status_code() == 200
        profile_default_parameters_response = response.get_result()
        assert profile_default_parameters_response is not None

    @needscredentials
    def test_compare_profiles(self):
        response = self.security_and_compliance_center_api_service.compare_profiles(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='2f598907-970d-4d52-9071-5cc95912f55e',
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        compare_predefined_profiles_response = response.get_result()
        assert compare_predefined_profiles_response is not None

    @needscredentials
    def test_list_profile_attachments(self):
        response = self.security_and_compliance_center_api_service.list_profile_attachments(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile_attachment_collection = response.get_result()
        assert profile_attachment_collection is not None

    @needscredentials
    def test_create_scope(self):
        global scope_id_link

        # Construct a dict representation of a ScopePropertyScopeAny model
        scope_property_model = {
            'name': 'scope_id',
            'value': 'ff88f007f9ff4622aac4fbc0eda36255',
        }

        response = self.security_and_compliance_center_api_service.create_scope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            name='ibm scope',
            description='The scope that is defined for IBM resources.',
            environment='ibm-cloud',
            properties=[scope_property_model],
        )

        assert response.get_status_code() == 201
        scope = response.get_result()
        assert scope is not None

        scope_id_link = scope['id']

    @needscredentials
    def test_list_scopes(self):
        response = self.security_and_compliance_center_api_service.list_scopes(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=50,
            start='testString',
            name='testString',
            description='testString',
            environment='testString',
        )

        assert response.get_status_code() == 200
        scope_collection = response.get_result()
        assert scope_collection is not None

    @needscredentials
    def test_list_scopes_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ScopesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ScopesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_scopes() returned a total of {len(all_results)} items(s) using ScopesPager.')

    @needscredentials
    def test_update_scope(self):
        response = self.security_and_compliance_center_api_service.update_scope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            name='updated name of scope',
            description='updated scope description',
        )

        assert response.get_status_code() == 200
        scope = response.get_result()
        assert scope is not None

    @needscredentials
    def test_get_scope(self):
        response = self.security_and_compliance_center_api_service.get_scope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
        )

        assert response.get_status_code() == 200
        scope = response.get_result()
        assert scope is not None

    @needscredentials
    def test_create_subscope(self):
        global sub_scope_id_link

        # Construct a dict representation of a ScopePropertyScopeAny model
        scope_property_model = {
            'name': 'scope_id',
            'value': '1f689f08ec9b47b885c2659c17029581',
        }
        # Construct a dict representation of a ScopePrototype model
        scope_prototype_model = {
            'name': 'ibm subscope update',
            'description': 'The subscope that is defined for IBM resources.',
            'environment': 'ibm-cloud',
            'properties': [scope_property_model],
        }

        response = self.security_and_compliance_center_api_service.create_subscope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            subscopes=[scope_prototype_model],
        )

        assert response.get_status_code() == 201
        sub_scope_response = response.get_result()
        assert sub_scope_response is not None

        sub_scope_id_link = sub_scope_response['subscopes'][0]['id']

    @needscredentials
    def test_list_subscopes(self):
        response = self.security_and_compliance_center_api_service.list_subscopes(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            limit=50,
            start='testString',
            name='testString',
            description='testString',
            environment='testString',
        )

        assert response.get_status_code() == 200
        sub_scope_collection = response.get_result()
        assert sub_scope_collection is not None

    @needscredentials
    def test_list_subscopes_with_pager(self):
        all_results = []

        # Test get_next().
        pager = SubscopesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = SubscopesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            limit=10,
            name='testString',
            description='testString',
            environment='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_subscopes() returned a total of {len(all_results)} items(s) using SubscopesPager.')

    @needscredentials
    def test_get_subscope(self):
        response = self.security_and_compliance_center_api_service.get_subscope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            subscope_id=sub_scope_id_link,
        )

        assert response.get_status_code() == 200
        sub_scope = response.get_result()
        assert sub_scope is not None

    @needscredentials
    def test_update_subscope(self):
        response = self.security_and_compliance_center_api_service.update_subscope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            subscope_id=sub_scope_id_link,
            name='updated name of scope',
            description='updated scope description',
        )

        assert response.get_status_code() == 200
        sub_scope = response.get_result()
        assert sub_scope is not None

    @needscredentials
    def test_create_target(self):
        global target_id_link

        # Construct a dict representation of a Account model
        account_model = {
            'id': '531fc3e28bfc43c5a2cea07786d93f5c',
            'name': 'NIST',
            'type': 'account_type',
        }
        # Construct a dict representation of a Tags model
        tags_model = {
            'user': ['testString'],
            'access': ['testString'],
            'service': ['testString'],
        }
        # Construct a dict representation of a Resource model
        resource_model = {
            'report_id': '30b434b3-cb08-4845-af10-7a8fc682b6a8',
            'home_account_id': '2411ffdc16844b07b42521c3443f456d',
            'id': 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::',
            'resource_name': 'jeff\'s key',
            'account': account_model,
            'component_id': 'cloud-object_storage',
            'component_name': 'cloud-object_storage',
            'environment': 'ibm cloud',
            'tags': tags_model,
            'status': 'compliant',
            'total_count': 140,
            'pass_count': 123,
            'failure_count': 12,
            'error_count': 5,
            'skipped_count': 7,
            'completed_count': 135,
            'service_name': 'pm-20',
            'instance_crn': 'testString',
        }
        # Construct a dict representation of a Credential model
        credential_model = {
            'secret_crn': 'testString',
            'resources': [resource_model],
        }

        response = self.security_and_compliance_center_api_service.create_target(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            account_id='62ecf99b240144dea9125666249edfcb',
            trusted_profile_id='Profile-cb2c1829-9a8d-4218-b9cd-9f83fc814e54',
            name='Target for IBM account',
            credentials=[credential_model],
        )

        assert response.get_status_code() == 201
        target = response.get_result()
        assert target is not None

        target_id_link = target['id']

    @needscredentials
    def test_list_targets(self):
        response = self.security_and_compliance_center_api_service.list_targets(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
        )

        assert response.get_status_code() == 200
        target_collection = response.get_result()
        assert target_collection is not None

    @needscredentials
    def test_get_target(self):
        response = self.security_and_compliance_center_api_service.get_target(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            target_id=target_id_link,
        )

        assert response.get_status_code() == 200
        target = response.get_result()
        assert target is not None

    @needscredentials
    def test_replace_target(self):
        # Construct a dict representation of a Account model
        account_model = {
            'id': '531fc3e28bfc43c5a2cea07786d93f5c',
            'name': 'NIST',
            'type': 'account_type',
        }
        # Construct a dict representation of a Tags model
        tags_model = {
            'user': ['testString'],
            'access': ['testString'],
            'service': ['testString'],
        }
        # Construct a dict representation of a Resource model
        resource_model = {
            'report_id': '30b434b3-cb08-4845-af10-7a8fc682b6a8',
            'home_account_id': '2411ffdc16844b07b42521c3443f456d',
            'id': 'crn:v1:bluemix:public:kms:us-south:a/5af747ca19a8a278b1b6e4eec20df507:03502a50-4ea9-463c-80e5-e27ed838cdb6::',
            'resource_name': 'jeff\'s key',
            'account': account_model,
            'component_id': 'cloud-object_storage',
            'component_name': 'cloud-object_storage',
            'environment': 'ibm cloud',
            'tags': tags_model,
            'status': 'compliant',
            'total_count': 140,
            'pass_count': 123,
            'failure_count': 12,
            'error_count': 5,
            'skipped_count': 7,
            'completed_count': 135,
            'service_name': 'pm-20',
            'instance_crn': 'testString',
        }
        # Construct a dict representation of a Credential model
        credential_model = {
            'secret_crn': 'dummy',
            'resources': [resource_model],
        }

        response = self.security_and_compliance_center_api_service.replace_target(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            target_id=target_id_link,
            account_id='be200c80cabc456e91139e4152327823',
            trusted_profile_id='Profile-a0a4c149-4fed-47ff-bfb2-680bcfaa64d3',
            name='Sample Target Name',
            credentials=[credential_model],
        )

        assert response.get_status_code() == 200
        target = response.get_result()
        assert target is not None

    @needscredentials
    def test_create_provider_type_instance(self):
        global provider_type_instance_id_link

        response = self.security_and_compliance_center_api_service.create_provider_type_instance(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            provider_type_id='3e25966275dccfa2c3a34786919c5af7',
            name='workload-protection-instance-1',
            attributes={'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'},
        )

        assert response.get_status_code() == 201
        provider_type_instance = response.get_result()
        assert provider_type_instance is not None

        provider_type_instance_id_link = provider_type_instance['id']

    @needscredentials
    def test_list_provider_type_instances(self):
        response = self.security_and_compliance_center_api_service.list_provider_type_instances(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            provider_type_id='3e25966275dccfa2c3a34786919c5af7',
        )

        assert response.get_status_code() == 200
        provider_type_instance_collection = response.get_result()
        assert provider_type_instance_collection is not None

    @needscredentials
    def test_get_provider_type_instance(self):
        response = self.security_and_compliance_center_api_service.get_provider_type_instance(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            provider_type_id='3e25966275dccfa2c3a34786919c5af7',
            provider_type_instance_id=provider_type_instance_id_link,
        )

        assert response.get_status_code() == 200
        provider_type_instance = response.get_result()
        assert provider_type_instance is not None

    @needscredentials
    def test_update_provider_type_instance(self):
        response = self.security_and_compliance_center_api_service.update_provider_type_instance(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            provider_type_id='3e25966275dccfa2c3a34786919c5af7',
            provider_type_instance_id=provider_type_instance_id_link,
            name='workload-protection-instance-1',
            attributes={'wp_crn': 'crn:v1:staging:public:sysdig-secure:eu-gb:a/14q5SEnVIbwxzvP4AWPCjr2dJg5BAvPb:d1461d1ae-df1eee12fa81812e0-12-aa259::'},
        )

        assert response.get_status_code() == 200
        provider_type_instance = response.get_result()
        assert provider_type_instance is not None

    @needscredentials
    def test_list_provider_types(self):
        response = self.security_and_compliance_center_api_service.list_provider_types(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
        )

        assert response.get_status_code() == 200
        provider_type_collection = response.get_result()
        assert provider_type_collection is not None

    @needscredentials
    def test_get_provider_type_by_id(self):
        response = self.security_and_compliance_center_api_service.get_provider_type_by_id(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            provider_type_id='3e25966275dccfa2c3a34786919c5af7',
        )

        assert response.get_status_code() == 200
        provider_type = response.get_result()
        assert provider_type is not None

    @needscredentials
    def test_get_latest_reports(self):
        global account_id_for_report_link
        global report_id_for_report_link
        global attachment_id_for_report_link
        global group_id_for_report_link
        global profile_id_for_report_link
        global type_for_report_link

        response = self.security_and_compliance_center_api_service.get_latest_reports(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            sort='profile_name',
        )

        assert response.get_status_code() == 200
        report_latest = response.get_result()
        assert report_latest is not None

        account_id_for_report_link = report_latest['reports'][0]['account']['id']
        report_id_for_report_link = report_latest['reports'][0]['id']
        attachment_id_for_report_link = report_latest['reports'][0]['attachment']['id']
        group_id_for_report_link = report_latest['reports'][0]['group_id']
        profile_id_for_report_link = report_latest['reports'][0]['profile']['id']
        type_for_report_link = report_latest['reports'][0]['type']

    @needscredentials
    def test_list_reports(self):
        response = self.security_and_compliance_center_api_service.list_reports(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_attachment_id=attachment_id_for_report_link,
            group_id=group_id_for_report_link,
            report_profile_id=profile_id_for_report_link,
            type=type_for_report_link,
            start='testString',
            limit=50,
            sort='profile_name',
        )

        assert response.get_status_code() == 200
        report_collection = response.get_result()
        assert report_collection is not None

    @needscredentials
    def test_list_reports_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ReportsPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_attachment_id=attachment_id_for_report_link,
            group_id=group_id_for_report_link,
            report_profile_id=profile_id_for_report_link,
            type=type_for_report_link,
            limit=10,
            sort='profile_name',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ReportsPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_attachment_id=attachment_id_for_report_link,
            group_id=group_id_for_report_link,
            report_profile_id=profile_id_for_report_link,
            type=type_for_report_link,
            limit=10,
            sort='profile_name',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_reports() returned a total of {len(all_results)} items(s) using ReportsPager.')

    @needscredentials
    def test_get_report(self):
        response = self.security_and_compliance_center_api_service.get_report(
            report_id=report_id_for_report_link,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id='testString',
            subscope_id='testString',
        )

        assert response.get_status_code() == 200
        report = response.get_result()
        assert report is not None

    @needscredentials
    def test_get_report_summary(self):
        response = self.security_and_compliance_center_api_service.get_report_summary(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
        )

        assert response.get_status_code() == 200
        report_summary = response.get_result()
        assert report_summary is not None

    @needscredentials
    def test_get_report_download_file(self):
        response = self.security_and_compliance_center_api_service.get_report_download_file(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            accept='application/csv',
            exclude_summary=True,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_report_controls(self):
        response = self.security_and_compliance_center_api_service.get_report_controls(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            control_id='testString',
            control_name='testString',
            control_description='testString',
            control_category='testString',
            status='compliant',
            sort='control_name',
            scope_id='testString',
            subscope_id='testString',
        )

        assert response.get_status_code() == 200
        report_controls = response.get_result()
        assert report_controls is not None

    @needscredentials
    def test_get_report_rule(self):
        response = self.security_and_compliance_center_api_service.get_report_rule(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            rule_id='rule-61fa114a-2bb9-43fd-8068-b873b48bdf79',
        )

        assert response.get_status_code() == 200
        rule_info = response.get_result()
        assert rule_info is not None

    @needscredentials
    def test_list_report_evaluations(self):
        response = self.security_and_compliance_center_api_service.list_report_evaluations(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            assessment_id='testString',
            assessment_method='testString',
            component_id='testString',
            target_id='testString',
            target_env='testString',
            target_name='testString',
            status='failure',
            start='testString',
            limit=50,
            sort='assessment_id',
            scope_id='testString',
            subscope_id='testString',
        )

        assert response.get_status_code() == 200
        evaluation_page = response.get_result()
        assert evaluation_page is not None

    @needscredentials
    def test_list_report_evaluations_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ReportEvaluationsPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            assessment_id='testString',
            assessment_method='testString',
            component_id='testString',
            target_id='testString',
            target_env='testString',
            target_name='testString',
            status='failure',
            limit=10,
            sort='assessment_id',
            scope_id='testString',
            subscope_id='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ReportEvaluationsPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            assessment_id='testString',
            assessment_method='testString',
            component_id='testString',
            target_id='testString',
            target_env='testString',
            target_name='testString',
            status='failure',
            limit=10,
            sort='assessment_id',
            scope_id='testString',
            subscope_id='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_report_evaluations() returned a total of {len(all_results)} items(s) using ReportEvaluationsPager.')

    @needscredentials
    def test_list_report_resources(self):
        response = self.security_and_compliance_center_api_service.list_report_resources(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            id='testString',
            resource_name='testString',
            account_id=account_id_for_report_link,
            component_id='testString',
            status='compliant',
            sort='account_id',
            start='testString',
            limit=50,
            scope_id='testString',
            subscope_id='testString',
        )

        assert response.get_status_code() == 200
        resource_page = response.get_result()
        assert resource_page is not None

    @needscredentials
    def test_list_report_resources_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ReportResourcesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            id='testString',
            resource_name='testString',
            account_id=account_id_for_report_link,
            component_id='testString',
            status='compliant',
            sort='account_id',
            limit=10,
            scope_id='testString',
            subscope_id='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ReportResourcesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            id='testString',
            resource_name='testString',
            account_id=account_id_for_report_link,
            component_id='testString',
            status='compliant',
            sort='account_id',
            limit=10,
            scope_id='testString',
            subscope_id='testString',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_report_resources() returned a total of {len(all_results)} items(s) using ReportResourcesPager.')

    @needscredentials
    def test_get_report_tags(self):
        response = self.security_and_compliance_center_api_service.get_report_tags(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
        )

        assert response.get_status_code() == 200
        report_tags = response.get_result()
        assert report_tags is not None

    @needscredentials
    def test_get_report_violations_drift(self):
        response = self.security_and_compliance_center_api_service.get_report_violations_drift(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            scan_time_duration=0,
            scope_id='testString',
            subscope_id='testString',
        )

        assert response.get_status_code() == 200
        report_violations_drift = response.get_result()
        assert report_violations_drift is not None

    @needscredentials
    def test_list_scan_reports(self):
        global scan_id_for_scan_report_link

        response = self.security_and_compliance_center_api_service.list_scan_reports(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            scope_id='testString',
            subscope_id='testString',
            sort='status',
        )

        assert response.get_status_code() == 200
        scan_report_collection = response.get_result()
        assert scan_report_collection is not None

        scan_id_for_scan_report_link = scan_report_collection['scan_reports'][0]['id']

    @needscredentials
    def test_create_scan_report(self):
        response = self.security_and_compliance_center_api_service.create_scan_report(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            format='csv',
            scope_id='132009ff-b982-412e-a110-ad8797e10f84',
            subscope_id='c7ddcbcc-6a43-4ab3-b6a7-b2d8f65cd54a',
        )

        assert response.get_status_code() == 202
        create_scan_report = response.get_result()
        assert create_scan_report is not None

    @needscredentials
    def test_get_scan_report(self):
        response = self.security_and_compliance_center_api_service.get_scan_report(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            job_id=scan_id_for_scan_report_link,
        )

        assert response.get_status_code() == 200
        scan_report = response.get_result()
        assert scan_report is not None

    @needscredentials
    def test_get_scan_report_download_file(self):
        response = self.security_and_compliance_center_api_service.get_scan_report_download_file(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            report_id=report_id_for_report_link,
            job_id=scan_id_for_scan_report_link,
            accept='application/csv',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_list_rules(self):
        response = self.security_and_compliance_center_api_service.list_rules(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=50,
            start='testString',
            type='system_defined',
            search='testString',
            service_name='testString',
            sort='updated_on',
        )

        assert response.get_status_code() == 200
        rule_collection = response.get_result()
        assert rule_collection is not None

    @needscredentials
    def test_list_rules_with_pager(self):
        all_results = []

        # Test get_next().
        pager = RulesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            type='system_defined',
            search='testString',
            service_name='testString',
            sort='updated_on',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = RulesPager(
            client=self.security_and_compliance_center_api_service,
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            limit=10,
            type='system_defined',
            search='testString',
            service_name='testString',
            sort='updated_on',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_rules() returned a total of {len(all_results)} items(s) using RulesPager.')

    @needscredentials
    def test_create_rule(self):
        global rule_id_link

        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {
            'name': 'location',
            'operator': 'string_equals',
            'value': 'us-east',
        }
        # Construct a dict representation of a RuleTargetPrototype model
        rule_target_prototype_model = {
            'service_name': 'cloud-object-storage',
            'resource_kind': 'bucket',
            'additional_target_attributes': [additional_target_attribute_model],
        }
        # Construct a dict representation of a RequiredConfigConditionBase model
        required_config_model = {
            'description': 'The Cloud Object Storage rule.',
            'property': 'testString',
            'operator': 'string_equals',
            'value': 'testString',
        }
        # Construct a dict representation of a RuleParameter model
        rule_parameter_model = {
            'name': 'hard_quota',
            'display_name': 'The Cloud Object Storage bucket quota.',
            'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
            'type': 'numeric',
        }
        # Construct a dict representation of a Import model
        import_model = {
            'parameters': [rule_parameter_model],
        }

        response = self.security_and_compliance_center_api_service.create_rule(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            description='Example rule',
            target=rule_target_prototype_model,
            required_config=required_config_model,
            version='1.0.0',
            import_=import_model,
            labels=[],
        )

        assert response.get_status_code() == 201
        rule = response.get_result()
        assert rule is not None

        rule_id_link = rule['id']

    @needscredentials
    def test_get_rule(self):
        global e_tag_link

        response = self.security_and_compliance_center_api_service.get_rule(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            rule_id=rule_id_link,
        )

        assert response.get_status_code() == 200
        rule = response.get_result()
        assert rule is not None

        e_tag_link = response.get_headers().get('ETag')

    @needscredentials
    def test_replace_rule(self):
        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {
            'name': 'location',
            'operator': 'string_equals',
            'value': 'us-south',
        }
        # Construct a dict representation of a RuleTargetPrototype model
        rule_target_prototype_model = {
            'service_name': 'cloud-object-storage',
            'resource_kind': 'bucket',
            'additional_target_attributes': [additional_target_attribute_model],
        }
        # Construct a dict representation of a RequiredConfigConditionBase model
        required_config_model = {
            'description': 'The Cloud Object Storage rule.',
            'property': 'testString',
            'operator': 'string_equals',
            'value': 'testString',
        }
        # Construct a dict representation of a RuleParameter model
        rule_parameter_model = {
            'name': 'hard_quota',
            'display_name': 'The Cloud Object Storage bucket quota.',
            'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
            'type': 'numeric',
        }
        # Construct a dict representation of a Import model
        import_model = {
            'parameters': [rule_parameter_model],
        }

        response = self.security_and_compliance_center_api_service.replace_rule(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            rule_id=rule_id_link,
            if_match=e_tag_link,
            description='Example rule',
            target=rule_target_prototype_model,
            required_config=required_config_model,
            version='1.0.1',
            import_=import_model,
            labels=[],
        )

        assert response.get_status_code() == 200
        rule = response.get_result()
        assert rule is not None

    @needscredentials
    def test_list_services(self):
        response = self.security_and_compliance_center_api_service.list_services()

        assert response.get_status_code() == 200
        service_collection = response.get_result()
        assert service_collection is not None

    @needscredentials
    def test_get_service(self):
        response = self.security_and_compliance_center_api_service.get_service(
            services_name='cloud-object-storage',
        )

        assert response.get_status_code() == 200
        service = response.get_result()
        assert service is not None

    @needscredentials
    def test_delete_profile_attachment(self):
        response = self.security_and_compliance_center_api_service.delete_profile_attachment(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            attachment_id=attachment_id_link,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile_attachment = response.get_result()
        assert profile_attachment is not None

    @needscredentials
    def test_delete_custom_control_library(self):
        response = self.security_and_compliance_center_api_service.delete_custom_control_library(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            control_library_id=control_library_id_link,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        control_library = response.get_result()
        assert control_library is not None

    @needscredentials
    def test_delete_custom_profile(self):
        response = self.security_and_compliance_center_api_service.delete_custom_profile(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            profile_id=profile_id_link,
            account_id=account_id_for_report_link,
        )

        assert response.get_status_code() == 200
        profile = response.get_result()
        assert profile is not None

    @needscredentials
    def test_delete_subscope(self):
        response = self.security_and_compliance_center_api_service.delete_subscope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
            subscope_id=sub_scope_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_scope(self):
        response = self.security_and_compliance_center_api_service.delete_scope(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            scope_id=scope_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_target(self):
        response = self.security_and_compliance_center_api_service.delete_target(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            target_id=target_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_provider_type_instance(self):
        response = self.security_and_compliance_center_api_service.delete_provider_type_instance(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            provider_type_id='3e25966275dccfa2c3a34786919c5af7',
            provider_type_instance_id=provider_type_instance_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_rule(self):
        response = self.security_and_compliance_center_api_service.delete_rule(
            instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            rule_id=rule_id_link,
        )

        assert response.get_status_code() == 204
