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
Integration Tests for ComplianceV2
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from compliancev2.compliance_v2 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Config file name
config_file = 'compliance_v2.env'


class TestComplianceV2:
    """
    Integration Test Class for ComplianceV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file
            
            cls.compliance_service = ComplianceV2.new_instance()
            
            assert cls.compliance_service is not None

            cls.config = read_external_sources(ComplianceV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.compliance_service.enable_retries()

            config = read_external_sources("compliance")
            cls.config = config

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_profile(self):
        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {
            'control_library_id': self.config["controlLibraryID"],
            'control_id': self.config["controlID"],
        }
        # Construct a dict representation of a DefaultParameters model
        # default_parameters_model = {
        #     'assessment_type': self.config["assessmentType"],
        #     'assessment_id': self.config["assessmentID"],
        #     'parameter_name': self.config["parameterName"],
        #     # 'parameter_default_value': self.config[""],
        #     'parameter_display_name': self.config["parameterDisplayName"],
        #     'parameter_type': self.config["parameterType"],
        # }

        response = self.compliance_service.create_profile(
            instance_id=self.config["instanceID"],
            profile_name=self.config["profileName"],
            profile_description=self.config["profileDescription"],
            profile_type=self.config["profileType"],
            profile_version=self.config["profileVersion"],
            latest=True,
            # version_group_label=self.config[""],
            controls=[profile_controls_in_request_model],
            default_parameters=[],
            transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        profile_response = response.get_result()
        assert profile_response is not None

    @needscredentials
    def test_list_profiles(self):       
        response = self.compliance_service.list_profiles(
            instance_id = self.config["instanceID"],
            transaction_id = self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        get_all_profiles_resp_body = response.get_result()
        assert get_all_profiles_resp_body is not None

    @needscredentials
    def test_add_profile(self):
        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {
            'control_library_id': self.config["controlLibrariesID"],
            'control_id': self.config["controlID"],
        }
        # Construct a dict representation of a DefaultParameters model
        # default_parameters_model = {
        #     'assessment_type': self.config["assessmentType"],
        #     'assessment_id': self.config["assessmentID"],
        #     'parameter_name': self.config["parameterName"],
        #     # 'parameter_default_value': self.config[""],
        #     'parameter_display_name': self.config["parameterDisplayName"],
        #     'parameter_type': self.config["parameterType"],
        # }

        response = self.compliance_service.add_profile(
            profiles_id=self.config["profilesID"],
            instance_id=self.config["instanceID"],
            profile_name=self.config["profileName"],
            profile_description=self.config["profileDescription"],
            profile_type=self.config["profileType"],
            profile_version=self.config["profileVersion"],
            latest=True,
            # version_group_label=self.config[""],
            controls=[profile_controls_in_request_model],
            default_parameters=[],
            transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        profile_response = response.get_result()
        assert profile_response is not None

    @needscredentials
    def test_get_profile(self):
        response = self.compliance_service.get_profile(
            profiles_id=self.config["profilesID"],
            instance_id=self.config["instanceID"],
            transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        profile_response = response.get_result()
        assert profile_response is not None

    @needscredentials
    def test_replace_profile_parameters(self):
        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {
            'assessment_type': self.config["assessmentType"],
            'assessment_id': self.config["assessmentID"],
            'parameter_name': self.config["parameterName"],
            # 'parameter_default_value': self.config[""],
            'parameter_display_name': self.config["parameterDisplayName"],
            'parameter_type': self.config["parameterType"],
        }

        response = self.compliance_service.replace_profile_parameters(
            profiles_id=self.config["profilesID"],
            instance_id=self.config["instanceID"],
            id=self.config["profilesID"],
            default_parameters=[default_parameters_model],
            transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        profile_default_parameters_response = response.get_result()
        assert profile_default_parameters_response is not None

    @needscredentials
    def test_create_attachment(self):
        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {
            'scope_id': self.config["scopeID"],
            'scope_type': self.config["scopeType"],
        }
        # Construct a dict representation of a ParameterInfo model
        # parameter_info_model = {
        #     'parameter_name': self.config["parameterName"],
        #     'parameter_display_name': self.config["parameterDisplayName"],
        #     'parameter_type': self.config["parameterType"],
        # }
        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {
            'parameter_name': self.config["parameterName"],
            'parameter_display_name': self.config["parameterDisplayName"],
            'parameter_type': self.config["parameterType"],
            'parameter_value': self.config["parameterValue"],
            'assessment_type': self.config["assessmentType"],
            'assessment_id': self.config["assessmentID"],
            # 'parameters': [parameter_info_model],
        }
        # Construct a dict representation of a FailedControls model
        # failed_controls_model = {
        #     'threshold_limit': 38,
        #     'failed_control_ids': [self.config[""]],
        # }
        # Construct a dict representation of a AttachmentsNotificationsPayload model
        # attachments_notifications_payload_model = {
        #     'enabled': True,
        #     'controls': failed_controls_model,
        # }
        # Construct a dict representation of a AttachmentPayload model
        attachment_payload_model = {
            # 'id': self.config["profilesID"],
            'account_id': self.config["accountID"],
            'included_scope': scope_payload_model,
            'exclusions': [],
            # 'created_by': self.config[""],
            # 'created_on': self.config[""],
            # 'updated_by': self.config[""],
            # 'updated_on': self.config[""],
            'status': 'enabled',
            'attachment_parameters': [parameter_details_model],
            # 'attachment_notifications': attachments_notifications_payload_model,
        }

        response = self.compliance_service.create_attachment(
            profiles_id=self.config["profilesID"],
            instance_id=self.config["instanceID"],
            attachments=[attachment_payload_model],
            transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        attachment_profile_response = response.get_result()
        assert attachment_profile_response is not None

    @needscredentials
    def test_check_profile_attachmnets(self):
        response = self.compliance_service.check_profile_attachmnets(
           profiles_id=self.config["profilesID"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        get_all_attachmnets_for_profile_resp_body = response.get_result()
        assert get_all_attachmnets_for_profile_resp_body is not None

    @needscredentials
    def test_get_profile_attachmnet(self):
        response = self.compliance_service.get_profile_attachmnet(
           profiles_id=self.config["profilesID"],
           attachment_id=self.config["attachmentID"],
           instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        attachment_payload = response.get_result()
        assert attachment_payload is not None

    @needscredentials
    def test_replace_profile_attachment(self):
        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {
            'scope_id': self.config["scopeID"],
            'scope_type': self.config["scopeType"],
        }
        # Construct a dict representation of a ParameterInfo model
        # parameter_info_model = {
        #      'parameter_name': self.config["parameterName"],
        #     'parameter_display_name': self.config["parameterDisplayName"],
        #     'parameter_type': self.config["parameterType"],
        # }
        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {
             'parameter_name': self.config["parameterName"],
            'parameter_display_name': self.config["parameterDisplayName"],
            'parameter_type': self.config["parameterType"],
            'parameter_value': self.config["parameterValue"],
            'assessment_type': self.config["assessmentType"],
            'assessment_id': self.config["assessmentID"],
            # 'parameters': [parameter_info_model],
        }
        # Construct a dict representation of a FailedControls model
        # failed_controls_model = {
        #     'threshold_limit': 38,
        #     'failed_control_ids': [self.config[""]],
        # }
        # Construct a dict representation of a AttachmentsNotificationsPayload model
        # attachments_notifications_payload_model = {
        #     'enabled': True,
        #     'controls': failed_controls_model,
        # }

        response = self.compliance_service.replace_profile_attachment(
           profiles_id=self.config["profilesID"],
            attachment_id=self.config["attachmentID"],
             instance_id=self.config["instanceID"],
            id=self.config["attachmentID"],
            account_id=self.config["accountID"],
            included_scope=scope_payload_model,
            exclusions=[],
            # created_by=self.config[""],
            # created_on=self.config[""],
            # updated_by=self.config[""],
            # updated_on=self.config[""],
            status='enabled',
            attachment_parameters=[parameter_details_model],
            # attachment_notifications=attachments_notifications_payload_model,
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        attachment_payload = response.get_result()
        assert attachment_payload is not None

    @needscredentials
    def test_list_attachment_parameters(self):
        response = self.compliance_service.list_attachment_parameters(
           profiles_id=self.config["profilesID"],
            attachment_id=self.config["attachmentID"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        parameter_details = response.get_result()
        assert parameter_details is not None

    @needscredentials
    def test_replace_attachment(self):
        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {
             'parameter_name': self.config["parameterName"],
            'parameter_display_name': self.config["parameterDisplayName"],
            'parameter_type': self.config["parameterType"],
        }

        response = self.compliance_service.replace_attachment(
           profiles_id=self.config["profilesID"],
            attachment_id=self.config["attachmentID"],
             instance_id=self.config["instanceID"],
            parameter_name=self.config["parameterName"],
            parameter_display_name=self.config["parameterDisplayName"],
            parameter_type=self.config["parameterType"],
            parameter_value=self.config["parameterValue"],
            assessment_type=self.config["assessmentTypeParameter"],
            assessment_id=self.config["assessmentIdParameter"],
            parameters=[parameter_info_model],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        parameter_details = response.get_result()
        assert parameter_details is not None

    @needscredentials
    def test_get_parameters_by_name(self):
        response = self.compliance_service.get_parameters_by_name(
           profiles_id=self.config["profilesID"],
            attachment_id=self.config["attachmentID"],
            parameter_name=self.config["parameterName"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        parameter_details = response.get_result()
        assert parameter_details is not None

    @needscredentials
    def test_replace_attachmnet_parameters_by_name(self):
        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {
             'parameter_name': self.config["parameterName"],
            'parameter_display_name': self.config["parameterDisplayName"],
            'parameter_type': self.config["parameterType"],
        }

        response = self.compliance_service.replace_attachmnet_parameters_by_name(
           profiles_id=self.config["profilesID"],
            attachment_id=self.config["attachmentID"],
            parameter_name=self.config["parameterName"],
            instance_id=self.config["instanceID"],
            new_parameter_name=self.config["parameterName"],
            new_parameter_display_name=self.config["parameterDisplayName"],
            new_parameter_type=self.config["parameterType"],
            new_parameter_value=self.config["parameterValue"],
            new_assessment_type=self.config["assessmentTypeParameter"],
            new_assessment_id=self.config["assessmentIdParameter"],
            new_parameters=[parameter_info_model],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        parameter_details = response.get_result()
        assert parameter_details is not None

    @needscredentials
    def test_create_custom_control_library(self):
        # Construct a dict representation of a ParameterInfo model
        # parameter_info_model = {
        #      'parameter_name': self.config["parameterName"],
        #     'parameter_display_name': self.config["parameterDisplayName"],
        #     'parameter_type': self.config["parameterType"],
        # }
        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {
            'assessment_id': self.config["assessmentID"],
            'assessment_method': self.config["assessmentMethod"],
            'assessment_type': self.config["assessmentType"],
            'assessment_description': self.config["assessmentDescription"],
            # 'parameter_count': 38,
            # 'parameters': [parameter_info_model],
        }
        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {
            'id': self.config["controlID"],
            'responsibility': self.config["responsibility"],
            'component_id': self.config["componentID"],
            'environment': self.config["environment"],
            'description': self.config["description"],
            # 'assessments_count': 38,
            'assessments': [implementation_payload_model],
        }
        # Construct a dict representation of a ControlDocs model
        # control_docs_model = {
        #     'control_docs_id': self.config[""],
        #     'control_docs_type': self.config[""],
        # }
        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {
            'control_name': self.config["controlName"],
            'control_id': self.config["controlID"],
            'control_description': self.config["controlDescription"],
            'control_category': self.config["controlCategory"],
            # 'control_parent': self.config[""],
            # 'control_severity': self.config[""],
            # 'control_tags': [self.config[""]],
            'control_specifications': [control_specifications_model],
            # 'control_docs': control_docs_model,
            # 'status': 'enabled',
        }

        response = self.compliance_service.create_custom_control_library(
            instance_id=self.config["instanceID"],
            # id=self.config[""],
            account_id=self.config["accountID"],
            control_library_name=self.config["controlLibraryName"],
            control_library_description=self.config["controlLibraryDescription"],
            control_library_type=self.config["controlLibraryType"],
            # version_group_label=self.config[""],
            control_library_version=self.config["controlLibraryVersion"],
            latest=True,
            # controls_count=38,
            controls=[controls_in_control_lib_request_payload_model],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        control_library_request = response.get_result()
        assert control_library_request is not None

    @needscredentials
    def test_list_control_libraries(self):
        response = self.compliance_service.list_control_libraries(
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        get_all_control_libraries_resp_body = response.get_result()
        assert get_all_control_libraries_resp_body is not None

    @needscredentials
    def test_replace_custom_control_library(self):
        # Construct a dict representation of a ParameterInfo model
        # parameter_info_model = {
        #      'parameter_name': self.config["parameterName"],
        #     'parameter_display_name': self.config["parameterDisplayName"],
        #     'parameter_type': self.config["parameterType"],
        # }
        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {
            'assessment_id': self.config["assessmentID"],
            'assessment_method': self.config["assessmentMethod"],
            'assessment_type': self.config["assessmentType"],
            'assessment_description': self.config["assessmentDescription"],
            # 'parameter_count': 38,
            # 'parameters': [parameter_info_model],
        }
        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {
            'id': self.config["controlID"],
            'responsibility': self.config["responsibility"],
            'component_id': self.config["componentID"],
            'environment': self.config["environment"],
            'description': self.config["description"],
            # 'assessments_count': 38,
            'assessments': [implementation_payload_model],
        }
        # Construct a dict representation of a ControlDocs model
        # control_docs_model = {
        #     'control_docs_id': self.config[""],
        #     'control_docs_type': self.config[""],
        # }
        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {
            'control_name': self.config["controlName"],
            # 'control_id': self.config["controlID"],
            'control_description': self.config["controlDescription"],
            'control_category': self.config["controlCategory"],
            # 'control_parent': self.config[""],
            # 'control_severity': self.config[""],
            # 'control_tags': [self.config[""]],
            'control_specifications': [control_specifications_model],
            # 'control_docs': control_docs_model,
            # 'status': 'enabled',
        }

        response = self.compliance_service.replace_custom_control_library(
            control_libraries_id=self.config["controlLibrariesID"],
            instance_id=self.config["instanceID"],
            id=self.config["controlLibrariesID"],
            account_id=self.config["accountID"],
            control_library_name=self.config["controlLibraryName"],
            control_library_description=self.config["controlLibraryDescription"],
            control_library_type=self.config["controlLibraryType"],
            # version_group_label=self.config[""],
            control_library_version=self.config["controlLibraryVersion"],
            latest=True,
            # controls_count=38,
            controls=[controls_in_control_lib_request_payload_model],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        control_library_request = response.get_result()
        assert control_library_request is not None

    @needscredentials
    def test_get_control_library(self):
        response = self.compliance_service.get_control_library(
            control_libraries_id=self.config["controlLibrariesID"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        control_library_request = response.get_result()
        assert control_library_request is not None

    @needscredentials
    def test_create_scan(self):
        response = self.compliance_service.create_scan(
             instance_id=self.config["instanceID"],
            attachment_id=self.config["attachmentID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        create_scan_response = response.get_result()
        assert create_scan_response is not None

    @needscredentials
    def test_delete_custom_profile(self):
        response = self.compliance_service.delete_custom_profile(
           profiles_id=self.config["profilesIdDelete"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        profile_response = response.get_result()
        assert profile_response is not None

    @needscredentials
    def test_delete_profile_attachmnet(self):
        response = self.compliance_service.delete_profile_attachmnet(
           profiles_id=self.config["profilesIdDelete"],
            attachment_id=self.config["attachmentIdDelete"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        attachment_payload = response.get_result()
        assert attachment_payload is not None

    @needscredentials
    def test_delete_custom_controllibrary(self):
        response = self.compliance_service.delete_custom_controllibrary(
            control_libraries_id=self.config["controlLibrariesIdDelete"],
             instance_id=self.config["instanceID"],
           transaction_id=self.config["transactionID"],
        )

        assert response.get_status_code() == 200
        control_library_request = response.get_result()
        assert control_library_request is not None
