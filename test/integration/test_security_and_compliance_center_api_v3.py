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
Integration Tests for SecurityAndComplianceCenterApiV3
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_scc.security_and_compliance_center_api_v3 import *

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
provider_type_id_link = None
provider_type_instance_id_link = None
report_id_for_report_link = None
rule_id_link = None
type_for_report_link = None
account_id = None
instance_id = None
create_scan_attachment_id = None

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
            cls.account_id=cls.config['ACCOUNTID']
            cls.instance_id = cls.config['INSTANCEID']
            if cls.instance_id == "": print("Unable to load instanceID configuration property, skipping tests")
            cls.create_scan_attachment_id = cls.config['ATTACHMENTID']
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
            x_correlation_id='1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        settings = response.get_result()
        assert settings is not None

        event_notifications_crn_for_update_settings_link = settings['event_notifications']['instance_crn']
        object_storage_crn_for_update_settings_link = settings['object_storage']['instance_crn']
        object_storage_bucket_for_update_settings_link = settings['object_storage']['bucket']
        object_storage_location_for_update_settings_link = settings['object_storage']['bucket_location']

    @needscredentials
    def test_create_rule(self):
        global rule_id_link

        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {
            'name': 'location',
            'operator': 'string_equals',
            'value': 'us-east',
        }
        # Construct a dict representation of a Target model
        target_model = {
            'service_name': 'cloud-object-storage',
            'service_display_name': 'testString',
            'resource_kind': 'bucket',
            'additional_target_attributes': [additional_target_attribute_model],
        }
        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {
            'description': 'testString',
            'property': 'hard_quota',
            'operator': 'num_equals',
            'value': '${hard_quota}',
        }
        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {
            'description': 'The Cloud Object Storage rule.',
            'and': [required_config_items_model],
        }
        # Construct a dict representation of a Parameter model
        parameter_model = {
            'name': 'hard_quota',
            'display_name': 'The Cloud Object Storage bucket quota.',
            'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
            'type': 'numeric',
        }
        # Construct a dict representation of a Import model
        import_model = {
            'parameters': [parameter_model],
        }

        response = self.security_and_compliance_center_api_service.create_rule(
            description='Example rule',
            target=target_model,
            required_config=required_config_model,
            type='user_defined',
            version='1.0.0',
            import_=import_model,
            labels=[],
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 201
        rule = response.get_result()
        assert rule is not None

        rule_id_link = rule['id']

    @needscredentials
    def test_get_rule(self):
        global e_tag_link

        response = self.security_and_compliance_center_api_service.get_rule(
            rule_id=rule_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        rule = response.get_result()
        assert rule is not None

        e_tag_link = response.get_headers().get('ETag')

    @needscredentials
    def test_get_latest_reports(self):
        global account_id_for_report_link
        global report_id_for_report_link
        global attachment_id_for_report_link
        global group_id_for_report_link
        global profile_id_for_report_link
        global type_for_report_link

        response = self.security_and_compliance_center_api_service.get_latest_reports(
            x_correlation_id='testString',
            x_request_id='testString',
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
    def test_update_settings(self):
        # Construct a dict representation of a EventNotifications model
        event_notifications_model = {
            'instance_crn': event_notifications_crn_for_update_settings_link,
            'updated_on': '2019-01-01T12:00:00.000Z',
            'source_id': 'crn:v1:staging:public:event-notifications:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:b8b07245-0bbe-4478-b11c-0dce523105fd::',
            'source_description': 'This source is used for integration with IBM Cloud Security and Compliance Center.',
            'source_name': 'compliance',
        }
        # Construct a dict representation of a ObjectStorage model
        object_storage_model = {
            'instance_crn': object_storage_crn_for_update_settings_link,
            'bucket': object_storage_bucket_for_update_settings_link,
            'bucket_location': object_storage_location_for_update_settings_link,
            'bucket_endpoint': 'testString',
            'updated_on': '2019-01-01T12:00:00.000Z',
        }

        response = self.security_and_compliance_center_api_service.update_settings(
            event_notifications=event_notifications_model,
            object_storage=object_storage_model,
            x_correlation_id='1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5',
            x_request_id='testString',
        )

        assert response.get_status_code() == 204
        settings = response.get_result()
        assert settings is None

    # @needscredentials
    # def test_post_test_event(self):
    #     response = self.security_and_compliance_center_api_service.post_test_event(
    #         x_correlation_id='1a2b3c4d-5e6f-4a7b-8c9d-e0f1a2b3c4d5',
    #         x_request_id='testString',
    #     )

    #     assert response.get_status_code() == 202
    #     test_event = response.get_result()
    #     assert test_event is not None

    @needscredentials
    def test_create_custom_control_library(self):
        global control_library_id_link

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {
            'parameter_name': 'session_invalidation_in_seconds',
            'parameter_display_name': 'Sign out due to inactivity in seconds',
            'parameter_type': 'numeric',
            'parameter_value': 'public',
        }
        # Construct a dict representation of a Implementation model
        implementation_model = {
            'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
            'assessment_method': 'ibm-cloud-rule',
            'assessment_type': 'automated',
            'assessment_description': 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services',
            'parameter_count': 38,
            'parameters': [parameter_info_model],
        }
        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {
            'control_specification_id': '5c7d6f88-a92f-4734-9b49-bd22b0900184',
            'responsibility': 'user',
            'component_id': 'iam-identity',
            'component_name': 'testString',
            'environment': 'ibm-cloud',
            'control_specification_description': 'IBM cloud',
            'assessments_count': 38,
            'assessments': [implementation_model],
        }
        # Construct a dict representation of a ControlDocs model
        control_docs_model = {
            'control_docs_id': 'sc-7',
            'control_docs_type': 'ibm-cloud',
        }
        # Construct a dict representation of a ControlsInControlLib model
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
            'status': 'enabled',
        }

        response = self.security_and_compliance_center_api_service.create_custom_control_library(
            control_library_name='IBM Cloud for Financial Services',
            control_library_description='IBM Cloud for Financial Services',
            control_library_type='custom',
            controls=[controls_in_control_lib_model],
            control_library_version='1.0.0',
            latest=True,
            controls_count=38,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 201
        control_library = response.get_result()
        assert control_library is not None

        control_library_id_link = control_library['id']

    @needscredentials
    def test_list_control_libraries(self):
        response = self.security_and_compliance_center_api_service.list_control_libraries(
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
            control_library_type='custom',
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
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
            control_library_type='custom',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ControlLibrariesPager(
            client=self.security_and_compliance_center_api_service,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
            control_library_type='custom',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_control_libraries() returned a total of {len(all_results)} items(s) using ControlLibrariesPager.')

    @needscredentials
    def test_get_control_library(self):
        response = self.security_and_compliance_center_api_service.get_control_library(
            control_libraries_id=control_library_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        control_library = response.get_result()
        assert control_library is not None

    @needscredentials
    def test_replace_custom_control_library(self):
        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {
            'parameter_name': 'session_invalidation_in_seconds',
            'parameter_display_name': 'Sign out due to inactivity in seconds',
            'parameter_type': 'numeric',
            'parameter_value': 'public',
        }
        # Construct a dict representation of a Implementation model
        implementation_model = {
            'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
            'assessment_method': 'ibm-cloud-rule',
            'assessment_type': 'automated',
            'assessment_description': 'Check that there is an Activity Tracker event route defined to collect global events generated by IBM Cloud services',
            'parameter_count': 38,
            'parameters': [parameter_info_model],
        }
        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {
            'control_specification_id': '5c7d6f88-a92f-4734-9b49-bd22b0900184',
            'responsibility': 'user',
            'component_id': 'iam-identity',
            'component_name': 'testString',
            'environment': 'ibm-cloud',
            'control_specification_description': 'IBM cloud',
            'assessments_count': 38,
            'assessments': [implementation_model],
        }
        # Construct a dict representation of a ControlDocs model
        control_docs_model = {
            'control_docs_id': 'sc-7',
            'control_docs_type': 'ibm-cloud',
        }
        # Construct a dict representation of a ControlsInControlLib model
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
            'status': 'enabled',
        }

        response = self.security_and_compliance_center_api_service.replace_custom_control_library(
            control_libraries_id=control_library_id_link,
            id='testString',
            account_id=account_id,
            control_library_name='IBM Cloud for Financial Services',
            control_library_description='IBM Cloud for Financial Services',
            control_library_type='custom',
            control_library_version='1.1.0',
            created_on=string_to_datetime('2019-01-01T12:00:00.000Z'),
            created_by='testString',
            updated_on=string_to_datetime('2019-01-01T12:00:00.000Z'),
            updated_by='testString',
            latest=True,
            hierarchy_enabled=True,
            controls_count=38,
            control_parents_count=38,
            controls=[controls_in_control_lib_model],
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        control_library = response.get_result()
        assert control_library is not None

    @needscredentials
    def test_create_profile(self):
        global profile_id_link

        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {
            'control_library_id': control_library_id_link,
            'control_id': '1fa45e17-9322-4e6c-bbd6-1c51db08e790',
        }
        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {
            'assessment_type': 'Automated',
            'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
            'parameter_name': 'session_invalidation_in_seconds',
            'parameter_default_value': '120',
            'parameter_display_name': 'Sign out due to inactivity in seconds',
            'parameter_type': 'numeric',
        }

        response = self.security_and_compliance_center_api_service.create_profile(
            profile_name='test_profile1',
            profile_description='test_description1',
            profile_type='custom',
            controls=[profile_controls_prototype_model],
            default_parameters=[default_parameters_prototype_model],
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 201
        profile = response.get_result()
        assert profile is not None

        profile_id_link = profile['id']

    @needscredentials
    def test_list_profiles(self):
        response = self.security_and_compliance_center_api_service.list_profiles(
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
            profile_type='custom',
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
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
            profile_type='custom',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ProfilesPager(
            client=self.security_and_compliance_center_api_service,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
            profile_type='custom',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_profiles() returned a total of {len(all_results)} items(s) using ProfilesPager.')

    @needscredentials
    def test_get_profile(self):
        response = self.security_and_compliance_center_api_service.get_profile(
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        profile = response.get_result()
        assert profile is not None

    @needscredentials
    def test_replace_profile(self):
        # Construct a dict representation of a ProfileControlsPrototype model
        profile_controls_prototype_model = {
            'control_library_id': control_library_id_link,
            'control_id': '1fa45e17-9322-4e6c-bbd6-1c51db08e790',
        }
        # Construct a dict representation of a DefaultParametersPrototype model
        default_parameters_prototype_model = {
            'assessment_type': 'Automated',
            'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
            'parameter_name': 'session_invalidation_in_seconds',
            'parameter_default_value': '120',
            'parameter_display_name': 'Sign out due to inactivity in seconds',
            'parameter_type': 'numeric',
        }

        response = self.security_and_compliance_center_api_service.replace_profile(
            profiles_id=profile_id_link,
            profile_name='test_profile1',
            profile_description='test_description1',
            profile_type='custom',
            controls=[profile_controls_prototype_model],
            default_parameters=[default_parameters_prototype_model],
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        profile = response.get_result()
        assert profile is not None

    @needscredentials
    def test_list_rules(self):
        response = self.security_and_compliance_center_api_service.list_rules(
            x_correlation_id='testString',
            x_request_id='testString',
            type='system_defined',
            search='testString',
            service_name='testString',
        )

        assert response.get_status_code() == 200
        rules_page_base = response.get_result()
        assert rules_page_base is not None

    @needscredentials
    def test_replace_rule(self):
        # Construct a dict representation of a AdditionalTargetAttribute model
        additional_target_attribute_model = {
            'name': 'location',
            'operator': 'string_equals',
            'value': 'us-south',
        }
        # Construct a dict representation of a Target model
        target_model = {
            'service_name': 'cloud-object-storage',
            'service_display_name': 'Cloud Object Storage',
            'resource_kind': 'bucket',
            'additional_target_attributes': [additional_target_attribute_model],
        }
        # Construct a dict representation of a RequiredConfigItemsRequiredConfigBase model
        required_config_items_model = {
            'description': 'testString',
            'property': 'hard_quota',
            'operator': 'num_equals',
            'value': '${hard_quota}',
        }
        # Construct a dict representation of a RequiredConfigRequiredConfigAnd model
        required_config_model = {
            'description': 'The Cloud Object Storage rule.',
            'and': [required_config_items_model],
        }
        # Construct a dict representation of a Parameter model
        parameter_model = {
            'name': 'hard_quota',
            'display_name': 'The Cloud Object Storage bucket quota.',
            'description': 'The maximum bytes that are allocated to the Cloud Object Storage bucket.',
            'type': 'numeric',
        }
        # Construct a dict representation of a Import model
        import_model = {
            'parameters': [parameter_model],
        }

        response = self.security_and_compliance_center_api_service.replace_rule(
            rule_id=rule_id_link,
            if_match=e_tag_link,
            description='Example rule',
            target=target_model,
            required_config=required_config_model,
            type='user_defined',
            version='1.0.1',
            import_=import_model,
            labels=[],
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        rule = response.get_result()
        assert rule is not None

    @needscredentials
    def test_create_attachment(self):
        global attachment_id_link

        # Construct a dict representation of a PropertyItem model
        property_scope_id = {
            'name': 'scope_id',
            'value': self.account_id,
        }
        property_scope_type = {
            'name': 'scope_type',
            'value': "account",
        }
        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {
            'environment': 'ibm-cloud',
            'properties': [property_scope_id, property_scope_type],
        }
        # Construct a dict representation of a FailedControls model
        failed_controls_model = {
            'threshold_limit': 15,
            'failed_control_ids': [],
        }
        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {
            'enabled': False,
            'controls': failed_controls_model,
        }
        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {
            'assessment_type': 'Automated',
            'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
            'parameter_name': 'session_invalidation_in_seconds',
            'parameter_value': '120',
            'parameter_display_name': 'Sign out due to inactivity in seconds',
            'parameter_type': 'numeric',
        }
        # Construct a dict representation of a AttachmentsPrototype model
        attachments_prototype_model = {
            'id': '130003ea8bfa43c5aacea07a86da3000',
            'name': 'account-0d8c3805dfea40aa8ad02265a18eb12b',
            'description': 'Test description',
            'scope': [multi_cloud_scope_model],
            'status': 'enabled',
            'schedule': 'every_30_days',
            'notifications': attachments_notifications_prototype_model,
            'attachment_parameters': [attachment_parameter_prototype_model],
        }
        response = self.security_and_compliance_center_api_service.create_attachment(
            profiles_id=profile_id_link,
            attachments=[attachments_prototype_model],
            profile_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )


        assert response.get_status_code() == 201
        attachment_prototype = response.get_result()
        assert attachment_prototype is not None

        attachment_id_link = attachment_prototype['attachments'][0]['id']

    @needscredentials
    def test_list_attachments(self):
        response = self.security_and_compliance_center_api_service.list_attachments(
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
        )
        assert response.get_status_code() == 200
        attachment_collection = response.get_result()
        assert attachment_collection is not None

    @needscredentials
    def test_list_attachments_with_pager(self):
        all_results = []

        # Test get_next().
        pager = AttachmentsPager(
            client=self.security_and_compliance_center_api_service,
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = AttachmentsPager(
            client=self.security_and_compliance_center_api_service,
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_attachments() returned a total of {len(all_results)} items(s) using AttachmentsPager.')

    @needscredentials
    def test_get_profile_attachment(self):
        response = self.security_and_compliance_center_api_service.get_profile_attachment(
            attachment_id=attachment_id_link,
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        attachment_item = response.get_result()
        assert attachment_item is not None

    @needscredentials
    def test_replace_profile_attachment(self):
        # Construct a dict representation of a PropertyItem model
        property_scope_id = {
            'name': 'scope_id',
            'value': self.account_id,
        }
        property_scope_type = {
            'name': 'scope_type',
            'value': "account",
        }
        # Construct a dict representation of a MultiCloudScope model
        multi_cloud_scope_model = {
            'environment': 'ibm-cloud',
            'properties': [property_scope_id, property_scope_type],
        }
        # Construct a dict representation of a FailedControls model
        failed_controls_model = {
            'threshold_limit': 15,
            'failed_control_ids': [],
        }
        # Construct a dict representation of a AttachmentsNotificationsPrototype model
        attachments_notifications_prototype_model = {
            'enabled': False,
            'controls': failed_controls_model,
        }
        # Construct a dict representation of a AttachmentParameterPrototype model
        attachment_parameter_prototype_model = {
            'assessment_type': 'Automated',
            'assessment_id': 'rule-a637949b-7e51-46c4-afd4-b96619001bf1',
            'parameter_name': 'session_invalidation_in_seconds',
            'parameter_value': '120',
            'parameter_display_name': 'Sign out due to inactivity in seconds',
            'parameter_type': 'numeric',
        }
        # Construct a dict representation of a LastScan model
        last_scan_model = {
            'id': 'e8a39d25-0051-4328-8462-988ad321f49a',
            'status': 'in_progress',
            'time': '2019-01-01T12:00:00.000Z',
        }

        response = self.security_and_compliance_center_api_service.replace_profile_attachment(
            attachment_id=attachment_id_link,
            profiles_id=profile_id_link,
            id='testString',
            profile_id=profile_id_link,
            account_id=account_id,
            instance_id=instance_id,
            scope=[multi_cloud_scope_model],
            created_on='2019-01-01T12:00:00.000Z',
            created_by='testString',
            updated_on='2019-01-01T12:00:00.000Z',
            updated_by='testString',
            status='enabled',
            schedule='every_30_days',
            notifications=attachments_notifications_prototype_model,
            attachment_parameters=[attachment_parameter_prototype_model],
            last_scan=last_scan_model,
            next_scan_time='2019-01-01T12:00:00.000Z',
            name='account-0d8c3805dfea40aa8ad02265a18eb12b',
            description='Test description',
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        attachment_item = response.get_result()
        assert attachment_item is not None

    @needscredentials
    def test_create_scan(self):
        try:
            response = self.security_and_compliance_center_api_service.create_scan(
                attachment_id=self.create_scan_attachment_id,
                x_correlation_id='testString',
                x_request_id='testString',
            )
        except Exception as e: 
            if  'another scan is currently in progress' in str(e).lower():
                return
        assert response.get_status_code() == 201
        scan = response.get_result()
        assert scan is not None

    @needscredentials
    def test_list_attachments_account(self):
        response = self.security_and_compliance_center_api_service.list_attachments_account(
            x_correlation_id='testString',
            x_request_id='testString',
            limit=50,
        )
        assert response.get_status_code() == 200
        attachment_collection = response.get_result()
        assert attachment_collection is not None

    @needscredentials
    def test_list_attachments_account_with_pager(self):
        all_results = []

        # Test get_next().
        pager = AttachmentsAccountPager(
            client=self.security_and_compliance_center_api_service,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = AttachmentsAccountPager(
            client=self.security_and_compliance_center_api_service,
            x_correlation_id='testString',
            x_request_id='testString',
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        print(f'\nlist_attachments_account() returned a total of {len(all_results)} items(s) using AttachmentsAccountPager.')

    @needscredentials
    def test_list_reports(self):
        response = self.security_and_compliance_center_api_service.list_reports(
            x_correlation_id='testString',
            x_request_id='testString',
            attachment_id=attachment_id_for_report_link,
            group_id=group_id_for_report_link,
            profile_id=profile_id_for_report_link,
            type=type_for_report_link,
            limit=50,
            sort='profile_name',
        )
        assert response.get_status_code() == 200
        report_page = response.get_result()
        assert report_page is not None

    @needscredentials
    def test_list_reports_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ReportsPager(
            client=self.security_and_compliance_center_api_service,
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

        # Test get_all().
        pager = ReportsPager(
            client=self.security_and_compliance_center_api_service,
            x_correlation_id='testString',
            x_request_id='testString',
            attachment_id=attachment_id_for_report_link,
            group_id=group_id_for_report_link,
            profile_id=profile_id_for_report_link,
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
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        report = response.get_result()
        assert report is not None

    @needscredentials
    def test_get_report_summary(self):
        response = self.security_and_compliance_center_api_service.get_report_summary(
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        report_summary = response.get_result()
        assert report_summary is not None

    @needscredentials
    def test_get_report_evaluation(self):
        response = self.security_and_compliance_center_api_service.get_report_evaluation(
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
            exclude_summary=True,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_report_controls(self):
        response = self.security_and_compliance_center_api_service.get_report_controls(
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
            control_id='testString',
            control_name='testString',
            control_description='testString',
            control_category='testString',
            status='compliant',
            sort='control_name',
        )

        assert response.get_status_code() == 200
        report_controls = response.get_result()
        assert report_controls is not None

    # @needscredentials
    # def test_get_report_rule(self):
    #     response = self.security_and_compliance_center_api_service.get_report_rule(
    #         report_id=report_id_for_report_link,
    #         rule_id='rule-8d444f8c-fd1d-48de-bcaa-f43732568761',
    #         x_correlation_id='testString',
    #         x_request_id='testString',
    #     )

    #     assert response.get_status_code() == 200
    #     rule_info = response.get_result()
    #     assert rule_info is not None

    @needscredentials
    def test_list_report_evaluations(self):
        response = self.security_and_compliance_center_api_service.list_report_evaluations(
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
        assert response.get_status_code() == 200
        evaluation_page = response.get_result()
        assert evaluation_page is not None

    @needscredentials
    def test_list_report_evaluations_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ReportEvaluationsPager(
            client=self.security_and_compliance_center_api_service,
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
            status='failure',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ReportEvaluationsPager(
            client=self.security_and_compliance_center_api_service,
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
            status='failure',
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_report_evaluations() returned a total of {len(all_results)} items(s) using ReportEvaluationsPager.')

    @needscredentials	
    def test_list_report_resources(self):	
        response = self.security_and_compliance_center_api_service.list_report_resources(	
            report_id=report_id_for_report_link,	
            x_correlation_id='testString',	
            x_request_id='testString',	
            id='testString',	
            resource_name='testString',	
            account_id=account_id_for_report_link,	
            component_id='testString',	
            status='compliant',	
            sort='account_id',	
            limit=50,	
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
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
            account_id=account_id_for_report_link,
            status='compliant',
            sort='account_id',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ReportResourcesPager(
            client=self.security_and_compliance_center_api_service,
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
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_report_resources() returned a total of {len(all_results)} items(s) using ReportResourcesPager.')

    @needscredentials
    def test_get_report_tags(self):
        response = self.security_and_compliance_center_api_service.get_report_tags(
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        report_tags = response.get_result()
        assert report_tags is not None

    @needscredentials
    def test_get_report_violations_drift(self):
        response = self.security_and_compliance_center_api_service.get_report_violations_drift(
            report_id=report_id_for_report_link,
            x_correlation_id='testString',
            x_request_id='testString',
            scan_time_duration=0,
        )

        assert response.get_status_code() == 200
        report_violations_drift = response.get_result()
        assert report_violations_drift is not None

    @needscredentials
    def test_list_provider_types(self):
        global provider_type_id_link

        response = self.security_and_compliance_center_api_service.list_provider_types(
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        provider_types_collection = response.get_result()
        assert provider_types_collection is not None

        provider_type_id_link = provider_types_collection['provider_types'][1]['id']

    @needscredentials
    def test_get_provider_type_by_id(self):
        response = self.security_and_compliance_center_api_service.get_provider_type_by_id(
            provider_type_id=provider_type_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        provider_type_item = response.get_result()
        assert provider_type_item is not None

    @needscredentials
    def test_list_provider_type_instances(self):
        response = self.security_and_compliance_center_api_service.list_provider_type_instances(
            provider_type_id=provider_type_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        provider_type_instances_response = response.get_result()
        assert provider_type_instances_response is not None

    @needscredentials
    def test_create_provider_type_instance(self):
        global provider_type_instance_id_link

        response = self.security_and_compliance_center_api_service.create_provider_type_instance(
            provider_type_id=provider_type_id_link,
            name='workload-protection-instance-1',
            attributes={'wp_crn':'crn:v1:staging:public:sysdig-secure:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:0df4004c-fb74-483b-97be-dd9bd35af4d8::'},
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 201
        provider_type_instance_item = response.get_result()
        assert provider_type_instance_item is not None

        provider_type_instance_id_link = provider_type_instance_item['id']

    @needscredentials
    def test_get_provider_type_instance(self):
        response = self.security_and_compliance_center_api_service.get_provider_type_instance(
            provider_type_id=provider_type_id_link,
            provider_type_instance_id=provider_type_instance_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        provider_type_instance_item = response.get_result()
        assert provider_type_instance_item is not None

    @needscredentials
    def test_update_provider_type_instance(self):
        response = self.security_and_compliance_center_api_service.update_provider_type_instance(
            provider_type_id=provider_type_id_link,
            provider_type_instance_id=provider_type_instance_id_link,
            name='workload-protection-instance-1',
            attributes={'wp_crn':'crn:v1:staging:public:sysdig-secure:us-south:a/ff88f007f9ff4622aac4fbc0eda36255:0df4004c-fb74-483b-97be-dd9bd35af4d8::'},
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        provider_type_instance_item = response.get_result()
        assert provider_type_instance_item is not None

    @needscredentials
    def test_get_provider_types_instances(self):
        response = self.security_and_compliance_center_api_service.get_provider_types_instances(
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        provider_types_instances_response = response.get_result()
        assert provider_types_instances_response is not None
    
    @needscredentials
    def test_delete_profile_attachment(self):
        response = self.security_and_compliance_center_api_service.delete_profile_attachment(
            attachment_id=attachment_id_link,
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        attachment_item = response.get_result()
        assert attachment_item is not None

    @needscredentials
    def test_delete_custom_profile(self):
        response = self.security_and_compliance_center_api_service.delete_custom_profile(
            profiles_id=profile_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        profile = response.get_result()
        assert profile is not None

    @needscredentials
    def test_delete_custom_control_library(self):
        response = self.security_and_compliance_center_api_service.delete_custom_control_library(
            control_libraries_id=control_library_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 200
        control_library_delete = response.get_result()
        assert control_library_delete is not None

    @needscredentials
    def test_delete_rule(self):
        response = self.security_and_compliance_center_api_service.delete_rule(
            rule_id=rule_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_provider_type_instance(self):
        response = self.security_and_compliance_center_api_service.delete_provider_type_instance(
            provider_type_id=provider_type_id_link,
            provider_type_instance_id=provider_type_instance_id_link,
            x_correlation_id='testString',
            x_request_id='testString',
        )

        assert response.get_status_code() == 204
