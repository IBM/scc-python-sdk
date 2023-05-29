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
Unit Tests for ComplianceV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from compliancev2.compliance_v2 import *


_service = ComplianceV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://fake'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: ProfileAPIs
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ComplianceV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ComplianceV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ComplianceV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateProfile:
    """
    Test Class for create_profile
    """

    @responses.activate
    def test_create_profile_all_params(self):
        """
        create_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {}
        profile_controls_in_request_model['control_library_id'] = 'testString'
        profile_controls_in_request_model['control_id'] = 'testString'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        instance_id = 'testString'
        profile_name = 'testString'
        profile_description = 'testString'
        profile_type = 'predefined'
        profile_version = 'testString'
        latest = True
        version_group_label = 'testString'
        controls = [profile_controls_in_request_model]
        default_parameters = [default_parameters_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_profile(
            instance_id,
            profile_name=profile_name,
            profile_description=profile_description,
            profile_type=profile_type,
            profile_version=profile_version,
            latest=latest,
            version_group_label=version_group_label,
            controls=controls,
            default_parameters=default_parameters,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'testString'
        assert req_body['profile_description'] == 'testString'
        assert req_body['profile_type'] == 'predefined'
        assert req_body['profile_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['version_group_label'] == 'testString'
        assert req_body['controls'] == [profile_controls_in_request_model]
        assert req_body['default_parameters'] == [default_parameters_model]

    def test_create_profile_all_params_with_retries(self):
        # Enable retries and run test_create_profile_all_params.
        _service.enable_retries()
        self.test_create_profile_all_params()

        # Disable retries and run test_create_profile_all_params.
        _service.disable_retries()
        self.test_create_profile_all_params()

    @responses.activate
    def test_create_profile_required_params(self):
        """
        test_create_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {}
        profile_controls_in_request_model['control_library_id'] = 'testString'
        profile_controls_in_request_model['control_id'] = 'testString'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        instance_id = 'testString'
        profile_name = 'testString'
        profile_description = 'testString'
        profile_type = 'predefined'
        profile_version = 'testString'
        latest = True
        version_group_label = 'testString'
        controls = [profile_controls_in_request_model]
        default_parameters = [default_parameters_model]

        # Invoke method
        response = _service.create_profile(
            instance_id,
            profile_name=profile_name,
            profile_description=profile_description,
            profile_type=profile_type,
            profile_version=profile_version,
            latest=latest,
            version_group_label=version_group_label,
            controls=controls,
            default_parameters=default_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'testString'
        assert req_body['profile_description'] == 'testString'
        assert req_body['profile_type'] == 'predefined'
        assert req_body['profile_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['version_group_label'] == 'testString'
        assert req_body['controls'] == [profile_controls_in_request_model]
        assert req_body['default_parameters'] == [default_parameters_model]

    def test_create_profile_required_params_with_retries(self):
        # Enable retries and run test_create_profile_required_params.
        _service.enable_retries()
        self.test_create_profile_required_params()

        # Disable retries and run test_create_profile_required_params.
        _service.disable_retries()
        self.test_create_profile_required_params()

    @responses.activate
    def test_create_profile_value_error(self):
        """
        test_create_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {}
        profile_controls_in_request_model['control_library_id'] = 'testString'
        profile_controls_in_request_model['control_id'] = 'testString'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        instance_id = 'testString'
        profile_name = 'testString'
        profile_description = 'testString'
        profile_type = 'predefined'
        profile_version = 'testString'
        latest = True
        version_group_label = 'testString'
        controls = [profile_controls_in_request_model]
        default_parameters = [default_parameters_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_profile(**req_copy)

    def test_create_profile_value_error_with_retries(self):
        # Enable retries and run test_create_profile_value_error.
        _service.enable_retries()
        self.test_create_profile_value_error()

        # Disable retries and run test_create_profile_value_error.
        _service.disable_retries()
        self.test_create_profile_value_error()


class TestListProfiles:
    """
    Test Class for list_profiles
    """

    @responses.activate
    def test_list_profiles_all_params(self):
        """
        list_profiles()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.list_profiles(
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_profiles_all_params_with_retries(self):
        # Enable retries and run test_list_profiles_all_params.
        _service.enable_retries()
        self.test_list_profiles_all_params()

        # Disable retries and run test_list_profiles_all_params.
        _service.disable_retries()
        self.test_list_profiles_all_params()

    @responses.activate
    def test_list_profiles_required_params(self):
        """
        test_list_profiles_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_profiles(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_profiles_required_params_with_retries(self):
        # Enable retries and run test_list_profiles_required_params.
        _service.enable_retries()
        self.test_list_profiles_required_params()

        # Disable retries and run test_list_profiles_required_params.
        _service.disable_retries()
        self.test_list_profiles_required_params()

    @responses.activate
    def test_list_profiles_value_error(self):
        """
        test_list_profiles_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profiles": [{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_profiles(**req_copy)

    def test_list_profiles_value_error_with_retries(self):
        # Enable retries and run test_list_profiles_value_error.
        _service.enable_retries()
        self.test_list_profiles_value_error()

        # Disable retries and run test_list_profiles_value_error.
        _service.disable_retries()
        self.test_list_profiles_value_error()


class TestAddProfile:
    """
    Test Class for add_profile
    """

    @responses.activate
    def test_add_profile_all_params(self):
        """
        add_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {}
        profile_controls_in_request_model['control_library_id'] = 'testString'
        profile_controls_in_request_model['control_id'] = 'testString'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        profile_name = 'testString'
        profile_description = 'testString'
        profile_type = 'predefined'
        profile_version = 'testString'
        latest = True
        version_group_label = 'testString'
        controls = [profile_controls_in_request_model]
        default_parameters = [default_parameters_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.add_profile(
            profiles_id,
            instance_id,
            profile_name=profile_name,
            profile_description=profile_description,
            profile_type=profile_type,
            profile_version=profile_version,
            latest=latest,
            version_group_label=version_group_label,
            controls=controls,
            default_parameters=default_parameters,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'testString'
        assert req_body['profile_description'] == 'testString'
        assert req_body['profile_type'] == 'predefined'
        assert req_body['profile_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['version_group_label'] == 'testString'
        assert req_body['controls'] == [profile_controls_in_request_model]
        assert req_body['default_parameters'] == [default_parameters_model]

    def test_add_profile_all_params_with_retries(self):
        # Enable retries and run test_add_profile_all_params.
        _service.enable_retries()
        self.test_add_profile_all_params()

        # Disable retries and run test_add_profile_all_params.
        _service.disable_retries()
        self.test_add_profile_all_params()

    @responses.activate
    def test_add_profile_required_params(self):
        """
        test_add_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {}
        profile_controls_in_request_model['control_library_id'] = 'testString'
        profile_controls_in_request_model['control_id'] = 'testString'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        profile_name = 'testString'
        profile_description = 'testString'
        profile_type = 'predefined'
        profile_version = 'testString'
        latest = True
        version_group_label = 'testString'
        controls = [profile_controls_in_request_model]
        default_parameters = [default_parameters_model]

        # Invoke method
        response = _service.add_profile(
            profiles_id,
            instance_id,
            profile_name=profile_name,
            profile_description=profile_description,
            profile_type=profile_type,
            profile_version=profile_version,
            latest=latest,
            version_group_label=version_group_label,
            controls=controls,
            default_parameters=default_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['profile_name'] == 'testString'
        assert req_body['profile_description'] == 'testString'
        assert req_body['profile_type'] == 'predefined'
        assert req_body['profile_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['version_group_label'] == 'testString'
        assert req_body['controls'] == [profile_controls_in_request_model]
        assert req_body['default_parameters'] == [default_parameters_model]

    def test_add_profile_required_params_with_retries(self):
        # Enable retries and run test_add_profile_required_params.
        _service.enable_retries()
        self.test_add_profile_required_params()

        # Disable retries and run test_add_profile_required_params.
        _service.disable_retries()
        self.test_add_profile_required_params()

    @responses.activate
    def test_add_profile_value_error(self):
        """
        test_add_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProfileControlsInRequest model
        profile_controls_in_request_model = {}
        profile_controls_in_request_model['control_library_id'] = 'testString'
        profile_controls_in_request_model['control_id'] = 'testString'

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        profile_name = 'testString'
        profile_description = 'testString'
        profile_type = 'predefined'
        profile_version = 'testString'
        latest = True
        version_group_label = 'testString'
        controls = [profile_controls_in_request_model]
        default_parameters = [default_parameters_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_profile(**req_copy)

    def test_add_profile_value_error_with_retries(self):
        # Enable retries and run test_add_profile_value_error.
        _service.enable_retries()
        self.test_add_profile_value_error()

        # Disable retries and run test_add_profile_value_error.
        _service.disable_retries()
        self.test_add_profile_value_error()


class TestGetProfile:
    """
    Test Class for get_profile
    """

    @responses.activate
    def test_get_profile_all_params(self):
        """
        get_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            profiles_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_all_params_with_retries(self):
        # Enable retries and run test_get_profile_all_params.
        _service.enable_retries()
        self.test_get_profile_all_params()

        # Disable retries and run test_get_profile_all_params.
        _service.disable_retries()
        self.test_get_profile_all_params()

    @responses.activate
    def test_get_profile_required_params(self):
        """
        test_get_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.get_profile(
            profiles_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_required_params_with_retries(self):
        # Enable retries and run test_get_profile_required_params.
        _service.enable_retries()
        self.test_get_profile_required_params()

        # Disable retries and run test_get_profile_required_params.
        _service.disable_retries()
        self.test_get_profile_required_params()

    @responses.activate
    def test_get_profile_value_error(self):
        """
        test_get_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile(**req_copy)

    def test_get_profile_value_error_with_retries(self):
        # Enable retries and run test_get_profile_value_error.
        _service.enable_retries()
        self.test_get_profile_value_error()

        # Disable retries and run test_get_profile_value_error.
        _service.disable_retries()
        self.test_get_profile_value_error()


class TestDeleteCustomProfile:
    """
    Test Class for delete_custom_profile
    """

    @responses.activate
    def test_delete_custom_profile_all_params(self):
        """
        delete_custom_profile()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_custom_profile(
            profiles_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_profile_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_profile_all_params.
        _service.enable_retries()
        self.test_delete_custom_profile_all_params()

        # Disable retries and run test_delete_custom_profile_all_params.
        _service.disable_retries()
        self.test_delete_custom_profile_all_params()

    @responses.activate
    def test_delete_custom_profile_required_params(self):
        """
        test_delete_custom_profile_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.delete_custom_profile(
            profiles_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_profile_required_params_with_retries(self):
        # Enable retries and run test_delete_custom_profile_required_params.
        _service.enable_retries()
        self.test_delete_custom_profile_required_params()

        # Disable retries and run test_delete_custom_profile_required_params.
        _service.disable_retries()
        self.test_delete_custom_profile_required_params()

    @responses.activate
    def test_delete_custom_profile_value_error(self):
        """
        test_delete_custom_profile_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString')
        mock_response = '{"id": "id", "profile_name": "profile_name", "profile_description": "profile_description", "profile_type": "profile_type", "profile_version": "profile_version", "version_group_label": "version_group_label", "latest": true, "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "controls_count": 14, "attachments_count": 17, "controls": [{"control_library_id": "control_library_id", "control_id": "control_id", "control_library_version": "control_library_version", "control_name": "control_name", "control_description": "control_description", "control_severity": "control_severity", "control_category": "control_category", "control_parent": "control_parent", "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}]}], "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_profile(**req_copy)

    def test_delete_custom_profile_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_profile_value_error.
        _service.enable_retries()
        self.test_delete_custom_profile_value_error()

        # Disable retries and run test_delete_custom_profile_value_error.
        _service.disable_retries()
        self.test_delete_custom_profile_value_error()


class TestReplaceProfileParameters:
    """
    Test Class for replace_profile_parameters
    """

    @responses.activate
    def test_replace_profile_parameters_all_params(self):
        """
        replace_profile_parameters()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        default_parameters = [default_parameters_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_profile_parameters(
            profiles_id,
            instance_id,
            id=id,
            default_parameters=default_parameters,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['default_parameters'] == [default_parameters_model]

    def test_replace_profile_parameters_all_params_with_retries(self):
        # Enable retries and run test_replace_profile_parameters_all_params.
        _service.enable_retries()
        self.test_replace_profile_parameters_all_params()

        # Disable retries and run test_replace_profile_parameters_all_params.
        _service.disable_retries()
        self.test_replace_profile_parameters_all_params()

    @responses.activate
    def test_replace_profile_parameters_required_params(self):
        """
        test_replace_profile_parameters_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        default_parameters = [default_parameters_model]

        # Invoke method
        response = _service.replace_profile_parameters(
            profiles_id,
            instance_id,
            id=id,
            default_parameters=default_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['default_parameters'] == [default_parameters_model]

    def test_replace_profile_parameters_required_params_with_retries(self):
        # Enable retries and run test_replace_profile_parameters_required_params.
        _service.enable_retries()
        self.test_replace_profile_parameters_required_params()

        # Disable retries and run test_replace_profile_parameters_required_params.
        _service.disable_retries()
        self.test_replace_profile_parameters_required_params()

    @responses.activate
    def test_replace_profile_parameters_value_error(self):
        """
        test_replace_profile_parameters_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/parameters')
        mock_response = '{"id": "id", "default_parameters": [{"assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameter_name": "parameter_name", "parameter_default_value": "parameter_default_value", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DefaultParameters model
        default_parameters_model = {}
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        default_parameters = [default_parameters_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_profile_parameters(**req_copy)

    def test_replace_profile_parameters_value_error_with_retries(self):
        # Enable retries and run test_replace_profile_parameters_value_error.
        _service.enable_retries()
        self.test_replace_profile_parameters_value_error()

        # Disable retries and run test_replace_profile_parameters_value_error.
        _service.disable_retries()
        self.test_replace_profile_parameters_value_error()


# endregion
##############################################################################
# End of Service: ProfileAPIs
##############################################################################

##############################################################################
# Start of Service: AttachmentAPIs
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ComplianceV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ComplianceV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ComplianceV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateAttachment:
    """
    Test Class for create_attachment
    """

    @responses.activate
    def test_create_attachment_all_params(self):
        """
        create_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "status", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "last_scan": "last_scan", "last_scan_status": "last_scan_status", "last_scan_time": "last_scan_time"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {}
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {}
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model = {}
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentPayload model
        attachment_payload_model = {}
        attachment_payload_model['id'] = 'testString'
        attachment_payload_model['account_id'] = 'testString'
        attachment_payload_model['included_scope'] = scope_payload_model
        attachment_payload_model['exclusions'] = [scope_payload_model]
        attachment_payload_model['created_by'] = 'testString'
        attachment_payload_model['created_on'] = 'testString'
        attachment_payload_model['updated_by'] = 'testString'
        attachment_payload_model['updated_on'] = 'testString'
        attachment_payload_model['status'] = 'enabled'
        attachment_payload_model['attachment_parameters'] = [parameter_details_model]
        attachment_payload_model['attachment_notifications'] = attachments_notifications_payload_model

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        attachments = [attachment_payload_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_attachment(
            profiles_id,
            instance_id,
            attachments=attachments,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [attachment_payload_model]

    def test_create_attachment_all_params_with_retries(self):
        # Enable retries and run test_create_attachment_all_params.
        _service.enable_retries()
        self.test_create_attachment_all_params()

        # Disable retries and run test_create_attachment_all_params.
        _service.disable_retries()
        self.test_create_attachment_all_params()

    @responses.activate
    def test_create_attachment_required_params(self):
        """
        test_create_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "status", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "last_scan": "last_scan", "last_scan_status": "last_scan_status", "last_scan_time": "last_scan_time"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {}
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {}
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model = {}
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentPayload model
        attachment_payload_model = {}
        attachment_payload_model['id'] = 'testString'
        attachment_payload_model['account_id'] = 'testString'
        attachment_payload_model['included_scope'] = scope_payload_model
        attachment_payload_model['exclusions'] = [scope_payload_model]
        attachment_payload_model['created_by'] = 'testString'
        attachment_payload_model['created_on'] = 'testString'
        attachment_payload_model['updated_by'] = 'testString'
        attachment_payload_model['updated_on'] = 'testString'
        attachment_payload_model['status'] = 'enabled'
        attachment_payload_model['attachment_parameters'] = [parameter_details_model]
        attachment_payload_model['attachment_notifications'] = attachments_notifications_payload_model

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        attachments = [attachment_payload_model]

        # Invoke method
        response = _service.create_attachment(
            profiles_id,
            instance_id,
            attachments=attachments,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachments'] == [attachment_payload_model]

    def test_create_attachment_required_params_with_retries(self):
        # Enable retries and run test_create_attachment_required_params.
        _service.enable_retries()
        self.test_create_attachment_required_params()

        # Disable retries and run test_create_attachment_required_params.
        _service.disable_retries()
        self.test_create_attachment_required_params()

    @responses.activate
    def test_create_attachment_value_error(self):
        """
        test_create_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments')
        mock_response = '{"profile_id": "profile_id", "attachments": [{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "status", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "last_scan": "last_scan", "last_scan_status": "last_scan_status", "last_scan_time": "last_scan_time"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {}
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {}
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model = {}
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Construct a dict representation of a AttachmentPayload model
        attachment_payload_model = {}
        attachment_payload_model['id'] = 'testString'
        attachment_payload_model['account_id'] = 'testString'
        attachment_payload_model['included_scope'] = scope_payload_model
        attachment_payload_model['exclusions'] = [scope_payload_model]
        attachment_payload_model['created_by'] = 'testString'
        attachment_payload_model['created_on'] = 'testString'
        attachment_payload_model['updated_by'] = 'testString'
        attachment_payload_model['updated_on'] = 'testString'
        attachment_payload_model['status'] = 'enabled'
        attachment_payload_model['attachment_parameters'] = [parameter_details_model]
        attachment_payload_model['attachment_notifications'] = attachments_notifications_payload_model

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        attachments = [attachment_payload_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_attachment(**req_copy)

    def test_create_attachment_value_error_with_retries(self):
        # Enable retries and run test_create_attachment_value_error.
        _service.enable_retries()
        self.test_create_attachment_value_error()

        # Disable retries and run test_create_attachment_value_error.
        _service.disable_retries()
        self.test_create_attachment_value_error()


class TestCheckProfileAttachmnets:
    """
    Test Class for check_profile_attachmnets
    """

    @responses.activate
    def test_check_profile_attachmnets_all_params(self):
        """
        check_profile_attachmnets()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments')
        mock_response = '{"total_count": 11, "limit": 5, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profile_id": "profile_id", "account_id": "account_id", "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "created_on", "created_by": "created_by", "updated_on": "updated_on", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}], "attachments": [{"attachments": [{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.check_profile_attachmnets(
            profiles_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_check_profile_attachmnets_all_params_with_retries(self):
        # Enable retries and run test_check_profile_attachmnets_all_params.
        _service.enable_retries()
        self.test_check_profile_attachmnets_all_params()

        # Disable retries and run test_check_profile_attachmnets_all_params.
        _service.disable_retries()
        self.test_check_profile_attachmnets_all_params()

    @responses.activate
    def test_check_profile_attachmnets_required_params(self):
        """
        test_check_profile_attachmnets_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments')
        mock_response = '{"total_count": 11, "limit": 5, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profile_id": "profile_id", "account_id": "account_id", "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "created_on", "created_by": "created_by", "updated_on": "updated_on", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}], "attachments": [{"attachments": [{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.check_profile_attachmnets(
            profiles_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_check_profile_attachmnets_required_params_with_retries(self):
        # Enable retries and run test_check_profile_attachmnets_required_params.
        _service.enable_retries()
        self.test_check_profile_attachmnets_required_params()

        # Disable retries and run test_check_profile_attachmnets_required_params.
        _service.disable_retries()
        self.test_check_profile_attachmnets_required_params()

    @responses.activate
    def test_check_profile_attachmnets_value_error(self):
        """
        test_check_profile_attachmnets_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments')
        mock_response = '{"total_count": 11, "limit": 5, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "profile_id": "profile_id", "account_id": "account_id", "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "created_on", "created_by": "created_by", "updated_on": "updated_on", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}], "attachments": [{"attachments": [{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.check_profile_attachmnets(**req_copy)

    def test_check_profile_attachmnets_value_error_with_retries(self):
        # Enable retries and run test_check_profile_attachmnets_value_error.
        _service.enable_retries()
        self.test_check_profile_attachmnets_value_error()

        # Disable retries and run test_check_profile_attachmnets_value_error.
        _service.disable_retries()
        self.test_check_profile_attachmnets_value_error()


class TestGetProfileAttachmnet:
    """
    Test Class for get_profile_attachmnet
    """

    @responses.activate
    def test_get_profile_attachmnet_all_params(self):
        """
        get_profile_attachmnet()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_profile_attachmnet(
            profiles_id,
            attachment_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_attachmnet_all_params_with_retries(self):
        # Enable retries and run test_get_profile_attachmnet_all_params.
        _service.enable_retries()
        self.test_get_profile_attachmnet_all_params()

        # Disable retries and run test_get_profile_attachmnet_all_params.
        _service.disable_retries()
        self.test_get_profile_attachmnet_all_params()

    @responses.activate
    def test_get_profile_attachmnet_required_params(self):
        """
        test_get_profile_attachmnet_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.get_profile_attachmnet(
            profiles_id,
            attachment_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_profile_attachmnet_required_params_with_retries(self):
        # Enable retries and run test_get_profile_attachmnet_required_params.
        _service.enable_retries()
        self.test_get_profile_attachmnet_required_params()

        # Disable retries and run test_get_profile_attachmnet_required_params.
        _service.disable_retries()
        self.test_get_profile_attachmnet_required_params()

    @responses.activate
    def test_get_profile_attachmnet_value_error(self):
        """
        test_get_profile_attachmnet_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_profile_attachmnet(**req_copy)

    def test_get_profile_attachmnet_value_error_with_retries(self):
        # Enable retries and run test_get_profile_attachmnet_value_error.
        _service.enable_retries()
        self.test_get_profile_attachmnet_value_error()

        # Disable retries and run test_get_profile_attachmnet_value_error.
        _service.disable_retries()
        self.test_get_profile_attachmnet_value_error()


class TestReplaceProfileAttachment:
    """
    Test Class for replace_profile_attachment
    """

    @responses.activate
    def test_replace_profile_attachment_all_params(self):
        """
        replace_profile_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {}
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {}
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model = {}
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        included_scope = scope_payload_model
        exclusions = [scope_payload_model]
        created_by = 'testString'
        created_on = 'testString'
        updated_by = 'testString'
        updated_on = 'testString'
        status = 'enabled'
        attachment_parameters = [parameter_details_model]
        attachment_notifications = attachments_notifications_payload_model
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_profile_attachment(
            profiles_id,
            attachment_id,
            instance_id,
            id=id,
            account_id=account_id,
            included_scope=included_scope,
            exclusions=exclusions,
            created_by=created_by,
            created_on=created_on,
            updated_by=updated_by,
            updated_on=updated_on,
            status=status,
            attachment_parameters=attachment_parameters,
            attachment_notifications=attachment_notifications,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['included_scope'] == scope_payload_model
        assert req_body['exclusions'] == [scope_payload_model]
        assert req_body['created_by'] == 'testString'
        assert req_body['created_on'] == 'testString'
        assert req_body['updated_by'] == 'testString'
        assert req_body['updated_on'] == 'testString'
        assert req_body['status'] == 'enabled'
        assert req_body['attachment_parameters'] == [parameter_details_model]
        assert req_body['attachment_notifications'] == attachments_notifications_payload_model

    def test_replace_profile_attachment_all_params_with_retries(self):
        # Enable retries and run test_replace_profile_attachment_all_params.
        _service.enable_retries()
        self.test_replace_profile_attachment_all_params()

        # Disable retries and run test_replace_profile_attachment_all_params.
        _service.disable_retries()
        self.test_replace_profile_attachment_all_params()

    @responses.activate
    def test_replace_profile_attachment_required_params(self):
        """
        test_replace_profile_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {}
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {}
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model = {}
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        included_scope = scope_payload_model
        exclusions = [scope_payload_model]
        created_by = 'testString'
        created_on = 'testString'
        updated_by = 'testString'
        updated_on = 'testString'
        status = 'enabled'
        attachment_parameters = [parameter_details_model]
        attachment_notifications = attachments_notifications_payload_model

        # Invoke method
        response = _service.replace_profile_attachment(
            profiles_id,
            attachment_id,
            instance_id,
            id=id,
            account_id=account_id,
            included_scope=included_scope,
            exclusions=exclusions,
            created_by=created_by,
            created_on=created_on,
            updated_by=updated_by,
            updated_on=updated_on,
            status=status,
            attachment_parameters=attachment_parameters,
            attachment_notifications=attachment_notifications,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['included_scope'] == scope_payload_model
        assert req_body['exclusions'] == [scope_payload_model]
        assert req_body['created_by'] == 'testString'
        assert req_body['created_on'] == 'testString'
        assert req_body['updated_by'] == 'testString'
        assert req_body['updated_on'] == 'testString'
        assert req_body['status'] == 'enabled'
        assert req_body['attachment_parameters'] == [parameter_details_model]
        assert req_body['attachment_notifications'] == attachments_notifications_payload_model

    def test_replace_profile_attachment_required_params_with_retries(self):
        # Enable retries and run test_replace_profile_attachment_required_params.
        _service.enable_retries()
        self.test_replace_profile_attachment_required_params()

        # Disable retries and run test_replace_profile_attachment_required_params.
        _service.disable_retries()
        self.test_replace_profile_attachment_required_params()

    @responses.activate
    def test_replace_profile_attachment_value_error(self):
        """
        test_replace_profile_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ScopePayload model
        scope_payload_model = {}
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ParameterDetails model
        parameter_details_model = {}
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a FailedControls model
        failed_controls_model = {}
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a dict representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model = {}
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        included_scope = scope_payload_model
        exclusions = [scope_payload_model]
        created_by = 'testString'
        created_on = 'testString'
        updated_by = 'testString'
        updated_on = 'testString'
        status = 'enabled'
        attachment_parameters = [parameter_details_model]
        attachment_notifications = attachments_notifications_payload_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_profile_attachment(**req_copy)

    def test_replace_profile_attachment_value_error_with_retries(self):
        # Enable retries and run test_replace_profile_attachment_value_error.
        _service.enable_retries()
        self.test_replace_profile_attachment_value_error()

        # Disable retries and run test_replace_profile_attachment_value_error.
        _service.disable_retries()
        self.test_replace_profile_attachment_value_error()


class TestDeleteProfileAttachmnet:
    """
    Test Class for delete_profile_attachmnet
    """

    @responses.activate
    def test_delete_profile_attachmnet_all_params(self):
        """
        delete_profile_attachmnet()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_profile_attachmnet(
            profiles_id,
            attachment_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_profile_attachmnet_all_params_with_retries(self):
        # Enable retries and run test_delete_profile_attachmnet_all_params.
        _service.enable_retries()
        self.test_delete_profile_attachmnet_all_params()

        # Disable retries and run test_delete_profile_attachmnet_all_params.
        _service.disable_retries()
        self.test_delete_profile_attachmnet_all_params()

    @responses.activate
    def test_delete_profile_attachmnet_required_params(self):
        """
        test_delete_profile_attachmnet_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.delete_profile_attachmnet(
            profiles_id,
            attachment_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_profile_attachmnet_required_params_with_retries(self):
        # Enable retries and run test_delete_profile_attachmnet_required_params.
        _service.enable_retries()
        self.test_delete_profile_attachmnet_required_params()

        # Disable retries and run test_delete_profile_attachmnet_required_params.
        _service.disable_retries()
        self.test_delete_profile_attachmnet_required_params()

    @responses.activate
    def test_delete_profile_attachmnet_value_error(self):
        """
        test_delete_profile_attachmnet_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "included_scope": {"scope_id": "scope_id", "scope_type": "scope_type"}, "exclusions": [{"scope_id": "scope_id", "scope_type": "scope_type"}], "created_by": "created_by", "created_on": "created_on", "updated_by": "updated_by", "updated_on": "updated_on", "status": "enabled", "attachment_parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}], "attachment_notifications": {"enabled": false, "controls": {"threshold_limit": 15, "failed_control_ids": ["failed_control_ids"]}}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_profile_attachmnet(**req_copy)

    def test_delete_profile_attachmnet_value_error_with_retries(self):
        # Enable retries and run test_delete_profile_attachmnet_value_error.
        _service.enable_retries()
        self.test_delete_profile_attachmnet_value_error()

        # Disable retries and run test_delete_profile_attachmnet_value_error.
        _service.disable_retries()
        self.test_delete_profile_attachmnet_value_error()


class TestListAttachmentParameters:
    """
    Test Class for list_attachment_parameters
    """

    @responses.activate
    def test_list_attachment_parameters_all_params(self):
        """
        list_attachment_parameters()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.list_attachment_parameters(
            profiles_id,
            attachment_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_attachment_parameters_all_params_with_retries(self):
        # Enable retries and run test_list_attachment_parameters_all_params.
        _service.enable_retries()
        self.test_list_attachment_parameters_all_params()

        # Disable retries and run test_list_attachment_parameters_all_params.
        _service.disable_retries()
        self.test_list_attachment_parameters_all_params()

    @responses.activate
    def test_list_attachment_parameters_required_params(self):
        """
        test_list_attachment_parameters_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.list_attachment_parameters(
            profiles_id,
            attachment_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_attachment_parameters_required_params_with_retries(self):
        # Enable retries and run test_list_attachment_parameters_required_params.
        _service.enable_retries()
        self.test_list_attachment_parameters_required_params()

        # Disable retries and run test_list_attachment_parameters_required_params.
        _service.disable_retries()
        self.test_list_attachment_parameters_required_params()

    @responses.activate
    def test_list_attachment_parameters_value_error(self):
        """
        test_list_attachment_parameters_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_attachment_parameters(**req_copy)

    def test_list_attachment_parameters_value_error_with_retries(self):
        # Enable retries and run test_list_attachment_parameters_value_error.
        _service.enable_retries()
        self.test_list_attachment_parameters_value_error()

        # Disable retries and run test_list_attachment_parameters_value_error.
        _service.disable_retries()
        self.test_list_attachment_parameters_value_error()


class TestReplaceAttachment:
    """
    Test Class for replace_attachment
    """

    @responses.activate
    def test_replace_attachment_all_params(self):
        """
        replace_attachment()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        parameter_name = 'testString'
        parameter_display_name = 'testString'
        parameter_type = 'numeric'
        parameter_value = 'testString'
        assessment_type = 'testString'
        assessment_id = 'testString'
        parameters = [parameter_info_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_attachment(
            profiles_id,
            attachment_id,
            instance_id,
            parameter_name=parameter_name,
            parameter_display_name=parameter_display_name,
            parameter_type=parameter_type,
            parameter_value=parameter_value,
            assessment_type=assessment_type,
            assessment_id=assessment_id,
            parameters=parameters,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parameter_name'] == 'testString'
        assert req_body['parameter_display_name'] == 'testString'
        assert req_body['parameter_type'] == 'numeric'
        assert req_body['parameter_value'] == 'testString'
        assert req_body['assessment_type'] == 'testString'
        assert req_body['assessment_id'] == 'testString'
        assert req_body['parameters'] == [parameter_info_model]

    def test_replace_attachment_all_params_with_retries(self):
        # Enable retries and run test_replace_attachment_all_params.
        _service.enable_retries()
        self.test_replace_attachment_all_params()

        # Disable retries and run test_replace_attachment_all_params.
        _service.disable_retries()
        self.test_replace_attachment_all_params()

    @responses.activate
    def test_replace_attachment_required_params(self):
        """
        test_replace_attachment_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        parameter_name = 'testString'
        parameter_display_name = 'testString'
        parameter_type = 'numeric'
        parameter_value = 'testString'
        assessment_type = 'testString'
        assessment_id = 'testString'
        parameters = [parameter_info_model]

        # Invoke method
        response = _service.replace_attachment(
            profiles_id,
            attachment_id,
            instance_id,
            parameter_name=parameter_name,
            parameter_display_name=parameter_display_name,
            parameter_type=parameter_type,
            parameter_value=parameter_value,
            assessment_type=assessment_type,
            assessment_id=assessment_id,
            parameters=parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parameter_name'] == 'testString'
        assert req_body['parameter_display_name'] == 'testString'
        assert req_body['parameter_type'] == 'numeric'
        assert req_body['parameter_value'] == 'testString'
        assert req_body['assessment_type'] == 'testString'
        assert req_body['assessment_id'] == 'testString'
        assert req_body['parameters'] == [parameter_info_model]

    def test_replace_attachment_required_params_with_retries(self):
        # Enable retries and run test_replace_attachment_required_params.
        _service.enable_retries()
        self.test_replace_attachment_required_params()

        # Disable retries and run test_replace_attachment_required_params.
        _service.disable_retries()
        self.test_replace_attachment_required_params()

    @responses.activate
    def test_replace_attachment_value_error(self):
        """
        test_replace_attachment_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        instance_id = 'testString'
        parameter_name = 'testString'
        parameter_display_name = 'testString'
        parameter_type = 'numeric'
        parameter_value = 'testString'
        assessment_type = 'testString'
        assessment_id = 'testString'
        parameters = [parameter_info_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_attachment(**req_copy)

    def test_replace_attachment_value_error_with_retries(self):
        # Enable retries and run test_replace_attachment_value_error.
        _service.enable_retries()
        self.test_replace_attachment_value_error()

        # Disable retries and run test_replace_attachment_value_error.
        _service.disable_retries()
        self.test_replace_attachment_value_error()


class TestGetParametersByName:
    """
    Test Class for get_parameters_by_name
    """

    @responses.activate
    def test_get_parameters_by_name_all_params(self):
        """
        get_parameters_by_name()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters/testString')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        parameter_name = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_parameters_by_name(
            profiles_id,
            attachment_id,
            parameter_name,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_parameters_by_name_all_params_with_retries(self):
        # Enable retries and run test_get_parameters_by_name_all_params.
        _service.enable_retries()
        self.test_get_parameters_by_name_all_params()

        # Disable retries and run test_get_parameters_by_name_all_params.
        _service.disable_retries()
        self.test_get_parameters_by_name_all_params()

    @responses.activate
    def test_get_parameters_by_name_required_params(self):
        """
        test_get_parameters_by_name_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters/testString')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        parameter_name = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.get_parameters_by_name(
            profiles_id,
            attachment_id,
            parameter_name,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_parameters_by_name_required_params_with_retries(self):
        # Enable retries and run test_get_parameters_by_name_required_params.
        _service.enable_retries()
        self.test_get_parameters_by_name_required_params()

        # Disable retries and run test_get_parameters_by_name_required_params.
        _service.disable_retries()
        self.test_get_parameters_by_name_required_params()

    @responses.activate
    def test_get_parameters_by_name_value_error(self):
        """
        test_get_parameters_by_name_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters/testString')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        parameter_name = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "parameter_name": parameter_name,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_parameters_by_name(**req_copy)

    def test_get_parameters_by_name_value_error_with_retries(self):
        # Enable retries and run test_get_parameters_by_name_value_error.
        _service.enable_retries()
        self.test_get_parameters_by_name_value_error()

        # Disable retries and run test_get_parameters_by_name_value_error.
        _service.disable_retries()
        self.test_get_parameters_by_name_value_error()


class TestReplaceAttachmnetParametersByName:
    """
    Test Class for replace_attachmnet_parameters_by_name
    """

    @responses.activate
    def test_replace_attachmnet_parameters_by_name_all_params(self):
        """
        replace_attachmnet_parameters_by_name()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters/testString')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        parameter_name = 'testString'
        instance_id = 'testString'
        new_parameter_name = 'testString'
        new_parameter_display_name = 'testString'
        new_parameter_type = 'numeric'
        new_parameter_value = 'testString'
        new_assessment_type = 'testString'
        new_assessment_id = 'testString'
        new_parameters = [parameter_info_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_attachmnet_parameters_by_name(
            profiles_id,
            attachment_id,
            parameter_name,
            instance_id,
            new_parameter_name=new_parameter_name,
            new_parameter_display_name=new_parameter_display_name,
            new_parameter_type=new_parameter_type,
            new_parameter_value=new_parameter_value,
            new_assessment_type=new_assessment_type,
            new_assessment_id=new_assessment_id,
            new_parameters=new_parameters,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parameter_name'] == 'testString'
        assert req_body['parameter_display_name'] == 'testString'
        assert req_body['parameter_type'] == 'numeric'
        assert req_body['parameter_value'] == 'testString'
        assert req_body['assessment_type'] == 'testString'
        assert req_body['assessment_id'] == 'testString'
        assert req_body['parameters'] == [parameter_info_model]

    def test_replace_attachmnet_parameters_by_name_all_params_with_retries(self):
        # Enable retries and run test_replace_attachmnet_parameters_by_name_all_params.
        _service.enable_retries()
        self.test_replace_attachmnet_parameters_by_name_all_params()

        # Disable retries and run test_replace_attachmnet_parameters_by_name_all_params.
        _service.disable_retries()
        self.test_replace_attachmnet_parameters_by_name_all_params()

    @responses.activate
    def test_replace_attachmnet_parameters_by_name_required_params(self):
        """
        test_replace_attachmnet_parameters_by_name_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters/testString')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        parameter_name = 'testString'
        instance_id = 'testString'
        new_parameter_name = 'testString'
        new_parameter_display_name = 'testString'
        new_parameter_type = 'numeric'
        new_parameter_value = 'testString'
        new_assessment_type = 'testString'
        new_assessment_id = 'testString'
        new_parameters = [parameter_info_model]

        # Invoke method
        response = _service.replace_attachmnet_parameters_by_name(
            profiles_id,
            attachment_id,
            parameter_name,
            instance_id,
            new_parameter_name=new_parameter_name,
            new_parameter_display_name=new_parameter_display_name,
            new_parameter_type=new_parameter_type,
            new_parameter_value=new_parameter_value,
            new_assessment_type=new_assessment_type,
            new_assessment_id=new_assessment_id,
            new_parameters=new_parameters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['parameter_name'] == 'testString'
        assert req_body['parameter_display_name'] == 'testString'
        assert req_body['parameter_type'] == 'numeric'
        assert req_body['parameter_value'] == 'testString'
        assert req_body['assessment_type'] == 'testString'
        assert req_body['assessment_id'] == 'testString'
        assert req_body['parameters'] == [parameter_info_model]

    def test_replace_attachmnet_parameters_by_name_required_params_with_retries(self):
        # Enable retries and run test_replace_attachmnet_parameters_by_name_required_params.
        _service.enable_retries()
        self.test_replace_attachmnet_parameters_by_name_required_params()

        # Disable retries and run test_replace_attachmnet_parameters_by_name_required_params.
        _service.disable_retries()
        self.test_replace_attachmnet_parameters_by_name_required_params()

    @responses.activate
    def test_replace_attachmnet_parameters_by_name_value_error(self):
        """
        test_replace_attachmnet_parameters_by_name_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/profiles/testString/attachments/testString/parameters/testString')
        mock_response = '{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric", "parameter_value": "parameter_value", "assessment_type": "assessment_type", "assessment_id": "assessment_id", "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Set up parameter values
        profiles_id = 'testString'
        attachment_id = 'testString'
        parameter_name = 'testString'
        instance_id = 'testString'
        new_parameter_name = 'testString'
        new_parameter_display_name = 'testString'
        new_parameter_type = 'numeric'
        new_parameter_value = 'testString'
        new_assessment_type = 'testString'
        new_assessment_id = 'testString'
        new_parameters = [parameter_info_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "profiles_id": profiles_id,
            "attachment_id": attachment_id,
            "parameter_name": parameter_name,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_attachmnet_parameters_by_name(**req_copy)

    def test_replace_attachmnet_parameters_by_name_value_error_with_retries(self):
        # Enable retries and run test_replace_attachmnet_parameters_by_name_value_error.
        _service.enable_retries()
        self.test_replace_attachmnet_parameters_by_name_value_error()

        # Disable retries and run test_replace_attachmnet_parameters_by_name_value_error.
        _service.disable_retries()
        self.test_replace_attachmnet_parameters_by_name_value_error()


# endregion
##############################################################################
# End of Service: AttachmentAPIs
##############################################################################

##############################################################################
# Start of Service: ControlLibraryAPIs
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ComplianceV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ComplianceV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ComplianceV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateCustomControlLibrary:
    """
    Test Class for create_custom_control_library
    """

    @responses.activate
    def test_create_custom_control_library_all_params(self):
        """
        create_custom_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {}
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {}
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'testString'
        control_library_description = 'testString'
        control_library_type = 'predefined'
        version_group_label = 'testString'
        control_library_version = 'testString'
        latest = True
        controls_count = 38
        controls = [controls_in_control_lib_request_payload_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_custom_control_library(
            instance_id,
            id=id,
            account_id=account_id,
            control_library_name=control_library_name,
            control_library_description=control_library_description,
            control_library_type=control_library_type,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            latest=latest,
            controls_count=controls_count,
            controls=controls,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['control_library_name'] == 'testString'
        assert req_body['control_library_description'] == 'testString'
        assert req_body['control_library_type'] == 'predefined'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['control_library_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['controls_count'] == 38
        assert req_body['controls'] == [controls_in_control_lib_request_payload_model]

    def test_create_custom_control_library_all_params_with_retries(self):
        # Enable retries and run test_create_custom_control_library_all_params.
        _service.enable_retries()
        self.test_create_custom_control_library_all_params()

        # Disable retries and run test_create_custom_control_library_all_params.
        _service.disable_retries()
        self.test_create_custom_control_library_all_params()

    @responses.activate
    def test_create_custom_control_library_required_params(self):
        """
        test_create_custom_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {}
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {}
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'testString'
        control_library_description = 'testString'
        control_library_type = 'predefined'
        version_group_label = 'testString'
        control_library_version = 'testString'
        latest = True
        controls_count = 38
        controls = [controls_in_control_lib_request_payload_model]

        # Invoke method
        response = _service.create_custom_control_library(
            instance_id,
            id=id,
            account_id=account_id,
            control_library_name=control_library_name,
            control_library_description=control_library_description,
            control_library_type=control_library_type,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            latest=latest,
            controls_count=controls_count,
            controls=controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['control_library_name'] == 'testString'
        assert req_body['control_library_description'] == 'testString'
        assert req_body['control_library_type'] == 'predefined'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['control_library_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['controls_count'] == 38
        assert req_body['controls'] == [controls_in_control_lib_request_payload_model]

    def test_create_custom_control_library_required_params_with_retries(self):
        # Enable retries and run test_create_custom_control_library_required_params.
        _service.enable_retries()
        self.test_create_custom_control_library_required_params()

        # Disable retries and run test_create_custom_control_library_required_params.
        _service.disable_retries()
        self.test_create_custom_control_library_required_params()

    @responses.activate
    def test_create_custom_control_library_value_error(self):
        """
        test_create_custom_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {}
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {}
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'testString'
        control_library_description = 'testString'
        control_library_type = 'predefined'
        version_group_label = 'testString'
        control_library_version = 'testString'
        latest = True
        controls_count = 38
        controls = [controls_in_control_lib_request_payload_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_custom_control_library(**req_copy)

    def test_create_custom_control_library_value_error_with_retries(self):
        # Enable retries and run test_create_custom_control_library_value_error.
        _service.enable_retries()
        self.test_create_custom_control_library_value_error()

        # Disable retries and run test_create_custom_control_library_value_error.
        _service.disable_retries()
        self.test_create_custom_control_library_value_error()


class TestListControlLibraries:
    """
    Test Class for list_control_libraries
    """

    @responses.activate
    def test_list_control_libraries_all_params(self):
        """
        list_control_libraries()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "created_on", "created_by": "created_by", "updated_on": "updated_on", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.list_control_libraries(
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_control_libraries_all_params_with_retries(self):
        # Enable retries and run test_list_control_libraries_all_params.
        _service.enable_retries()
        self.test_list_control_libraries_all_params()

        # Disable retries and run test_list_control_libraries_all_params.
        _service.disable_retries()
        self.test_list_control_libraries_all_params()

    @responses.activate
    def test_list_control_libraries_required_params(self):
        """
        test_list_control_libraries_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "created_on", "created_by": "created_by", "updated_on": "updated_on", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_control_libraries(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_control_libraries_required_params_with_retries(self):
        # Enable retries and run test_list_control_libraries_required_params.
        _service.enable_retries()
        self.test_list_control_libraries_required_params()

        # Disable retries and run test_list_control_libraries_required_params.
        _service.disable_retries()
        self.test_list_control_libraries_required_params()

    @responses.activate
    def test_list_control_libraries_value_error(self):
        """
        test_list_control_libraries_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries')
        mock_response = '{"total_count": 1, "limit": 20, "first": {"href": "href"}, "next": {"href": "href", "start": "start"}, "control_libraries": [{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "control_library_type", "created_on": "created_on", "created_by": "created_by", "updated_on": "updated_on", "updated_by": "updated_by", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_control_libraries(**req_copy)

    def test_list_control_libraries_value_error_with_retries(self):
        # Enable retries and run test_list_control_libraries_value_error.
        _service.enable_retries()
        self.test_list_control_libraries_value_error()

        # Disable retries and run test_list_control_libraries_value_error.
        _service.disable_retries()
        self.test_list_control_libraries_value_error()


class TestReplaceCustomControlLibrary:
    """
    Test Class for replace_custom_control_library
    """

    @responses.activate
    def test_replace_custom_control_library_all_params(self):
        """
        replace_custom_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {}
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {}
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'testString'
        control_library_description = 'testString'
        control_library_type = 'predefined'
        version_group_label = 'testString'
        control_library_version = 'testString'
        latest = True
        controls_count = 38
        controls = [controls_in_control_lib_request_payload_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.replace_custom_control_library(
            control_libraries_id,
            instance_id,
            id=id,
            account_id=account_id,
            control_library_name=control_library_name,
            control_library_description=control_library_description,
            control_library_type=control_library_type,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            latest=latest,
            controls_count=controls_count,
            controls=controls,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['control_library_name'] == 'testString'
        assert req_body['control_library_description'] == 'testString'
        assert req_body['control_library_type'] == 'predefined'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['control_library_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['controls_count'] == 38
        assert req_body['controls'] == [controls_in_control_lib_request_payload_model]

    def test_replace_custom_control_library_all_params_with_retries(self):
        # Enable retries and run test_replace_custom_control_library_all_params.
        _service.enable_retries()
        self.test_replace_custom_control_library_all_params()

        # Disable retries and run test_replace_custom_control_library_all_params.
        _service.disable_retries()
        self.test_replace_custom_control_library_all_params()

    @responses.activate
    def test_replace_custom_control_library_required_params(self):
        """
        test_replace_custom_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {}
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {}
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'testString'
        control_library_description = 'testString'
        control_library_type = 'predefined'
        version_group_label = 'testString'
        control_library_version = 'testString'
        latest = True
        controls_count = 38
        controls = [controls_in_control_lib_request_payload_model]

        # Invoke method
        response = _service.replace_custom_control_library(
            control_libraries_id,
            instance_id,
            id=id,
            account_id=account_id,
            control_library_name=control_library_name,
            control_library_description=control_library_description,
            control_library_type=control_library_type,
            version_group_label=version_group_label,
            control_library_version=control_library_version,
            latest=latest,
            controls_count=controls_count,
            controls=controls,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == 'testString'
        assert req_body['account_id'] == 'testString'
        assert req_body['control_library_name'] == 'testString'
        assert req_body['control_library_description'] == 'testString'
        assert req_body['control_library_type'] == 'predefined'
        assert req_body['version_group_label'] == 'testString'
        assert req_body['control_library_version'] == 'testString'
        assert req_body['latest'] == True
        assert req_body['controls_count'] == 38
        assert req_body['controls'] == [controls_in_control_lib_request_payload_model]

    def test_replace_custom_control_library_required_params_with_retries(self):
        # Enable retries and run test_replace_custom_control_library_required_params.
        _service.enable_retries()
        self.test_replace_custom_control_library_required_params()

        # Disable retries and run test_replace_custom_control_library_required_params.
        _service.disable_retries()
        self.test_replace_custom_control_library_required_params()

    @responses.activate
    def test_replace_custom_control_library_value_error(self):
        """
        test_replace_custom_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ParameterInfo model
        parameter_info_model = {}
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a dict representation of a ImplementationPayload model
        implementation_payload_model = {}
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a dict representation of a ControlSpecifications model
        control_specifications_model = {}
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a dict representation of a ControlDocs model
        control_docs_model = {}
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a dict representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model = {}
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'
        id = 'testString'
        account_id = 'testString'
        control_library_name = 'testString'
        control_library_description = 'testString'
        control_library_type = 'predefined'
        version_group_label = 'testString'
        control_library_version = 'testString'
        latest = True
        controls_count = 38
        controls = [controls_in_control_lib_request_payload_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_libraries_id": control_libraries_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_custom_control_library(**req_copy)

    def test_replace_custom_control_library_value_error_with_retries(self):
        # Enable retries and run test_replace_custom_control_library_value_error.
        _service.enable_retries()
        self.test_replace_custom_control_library_value_error()

        # Disable retries and run test_replace_custom_control_library_value_error.
        _service.disable_retries()
        self.test_replace_custom_control_library_value_error()


class TestGetControlLibrary:
    """
    Test Class for get_control_library
    """

    @responses.activate
    def test_get_control_library_all_params(self):
        """
        get_control_library()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_control_library(
            control_libraries_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_control_library_all_params_with_retries(self):
        # Enable retries and run test_get_control_library_all_params.
        _service.enable_retries()
        self.test_get_control_library_all_params()

        # Disable retries and run test_get_control_library_all_params.
        _service.disable_retries()
        self.test_get_control_library_all_params()

    @responses.activate
    def test_get_control_library_required_params(self):
        """
        test_get_control_library_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.get_control_library(
            control_libraries_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_control_library_required_params_with_retries(self):
        # Enable retries and run test_get_control_library_required_params.
        _service.enable_retries()
        self.test_get_control_library_required_params()

        # Disable retries and run test_get_control_library_required_params.
        _service.disable_retries()
        self.test_get_control_library_required_params()

    @responses.activate
    def test_get_control_library_value_error(self):
        """
        test_get_control_library_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_libraries_id": control_libraries_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_control_library(**req_copy)

    def test_get_control_library_value_error_with_retries(self):
        # Enable retries and run test_get_control_library_value_error.
        _service.enable_retries()
        self.test_get_control_library_value_error()

        # Disable retries and run test_get_control_library_value_error.
        _service.disable_retries()
        self.test_get_control_library_value_error()


class TestDeleteCustomControllibrary:
    """
    Test Class for delete_custom_controllibrary
    """

    @responses.activate
    def test_delete_custom_controllibrary_all_params(self):
        """
        delete_custom_controllibrary()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_custom_controllibrary(
            control_libraries_id,
            instance_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_controllibrary_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_controllibrary_all_params.
        _service.enable_retries()
        self.test_delete_custom_controllibrary_all_params()

        # Disable retries and run test_delete_custom_controllibrary_all_params.
        _service.disable_retries()
        self.test_delete_custom_controllibrary_all_params()

    @responses.activate
    def test_delete_custom_controllibrary_required_params(self):
        """
        test_delete_custom_controllibrary_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'

        # Invoke method
        response = _service.delete_custom_controllibrary(
            control_libraries_id,
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_controllibrary_required_params_with_retries(self):
        # Enable retries and run test_delete_custom_controllibrary_required_params.
        _service.enable_retries()
        self.test_delete_custom_controllibrary_required_params()

        # Disable retries and run test_delete_custom_controllibrary_required_params.
        _service.disable_retries()
        self.test_delete_custom_controllibrary_required_params()

    @responses.activate
    def test_delete_custom_controllibrary_value_error(self):
        """
        test_delete_custom_controllibrary_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/control_libraries/testString')
        mock_response = '{"id": "id", "account_id": "account_id", "control_library_name": "control_library_name", "control_library_description": "control_library_description", "control_library_type": "predefined", "version_group_label": "version_group_label", "control_library_version": "control_library_version", "latest": true, "controls_count": 14, "controls": [{"control_name": "control_name", "control_id": "control_id", "control_description": "control_description", "control_category": "control_category", "control_parent": "control_parent", "control_severity": "control_severity", "control_tags": ["control_tags"], "control_specifications": [{"id": "id", "responsibility": "user", "component_id": "component_id", "environment": "environment", "description": "description", "assessments_count": 17, "assessments": [{"assessment_id": "assessment_id", "assessment_method": "assessment_method", "assessment_type": "assessment_type", "assessment_description": "assessment_description", "parameter_count": 15, "parameters": [{"parameter_name": "parameter_name", "parameter_display_name": "parameter_display_name", "parameter_type": "numeric"}]}]}], "control_docs": {"control_docs_id": "control_docs_id", "control_docs_type": "control_docs_type"}, "status": "enabled"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        control_libraries_id = 'testString'
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "control_libraries_id": control_libraries_id,
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_controllibrary(**req_copy)

    def test_delete_custom_controllibrary_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_controllibrary_value_error.
        _service.enable_retries()
        self.test_delete_custom_controllibrary_value_error()

        # Disable retries and run test_delete_custom_controllibrary_value_error.
        _service.disable_retries()
        self.test_delete_custom_controllibrary_value_error()


# endregion
##############################################################################
# End of Service: ControlLibraryAPIs
##############################################################################

##############################################################################
# Start of Service: ScanAPI
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ComplianceV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ComplianceV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ComplianceV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateScan:
    """
    Test Class for create_scan
    """

    @responses.activate
    def test_create_scan_all_params(self):
        """
        create_scan()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "status", "last_scan_time": "last_scan_time", "next_scan_time": "next_scan_time", "scan_type": "scan_type", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        attachment_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_scan(
            instance_id,
            attachment_id=attachment_id,
            transaction_id=transaction_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_id'] == 'testString'

    def test_create_scan_all_params_with_retries(self):
        # Enable retries and run test_create_scan_all_params.
        _service.enable_retries()
        self.test_create_scan_all_params()

        # Disable retries and run test_create_scan_all_params.
        _service.disable_retries()
        self.test_create_scan_all_params()

    @responses.activate
    def test_create_scan_required_params(self):
        """
        test_create_scan_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "status", "last_scan_time": "last_scan_time", "next_scan_time": "next_scan_time", "scan_type": "scan_type", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        attachment_id = 'testString'

        # Invoke method
        response = _service.create_scan(
            instance_id,
            attachment_id=attachment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['attachment_id'] == 'testString'

    def test_create_scan_required_params_with_retries(self):
        # Enable retries and run test_create_scan_required_params.
        _service.enable_retries()
        self.test_create_scan_required_params()

        # Disable retries and run test_create_scan_required_params.
        _service.disable_retries()
        self.test_create_scan_required_params()

    @responses.activate
    def test_create_scan_value_error(self):
        """
        test_create_scan_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/v3/scans')
        mock_response = '{"id": "id", "account_id": "account_id", "attachment_id": "attachment_id", "report_id": "report_id", "status": "status", "last_scan_time": "last_scan_time", "next_scan_time": "next_scan_time", "scan_type": "scan_type", "occurence": 9}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        attachment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_scan(**req_copy)

    def test_create_scan_value_error_with_retries(self):
        # Enable retries and run test_create_scan_value_error.
        _service.enable_retries()
        self.test_create_scan_value_error()

        # Disable retries and run test_create_scan_value_error.
        _service.disable_retries()
        self.test_create_scan_value_error()


# endregion
##############################################################################
# End of Service: ScanAPI
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AttachmentPayload:
    """
    Test Class for AttachmentPayload
    """

    def test_attachment_payload_serialization(self):
        """
        Test serialization/deserialization for AttachmentPayload
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_payload_model = {}  # ScopePayload
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        parameter_details_model = {}  # ParameterDetails
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        attachments_notifications_payload_model = {}  # AttachmentsNotificationsPayload
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        # Construct a json representation of a AttachmentPayload model
        attachment_payload_model_json = {}
        attachment_payload_model_json['id'] = 'testString'
        attachment_payload_model_json['account_id'] = 'testString'
        attachment_payload_model_json['included_scope'] = scope_payload_model
        attachment_payload_model_json['exclusions'] = [scope_payload_model]
        attachment_payload_model_json['created_by'] = 'testString'
        attachment_payload_model_json['created_on'] = 'testString'
        attachment_payload_model_json['updated_by'] = 'testString'
        attachment_payload_model_json['updated_on'] = 'testString'
        attachment_payload_model_json['status'] = 'enabled'
        attachment_payload_model_json['attachment_parameters'] = [parameter_details_model]
        attachment_payload_model_json['attachment_notifications'] = attachments_notifications_payload_model

        # Construct a model instance of AttachmentPayload by calling from_dict on the json representation
        attachment_payload_model = AttachmentPayload.from_dict(attachment_payload_model_json)
        assert attachment_payload_model != False

        # Construct a model instance of AttachmentPayload by calling from_dict on the json representation
        attachment_payload_model_dict = AttachmentPayload.from_dict(attachment_payload_model_json).__dict__
        attachment_payload_model2 = AttachmentPayload(**attachment_payload_model_dict)

        # Verify the model instances are equivalent
        assert attachment_payload_model == attachment_payload_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_payload_model_json2 = attachment_payload_model.to_dict()
        assert attachment_payload_model_json2 == attachment_payload_model_json


class TestModel_AttachmentProfileRequest:
    """
    Test Class for AttachmentProfileRequest
    """

    def test_attachment_profile_request_serialization(self):
        """
        Test serialization/deserialization for AttachmentProfileRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_payload_model = {}  # ScopePayload
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        parameter_details_model = {}  # ParameterDetails
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        attachments_notifications_payload_model = {}  # AttachmentsNotificationsPayload
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        attachment_payload_model = {}  # AttachmentPayload
        attachment_payload_model['id'] = 'testString'
        attachment_payload_model['account_id'] = 'testString'
        attachment_payload_model['included_scope'] = scope_payload_model
        attachment_payload_model['exclusions'] = [scope_payload_model]
        attachment_payload_model['created_by'] = 'testString'
        attachment_payload_model['created_on'] = 'testString'
        attachment_payload_model['updated_by'] = 'testString'
        attachment_payload_model['updated_on'] = 'testString'
        attachment_payload_model['status'] = 'enabled'
        attachment_payload_model['attachment_parameters'] = [parameter_details_model]
        attachment_payload_model['attachment_notifications'] = attachments_notifications_payload_model

        # Construct a json representation of a AttachmentProfileRequest model
        attachment_profile_request_model_json = {}
        attachment_profile_request_model_json['attachments'] = [attachment_payload_model]

        # Construct a model instance of AttachmentProfileRequest by calling from_dict on the json representation
        attachment_profile_request_model = AttachmentProfileRequest.from_dict(attachment_profile_request_model_json)
        assert attachment_profile_request_model != False

        # Construct a model instance of AttachmentProfileRequest by calling from_dict on the json representation
        attachment_profile_request_model_dict = AttachmentProfileRequest.from_dict(attachment_profile_request_model_json).__dict__
        attachment_profile_request_model2 = AttachmentProfileRequest(**attachment_profile_request_model_dict)

        # Verify the model instances are equivalent
        assert attachment_profile_request_model == attachment_profile_request_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_profile_request_model_json2 = attachment_profile_request_model.to_dict()
        assert attachment_profile_request_model_json2 == attachment_profile_request_model_json


class TestModel_AttachmentProfileResponse:
    """
    Test Class for AttachmentProfileResponse
    """

    def test_attachment_profile_response_serialization(self):
        """
        Test serialization/deserialization for AttachmentProfileResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_payload_model = {}  # ScopePayload
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        parameter_details_model = {}  # ParameterDetails
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        attachment_response_model = {}  # AttachmentResponse
        attachment_response_model['id'] = 'testString'
        attachment_response_model['account_id'] = 'testString'
        attachment_response_model['included_scope'] = scope_payload_model
        attachment_response_model['exclusions'] = [scope_payload_model]
        attachment_response_model['created_by'] = 'testString'
        attachment_response_model['created_on'] = 'testString'
        attachment_response_model['updated_by'] = 'testString'
        attachment_response_model['updated_on'] = 'testString'
        attachment_response_model['status'] = 'testString'
        attachment_response_model['attachment_parameters'] = [parameter_details_model]
        attachment_response_model['last_scan'] = 'testString'
        attachment_response_model['last_scan_status'] = 'testString'
        attachment_response_model['last_scan_time'] = 'testString'

        # Construct a json representation of a AttachmentProfileResponse model
        attachment_profile_response_model_json = {}
        attachment_profile_response_model_json['profile_id'] = 'testString'
        attachment_profile_response_model_json['attachments'] = [attachment_response_model]

        # Construct a model instance of AttachmentProfileResponse by calling from_dict on the json representation
        attachment_profile_response_model = AttachmentProfileResponse.from_dict(attachment_profile_response_model_json)
        assert attachment_profile_response_model != False

        # Construct a model instance of AttachmentProfileResponse by calling from_dict on the json representation
        attachment_profile_response_model_dict = AttachmentProfileResponse.from_dict(attachment_profile_response_model_json).__dict__
        attachment_profile_response_model2 = AttachmentProfileResponse(**attachment_profile_response_model_dict)

        # Verify the model instances are equivalent
        assert attachment_profile_response_model == attachment_profile_response_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_profile_response_model_json2 = attachment_profile_response_model.to_dict()
        assert attachment_profile_response_model_json2 == attachment_profile_response_model_json


class TestModel_AttachmentResponse:
    """
    Test Class for AttachmentResponse
    """

    def test_attachment_response_serialization(self):
        """
        Test serialization/deserialization for AttachmentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        scope_payload_model = {}  # ScopePayload
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        parameter_details_model = {}  # ParameterDetails
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        # Construct a json representation of a AttachmentResponse model
        attachment_response_model_json = {}
        attachment_response_model_json['id'] = 'testString'
        attachment_response_model_json['account_id'] = 'testString'
        attachment_response_model_json['included_scope'] = scope_payload_model
        attachment_response_model_json['exclusions'] = [scope_payload_model]
        attachment_response_model_json['created_by'] = 'testString'
        attachment_response_model_json['created_on'] = 'testString'
        attachment_response_model_json['updated_by'] = 'testString'
        attachment_response_model_json['updated_on'] = 'testString'
        attachment_response_model_json['status'] = 'testString'
        attachment_response_model_json['attachment_parameters'] = [parameter_details_model]
        attachment_response_model_json['last_scan'] = 'testString'
        attachment_response_model_json['last_scan_status'] = 'testString'
        attachment_response_model_json['last_scan_time'] = 'testString'

        # Construct a model instance of AttachmentResponse by calling from_dict on the json representation
        attachment_response_model = AttachmentResponse.from_dict(attachment_response_model_json)
        assert attachment_response_model != False

        # Construct a model instance of AttachmentResponse by calling from_dict on the json representation
        attachment_response_model_dict = AttachmentResponse.from_dict(attachment_response_model_json).__dict__
        attachment_response_model2 = AttachmentResponse(**attachment_response_model_dict)

        # Verify the model instances are equivalent
        assert attachment_response_model == attachment_response_model2

        # Convert model instance back to dict and verify no loss of data
        attachment_response_model_json2 = attachment_response_model.to_dict()
        assert attachment_response_model_json2 == attachment_response_model_json


class TestModel_ControlDocs:
    """
    Test Class for ControlDocs
    """

    def test_control_docs_serialization(self):
        """
        Test serialization/deserialization for ControlDocs
        """

        # Construct a json representation of a ControlDocs model
        control_docs_model_json = {}
        control_docs_model_json['control_docs_id'] = 'testString'
        control_docs_model_json['control_docs_type'] = 'testString'

        # Construct a model instance of ControlDocs by calling from_dict on the json representation
        control_docs_model = ControlDocs.from_dict(control_docs_model_json)
        assert control_docs_model != False

        # Construct a model instance of ControlDocs by calling from_dict on the json representation
        control_docs_model_dict = ControlDocs.from_dict(control_docs_model_json).__dict__
        control_docs_model2 = ControlDocs(**control_docs_model_dict)

        # Verify the model instances are equivalent
        assert control_docs_model == control_docs_model2

        # Convert model instance back to dict and verify no loss of data
        control_docs_model_json2 = control_docs_model.to_dict()
        assert control_docs_model_json2 == control_docs_model_json


class TestModel_ControlLibraryListResponse:
    """
    Test Class for ControlLibraryListResponse
    """

    def test_control_library_list_response_serialization(self):
        """
        Test serialization/deserialization for ControlLibraryListResponse
        """

        # Construct a json representation of a ControlLibraryListResponse model
        control_library_list_response_model_json = {}
        control_library_list_response_model_json['id'] = 'testString'
        control_library_list_response_model_json['account_id'] = 'testString'
        control_library_list_response_model_json['control_library_name'] = 'testString'
        control_library_list_response_model_json['control_library_description'] = 'testString'
        control_library_list_response_model_json['control_library_type'] = 'testString'
        control_library_list_response_model_json['created_on'] = 'testString'
        control_library_list_response_model_json['created_by'] = 'testString'
        control_library_list_response_model_json['updated_on'] = 'testString'
        control_library_list_response_model_json['updated_by'] = 'testString'
        control_library_list_response_model_json['version_group_label'] = 'testString'
        control_library_list_response_model_json['control_library_version'] = 'testString'
        control_library_list_response_model_json['latest'] = True
        control_library_list_response_model_json['controls_count'] = 38

        # Construct a model instance of ControlLibraryListResponse by calling from_dict on the json representation
        control_library_list_response_model = ControlLibraryListResponse.from_dict(control_library_list_response_model_json)
        assert control_library_list_response_model != False

        # Construct a model instance of ControlLibraryListResponse by calling from_dict on the json representation
        control_library_list_response_model_dict = ControlLibraryListResponse.from_dict(control_library_list_response_model_json).__dict__
        control_library_list_response_model2 = ControlLibraryListResponse(**control_library_list_response_model_dict)

        # Verify the model instances are equivalent
        assert control_library_list_response_model == control_library_list_response_model2

        # Convert model instance back to dict and verify no loss of data
        control_library_list_response_model_json2 = control_library_list_response_model.to_dict()
        assert control_library_list_response_model_json2 == control_library_list_response_model_json


class TestModel_ControlLibraryRequest:
    """
    Test Class for ControlLibraryRequest
    """

    def test_control_library_request_serialization(self):
        """
        Test serialization/deserialization for ControlLibraryRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        implementation_payload_model = {}  # ImplementationPayload
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        controls_in_control_lib_request_payload_model = {}  # ControlsInControlLibRequestPayload
        controls_in_control_lib_request_payload_model['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model['status'] = 'enabled'

        # Construct a json representation of a ControlLibraryRequest model
        control_library_request_model_json = {}
        control_library_request_model_json['id'] = 'testString'
        control_library_request_model_json['account_id'] = 'testString'
        control_library_request_model_json['control_library_name'] = 'testString'
        control_library_request_model_json['control_library_description'] = 'testString'
        control_library_request_model_json['control_library_type'] = 'predefined'
        control_library_request_model_json['version_group_label'] = 'testString'
        control_library_request_model_json['control_library_version'] = 'testString'
        control_library_request_model_json['latest'] = True
        control_library_request_model_json['controls_count'] = 38
        control_library_request_model_json['controls'] = [controls_in_control_lib_request_payload_model]

        # Construct a model instance of ControlLibraryRequest by calling from_dict on the json representation
        control_library_request_model = ControlLibraryRequest.from_dict(control_library_request_model_json)
        assert control_library_request_model != False

        # Construct a model instance of ControlLibraryRequest by calling from_dict on the json representation
        control_library_request_model_dict = ControlLibraryRequest.from_dict(control_library_request_model_json).__dict__
        control_library_request_model2 = ControlLibraryRequest(**control_library_request_model_dict)

        # Verify the model instances are equivalent
        assert control_library_request_model == control_library_request_model2

        # Convert model instance back to dict and verify no loss of data
        control_library_request_model_json2 = control_library_request_model.to_dict()
        assert control_library_request_model_json2 == control_library_request_model_json


class TestModel_ControlSpecifications:
    """
    Test Class for ControlSpecifications
    """

    def test_control_specifications_serialization(self):
        """
        Test serialization/deserialization for ControlSpecifications
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        implementation_payload_model = {}  # ImplementationPayload
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        # Construct a json representation of a ControlSpecifications model
        control_specifications_model_json = {}
        control_specifications_model_json['id'] = 'testString'
        control_specifications_model_json['responsibility'] = 'user'
        control_specifications_model_json['component_id'] = 'testString'
        control_specifications_model_json['environment'] = 'testString'
        control_specifications_model_json['description'] = 'testString'
        control_specifications_model_json['assessments_count'] = 38
        control_specifications_model_json['assessments'] = [implementation_payload_model]

        # Construct a model instance of ControlSpecifications by calling from_dict on the json representation
        control_specifications_model = ControlSpecifications.from_dict(control_specifications_model_json)
        assert control_specifications_model != False

        # Construct a model instance of ControlSpecifications by calling from_dict on the json representation
        control_specifications_model_dict = ControlSpecifications.from_dict(control_specifications_model_json).__dict__
        control_specifications_model2 = ControlSpecifications(**control_specifications_model_dict)

        # Verify the model instances are equivalent
        assert control_specifications_model == control_specifications_model2

        # Convert model instance back to dict and verify no loss of data
        control_specifications_model_json2 = control_specifications_model.to_dict()
        assert control_specifications_model_json2 == control_specifications_model_json


class TestModel_ControlsInControlLibRequestPayload:
    """
    Test Class for ControlsInControlLibRequestPayload
    """

    def test_controls_in_control_lib_request_payload_serialization(self):
        """
        Test serialization/deserialization for ControlsInControlLibRequestPayload
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        implementation_payload_model = {}  # ImplementationPayload
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        # Construct a json representation of a ControlsInControlLibRequestPayload model
        controls_in_control_lib_request_payload_model_json = {}
        controls_in_control_lib_request_payload_model_json['control_name'] = 'testString'
        controls_in_control_lib_request_payload_model_json['control_id'] = 'testString'
        controls_in_control_lib_request_payload_model_json['control_description'] = 'testString'
        controls_in_control_lib_request_payload_model_json['control_category'] = 'testString'
        controls_in_control_lib_request_payload_model_json['control_parent'] = 'testString'
        controls_in_control_lib_request_payload_model_json['control_severity'] = 'testString'
        controls_in_control_lib_request_payload_model_json['control_tags'] = ['testString']
        controls_in_control_lib_request_payload_model_json['control_specifications'] = [control_specifications_model]
        controls_in_control_lib_request_payload_model_json['control_docs'] = control_docs_model
        controls_in_control_lib_request_payload_model_json['status'] = 'enabled'

        # Construct a model instance of ControlsInControlLibRequestPayload by calling from_dict on the json representation
        controls_in_control_lib_request_payload_model = ControlsInControlLibRequestPayload.from_dict(controls_in_control_lib_request_payload_model_json)
        assert controls_in_control_lib_request_payload_model != False

        # Construct a model instance of ControlsInControlLibRequestPayload by calling from_dict on the json representation
        controls_in_control_lib_request_payload_model_dict = ControlsInControlLibRequestPayload.from_dict(controls_in_control_lib_request_payload_model_json).__dict__
        controls_in_control_lib_request_payload_model2 = ControlsInControlLibRequestPayload(**controls_in_control_lib_request_payload_model_dict)

        # Verify the model instances are equivalent
        assert controls_in_control_lib_request_payload_model == controls_in_control_lib_request_payload_model2

        # Convert model instance back to dict and verify no loss of data
        controls_in_control_lib_request_payload_model_json2 = controls_in_control_lib_request_payload_model.to_dict()
        assert controls_in_control_lib_request_payload_model_json2 == controls_in_control_lib_request_payload_model_json


class TestModel_CreateScanResponse:
    """
    Test Class for CreateScanResponse
    """

    def test_create_scan_response_serialization(self):
        """
        Test serialization/deserialization for CreateScanResponse
        """

        # Construct a json representation of a CreateScanResponse model
        create_scan_response_model_json = {}
        create_scan_response_model_json['id'] = 'testString'
        create_scan_response_model_json['account_id'] = 'testString'
        create_scan_response_model_json['attachment_id'] = 'testString'
        create_scan_response_model_json['report_id'] = 'testString'
        create_scan_response_model_json['status'] = 'testString'
        create_scan_response_model_json['last_scan_time'] = 'testString'
        create_scan_response_model_json['next_scan_time'] = 'testString'
        create_scan_response_model_json['scan_type'] = 'testString'
        create_scan_response_model_json['occurence'] = 38

        # Construct a model instance of CreateScanResponse by calling from_dict on the json representation
        create_scan_response_model = CreateScanResponse.from_dict(create_scan_response_model_json)
        assert create_scan_response_model != False

        # Construct a model instance of CreateScanResponse by calling from_dict on the json representation
        create_scan_response_model_dict = CreateScanResponse.from_dict(create_scan_response_model_json).__dict__
        create_scan_response_model2 = CreateScanResponse(**create_scan_response_model_dict)

        # Verify the model instances are equivalent
        assert create_scan_response_model == create_scan_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_scan_response_model_json2 = create_scan_response_model.to_dict()
        assert create_scan_response_model_json2 == create_scan_response_model_json


class TestModel_DefaultParameters:
    """
    Test Class for DefaultParameters
    """

    def test_default_parameters_serialization(self):
        """
        Test serialization/deserialization for DefaultParameters
        """

        # Construct a json representation of a DefaultParameters model
        default_parameters_model_json = {}
        default_parameters_model_json['assessment_type'] = 'testString'
        default_parameters_model_json['assessment_id'] = 'testString'
        default_parameters_model_json['parameter_name'] = 'testString'
        default_parameters_model_json['parameter_default_value'] = 'testString'
        default_parameters_model_json['parameter_display_name'] = 'testString'
        default_parameters_model_json['parameter_type'] = 'numeric'

        # Construct a model instance of DefaultParameters by calling from_dict on the json representation
        default_parameters_model = DefaultParameters.from_dict(default_parameters_model_json)
        assert default_parameters_model != False

        # Construct a model instance of DefaultParameters by calling from_dict on the json representation
        default_parameters_model_dict = DefaultParameters.from_dict(default_parameters_model_json).__dict__
        default_parameters_model2 = DefaultParameters(**default_parameters_model_dict)

        # Verify the model instances are equivalent
        assert default_parameters_model == default_parameters_model2

        # Convert model instance back to dict and verify no loss of data
        default_parameters_model_json2 = default_parameters_model.to_dict()
        assert default_parameters_model_json2 == default_parameters_model_json


class TestModel_ImplementationPayload:
    """
    Test Class for ImplementationPayload
    """

    def test_implementation_payload_serialization(self):
        """
        Test serialization/deserialization for ImplementationPayload
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a json representation of a ImplementationPayload model
        implementation_payload_model_json = {}
        implementation_payload_model_json['assessment_id'] = 'testString'
        implementation_payload_model_json['assessment_method'] = 'testString'
        implementation_payload_model_json['assessment_type'] = 'testString'
        implementation_payload_model_json['assessment_description'] = 'testString'
        implementation_payload_model_json['parameter_count'] = 38
        implementation_payload_model_json['parameters'] = [parameter_info_model]

        # Construct a model instance of ImplementationPayload by calling from_dict on the json representation
        implementation_payload_model = ImplementationPayload.from_dict(implementation_payload_model_json)
        assert implementation_payload_model != False

        # Construct a model instance of ImplementationPayload by calling from_dict on the json representation
        implementation_payload_model_dict = ImplementationPayload.from_dict(implementation_payload_model_json).__dict__
        implementation_payload_model2 = ImplementationPayload(**implementation_payload_model_dict)

        # Verify the model instances are equivalent
        assert implementation_payload_model == implementation_payload_model2

        # Convert model instance back to dict and verify no loss of data
        implementation_payload_model_json2 = implementation_payload_model.to_dict()
        assert implementation_payload_model_json2 == implementation_payload_model_json


class TestModel_PageRefFirst:
    """
    Test Class for PageRefFirst
    """

    def test_page_ref_first_serialization(self):
        """
        Test serialization/deserialization for PageRefFirst
        """

        # Construct a json representation of a PageRefFirst model
        page_ref_first_model_json = {}
        page_ref_first_model_json['href'] = 'testString'

        # Construct a model instance of PageRefFirst by calling from_dict on the json representation
        page_ref_first_model = PageRefFirst.from_dict(page_ref_first_model_json)
        assert page_ref_first_model != False

        # Construct a model instance of PageRefFirst by calling from_dict on the json representation
        page_ref_first_model_dict = PageRefFirst.from_dict(page_ref_first_model_json).__dict__
        page_ref_first_model2 = PageRefFirst(**page_ref_first_model_dict)

        # Verify the model instances are equivalent
        assert page_ref_first_model == page_ref_first_model2

        # Convert model instance back to dict and verify no loss of data
        page_ref_first_model_json2 = page_ref_first_model.to_dict()
        assert page_ref_first_model_json2 == page_ref_first_model_json


class TestModel_PageRefNext:
    """
    Test Class for PageRefNext
    """

    def test_page_ref_next_serialization(self):
        """
        Test serialization/deserialization for PageRefNext
        """

        # Construct a json representation of a PageRefNext model
        page_ref_next_model_json = {}
        page_ref_next_model_json['href'] = 'testString'
        page_ref_next_model_json['start'] = 'testString'

        # Construct a model instance of PageRefNext by calling from_dict on the json representation
        page_ref_next_model = PageRefNext.from_dict(page_ref_next_model_json)
        assert page_ref_next_model != False

        # Construct a model instance of PageRefNext by calling from_dict on the json representation
        page_ref_next_model_dict = PageRefNext.from_dict(page_ref_next_model_json).__dict__
        page_ref_next_model2 = PageRefNext(**page_ref_next_model_dict)

        # Verify the model instances are equivalent
        assert page_ref_next_model == page_ref_next_model2

        # Convert model instance back to dict and verify no loss of data
        page_ref_next_model_json2 = page_ref_next_model.to_dict()
        assert page_ref_next_model_json2 == page_ref_next_model_json


class TestModel_ParameterDetails:
    """
    Test Class for ParameterDetails
    """

    def test_parameter_details_serialization(self):
        """
        Test serialization/deserialization for ParameterDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        # Construct a json representation of a ParameterDetails model
        parameter_details_model_json = {}
        parameter_details_model_json['parameter_name'] = 'testString'
        parameter_details_model_json['parameter_display_name'] = 'testString'
        parameter_details_model_json['parameter_type'] = 'numeric'
        parameter_details_model_json['parameter_value'] = 'testString'
        parameter_details_model_json['assessment_type'] = 'testString'
        parameter_details_model_json['assessment_id'] = 'testString'
        parameter_details_model_json['parameters'] = [parameter_info_model]

        # Construct a model instance of ParameterDetails by calling from_dict on the json representation
        parameter_details_model = ParameterDetails.from_dict(parameter_details_model_json)
        assert parameter_details_model != False

        # Construct a model instance of ParameterDetails by calling from_dict on the json representation
        parameter_details_model_dict = ParameterDetails.from_dict(parameter_details_model_json).__dict__
        parameter_details_model2 = ParameterDetails(**parameter_details_model_dict)

        # Verify the model instances are equivalent
        assert parameter_details_model == parameter_details_model2

        # Convert model instance back to dict and verify no loss of data
        parameter_details_model_json2 = parameter_details_model.to_dict()
        assert parameter_details_model_json2 == parameter_details_model_json


class TestModel_ParameterInfo:
    """
    Test Class for ParameterInfo
    """

    def test_parameter_info_serialization(self):
        """
        Test serialization/deserialization for ParameterInfo
        """

        # Construct a json representation of a ParameterInfo model
        parameter_info_model_json = {}
        parameter_info_model_json['parameter_name'] = 'testString'
        parameter_info_model_json['parameter_display_name'] = 'testString'
        parameter_info_model_json['parameter_type'] = 'numeric'

        # Construct a model instance of ParameterInfo by calling from_dict on the json representation
        parameter_info_model = ParameterInfo.from_dict(parameter_info_model_json)
        assert parameter_info_model != False

        # Construct a model instance of ParameterInfo by calling from_dict on the json representation
        parameter_info_model_dict = ParameterInfo.from_dict(parameter_info_model_json).__dict__
        parameter_info_model2 = ParameterInfo(**parameter_info_model_dict)

        # Verify the model instances are equivalent
        assert parameter_info_model == parameter_info_model2

        # Convert model instance back to dict and verify no loss of data
        parameter_info_model_json2 = parameter_info_model.to_dict()
        assert parameter_info_model_json2 == parameter_info_model_json


class TestModel_ProfileControlsInRequest:
    """
    Test Class for ProfileControlsInRequest
    """

    def test_profile_controls_in_request_serialization(self):
        """
        Test serialization/deserialization for ProfileControlsInRequest
        """

        # Construct a json representation of a ProfileControlsInRequest model
        profile_controls_in_request_model_json = {}
        profile_controls_in_request_model_json['control_library_id'] = 'testString'
        profile_controls_in_request_model_json['control_id'] = 'testString'

        # Construct a model instance of ProfileControlsInRequest by calling from_dict on the json representation
        profile_controls_in_request_model = ProfileControlsInRequest.from_dict(profile_controls_in_request_model_json)
        assert profile_controls_in_request_model != False

        # Construct a model instance of ProfileControlsInRequest by calling from_dict on the json representation
        profile_controls_in_request_model_dict = ProfileControlsInRequest.from_dict(profile_controls_in_request_model_json).__dict__
        profile_controls_in_request_model2 = ProfileControlsInRequest(**profile_controls_in_request_model_dict)

        # Verify the model instances are equivalent
        assert profile_controls_in_request_model == profile_controls_in_request_model2

        # Convert model instance back to dict and verify no loss of data
        profile_controls_in_request_model_json2 = profile_controls_in_request_model.to_dict()
        assert profile_controls_in_request_model_json2 == profile_controls_in_request_model_json


class TestModel_ProfileControlsInResponse:
    """
    Test Class for ProfileControlsInResponse
    """

    def test_profile_controls_in_response_serialization(self):
        """
        Test serialization/deserialization for ProfileControlsInResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        implementation_payload_model = {}  # ImplementationPayload
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        # Construct a json representation of a ProfileControlsInResponse model
        profile_controls_in_response_model_json = {}
        profile_controls_in_response_model_json['control_library_id'] = 'testString'
        profile_controls_in_response_model_json['control_id'] = 'testString'
        profile_controls_in_response_model_json['control_library_version'] = 'testString'
        profile_controls_in_response_model_json['control_name'] = 'testString'
        profile_controls_in_response_model_json['control_description'] = 'testString'
        profile_controls_in_response_model_json['control_severity'] = 'testString'
        profile_controls_in_response_model_json['control_category'] = 'testString'
        profile_controls_in_response_model_json['control_parent'] = 'testString'
        profile_controls_in_response_model_json['control_docs'] = control_docs_model
        profile_controls_in_response_model_json['control_specifications'] = [control_specifications_model]

        # Construct a model instance of ProfileControlsInResponse by calling from_dict on the json representation
        profile_controls_in_response_model = ProfileControlsInResponse.from_dict(profile_controls_in_response_model_json)
        assert profile_controls_in_response_model != False

        # Construct a model instance of ProfileControlsInResponse by calling from_dict on the json representation
        profile_controls_in_response_model_dict = ProfileControlsInResponse.from_dict(profile_controls_in_response_model_json).__dict__
        profile_controls_in_response_model2 = ProfileControlsInResponse(**profile_controls_in_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_controls_in_response_model == profile_controls_in_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_controls_in_response_model_json2 = profile_controls_in_response_model.to_dict()
        assert profile_controls_in_response_model_json2 == profile_controls_in_response_model_json


class TestModel_ProfileDefaultParametersResponse:
    """
    Test Class for ProfileDefaultParametersResponse
    """

    def test_profile_default_parameters_response_serialization(self):
        """
        Test serialization/deserialization for ProfileDefaultParametersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Construct a json representation of a ProfileDefaultParametersResponse model
        profile_default_parameters_response_model_json = {}
        profile_default_parameters_response_model_json['id'] = 'testString'
        profile_default_parameters_response_model_json['default_parameters'] = [default_parameters_model]

        # Construct a model instance of ProfileDefaultParametersResponse by calling from_dict on the json representation
        profile_default_parameters_response_model = ProfileDefaultParametersResponse.from_dict(profile_default_parameters_response_model_json)
        assert profile_default_parameters_response_model != False

        # Construct a model instance of ProfileDefaultParametersResponse by calling from_dict on the json representation
        profile_default_parameters_response_model_dict = ProfileDefaultParametersResponse.from_dict(profile_default_parameters_response_model_json).__dict__
        profile_default_parameters_response_model2 = ProfileDefaultParametersResponse(**profile_default_parameters_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_default_parameters_response_model == profile_default_parameters_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_default_parameters_response_model_json2 = profile_default_parameters_response_model.to_dict()
        assert profile_default_parameters_response_model_json2 == profile_default_parameters_response_model_json


class TestModel_ProfileResponse:
    """
    Test Class for ProfileResponse
    """

    def test_profile_response_serialization(self):
        """
        Test serialization/deserialization for ProfileResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        control_docs_model = {}  # ControlDocs
        control_docs_model['control_docs_id'] = 'testString'
        control_docs_model['control_docs_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        implementation_payload_model = {}  # ImplementationPayload
        implementation_payload_model['assessment_id'] = 'testString'
        implementation_payload_model['assessment_method'] = 'testString'
        implementation_payload_model['assessment_type'] = 'testString'
        implementation_payload_model['assessment_description'] = 'testString'
        implementation_payload_model['parameter_count'] = 38
        implementation_payload_model['parameters'] = [parameter_info_model]

        control_specifications_model = {}  # ControlSpecifications
        control_specifications_model['id'] = 'testString'
        control_specifications_model['responsibility'] = 'user'
        control_specifications_model['component_id'] = 'testString'
        control_specifications_model['environment'] = 'testString'
        control_specifications_model['description'] = 'testString'
        control_specifications_model['assessments_count'] = 38
        control_specifications_model['assessments'] = [implementation_payload_model]

        profile_controls_in_response_model = {}  # ProfileControlsInResponse
        profile_controls_in_response_model['control_library_id'] = 'testString'
        profile_controls_in_response_model['control_id'] = 'testString'
        profile_controls_in_response_model['control_library_version'] = 'testString'
        profile_controls_in_response_model['control_name'] = 'testString'
        profile_controls_in_response_model['control_description'] = 'testString'
        profile_controls_in_response_model['control_severity'] = 'testString'
        profile_controls_in_response_model['control_category'] = 'testString'
        profile_controls_in_response_model['control_parent'] = 'testString'
        profile_controls_in_response_model['control_docs'] = control_docs_model
        profile_controls_in_response_model['control_specifications'] = [control_specifications_model]

        default_parameters_model = {}  # DefaultParameters
        default_parameters_model['assessment_type'] = 'testString'
        default_parameters_model['assessment_id'] = 'testString'
        default_parameters_model['parameter_name'] = 'testString'
        default_parameters_model['parameter_default_value'] = 'testString'
        default_parameters_model['parameter_display_name'] = 'testString'
        default_parameters_model['parameter_type'] = 'numeric'

        # Construct a json representation of a ProfileResponse model
        profile_response_model_json = {}
        profile_response_model_json['id'] = 'testString'
        profile_response_model_json['profile_name'] = 'testString'
        profile_response_model_json['profile_description'] = 'testString'
        profile_response_model_json['profile_type'] = 'testString'
        profile_response_model_json['profile_version'] = 'testString'
        profile_response_model_json['version_group_label'] = 'testString'
        profile_response_model_json['latest'] = True
        profile_response_model_json['created_by'] = 'testString'
        profile_response_model_json['created_on'] = 'testString'
        profile_response_model_json['updated_by'] = 'testString'
        profile_response_model_json['updated_on'] = 'testString'
        profile_response_model_json['controls_count'] = 38
        profile_response_model_json['attachments_count'] = 38
        profile_response_model_json['controls'] = [profile_controls_in_response_model]
        profile_response_model_json['default_parameters'] = [default_parameters_model]

        # Construct a model instance of ProfileResponse by calling from_dict on the json representation
        profile_response_model = ProfileResponse.from_dict(profile_response_model_json)
        assert profile_response_model != False

        # Construct a model instance of ProfileResponse by calling from_dict on the json representation
        profile_response_model_dict = ProfileResponse.from_dict(profile_response_model_json).__dict__
        profile_response_model2 = ProfileResponse(**profile_response_model_dict)

        # Verify the model instances are equivalent
        assert profile_response_model == profile_response_model2

        # Convert model instance back to dict and verify no loss of data
        profile_response_model_json2 = profile_response_model.to_dict()
        assert profile_response_model_json2 == profile_response_model_json


class TestModel_ScopePayload:
    """
    Test Class for ScopePayload
    """

    def test_scope_payload_serialization(self):
        """
        Test serialization/deserialization for ScopePayload
        """

        # Construct a json representation of a ScopePayload model
        scope_payload_model_json = {}
        scope_payload_model_json['scope_id'] = 'testString'
        scope_payload_model_json['scope_type'] = 'testString'

        # Construct a model instance of ScopePayload by calling from_dict on the json representation
        scope_payload_model = ScopePayload.from_dict(scope_payload_model_json)
        assert scope_payload_model != False

        # Construct a model instance of ScopePayload by calling from_dict on the json representation
        scope_payload_model_dict = ScopePayload.from_dict(scope_payload_model_json).__dict__
        scope_payload_model2 = ScopePayload(**scope_payload_model_dict)

        # Verify the model instances are equivalent
        assert scope_payload_model == scope_payload_model2

        # Convert model instance back to dict and verify no loss of data
        scope_payload_model_json2 = scope_payload_model.to_dict()
        assert scope_payload_model_json2 == scope_payload_model_json


class TestModel_AttachmentsNotificationsPayload:
    """
    Test Class for AttachmentsNotificationsPayload
    """

    def test_attachments_notifications_payload_serialization(self):
        """
        Test serialization/deserialization for AttachmentsNotificationsPayload
        """

        # Construct dict forms of any model objects needed in order to build this model.

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        # Construct a json representation of a AttachmentsNotificationsPayload model
        attachments_notifications_payload_model_json = {}
        attachments_notifications_payload_model_json['enabled'] = True
        attachments_notifications_payload_model_json['controls'] = failed_controls_model

        # Construct a model instance of AttachmentsNotificationsPayload by calling from_dict on the json representation
        attachments_notifications_payload_model = AttachmentsNotificationsPayload.from_dict(attachments_notifications_payload_model_json)
        assert attachments_notifications_payload_model != False

        # Construct a model instance of AttachmentsNotificationsPayload by calling from_dict on the json representation
        attachments_notifications_payload_model_dict = AttachmentsNotificationsPayload.from_dict(attachments_notifications_payload_model_json).__dict__
        attachments_notifications_payload_model2 = AttachmentsNotificationsPayload(**attachments_notifications_payload_model_dict)

        # Verify the model instances are equivalent
        assert attachments_notifications_payload_model == attachments_notifications_payload_model2

        # Convert model instance back to dict and verify no loss of data
        attachments_notifications_payload_model_json2 = attachments_notifications_payload_model.to_dict()
        assert attachments_notifications_payload_model_json2 == attachments_notifications_payload_model_json


class TestModel_FailedControls:
    """
    Test Class for FailedControls
    """

    def test_failed_controls_serialization(self):
        """
        Test serialization/deserialization for FailedControls
        """

        # Construct a json representation of a FailedControls model
        failed_controls_model_json = {}
        failed_controls_model_json['threshold_limit'] = 38
        failed_controls_model_json['failed_control_ids'] = ['testString']

        # Construct a model instance of FailedControls by calling from_dict on the json representation
        failed_controls_model = FailedControls.from_dict(failed_controls_model_json)
        assert failed_controls_model != False

        # Construct a model instance of FailedControls by calling from_dict on the json representation
        failed_controls_model_dict = FailedControls.from_dict(failed_controls_model_json).__dict__
        failed_controls_model2 = FailedControls(**failed_controls_model_dict)

        # Verify the model instances are equivalent
        assert failed_controls_model == failed_controls_model2

        # Convert model instance back to dict and verify no loss of data
        failed_controls_model_json2 = failed_controls_model.to_dict()
        assert failed_controls_model_json2 == failed_controls_model_json


class TestModel_GetAllAttachmnetsForProfileRespBody:
    """
    Test Class for GetAllAttachmnetsForProfileRespBody
    """

    def test_get_all_attachmnets_for_profile_resp_body_serialization(self):
        """
        Test serialization/deserialization for GetAllAttachmnetsForProfileRespBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_ref_first_model = {}  # PageRefFirst
        page_ref_first_model['href'] = 'testString'

        page_ref_next_model = {}  # PageRefNext
        page_ref_next_model['href'] = 'testString'
        page_ref_next_model['start'] = 'testString'

        control_library_list_response_model = {}  # ControlLibraryListResponse
        control_library_list_response_model['id'] = 'testString'
        control_library_list_response_model['account_id'] = 'testString'
        control_library_list_response_model['control_library_name'] = 'testString'
        control_library_list_response_model['control_library_description'] = 'testString'
        control_library_list_response_model['control_library_type'] = 'testString'
        control_library_list_response_model['created_on'] = 'testString'
        control_library_list_response_model['created_by'] = 'testString'
        control_library_list_response_model['updated_on'] = 'testString'
        control_library_list_response_model['updated_by'] = 'testString'
        control_library_list_response_model['version_group_label'] = 'testString'
        control_library_list_response_model['control_library_version'] = 'testString'
        control_library_list_response_model['latest'] = True
        control_library_list_response_model['controls_count'] = 38

        scope_payload_model = {}  # ScopePayload
        scope_payload_model['scope_id'] = 'testString'
        scope_payload_model['scope_type'] = 'testString'

        parameter_info_model = {}  # ParameterInfo
        parameter_info_model['parameter_name'] = 'testString'
        parameter_info_model['parameter_display_name'] = 'testString'
        parameter_info_model['parameter_type'] = 'numeric'

        parameter_details_model = {}  # ParameterDetails
        parameter_details_model['parameter_name'] = 'testString'
        parameter_details_model['parameter_display_name'] = 'testString'
        parameter_details_model['parameter_type'] = 'numeric'
        parameter_details_model['parameter_value'] = 'testString'
        parameter_details_model['assessment_type'] = 'testString'
        parameter_details_model['assessment_id'] = 'testString'
        parameter_details_model['parameters'] = [parameter_info_model]

        failed_controls_model = {}  # FailedControls
        failed_controls_model['threshold_limit'] = 38
        failed_controls_model['failed_control_ids'] = ['testString']

        attachments_notifications_payload_model = {}  # AttachmentsNotificationsPayload
        attachments_notifications_payload_model['enabled'] = True
        attachments_notifications_payload_model['controls'] = failed_controls_model

        attachment_payload_model = {}  # AttachmentPayload
        attachment_payload_model['id'] = 'testString'
        attachment_payload_model['account_id'] = 'testString'
        attachment_payload_model['included_scope'] = scope_payload_model
        attachment_payload_model['exclusions'] = [scope_payload_model]
        attachment_payload_model['created_by'] = 'testString'
        attachment_payload_model['created_on'] = 'testString'
        attachment_payload_model['updated_by'] = 'testString'
        attachment_payload_model['updated_on'] = 'testString'
        attachment_payload_model['status'] = 'enabled'
        attachment_payload_model['attachment_parameters'] = [parameter_details_model]
        attachment_payload_model['attachment_notifications'] = attachments_notifications_payload_model

        attachment_profile_request_model = {}  # AttachmentProfileRequest
        attachment_profile_request_model['attachments'] = [attachment_payload_model]

        # Construct a json representation of a GetAllAttachmnetsForProfileRespBody model
        get_all_attachmnets_for_profile_resp_body_model_json = {}
        get_all_attachmnets_for_profile_resp_body_model_json['total_count'] = 38
        get_all_attachmnets_for_profile_resp_body_model_json['limit'] = 38
        get_all_attachmnets_for_profile_resp_body_model_json['first'] = page_ref_first_model
        get_all_attachmnets_for_profile_resp_body_model_json['next'] = page_ref_next_model
        get_all_attachmnets_for_profile_resp_body_model_json['profile_id'] = 'testString'
        get_all_attachmnets_for_profile_resp_body_model_json['account_id'] = 'testString'
        get_all_attachmnets_for_profile_resp_body_model_json['control_libraries'] = [control_library_list_response_model]
        get_all_attachmnets_for_profile_resp_body_model_json['attachments'] = [attachment_profile_request_model]

        # Construct a model instance of GetAllAttachmnetsForProfileRespBody by calling from_dict on the json representation
        get_all_attachmnets_for_profile_resp_body_model = GetAllAttachmnetsForProfileRespBody.from_dict(get_all_attachmnets_for_profile_resp_body_model_json)
        assert get_all_attachmnets_for_profile_resp_body_model != False

        # Construct a model instance of GetAllAttachmnetsForProfileRespBody by calling from_dict on the json representation
        get_all_attachmnets_for_profile_resp_body_model_dict = GetAllAttachmnetsForProfileRespBody.from_dict(get_all_attachmnets_for_profile_resp_body_model_json).__dict__
        get_all_attachmnets_for_profile_resp_body_model2 = GetAllAttachmnetsForProfileRespBody(**get_all_attachmnets_for_profile_resp_body_model_dict)

        # Verify the model instances are equivalent
        assert get_all_attachmnets_for_profile_resp_body_model == get_all_attachmnets_for_profile_resp_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_all_attachmnets_for_profile_resp_body_model_json2 = get_all_attachmnets_for_profile_resp_body_model.to_dict()
        assert get_all_attachmnets_for_profile_resp_body_model_json2 == get_all_attachmnets_for_profile_resp_body_model_json


class TestModel_GetAllControlLibrariesRespBody:
    """
    Test Class for GetAllControlLibrariesRespBody
    """

    def test_get_all_control_libraries_resp_body_serialization(self):
        """
        Test serialization/deserialization for GetAllControlLibrariesRespBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_ref_first_model = {}  # PageRefFirst
        page_ref_first_model['href'] = 'testString'

        page_ref_next_model = {}  # PageRefNext
        page_ref_next_model['href'] = 'testString'
        page_ref_next_model['start'] = 'testString'

        control_library_list_response_model = {}  # ControlLibraryListResponse
        control_library_list_response_model['id'] = 'testString'
        control_library_list_response_model['account_id'] = 'testString'
        control_library_list_response_model['control_library_name'] = 'testString'
        control_library_list_response_model['control_library_description'] = 'testString'
        control_library_list_response_model['control_library_type'] = 'testString'
        control_library_list_response_model['created_on'] = 'testString'
        control_library_list_response_model['created_by'] = 'testString'
        control_library_list_response_model['updated_on'] = 'testString'
        control_library_list_response_model['updated_by'] = 'testString'
        control_library_list_response_model['version_group_label'] = 'testString'
        control_library_list_response_model['control_library_version'] = 'testString'
        control_library_list_response_model['latest'] = True
        control_library_list_response_model['controls_count'] = 38

        # Construct a json representation of a GetAllControlLibrariesRespBody model
        get_all_control_libraries_resp_body_model_json = {}
        get_all_control_libraries_resp_body_model_json['total_count'] = 1
        get_all_control_libraries_resp_body_model_json['limit'] = 20
        get_all_control_libraries_resp_body_model_json['first'] = page_ref_first_model
        get_all_control_libraries_resp_body_model_json['next'] = page_ref_next_model
        get_all_control_libraries_resp_body_model_json['control_libraries'] = [control_library_list_response_model]

        # Construct a model instance of GetAllControlLibrariesRespBody by calling from_dict on the json representation
        get_all_control_libraries_resp_body_model = GetAllControlLibrariesRespBody.from_dict(get_all_control_libraries_resp_body_model_json)
        assert get_all_control_libraries_resp_body_model != False

        # Construct a model instance of GetAllControlLibrariesRespBody by calling from_dict on the json representation
        get_all_control_libraries_resp_body_model_dict = GetAllControlLibrariesRespBody.from_dict(get_all_control_libraries_resp_body_model_json).__dict__
        get_all_control_libraries_resp_body_model2 = GetAllControlLibrariesRespBody(**get_all_control_libraries_resp_body_model_dict)

        # Verify the model instances are equivalent
        assert get_all_control_libraries_resp_body_model == get_all_control_libraries_resp_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_all_control_libraries_resp_body_model_json2 = get_all_control_libraries_resp_body_model.to_dict()
        assert get_all_control_libraries_resp_body_model_json2 == get_all_control_libraries_resp_body_model_json


class TestModel_GetAllProfilesRespBody:
    """
    Test Class for GetAllProfilesRespBody
    """

    def test_get_all_profiles_resp_body_serialization(self):
        """
        Test serialization/deserialization for GetAllProfilesRespBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        page_ref_first_model = {}  # PageRefFirst
        page_ref_first_model['href'] = 'testString'

        page_ref_next_model = {}  # PageRefNext
        page_ref_next_model['href'] = 'testString'
        page_ref_next_model['start'] = 'testString'

        list_profiles_response_structure_model = {}  # ListProfilesResponseStructure
        list_profiles_response_structure_model['id'] = 'testString'
        list_profiles_response_structure_model['profile_name'] = 'testString'
        list_profiles_response_structure_model['profile_description'] = 'testString'
        list_profiles_response_structure_model['profile_type'] = 'testString'
        list_profiles_response_structure_model['profile_version'] = 'testString'
        list_profiles_response_structure_model['version_group_label'] = 'testString'
        list_profiles_response_structure_model['latest'] = True
        list_profiles_response_structure_model['created_by'] = 'testString'
        list_profiles_response_structure_model['created_on'] = 'testString'
        list_profiles_response_structure_model['updated_by'] = 'testString'
        list_profiles_response_structure_model['updated_on'] = 'testString'
        list_profiles_response_structure_model['controls_count'] = 38
        list_profiles_response_structure_model['attachments_count'] = 38

        # Construct a json representation of a GetAllProfilesRespBody model
        get_all_profiles_resp_body_model_json = {}
        get_all_profiles_resp_body_model_json['total_count'] = 1
        get_all_profiles_resp_body_model_json['limit'] = 20
        get_all_profiles_resp_body_model_json['first'] = page_ref_first_model
        get_all_profiles_resp_body_model_json['next'] = page_ref_next_model
        get_all_profiles_resp_body_model_json['profiles'] = [list_profiles_response_structure_model]

        # Construct a model instance of GetAllProfilesRespBody by calling from_dict on the json representation
        get_all_profiles_resp_body_model = GetAllProfilesRespBody.from_dict(get_all_profiles_resp_body_model_json)
        assert get_all_profiles_resp_body_model != False

        # Construct a model instance of GetAllProfilesRespBody by calling from_dict on the json representation
        get_all_profiles_resp_body_model_dict = GetAllProfilesRespBody.from_dict(get_all_profiles_resp_body_model_json).__dict__
        get_all_profiles_resp_body_model2 = GetAllProfilesRespBody(**get_all_profiles_resp_body_model_dict)

        # Verify the model instances are equivalent
        assert get_all_profiles_resp_body_model == get_all_profiles_resp_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_all_profiles_resp_body_model_json2 = get_all_profiles_resp_body_model.to_dict()
        assert get_all_profiles_resp_body_model_json2 == get_all_profiles_resp_body_model_json


class TestModel_ListProfilesResponseStructure:
    """
    Test Class for ListProfilesResponseStructure
    """

    def test_list_profiles_response_structure_serialization(self):
        """
        Test serialization/deserialization for ListProfilesResponseStructure
        """

        # Construct a json representation of a ListProfilesResponseStructure model
        list_profiles_response_structure_model_json = {}
        list_profiles_response_structure_model_json['id'] = 'testString'
        list_profiles_response_structure_model_json['profile_name'] = 'testString'
        list_profiles_response_structure_model_json['profile_description'] = 'testString'
        list_profiles_response_structure_model_json['profile_type'] = 'testString'
        list_profiles_response_structure_model_json['profile_version'] = 'testString'
        list_profiles_response_structure_model_json['version_group_label'] = 'testString'
        list_profiles_response_structure_model_json['latest'] = True
        list_profiles_response_structure_model_json['created_by'] = 'testString'
        list_profiles_response_structure_model_json['created_on'] = 'testString'
        list_profiles_response_structure_model_json['updated_by'] = 'testString'
        list_profiles_response_structure_model_json['updated_on'] = 'testString'
        list_profiles_response_structure_model_json['controls_count'] = 38
        list_profiles_response_structure_model_json['attachments_count'] = 38

        # Construct a model instance of ListProfilesResponseStructure by calling from_dict on the json representation
        list_profiles_response_structure_model = ListProfilesResponseStructure.from_dict(list_profiles_response_structure_model_json)
        assert list_profiles_response_structure_model != False

        # Construct a model instance of ListProfilesResponseStructure by calling from_dict on the json representation
        list_profiles_response_structure_model_dict = ListProfilesResponseStructure.from_dict(list_profiles_response_structure_model_json).__dict__
        list_profiles_response_structure_model2 = ListProfilesResponseStructure(**list_profiles_response_structure_model_dict)

        # Verify the model instances are equivalent
        assert list_profiles_response_structure_model == list_profiles_response_structure_model2

        # Convert model instance back to dict and verify no loss of data
        list_profiles_response_structure_model_json2 = list_profiles_response_structure_model.to_dict()
        assert list_profiles_response_structure_model_json2 == list_profiles_response_structure_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
