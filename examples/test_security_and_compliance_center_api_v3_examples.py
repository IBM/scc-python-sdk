# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
provider_type_id_link = None
provider_type_instance_id_link = None
report_id_for_report_link = None
rule_id_link = None
type_for_report_link = None
account_id = None
instance_id = None
create_scan_attachment_id = None

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
            cls.account_id=config['ACCOUNTID']
            cls.instance_id = config['INSTANCEID']
            if cls.instance_id == "": print("Unable to load instanceID configuration property, skipping tests")
            cls.create_scan_attachment_id = config['ATTACHMENTID']
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
                x_correlation_id='1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5',
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

            target_model = {
                'service_name': 'cloud-object-storage',
                'resource_kind': 'bucket',
                'additional_target_attributes': [additional_target_attribute_model],
            }

            required_config_items_model = {
                'property': 'hard_quota',
                'operator': 'num_equals',
                'value': '${hard_quota}',
            }

            required_config_model = {
                'description': 'The Cloud Object Storage rule.',
                'and': [required_config_items_model],
            }

            parameter_model = {
                'name': 'hard_quota',
                'display_name': 'The Cloud Object Storage bucket quota.',
                'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
                'type': 'numeric',
            }

            import_model = {
                'parameters': [parameter_model],
            }

            response = security_and_compliance_center_api_service.create_rule(
                description='Example rule',
                target=target_model,
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
                rule_id=rule_id_link,
            )
            rule = response.get_result()

            print(json.dumps(rule, indent=2))

            # end-get_rule

            e_tag_link = response.get_headers().get('ETag')
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
                sort='profile_name',
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
    def test_update_settings_example(self):
        """
        update_settings request example
        """
        try:
            print('\nupdate_settings() result:')
            # begin-update_settings

            event_notifications_model = {
                'instance_crn': event_notifications_crn_for_update_settings_link,
                'source_description': 'This source is used for integration with IBM Cloud Security and Compliance Center.',
                'source_name': 'compliance',
            }

            object_storage_model = {
                'instance_crn': object_storage_crn_for_update_settings_link,
                'bucket': object_storage_bucket_for_update_settings_link,
                'bucket_location': object_storage_location_for_update_settings_link,
            }

            response = security_and_compliance_center_api_service.update_settings(
                event_notifications=event_notifications_model,
                object_storage=object_storage_model,
                x_correlation_id='1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5',
            )
            settings = response.get_result()

            print(json.dumps(settings, indent=2))

            # end-update_settings

        except ApiException as e:
            pytest.fail(str(e))

    # @needscredentials
    # def test_post_test_event_example(self):
    #     """
    #     post_test_event request example
    #     """
    #     try:
    #         print('\npost_test_event() result:')
    #         # begin-post_test_event

    #         response = security_and_compliance_center_api_service.post_test_event(
    #             x_correlation_id='1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5',
    #         )
    #         test_event = response.get_result()

    #         print(json.dumps(test_event, indent=2))

    #         # end-post_test_event

    #     except ApiException as e:
    #         pytest.fail(str(e))

    @needscredentials
    def test_create_custom_control_library_example(self):
        """
        create_custom_control_library request example
        """
        try:
            global control_library_id_link
            print('\ncreate_custom_control_library() result:')
            # begin-create_custom_control_library

            parameter_info_model = {
                'parameter_name': 'session_invalidation_in_seconds',
                'parameter_display_name': 'Sign out due to inactivity in seconds',
                'parameter_type': 'numeric',
            }

            implementation_model = {
                'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
                'assessment_method': 'ibm-cloud-rule',
                'assessment_type': 'automated',
                'assessment_description': 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services',
                'parameters': [parameter_info_model],
            }

            control_specifications_model = {
                'control_specification_id': '5c7d6f88-a92f-4734-9b49-bd22b0900184',
                'component_id': 'iam-identity',
                'environment': 'ibm-cloud',
                'control_specification_description': 'IBM cloud',
                'assessments': [implementation_model],
            }

            control_docs_model = {
                'control_docs_id': 'sc-7',
                'control_docs_type': 'ibm-cloud',
            }

            controls_in_control_lib_model = {
                'control_name': 'SC-7',
                'control_id': '1fa45e17-9322-4e6c-bbd6-1c51db08e790',
                'control_description': 'Boundary Protection',
                'control_category': 'System and Communications Protection',
                'control_parent': '',
                'control_tags': ['1fa45e17-9322-4e6c-bbd6-1c51db08e790'],
                'control_specifications': [control_specifications_model],
                'control_docs': control_docs_model,
                'control_requirement': True,
            }

            response = security_and_compliance_center_api_service.create_custom_control_library(
                control_library_name='IBM Cloud for Financial Services',
                control_library_description='IBM Cloud for Financial Services',
                control_library_type='custom',
                controls=[controls_in_control_lib_model],
                control_library_version='1.0.0',
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-create_custom_control_library

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
                x_correlation_id='testString',
                x_request_id='testString',
                limit=50,
                control_library_type='custom',
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
    def test_get_control_library_example(self):
        """
        get_control_library request example
        """
        try:
            print('\nget_control_library() result:')
            # begin-get_control_library

            response = security_and_compliance_center_api_service.get_control_library(
                control_libraries_id=control_library_id_link,
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-get_control_library

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

            parameter_info_model = {
                'parameter_name': 'session_invalidation_in_seconds',
                'parameter_display_name': 'Sign out due to inactivity in seconds',
                'parameter_type': 'numeric',
            }

            implementation_model = {
                'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
                'assessment_method': 'ibm-cloud-rule',
                'assessment_type': 'automated',
                'assessment_description': 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services',
                'parameters': [parameter_info_model],
            }

            control_specifications_model = {
                'control_specification_id': '5c7d6f88-a92f-4734-9b49-bd22b0900184',
                'responsibility': 'user',
                'component_id': 'iam-identity',
                'environment': 'ibm-cloud',
                'control_specification_description': 'IBM cloud',
                'assessments': [implementation_model],
            }

            control_docs_model = {
                'control_docs_id': 'sc-7',
                'control_docs_type': 'ibm-cloud',
            }

            controls_in_control_lib_model = {
                'control_name': 'SC-7',
                'control_id': '1fa45e17-9322-4e6c-bbd6-1c51db08e790',
                'control_description': 'Boundary Protection',
                'control_category': 'System and Communications Protection',
                'control_parent': '',
                'control_tags': ['1fa45e17-9322-4e6c-bbd6-1c51db08e790'],
                'control_specifications': [control_specifications_model],
                'control_docs': control_docs_model,
                'control_requirement': True,
            }

            response = security_and_compliance_center_api_service.replace_custom_control_library(
                control_libraries_id=control_library_id_link,
                control_library_name='IBM Cloud for Financial Services',
                control_library_description='IBM Cloud for Financial Services',
                control_library_type='custom',
                control_library_version='1.1.0',
                controls=[controls_in_control_lib_model],
            )
            control_library = response.get_result()

            print(json.dumps(control_library, indent=2))

            # end-replace_custom_control_library

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

            profile_controls_prototype_model = {
                'control_library_id': control_library_id_link,
                'control_id': '1fa45e17-9322-4e6c-bbd6-1c51db08e790',
            }

            default_parameters_prototype_model = {
                'assessment_type': 'Automated',
                'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
                'parameter_name': 'session_invalidation_in_seconds',
                'parameter_default_value': '120',
                'parameter_display_name': 'Sign out due to inactivity in seconds',
                'parameter_type': 'numeric',
            }

            response = security_and_compliance_center_api_service.create_profile(
                profile_name='test_profile1',
                profile_description='test_description1',
                profile_type='custom',
                controls=[profile_controls_prototype_model],
                default_parameters=[default_parameters_prototype_model],
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
                x_correlation_id='testString',
                x_request_id='testString',
                limit=10,
                profile_type='custom',
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
    def test_get_profile_example(self):
        """
        get_profile request example
        """
        try:
            print('\nget_profile() result:')
            # begin-get_profile

            response = security_and_compliance_center_api_service.get_profile(
                profiles_id=profile_id_link,
            )
            profile = response.get_result()

            print(json.dumps(profile, indent=2))

            # end-get_profile

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

            profile_controls_prototype_model = {
                'control_library_id': control_library_id_link,
                'control_id': '1fa45e17-9322-4e6c-bbd6-1c51db08e790',
            }

            default_parameters_prototype_model = {
                'assessment_type': 'Automated',
                'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
                'parameter_name': 'session_invalidation_in_seconds',
                'parameter_default_value': '120',
                'parameter_display_name': 'Sign out due to inactivity in seconds',
                'parameter_type': 'numeric',
            }

            response = security_and_compliance_center_api_service.replace_profile(
                profiles_id=profile_id_link,
                profile_name='test_profile1',
                profile_description='test_description1',
                profile_type='custom',
                controls=[profile_controls_prototype_model],
                default_parameters=[default_parameters_prototype_model],
            )
            profile = response.get_result()

            print(json.dumps(profile, indent=2))

            # end-replace_profile

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

            response = security_and_compliance_center_api_service.list_rules(
                type='system_defined',
            )
            rules_page_base = response.get_result()

            print(json.dumps(rules_page_base, indent=2))

            # end-list_rules

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

            target_model = {
                'service_name': 'cloud-object-storage',
                'service_display_name': 'Cloud Object Storage',
                'resource_kind': 'bucket',
                'additional_target_attributes': [additional_target_attribute_model],
            }

            required_config_items_model = {
                'property': 'hard_quota',
                'operator': 'num_equals',
                'value': '${hard_quota}',
            }

            required_config_model = {
                'description': 'The Cloud Object Storage rule.',
                'and': [required_config_items_model],
            }

            parameter_model = {
                'name': 'hard_quota',
                'display_name': 'The Cloud Object Storage bucket quota.',
                'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
                'type': 'numeric',
            }

            import_model = {
                'parameters': [parameter_model],
            }

            response = security_and_compliance_center_api_service.replace_rule(
                rule_id=rule_id_link,
                if_match=e_tag_link,
                description='Example rule',
                target=target_model,
                required_config=required_config_model,
                type='user_defined',
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
    def test_create_attachment_example(self):
        """
        create_attachment request example
        """
        try:
            global attachment_id_link
            print('\ncreate_attachment() result:')
            # begin-create_attachment
            property_scope_id = {
                'name': 'scope_id',
                'value': self.account_id,
            }
            property_scope_type = {
                'name': 'scope_type',
                'value': "account",
            }

            multi_cloud_scope_model = {
                'environment': 'ibm-cloud',
                'properties': [property_scope_id, property_scope_type],
            }

            failed_controls_model = {
                'threshold_limit': 15,
                'failed_control_ids': [],
            }

            attachments_notifications_prototype_model = {
                'enabled': False,
                'controls': failed_controls_model,
            }

            attachment_parameter_prototype_model = {
                'assessment_type': 'Automated',
                'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
                'parameter_name': 'session_invalidation_in_seconds',
                'parameter_value': '120',
                'parameter_display_name': 'Sign out due to inactivity in seconds',
                'parameter_type': 'numeric',
            }

            attachments_prototype_model = {
                'name': 'account-0d8c3805dfea40aa8ad02265a18eb12b',
                'description': 'Test description',
                'scope': [multi_cloud_scope_model],
                'status': 'enabled',
                'schedule': 'every_30_days',
                'notifications': attachments_notifications_prototype_model,
                'attachment_parameters': [attachment_parameter_prototype_model],
            }

            response = security_and_compliance_center_api_service.create_attachment(
                profiles_id=profile_id_link,
                attachments=[attachments_prototype_model],
            )
            attachment_prototype = response.get_result()

            print(json.dumps(attachment_prototype, indent=2))

            # end-create_attachment

            attachment_id_link = attachment_prototype['attachments'][0]['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_attachments_example(self):
        """
        list_attachments request example
        """
        try:
            print('\nlist_attachments() result:')
            # begin-list_attachments

            all_results = []
            pager = AttachmentsPager(
                client=security_and_compliance_center_api_service,
                profiles_id=profile_id_link,
                x_correlation_id='testString',
                x_request_id='testString',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_attachments
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
                attachment_id=attachment_id_link,
                profiles_id=profile_id_link,
            )
            attachment_item = response.get_result()

            print(json.dumps(attachment_item, indent=2))

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
            property_scope_id = {
                'name': 'scope_id',
                'value': self.account_id,
            }
            property_scope_type = {
                'name': 'scope_type',
                'value': "account",
            }
            multi_cloud_scope_model = {
                'environment': 'ibm-cloud',
                'properties': [property_scope_id, property_scope_type],
            }

            failed_controls_model = {
                'threshold_limit': 15,
                'failed_control_ids': [],
            }

            attachments_notifications_prototype_model = {
                'enabled': False,
                'controls': failed_controls_model,
            }

            attachment_parameter_prototype_model = {
                'assessment_type': 'Automated',
                'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
                'parameter_name': 'session_invalidation_in_seconds',
                'parameter_value': '120',
                'parameter_display_name': 'Sign out due to inactivity in seconds',
                'parameter_type': 'numeric',
            }

            response = security_and_compliance_center_api_service.replace_profile_attachment(
                attachment_id=attachment_id_link,
                profiles_id=profile_id_link,
                scope=[multi_cloud_scope_model],
                status='enabled',
                schedule='every_30_days',
                notifications=attachments_notifications_prototype_model,
                attachment_parameters=[attachment_parameter_prototype_model],
                name='account-0d8c3805dfea40aa8ad02265a18eb12b',
                description='Test description',
            )
            attachment_item = response.get_result()

            print(json.dumps(attachment_item, indent=2))

            # end-replace_profile_attachment

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
                attachment_id=attachment_id_link,
            )
            scan = response.get_result()
            
            print(json.dumps(scan, indent=2))

            # end-create_scan

        except ApiException as e:
            if "Another scan is currently in progress" in str(e):
                return
            else:
                pytest.fail(str(e))

    @needscredentials
    def test_list_attachments_account_example(self):
        """
        list_attachments_account request example
        """
        try:
            print('\nlist_attachments_account() result:')
            # begin-list_attachments_account

            all_results = []
            pager = AttachmentsAccountPager(
                client=security_and_compliance_center_api_service,
                x_correlation_id='testString',
                x_request_id='testString',
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_attachments_account
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
                x_correlation_id='testString',
                x_request_id='testString',
                attachment_id=attachment_id_for_report_link,
                group_id=group_id_for_report_link,
                profile_id=profile_id_for_report_link,
                type=type_for_report_link,
                limit=10,
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
                report_id=report_id_for_report_link,
            )
            report_summary = response.get_result()

            print(json.dumps(report_summary, indent=2))

            # end-get_report_summary

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_report_evaluation_example(self):
        """
        get_report_evaluation request example
        """
        try:
            print('\nget_report_evaluation() result:')
            # begin-get_report_evaluation

            response = security_and_compliance_center_api_service.get_report_evaluation(
                report_id=report_id_for_report_link,
            )
            result = response.get_result()
            with open('/tmp/result.out', 'wb') as fp:
                fp.write(str(result).encode('utf-8'))

            # end-get_report_evaluation

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
                report_id=report_id_for_report_link,
                status='compliant',
            )
            report_controls = response.get_result()

            print(json.dumps(report_controls, indent=2))

            # end-get_report_controls

        except ApiException as e:
            pytest.fail(str(e))

    # @needscredentials
    # def test_get_report_rule_example(self):
    #     """
    #     get_report_rule request example
    #     """
    #     try:
    #         print('\nget_report_rule() result:')
    #         # begin-get_report_rule

    #         response = security_and_compliance_center_api_service.get_report_rule(
    #             report_id=report_id_for_report_link,
    #             rule_id='rule-8d444f8c-fd1d-48de-bcaa-f43732568761',
    #         )
    #         rule_info = response.get_result()

    #         print(json.dumps(rule_info, indent=2))

    #         # end-get_report_rule

    #     except ApiException as e:
    #         pytest.fail(str(e))

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
                report_id=report_id_for_report_link,
                x_correlation_id='testString',
                x_request_id='testString',
                assessment_id='testString',
                component_id='testString',
                target_id='testString',
                target_name='testString',
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
                report_id=report_id_for_report_link,
                x_correlation_id='testString',
                x_request_id='testString',
                id='testString',
                resource_name='testString',
                account_id=account_id_for_report_link,
                component_id='testString',
                status='compliant',
                sort='account_id',
                limit=10,
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
                report_id=report_id_for_report_link,
            )
            report_violations_drift = response.get_result()

            print(json.dumps(report_violations_drift, indent=2))

            # end-get_report_violations_drift

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_provider_types_example(self):
        """
        list_provider_types request example
        """
        try:
            global provider_type_id_link
            print('\nlist_provider_types() result:')
            # begin-list_provider_types

            response = security_and_compliance_center_api_service.list_provider_types()
            provider_types_collection = response.get_result()

            print(json.dumps(provider_types_collection, indent=2))

            # end-list_provider_types

            provider_type_id_link = provider_types_collection['provider_types'][1]['id']
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
                provider_type_id=provider_type_id_link,
            )
            provider_type_item = response.get_result()

            print(json.dumps(provider_type_item, indent=2))

            # end-get_provider_type_by_id

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
                provider_type_id=provider_type_id_link,
            )
            provider_type_instances_response = response.get_result()

            print(json.dumps(provider_type_instances_response, indent=2))

            # end-list_provider_type_instances

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
                provider_type_id=provider_type_id_link,
                name='workload-protection-instance-1',
                attributes={'wp_crn':'crn:v1:staging:public:sysdig-secure:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:0df4004c-fb74-483b-97be-dd9bd35af4d8::'},
                x_correlation_id='testString',
                x_request_id='testString',
            )
            provider_type_instance_item = response.get_result()

            print(json.dumps(provider_type_instance_item, indent=2))

            # end-create_provider_type_instance

            provider_type_instance_id_link = provider_type_instance_item['id']
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
                provider_type_id=provider_type_id_link,
                provider_type_instance_id=provider_type_instance_id_link,
            )
            provider_type_instance_item = response.get_result()

            print(json.dumps(provider_type_instance_item, indent=2))

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
                provider_type_id=provider_type_id_link,
                provider_type_instance_id=provider_type_instance_id_link,
                name='workload-protection-instance-1',
                attributes={'wp_crn':'crn:v1:staging:public:sysdig-secure:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:0df4004c-fb74-483b-97be-dd9bd35af4d8::'},
                x_correlation_id='testString',
                x_request_id='testString',
            )
            provider_type_instance_item = response.get_result()

            print(json.dumps(provider_type_instance_item, indent=2))

            # end-update_provider_type_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_provider_types_instances_example(self):
        """
        get_provider_types_instances request example
        """
        try:
            print('\nget_provider_types_instances() result:')
            # begin-get_provider_types_instances

            response = security_and_compliance_center_api_service.get_provider_types_instances()
            provider_types_instances_response = response.get_result()

            print(json.dumps(provider_types_instances_response, indent=2))

            # end-get_provider_types_instances

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
                attachment_id=attachment_id_link,
                profiles_id=profile_id_link,
            )
            attachment_item = response.get_result()

            print(json.dumps(attachment_item, indent=2))

            # end-delete_profile_attachment

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
                profiles_id=profile_id_link,
            )
            profile = response.get_result()

            print(json.dumps(profile, indent=2))

            # end-delete_custom_profile

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
                control_libraries_id=control_library_id_link,
            )
            control_library_delete = response.get_result()

            print(json.dumps(control_library_delete, indent=2))

            # end-delete_custom_control_library

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
                rule_id=rule_id_link,
            )

            # end-delete_rule
            print('\ndelete_rule() response status code: ', response.get_status_code())

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
                provider_type_id=provider_type_id_link,
                provider_type_instance_id=provider_type_instance_id_link,
            )

            # end-delete_provider_type_instance
            print('\ndelete_provider_type_instance() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: SecurityAndComplianceCenterApiV3
##############################################################################
