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
Examples for SecurityAndComplianceCenterApiV3
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import os
import pytest
from ibm_scc.security_and_compliance_center_api_v3 import *

#
# This file provides an example of how to use the Security and Compliance Center API service.
#
# The following configuration properties are assumed to be defined:
# SECURITY_AND_COMPLIANCE_CENTER_API_URL=<service base url>
# SECURITY_AND_COMPLIANCE_CENTER_API_AUTH_TYPE=iam
# SECURITY_AND_COMPLIANCE_CENTER_API_APIKEY=<IAM apikey>
# SECURITY_AND_COMPLIANCE_CENTER_API_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'security_and_compliance_center_api_v3.env'

security_and_compliance_center_api_service = None

config = None

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


##############################################################################
# Start of Examples for Service: SecurityAndComplianceCenterApiV3
##############################################################################
# region
class TestSecurityAndComplianceCenterApiV3Examples:
    """
    Example Test Class for SecurityAndComplianceCenterApiV3
    """

    @classmethod
    def setup_class(cls):
        global security_and_compliance_center_api_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            security_and_compliance_center_api_service = SecurityAndComplianceCenterApiV3.new_instance(
            )

            # end-common
            assert security_and_compliance_center_api_service is not None

            # Load the configuration
            global config
            config = read_external_sources(SecurityAndComplianceCenterApiV3.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_settings_example(self):
        """
        get_settings request example
        """
        try:
            global event_notifications_crn_for_update_settings_link
            global object_storage_crn_for_update_settings_link
            global object_storage_bucket_for_update_settings_link
            global object_storage_location_for_update_settings_link

            print('\nget_settings() result:')

            # begin-get_settings

            response = security_and_compliance_center_api_service.get_settings(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            )
            settings = response.get_result()

            print(json.dumps(settings, indent=2))

            # end-get_settings

            event_notifications_crn_for_update_settings_link = settings['event_notifications']['instance_crn']
            object_storage_crn_for_update_settings_link = settings['object_storage']['instance_crn']
            object_storage_bucket_for_update_settings_link = settings['object_storage']['bucket']
            object_storage_location_for_update_settings_link = settings['object_storage']['bucket_location']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_settings_example(self):
        """
        update_settings request example
        """
        try:
            print('\nupdate_settings() result:')

            # begin-update_settings

            object_storage_prototype_model = {
                'bucket': 'px-scan-results',
                'instance_crn': 'crn:v1:staging:public:cloud-object-storage:global:a/ff88f007f9ff4622aac4fbc0eda36255:7199ae60-a214-4dd8-9bf7-ce571de49d01::',
            }

            event_notifications_prototype_model = {
                'instance_crn': 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::',
                'source_description': 'This source is used for integration with IBM Cloud Security and Compliance Center.',
                'source_name': 'scc-sdk-integration',
            }

            response = security_and_compliance_center_api_service.update_settings(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                object_storage=object_storage_prototype_model,
                event_notifications=event_notifications_prototype_model,
            )
            settings = response.get_result()

            print(json.dumps(settings, indent=2))

            # end-update_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_post_test_event_example(self):
        """
        post_test_event request example
        """
        try:
            print('\npost_test_event() result:')

            # begin-post_test_event

            response = security_and_compliance_center_api_service.post_test_event(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            )
            test_event = response.get_result()

            print(json.dumps(test_event, indent=2))

            # end-post_test_event

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_instance_attachments_example(self):
        """
        list_instance_attachments request example
        """
        try:
            print('\nlist_instance_attachments() result:')

            # begin-list_instance_attachments

            all_results = []
            pager = InstanceAttachmentsPager(
                client=security_and_compliance_center_api_service,
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

            print(json.dumps(all_results, indent=2))

            # end-list_instance_attachments
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_profile_attachment_example(self):
        """
        create_profile_attachment request example
        """
        try:
            global attachment_id_link

            print('\ncreate_profile_attachment() result:')

            # begin-create_profile_attachment
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

            attachment_notifications_controls_model = {
                'threshold_limit': 15,
                'failed_control_ids': [],
            }

            attachment_notifications_model = {
                'enabled': True,
                'controls': attachment_notifications_controls_model,
            }

            multi_cloud_scope_payload_model = {
                'id': '8baad3b5-2e69-4027-9967-efac19508e1c',
            }

            profile_attachment_base_model = {
                'attachment_parameters': parameter_list,
                'description': 'This is a profile attachment targeting IBM CIS Foundation using a SDK',
                'name': 'Profile Attachment for IBM CIS Foundation SDK test',
                'notifications': attachment_notifications_model,
                'schedule': 'daily',
                'scope': [multi_cloud_scope_payload_model],
                'status': 'disabled',

            }

            response = security_and_compliance_center_api_service.create_profile_attachment(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
                new_attachments=[profile_attachment_base_model],
                new_profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3',
                account_id=account_id_for_report_link,
            )
            profile_attachment_response = response.get_result()

            print(json.dumps(profile_attachment_response, indent=2))

            # end-create_profile_attachment
            attachment_id_link = profile_attachment_response['attachments'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_profile_attachment_example(self):
        """
        get_profile_attachment request example
        """
        try:
            print('\nget_profile_attachment() result:')

            # begin-get_profile_attachment

            response = security_and_compliance_center_api_service.get_profile_attachment(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
                attachment_id=attachment_id_link,
            )
            profile_attachment = response.get_result()

            print(json.dumps(profile_attachment, indent=2))

            # end-get_profile_attachment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_profile_attachment_example(self):
        """
        replace_profile_attachment request example
        """
        try:
            print('\nreplace_profile_attachment() result:')

            # begin-replace_profile_attachment

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

            attachment_notifications_controls_model = {
                'threshold_limit': 15,
                'failed_control_ids': [],
            }

            attachment_notifications_model = {
                'enabled': True,
                'controls': attachment_notifications_controls_model,
            }

            multi_cloud_scope_payload_model = {
                'id': '8baad3b5-2e69-4027-9967-efac19508e1c',
            }

            response = security_and_compliance_center_api_service.replace_profile_attachment(
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
                account_id=account_id_for_report_link,
            )
            profile_attachment = response.get_result()

            print(json.dumps(profile_attachment, indent=2))

            # end-replace_profile_attachment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_upgrade_attachment_example(self):
        """
        upgrade_attachment request example
        """
        try:
            print('\nupgrade_attachment() result:')

            # begin-upgrade_attachment

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

            response = security_and_compliance_center_api_service.upgrade_attachment(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
                attachment_id=attachment_id_link,
                attachment_parameters=parameter_list,
                account_id=account_id_for_report_link,
            )
            profile_attachment = response.get_result()

            print(json.dumps(profile_attachment, indent=2))

            # end-upgrade_attachment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_scan_example(self):
        """
        create_scan request example
        """
        try:
            print('\ncreate_scan() result:')

            # begin-create_scan

            response = security_and_compliance_center_api_service.create_scan(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                attachment_id='4deb572c-9f37-4126-9cc0-d550672533cb',
            )
            create_scan_response = response.get_result()

            print(json.dumps(create_scan_response, indent=2))

            # end-create_scan

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_control_library_example(self):
        """
        create_control_library request example
        """
        try:
            global control_library_id_link

            print('\ncreate_control_library() result:')

            # begin-create_control_library

            assessment_prototype_model = {
                'assessment_id': 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e',
                'assessment_description': 'This rule will check on regulation',
            }

            control_specification_prototype_model = {
                'component_id': 'apprapp',
                'environment': 'ibm-cloud',
                'control_specification_description': 'This field is used to describe a control specification',
                'assessments': [assessment_prototype_model],
            }

            control_doc_model = {
            }

            control_prototype_model = {
                'control_name': 'security',
                'control_description': 'This is a description of a control',
                'control_category': 'test-control',
                'control_requirement': True,
                'control_parent': 'testString',
                'control_specifications': [control_specification_prototype_model],
                'control_docs': control_doc_model,
                'status': 'disabled',
            }

            response = security_and_compliance_center_api_service.create_control_library(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                control_library_name='custom control library from SDK',
                control_library_description='This is a custom control library made from the SDK test framework',
                control_library_type='custom',
                control_library_version='0.0.1',
                controls=[control_prototype_model],
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-create_control_library

            control_library_id_link = control_library['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_control_libraries_example(self):
        """
        list_control_libraries request example
        """
        try:
            print('\nlist_control_libraries() result:')

            # begin-list_control_libraries

            all_results = []
            pager = ControlLibrariesPager(
                client=security_and_compliance_center_api_service,
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                account_id=account_id_for_report_link,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_control_libraries
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_custom_control_library_example(self):
        """
        replace_custom_control_library request example
        """
        try:
            print('\nreplace_custom_control_library() result:')

            # begin-replace_custom_control_library

            assessment_prototype_model = {
                'assessment_id': 'rule-d1bd9f3f-bee1-46c5-9533-da8bba9eed4e',
                'assessment_description': 'This rule will check on regulation',
            }

            control_specification_prototype_model = {
                'component_id': 'apprapp',
                'environment': 'ibm-cloud',
                'control_specification_description': 'This field is used to describe a control specification',
                'assessments': [assessment_prototype_model],
            }

            control_prototype_model = {
                'control_name': 'security',
                'control_description': 'This is a description of a control',
                'control_category': 'test-control',
                'control_requirement': True,
                'control_parent': '',
                'control_specifications': [control_specification_prototype_model],
                'status': 'enabled',
            }

            response = security_and_compliance_center_api_service.replace_custom_control_library(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                control_library_id=control_library_id_link,
                control_library_name='custom control library from SDK',
                control_library_description='This is a custom control library made from the SDK test framework',
                control_library_type='custom',
                control_library_version='0.0.2',
                controls=[control_prototype_model],
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-replace_custom_control_library

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_control_library_example(self):
        """
        get_control_library request example
        """
        try:
            print('\nget_control_library() result:')

            # begin-get_control_library

            response = security_and_compliance_center_api_service.get_control_library(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                control_library_id=control_library_id_link,
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-get_control_library

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_profile_example(self):
        """
        create_profile request example
        """
        try:
            global profile_id_link

            print('\ncreate_profile() result:')

            # begin-create_profile
            profile_controls_prototype_model0 = {
                'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
                'control_id': '2ce21ba3-0548-49a3-88e2-1122632218f4',
            }

            profile_controls_prototype_model1 = {
                'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
                'control_id': 'bdc5fdab-6934-461c-8bb1-9af7ed8e8d33',
            }

            profile_controls_prototype_model2 = {
                'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
                'control_id': '60dae3b5-6104-4b3e-bac7-26cc7b741aca',
            }

            default_parameters_model = {
                'assessment_type': 'automated',
                'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
                'parameter_name': 'tls_version',
                'parameter_default_value': '["1.2","1.3"]',
                'parameter_display_name': 'IBM Cloud Internet Services TLS version',
                'parameter_type': 'string_list',
            }

            response = security_and_compliance_center_api_service.create_profile(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_name='Example Profile',
                profile_version='0.0.1',
                controls=[profile_controls_prototype_model0, profile_controls_prototype_model1,
                          profile_controls_prototype_model2],
                default_parameters=[default_parameters_model],
                profile_description='This profile is created as an example of the SDK gen',
                latest=True,
                account_id=account_id_for_report_link
            )
            profile = response.get_result()
            print(json.dumps(profile, indent=2))

            # end-create_profile
            profile_id_link = profile['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profiles_example(self):
        """
        list_profiles request example
        """
        try:
            print('\nlist_profiles() result:')

            # begin-list_profiles

            all_results = []
            pager = ProfilesPager(
                client=security_and_compliance_center_api_service,
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                account_id=account_id_for_report_link,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_profiles
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_profile_example(self):
        """
        replace_profile request example
        """
        try:
            print('\nreplace_profile() result:')

            # begin-replace_profile
            profile_controls_model0 = {
                'control_requirement': True,
                'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
                'control_id': '2ce21ba3-0548-49a3-88e2-1122632218f4',
            }

            profile_controls_model1 = {
                'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
                'control_id': 'bdc5fdab-6934-461c-8bb1-9af7ed8e8d33',
            }

            profile_controls_model2 = {
                'control_library_id': 'a046fb6b-aba5-4646-b190-a2c76241e7af',
                'control_id': '60dae3b5-6104-4b3e-bac7-26cc7b741aca',
            }

            default_parameters_model = {
                'assessment_type': 'automated',
                'assessment_id': 'rule-e16fcfea-fe21-4d30-a721-423611481fea',
                'parameter_name': 'tls_version',
                'parameter_default_value': '["1.2","1.3"]',
                'parameter_display_name': 'IBM Cloud Internet Services TLS version',
                'parameter_type': 'string_list',
            }

            response = security_and_compliance_center_api_service.replace_profile(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id=profile_id_link,
                new_profile_type='custom',
                new_controls=[profile_controls_model0, profile_controls_model1, profile_controls_model2],
                new_default_parameters=[default_parameters_model],
                new_profile_name='Example Profile Updated',
                new_profile_description='This profile has been updated',
                new_profile_version='0.0.2',
                new_latest=True,
                account_id=account_id_for_report_link
            )
            profile = response.get_result()
            print(json.dumps(profile, indent=2))

            # end-replace_profile
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_profile_example(self):
        """
        get_profile request example
        """
        try:
            print('\nget_profile() result:')

            # begin-get_profile

            response = security_and_compliance_center_api_service.get_profile(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id=profile_id_link,
            )
            profile = response.get_result()

            print(json.dumps(profile, indent=2))

            # end-get_profile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_profile_parameters_example(self):
        """
        replace_profile_parameters request example
        """
        try:
            print('\nreplace_profile_parameters() result:')

            # begin-replace_profile_parameters

            default_parameters_model = {
            }

            response = security_and_compliance_center_api_service.replace_profile_parameters(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id=profile_id_link,
                default_parameters=[default_parameters_model],
            )
            profile_default_parameters_response = response.get_result()

            print(json.dumps(profile_default_parameters_response, indent=2))

            # end-replace_profile_parameters

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profile_parameters_example(self):
        """
        list_profile_parameters request example
        """
        try:
            print('\nlist_profile_parameters() result:')

            # begin-list_profile_parameters

            response = security_and_compliance_center_api_service.list_profile_parameters(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id=profile_id_link,
            )
            profile_default_parameters_response = response.get_result()

            print(json.dumps(profile_default_parameters_response, indent=2))

            # end-list_profile_parameters

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_compare_profiles_example(self):
        """
        compare_profiles request example
        """
        try:
            print('\ncompare_profiles() result:')

            # begin-compare_profiles

            response = security_and_compliance_center_api_service.compare_profiles(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id='2f598907-970d-4d52-9071-5cc95912f55e',
            )
            compare_predefined_profiles_response = response.get_result()

            print(json.dumps(compare_predefined_profiles_response, indent=2))

            # end-compare_profiles

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_profile_attachments_example(self):
        """
        list_profile_attachments request example
        """
        try:
            print('\nlist_profile_attachments() result:')

            # begin-list_profile_attachments

            response = security_and_compliance_center_api_service.list_profile_attachments(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
            )
            profile_attachment_collection = response.get_result()

            print(json.dumps(profile_attachment_collection, indent=2))

            # end-list_profile_attachments

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_scope_example(self):
        """
        create_scope request example
        """
        try:
            global scope_id_link
            print('\ncreate_scope() result:')

            # begin-create_scope
            # Construct a dict representation of a ScopePropertyScopeAny model
            scope_property_model0 = {
                'name': 'scope_id',
                'value': 'ff88f007f9ff4622aac4fbc0eda36255',
            }

            scope_property_model1 = {
                'name': 'scope_type',
                'value': 'account',
            }

            response = security_and_compliance_center_api_service.create_scope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                name='ibm scope',
                description='The scope that is defined for IBM resources.',
                environment='ibm-cloud',
                properties=[scope_property_model0, scope_property_model1],
            )
            scope = response.get_result()
            print(json.dumps(scope, indent=2))

            # end-create_scope
            scope_id_link = scope['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_scopes_example(self):
        """
        list_scopes request example
        """
        try:
            print('\nlist_scopes() result:')

            # begin-list_scopes

            all_results = []
            pager = ScopesPager(
                client=security_and_compliance_center_api_service,
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

            print(json.dumps(all_results, indent=2))

            # end-list_scopes
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_scope_example(self):
        """
        update_scope request example
        """
        try:
            print('\nupdate_scope() result:')

            # begin-update_scope

            response = security_and_compliance_center_api_service.update_scope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
                name='updated name of scope',
                description='updated scope description',
            )
            scope = response.get_result()

            print(json.dumps(scope, indent=2))

            # end-update_scope

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_scope_example(self):
        """
        get_scope request example
        """
        try:
            print('\nget_scope() result:')

            # begin-get_scope

            response = security_and_compliance_center_api_service.get_scope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
            )
            scope = response.get_result()

            print(json.dumps(scope, indent=2))

            # end-get_scope

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_subscope_example(self):
        """
        create_subscope request example
        """
        try:
            global sub_scope_id_link
            print('\ncreate_subscope() result:')

            # begin-create_subscope
            scope_property_model0 = {
                'name': 'scope_id',
                'value': '1f689f08ec9b47b885c2659c17029581',
            }

            scope_property_model1 = {
                'name': 'scope_type',
                'value': 'account.resource_group',
            }

            scope_prototype_model = {
                'name': 'ibm subscope update',
                'description': 'The subscope that is defined for IBM resources.',
                'environment': 'ibm-cloud',
                'properties': [scope_property_model0, scope_property_model1],
            }

            response = security_and_compliance_center_api_service.create_subscope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
                subscopes=[scope_prototype_model],
            )
            sub_scope_response = response.get_result()
            print(json.dumps(sub_scope_response, indent=2))

            # end-create_subscope
            sub_scope_id_link = sub_scope_response['subscopes'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_subscopes_example(self):
        """
        list_subscopes request example
        """
        try:
            print('\nlist_subscopes() result:')

            # begin-list_subscopes

            all_results = []
            pager = SubscopesPager(
                client=security_and_compliance_center_api_service,
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

            print(json.dumps(all_results, indent=2))

            # end-list_subscopes
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_subscope_example(self):
        """
        get_subscope request example
        """
        try:
            print('\nget_subscope() result:')

            # begin-get_subscope

            response = security_and_compliance_center_api_service.get_subscope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
                subscope_id=sub_scope_id_link,
            )
            sub_scope = response.get_result()

            print(json.dumps(sub_scope, indent=2))

            # end-get_subscope

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_subscope_example(self):
        """
        update_subscope request example
        """
        try:
            print('\nupdate_subscope() result:')

            # begin-update_subscope

            response = security_and_compliance_center_api_service.update_subscope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
                subscope_id=sub_scope_id_link,
                name='updated name of scope',
                description='updated scope description',
            )
            sub_scope = response.get_result()

            print(json.dumps(sub_scope, indent=2))

            # end-update_subscope

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_target_example(self):
        """
        create_target request example
        """
        try:
            global target_id_link

            print('\ncreate_target() result:')

            # begin-create_target
            response = security_and_compliance_center_api_service.create_target(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                account_id='62ecf99b240144dea9125666249edfcb',
                trusted_profile_id='Profile-cb2c1829-9a8d-4218-b9cd-9f83fc814e54',
                name='Target for IBM account',
            )
            target = response.get_result()
            print(json.dumps(target, indent=2))

            # end-create_target
            target_id_link = target['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_targets_example(self):
        """
        list_targets request example
        """
        try:
            print('\nlist_targets() result:')

            # begin-list_targets

            response = security_and_compliance_center_api_service.list_targets(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            )
            target_collection = response.get_result()

            print(json.dumps(target_collection, indent=2))

            # end-list_targets

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_target_example(self):
        """
        get_target request example
        """
        try:
            print('\nget_target() result:')

            # begin-get_target

            response = security_and_compliance_center_api_service.get_target(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                target_id=target_id_link,
            )
            target = response.get_result()

            print(json.dumps(target, indent=2))

            # end-get_target

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_target_example(self):
        """
        replace_target request example
        """
        try:
            print('\nreplace_target() result:')

            # begin-replace_target
            response = security_and_compliance_center_api_service.replace_target(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                target_id=target_id_link,
                account_id='62ecf99b240144dea9125666249edfcb',
                trusted_profile_id='Profile-cb2c1829-9a8d-4218-b9cd-9f83fc814e54',
                name='Updated Target Name',
            )
            target = response.get_result()
            print(json.dumps(target, indent=2))

            # end-replace_target
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_provider_type_instance_example(self):
        """
        create_provider_type_instance request example
        """
        try:
            global provider_type_instance_id_link

            print('\ncreate_provider_type_instance() result:')

            # begin-create_provider_type_instance
            response = security_and_compliance_center_api_service.create_provider_type_instance(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                provider_type_id='3e25966275dccfa2c3a34786919c5af7',
                name='Caveonix-instance-1',
                attributes={},
            )
            provider_type_instance = response.get_result()
            print(json.dumps(provider_type_instance, indent=2))

            # end-create_provider_type_instance
            provider_type_instance_id_link = provider_type_instance['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_provider_type_instances_example(self):
        """
        list_provider_type_instances request example
        """
        try:
            print('\nlist_provider_type_instances() result:')

            # begin-list_provider_type_instances

            response = security_and_compliance_center_api_service.list_provider_type_instances(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                provider_type_id='3e25966275dccfa2c3a34786919c5af7',
            )
            provider_type_instance_collection = response.get_result()

            print(json.dumps(provider_type_instance_collection, indent=2))

            # end-list_provider_type_instances

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_provider_type_instance_example(self):
        """
        get_provider_type_instance request example
        """
        try:
            print('\nget_provider_type_instance() result:')

            # begin-get_provider_type_instance

            response = security_and_compliance_center_api_service.get_provider_type_instance(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                provider_type_id='3e25966275dccfa2c3a34786919c5af7',
                provider_type_instance_id=provider_type_instance_id_link,
            )
            provider_type_instance = response.get_result()

            print(json.dumps(provider_type_instance, indent=2))

            # end-get_provider_type_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_provider_type_instance_example(self):
        """
        update_provider_type_instance request example
        """
        try:
            print('\nupdate_provider_type_instance() result:')

            # begin-update_provider_type_instance
            response = security_and_compliance_center_api_service.update_provider_type_instance(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                provider_type_id='3e25966275dccfa2c3a34786919c5af7',
                provider_type_instance_id=provider_type_instance_id_link,
                name='Caveonix-instance-1-update',
                attributes={},
            )
            provider_type_instance = response.get_result()
            print(json.dumps(provider_type_instance, indent=2))

            # end-update_provider_type_instance
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_provider_types_example(self):
        """
        list_provider_types request example
        """
        try:
            print('\nlist_provider_types() result:')

            # begin-list_provider_types

            response = security_and_compliance_center_api_service.list_provider_types(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            )
            provider_type_collection = response.get_result()

            print(json.dumps(provider_type_collection, indent=2))

            # end-list_provider_types

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_provider_type_by_id_example(self):
        """
        get_provider_type_by_id request example
        """
        try:
            print('\nget_provider_type_by_id() result:')

            # begin-get_provider_type_by_id

            response = security_and_compliance_center_api_service.get_provider_type_by_id(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                provider_type_id='3e25966275dccfa2c3a34786919c5af7',
            )
            provider_type = response.get_result()

            print(json.dumps(provider_type, indent=2))

            # end-get_provider_type_by_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_latest_reports_example(self):
        """
        get_latest_reports request example
        """
        try:
            global account_id_for_report_link
            global report_id_for_report_link
            global attachment_id_for_report_link
            global group_id_for_report_link
            global profile_id_for_report_link
            global type_for_report_link

            print('\nget_latest_reports() result:')

            # begin-get_latest_reports

            response = security_and_compliance_center_api_service.get_latest_reports(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            )
            report_latest = response.get_result()

            print(json.dumps(report_latest, indent=2))

            # end-get_latest_reports

            account_id_for_report_link = report_latest['reports'][0]['account']['id']
            report_id_for_report_link = report_latest['reports'][0]['id']
            attachment_id_for_report_link = report_latest['reports'][0]['attachment']['id']
            group_id_for_report_link = report_latest['reports'][0]['group_id']
            profile_id_for_report_link = report_latest['reports'][0]['profile']['id']
            type_for_report_link = report_latest['reports'][0]['type']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_reports_example(self):
        """
        list_reports request example
        """
        try:
            print('\nlist_reports() result:')

            # begin-list_reports
            all_results = []
            pager = ReportsPager(
                client=security_and_compliance_center_api_service,
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_attachment_id=attachment_id_for_report_link,
                group_id=group_id_for_report_link,
                report_profile_id=profile_id_for_report_link,
                type=type_for_report_link,
                limit=50,
                sort='profile_name',
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_reports
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_example(self):
        """
        get_report request example
        """
        try:
            print('\nget_report() result:')

            # begin-get_report

            response = security_and_compliance_center_api_service.get_report(
                report_id=report_id_for_report_link,
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
            )
            report = response.get_result()

            print(json.dumps(report, indent=2))

            # end-get_report

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_summary_example(self):
        """
        get_report_summary request example
        """
        try:
            print('\nget_report_summary() result:')

            # begin-get_report_summary

            response = security_and_compliance_center_api_service.get_report_summary(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
            )
            report_summary = response.get_result()

            print(json.dumps(report_summary, indent=2))

            # end-get_report_summary

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_download_file_example(self):
        """
        get_report_download_file request example
        """
        try:
            print('\nget_report_download_file() result:')

            # begin-get_report_download_file

            response = security_and_compliance_center_api_service.get_report_download_file(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
            )
            result = response.get_result()

            with open('/tmp/result.out', 'wb') as fp:
                fp.write(result)

            # end-get_report_download_file

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_controls_example(self):
        """
        get_report_controls request example
        """
        try:
            print('\nget_report_controls() result:')

            # begin-get_report_controls
            response = security_and_compliance_center_api_service.get_report_controls(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
                status='compliant',
            )
            report_controls = response.get_result()
            print(json.dumps(report_controls, indent=2))

            # end-get_report_controls
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_rule_example(self):
        """
        get_report_rule request example
        """
        try:
            print('\nget_report_rule() result:')

            # begin-get_report_rule

            response = security_and_compliance_center_api_service.get_report_rule(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
                rule_id='rule-61fa114a-2bb9-43fd-8068-b873b48bdf79',
            )
            rule_info = response.get_result()

            print(json.dumps(rule_info, indent=2))

            # end-get_report_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_report_evaluations_example(self):
        """
        list_report_evaluations request example
        """
        try:
            print('\nlist_report_evaluations() result:')

            # begin-list_report_evaluations
            all_results = []
            pager = ReportEvaluationsPager(
                client=security_and_compliance_center_api_service,
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
                status='failure',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_report_evaluations
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_report_resources_example(self):
        """
        list_report_resources request example
        """
        try:
            print('\nlist_report_resources() result:')

            # begin-list_report_resources

            all_results = []
            pager = ReportResourcesPager(
                client=security_and_compliance_center_api_service,
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

            print(json.dumps(all_results, indent=2))

            # end-list_report_resources
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_tags_example(self):
        """
        get_report_tags request example
        """
        try:
            print('\nget_report_tags() result:')

            # begin-get_report_tags

            response = security_and_compliance_center_api_service.get_report_tags(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
            )
            report_tags = response.get_result()

            print(json.dumps(report_tags, indent=2))

            # end-get_report_tags

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_violations_drift_example(self):
        """
        get_report_violations_drift request example
        """
        try:
            print('\nget_report_violations_drift() result:')

            # begin-get_report_violations_drift

            response = security_and_compliance_center_api_service.get_report_violations_drift(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
            )
            report_violations_drift = response.get_result()

            print(json.dumps(report_violations_drift, indent=2))

            # end-get_report_violations_drift

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_scan_reports_example(self):
        """
        list_scan_reports request example
        """
        try:
            global scan_id_for_scan_report_link

            print('\nlist_scan_reports() result:')

            # begin-list_scan_reports

            response = security_and_compliance_center_api_service.list_scan_reports(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
            )
            scan_report_collection = response.get_result()

            print(json.dumps(scan_report_collection, indent=2))

            # end-list_scan_reports

            scan_id_for_scan_report_link = scan_report_collection['scan_reports'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_scan_report_example(self):
        """
        create_scan_report request example
        """
        try:
            print('\ncreate_scan_report() result:')

            # begin-create_scan_report

            response = security_and_compliance_center_api_service.create_scan_report(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
                format='csv',
                scope_id='132009ff-b982-412e-a110-ad8797e10f84',
                subscope_id='c7ddcbcc-6a43-4ab3-b6a7-b2d8f65cd54a',
            )
            create_scan_report = response.get_result()

            print(json.dumps(create_scan_report, indent=2))

            # end-create_scan_report

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_scan_report_example(self):
        """
        get_scan_report request example
        """
        try:
            print('\nget_scan_report() result:')

            # begin-get_scan_report

            response = security_and_compliance_center_api_service.get_scan_report(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
                job_id=scan_id_for_scan_report_link,
            )
            scan_report = response.get_result()

            print(json.dumps(scan_report, indent=2))

            # end-get_scan_report

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_scan_report_download_file_example(self):
        """
        get_scan_report_download_file request example
        """
        try:
            print('\nget_scan_report_download_file() result:')

            # begin-get_scan_report_download_file

            response = security_and_compliance_center_api_service.get_scan_report_download_file(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                report_id=report_id_for_report_link,
                job_id=scan_id_for_scan_report_link,
            )
            result = response.get_result()

            with open('/tmp/result.out', 'wb') as fp:
                fp.write(result)

            # end-get_scan_report_download_file

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_rules_example(self):
        """
        list_rules request example
        """
        try:
            print('\nlist_rules() result:')

            # begin-list_rules

            all_results = []
            pager = RulesPager(
                client=security_and_compliance_center_api_service,
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

            print(json.dumps(all_results, indent=2))

            # end-list_rules
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_rule_example(self):
        """
        create_rule request example
        """
        try:
            global rule_id_link

            print('\ncreate_rule() result:')

            # begin-create_rule

            additional_target_attribute_model = {
                'name': 'location',
                'operator': 'string_equals',
                'value': 'us-east',
            }

            rule_target_prototype_model = {
                'service_name': 'cloud-object-storage',
                'resource_kind': 'bucket',
                'additional_target_attributes': [additional_target_attribute_model],
            }

            required_config_model = {
                'description': 'The Cloud Object Storage rule.',
                'property': 'testString',
                'operator': 'string_equals',
            }

            rule_parameter_model = {
                'name': 'hard_quota',
                'display_name': 'The Cloud Object Storage bucket quota.',
                'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
                'type': 'numeric',
            }

            import_model = {
                'parameters': [rule_parameter_model],
            }

            response = security_and_compliance_center_api_service.create_rule(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                description='Example rule',
                target=rule_target_prototype_model,
                required_config=required_config_model,
                version='1.0.0',
                import_=import_model,
                labels=[],
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-create_rule

            rule_id_link = rule['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_rule_example(self):
        """
        get_rule request example
        """
        try:
            global e_tag_link

            print('\nget_rule() result:')

            # begin-get_rule

            response = security_and_compliance_center_api_service.get_rule(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                rule_id=rule_id_link,
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-get_rule

            e_tag_link = response.get_headers().get('ETag')
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_rule_example(self):
        """
        replace_rule request example
        """
        try:
            print('\nreplace_rule() result:')

            # begin-replace_rule

            additional_target_attribute_model = {
                'name': 'location',
                'operator': 'string_equals',
                'value': 'us-south',
            }

            rule_target_prototype_model = {
                'service_name': 'cloud-object-storage',
                'resource_kind': 'bucket',
                'additional_target_attributes': [additional_target_attribute_model],
            }

            required_config_model = {
                'description': 'The Cloud Object Storage rule.',
                'property': 'testString',
                'operator': 'string_equals',
            }

            rule_parameter_model = {
                'name': 'hard_quota',
                'display_name': 'The Cloud Object Storage bucket quota.',
                'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
                'type': 'numeric',
            }

            import_model = {
                'parameters': [rule_parameter_model],
            }

            response = security_and_compliance_center_api_service.replace_rule(
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
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-replace_rule

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_services_example(self):
        """
        list_services request example
        """
        try:
            print('\nlist_services() result:')

            # begin-list_services

            response = security_and_compliance_center_api_service.list_services()
            service_collection = response.get_result()

            print(json.dumps(service_collection, indent=2))

            # end-list_services

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_service_example(self):
        """
        get_service request example
        """
        try:
            print('\nget_service() result:')

            # begin-get_service

            response = security_and_compliance_center_api_service.get_service(
                services_name='cloud-object-storage',
            )
            service = response.get_result()

            print(json.dumps(service, indent=2))

            # end-get_service

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_profile_attachment_example(self):
        """
        delete_profile_attachment request example
        """
        try:
            print('\ndelete_profile_attachment() result:')

            # begin-delete_profile_attachment

            response = security_and_compliance_center_api_service.delete_profile_attachment(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id='9c265b4a-4cdf-47f1-acd3-17b5808f7f3f',
                attachment_id=attachment_id_link,
            )
            profile_attachment = response.get_result()

            print(json.dumps(profile_attachment, indent=2))

            # end-delete_profile_attachment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_custom_control_library_example(self):
        """
        delete_custom_control_library request example
        """
        try:
            print('\ndelete_custom_control_library() result:')

            # begin-delete_custom_control_library

            response = security_and_compliance_center_api_service.delete_custom_control_library(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                control_library_id=control_library_id_link,
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-delete_custom_control_library

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_custom_profile_example(self):
        """
        delete_custom_profile request example
        """
        try:
            print('\ndelete_custom_profile() result:')

            # begin-delete_custom_profile

            response = security_and_compliance_center_api_service.delete_custom_profile(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                profile_id=profile_id_link,
            )
            profile = response.get_result()

            print(json.dumps(profile, indent=2))

            # end-delete_custom_profile

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_subscope_example(self):
        """
        delete_subscope request example
        """
        try:
            # begin-delete_subscope

            response = security_and_compliance_center_api_service.delete_subscope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
                subscope_id=sub_scope_id_link,
            )

            # end-delete_subscope
            print('\ndelete_subscope() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_scope_example(self):
        """
        delete_scope request example
        """
        try:
            # begin-delete_scope

            response = security_and_compliance_center_api_service.delete_scope(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                scope_id=scope_id_link,
            )

            # end-delete_scope
            print('\ndelete_scope() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_target_example(self):
        """
        delete_target request example
        """
        try:
            # begin-delete_target

            response = security_and_compliance_center_api_service.delete_target(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                target_id=target_id_link,
            )

            # end-delete_target
            print('\ndelete_target() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_provider_type_instance_example(self):
        """
        delete_provider_type_instance request example
        """
        try:
            # begin-delete_provider_type_instance

            response = security_and_compliance_center_api_service.delete_provider_type_instance(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                provider_type_id='3e25966275dccfa2c3a34786919c5af7',
                provider_type_instance_id=provider_type_instance_id_link,
            )

            # end-delete_provider_type_instance
            print('\ndelete_provider_type_instance() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_rule_example(self):
        """
        delete_rule request example
        """
        try:
            # begin-delete_rule

            response = security_and_compliance_center_api_service.delete_rule(
                instance_id='acd7032c-15a3-484f-bf5b-67d41534d940',
                rule_id=rule_id_link,
            )

            # end-delete_rule
            print('\ndelete_rule() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: SecurityAndComplianceCenterApiV3
##############################################################################
