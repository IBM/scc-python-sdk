# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.76.0-ad3e6f96-20230724-172814

"""
Security and Compliance Center API

API Version: 3.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse, get_query_param
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class SecurityAndComplianceCenterApiV3(BaseService):
    """The Security and Compliance Center API V3 service."""

    DEFAULT_SERVICE_URL = 'https://us-south.compliance.cloud.ibm.com/instances/instance_id/v3'
    DEFAULT_SERVICE_NAME = 'security_and_compliance_center_api'

    PARAMETERIZED_SERVICE_URL = 'https://{region}.cloud.ibm.com/instances/{instance_id}/v3'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'SecurityAndComplianceCenterApiV3':
        """
        Return a new client for the Security and Compliance Center API service
               using the specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    @classmethod
    def construct_service_url(
        cls,
        region: str = 'us-south.compliance',
        instance_id: str = 'instance_id',
    ) -> str:
        """
        Construct a service URL by formatting the parameterized service URL.

        The parameterized service URL is:
        'https://{region}.cloud.ibm.com/instances/{instance_id}/v3'

        :param str region: (optional) No description provided.
            (default 'us-south.compliance')
        :param str instance_id: (optional) The ID of the managing instance.
            (default 'instance_id')
        :return: The formatted URL with all variable placeholders replaced by values.
        :rtype: str
        """
        return cls.PARAMETERIZED_SERVICE_URL.format(
            region=region,
            instance_id=instance_id,
        )

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Security and Compliance Center API service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Settings
    #########################

    def get_settings(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get settings.

        Retrieve the settings of your service instance.

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request, and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request, and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Settings` object
        """

        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_settings',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/settings'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_settings(
        self,
        *,
        event_notifications: 'EventNotifications' = None,
        object_storage: 'ObjectStorage' = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update settings.

        Update the settings of your service instance.

        :param EventNotifications event_notifications: (optional) The Event
               Notifications settings.
        :param ObjectStorage object_storage: (optional) The Cloud Object Storage
               settings.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request, and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request, and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Settings` object
        """

        if event_notifications is not None:
            event_notifications = convert_model(event_notifications)
        if object_storage is not None:
            object_storage = convert_model(object_storage)
        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='update_settings',
        )
        headers.update(sdk_headers)

        data = {
            'event_notifications': event_notifications,
            'object_storage': object_storage,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/settings'
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def post_test_event(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a test event.

        Send a test event to your Event Notifications instance to ensure that the events
        that are generated  by Security and Compliance Center are being forwarded to Event
        Notifications. For more information, see [Enabling event
        notifications](/docs/security-compliance?topic=security-compliance-event-notifications#event-notifications-test-api).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request, and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request, and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TestEvent` object
        """

        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='post_test_event',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/test_event'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Control libraries
    #########################

    def list_control_libraries(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
        control_library_type: str = None,
        start: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get control libraries.

        Retrieve all of the control libraries that are available in your account,
        including predefined, and custom libraries.
        With Security and Compliance Center, you can create a custom control library that
        is specific to your organization's needs.  You define the controls and
        specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. A specification is
        a defined requirement that is specific to a component. An assessment, or several,
        are mapped to each specification with a detailed evaluation that is done to check
        whether the specification is compliant. For more information, see [Creating custom
        libraries](/docs/security-compliance?topic=security-compliance-custom-library).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The field that indicates how many resources to
               return, unless the response is the last page of resources.
        :param str control_library_type: (optional) The field that indicate how you
               want the resources to be filtered by.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryCollection` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_control_libraries',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'control_library_type': control_library_type,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/control_libraries'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_custom_control_library(
        self,
        control_library_name: str,
        control_library_description: str,
        control_library_type: str,
        controls: List['ControlsInControlLib'],
        *,
        version_group_label: str = None,
        control_library_version: str = None,
        latest: bool = None,
        controls_count: int = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom control library.

        Create a custom control library that is specific to your organization's needs.
        With Security and Compliance Center, you can create a custom control library that
        is specific to your organization's needs.  You define the controls and
        specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. A specification is
        a defined requirement that is specific to a component. An assessment, or several,
        are mapped to each specification with a detailed evaluation that is done to check
        whether the specification is compliant. For more information, see [Creating custom
        libraries](/docs/security-compliance?topic=security-compliance-custom-library).

        :param str control_library_name: The control library name.
        :param str control_library_description: The control library description.
        :param str control_library_type: The control library type.
        :param List[ControlsInControlLib] controls: The controls.
        :param str version_group_label: (optional) The version group label.
        :param str control_library_version: (optional) The control library version.
        :param bool latest: (optional) The latest control library version.
        :param int controls_count: (optional) The number of controls.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if control_library_name is None:
            raise ValueError('control_library_name must be provided')
        if control_library_description is None:
            raise ValueError('control_library_description must be provided')
        if control_library_type is None:
            raise ValueError('control_library_type must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        controls = [convert_model(x) for x in controls]
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_custom_control_library',
        )
        headers.update(sdk_headers)

        data = {
            'control_library_name': control_library_name,
            'control_library_description': control_library_description,
            'control_library_type': control_library_type,
            'controls': controls,
            'version_group_label': version_group_label,
            'control_library_version': control_library_version,
            'latest': latest,
            'controls_count': controls_count,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/control_libraries'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_control_library(
        self,
        control_libraries_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a control library.

        Delete a custom control library by providing the control library ID.  You can find
        this ID by looking in the Security and Compliance Center UI.
        With Security and Compliance Center, you can manage a custom control library  that
        is specific to your organization's needs. Each control has several specifications
        and assessments that are mapped to it.  For more information, see [Creating custom
        libraries](/docs/security-compliance?topic=security-compliance-custom-library).

        :param str control_libraries_id: The control library ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryDelete` object
        """

        if not control_libraries_id:
            raise ValueError('control_libraries_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_custom_control_library',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['control_libraries_id']
        path_param_values = self.encode_path_vars(control_libraries_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/control_libraries/{control_libraries_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_control_library(
        self,
        control_libraries_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a control library.

        View the details of a control library by specifying its ID.
        With Security and Compliance Center, you can create a custom control library that
        is specific to your organization's needs.  You define the controls and
        specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. A specification is
        a defined requirement that is specific to a component. An assessment, or several,
        are mapped to each specification with a detailed evaluation that is done to check
        whether the specification is compliant. For more information, see [Creating custom
        libraries](/docs/security-compliance?topic=security-compliance-custom-library).

        :param str control_libraries_id: The control library ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if not control_libraries_id:
            raise ValueError('control_libraries_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_control_library',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['control_libraries_id']
        path_param_values = self.encode_path_vars(control_libraries_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/control_libraries/{control_libraries_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_custom_control_library(
        self,
        control_libraries_id: str,
        *,
        id: str = None,
        account_id: str = None,
        control_library_name: str = None,
        control_library_description: str = None,
        control_library_type: str = None,
        version_group_label: str = None,
        control_library_version: str = None,
        created_on: datetime = None,
        created_by: str = None,
        updated_on: datetime = None,
        updated_by: str = None,
        latest: bool = None,
        hierarchy_enabled: bool = None,
        controls_count: int = None,
        control_parents_count: int = None,
        controls: List['ControlsInControlLib'] = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a control library.

        Update a custom control library by providing the control library ID. You can find
        this ID in the Security and Compliance Center UI.
        With Security and Compliance Center, you can create and update a custom control
        library that is specific to your organization's needs.  You define the controls
        and specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. For more
        information, see [Creating custom
        libraries](/docs/security-compliance?topic=security-compliance-custom-library).

        :param str control_libraries_id: The control library ID.
        :param str id: (optional) The control library ID.
        :param str account_id: (optional) The account ID.
        :param str control_library_name: (optional) The control library name.
        :param str control_library_description: (optional) The control library
               description.
        :param str control_library_type: (optional) The control library type.
        :param str version_group_label: (optional) The version group label.
        :param str control_library_version: (optional) The control library version.
        :param datetime created_on: (optional) The date when the control library
               was created.
        :param str created_by: (optional) The user who created the control library.
        :param datetime updated_on: (optional) The date when the control library
               was updated.
        :param str updated_by: (optional) The user who updated the control library.
        :param bool latest: (optional) The latest version of the control library.
        :param bool hierarchy_enabled: (optional) The indication of whether
               hierarchy is enabled for the control library.
        :param int controls_count: (optional) The number of controls.
        :param int control_parents_count: (optional) The number of parent controls
               in the control library.
        :param List[ControlsInControlLib] controls: (optional) The list of controls
               in a control library.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if not control_libraries_id:
            raise ValueError('control_libraries_id must be provided')
        if created_on is not None:
            created_on = datetime_to_string(created_on)
        if updated_on is not None:
            updated_on = datetime_to_string(updated_on)
        if controls is not None:
            controls = [convert_model(x) for x in controls]
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_custom_control_library',
        )
        headers.update(sdk_headers)

        data = {
            'id': id,
            'account_id': account_id,
            'control_library_name': control_library_name,
            'control_library_description': control_library_description,
            'control_library_type': control_library_type,
            'version_group_label': version_group_label,
            'control_library_version': control_library_version,
            'created_on': created_on,
            'created_by': created_by,
            'updated_on': updated_on,
            'updated_by': updated_by,
            'latest': latest,
            'hierarchy_enabled': hierarchy_enabled,
            'controls_count': controls_count,
            'control_parents_count': control_parents_count,
            'controls': controls,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['control_libraries_id']
        path_param_values = self.encode_path_vars(control_libraries_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/control_libraries/{control_libraries_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Profiles
    #########################

    def list_profiles(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
        profile_type: str = None,
        start: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all profiles.

        View all of the predefined and custom profiles that are available in your account.

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request, and repeated in a response header for
               the corresponding response. The same value is used for downstream requests,
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str profile_type: (optional) The field that indicate how you want
               the resources to be filtered by.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileCollection` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_profiles',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'profile_type': profile_type,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/profiles'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_profile(
        self,
        profile_name: str,
        profile_description: str,
        profile_type: str,
        controls: List['ProfileControlsPrototype'],
        default_parameters: List['DefaultParametersPrototype'],
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom profile.

        Create a custom profile that is specific to your usecase, by using an existing
        library as a starting point.  For more information, see [Building custom
        profiles](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str profile_name: The name of the profile.
        :param str profile_description: The description of the profile.
        :param str profile_type: The profile type.
        :param List[ProfileControlsPrototype] controls: The controls that are in
               the profile.
        :param List[DefaultParametersPrototype] default_parameters: The default
               parameters of the profile.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request, and repeated in a response header for
               the corresponding response. The same value is used for downstream requests,
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if profile_name is None:
            raise ValueError('profile_name must be provided')
        if profile_description is None:
            raise ValueError('profile_description must be provided')
        if profile_type is None:
            raise ValueError('profile_type must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        if default_parameters is None:
            raise ValueError('default_parameters must be provided')
        controls = [convert_model(x) for x in controls]
        default_parameters = [convert_model(x) for x in default_parameters]
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_profile',
        )
        headers.update(sdk_headers)

        data = {
            'profile_name': profile_name,
            'profile_description': profile_description,
            'profile_type': profile_type,
            'controls': controls,
            'default_parameters': default_parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/profiles'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_profile(
        self,
        profile_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom profile.

        Delete a custom profile by providing the profile ID.  You can find the ID in the
        Security and Compliance Center UI. For more information about managing your custom
        profiles, see [Building custom
        profiles](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str profile_id: The profile ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_custom_profile',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile_id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_profile(
        self,
        profile_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a profile.

        View the details of a profile by providing the profile ID.  You can find the
        profile ID in the Security and Compliance Center UI. For more information, see
        [Building custom
        profiles](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str profile_id: The profile ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_profile',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile_id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile(
        self,
        profile_id: str,
        profile_name: str,
        profile_description: str,
        profile_type: str,
        controls: List['ProfileControlsPrototype'],
        default_parameters: List['DefaultParametersPrototype'],
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a profile.

        Update the details of a custom profile. With Security and Compliance Center, you
        can manage  a profile that is specific to your usecase, by using an existing
        library as a starting point.  For more information, see [Building custom
        profiles](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str profile_id: The profile ID.
        :param str profile_name: The name of the profile.
        :param str profile_description: The description of the profile.
        :param str profile_type: The profile type.
        :param List[ProfileControlsPrototype] controls: The controls that are in
               the profile.
        :param List[DefaultParametersPrototype] default_parameters: The default
               parameters of the profile.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not profile_id:
            raise ValueError('profile_id must be provided')
        if profile_name is None:
            raise ValueError('profile_name must be provided')
        if profile_description is None:
            raise ValueError('profile_description must be provided')
        if profile_type is None:
            raise ValueError('profile_type must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        if default_parameters is None:
            raise ValueError('default_parameters must be provided')
        controls = [convert_model(x) for x in controls]
        default_parameters = [convert_model(x) for x in default_parameters]
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_profile',
        )
        headers.update(sdk_headers)

        data = {
            'profile_name': profile_name,
            'profile_description': profile_description,
            'profile_type': profile_type,
            'controls': controls,
            'default_parameters': default_parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile_id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Rules
    #########################

    def list_rules(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        type: str = None,
        search: str = None,
        service_name: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all rules.

        Retrieve all the rules that you use to target the exact configuration properties
        that you need to ensure are compliant. For more information, see [Defining custom
        rules](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str type: (optional) The list of only user-defined, or
               system-defined rules.
        :param str search: (optional) The indication of whether to search for rules
               with a specific string string in the name, description, or labels.
        :param str service_name: (optional) Searches for rules targeting
               corresponding service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesPageBase` object
        """

        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_rules',
        )
        headers.update(sdk_headers)

        params = {
            'type': type,
            'search': search,
            'service_name': service_name,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/rules'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_rule(
        self,
        description: str,
        target: 'Target',
        required_config: 'RequiredConfig',
        *,
        type: str = None,
        version: str = None,
        import_: 'Import' = None,
        labels: List[str] = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom rule.

        Create a custom rule to to target the exact configuration properties  that you
        need to evaluate your resources for compliance. For more information, see
        [Defining custom
        rules](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str description: The rule description.
        :param Target target: The rule target.
        :param RequiredConfig required_config: The required configurations.
        :param str type: (optional) The rule type (user_defined or system_defined).
        :param str version: (optional) The rule version number.
        :param Import import_: (optional) The collection of import parameters.
        :param List[str] labels: (optional) The list of labels that correspond to a
               rule.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if description is None:
            raise ValueError('description must be provided')
        if target is None:
            raise ValueError('target must be provided')
        if required_config is None:
            raise ValueError('required_config must be provided')
        target = convert_model(target)
        required_config = convert_model(required_config)
        if import_ is not None:
            import_ = convert_model(import_)
        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_rule',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'target': target,
            'required_config': required_config,
            'type': type,
            'version': version,
            'import': import_,
            'labels': labels,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/rules'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_rule(
        self,
        rule_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom rule.

        Delete a custom rule that you no longer require to evaluate your resources. For
        more information, see [Defining custom
        rules](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str rule_id: The ID of the corresponding rule.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_rule(
        self,
        rule_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a custom rule.

        Retrieve a rule that you created to evaluate your resources.  For more
        information, see [Defining custom
        rules](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str rule_id: The ID of the corresponding rule.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_rule(
        self,
        rule_id: str,
        if_match: str,
        description: str,
        target: 'Target',
        required_config: 'RequiredConfig',
        *,
        type: str = None,
        version: str = None,
        import_: 'Import' = None,
        labels: List[str] = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a custom rule.

        Update a custom rule that you use to target the exact configuration properties
        that you need to evaluate your resources for compliance. For more information, see
        [Defining custom
        rules](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str rule_id: The ID of the corresponding rule.
        :param str if_match: This field compares a supplied `Etag` value with the
               version that is stored for the requested resource. If the values match, the
               server allows the request method to continue.
               To find the `Etag` value, run a GET request on the resource that you want
               to modify, and check the response headers.
        :param str description: The rule description.
        :param Target target: The rule target.
        :param RequiredConfig required_config: The required configurations.
        :param str type: (optional) The rule type (user_defined or system_defined).
        :param str version: (optional) The rule version number.
        :param Import import_: (optional) The collection of import parameters.
        :param List[str] labels: (optional) The list of labels that correspond to a
               rule.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not rule_id:
            raise ValueError('rule_id must be provided')
        if not if_match:
            raise ValueError('if_match must be provided')
        if description is None:
            raise ValueError('description must be provided')
        if target is None:
            raise ValueError('target must be provided')
        if required_config is None:
            raise ValueError('required_config must be provided')
        target = convert_model(target)
        required_config = convert_model(required_config)
        if import_ is not None:
            import_ = convert_model(import_)
        headers = {
            'If-Match': if_match,
            'X-Correlation-Id': x_correlation_id,
            'X-Request-Id': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_rule',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'target': target,
            'required_config': required_config,
            'type': type,
            'version': version,
            'import': import_,
            'labels': labels,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule_id']
        path_param_values = self.encode_path_vars(rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Attachments
    #########################

    def list_attachments(
        self,
        profile_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
        start: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all attachments linked to a specific profile.

        View all of the attachments that are linked to a specific profile.  An attachment
        is the association between the set of resources that you want to evaluate  and a
        profile that contains the specific controls that you want to use. For more
        information, see [Running an evaluation for IBM
        Cloud](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str profile_id: The profile ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentCollection` object
        """

        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_attachments',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile_id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_attachment(
        self,
        profile_id: str,
        attachments: List['AttachmentsPrototype'],
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an attachment.

        Create an attachment to link to a profile to schedule evaluations  of your
        resources on a recurring schedule, or on-demand. For more information, see
        [Running an evaluation for IBM
        Cloud](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str profile_id: The profile ID.
        :param List[AttachmentsPrototype] attachments: The array that displays all
               of the available attachments.
        :param str profile_id: (optional) The ID of the profile that is specified
               in the attachment.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentPrototype` object
        """

        if not profile_id:
            raise ValueError('profile_id must be provided')
        if attachments is None:
            raise ValueError('attachments must be provided')
        attachments = [convert_model(x) for x in attachments]
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_attachment',
        )
        headers.update(sdk_headers)

        data = {
            'attachments': attachments,
            'profile_id': profile_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profile_id']
        path_param_values = self.encode_path_vars(profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_profile_attachment(
        self,
        attachment_id: str,
        profile_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an attachment.

        Delete an attachment. Alternatively, if you think that you might need  this
        configuration in the future, you can pause an attachment to stop being charged.
        For more information, see [Running an evaluation for IBM
        Cloud](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str attachment_id: The attachment ID.
        :param str profile_id: The profile ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentItem` object
        """

        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_profile_attachment',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['attachment_id', 'profile_id']
        path_param_values = self.encode_path_vars(attachment_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_profile_attachment(
        self,
        attachment_id: str,
        profile_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an attachment.

        View the details of an attachment a profile by providing the attachment ID.  You
        can find this value in the Security and Compliance Center UI. For more
        information, see [Running an evaluation for IBM
        Cloud](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str attachment_id: The attachment ID.
        :param str profile_id: The profile ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentItem` object
        """

        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_profile_attachment',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['attachment_id', 'profile_id']
        path_param_values = self.encode_path_vars(attachment_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile_attachment(
        self,
        attachment_id: str,
        profile_id: str,
        *,
        id: str = None,
        account_id: str = None,
        instance_id: str = None,
        scope: List['MultiCloudScope'] = None,
        created_on: datetime = None,
        created_by: str = None,
        updated_on: datetime = None,
        updated_by: str = None,
        status: str = None,
        schedule: str = None,
        notifications: 'AttachmentsNotificationsPrototype' = None,
        attachment_parameters: List['AttachmentParameterPrototype'] = None,
        last_scan: 'LastScan' = None,
        next_scan_time: datetime = None,
        name: str = None,
        description: str = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an attachment.

        Update an attachment that is linked to a profile to evaluate your resources  on a
        recurring schedule, or on-demand. For more information, see [Running an evaluation
        for IBM
        Cloud](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str attachment_id: The attachment ID.
        :param str profile_id: The profile ID.
        :param str id: (optional) The ID of the attachment.
        :param str profile_id: (optional) The ID of the profile that is specified
               in the attachment.
        :param str account_id: (optional) The account ID that is associated to the
               attachment.
        :param str instance_id: (optional) The instance ID of the account that is
               associated to the attachment.
        :param List[MultiCloudScope] scope: (optional) The scope payload for the
               multi cloud feature.
        :param datetime created_on: (optional) The date when the attachment was
               created.
        :param str created_by: (optional) The user who created the attachment.
        :param datetime updated_on: (optional) The date when the attachment was
               updated.
        :param str updated_by: (optional) The user who updated the attachment.
        :param str status: (optional) The status of an attachment evaluation.
        :param str schedule: (optional) The schedule of an attachment evaluation.
        :param AttachmentsNotificationsPrototype notifications: (optional) The
               request payload of the attachment notifications.
        :param List[AttachmentParameterPrototype] attachment_parameters: (optional)
               The profile parameters for the attachment.
        :param LastScan last_scan: (optional) The details of the last scan of an
               attachment.
        :param datetime next_scan_time: (optional) The start time of the next scan.
        :param str name: (optional) The name of the attachment.
        :param str description: (optional) The description for the attachment.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentItem` object
        """

        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if scope is not None:
            scope = [convert_model(x) for x in scope]
        if created_on is not None:
            created_on = datetime_to_string(created_on)
        if updated_on is not None:
            updated_on = datetime_to_string(updated_on)
        if notifications is not None:
            notifications = convert_model(notifications)
        if attachment_parameters is not None:
            attachment_parameters = [convert_model(x) for x in attachment_parameters]
        if last_scan is not None:
            last_scan = convert_model(last_scan)
        if next_scan_time is not None:
            next_scan_time = datetime_to_string(next_scan_time)
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_profile_attachment',
        )
        headers.update(sdk_headers)

        data = {
            'id': id,
            'profile_id': profile_id,
            'account_id': account_id,
            'instance_id': instance_id,
            'scope': scope,
            'created_on': created_on,
            'created_by': created_by,
            'updated_on': updated_on,
            'updated_by': updated_by,
            'status': status,
            'schedule': schedule,
            'notifications': notifications,
            'attachment_parameters': attachment_parameters,
            'last_scan': last_scan,
            'next_scan_time': next_scan_time,
            'name': name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['attachment_id', 'profile_id']
        path_param_values = self.encode_path_vars(attachment_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/profiles/{profile_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_scan(
        self,
        attachment_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a scan.

        Create a scan to evaluate your resources on a recurring basis or on demand.

        :param str attachment_id: The attachment ID of a profile.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Scan` object
        """

        if attachment_id is None:
            raise ValueError('attachment_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_scan',
        )
        headers.update(sdk_headers)

        data = {
            'attachment_id': attachment_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/scans'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_attachments_account(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
        start: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all attachments in an instance.

        View all of the attachments that are linked to an account. An attachment is the
        association between the set of resources that you want to evaluate  and a profile
        that contains the specific controls that you want to use. For more information,
        see [Running an evaluation for IBM
        Cloud](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentCollection` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_attachments_account',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/attachments'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Reports
    #########################

    def get_latest_reports(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        sort: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the latest reports.

        Retrieve the latest reports, which are grouped by profile ID, scope ID, and
        attachment ID. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str sort: (optional) This field sorts results by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportLatest` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_latest_reports',
        )
        headers.update(sdk_headers)

        params = {
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/reports/latest'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def list_reports(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        attachment_id: str = None,
        group_id: str = None,
        profile_id: str = None,
        type: str = None,
        start: str = None,
        limit: int = None,
        sort: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List reports.

        Retrieve a page of reports that are filtered by the specified parameters. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str attachment_id: (optional) The ID of the attachment.
        :param str group_id: (optional) The report group ID.
        :param str profile_id: (optional) The ID of the profile.
        :param str type: (optional) The type of the scan.
        :param str start: (optional) The indication of what resource to start the
               page on.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param str sort: (optional) This field sorts results by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportPage` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_reports',
        )
        headers.update(sdk_headers)

        params = {
            'attachment_id': attachment_id,
            'group_id': group_id,
            'profile_id': profile_id,
            'type': type,
            'start': start,
            'limit': limit,
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/reports'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a report.

        Retrieve a report by specifying its ID. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Report` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_summary(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a report summary.

        Retrieve the complete summarized information for a report. For more information,
        see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportSummary` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_summary',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/summary'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_evaluation(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        exclude_summary: bool = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report evaluation details.

        Retrieve the evaluation details of a report by specifying the report ID. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param bool exclude_summary: (optional) The indication of whether report
               summary metadata must be excluded.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_evaluation',
        )
        headers.update(sdk_headers)

        params = {
            'exclude_summary': exclude_summary,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/csv'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/download'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_controls(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        control_id: str = None,
        control_name: str = None,
        control_description: str = None,
        control_category: str = None,
        status: str = None,
        sort: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report controls.

        Retrieve a sorted and filtered list of controls for the specified report. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str control_id: (optional) The ID of the control.
        :param str control_name: (optional) The name of the control.
        :param str control_description: (optional) The description of the control.
        :param str control_category: (optional) A control category value.
        :param str status: (optional) The compliance status value.
        :param str sort: (optional) This field sorts controls by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportControls` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_controls',
        )
        headers.update(sdk_headers)

        params = {
            'control_id': control_id,
            'control_name': control_name,
            'control_description': control_description,
            'control_category': control_category,
            'status': status,
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/controls'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_rule(
        self,
        report_id: str,
        rule_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a report rule.

        Retrieve the rule by specifying the report ID and rule ID. For more information,
        see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str rule_id: The ID of a rule in a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleInfo` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id', 'rule_id']
        path_param_values = self.encode_path_vars(report_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_report_evaluations(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        assessment_id: str = None,
        component_id: str = None,
        target_id: str = None,
        target_name: str = None,
        status: str = None,
        start: str = None,
        limit: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List report evaluations.

        Get a paginated list of evaluations for the specified report. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str assessment_id: (optional) The ID of the assessment.
        :param str component_id: (optional) The ID of component.
        :param str target_id: (optional) The ID of the evaluation target.
        :param str target_name: (optional) The name of the evaluation target.
        :param str status: (optional) The evaluation status value.
        :param str start: (optional) The indication of what resource to start the
               page on.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EvaluationPage` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_report_evaluations',
        )
        headers.update(sdk_headers)

        params = {
            'assessment_id': assessment_id,
            'component_id': component_id,
            'target_id': target_id,
            'target_name': target_name,
            'status': status,
            'start': start,
            'limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/evaluations'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def list_report_resources(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        id: str = None,
        resource_name: str = None,
        account_id: str = None,
        component_id: str = None,
        status: str = None,
        sort: str = None,
        start: str = None,
        limit: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List report resources.

        Get a paginated list of resources for the specified report. For more information,
        see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str id: (optional) The ID of the resource.
        :param str resource_name: (optional) The name of the resource.
        :param str account_id: (optional) The ID of the account owning a resource.
        :param str component_id: (optional) The ID of component.
        :param str status: (optional) The compliance status value.
        :param str sort: (optional) This field sorts resources by using a valid
               sort field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param str start: (optional) The indication of what resource to start the
               page on.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourcePage` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_report_resources',
        )
        headers.update(sdk_headers)

        params = {
            'id': id,
            'resource_name': resource_name,
            'account_id': account_id,
            'component_id': component_id,
            'status': status,
            'sort': sort,
            'start': start,
            'limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/resources'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_tags(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report tags.

        Retrieve a list of tags for the specified report. For more information, see
        [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportTags` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_tags',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/tags'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_violations_drift(
        self,
        report_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        scan_time_duration: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report violations drift.

        Get a list of report violation data points for the specified report and time
        frame. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param int scan_time_duration: (optional) The duration of the `scan_time`
               timestamp in number of days.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportViolationsDrift` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_violations_drift',
        )
        headers.update(sdk_headers)

        params = {
            'scan_time_duration': scan_time_duration,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id']
        path_param_values = self.encode_path_vars(report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/reports/{report_id}/violations_drift'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Provider types
    #########################

    def list_provider_types(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all provider types.

        List all the registered provider types. For more information about connecting
        Workload Protection with the Security and Compliance Center, see [Connecting
        Workload
        Protection](/docs/security-compliance?topic=security-compliance-setup-workload-protection&interface=api#wp-register).

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypesCollection` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_provider_types',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/provider_types'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_provider_type_by_id(
        self,
        provider_type_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a provider type.

        Retrieve a provider type by specifying its ID. For more information about
        integrations, see [Connecting Workload
        Protection](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str provider_type_id: The provider type ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeItem` object
        """

        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_provider_type_by_id',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['provider_type_id']
        path_param_values = self.encode_path_vars(provider_type_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/provider_types/{provider_type_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Provider type instances
    #########################

    def list_provider_type_instances(
        self,
        provider_type_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all provider type instances.

        Retrieve all instances of provider type. For more information about integrations,
        see [Connecting Workload
        Protection](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str provider_type_id: The provider type ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstancesResponse` object
        """

        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_provider_type_instances',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['provider_type_id']
        path_param_values = self.encode_path_vars(provider_type_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/provider_types/{provider_type_id}/provider_type_instances'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_provider_type_instance(
        self,
        provider_type_id: str,
        *,
        name: str = None,
        attributes: dict = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a provider type instance.

        Create an instance of a provider type. For more information about integrations,
        see [Connecting Workload
        Protection](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str provider_type_id: The provider type ID.
        :param str name: (optional) The provider type instance name.
        :param dict attributes: (optional) The attributes for connecting to the
               provider type instance.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstanceItem` object
        """

        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_provider_type_instance',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'attributes': attributes,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['provider_type_id']
        path_param_values = self.encode_path_vars(provider_type_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/provider_types/{provider_type_id}/provider_type_instances'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )
        response = self.send(request, **kwargs)
        return response

    def delete_provider_type_instance(
        self,
        provider_type_id: str,
        provider_type_instance_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Remove a specific instance of a provider type.

        Remove a specific instance of a provider type.

        :param str provider_type_id: The provider type ID.
        :param str provider_type_instance_id: The provider type instance ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        if not provider_type_instance_id:
            raise ValueError('provider_type_instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_provider_type_instance',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['provider_type_id', 'provider_type_instance_id']
        path_param_values = self.encode_path_vars(provider_type_id, provider_type_instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/provider_types/{provider_type_id}/provider_type_instances/{provider_type_instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_provider_type_instance(
        self,
        provider_type_id: str,
        provider_type_instance_id: str,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List a provider type instance.

        Retrieve a provider type instance by specifying the provider type ID, and Security
        and Compliance Center instance ID. For more information about integrations, see
        [Connecting Workload
        Protection](https://test.cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str provider_type_id: The provider type ID.
        :param str provider_type_instance_id: The provider type instance ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstanceItem` object
        """

        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        if not provider_type_instance_id:
            raise ValueError('provider_type_instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_provider_type_instance',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['provider_type_id', 'provider_type_instance_id']
        path_param_values = self.encode_path_vars(provider_type_id, provider_type_instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/provider_types/{provider_type_id}/provider_type_instances/{provider_type_instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_provider_type_instance(
        self,
        provider_type_id: str,
        provider_type_instance_id: str,
        *,
        name: str = None,
        attributes: dict = None,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Patch a specific instance of a provider type.

        Patch a specific instance of a provider type.

        :param str provider_type_id: The provider type ID.
        :param str provider_type_instance_id: The provider type instance ID.
        :param str name: (optional) The provider type instance name.
        :param dict attributes: (optional) The attributes for connecting to the
               provider type instance.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstanceItem` object
        """

        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        if not provider_type_instance_id:
            raise ValueError('provider_type_instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='update_provider_type_instance',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'attributes': attributes,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['provider_type_id', 'provider_type_instance_id']
        path_param_values = self.encode_path_vars(provider_type_id, provider_type_instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/provider_types/{provider_type_id}/provider_type_instances/{provider_type_instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_provider_types_instances(
        self,
        *,
        x_correlation_id: str = None,
        x_request_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of instances for all provider types.

        Get a list of instances for all provider types.

        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this headers is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypesInstancesResponse` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id,
            'X-Request-ID': x_request_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_provider_types_instances',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/provider_types_instances'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


class ListReportsEnums:
    """
    Enums for list_reports parameters.
    """

    class Type(str, Enum):
        """
        The type of the scan.
        """

        ONDEMAND = 'ondemand'
        SCHEDULED = 'scheduled'


class GetReportControlsEnums:
    """
    Enums for get_report_controls parameters.
    """

    class Status(str, Enum):
        """
        The compliance status value.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'
    class Sort(str, Enum):
        """
        This field sorts controls by using a valid sort field. To learn more, see
        [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        """

        CONTROL_NAME = 'control_name'
        CONTROL_CATEGORY = 'control_category'
        STATUS = 'status'


class ListReportEvaluationsEnums:
    """
    Enums for list_report_evaluations parameters.
    """

    class Status(str, Enum):
        """
        The evaluation status value.
        """

        PASS = 'pass'
        FAILURE = 'failure'
        ERROR = 'error'
        SKIPPED = 'skipped'


class ListReportResourcesEnums:
    """
    Enums for list_report_resources parameters.
    """

    class Status(str, Enum):
        """
        The compliance status value.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'
    class Sort(str, Enum):
        """
        This field sorts resources by using a valid sort field. To learn more, see
        [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        """

        ACCOUNT_ID = 'account_id'
        COMPONENT_ID = 'component_id'
        RESOURCE_NAME = 'resource_name'
        STATUS = 'status'


##############################################################################
# Models
##############################################################################


class Account:
    """
    The account that is associated with a report.

    :attr str id: (optional) The account ID.
    :attr str name: (optional) The account name.
    :attr str type: (optional) The account type.
    """

    def __init__(
        self,
        *,
        id: str = None,
        name: str = None,
        type: str = None,
    ) -> None:
        """
        Initialize a Account object.

        :param str id: (optional) The account ID.
        :param str name: (optional) The account name.
        :param str type: (optional) The account type.
        """
        self.id = id
        self.name = name
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Account':
        """Initialize a Account object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Account object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Account object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Account') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Account') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AdditionalProperty:
    """
    AdditionalProperty.

    :attr str type: An additional property that indicates the type of the attribute
          in various formats (text, url, secret, label, masked).
    :attr str display_name: The name of the attribute that is displayed in the UI.
    """

    def __init__(
        self,
        type: str,
        display_name: str,
    ) -> None:
        """
        Initialize a AdditionalProperty object.

        :param str type: An additional property that indicates the type of the
               attribute in various formats (text, url, secret, label, masked).
        :param str display_name: The name of the attribute that is displayed in the
               UI.
        """
        self.type = type
        self.display_name = display_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AdditionalProperty':
        """Initialize a AdditionalProperty object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AdditionalProperty JSON')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        else:
            raise ValueError('Required property \'display_name\' not present in AdditionalProperty JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AdditionalProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AdditionalProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AdditionalProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AdditionalProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        An additional property that indicates the type of the attribute in various formats
        (text, url, secret, label, masked).
        """

        SECRET = 'secret'
        LABEL = 'label'
        URL = 'url'
        TEXT = 'text'
        MASKED = 'masked'



class AdditionalTargetAttribute:
    """
    The additional target attribute of the service.

    :attr str name: (optional) The additional target attribute name.
    :attr str operator: (optional) The operator.
    :attr str value: (optional) The value.
    """

    def __init__(
        self,
        *,
        name: str = None,
        operator: str = None,
        value: str = None,
    ) -> None:
        """
        Initialize a AdditionalTargetAttribute object.

        :param str name: (optional) The additional target attribute name.
        :param str operator: (optional) The operator.
        :param str value: (optional) The value.
        """
        self.name = name
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AdditionalTargetAttribute':
        """Initialize a AdditionalTargetAttribute object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AdditionalTargetAttribute object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AdditionalTargetAttribute object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AdditionalTargetAttribute') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AdditionalTargetAttribute') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator.
        """

        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        STRING_CONTAINS = 'string_contains'
        STRING_NOT_CONTAINS = 'string_not_contains'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        STRINGS_IN_LIST = 'strings_in_list'
        STRINGS_ALLOWED = 'strings_allowed'
        STRINGS_REQUIRED = 'strings_required'
        IPS_IN_RANGE = 'ips_in_range'
        IPS_EQUALS = 'ips_equals'
        IPS_NOT_EQUALS = 'ips_not_equals'
        DAYS_LESS_THAN = 'days_less_than'



class Assessment:
    """
    The control specification assessment.

    :attr str assessment_id: (optional) The assessment ID.
    :attr str assessment_type: (optional) The assessment type.
    :attr str assessment_method: (optional) The assessment method.
    :attr str assessment_description: (optional) The assessment description.
    :attr int parameter_count: (optional) The number of parameters of this
          assessment.
    :attr List[ParameterInfo] parameters: (optional) The list of parameters of this
          assessment.
    """

    def __init__(
        self,
        *,
        assessment_id: str = None,
        assessment_type: str = None,
        assessment_method: str = None,
        assessment_description: str = None,
        parameter_count: int = None,
        parameters: List['ParameterInfo'] = None,
    ) -> None:
        """
        Initialize a Assessment object.

        :param str assessment_id: (optional) The assessment ID.
        :param str assessment_type: (optional) The assessment type.
        :param str assessment_method: (optional) The assessment method.
        :param str assessment_description: (optional) The assessment description.
        :param int parameter_count: (optional) The number of parameters of this
               assessment.
        :param List[ParameterInfo] parameters: (optional) The list of parameters of
               this assessment.
        """
        self.assessment_id = assessment_id
        self.assessment_type = assessment_type
        self.assessment_method = assessment_method
        self.assessment_description = assessment_description
        self.parameter_count = parameter_count
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Assessment':
        """Initialize a Assessment object from a json dictionary."""
        args = {}
        if 'assessment_id' in _dict:
            args['assessment_id'] = _dict.get('assessment_id')
        if 'assessment_type' in _dict:
            args['assessment_type'] = _dict.get('assessment_type')
        if 'assessment_method' in _dict:
            args['assessment_method'] = _dict.get('assessment_method')
        if 'assessment_description' in _dict:
            args['assessment_description'] = _dict.get('assessment_description')
        if 'parameter_count' in _dict:
            args['parameter_count'] = _dict.get('parameter_count')
        if 'parameters' in _dict:
            args['parameters'] = [ParameterInfo.from_dict(v) for v in _dict.get('parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Assessment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assessment_id') and self.assessment_id is not None:
            _dict['assessment_id'] = self.assessment_id
        if hasattr(self, 'assessment_type') and self.assessment_type is not None:
            _dict['assessment_type'] = self.assessment_type
        if hasattr(self, 'assessment_method') and self.assessment_method is not None:
            _dict['assessment_method'] = self.assessment_method
        if hasattr(self, 'assessment_description') and self.assessment_description is not None:
            _dict['assessment_description'] = self.assessment_description
        if hasattr(self, 'parameter_count') and self.parameter_count is not None:
            _dict['parameter_count'] = self.parameter_count
        if hasattr(self, 'parameters') and self.parameters is not None:
            parameters_list = []
            for v in self.parameters:
                if isinstance(v, dict):
                    parameters_list.append(v)
                else:
                    parameters_list.append(v.to_dict())
            _dict['parameters'] = parameters_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Assessment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Assessment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Assessment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Attachment:
    """
    The attachment that is associated with a report.

    :attr str id: (optional) The attachment ID.
    :attr str name: (optional) The name of the attachment.
    :attr str description: (optional) The description of the attachment.
    :attr str schedule: (optional) The attachment schedule.
    :attr List[AttachmentScope] scope: (optional) The scope of the attachment.
    """

    def __init__(
        self,
        *,
        id: str = None,
        name: str = None,
        description: str = None,
        schedule: str = None,
        scope: List['AttachmentScope'] = None,
    ) -> None:
        """
        Initialize a Attachment object.

        :param str id: (optional) The attachment ID.
        :param str name: (optional) The name of the attachment.
        :param str description: (optional) The description of the attachment.
        :param str schedule: (optional) The attachment schedule.
        :param List[AttachmentScope] scope: (optional) The scope of the attachment.
        """
        self.id = id
        self.name = name
        self.description = description
        self.schedule = schedule
        self.scope = scope

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Attachment':
        """Initialize a Attachment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'schedule' in _dict:
            args['schedule'] = _dict.get('schedule')
        if 'scope' in _dict:
            args['scope'] = [AttachmentScope.from_dict(v) for v in _dict.get('scope')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Attachment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'schedule') and self.schedule is not None:
            _dict['schedule'] = self.schedule
        if hasattr(self, 'scope') and self.scope is not None:
            scope_list = []
            for v in self.scope:
                if isinstance(v, dict):
                    scope_list.append(v)
                else:
                    scope_list.append(v.to_dict())
            _dict['scope'] = scope_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Attachment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Attachment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Attachment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentCollection:
    """
    The response body of an attachment.

    :attr int total_count: The number of attachments.
    :attr int limit: The limit of attachments per request.
    :attr PaginatedCollectionFirst first: The reference to the first page of
          entries.
    :attr PaginatedCollectionNext next: The reference URL for the next few entries.
    :attr List[AttachmentItem] attachments: The list of attachments.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'PaginatedCollectionFirst',
        next: 'PaginatedCollectionNext',
        attachments: List['AttachmentItem'],
    ) -> None:
        """
        Initialize a AttachmentCollection object.

        :param int total_count: The number of attachments.
        :param int limit: The limit of attachments per request.
        :param PaginatedCollectionFirst first: The reference to the first page of
               entries.
        :param PaginatedCollectionNext next: The reference URL for the next few
               entries.
        :param List[AttachmentItem] attachments: The list of attachments.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.next = next
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentCollection':
        """Initialize a AttachmentCollection object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in AttachmentCollection JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in AttachmentCollection JSON')
        if 'first' in _dict:
            args['first'] = PaginatedCollectionFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in AttachmentCollection JSON')
        if 'next' in _dict:
            args['next'] = PaginatedCollectionNext.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in AttachmentCollection JSON')
        if 'attachments' in _dict:
            args['attachments'] = [AttachmentItem.from_dict(v) for v in _dict.get('attachments')]
        else:
            raise ValueError('Required property \'attachments\' not present in AttachmentCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'attachments') and self.attachments is not None:
            attachments_list = []
            for v in self.attachments:
                if isinstance(v, dict):
                    attachments_list.append(v)
                else:
                    attachments_list.append(v.to_dict())
            _dict['attachments'] = attachments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentItem:
    """
    The request payload of the attachments parameter.

    :attr str id: (optional) The ID of the attachment.
    :attr str profile_id: (optional) The ID of the profile that is specified in the
          attachment.
    :attr str account_id: (optional) The account ID that is associated to the
          attachment.
    :attr str instance_id: (optional) The instance ID of the account that is
          associated to the attachment.
    :attr List[MultiCloudScope] scope: (optional) The scope payload for the multi
          cloud feature.
    :attr datetime created_on: (optional) The date when the attachment was created.
    :attr str created_by: (optional) The user who created the attachment.
    :attr datetime updated_on: (optional) The date when the attachment was updated.
    :attr str updated_by: (optional) The user who updated the attachment.
    :attr str status: (optional) The status of an attachment evaluation.
    :attr str schedule: (optional) The schedule of an attachment evaluation.
    :attr AttachmentsNotificationsPrototype notifications: (optional) The request
          payload of the attachment notifications.
    :attr List[AttachmentParameterPrototype] attachment_parameters: (optional) The
          profile parameters for the attachment.
    :attr LastScan last_scan: (optional) The details of the last scan of an
          attachment.
    :attr datetime next_scan_time: (optional) The start time of the next scan.
    :attr str name: (optional) The name of the attachment.
    :attr str description: (optional) The description for the attachment.
    """

    def __init__(
        self,
        *,
        id: str = None,
        profile_id: str = None,
        account_id: str = None,
        instance_id: str = None,
        scope: List['MultiCloudScope'] = None,
        created_on: datetime = None,
        created_by: str = None,
        updated_on: datetime = None,
        updated_by: str = None,
        status: str = None,
        schedule: str = None,
        notifications: 'AttachmentsNotificationsPrototype' = None,
        attachment_parameters: List['AttachmentParameterPrototype'] = None,
        last_scan: 'LastScan' = None,
        next_scan_time: datetime = None,
        name: str = None,
        description: str = None,
    ) -> None:
        """
        Initialize a AttachmentItem object.

        :param str id: (optional) The ID of the attachment.
        :param str profile_id: (optional) The ID of the profile that is specified
               in the attachment.
        :param str account_id: (optional) The account ID that is associated to the
               attachment.
        :param str instance_id: (optional) The instance ID of the account that is
               associated to the attachment.
        :param List[MultiCloudScope] scope: (optional) The scope payload for the
               multi cloud feature.
        :param datetime created_on: (optional) The date when the attachment was
               created.
        :param str created_by: (optional) The user who created the attachment.
        :param datetime updated_on: (optional) The date when the attachment was
               updated.
        :param str updated_by: (optional) The user who updated the attachment.
        :param str status: (optional) The status of an attachment evaluation.
        :param str schedule: (optional) The schedule of an attachment evaluation.
        :param AttachmentsNotificationsPrototype notifications: (optional) The
               request payload of the attachment notifications.
        :param List[AttachmentParameterPrototype] attachment_parameters: (optional)
               The profile parameters for the attachment.
        :param LastScan last_scan: (optional) The details of the last scan of an
               attachment.
        :param datetime next_scan_time: (optional) The start time of the next scan.
        :param str name: (optional) The name of the attachment.
        :param str description: (optional) The description for the attachment.
        """
        self.id = id
        self.profile_id = profile_id
        self.account_id = account_id
        self.instance_id = instance_id
        self.scope = scope
        self.created_on = created_on
        self.created_by = created_by
        self.updated_on = updated_on
        self.updated_by = updated_by
        self.status = status
        self.schedule = schedule
        self.notifications = notifications
        self.attachment_parameters = attachment_parameters
        self.last_scan = last_scan
        self.next_scan_time = next_scan_time
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentItem':
        """Initialize a AttachmentItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'profile_id' in _dict:
            args['profile_id'] = _dict.get('profile_id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'scope' in _dict:
            args['scope'] = [MultiCloudScope.from_dict(v) for v in _dict.get('scope')]
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'schedule' in _dict:
            args['schedule'] = _dict.get('schedule')
        if 'notifications' in _dict:
            args['notifications'] = AttachmentsNotificationsPrototype.from_dict(_dict.get('notifications'))
        if 'attachment_parameters' in _dict:
            args['attachment_parameters'] = [AttachmentParameterPrototype.from_dict(v) for v in _dict.get('attachment_parameters')]
        if 'last_scan' in _dict:
            args['last_scan'] = LastScan.from_dict(_dict.get('last_scan'))
        if 'next_scan_time' in _dict:
            args['next_scan_time'] = string_to_datetime(_dict.get('next_scan_time'))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'profile_id') and self.profile_id is not None:
            _dict['profile_id'] = self.profile_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'scope') and self.scope is not None:
            scope_list = []
            for v in self.scope:
                if isinstance(v, dict):
                    scope_list.append(v)
                else:
                    scope_list.append(v.to_dict())
            _dict['scope'] = scope_list
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'schedule') and self.schedule is not None:
            _dict['schedule'] = self.schedule
        if hasattr(self, 'notifications') and self.notifications is not None:
            if isinstance(self.notifications, dict):
                _dict['notifications'] = self.notifications
            else:
                _dict['notifications'] = self.notifications.to_dict()
        if hasattr(self, 'attachment_parameters') and self.attachment_parameters is not None:
            attachment_parameters_list = []
            for v in self.attachment_parameters:
                if isinstance(v, dict):
                    attachment_parameters_list.append(v)
                else:
                    attachment_parameters_list.append(v.to_dict())
            _dict['attachment_parameters'] = attachment_parameters_list
        if hasattr(self, 'last_scan') and self.last_scan is not None:
            if isinstance(self.last_scan, dict):
                _dict['last_scan'] = self.last_scan
            else:
                _dict['last_scan'] = self.last_scan.to_dict()
        if hasattr(self, 'next_scan_time') and self.next_scan_time is not None:
            _dict['next_scan_time'] = datetime_to_string(self.next_scan_time)
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of an attachment evaluation.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'


    class ScheduleEnum(str, Enum):
        """
        The schedule of an attachment evaluation.
        """

        DAILY = 'daily'
        EVERY_7_DAYS = 'every_7_days'
        EVERY_30_DAYS = 'every_30_days'



class AttachmentParameterPrototype:
    """
    The parameters related to the Attachment.

    :attr str assessment_type: (optional) The type of the implementation.
    :attr str assessment_id: (optional) The implementation ID of the parameter.
    :attr str parameter_name: (optional) The parameter name.
    :attr str parameter_value: (optional) The value of the parameter.
    :attr str parameter_display_name: (optional) The parameter display name.
    :attr str parameter_type: (optional) The parameter type.
    """

    def __init__(
        self,
        *,
        assessment_type: str = None,
        assessment_id: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        parameter_display_name: str = None,
        parameter_type: str = None,
    ) -> None:
        """
        Initialize a AttachmentParameterPrototype object.

        :param str assessment_type: (optional) The type of the implementation.
        :param str assessment_id: (optional) The implementation ID of the
               parameter.
        :param str parameter_name: (optional) The parameter name.
        :param str parameter_value: (optional) The value of the parameter.
        :param str parameter_display_name: (optional) The parameter display name.
        :param str parameter_type: (optional) The parameter type.
        """
        self.assessment_type = assessment_type
        self.assessment_id = assessment_id
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.parameter_display_name = parameter_display_name
        self.parameter_type = parameter_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentParameterPrototype':
        """Initialize a AttachmentParameterPrototype object from a json dictionary."""
        args = {}
        if 'assessment_type' in _dict:
            args['assessment_type'] = _dict.get('assessment_type')
        if 'assessment_id' in _dict:
            args['assessment_id'] = _dict.get('assessment_id')
        if 'parameter_name' in _dict:
            args['parameter_name'] = _dict.get('parameter_name')
        if 'parameter_value' in _dict:
            args['parameter_value'] = _dict.get('parameter_value')
        if 'parameter_display_name' in _dict:
            args['parameter_display_name'] = _dict.get('parameter_display_name')
        if 'parameter_type' in _dict:
            args['parameter_type'] = _dict.get('parameter_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentParameterPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assessment_type') and self.assessment_type is not None:
            _dict['assessment_type'] = self.assessment_type
        if hasattr(self, 'assessment_id') and self.assessment_id is not None:
            _dict['assessment_id'] = self.assessment_id
        if hasattr(self, 'parameter_name') and self.parameter_name is not None:
            _dict['parameter_name'] = self.parameter_name
        if hasattr(self, 'parameter_value') and self.parameter_value is not None:
            _dict['parameter_value'] = self.parameter_value
        if hasattr(self, 'parameter_display_name') and self.parameter_display_name is not None:
            _dict['parameter_display_name'] = self.parameter_display_name
        if hasattr(self, 'parameter_type') and self.parameter_type is not None:
            _dict['parameter_type'] = self.parameter_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentParameterPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentParameterPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentParameterPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ParameterTypeEnum(str, Enum):
        """
        The parameter type.
        """

        STRING = 'string'
        NUMERIC = 'numeric'
        GENERAL = 'general'
        BOOLEAN = 'boolean'
        STRING_LIST = 'string_list'
        IP_LIST = 'ip_list'
        TIMESTAMP = 'timestamp'



class AttachmentPrototype:
    """
    The request body of getting an attachment that is associated with your account.

    :attr str profile_id: (optional) The ID of the profile that is specified in the
          attachment.
    :attr List[AttachmentsPrototype] attachments: The array that displays all of the
          available attachments.
    """

    def __init__(
        self,
        attachments: List['AttachmentsPrototype'],
        *,
        profile_id: str = None,
    ) -> None:
        """
        Initialize a AttachmentPrototype object.

        :param List[AttachmentsPrototype] attachments: The array that displays all
               of the available attachments.
        :param str profile_id: (optional) The ID of the profile that is specified
               in the attachment.
        """
        self.profile_id = profile_id
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentPrototype':
        """Initialize a AttachmentPrototype object from a json dictionary."""
        args = {}
        if 'profile_id' in _dict:
            args['profile_id'] = _dict.get('profile_id')
        if 'attachments' in _dict:
            args['attachments'] = [AttachmentsPrototype.from_dict(v) for v in _dict.get('attachments')]
        else:
            raise ValueError('Required property \'attachments\' not present in AttachmentPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'profile_id') and self.profile_id is not None:
            _dict['profile_id'] = self.profile_id
        if hasattr(self, 'attachments') and self.attachments is not None:
            attachments_list = []
            for v in self.attachments:
                if isinstance(v, dict):
                    attachments_list.append(v)
                else:
                    attachments_list.append(v.to_dict())
            _dict['attachments'] = attachments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentScope:
    """
    A scope of the attachment.

    :attr str id: (optional) The unique identifier for this scope.
    :attr str environment: (optional) The environment that relates to this scope.
    :attr List[ScopeProperty] properties: (optional) The properties that are
          supported for scoping by this environment.
    """

    def __init__(
        self,
        *,
        id: str = None,
        environment: str = None,
        properties: List['ScopeProperty'] = None,
    ) -> None:
        """
        Initialize a AttachmentScope object.

        :param str id: (optional) The unique identifier for this scope.
        :param str environment: (optional) The environment that relates to this
               scope.
        :param List[ScopeProperty] properties: (optional) The properties that are
               supported for scoping by this environment.
        """
        self.id = id
        self.environment = environment
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentScope':
        """Initialize a AttachmentScope object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'properties' in _dict:
            args['properties'] = [ScopeProperty.from_dict(v) for v in _dict.get('properties')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentScope object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentScope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentScope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentScope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentsNotificationsPrototype:
    """
    The request payload of the attachment notifications.

    :attr bool enabled: enabled notifications.
    :attr FailedControls controls: The failed controls.
    """

    def __init__(
        self,
        enabled: bool,
        controls: 'FailedControls',
    ) -> None:
        """
        Initialize a AttachmentsNotificationsPrototype object.

        :param bool enabled: enabled notifications.
        :param FailedControls controls: The failed controls.
        """
        self.enabled = enabled
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentsNotificationsPrototype':
        """Initialize a AttachmentsNotificationsPrototype object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in AttachmentsNotificationsPrototype JSON')
        if 'controls' in _dict:
            args['controls'] = FailedControls.from_dict(_dict.get('controls'))
        else:
            raise ValueError('Required property \'controls\' not present in AttachmentsNotificationsPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentsNotificationsPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'controls') and self.controls is not None:
            if isinstance(self.controls, dict):
                _dict['controls'] = self.controls
            else:
                _dict['controls'] = self.controls.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentsNotificationsPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentsNotificationsPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentsNotificationsPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentsPrototype:
    """
    The request payload of getting all of the attachments that are associated with the
    account.

    :attr str id: (optional) The id that is generated from the scope type and ID.
    :attr str name: The name that is generated from the scope type and ID.
    :attr str description: (optional) The description for the attachment.
    :attr List[MultiCloudScope] scope: The scope payload for the multi cloud
          feature.
    :attr str status: The status of the scan of an attachment.
    :attr str schedule: The schedule of an attachment evaluation.
    :attr AttachmentsNotificationsPrototype notifications: (optional) The request
          payload of the attachment notifications.
    :attr List[AttachmentParameterPrototype] attachment_parameters: The profile
          parameters for the attachment.
    """

    def __init__(
        self,
        name: str,
        scope: List['MultiCloudScope'],
        status: str,
        schedule: str,
        attachment_parameters: List['AttachmentParameterPrototype'],
        *,
        id: str = None,
        description: str = None,
        notifications: 'AttachmentsNotificationsPrototype' = None,
    ) -> None:
        """
        Initialize a AttachmentsPrototype object.

        :param str name: The name that is generated from the scope type and ID.
        :param List[MultiCloudScope] scope: The scope payload for the multi cloud
               feature.
        :param str status: The status of the scan of an attachment.
        :param str schedule: The schedule of an attachment evaluation.
        :param List[AttachmentParameterPrototype] attachment_parameters: The
               profile parameters for the attachment.
        :param str id: (optional) The id that is generated from the scope type and
               ID.
        :param str description: (optional) The description for the attachment.
        :param AttachmentsNotificationsPrototype notifications: (optional) The
               request payload of the attachment notifications.
        """
        self.id = id
        self.name = name
        self.description = description
        self.scope = scope
        self.status = status
        self.schedule = schedule
        self.notifications = notifications
        self.attachment_parameters = attachment_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentsPrototype':
        """Initialize a AttachmentsPrototype object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in AttachmentsPrototype JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'scope' in _dict:
            args['scope'] = [MultiCloudScope.from_dict(v) for v in _dict.get('scope')]
        else:
            raise ValueError('Required property \'scope\' not present in AttachmentsPrototype JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in AttachmentsPrototype JSON')
        if 'schedule' in _dict:
            args['schedule'] = _dict.get('schedule')
        else:
            raise ValueError('Required property \'schedule\' not present in AttachmentsPrototype JSON')
        if 'notifications' in _dict:
            args['notifications'] = AttachmentsNotificationsPrototype.from_dict(_dict.get('notifications'))
        if 'attachment_parameters' in _dict:
            args['attachment_parameters'] = [AttachmentParameterPrototype.from_dict(v) for v in _dict.get('attachment_parameters')]
        else:
            raise ValueError('Required property \'attachment_parameters\' not present in AttachmentsPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentsPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'scope') and self.scope is not None:
            scope_list = []
            for v in self.scope:
                if isinstance(v, dict):
                    scope_list.append(v)
                else:
                    scope_list.append(v.to_dict())
            _dict['scope'] = scope_list
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'schedule') and self.schedule is not None:
            _dict['schedule'] = self.schedule
        if hasattr(self, 'notifications') and self.notifications is not None:
            if isinstance(self.notifications, dict):
                _dict['notifications'] = self.notifications
            else:
                _dict['notifications'] = self.notifications.to_dict()
        if hasattr(self, 'attachment_parameters') and self.attachment_parameters is not None:
            attachment_parameters_list = []
            for v in self.attachment_parameters:
                if isinstance(v, dict):
                    attachment_parameters_list.append(v)
                else:
                    attachment_parameters_list.append(v.to_dict())
            _dict['attachment_parameters'] = attachment_parameters_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentsPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentsPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentsPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the scan of an attachment.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'


    class ScheduleEnum(str, Enum):
        """
        The schedule of an attachment evaluation.
        """

        DAILY = 'daily'
        EVERY_7_DAYS = 'every_7_days'
        EVERY_30_DAYS = 'every_30_days'



class ComplianceScore:
    """
    The compliance score.

    :attr int passed: (optional) The number of successful evaluations.
    :attr int total_count: (optional) The total number of evaluations.
    :attr int percent: (optional) The percentage of successful evaluations.
    """

    def __init__(
        self,
        *,
        passed: int = None,
        total_count: int = None,
        percent: int = None,
    ) -> None:
        """
        Initialize a ComplianceScore object.

        :param int passed: (optional) The number of successful evaluations.
        :param int total_count: (optional) The total number of evaluations.
        :param int percent: (optional) The percentage of successful evaluations.
        """
        self.passed = passed
        self.total_count = total_count
        self.percent = percent

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComplianceScore':
        """Initialize a ComplianceScore object from a json dictionary."""
        args = {}
        if 'passed' in _dict:
            args['passed'] = _dict.get('passed')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'percent' in _dict:
            args['percent'] = _dict.get('percent')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComplianceScore object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'passed') and self.passed is not None:
            _dict['passed'] = self.passed
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'percent') and self.percent is not None:
            _dict['percent'] = self.percent
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComplianceScore object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComplianceScore') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComplianceScore') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComplianceStats:
    """
    The compliance stats.

    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of checks.
    :attr int compliant_count: (optional) The number of compliant checks.
    :attr int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :attr int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :attr int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    """

    def __init__(
        self,
        *,
        status: str = None,
        total_count: int = None,
        compliant_count: int = None,
        not_compliant_count: int = None,
        unable_to_perform_count: int = None,
        user_evaluation_required_count: int = None,
    ) -> None:
        """
        Initialize a ComplianceStats object.

        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        """
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComplianceStats':
        """Initialize a ComplianceStats object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'compliant_count' in _dict:
            args['compliant_count'] = _dict.get('compliant_count')
        if 'not_compliant_count' in _dict:
            args['not_compliant_count'] = _dict.get('not_compliant_count')
        if 'unable_to_perform_count' in _dict:
            args['unable_to_perform_count'] = _dict.get('unable_to_perform_count')
        if 'user_evaluation_required_count' in _dict:
            args['user_evaluation_required_count'] = _dict.get('user_evaluation_required_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComplianceStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'compliant_count') and self.compliant_count is not None:
            _dict['compliant_count'] = self.compliant_count
        if hasattr(self, 'not_compliant_count') and self.not_compliant_count is not None:
            _dict['not_compliant_count'] = self.not_compliant_count
        if hasattr(self, 'unable_to_perform_count') and self.unable_to_perform_count is not None:
            _dict['unable_to_perform_count'] = self.unable_to_perform_count
        if hasattr(self, 'user_evaluation_required_count') and self.user_evaluation_required_count is not None:
            _dict['user_evaluation_required_count'] = self.user_evaluation_required_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComplianceStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComplianceStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComplianceStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class ControlDocs:
    """
    The control documentation.

    :attr str control_docs_id: (optional) The ID of the control documentation.
    :attr str control_docs_type: (optional) The type of control documentation.
    """

    def __init__(
        self,
        *,
        control_docs_id: str = None,
        control_docs_type: str = None,
    ) -> None:
        """
        Initialize a ControlDocs object.

        :param str control_docs_id: (optional) The ID of the control documentation.
        :param str control_docs_type: (optional) The type of control documentation.
        """
        self.control_docs_id = control_docs_id
        self.control_docs_type = control_docs_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlDocs':
        """Initialize a ControlDocs object from a json dictionary."""
        args = {}
        if 'control_docs_id' in _dict:
            args['control_docs_id'] = _dict.get('control_docs_id')
        if 'control_docs_type' in _dict:
            args['control_docs_type'] = _dict.get('control_docs_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlDocs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_docs_id') and self.control_docs_id is not None:
            _dict['control_docs_id'] = self.control_docs_id
        if hasattr(self, 'control_docs_type') and self.control_docs_type is not None:
            _dict['control_docs_type'] = self.control_docs_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlDocs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlDocs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlDocs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlLibrary:
    """
    The request payload of the control library.

    :attr str id: (optional) The control library ID.
    :attr str account_id: (optional) The account ID.
    :attr str control_library_name: (optional) The control library name.
    :attr str control_library_description: (optional) The control library
          description.
    :attr str control_library_type: (optional) The control library type.
    :attr str version_group_label: (optional) The version group label.
    :attr str control_library_version: (optional) The control library version.
    :attr datetime created_on: (optional) The date when the control library was
          created.
    :attr str created_by: (optional) The user who created the control library.
    :attr datetime updated_on: (optional) The date when the control library was
          updated.
    :attr str updated_by: (optional) The user who updated the control library.
    :attr bool latest: (optional) The latest version of the control library.
    :attr bool hierarchy_enabled: (optional) The indication of whether hierarchy is
          enabled for the control library.
    :attr int controls_count: (optional) The number of controls.
    :attr int control_parents_count: (optional) The number of parent controls in the
          control library.
    :attr List[ControlsInControlLib] controls: (optional) The list of controls in a
          control library.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        control_library_name: str = None,
        control_library_description: str = None,
        control_library_type: str = None,
        version_group_label: str = None,
        control_library_version: str = None,
        created_on: datetime = None,
        created_by: str = None,
        updated_on: datetime = None,
        updated_by: str = None,
        latest: bool = None,
        hierarchy_enabled: bool = None,
        controls_count: int = None,
        control_parents_count: int = None,
        controls: List['ControlsInControlLib'] = None,
    ) -> None:
        """
        Initialize a ControlLibrary object.

        :param str id: (optional) The control library ID.
        :param str account_id: (optional) The account ID.
        :param str control_library_name: (optional) The control library name.
        :param str control_library_description: (optional) The control library
               description.
        :param str control_library_type: (optional) The control library type.
        :param str version_group_label: (optional) The version group label.
        :param str control_library_version: (optional) The control library version.
        :param datetime created_on: (optional) The date when the control library
               was created.
        :param str created_by: (optional) The user who created the control library.
        :param datetime updated_on: (optional) The date when the control library
               was updated.
        :param str updated_by: (optional) The user who updated the control library.
        :param bool latest: (optional) The latest version of the control library.
        :param bool hierarchy_enabled: (optional) The indication of whether
               hierarchy is enabled for the control library.
        :param int controls_count: (optional) The number of controls.
        :param int control_parents_count: (optional) The number of parent controls
               in the control library.
        :param List[ControlsInControlLib] controls: (optional) The list of controls
               in a control library.
        """
        self.id = id
        self.account_id = account_id
        self.control_library_name = control_library_name
        self.control_library_description = control_library_description
        self.control_library_type = control_library_type
        self.version_group_label = version_group_label
        self.control_library_version = control_library_version
        self.created_on = created_on
        self.created_by = created_by
        self.updated_on = updated_on
        self.updated_by = updated_by
        self.latest = latest
        self.hierarchy_enabled = hierarchy_enabled
        self.controls_count = controls_count
        self.control_parents_count = control_parents_count
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibrary':
        """Initialize a ControlLibrary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'control_library_name' in _dict:
            args['control_library_name'] = _dict.get('control_library_name')
        if 'control_library_description' in _dict:
            args['control_library_description'] = _dict.get('control_library_description')
        if 'control_library_type' in _dict:
            args['control_library_type'] = _dict.get('control_library_type')
        if 'version_group_label' in _dict:
            args['version_group_label'] = _dict.get('version_group_label')
        if 'control_library_version' in _dict:
            args['control_library_version'] = _dict.get('control_library_version')
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'latest' in _dict:
            args['latest'] = _dict.get('latest')
        if 'hierarchy_enabled' in _dict:
            args['hierarchy_enabled'] = _dict.get('hierarchy_enabled')
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        if 'control_parents_count' in _dict:
            args['control_parents_count'] = _dict.get('control_parents_count')
        if 'controls' in _dict:
            args['controls'] = [ControlsInControlLib.from_dict(v) for v in _dict.get('controls')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlLibrary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'control_library_name') and self.control_library_name is not None:
            _dict['control_library_name'] = self.control_library_name
        if hasattr(self, 'control_library_description') and self.control_library_description is not None:
            _dict['control_library_description'] = self.control_library_description
        if hasattr(self, 'control_library_type') and self.control_library_type is not None:
            _dict['control_library_type'] = self.control_library_type
        if hasattr(self, 'version_group_label') and self.version_group_label is not None:
            _dict['version_group_label'] = self.version_group_label
        if hasattr(self, 'control_library_version') and self.control_library_version is not None:
            _dict['control_library_version'] = self.control_library_version
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'latest') and self.latest is not None:
            _dict['latest'] = self.latest
        if hasattr(self, 'hierarchy_enabled') and self.hierarchy_enabled is not None:
            _dict['hierarchy_enabled'] = self.hierarchy_enabled
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
        if hasattr(self, 'control_parents_count') and self.control_parents_count is not None:
            _dict['control_parents_count'] = self.control_parents_count
        if hasattr(self, 'controls') and self.controls is not None:
            controls_list = []
            for v in self.controls:
                if isinstance(v, dict):
                    controls_list.append(v)
                else:
                    controls_list.append(v.to_dict())
            _dict['controls'] = controls_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlLibrary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlLibrary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlLibrary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ControlLibraryTypeEnum(str, Enum):
        """
        The control library type.
        """

        PREDEFINED = 'predefined'
        CUSTOM = 'custom'



class ControlLibraryCollection:
    """
    The response body of control libraries.

    :attr int total_count: The number of control libraries.
    :attr int limit: limit.
    :attr PaginatedCollectionFirst first: The reference to the first page of
          entries.
    :attr PaginatedCollectionNext next: The reference URL for the next few entries.
    :attr List[ControlLibraryItem] control_libraries: The control libraries.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'PaginatedCollectionFirst',
        next: 'PaginatedCollectionNext',
        control_libraries: List['ControlLibraryItem'],
    ) -> None:
        """
        Initialize a ControlLibraryCollection object.

        :param int total_count: The number of control libraries.
        :param int limit: limit.
        :param PaginatedCollectionFirst first: The reference to the first page of
               entries.
        :param PaginatedCollectionNext next: The reference URL for the next few
               entries.
        :param List[ControlLibraryItem] control_libraries: The control libraries.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.next = next
        self.control_libraries = control_libraries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibraryCollection':
        """Initialize a ControlLibraryCollection object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ControlLibraryCollection JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ControlLibraryCollection JSON')
        if 'first' in _dict:
            args['first'] = PaginatedCollectionFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ControlLibraryCollection JSON')
        if 'next' in _dict:
            args['next'] = PaginatedCollectionNext.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ControlLibraryCollection JSON')
        if 'control_libraries' in _dict:
            args['control_libraries'] = [ControlLibraryItem.from_dict(v) for v in _dict.get('control_libraries')]
        else:
            raise ValueError('Required property \'control_libraries\' not present in ControlLibraryCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlLibraryCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'control_libraries') and self.control_libraries is not None:
            control_libraries_list = []
            for v in self.control_libraries:
                if isinstance(v, dict):
                    control_libraries_list.append(v)
                else:
                    control_libraries_list.append(v.to_dict())
            _dict['control_libraries'] = control_libraries_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlLibraryCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlLibraryCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlLibraryCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlLibraryDelete:
    """
    The response body of deleting of a control library.

    :attr str deleted: (optional) The delete message of a control library.
    """

    def __init__(
        self,
        *,
        deleted: str = None,
    ) -> None:
        """
        Initialize a ControlLibraryDelete object.

        :param str deleted: (optional) The delete message of a control library.
        """
        self.deleted = deleted

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibraryDelete':
        """Initialize a ControlLibraryDelete object from a json dictionary."""
        args = {}
        if 'deleted' in _dict:
            args['deleted'] = _dict.get('deleted')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlLibraryDelete object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlLibraryDelete object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlLibraryDelete') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlLibraryDelete') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlLibraryItem:
    """
    ControlLibraryItem.

    :attr str id: (optional) The ID of the control library.
    :attr str account_id: (optional) The Account ID.
    :attr str control_library_name: (optional) The control library name.
    :attr str control_library_description: (optional) The control library
          description.
    :attr str control_library_type: (optional) The control library type.
    :attr datetime created_on: (optional) The date when the control library was
          created.
    :attr str created_by: (optional) The user who created the control library.
    :attr datetime updated_on: (optional) The date when the control library was
          updated.
    :attr str updated_by: (optional) The use who updated the control library.
    :attr str version_group_label: (optional) The version group label.
    :attr str control_library_version: (optional) The control library version.
    :attr bool latest: (optional) The latest control library version.
    :attr int controls_count: (optional) The number of controls.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        control_library_name: str = None,
        control_library_description: str = None,
        control_library_type: str = None,
        created_on: datetime = None,
        created_by: str = None,
        updated_on: datetime = None,
        updated_by: str = None,
        version_group_label: str = None,
        control_library_version: str = None,
        latest: bool = None,
        controls_count: int = None,
    ) -> None:
        """
        Initialize a ControlLibraryItem object.

        :param str id: (optional) The ID of the control library.
        :param str account_id: (optional) The Account ID.
        :param str control_library_name: (optional) The control library name.
        :param str control_library_description: (optional) The control library
               description.
        :param str control_library_type: (optional) The control library type.
        :param datetime created_on: (optional) The date when the control library
               was created.
        :param str created_by: (optional) The user who created the control library.
        :param datetime updated_on: (optional) The date when the control library
               was updated.
        :param str updated_by: (optional) The use who updated the control library.
        :param str version_group_label: (optional) The version group label.
        :param str control_library_version: (optional) The control library version.
        :param bool latest: (optional) The latest control library version.
        :param int controls_count: (optional) The number of controls.
        """
        self.id = id
        self.account_id = account_id
        self.control_library_name = control_library_name
        self.control_library_description = control_library_description
        self.control_library_type = control_library_type
        self.created_on = created_on
        self.created_by = created_by
        self.updated_on = updated_on
        self.updated_by = updated_by
        self.version_group_label = version_group_label
        self.control_library_version = control_library_version
        self.latest = latest
        self.controls_count = controls_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibraryItem':
        """Initialize a ControlLibraryItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'control_library_name' in _dict:
            args['control_library_name'] = _dict.get('control_library_name')
        if 'control_library_description' in _dict:
            args['control_library_description'] = _dict.get('control_library_description')
        if 'control_library_type' in _dict:
            args['control_library_type'] = _dict.get('control_library_type')
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'version_group_label' in _dict:
            args['version_group_label'] = _dict.get('version_group_label')
        if 'control_library_version' in _dict:
            args['control_library_version'] = _dict.get('control_library_version')
        if 'latest' in _dict:
            args['latest'] = _dict.get('latest')
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlLibraryItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'control_library_name') and self.control_library_name is not None:
            _dict['control_library_name'] = self.control_library_name
        if hasattr(self, 'control_library_description') and self.control_library_description is not None:
            _dict['control_library_description'] = self.control_library_description
        if hasattr(self, 'control_library_type') and self.control_library_type is not None:
            _dict['control_library_type'] = self.control_library_type
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'version_group_label') and self.version_group_label is not None:
            _dict['version_group_label'] = self.version_group_label
        if hasattr(self, 'control_library_version') and self.control_library_version is not None:
            _dict['control_library_version'] = self.control_library_version
        if hasattr(self, 'latest') and self.latest is not None:
            _dict['latest'] = self.latest
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlLibraryItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlLibraryItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlLibraryItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlSpecificationWithStats:
    """
    The control specification with compliance stats.

    :attr str control_specification_id: (optional) The control specification ID.
    :attr str component_id: (optional) The component ID.
    :attr str control_specification_description: (optional) The component
          description.
    :attr str environment: (optional) The environment.
    :attr str responsibility: (optional) The responsibility for managing control
          specifications.
    :attr List[Assessment] assessments: (optional) The list of assessments.
    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of checks.
    :attr int compliant_count: (optional) The number of compliant checks.
    :attr int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :attr int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :attr int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    """

    def __init__(
        self,
        *,
        control_specification_id: str = None,
        component_id: str = None,
        control_specification_description: str = None,
        environment: str = None,
        responsibility: str = None,
        assessments: List['Assessment'] = None,
        status: str = None,
        total_count: int = None,
        compliant_count: int = None,
        not_compliant_count: int = None,
        unable_to_perform_count: int = None,
        user_evaluation_required_count: int = None,
    ) -> None:
        """
        Initialize a ControlSpecificationWithStats object.

        :param str control_specification_id: (optional) The control specification
               ID.
        :param str component_id: (optional) The component ID.
        :param str control_specification_description: (optional) The component
               description.
        :param str environment: (optional) The environment.
        :param str responsibility: (optional) The responsibility for managing
               control specifications.
        :param List[Assessment] assessments: (optional) The list of assessments.
        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        """
        self.control_specification_id = control_specification_id
        self.component_id = component_id
        self.control_specification_description = control_specification_description
        self.environment = environment
        self.responsibility = responsibility
        self.assessments = assessments
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSpecificationWithStats':
        """Initialize a ControlSpecificationWithStats object from a json dictionary."""
        args = {}
        if 'control_specification_id' in _dict:
            args['control_specification_id'] = _dict.get('control_specification_id')
        if 'component_id' in _dict:
            args['component_id'] = _dict.get('component_id')
        if 'control_specification_description' in _dict:
            args['control_specification_description'] = _dict.get('control_specification_description')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'responsibility' in _dict:
            args['responsibility'] = _dict.get('responsibility')
        if 'assessments' in _dict:
            args['assessments'] = [Assessment.from_dict(v) for v in _dict.get('assessments')]
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'compliant_count' in _dict:
            args['compliant_count'] = _dict.get('compliant_count')
        if 'not_compliant_count' in _dict:
            args['not_compliant_count'] = _dict.get('not_compliant_count')
        if 'unable_to_perform_count' in _dict:
            args['unable_to_perform_count'] = _dict.get('unable_to_perform_count')
        if 'user_evaluation_required_count' in _dict:
            args['user_evaluation_required_count'] = _dict.get('user_evaluation_required_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlSpecificationWithStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_specification_id') and self.control_specification_id is not None:
            _dict['control_specification_id'] = self.control_specification_id
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'control_specification_description') and self.control_specification_description is not None:
            _dict['control_specification_description'] = self.control_specification_description
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'responsibility') and self.responsibility is not None:
            _dict['responsibility'] = self.responsibility
        if hasattr(self, 'assessments') and self.assessments is not None:
            assessments_list = []
            for v in self.assessments:
                if isinstance(v, dict):
                    assessments_list.append(v)
                else:
                    assessments_list.append(v.to_dict())
            _dict['assessments'] = assessments_list
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'compliant_count') and self.compliant_count is not None:
            _dict['compliant_count'] = self.compliant_count
        if hasattr(self, 'not_compliant_count') and self.not_compliant_count is not None:
            _dict['not_compliant_count'] = self.not_compliant_count
        if hasattr(self, 'unable_to_perform_count') and self.unable_to_perform_count is not None:
            _dict['unable_to_perform_count'] = self.unable_to_perform_count
        if hasattr(self, 'user_evaluation_required_count') and self.user_evaluation_required_count is not None:
            _dict['user_evaluation_required_count'] = self.user_evaluation_required_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlSpecificationWithStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlSpecificationWithStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlSpecificationWithStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class ControlSpecifications:
    """
    The control specifications of a control library.

    :attr str control_specification_id: (optional) The control specification ID.
    :attr str responsibility: (optional) The responsibility for managing the
          control.
    :attr str component_id: (optional) The component ID.
    :attr str component_name: (optional) The component name.
    :attr str environment: (optional) The control specifications environment.
    :attr str control_specification_description: (optional) The control
          specifications description.
    :attr int assessments_count: (optional) The number of assessments.
    :attr List[Implementation] assessments: (optional) The assessments.
    """

    def __init__(
        self,
        *,
        control_specification_id: str = None,
        responsibility: str = None,
        component_id: str = None,
        component_name: str = None,
        environment: str = None,
        control_specification_description: str = None,
        assessments_count: int = None,
        assessments: List['Implementation'] = None,
    ) -> None:
        """
        Initialize a ControlSpecifications object.

        :param str control_specification_id: (optional) The control specification
               ID.
        :param str responsibility: (optional) The responsibility for managing the
               control.
        :param str component_id: (optional) The component ID.
        :param str component_name: (optional) The component name.
        :param str environment: (optional) The control specifications environment.
        :param str control_specification_description: (optional) The control
               specifications description.
        :param int assessments_count: (optional) The number of assessments.
        :param List[Implementation] assessments: (optional) The assessments.
        """
        self.control_specification_id = control_specification_id
        self.responsibility = responsibility
        self.component_id = component_id
        self.component_name = component_name
        self.environment = environment
        self.control_specification_description = control_specification_description
        self.assessments_count = assessments_count
        self.assessments = assessments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSpecifications':
        """Initialize a ControlSpecifications object from a json dictionary."""
        args = {}
        if 'control_specification_id' in _dict:
            args['control_specification_id'] = _dict.get('control_specification_id')
        if 'responsibility' in _dict:
            args['responsibility'] = _dict.get('responsibility')
        if 'component_id' in _dict:
            args['component_id'] = _dict.get('component_id')
        if 'component_name' in _dict:
            args['component_name'] = _dict.get('component_name')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'control_specification_description' in _dict:
            args['control_specification_description'] = _dict.get('control_specification_description')
        if 'assessments_count' in _dict:
            args['assessments_count'] = _dict.get('assessments_count')
        if 'assessments' in _dict:
            args['assessments'] = [Implementation.from_dict(v) for v in _dict.get('assessments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlSpecifications object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_specification_id') and self.control_specification_id is not None:
            _dict['control_specification_id'] = self.control_specification_id
        if hasattr(self, 'responsibility') and self.responsibility is not None:
            _dict['responsibility'] = self.responsibility
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'control_specification_description') and self.control_specification_description is not None:
            _dict['control_specification_description'] = self.control_specification_description
        if hasattr(self, 'assessments_count') and self.assessments_count is not None:
            _dict['assessments_count'] = self.assessments_count
        if hasattr(self, 'assessments') and self.assessments is not None:
            assessments_list = []
            for v in self.assessments:
                if isinstance(v, dict):
                    assessments_list.append(v)
                else:
                    assessments_list.append(v.to_dict())
            _dict['assessments'] = assessments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlSpecifications object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlSpecifications') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlSpecifications') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResponsibilityEnum(str, Enum):
        """
        The responsibility for managing the control.
        """

        USER = 'user'



class ControlWithStats:
    """
    The control with compliance stats.

    :attr str id: (optional) The control ID.
    :attr str control_library_id: (optional) The control library ID.
    :attr str control_library_version: (optional) The control library version.
    :attr str control_name: (optional) The control name.
    :attr str control_description: (optional) The control description.
    :attr str control_category: (optional) The control category.
    :attr str control_path: (optional) The control path.
    :attr List[ControlSpecificationWithStats] control_specifications: (optional) The
          list of specifications that are on the page.
    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of checks.
    :attr int compliant_count: (optional) The number of compliant checks.
    :attr int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :attr int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :attr int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    """

    def __init__(
        self,
        *,
        id: str = None,
        control_library_id: str = None,
        control_library_version: str = None,
        control_name: str = None,
        control_description: str = None,
        control_category: str = None,
        control_path: str = None,
        control_specifications: List['ControlSpecificationWithStats'] = None,
        status: str = None,
        total_count: int = None,
        compliant_count: int = None,
        not_compliant_count: int = None,
        unable_to_perform_count: int = None,
        user_evaluation_required_count: int = None,
    ) -> None:
        """
        Initialize a ControlWithStats object.

        :param str id: (optional) The control ID.
        :param str control_library_id: (optional) The control library ID.
        :param str control_library_version: (optional) The control library version.
        :param str control_name: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_category: (optional) The control category.
        :param str control_path: (optional) The control path.
        :param List[ControlSpecificationWithStats] control_specifications:
               (optional) The list of specifications that are on the page.
        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        """
        self.id = id
        self.control_library_id = control_library_id
        self.control_library_version = control_library_version
        self.control_name = control_name
        self.control_description = control_description
        self.control_category = control_category
        self.control_path = control_path
        self.control_specifications = control_specifications
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlWithStats':
        """Initialize a ControlWithStats object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'control_library_id' in _dict:
            args['control_library_id'] = _dict.get('control_library_id')
        if 'control_library_version' in _dict:
            args['control_library_version'] = _dict.get('control_library_version')
        if 'control_name' in _dict:
            args['control_name'] = _dict.get('control_name')
        if 'control_description' in _dict:
            args['control_description'] = _dict.get('control_description')
        if 'control_category' in _dict:
            args['control_category'] = _dict.get('control_category')
        if 'control_path' in _dict:
            args['control_path'] = _dict.get('control_path')
        if 'control_specifications' in _dict:
            args['control_specifications'] = [ControlSpecificationWithStats.from_dict(v) for v in _dict.get('control_specifications')]
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'compliant_count' in _dict:
            args['compliant_count'] = _dict.get('compliant_count')
        if 'not_compliant_count' in _dict:
            args['not_compliant_count'] = _dict.get('not_compliant_count')
        if 'unable_to_perform_count' in _dict:
            args['unable_to_perform_count'] = _dict.get('unable_to_perform_count')
        if 'user_evaluation_required_count' in _dict:
            args['user_evaluation_required_count'] = _dict.get('user_evaluation_required_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlWithStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'control_library_id') and self.control_library_id is not None:
            _dict['control_library_id'] = self.control_library_id
        if hasattr(self, 'control_library_version') and self.control_library_version is not None:
            _dict['control_library_version'] = self.control_library_version
        if hasattr(self, 'control_name') and self.control_name is not None:
            _dict['control_name'] = self.control_name
        if hasattr(self, 'control_description') and self.control_description is not None:
            _dict['control_description'] = self.control_description
        if hasattr(self, 'control_category') and self.control_category is not None:
            _dict['control_category'] = self.control_category
        if hasattr(self, 'control_path') and self.control_path is not None:
            _dict['control_path'] = self.control_path
        if hasattr(self, 'control_specifications') and self.control_specifications is not None:
            control_specifications_list = []
            for v in self.control_specifications:
                if isinstance(v, dict):
                    control_specifications_list.append(v)
                else:
                    control_specifications_list.append(v.to_dict())
            _dict['control_specifications'] = control_specifications_list
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'compliant_count') and self.compliant_count is not None:
            _dict['compliant_count'] = self.compliant_count
        if hasattr(self, 'not_compliant_count') and self.not_compliant_count is not None:
            _dict['not_compliant_count'] = self.not_compliant_count
        if hasattr(self, 'unable_to_perform_count') and self.unable_to_perform_count is not None:
            _dict['unable_to_perform_count'] = self.unable_to_perform_count
        if hasattr(self, 'user_evaluation_required_count') and self.user_evaluation_required_count is not None:
            _dict['user_evaluation_required_count'] = self.user_evaluation_required_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlWithStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlWithStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlWithStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class ControlsInControlLib:
    """
    The control details of a control library.

    :attr str control_name: (optional) The ID of the control library that contains
          the profile.
    :attr str control_id: (optional) The control name.
    :attr str control_description: (optional) The control description.
    :attr str control_category: (optional) The control category.
    :attr str control_parent: (optional) The parent control.
    :attr List[str] control_tags: (optional) The control tags.
    :attr List[ControlSpecifications] control_specifications: (optional) The control
          specifications.
    :attr ControlDocs control_docs: (optional) The control documentation.
    :attr bool control_requirement: (optional) Is this a control that can be
          automated or manually evaluated.
    :attr str status: (optional) The control status.
    """

    def __init__(
        self,
        *,
        control_name: str = None,
        control_id: str = None,
        control_description: str = None,
        control_category: str = None,
        control_parent: str = None,
        control_tags: List[str] = None,
        control_specifications: List['ControlSpecifications'] = None,
        control_docs: 'ControlDocs' = None,
        control_requirement: bool = None,
        status: str = None,
    ) -> None:
        """
        Initialize a ControlsInControlLib object.

        :param str control_name: (optional) The ID of the control library that
               contains the profile.
        :param str control_id: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_category: (optional) The control category.
        :param str control_parent: (optional) The parent control.
        :param List[str] control_tags: (optional) The control tags.
        :param List[ControlSpecifications] control_specifications: (optional) The
               control specifications.
        :param ControlDocs control_docs: (optional) The control documentation.
        :param bool control_requirement: (optional) Is this a control that can be
               automated or manually evaluated.
        :param str status: (optional) The control status.
        """
        self.control_name = control_name
        self.control_id = control_id
        self.control_description = control_description
        self.control_category = control_category
        self.control_parent = control_parent
        self.control_tags = control_tags
        self.control_specifications = control_specifications
        self.control_docs = control_docs
        self.control_requirement = control_requirement
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlsInControlLib':
        """Initialize a ControlsInControlLib object from a json dictionary."""
        args = {}
        if 'control_name' in _dict:
            args['control_name'] = _dict.get('control_name')
        if 'control_id' in _dict:
            args['control_id'] = _dict.get('control_id')
        if 'control_description' in _dict:
            args['control_description'] = _dict.get('control_description')
        if 'control_category' in _dict:
            args['control_category'] = _dict.get('control_category')
        if 'control_parent' in _dict:
            args['control_parent'] = _dict.get('control_parent')
        if 'control_tags' in _dict:
            args['control_tags'] = _dict.get('control_tags')
        if 'control_specifications' in _dict:
            args['control_specifications'] = [ControlSpecifications.from_dict(v) for v in _dict.get('control_specifications')]
        if 'control_docs' in _dict:
            args['control_docs'] = ControlDocs.from_dict(_dict.get('control_docs'))
        if 'control_requirement' in _dict:
            args['control_requirement'] = _dict.get('control_requirement')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlsInControlLib object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_name') and self.control_name is not None:
            _dict['control_name'] = self.control_name
        if hasattr(self, 'control_id') and self.control_id is not None:
            _dict['control_id'] = self.control_id
        if hasattr(self, 'control_description') and self.control_description is not None:
            _dict['control_description'] = self.control_description
        if hasattr(self, 'control_category') and self.control_category is not None:
            _dict['control_category'] = self.control_category
        if hasattr(self, 'control_parent') and self.control_parent is not None:
            _dict['control_parent'] = self.control_parent
        if hasattr(self, 'control_tags') and self.control_tags is not None:
            _dict['control_tags'] = self.control_tags
        if hasattr(self, 'control_specifications') and self.control_specifications is not None:
            control_specifications_list = []
            for v in self.control_specifications:
                if isinstance(v, dict):
                    control_specifications_list.append(v)
                else:
                    control_specifications_list.append(v.to_dict())
            _dict['control_specifications'] = control_specifications_list
        if hasattr(self, 'control_docs') and self.control_docs is not None:
            if isinstance(self.control_docs, dict):
                _dict['control_docs'] = self.control_docs
            else:
                _dict['control_docs'] = self.control_docs.to_dict()
        if hasattr(self, 'control_requirement') and self.control_requirement is not None:
            _dict['control_requirement'] = self.control_requirement
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlsInControlLib object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlsInControlLib') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlsInControlLib') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The control status.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'



class DefaultParametersPrototype:
    """
    The control details of a profile.

    :attr str assessment_type: (optional) The type of the implementation.
    :attr str assessment_id: (optional) The implementation ID of the parameter.
    :attr str parameter_name: (optional) The parameter name.
    :attr str parameter_default_value: (optional) The default value of the
          parameter.
    :attr str parameter_display_name: (optional) The parameter display name.
    :attr str parameter_type: (optional) The parameter type.
    """

    def __init__(
        self,
        *,
        assessment_type: str = None,
        assessment_id: str = None,
        parameter_name: str = None,
        parameter_default_value: str = None,
        parameter_display_name: str = None,
        parameter_type: str = None,
    ) -> None:
        """
        Initialize a DefaultParametersPrototype object.

        :param str assessment_type: (optional) The type of the implementation.
        :param str assessment_id: (optional) The implementation ID of the
               parameter.
        :param str parameter_name: (optional) The parameter name.
        :param str parameter_default_value: (optional) The default value of the
               parameter.
        :param str parameter_display_name: (optional) The parameter display name.
        :param str parameter_type: (optional) The parameter type.
        """
        self.assessment_type = assessment_type
        self.assessment_id = assessment_id
        self.parameter_name = parameter_name
        self.parameter_default_value = parameter_default_value
        self.parameter_display_name = parameter_display_name
        self.parameter_type = parameter_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultParametersPrototype':
        """Initialize a DefaultParametersPrototype object from a json dictionary."""
        args = {}
        if 'assessment_type' in _dict:
            args['assessment_type'] = _dict.get('assessment_type')
        if 'assessment_id' in _dict:
            args['assessment_id'] = _dict.get('assessment_id')
        if 'parameter_name' in _dict:
            args['parameter_name'] = _dict.get('parameter_name')
        if 'parameter_default_value' in _dict:
            args['parameter_default_value'] = _dict.get('parameter_default_value')
        if 'parameter_display_name' in _dict:
            args['parameter_display_name'] = _dict.get('parameter_display_name')
        if 'parameter_type' in _dict:
            args['parameter_type'] = _dict.get('parameter_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultParametersPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assessment_type') and self.assessment_type is not None:
            _dict['assessment_type'] = self.assessment_type
        if hasattr(self, 'assessment_id') and self.assessment_id is not None:
            _dict['assessment_id'] = self.assessment_id
        if hasattr(self, 'parameter_name') and self.parameter_name is not None:
            _dict['parameter_name'] = self.parameter_name
        if hasattr(self, 'parameter_default_value') and self.parameter_default_value is not None:
            _dict['parameter_default_value'] = self.parameter_default_value
        if hasattr(self, 'parameter_display_name') and self.parameter_display_name is not None:
            _dict['parameter_display_name'] = self.parameter_display_name
        if hasattr(self, 'parameter_type') and self.parameter_type is not None:
            _dict['parameter_type'] = self.parameter_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultParametersPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultParametersPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultParametersPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ParameterTypeEnum(str, Enum):
        """
        The parameter type.
        """

        STRING = 'string'
        NUMERIC = 'numeric'
        GENERAL = 'general'
        BOOLEAN = 'boolean'
        STRING_LIST = 'string_list'
        IP_LIST = 'ip_list'
        TIMESTAMP = 'timestamp'



class EvalDetails:
    """
    The evaluation details.

    :attr List[Property] properties: (optional) The evaluation properties.
    """

    def __init__(
        self,
        *,
        properties: List['Property'] = None,
    ) -> None:
        """
        Initialize a EvalDetails object.

        :param List[Property] properties: (optional) The evaluation properties.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvalDetails':
        """Initialize a EvalDetails object from a json dictionary."""
        args = {}
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(v) for v in _dict.get('properties')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvalDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EvalDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EvalDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EvalDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EvalStats:
    """
    The evaluation stats.

    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of evaluations.
    :attr int pass_count: (optional) The number of passed evaluations.
    :attr int failure_count: (optional) The number of failed evaluations.
    :attr int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :attr int completed_count: (optional) The total number of completed evaluations.
    """

    def __init__(
        self,
        *,
        status: str = None,
        total_count: int = None,
        pass_count: int = None,
        failure_count: int = None,
        error_count: int = None,
        completed_count: int = None,
    ) -> None:
        """
        Initialize a EvalStats object.

        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        """
        self.status = status
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.completed_count = completed_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvalStats':
        """Initialize a EvalStats object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'pass_count' in _dict:
            args['pass_count'] = _dict.get('pass_count')
        if 'failure_count' in _dict:
            args['failure_count'] = _dict.get('failure_count')
        if 'error_count' in _dict:
            args['error_count'] = _dict.get('error_count')
        if 'completed_count' in _dict:
            args['completed_count'] = _dict.get('completed_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvalStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'pass_count') and self.pass_count is not None:
            _dict['pass_count'] = self.pass_count
        if hasattr(self, 'failure_count') and self.failure_count is not None:
            _dict['failure_count'] = self.failure_count
        if hasattr(self, 'error_count') and self.error_count is not None:
            _dict['error_count'] = self.error_count
        if hasattr(self, 'completed_count') and self.completed_count is not None:
            _dict['completed_count'] = self.completed_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EvalStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EvalStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EvalStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class Evaluation:
    """
    The evaluation of a control specification assessment.

    :attr str home_account_id: (optional) The ID of the home account.
    :attr str report_id: (optional) The ID of the report that is associated to the
          evaluation.
    :attr str control_id: (optional) The control ID.
    :attr str component_id: (optional) The component ID.
    :attr Assessment assessment: (optional) The control specification assessment.
    :attr str evaluate_time: (optional) The time when the evaluation was made.
    :attr TargetInfo target: (optional) The evaluation target.
    :attr str status: (optional) The allowed values of an evaluation status.
    :attr str reason: (optional) The reason for the evaluation failure.
    :attr EvalDetails details: (optional) The evaluation details.
    """

    def __init__(
        self,
        *,
        home_account_id: str = None,
        report_id: str = None,
        control_id: str = None,
        component_id: str = None,
        assessment: 'Assessment' = None,
        evaluate_time: str = None,
        target: 'TargetInfo' = None,
        status: str = None,
        reason: str = None,
        details: 'EvalDetails' = None,
    ) -> None:
        """
        Initialize a Evaluation object.

        :param str home_account_id: (optional) The ID of the home account.
        :param str report_id: (optional) The ID of the report that is associated to
               the evaluation.
        :param str control_id: (optional) The control ID.
        :param str component_id: (optional) The component ID.
        :param Assessment assessment: (optional) The control specification
               assessment.
        :param str evaluate_time: (optional) The time when the evaluation was made.
        :param TargetInfo target: (optional) The evaluation target.
        :param str status: (optional) The allowed values of an evaluation status.
        :param str reason: (optional) The reason for the evaluation failure.
        :param EvalDetails details: (optional) The evaluation details.
        """
        self.home_account_id = home_account_id
        self.report_id = report_id
        self.control_id = control_id
        self.component_id = component_id
        self.assessment = assessment
        self.evaluate_time = evaluate_time
        self.target = target
        self.status = status
        self.reason = reason
        self.details = details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Evaluation':
        """Initialize a Evaluation object from a json dictionary."""
        args = {}
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'control_id' in _dict:
            args['control_id'] = _dict.get('control_id')
        if 'component_id' in _dict:
            args['component_id'] = _dict.get('component_id')
        if 'assessment' in _dict:
            args['assessment'] = Assessment.from_dict(_dict.get('assessment'))
        if 'evaluate_time' in _dict:
            args['evaluate_time'] = _dict.get('evaluate_time')
        if 'target' in _dict:
            args['target'] = TargetInfo.from_dict(_dict.get('target'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        if 'details' in _dict:
            args['details'] = EvalDetails.from_dict(_dict.get('details'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Evaluation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'control_id') and self.control_id is not None:
            _dict['control_id'] = self.control_id
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'assessment') and self.assessment is not None:
            if isinstance(self.assessment, dict):
                _dict['assessment'] = self.assessment
            else:
                _dict['assessment'] = self.assessment.to_dict()
        if hasattr(self, 'evaluate_time') and self.evaluate_time is not None:
            _dict['evaluate_time'] = self.evaluate_time
        if hasattr(self, 'target') and self.target is not None:
            if isinstance(self.target, dict):
                _dict['target'] = self.target
            else:
                _dict['target'] = self.target.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        if hasattr(self, 'details') and self.details is not None:
            if isinstance(self.details, dict):
                _dict['details'] = self.details
            else:
                _dict['details'] = self.details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Evaluation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Evaluation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Evaluation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an evaluation status.
        """

        PASS = 'pass'
        FAILURE = 'failure'
        ERROR = 'error'
        SKIPPED = 'skipped'



class EvaluationPage:
    """
    The page of assessment evaluations.

    :attr int total_count: The total number of resources that are in the collection.
    :attr int limit: The requested page limi.t.
    :attr str start: (optional) The token of the next page, when it's present.
    :attr PageHRef first: The page reference.
    :attr PageHRef next: (optional) The page reference.
    :attr str home_account_id: (optional) The ID of the home account.
    :attr str report_id: (optional) The ID of the report.
    :attr List[Evaluation] evaluations: (optional) The list of evaluations that are
          on the page.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'PageHRef',
        *,
        start: str = None,
        next: 'PageHRef' = None,
        home_account_id: str = None,
        report_id: str = None,
        evaluations: List['Evaluation'] = None,
    ) -> None:
        """
        Initialize a EvaluationPage object.

        :param int total_count: The total number of resources that are in the
               collection.
        :param int limit: The requested page limi.t.
        :param PageHRef first: The page reference.
        :param str start: (optional) The token of the next page, when it's present.
        :param PageHRef next: (optional) The page reference.
        :param str home_account_id: (optional) The ID of the home account.
        :param str report_id: (optional) The ID of the report.
        :param List[Evaluation] evaluations: (optional) The list of evaluations
               that are on the page.
        """
        self.total_count = total_count
        self.limit = limit
        self.start = start
        self.first = first
        self.next = next
        self.home_account_id = home_account_id
        self.report_id = report_id
        self.evaluations = evaluations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvaluationPage':
        """Initialize a EvaluationPage object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in EvaluationPage JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in EvaluationPage JSON')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'first' in _dict:
            args['first'] = PageHRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in EvaluationPage JSON')
        if 'next' in _dict:
            args['next'] = PageHRef.from_dict(_dict.get('next'))
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'evaluations' in _dict:
            args['evaluations'] = [Evaluation.from_dict(v) for v in _dict.get('evaluations')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvaluationPage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'evaluations') and self.evaluations is not None:
            evaluations_list = []
            for v in self.evaluations:
                if isinstance(v, dict):
                    evaluations_list.append(v)
                else:
                    evaluations_list.append(v.to_dict())
            _dict['evaluations'] = evaluations_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EvaluationPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EvaluationPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EvaluationPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EventNotifications:
    """
    The Event Notifications settings.

    :attr str instance_crn: (optional) The Event Notifications instance CRN.
    :attr datetime updated_on: (optional) The date when the Event Notifications
          connection was updated.
    :attr str source_id: (optional) The connected Security and Compliance Center
          instance CRN.
    :attr str source_description: (optional) The description of the source of the
          Event Notifications.
    :attr str source_name: (optional) The name of the source of the Event
          Notifications.
    """

    def __init__(
        self,
        *,
        instance_crn: str = None,
        updated_on: datetime = None,
        source_id: str = None,
        source_description: str = None,
        source_name: str = None,
    ) -> None:
        """
        Initialize a EventNotifications object.

        :param str instance_crn: (optional) The Event Notifications instance CRN.
        :param datetime updated_on: (optional) The date when the Event
               Notifications connection was updated.
        :param str source_id: (optional) The connected Security and Compliance
               Center instance CRN.
        :param str source_description: (optional) The description of the source of
               the Event Notifications.
        :param str source_name: (optional) The name of the source of the Event
               Notifications.
        """
        self.instance_crn = instance_crn
        self.updated_on = updated_on
        self.source_id = source_id
        self.source_description = source_description
        self.source_name = source_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EventNotifications':
        """Initialize a EventNotifications object from a json dictionary."""
        args = {}
        if 'instance_crn' in _dict:
            args['instance_crn'] = _dict.get('instance_crn')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        if 'source_id' in _dict:
            args['source_id'] = _dict.get('source_id')
        if 'source_description' in _dict:
            args['source_description'] = _dict.get('source_description')
        if 'source_name' in _dict:
            args['source_name'] = _dict.get('source_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EventNotifications object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'source_id') and self.source_id is not None:
            _dict['source_id'] = self.source_id
        if hasattr(self, 'source_description') and self.source_description is not None:
            _dict['source_description'] = self.source_description
        if hasattr(self, 'source_name') and self.source_name is not None:
            _dict['source_name'] = self.source_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EventNotifications object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EventNotifications') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EventNotifications') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FailedControls:
    """
    The failed controls.

    :attr int threshold_limit: (optional) The threshold limit.
    :attr List[str] failed_control_ids: (optional) The failed control IDs.
    """

    def __init__(
        self,
        *,
        threshold_limit: int = None,
        failed_control_ids: List[str] = None,
    ) -> None:
        """
        Initialize a FailedControls object.

        :param int threshold_limit: (optional) The threshold limit.
        :param List[str] failed_control_ids: (optional) The failed control IDs.
        """
        self.threshold_limit = threshold_limit
        self.failed_control_ids = failed_control_ids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FailedControls':
        """Initialize a FailedControls object from a json dictionary."""
        args = {}
        if 'threshold_limit' in _dict:
            args['threshold_limit'] = _dict.get('threshold_limit')
        if 'failed_control_ids' in _dict:
            args['failed_control_ids'] = _dict.get('failed_control_ids')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FailedControls object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'threshold_limit') and self.threshold_limit is not None:
            _dict['threshold_limit'] = self.threshold_limit
        if hasattr(self, 'failed_control_ids') and self.failed_control_ids is not None:
            _dict['failed_control_ids'] = self.failed_control_ids
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FailedControls object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FailedControls') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FailedControls') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Implementation:
    """
    The implementation details of a control library.

    :attr str assessment_id: (optional) The assessment ID.
    :attr str assessment_method: (optional) The assessment method.
    :attr str assessment_type: (optional) The assessment type.
    :attr str assessment_description: (optional) The assessment description.
    :attr int parameter_count: (optional) The parameter count.
    :attr List[ParameterInfo] parameters: (optional) The parameters.
    """

    def __init__(
        self,
        *,
        assessment_id: str = None,
        assessment_method: str = None,
        assessment_type: str = None,
        assessment_description: str = None,
        parameter_count: int = None,
        parameters: List['ParameterInfo'] = None,
    ) -> None:
        """
        Initialize a Implementation object.

        :param str assessment_id: (optional) The assessment ID.
        :param str assessment_method: (optional) The assessment method.
        :param str assessment_type: (optional) The assessment type.
        :param str assessment_description: (optional) The assessment description.
        :param int parameter_count: (optional) The parameter count.
        :param List[ParameterInfo] parameters: (optional) The parameters.
        """
        self.assessment_id = assessment_id
        self.assessment_method = assessment_method
        self.assessment_type = assessment_type
        self.assessment_description = assessment_description
        self.parameter_count = parameter_count
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Implementation':
        """Initialize a Implementation object from a json dictionary."""
        args = {}
        if 'assessment_id' in _dict:
            args['assessment_id'] = _dict.get('assessment_id')
        if 'assessment_method' in _dict:
            args['assessment_method'] = _dict.get('assessment_method')
        if 'assessment_type' in _dict:
            args['assessment_type'] = _dict.get('assessment_type')
        if 'assessment_description' in _dict:
            args['assessment_description'] = _dict.get('assessment_description')
        if 'parameter_count' in _dict:
            args['parameter_count'] = _dict.get('parameter_count')
        if 'parameters' in _dict:
            args['parameters'] = [ParameterInfo.from_dict(v) for v in _dict.get('parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Implementation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assessment_id') and self.assessment_id is not None:
            _dict['assessment_id'] = self.assessment_id
        if hasattr(self, 'assessment_method') and self.assessment_method is not None:
            _dict['assessment_method'] = self.assessment_method
        if hasattr(self, 'assessment_type') and self.assessment_type is not None:
            _dict['assessment_type'] = self.assessment_type
        if hasattr(self, 'assessment_description') and self.assessment_description is not None:
            _dict['assessment_description'] = self.assessment_description
        if hasattr(self, 'parameter_count') and self.parameter_count is not None:
            _dict['parameter_count'] = self.parameter_count
        if hasattr(self, 'parameters') and self.parameters is not None:
            parameters_list = []
            for v in self.parameters:
                if isinstance(v, dict):
                    parameters_list.append(v)
                else:
                    parameters_list.append(v.to_dict())
            _dict['parameters'] = parameters_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Implementation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Implementation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Implementation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Import:
    """
    The collection of import parameters.

    :attr List[Parameter] parameters: (optional) The list of import parameters.
    """

    def __init__(
        self,
        *,
        parameters: List['Parameter'] = None,
    ) -> None:
        """
        Initialize a Import object.

        :param List[Parameter] parameters: (optional) The list of import
               parameters.
        """
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Import':
        """Initialize a Import object from a json dictionary."""
        args = {}
        if 'parameters' in _dict:
            args['parameters'] = [Parameter.from_dict(v) for v in _dict.get('parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Import object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'parameters') and self.parameters is not None:
            parameters_list = []
            for v in self.parameters:
                if isinstance(v, dict):
                    parameters_list.append(v)
                else:
                    parameters_list.append(v.to_dict())
            _dict['parameters'] = parameters_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Import object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Import') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Import') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LabelType:
    """
    The label that is associated with the provider type.

    :attr str text: (optional) The text of the label.
    :attr str tip: (optional) The text to be shown when user hover overs the label.
    """

    def __init__(
        self,
        *,
        text: str = None,
        tip: str = None,
    ) -> None:
        """
        Initialize a LabelType object.

        :param str text: (optional) The text of the label.
        :param str tip: (optional) The text to be shown when user hover overs the
               label.
        """
        self.text = text
        self.tip = tip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LabelType':
        """Initialize a LabelType object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'tip' in _dict:
            args['tip'] = _dict.get('tip')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LabelType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'tip') and self.tip is not None:
            _dict['tip'] = self.tip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LabelType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LabelType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LabelType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LastScan:
    """
    The details of the last scan of an attachment.

    :attr str id: (optional) The ID of the last scan of an attachment.
    :attr str status: (optional) The status of the last scan of an attachment.
    :attr datetime time: (optional) The time when the last scan started.
    """

    def __init__(
        self,
        *,
        id: str = None,
        status: str = None,
        time: datetime = None,
    ) -> None:
        """
        Initialize a LastScan object.

        :param str id: (optional) The ID of the last scan of an attachment.
        :param str status: (optional) The status of the last scan of an attachment.
        :param datetime time: (optional) The time when the last scan started.
        """
        self.id = id
        self.status = status
        self.time = time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LastScan':
        """Initialize a LastScan object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'time' in _dict:
            args['time'] = string_to_datetime(_dict.get('time'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LastScan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'time') and self.time is not None:
            _dict['time'] = datetime_to_string(self.time)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LastScan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LastScan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LastScan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the last scan of an attachment.
        """

        IN_PROGRESS = 'in_progress'
        COMPLETED = 'completed'



class MultiCloudScope:
    """
    The scope payload for the multi cloud feature.

    :attr str environment: The environment that relates to this scope.
    :attr List[PropertyItem] properties: The properties supported for scoping by
          this environment.
    """

    def __init__(
        self,
        environment: str,
        properties: List['PropertyItem'],
    ) -> None:
        """
        Initialize a MultiCloudScope object.

        :param str environment: The environment that relates to this scope.
        :param List[PropertyItem] properties: The properties supported for scoping
               by this environment.
        """
        self.environment = environment
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MultiCloudScope':
        """Initialize a MultiCloudScope object from a json dictionary."""
        args = {}
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        else:
            raise ValueError('Required property \'environment\' not present in MultiCloudScope JSON')
        if 'properties' in _dict:
            args['properties'] = [PropertyItem.from_dict(v) for v in _dict.get('properties')]
        else:
            raise ValueError('Required property \'properties\' not present in MultiCloudScope JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MultiCloudScope object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MultiCloudScope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MultiCloudScope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MultiCloudScope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectStorage:
    """
    The Cloud Object Storage settings.

    :attr str instance_crn: (optional) The connected Cloud Object Storage instance
          CRN.
    :attr str bucket: (optional) The connected Cloud Object Storage bucket name.
    :attr str bucket_location: (optional) The connected Cloud Object Storage bucket
          location.
    :attr str bucket_endpoint: (optional) The connected Cloud Object Storage bucket
          endpoint.
    :attr datetime updated_on: (optional) The date when the bucket connection was
          updated.
    """

    def __init__(
        self,
        *,
        instance_crn: str = None,
        bucket: str = None,
        bucket_location: str = None,
        bucket_endpoint: str = None,
        updated_on: datetime = None,
    ) -> None:
        """
        Initialize a ObjectStorage object.

        :param str instance_crn: (optional) The connected Cloud Object Storage
               instance CRN.
        :param str bucket: (optional) The connected Cloud Object Storage bucket
               name.
        :param str bucket_location: (optional) The connected Cloud Object Storage
               bucket location.
        :param str bucket_endpoint: (optional) The connected Cloud Object Storage
               bucket endpoint.
        :param datetime updated_on: (optional) The date when the bucket connection
               was updated.
        """
        self.instance_crn = instance_crn
        self.bucket = bucket
        self.bucket_location = bucket_location
        self.bucket_endpoint = bucket_endpoint
        self.updated_on = updated_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectStorage':
        """Initialize a ObjectStorage object from a json dictionary."""
        args = {}
        if 'instance_crn' in _dict:
            args['instance_crn'] = _dict.get('instance_crn')
        if 'bucket' in _dict:
            args['bucket'] = _dict.get('bucket')
        if 'bucket_location' in _dict:
            args['bucket_location'] = _dict.get('bucket_location')
        if 'bucket_endpoint' in _dict:
            args['bucket_endpoint'] = _dict.get('bucket_endpoint')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectStorage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
        if hasattr(self, 'bucket') and self.bucket is not None:
            _dict['bucket'] = self.bucket
        if hasattr(self, 'bucket_location') and self.bucket_location is not None:
            _dict['bucket_location'] = self.bucket_location
        if hasattr(self, 'bucket_endpoint') and self.bucket_endpoint is not None:
            _dict['bucket_endpoint'] = self.bucket_endpoint
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectStorage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectStorage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectStorage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PageHRef:
    """
    The page reference.

    :attr str href: The URL for the first and next page.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a PageHRef object.

        :param str href: The URL for the first and next page.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageHRef':
        """Initialize a PageHRef object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PageHRef JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageHRef object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageHRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageHRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageHRef') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PageHRefFirst:
    """
    A page reference.

    :attr str href: A URL for the first and next page.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a PageHRefFirst object.

        :param str href: A URL for the first and next page.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageHRefFirst':
        """Initialize a PageHRefFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PageHRefFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageHRefFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageHRefFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageHRefFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageHRefFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PageHRefNext:
    """
    A page reference.

    :attr str href: A URL for the first and next page.
    :attr str start: (optional) The token of the next page when present.
    """

    def __init__(
        self,
        href: str,
        *,
        start: str = None,
    ) -> None:
        """
        Initialize a PageHRefNext object.

        :param str href: A URL for the first and next page.
        :param str start: (optional) The token of the next page when present.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageHRefNext':
        """Initialize a PageHRefNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PageHRefNext JSON')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageHRefNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PageHRefNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageHRefNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageHRefNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PaginatedCollectionFirst:
    """
    The reference to the first page of entries.

    :attr str href: (optional) The reference URL for the first few entries.
    """

    def __init__(
        self,
        *,
        href: str = None,
    ) -> None:
        """
        Initialize a PaginatedCollectionFirst object.

        :param str href: (optional) The reference URL for the first few entries.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginatedCollectionFirst':
        """Initialize a PaginatedCollectionFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaginatedCollectionFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PaginatedCollectionFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PaginatedCollectionFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaginatedCollectionFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PaginatedCollectionNext:
    """
    The reference URL for the next few entries.

    :attr str href: (optional) The reference URL for the entries.
    :attr str start: (optional) The reference to the start of the list of entries.
    """

    def __init__(
        self,
        *,
        href: str = None,
        start: str = None,
    ) -> None:
        """
        Initialize a PaginatedCollectionNext object.

        :param str href: (optional) The reference URL for the entries.
        :param str start: (optional) The reference to the start of the list of
               entries.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginatedCollectionNext':
        """Initialize a PaginatedCollectionNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaginatedCollectionNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PaginatedCollectionNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PaginatedCollectionNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaginatedCollectionNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Parameter:
    """
    The rule import parameter.

    :attr str name: (optional) The import parameter name.
    :attr str display_name: (optional) The display name of the property.
    :attr str description: (optional) The propery description.
    :attr str type: (optional) The property type.
    """

    def __init__(
        self,
        *,
        name: str = None,
        display_name: str = None,
        description: str = None,
        type: str = None,
    ) -> None:
        """
        Initialize a Parameter object.

        :param str name: (optional) The import parameter name.
        :param str display_name: (optional) The display name of the property.
        :param str description: (optional) The propery description.
        :param str type: (optional) The property type.
        """
        self.name = name
        self.display_name = display_name
        self.description = description
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Parameter':
        """Initialize a Parameter object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'display_name' in _dict:
            args['display_name'] = _dict.get('display_name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Parameter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'display_name') and self.display_name is not None:
            _dict['display_name'] = self.display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Parameter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Parameter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Parameter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The property type.
        """

        STRING = 'string'
        NUMERIC = 'numeric'
        GENERAL = 'general'
        BOOLEAN = 'boolean'
        STRING_LIST = 'string_list'
        IP_LIST = 'ip_list'
        TIMESTAMP = 'timestamp'



class ParameterInfo:
    """
    The parameter details.

    :attr str parameter_name: (optional) The parameter name.
    :attr str parameter_display_name: (optional) The parameter display name.
    :attr str parameter_type: (optional) The parameter type.
    :attr object parameter_value: (optional) The property value.
    """

    def __init__(
        self,
        *,
        parameter_name: str = None,
        parameter_display_name: str = None,
        parameter_type: str = None,
        parameter_value: object = None,
    ) -> None:
        """
        Initialize a ParameterInfo object.

        :param str parameter_name: (optional) The parameter name.
        :param str parameter_display_name: (optional) The parameter display name.
        :param str parameter_type: (optional) The parameter type.
        :param object parameter_value: (optional) The property value.
        """
        self.parameter_name = parameter_name
        self.parameter_display_name = parameter_display_name
        self.parameter_type = parameter_type
        self.parameter_value = parameter_value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ParameterInfo':
        """Initialize a ParameterInfo object from a json dictionary."""
        args = {}
        if 'parameter_name' in _dict:
            args['parameter_name'] = _dict.get('parameter_name')
        if 'parameter_display_name' in _dict:
            args['parameter_display_name'] = _dict.get('parameter_display_name')
        if 'parameter_type' in _dict:
            args['parameter_type'] = _dict.get('parameter_type')
        if 'parameter_value' in _dict:
            args['parameter_value'] = _dict.get('parameter_value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ParameterInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'parameter_name') and self.parameter_name is not None:
            _dict['parameter_name'] = self.parameter_name
        if hasattr(self, 'parameter_display_name') and self.parameter_display_name is not None:
            _dict['parameter_display_name'] = self.parameter_display_name
        if hasattr(self, 'parameter_type') and self.parameter_type is not None:
            _dict['parameter_type'] = self.parameter_type
        if hasattr(self, 'parameter_value') and self.parameter_value is not None:
            _dict['parameter_value'] = self.parameter_value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ParameterInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ParameterInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ParameterInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ParameterTypeEnum(str, Enum):
        """
        The parameter type.
        """

        STRING = 'string'
        NUMERIC = 'numeric'
        GENERAL = 'general'
        BOOLEAN = 'boolean'
        STRING_LIST = 'string_list'
        IP_LIST = 'ip_list'
        TIMESTAMP = 'timestamp'



class Profile:
    """
    The response body of the profile.

    :attr str id: (optional) The unique ID of the profile.
    :attr str profile_name: (optional) The profile name.
    :attr str profile_description: (optional) The profile description.
    :attr str profile_type: (optional) The profile type, such as custom or
          predefined.
    :attr str profile_version: (optional) The version status of the profile.
    :attr str version_group_label: (optional) The version group label of the
          profile.
    :attr str instance_id: (optional) The instance ID.
    :attr bool latest: (optional) The latest version of the profile.
    :attr bool hierarchy_enabled: (optional) The indication of whether hierarchy is
          enabled for the profile.
    :attr str created_by: (optional) The user who created the profile.
    :attr datetime created_on: (optional) The date when the profile was created.
    :attr str updated_by: (optional) The user who updated the profile.
    :attr datetime updated_on: (optional) The date when the profile was updated.
    :attr int controls_count: (optional) The number of controls for the profile.
    :attr int control_parents_count: (optional) The number of parent controls for
          the profile.
    :attr int attachments_count: (optional) The number of attachments related to
          this profile.
    :attr List[ProfileControls] controls: (optional) The array of controls that are
          used to create the profile.
    :attr List[DefaultParametersPrototype] default_parameters: (optional) The
          default parameters of the profile.
    """

    def __init__(
        self,
        *,
        id: str = None,
        profile_name: str = None,
        profile_description: str = None,
        profile_type: str = None,
        profile_version: str = None,
        version_group_label: str = None,
        instance_id: str = None,
        latest: bool = None,
        hierarchy_enabled: bool = None,
        created_by: str = None,
        created_on: datetime = None,
        updated_by: str = None,
        updated_on: datetime = None,
        controls_count: int = None,
        control_parents_count: int = None,
        attachments_count: int = None,
        controls: List['ProfileControls'] = None,
        default_parameters: List['DefaultParametersPrototype'] = None,
    ) -> None:
        """
        Initialize a Profile object.

        :param str id: (optional) The unique ID of the profile.
        :param str profile_name: (optional) The profile name.
        :param str profile_description: (optional) The profile description.
        :param str profile_type: (optional) The profile type, such as custom or
               predefined.
        :param str profile_version: (optional) The version status of the profile.
        :param str version_group_label: (optional) The version group label of the
               profile.
        :param str instance_id: (optional) The instance ID.
        :param bool latest: (optional) The latest version of the profile.
        :param bool hierarchy_enabled: (optional) The indication of whether
               hierarchy is enabled for the profile.
        :param str created_by: (optional) The user who created the profile.
        :param datetime created_on: (optional) The date when the profile was
               created.
        :param str updated_by: (optional) The user who updated the profile.
        :param datetime updated_on: (optional) The date when the profile was
               updated.
        :param int controls_count: (optional) The number of controls for the
               profile.
        :param int control_parents_count: (optional) The number of parent controls
               for the profile.
        :param int attachments_count: (optional) The number of attachments related
               to this profile.
        :param List[ProfileControls] controls: (optional) The array of controls
               that are used to create the profile.
        :param List[DefaultParametersPrototype] default_parameters: (optional) The
               default parameters of the profile.
        """
        self.id = id
        self.profile_name = profile_name
        self.profile_description = profile_description
        self.profile_type = profile_type
        self.profile_version = profile_version
        self.version_group_label = version_group_label
        self.instance_id = instance_id
        self.latest = latest
        self.hierarchy_enabled = hierarchy_enabled
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.controls_count = controls_count
        self.control_parents_count = control_parents_count
        self.attachments_count = attachments_count
        self.controls = controls
        self.default_parameters = default_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Profile':
        """Initialize a Profile object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'profile_name' in _dict:
            args['profile_name'] = _dict.get('profile_name')
        if 'profile_description' in _dict:
            args['profile_description'] = _dict.get('profile_description')
        if 'profile_type' in _dict:
            args['profile_type'] = _dict.get('profile_type')
        if 'profile_version' in _dict:
            args['profile_version'] = _dict.get('profile_version')
        if 'version_group_label' in _dict:
            args['version_group_label'] = _dict.get('version_group_label')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'latest' in _dict:
            args['latest'] = _dict.get('latest')
        if 'hierarchy_enabled' in _dict:
            args['hierarchy_enabled'] = _dict.get('hierarchy_enabled')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        if 'control_parents_count' in _dict:
            args['control_parents_count'] = _dict.get('control_parents_count')
        if 'attachments_count' in _dict:
            args['attachments_count'] = _dict.get('attachments_count')
        if 'controls' in _dict:
            args['controls'] = [ProfileControls.from_dict(v) for v in _dict.get('controls')]
        if 'default_parameters' in _dict:
            args['default_parameters'] = [DefaultParametersPrototype.from_dict(v) for v in _dict.get('default_parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Profile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'profile_name') and self.profile_name is not None:
            _dict['profile_name'] = self.profile_name
        if hasattr(self, 'profile_description') and self.profile_description is not None:
            _dict['profile_description'] = self.profile_description
        if hasattr(self, 'profile_type') and self.profile_type is not None:
            _dict['profile_type'] = self.profile_type
        if hasattr(self, 'profile_version') and self.profile_version is not None:
            _dict['profile_version'] = self.profile_version
        if hasattr(self, 'version_group_label') and self.version_group_label is not None:
            _dict['version_group_label'] = self.version_group_label
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'latest') and self.latest is not None:
            _dict['latest'] = self.latest
        if hasattr(self, 'hierarchy_enabled') and self.hierarchy_enabled is not None:
            _dict['hierarchy_enabled'] = self.hierarchy_enabled
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
        if hasattr(self, 'control_parents_count') and self.control_parents_count is not None:
            _dict['control_parents_count'] = self.control_parents_count
        if hasattr(self, 'attachments_count') and self.attachments_count is not None:
            _dict['attachments_count'] = self.attachments_count
        if hasattr(self, 'controls') and self.controls is not None:
            controls_list = []
            for v in self.controls:
                if isinstance(v, dict):
                    controls_list.append(v)
                else:
                    controls_list.append(v.to_dict())
            _dict['controls'] = controls_list
        if hasattr(self, 'default_parameters') and self.default_parameters is not None:
            default_parameters_list = []
            for v in self.default_parameters:
                if isinstance(v, dict):
                    default_parameters_list.append(v)
                else:
                    default_parameters_list.append(v.to_dict())
            _dict['default_parameters'] = default_parameters_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Profile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Profile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Profile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProfileTypeEnum(str, Enum):
        """
        The profile type, such as custom or predefined.
        """

        PREDEFINED = 'predefined'
        CUSTOM = 'custom'



class ProfileCollection:
    """
    The response body to get all profiles that are linked to your account.

    :attr int total_count: The number of profiles.
    :attr int limit: The limit of profiles that can be created.
    :attr PaginatedCollectionFirst first: The reference to the first page of
          entries.
    :attr PaginatedCollectionNext next: The reference URL for the next few entries.
    :attr List[ProfileItem] profiles: The profiles.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'PaginatedCollectionFirst',
        next: 'PaginatedCollectionNext',
        profiles: List['ProfileItem'],
    ) -> None:
        """
        Initialize a ProfileCollection object.

        :param int total_count: The number of profiles.
        :param int limit: The limit of profiles that can be created.
        :param PaginatedCollectionFirst first: The reference to the first page of
               entries.
        :param PaginatedCollectionNext next: The reference URL for the next few
               entries.
        :param List[ProfileItem] profiles: The profiles.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.next = next
        self.profiles = profiles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileCollection':
        """Initialize a ProfileCollection object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ProfileCollection JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ProfileCollection JSON')
        if 'first' in _dict:
            args['first'] = PaginatedCollectionFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ProfileCollection JSON')
        if 'next' in _dict:
            args['next'] = PaginatedCollectionNext.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ProfileCollection JSON')
        if 'profiles' in _dict:
            args['profiles'] = [ProfileItem.from_dict(v) for v in _dict.get('profiles')]
        else:
            raise ValueError('Required property \'profiles\' not present in ProfileCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'profiles') and self.profiles is not None:
            profiles_list = []
            for v in self.profiles:
                if isinstance(v, dict):
                    profiles_list.append(v)
                else:
                    profiles_list.append(v.to_dict())
            _dict['profiles'] = profiles_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileControls:
    """
    The control details for the profile.

    :attr str control_library_id: (optional) The ID of the control library that
          contains the profile.
    :attr str control_id: (optional) The unique ID of the control library that
          contains the profile.
    :attr str control_library_version: (optional) The most recent version of the
          control library.
    :attr str control_name: (optional) The control name.
    :attr str control_description: (optional) The control description.
    :attr str control_category: (optional) The control category.
    :attr str control_parent: (optional) The parent control.
    :attr bool control_requirement: (optional) Is this a control that can be
          automated or manually evaluated.
    :attr ControlDocs control_docs: (optional) The control documentation.
    :attr int control_specifications_count: (optional) The number of control
          specifications.
    :attr List[ControlSpecifications] control_specifications: (optional) The control
          specifications.
    """

    def __init__(
        self,
        *,
        control_library_id: str = None,
        control_id: str = None,
        control_library_version: str = None,
        control_name: str = None,
        control_description: str = None,
        control_category: str = None,
        control_parent: str = None,
        control_requirement: bool = None,
        control_docs: 'ControlDocs' = None,
        control_specifications_count: int = None,
        control_specifications: List['ControlSpecifications'] = None,
    ) -> None:
        """
        Initialize a ProfileControls object.

        :param str control_library_id: (optional) The ID of the control library
               that contains the profile.
        :param str control_id: (optional) The unique ID of the control library that
               contains the profile.
        :param str control_library_version: (optional) The most recent version of
               the control library.
        :param str control_name: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_category: (optional) The control category.
        :param str control_parent: (optional) The parent control.
        :param bool control_requirement: (optional) Is this a control that can be
               automated or manually evaluated.
        :param ControlDocs control_docs: (optional) The control documentation.
        :param int control_specifications_count: (optional) The number of control
               specifications.
        :param List[ControlSpecifications] control_specifications: (optional) The
               control specifications.
        """
        self.control_library_id = control_library_id
        self.control_id = control_id
        self.control_library_version = control_library_version
        self.control_name = control_name
        self.control_description = control_description
        self.control_category = control_category
        self.control_parent = control_parent
        self.control_requirement = control_requirement
        self.control_docs = control_docs
        self.control_specifications_count = control_specifications_count
        self.control_specifications = control_specifications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileControls':
        """Initialize a ProfileControls object from a json dictionary."""
        args = {}
        if 'control_library_id' in _dict:
            args['control_library_id'] = _dict.get('control_library_id')
        if 'control_id' in _dict:
            args['control_id'] = _dict.get('control_id')
        if 'control_library_version' in _dict:
            args['control_library_version'] = _dict.get('control_library_version')
        if 'control_name' in _dict:
            args['control_name'] = _dict.get('control_name')
        if 'control_description' in _dict:
            args['control_description'] = _dict.get('control_description')
        if 'control_category' in _dict:
            args['control_category'] = _dict.get('control_category')
        if 'control_parent' in _dict:
            args['control_parent'] = _dict.get('control_parent')
        if 'control_requirement' in _dict:
            args['control_requirement'] = _dict.get('control_requirement')
        if 'control_docs' in _dict:
            args['control_docs'] = ControlDocs.from_dict(_dict.get('control_docs'))
        if 'control_specifications_count' in _dict:
            args['control_specifications_count'] = _dict.get('control_specifications_count')
        if 'control_specifications' in _dict:
            args['control_specifications'] = [ControlSpecifications.from_dict(v) for v in _dict.get('control_specifications')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileControls object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_library_id') and self.control_library_id is not None:
            _dict['control_library_id'] = self.control_library_id
        if hasattr(self, 'control_id') and self.control_id is not None:
            _dict['control_id'] = self.control_id
        if hasattr(self, 'control_library_version') and self.control_library_version is not None:
            _dict['control_library_version'] = self.control_library_version
        if hasattr(self, 'control_name') and self.control_name is not None:
            _dict['control_name'] = self.control_name
        if hasattr(self, 'control_description') and self.control_description is not None:
            _dict['control_description'] = self.control_description
        if hasattr(self, 'control_category') and self.control_category is not None:
            _dict['control_category'] = self.control_category
        if hasattr(self, 'control_parent') and self.control_parent is not None:
            _dict['control_parent'] = self.control_parent
        if hasattr(self, 'control_requirement') and self.control_requirement is not None:
            _dict['control_requirement'] = self.control_requirement
        if hasattr(self, 'control_docs') and self.control_docs is not None:
            if isinstance(self.control_docs, dict):
                _dict['control_docs'] = self.control_docs
            else:
                _dict['control_docs'] = self.control_docs.to_dict()
        if hasattr(self, 'control_specifications_count') and self.control_specifications_count is not None:
            _dict['control_specifications_count'] = self.control_specifications_count
        if hasattr(self, 'control_specifications') and self.control_specifications is not None:
            control_specifications_list = []
            for v in self.control_specifications:
                if isinstance(v, dict):
                    control_specifications_list.append(v)
                else:
                    control_specifications_list.append(v.to_dict())
            _dict['control_specifications'] = control_specifications_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileControls object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileControls') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileControls') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileControlsPrototype:
    """
    The control details of a profile.

    :attr str control_library_id: (optional) The ID of the control library that
          contains the profile.
    :attr str control_id: (optional) The control ID.
    """

    def __init__(
        self,
        *,
        control_library_id: str = None,
        control_id: str = None,
    ) -> None:
        """
        Initialize a ProfileControlsPrototype object.

        :param str control_library_id: (optional) The ID of the control library
               that contains the profile.
        :param str control_id: (optional) The control ID.
        """
        self.control_library_id = control_library_id
        self.control_id = control_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileControlsPrototype':
        """Initialize a ProfileControlsPrototype object from a json dictionary."""
        args = {}
        if 'control_library_id' in _dict:
            args['control_library_id'] = _dict.get('control_library_id')
        if 'control_id' in _dict:
            args['control_id'] = _dict.get('control_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileControlsPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_library_id') and self.control_library_id is not None:
            _dict['control_library_id'] = self.control_library_id
        if hasattr(self, 'control_id') and self.control_id is not None:
            _dict['control_id'] = self.control_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileControlsPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileControlsPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileControlsPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileInfo:
    """
    The profile information.

    :attr str id: (optional) The profile ID.
    :attr str name: (optional) The profile name.
    :attr str version: (optional) The profile version.
    """

    def __init__(
        self,
        *,
        id: str = None,
        name: str = None,
        version: str = None,
    ) -> None:
        """
        Initialize a ProfileInfo object.

        :param str id: (optional) The profile ID.
        :param str name: (optional) The profile name.
        :param str version: (optional) The profile version.
        """
        self.id = id
        self.name = name
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileInfo':
        """Initialize a ProfileInfo object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileItem:
    """
    ProfileItem.

    :attr str id: (optional) The profile ID.
    :attr str profile_name: (optional) The profile name.
    :attr str profile_description: (optional) The profile description.
    :attr str profile_type: (optional) The profile type.
    :attr str profile_version: (optional) The profile version.
    :attr str version_group_label: (optional) The version group label.
    :attr bool latest: (optional) The latest profile.
    :attr str created_by: (optional) The user who created the profile.
    :attr datetime created_on: (optional) The date when the profile was created.
    :attr str updated_by: (optional) The user who updated the profile.
    :attr datetime updated_on: (optional) The date when the profile was updated.
    :attr int controls_count: (optional) The number of controls.
    :attr int attachments_count: (optional) The number of attachments.
    """

    def __init__(
        self,
        *,
        id: str = None,
        profile_name: str = None,
        profile_description: str = None,
        profile_type: str = None,
        profile_version: str = None,
        version_group_label: str = None,
        latest: bool = None,
        created_by: str = None,
        created_on: datetime = None,
        updated_by: str = None,
        updated_on: datetime = None,
        controls_count: int = None,
        attachments_count: int = None,
    ) -> None:
        """
        Initialize a ProfileItem object.

        :param str id: (optional) The profile ID.
        :param str profile_name: (optional) The profile name.
        :param str profile_description: (optional) The profile description.
        :param str profile_type: (optional) The profile type.
        :param str profile_version: (optional) The profile version.
        :param str version_group_label: (optional) The version group label.
        :param bool latest: (optional) The latest profile.
        :param str created_by: (optional) The user who created the profile.
        :param datetime created_on: (optional) The date when the profile was
               created.
        :param str updated_by: (optional) The user who updated the profile.
        :param datetime updated_on: (optional) The date when the profile was
               updated.
        :param int controls_count: (optional) The number of controls.
        :param int attachments_count: (optional) The number of attachments.
        """
        self.id = id
        self.profile_name = profile_name
        self.profile_description = profile_description
        self.profile_type = profile_type
        self.profile_version = profile_version
        self.version_group_label = version_group_label
        self.latest = latest
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.controls_count = controls_count
        self.attachments_count = attachments_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileItem':
        """Initialize a ProfileItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'profile_name' in _dict:
            args['profile_name'] = _dict.get('profile_name')
        if 'profile_description' in _dict:
            args['profile_description'] = _dict.get('profile_description')
        if 'profile_type' in _dict:
            args['profile_type'] = _dict.get('profile_type')
        if 'profile_version' in _dict:
            args['profile_version'] = _dict.get('profile_version')
        if 'version_group_label' in _dict:
            args['version_group_label'] = _dict.get('version_group_label')
        if 'latest' in _dict:
            args['latest'] = _dict.get('latest')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        if 'attachments_count' in _dict:
            args['attachments_count'] = _dict.get('attachments_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'profile_name') and self.profile_name is not None:
            _dict['profile_name'] = self.profile_name
        if hasattr(self, 'profile_description') and self.profile_description is not None:
            _dict['profile_description'] = self.profile_description
        if hasattr(self, 'profile_type') and self.profile_type is not None:
            _dict['profile_type'] = self.profile_type
        if hasattr(self, 'profile_version') and self.profile_version is not None:
            _dict['profile_version'] = self.profile_version
        if hasattr(self, 'version_group_label') and self.version_group_label is not None:
            _dict['version_group_label'] = self.version_group_label
        if hasattr(self, 'latest') and self.latest is not None:
            _dict['latest'] = self.latest
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
        if hasattr(self, 'attachments_count') and self.attachments_count is not None:
            _dict['attachments_count'] = self.attachments_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Property:
    """
    The property.

    :attr str property: (optional) The property name.
    :attr str property_description: (optional) The property description.
    :attr str operator: (optional) The property operator.
    :attr object expected_value: (optional) The property value.
    :attr object found_value: (optional) The property value.
    """

    def __init__(
        self,
        *,
        property: str = None,
        property_description: str = None,
        operator: str = None,
        expected_value: object = None,
        found_value: object = None,
    ) -> None:
        """
        Initialize a Property object.

        :param str property: (optional) The property name.
        :param str property_description: (optional) The property description.
        :param str operator: (optional) The property operator.
        :param object expected_value: (optional) The property value.
        :param object found_value: (optional) The property value.
        """
        self.property = property
        self.property_description = property_description
        self.operator = operator
        self.expected_value = expected_value
        self.found_value = found_value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Property':
        """Initialize a Property object from a json dictionary."""
        args = {}
        if 'property' in _dict:
            args['property'] = _dict.get('property')
        if 'property_description' in _dict:
            args['property_description'] = _dict.get('property_description')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        if 'expected_value' in _dict:
            args['expected_value'] = _dict.get('expected_value')
        if 'found_value' in _dict:
            args['found_value'] = _dict.get('found_value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Property object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'property_description') and self.property_description is not None:
            _dict['property_description'] = self.property_description
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'expected_value') and self.expected_value is not None:
            _dict['expected_value'] = self.expected_value
        if hasattr(self, 'found_value') and self.found_value is not None:
            _dict['found_value'] = self.found_value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Property object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Property') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Property') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PropertyItem:
    """
    The properties supported for scoping by this environment.

    :attr str name: (optional) The name of the property.
    :attr str value: (optional) The value of the property.
    """

    def __init__(
        self,
        *,
        name: {} = None,
        value: {} = None,
    ) -> None:
        """
        Initialize a PropertyItem object.

        :param str name: (optional) The name of the property.
        :param str value: (optional) The value of the property.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PropertyItem':
        """Initialize a PropertyItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PropertyItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PropertyItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PropertyItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PropertyItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypeInstanceItem:
    """
    A provider type instance.

    :attr str id: (optional) The unique identifier of the provider type instance.
    :attr str type: (optional) The type of the provider type.
    :attr str name: (optional) The name of the provider type instance.
    :attr dict attributes: (optional) The attributes for connecting to the provider
          type instance.
    :attr datetime created_at: (optional) Time at which resource was created.
    :attr datetime updated_at: (optional) Time at which resource was updated.
    """

    def __init__(
        self,
        *,
        id: str = None,
        type: str = None,
        name: str = None,
        attributes: dict = None,
        created_at: datetime = None,
        updated_at: datetime = None,
    ) -> None:
        """
        Initialize a ProviderTypeInstanceItem object.

        :param str id: (optional) The unique identifier of the provider type
               instance.
        :param str type: (optional) The type of the provider type.
        :param str name: (optional) The name of the provider type instance.
        :param dict attributes: (optional) The attributes for connecting to the
               provider type instance.
        :param datetime created_at: (optional) Time at which resource was created.
        :param datetime updated_at: (optional) Time at which resource was updated.
        """
        self.id = id
        self.type = type
        self.name = name
        self.attributes = attributes
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypeInstanceItem':
        """Initialize a ProviderTypeInstanceItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'attributes' in _dict:
            args['attributes'] = _dict.get('attributes')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypeInstanceItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'attributes') and self.attributes is not None:
            _dict['attributes'] = self.attributes
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderTypeInstanceItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypeInstanceItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypeInstanceItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypeInstancesResponse:
    """
    Provider type instances response.

    :attr List[ProviderTypeInstanceItem] provider_type_instances: (optional) The
          array of instances for a provider type.
    """

    def __init__(
        self,
        *,
        provider_type_instances: List['ProviderTypeInstanceItem'] = None,
    ) -> None:
        """
        Initialize a ProviderTypeInstancesResponse object.

        :param List[ProviderTypeInstanceItem] provider_type_instances: (optional)
               The array of instances for a provider type.
        """
        self.provider_type_instances = provider_type_instances

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypeInstancesResponse':
        """Initialize a ProviderTypeInstancesResponse object from a json dictionary."""
        args = {}
        if 'provider_type_instances' in _dict:
            args['provider_type_instances'] = [ProviderTypeInstanceItem.from_dict(v) for v in _dict.get('provider_type_instances')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypeInstancesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_type_instances') and self.provider_type_instances is not None:
            provider_type_instances_list = []
            for v in self.provider_type_instances:
                if isinstance(v, dict):
                    provider_type_instances_list.append(v)
                else:
                    provider_type_instances_list.append(v.to_dict())
            _dict['provider_type_instances'] = provider_type_instances_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderTypeInstancesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypeInstancesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypeInstancesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypeItem:
    """
    The provider type item.

    :attr str id: The unique identifier of the provider type.
    :attr str type: The type of the provider type.
    :attr str name: The name of the provider type.
    :attr str description: The provider type description.
    :attr bool s2s_enabled: A boolean that indicates whether the provider type is
          s2s-enabled.
    :attr int instance_limit: The maximum number of instances that can be created
          for the provider type.
    :attr str mode: The mode that is used to get results from provider (`PUSH` or
          `PULL`).
    :attr str data_type: The format of the results that a provider supports.
    :attr str icon: The icon of a provider in .svg format that is encoded as a
          base64 string.
    :attr LabelType label: (optional) The label that is associated with the provider
          type.
    :attr dict attributes: The attributes that are required when you're creating an
          instance of a provider type. The attributes field can have multiple  keys in its
          value. Each of those keys has a value  object that includes the type, and
          display name as keys. For example, `{type:"", display_name:""}`.
          **NOTE;** If the provider type is s2s-enabled, which means that if the
          `s2s_enabled` field is set to `true`, then a CRN field of type text is required
          in the attributes value object.
    :attr datetime created_at: (optional) Time at which resource was created.
    :attr datetime updated_at: (optional) Time at which resource was updated.
    """

    def __init__(
        self,
        id: str,
        type: str,
        name: str,
        description: str,
        s2s_enabled: bool,
        instance_limit: int,
        mode: str,
        data_type: str,
        icon: str,
        attributes: dict,
        *,
        label: 'LabelType' = None,
        created_at: datetime = None,
        updated_at: datetime = None,
    ) -> None:
        """
        Initialize a ProviderTypeItem object.

        :param str id: The unique identifier of the provider type.
        :param str type: The type of the provider type.
        :param str name: The name of the provider type.
        :param str description: The provider type description.
        :param bool s2s_enabled: A boolean that indicates whether the provider type
               is s2s-enabled.
        :param int instance_limit: The maximum number of instances that can be
               created for the provider type.
        :param str mode: The mode that is used to get results from provider (`PUSH`
               or `PULL`).
        :param str data_type: The format of the results that a provider supports.
        :param str icon: The icon of a provider in .svg format that is encoded as a
               base64 string.
        :param dict attributes: The attributes that are required when you're
               creating an instance of a provider type. The attributes field can have
               multiple  keys in its value. Each of those keys has a value  object that
               includes the type, and display name as keys. For example, `{type:"",
               display_name:""}`.
               **NOTE;** If the provider type is s2s-enabled, which means that if the
               `s2s_enabled` field is set to `true`, then a CRN field of type text is
               required in the attributes value object.
        :param LabelType label: (optional) The label that is associated with the
               provider type.
        :param datetime created_at: (optional) Time at which resource was created.
        :param datetime updated_at: (optional) Time at which resource was updated.
        """
        self.id = id
        self.type = type
        self.name = name
        self.description = description
        self.s2s_enabled = s2s_enabled
        self.instance_limit = instance_limit
        self.mode = mode
        self.data_type = data_type
        self.icon = icon
        self.label = label
        self.attributes = attributes
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypeItem':
        """Initialize a ProviderTypeItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProviderTypeItem JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ProviderTypeItem JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProviderTypeItem JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in ProviderTypeItem JSON')
        if 's2s_enabled' in _dict:
            args['s2s_enabled'] = _dict.get('s2s_enabled')
        else:
            raise ValueError('Required property \'s2s_enabled\' not present in ProviderTypeItem JSON')
        if 'instance_limit' in _dict:
            args['instance_limit'] = _dict.get('instance_limit')
        else:
            raise ValueError('Required property \'instance_limit\' not present in ProviderTypeItem JSON')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in ProviderTypeItem JSON')
        if 'data_type' in _dict:
            args['data_type'] = _dict.get('data_type')
        else:
            raise ValueError('Required property \'data_type\' not present in ProviderTypeItem JSON')
        if 'icon' in _dict:
            args['icon'] = _dict.get('icon')
        else:
            raise ValueError('Required property \'icon\' not present in ProviderTypeItem JSON')
        if 'label' in _dict:
            args['label'] = LabelType.from_dict(_dict.get('label'))
        if 'attributes' in _dict:
            args['attributes'] = {k: AdditionalProperty.from_dict(v) for k, v in _dict.get('attributes').items()}
        else:
            raise ValueError('Required property \'attributes\' not present in ProviderTypeItem JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypeItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 's2s_enabled') and self.s2s_enabled is not None:
            _dict['s2s_enabled'] = self.s2s_enabled
        if hasattr(self, 'instance_limit') and self.instance_limit is not None:
            _dict['instance_limit'] = self.instance_limit
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'data_type') and self.data_type is not None:
            _dict['data_type'] = self.data_type
        if hasattr(self, 'icon') and self.icon is not None:
            _dict['icon'] = self.icon
        if hasattr(self, 'label') and self.label is not None:
            if isinstance(self.label, dict):
                _dict['label'] = self.label
            else:
                _dict['label'] = self.label.to_dict()
        if hasattr(self, 'attributes') and self.attributes is not None:
            attributes_map = {}
            for k, v in self.attributes.items():
                if isinstance(v, dict):
                    attributes_map[k] = v
                else:
                    attributes_map[k] = v.to_dict()
            _dict['attributes'] = attributes_map
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderTypeItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypeItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypeItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypesCollection:
    """
    The provider types collection.

    :attr List[ProviderTypeItem] provider_types: (optional) The array of provder
          type.
    """

    def __init__(
        self,
        *,
        provider_types: List['ProviderTypeItem'] = None,
    ) -> None:
        """
        Initialize a ProviderTypesCollection object.

        :param List[ProviderTypeItem] provider_types: (optional) The array of
               provder type.
        """
        self.provider_types = provider_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypesCollection':
        """Initialize a ProviderTypesCollection object from a json dictionary."""
        args = {}
        if 'provider_types' in _dict:
            args['provider_types'] = [ProviderTypeItem.from_dict(v) for v in _dict.get('provider_types')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypesCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_types') and self.provider_types is not None:
            provider_types_list = []
            for v in self.provider_types:
                if isinstance(v, dict):
                    provider_types_list.append(v)
                else:
                    provider_types_list.append(v.to_dict())
            _dict['provider_types'] = provider_types_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderTypesCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypesCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypesCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypesInstancesResponse:
    """
    Provider types instances response.

    :attr List[ProviderTypeInstanceItem] provider_types_instances: (optional) The
          array of instances for all provider types.
    """

    def __init__(
        self,
        *,
        provider_types_instances: List['ProviderTypeInstanceItem'] = None,
    ) -> None:
        """
        Initialize a ProviderTypesInstancesResponse object.

        :param List[ProviderTypeInstanceItem] provider_types_instances: (optional)
               The array of instances for all provider types.
        """
        self.provider_types_instances = provider_types_instances

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypesInstancesResponse':
        """Initialize a ProviderTypesInstancesResponse object from a json dictionary."""
        args = {}
        if 'provider_types_instances' in _dict:
            args['provider_types_instances'] = [ProviderTypeInstanceItem.from_dict(v) for v in _dict.get('provider_types_instances')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypesInstancesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_types_instances') and self.provider_types_instances is not None:
            provider_types_instances_list = []
            for v in self.provider_types_instances:
                if isinstance(v, dict):
                    provider_types_instances_list.append(v)
                else:
                    provider_types_instances_list.append(v.to_dict())
            _dict['provider_types_instances'] = provider_types_instances_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderTypesInstancesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypesInstancesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypesInstancesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Report:
    """
    The report.

    :attr str id: (optional) The ID of the report.
    :attr str group_id: (optional) The group ID that is associated with the report.
          The group ID combines profile, scope, and attachment IDs.
    :attr str created_on: (optional) The date when the report was created.
    :attr str scan_time: (optional) The date when the scan was run.
    :attr str type: (optional) The type of the scan.
    :attr str cos_object: (optional) The Cloud Object Storage object that is
          associated with the report.
    :attr str instance_id: (optional) Instance ID.
    :attr Account account: (optional) The account that is associated with a report.
    :attr ProfileInfo profile: (optional) The profile information.
    :attr Attachment attachment: (optional) The attachment that is associated with a
          report.
    """

    def __init__(
        self,
        *,
        id: str = None,
        group_id: str = None,
        created_on: str = None,
        scan_time: str = None,
        type: str = None,
        cos_object: str = None,
        instance_id: str = None,
        account: 'Account' = None,
        profile: 'ProfileInfo' = None,
        attachment: 'Attachment' = None,
    ) -> None:
        """
        Initialize a Report object.

        :param str id: (optional) The ID of the report.
        :param str group_id: (optional) The group ID that is associated with the
               report. The group ID combines profile, scope, and attachment IDs.
        :param str created_on: (optional) The date when the report was created.
        :param str scan_time: (optional) The date when the scan was run.
        :param str type: (optional) The type of the scan.
        :param str cos_object: (optional) The Cloud Object Storage object that is
               associated with the report.
        :param str instance_id: (optional) Instance ID.
        :param Account account: (optional) The account that is associated with a
               report.
        :param ProfileInfo profile: (optional) The profile information.
        :param Attachment attachment: (optional) The attachment that is associated
               with a report.
        """
        self.id = id
        self.group_id = group_id
        self.created_on = created_on
        self.scan_time = scan_time
        self.type = type
        self.cos_object = cos_object
        self.instance_id = instance_id
        self.account = account
        self.profile = profile
        self.attachment = attachment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Report':
        """Initialize a Report object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'group_id' in _dict:
            args['group_id'] = _dict.get('group_id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'scan_time' in _dict:
            args['scan_time'] = _dict.get('scan_time')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'cos_object' in _dict:
            args['cos_object'] = _dict.get('cos_object')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'account' in _dict:
            args['account'] = Account.from_dict(_dict.get('account'))
        if 'profile' in _dict:
            args['profile'] = ProfileInfo.from_dict(_dict.get('profile'))
        if 'attachment' in _dict:
            args['attachment'] = Attachment.from_dict(_dict.get('attachment'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Report object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'group_id') and self.group_id is not None:
            _dict['group_id'] = self.group_id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'scan_time') and self.scan_time is not None:
            _dict['scan_time'] = self.scan_time
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'cos_object') and self.cos_object is not None:
            _dict['cos_object'] = self.cos_object
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'account') and self.account is not None:
            if isinstance(self.account, dict):
                _dict['account'] = self.account
            else:
                _dict['account'] = self.account.to_dict()
        if hasattr(self, 'profile') and self.profile is not None:
            if isinstance(self.profile, dict):
                _dict['profile'] = self.profile
            else:
                _dict['profile'] = self.profile.to_dict()
        if hasattr(self, 'attachment') and self.attachment is not None:
            if isinstance(self.attachment, dict):
                _dict['attachment'] = self.attachment
            else:
                _dict['attachment'] = self.attachment.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Report object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Report') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Report') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportControls:
    """
    The list of controls.

    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of checks.
    :attr int compliant_count: (optional) The number of compliant checks.
    :attr int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :attr int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :attr int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :attr str home_account_id: (optional) The ID of the home account.
    :attr str report_id: (optional) The ID of the report.
    :attr List[ControlWithStats] controls: (optional) The list of controls that are
          in the report.
    """

    def __init__(
        self,
        *,
        status: str = None,
        total_count: int = None,
        compliant_count: int = None,
        not_compliant_count: int = None,
        unable_to_perform_count: int = None,
        user_evaluation_required_count: int = None,
        home_account_id: str = None,
        report_id: str = None,
        controls: List['ControlWithStats'] = None,
    ) -> None:
        """
        Initialize a ReportControls object.

        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param str home_account_id: (optional) The ID of the home account.
        :param str report_id: (optional) The ID of the report.
        :param List[ControlWithStats] controls: (optional) The list of controls
               that are in the report.
        """
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.home_account_id = home_account_id
        self.report_id = report_id
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportControls':
        """Initialize a ReportControls object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'compliant_count' in _dict:
            args['compliant_count'] = _dict.get('compliant_count')
        if 'not_compliant_count' in _dict:
            args['not_compliant_count'] = _dict.get('not_compliant_count')
        if 'unable_to_perform_count' in _dict:
            args['unable_to_perform_count'] = _dict.get('unable_to_perform_count')
        if 'user_evaluation_required_count' in _dict:
            args['user_evaluation_required_count'] = _dict.get('user_evaluation_required_count')
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'controls' in _dict:
            args['controls'] = [ControlWithStats.from_dict(v) for v in _dict.get('controls')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportControls object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'compliant_count') and self.compliant_count is not None:
            _dict['compliant_count'] = self.compliant_count
        if hasattr(self, 'not_compliant_count') and self.not_compliant_count is not None:
            _dict['not_compliant_count'] = self.not_compliant_count
        if hasattr(self, 'unable_to_perform_count') and self.unable_to_perform_count is not None:
            _dict['unable_to_perform_count'] = self.unable_to_perform_count
        if hasattr(self, 'user_evaluation_required_count') and self.user_evaluation_required_count is not None:
            _dict['user_evaluation_required_count'] = self.user_evaluation_required_count
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'controls') and self.controls is not None:
            controls_list = []
            for v in self.controls:
                if isinstance(v, dict):
                    controls_list.append(v)
                else:
                    controls_list.append(v.to_dict())
            _dict['controls'] = controls_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportControls object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportControls') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportControls') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class ReportLatest:
    """
    The response body of the `get_latest_reports` operation.

    :attr str home_account_id: (optional) The ID of the home account.
    :attr ComplianceStats controls_summary: (optional) The compliance stats.
    :attr EvalStats evaluations_summary: (optional) The evaluation stats.
    :attr ComplianceScore score: (optional) The compliance score.
    :attr List[Report] reports: (optional) The list of reports.
    """

    def __init__(
        self,
        *,
        home_account_id: str = None,
        controls_summary: 'ComplianceStats' = None,
        evaluations_summary: 'EvalStats' = None,
        score: 'ComplianceScore' = None,
        reports: List['Report'] = None,
    ) -> None:
        """
        Initialize a ReportLatest object.

        :param str home_account_id: (optional) The ID of the home account.
        :param ComplianceStats controls_summary: (optional) The compliance stats.
        :param EvalStats evaluations_summary: (optional) The evaluation stats.
        :param ComplianceScore score: (optional) The compliance score.
        :param List[Report] reports: (optional) The list of reports.
        """
        self.home_account_id = home_account_id
        self.controls_summary = controls_summary
        self.evaluations_summary = evaluations_summary
        self.score = score
        self.reports = reports

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportLatest':
        """Initialize a ReportLatest object from a json dictionary."""
        args = {}
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'controls_summary' in _dict:
            args['controls_summary'] = ComplianceStats.from_dict(_dict.get('controls_summary'))
        if 'evaluations_summary' in _dict:
            args['evaluations_summary'] = EvalStats.from_dict(_dict.get('evaluations_summary'))
        if 'score' in _dict:
            args['score'] = ComplianceScore.from_dict(_dict.get('score'))
        if 'reports' in _dict:
            args['reports'] = [Report.from_dict(v) for v in _dict.get('reports')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportLatest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'controls_summary') and self.controls_summary is not None:
            if isinstance(self.controls_summary, dict):
                _dict['controls_summary'] = self.controls_summary
            else:
                _dict['controls_summary'] = self.controls_summary.to_dict()
        if hasattr(self, 'evaluations_summary') and self.evaluations_summary is not None:
            if isinstance(self.evaluations_summary, dict):
                _dict['evaluations_summary'] = self.evaluations_summary
            else:
                _dict['evaluations_summary'] = self.evaluations_summary.to_dict()
        if hasattr(self, 'score') and self.score is not None:
            if isinstance(self.score, dict):
                _dict['score'] = self.score
            else:
                _dict['score'] = self.score.to_dict()
        if hasattr(self, 'reports') and self.reports is not None:
            reports_list = []
            for v in self.reports:
                if isinstance(v, dict):
                    reports_list.append(v)
                else:
                    reports_list.append(v.to_dict())
            _dict['reports'] = reports_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportLatest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportLatest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportLatest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportPage:
    """
    The page of reports.

    :attr int total_count: The total number of resources that are in the collection.
    :attr int limit: The requested page limi.t.
    :attr str start: (optional) The token of the next page, when it's present.
    :attr PageHRef first: The page reference.
    :attr PageHRef next: (optional) The page reference.
    :attr str home_account_id: (optional) The ID of the home account.
    :attr List[Report] reports: (optional) The list of reports that are on the page.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'PageHRef',
        *,
        start: str = None,
        next: 'PageHRef' = None,
        home_account_id: str = None,
        reports: List['Report'] = None,
    ) -> None:
        """
        Initialize a ReportPage object.

        :param int total_count: The total number of resources that are in the
               collection.
        :param int limit: The requested page limi.t.
        :param PageHRef first: The page reference.
        :param str start: (optional) The token of the next page, when it's present.
        :param PageHRef next: (optional) The page reference.
        :param str home_account_id: (optional) The ID of the home account.
        :param List[Report] reports: (optional) The list of reports that are on the
               page.
        """
        self.total_count = total_count
        self.limit = limit
        self.start = start
        self.first = first
        self.next = next
        self.home_account_id = home_account_id
        self.reports = reports

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportPage':
        """Initialize a ReportPage object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ReportPage JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ReportPage JSON')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'first' in _dict:
            args['first'] = PageHRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ReportPage JSON')
        if 'next' in _dict:
            args['next'] = PageHRef.from_dict(_dict.get('next'))
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'reports' in _dict:
            args['reports'] = [Report.from_dict(v) for v in _dict.get('reports')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportPage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'reports') and self.reports is not None:
            reports_list = []
            for v in self.reports:
                if isinstance(v, dict):
                    reports_list.append(v)
                else:
                    reports_list.append(v.to_dict())
            _dict['reports'] = reports_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportSummary:
    """
    The report summary.

    :attr str report_id: (optional) The ID of the report.
    :attr str isntance_id: (optional) Instance ID.
    :attr Account account: (optional) The account that is associated with a report.
    :attr ComplianceScore score: (optional) The compliance score.
    :attr ComplianceStats controls: (optional) The compliance stats.
    :attr EvalStats evaluations: (optional) The evaluation stats.
    :attr ResourceSummary resources: (optional) The resource summary.
    """

    def __init__(
        self,
        *,
        report_id: str = None,
        isntance_id: str = None,
        account: 'Account' = None,
        score: 'ComplianceScore' = None,
        controls: 'ComplianceStats' = None,
        evaluations: 'EvalStats' = None,
        resources: 'ResourceSummary' = None,
    ) -> None:
        """
        Initialize a ReportSummary object.

        :param str report_id: (optional) The ID of the report.
        :param str isntance_id: (optional) Instance ID.
        :param Account account: (optional) The account that is associated with a
               report.
        :param ComplianceScore score: (optional) The compliance score.
        :param ComplianceStats controls: (optional) The compliance stats.
        :param EvalStats evaluations: (optional) The evaluation stats.
        :param ResourceSummary resources: (optional) The resource summary.
        """
        self.report_id = report_id
        self.isntance_id = isntance_id
        self.account = account
        self.score = score
        self.controls = controls
        self.evaluations = evaluations
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportSummary':
        """Initialize a ReportSummary object from a json dictionary."""
        args = {}
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'isntance_id' in _dict:
            args['isntance_id'] = _dict.get('isntance_id')
        if 'account' in _dict:
            args['account'] = Account.from_dict(_dict.get('account'))
        if 'score' in _dict:
            args['score'] = ComplianceScore.from_dict(_dict.get('score'))
        if 'controls' in _dict:
            args['controls'] = ComplianceStats.from_dict(_dict.get('controls'))
        if 'evaluations' in _dict:
            args['evaluations'] = EvalStats.from_dict(_dict.get('evaluations'))
        if 'resources' in _dict:
            args['resources'] = ResourceSummary.from_dict(_dict.get('resources'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'isntance_id') and self.isntance_id is not None:
            _dict['isntance_id'] = self.isntance_id
        if hasattr(self, 'account') and self.account is not None:
            if isinstance(self.account, dict):
                _dict['account'] = self.account
            else:
                _dict['account'] = self.account.to_dict()
        if hasattr(self, 'score') and self.score is not None:
            if isinstance(self.score, dict):
                _dict['score'] = self.score
            else:
                _dict['score'] = self.score.to_dict()
        if hasattr(self, 'controls') and self.controls is not None:
            if isinstance(self.controls, dict):
                _dict['controls'] = self.controls
            else:
                _dict['controls'] = self.controls.to_dict()
        if hasattr(self, 'evaluations') and self.evaluations is not None:
            if isinstance(self.evaluations, dict):
                _dict['evaluations'] = self.evaluations
            else:
                _dict['evaluations'] = self.evaluations.to_dict()
        if hasattr(self, 'resources') and self.resources is not None:
            if isinstance(self.resources, dict):
                _dict['resources'] = self.resources
            else:
                _dict['resources'] = self.resources.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportTags:
    """
    The response body of the `get_tags` operation.

    :attr str report_id: (optional) The ID of the report.
    :attr Tags tags: (optional) The collection of different types of tags.
    """

    def __init__(
        self,
        *,
        report_id: str = None,
        tags: 'Tags' = None,
    ) -> None:
        """
        Initialize a ReportTags object.

        :param str report_id: (optional) The ID of the report.
        :param Tags tags: (optional) The collection of different types of tags.
        """
        self.report_id = report_id
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportTags':
        """Initialize a ReportTags object from a json dictionary."""
        args = {}
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'tags' in _dict:
            args['tags'] = Tags.from_dict(_dict.get('tags'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportTags object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'tags') and self.tags is not None:
            if isinstance(self.tags, dict):
                _dict['tags'] = self.tags
            else:
                _dict['tags'] = self.tags.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportTags object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportTags') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportTags') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportViolationDataPoint:
    """
    The report violation data point.

    :attr str report_id: (optional) The ID of the report.
    :attr str report_group_id: (optional) The group ID that is associated with the
          report. The group ID combines profile, scope, and attachment IDs.
    :attr str scan_time: (optional) The date when the scan was run.
    :attr ComplianceStats controls: (optional) The compliance stats.
    """

    def __init__(
        self,
        *,
        report_id: str = None,
        report_group_id: str = None,
        scan_time: str = None,
        controls: 'ComplianceStats' = None,
    ) -> None:
        """
        Initialize a ReportViolationDataPoint object.

        :param str report_id: (optional) The ID of the report.
        :param str report_group_id: (optional) The group ID that is associated with
               the report. The group ID combines profile, scope, and attachment IDs.
        :param str scan_time: (optional) The date when the scan was run.
        :param ComplianceStats controls: (optional) The compliance stats.
        """
        self.report_id = report_id
        self.report_group_id = report_group_id
        self.scan_time = scan_time
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportViolationDataPoint':
        """Initialize a ReportViolationDataPoint object from a json dictionary."""
        args = {}
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'report_group_id' in _dict:
            args['report_group_id'] = _dict.get('report_group_id')
        if 'scan_time' in _dict:
            args['scan_time'] = _dict.get('scan_time')
        if 'controls' in _dict:
            args['controls'] = ComplianceStats.from_dict(_dict.get('controls'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportViolationDataPoint object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'report_group_id') and self.report_group_id is not None:
            _dict['report_group_id'] = self.report_group_id
        if hasattr(self, 'scan_time') and self.scan_time is not None:
            _dict['scan_time'] = self.scan_time
        if hasattr(self, 'controls') and self.controls is not None:
            if isinstance(self.controls, dict):
                _dict['controls'] = self.controls
            else:
                _dict['controls'] = self.controls.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportViolationDataPoint object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportViolationDataPoint') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportViolationDataPoint') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportViolationsDrift:
    """
    The response body of the `get_report_violations_drift` operation.

    :attr str home_account_id: (optional) The ID of the home account.
    :attr str report_id: (optional) The ID of the report.
    :attr List[ReportViolationDataPoint] data_points: (optional) The list of report
          violations data points.
    """

    def __init__(
        self,
        *,
        home_account_id: str = None,
        report_id: str = None,
        data_points: List['ReportViolationDataPoint'] = None,
    ) -> None:
        """
        Initialize a ReportViolationsDrift object.

        :param str home_account_id: (optional) The ID of the home account.
        :param str report_id: (optional) The ID of the report.
        :param List[ReportViolationDataPoint] data_points: (optional) The list of
               report violations data points.
        """
        self.home_account_id = home_account_id
        self.report_id = report_id
        self.data_points = data_points

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportViolationsDrift':
        """Initialize a ReportViolationsDrift object from a json dictionary."""
        args = {}
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'data_points' in _dict:
            args['data_points'] = [ReportViolationDataPoint.from_dict(v) for v in _dict.get('data_points')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportViolationsDrift object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'data_points') and self.data_points is not None:
            data_points_list = []
            for v in self.data_points:
                if isinstance(v, dict):
                    data_points_list.append(v)
                else:
                    data_points_list.append(v.to_dict())
            _dict['data_points'] = data_points_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportViolationsDrift object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportViolationsDrift') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportViolationsDrift') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfig:
    """
    The required configurations.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a RequiredConfig object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['RequiredConfigRequiredConfigAnd', 'RequiredConfigRequiredConfigOr', 'RequiredConfigRequiredConfigBase'])
        )
        raise Exception(msg)


class RequiredConfigItems:
    """
    RequiredConfigItems.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a RequiredConfigItems object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['RequiredConfigItemsRequiredConfigOr', 'RequiredConfigItemsRequiredConfigAnd', 'RequiredConfigItemsRequiredConfigBase'])
        )
        raise Exception(msg)


class Resource:
    """
    The resource.

    :attr str report_id: (optional) The ID of the report.
    :attr str id: (optional) The resource CRN.
    :attr str resource_name: (optional) The resource name.
    :attr str component_id: (optional) The ID of the component.
    :attr str environment: (optional) The environment.
    :attr Account account: (optional) The account that is associated with a report.
    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of evaluations.
    :attr int pass_count: (optional) The number of passed evaluations.
    :attr int failure_count: (optional) The number of failed evaluations.
    :attr int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :attr int completed_count: (optional) The total number of completed evaluations.
    """

    def __init__(
        self,
        *,
        report_id: str = None,
        id: str = None,
        resource_name: str = None,
        component_id: str = None,
        environment: str = None,
        account: 'Account' = None,
        status: str = None,
        total_count: int = None,
        pass_count: int = None,
        failure_count: int = None,
        error_count: int = None,
        completed_count: int = None,
    ) -> None:
        """
        Initialize a Resource object.

        :param str report_id: (optional) The ID of the report.
        :param str id: (optional) The resource CRN.
        :param str resource_name: (optional) The resource name.
        :param str component_id: (optional) The ID of the component.
        :param str environment: (optional) The environment.
        :param Account account: (optional) The account that is associated with a
               report.
        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        """
        self.report_id = report_id
        self.id = id
        self.resource_name = resource_name
        self.component_id = component_id
        self.environment = environment
        self.account = account
        self.status = status
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.completed_count = completed_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'component_id' in _dict:
            args['component_id'] = _dict.get('component_id')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'account' in _dict:
            args['account'] = Account.from_dict(_dict.get('account'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'pass_count' in _dict:
            args['pass_count'] = _dict.get('pass_count')
        if 'failure_count' in _dict:
            args['failure_count'] = _dict.get('failure_count')
        if 'error_count' in _dict:
            args['error_count'] = _dict.get('error_count')
        if 'completed_count' in _dict:
            args['completed_count'] = _dict.get('completed_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'account') and self.account is not None:
            if isinstance(self.account, dict):
                _dict['account'] = self.account
            else:
                _dict['account'] = self.account.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'pass_count') and self.pass_count is not None:
            _dict['pass_count'] = self.pass_count
        if hasattr(self, 'failure_count') and self.failure_count is not None:
            _dict['failure_count'] = self.failure_count
        if hasattr(self, 'error_count') and self.error_count is not None:
            _dict['error_count'] = self.error_count
        if hasattr(self, 'completed_count') and self.completed_count is not None:
            _dict['completed_count'] = self.completed_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Resource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class ResourcePage:
    """
    The page of resource evaluation summaries.

    :attr int total_count: The total number of resources that are in the collection.
    :attr int limit: The requested page limi.t.
    :attr str start: (optional) The token of the next page, when it's present.
    :attr PageHRef first: The page reference.
    :attr PageHRef next: (optional) The page reference.
    :attr str home_account_id: (optional) The ID of the home account.
    :attr str report_id: (optional) The ID of the report.
    :attr List[Resource] resources: (optional) The list of resource evaluation
          summaries that are on the page.
    """

    def __init__(
        self,
        total_count: int,
        limit: int,
        first: 'PageHRef',
        *,
        start: str = None,
        next: 'PageHRef' = None,
        home_account_id: str = None,
        report_id: str = None,
        resources: List['Resource'] = None,
    ) -> None:
        """
        Initialize a ResourcePage object.

        :param int total_count: The total number of resources that are in the
               collection.
        :param int limit: The requested page limi.t.
        :param PageHRef first: The page reference.
        :param str start: (optional) The token of the next page, when it's present.
        :param PageHRef next: (optional) The page reference.
        :param str home_account_id: (optional) The ID of the home account.
        :param str report_id: (optional) The ID of the report.
        :param List[Resource] resources: (optional) The list of resource evaluation
               summaries that are on the page.
        """
        self.total_count = total_count
        self.limit = limit
        self.start = start
        self.first = first
        self.next = next
        self.home_account_id = home_account_id
        self.report_id = report_id
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourcePage':
        """Initialize a ResourcePage object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ResourcePage JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ResourcePage JSON')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'first' in _dict:
            args['first'] = PageHRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ResourcePage JSON')
        if 'next' in _dict:
            args['next'] = PageHRef.from_dict(_dict.get('next'))
        if 'home_account_id' in _dict:
            args['home_account_id'] = _dict.get('home_account_id')
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'resources' in _dict:
            args['resources'] = [Resource.from_dict(v) for v in _dict.get('resources')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourcePage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'resources') and self.resources is not None:
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourcePage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourcePage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourcePage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResourceSummary:
    """
    The resource summary.

    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of checks.
    :attr int compliant_count: (optional) The number of compliant checks.
    :attr int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :attr int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :attr int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :attr List[ResourceSummaryItem] top_failed: (optional) The top 10 resources that
          have the most failures.
    """

    def __init__(
        self,
        *,
        status: str = None,
        total_count: int = None,
        compliant_count: int = None,
        not_compliant_count: int = None,
        unable_to_perform_count: int = None,
        user_evaluation_required_count: int = None,
        top_failed: List['ResourceSummaryItem'] = None,
    ) -> None:
        """
        Initialize a ResourceSummary object.

        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param List[ResourceSummaryItem] top_failed: (optional) The top 10
               resources that have the most failures.
        """
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.top_failed = top_failed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceSummary':
        """Initialize a ResourceSummary object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'compliant_count' in _dict:
            args['compliant_count'] = _dict.get('compliant_count')
        if 'not_compliant_count' in _dict:
            args['not_compliant_count'] = _dict.get('not_compliant_count')
        if 'unable_to_perform_count' in _dict:
            args['unable_to_perform_count'] = _dict.get('unable_to_perform_count')
        if 'user_evaluation_required_count' in _dict:
            args['user_evaluation_required_count'] = _dict.get('user_evaluation_required_count')
        if 'top_failed' in _dict:
            args['top_failed'] = [ResourceSummaryItem.from_dict(v) for v in _dict.get('top_failed')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'compliant_count') and self.compliant_count is not None:
            _dict['compliant_count'] = self.compliant_count
        if hasattr(self, 'not_compliant_count') and self.not_compliant_count is not None:
            _dict['not_compliant_count'] = self.not_compliant_count
        if hasattr(self, 'unable_to_perform_count') and self.unable_to_perform_count is not None:
            _dict['unable_to_perform_count'] = self.unable_to_perform_count
        if hasattr(self, 'user_evaluation_required_count') and self.user_evaluation_required_count is not None:
            _dict['user_evaluation_required_count'] = self.user_evaluation_required_count
        if hasattr(self, 'top_failed') and self.top_failed is not None:
            top_failed_list = []
            for v in self.top_failed:
                if isinstance(v, dict):
                    top_failed_list.append(v)
                else:
                    top_failed_list.append(v.to_dict())
            _dict['top_failed'] = top_failed_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class ResourceSummaryItem:
    """
    The resource summary item.

    :attr str name: (optional) The resource name.
    :attr str id: (optional) The resource ID.
    :attr str service: (optional) The service that is managing the resource.
    :attr Tags tags: (optional) The collection of different types of tags.
    :attr str account: (optional) The account that owns the resource.
    :attr str status: (optional) The allowed values of an aggregated status for
          controls, specifications, assessments, and resources.
    :attr int total_count: (optional) The total number of evaluations.
    :attr int pass_count: (optional) The number of passed evaluations.
    :attr int failure_count: (optional) The number of failed evaluations.
    :attr int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :attr int completed_count: (optional) The total number of completed evaluations.
    """

    def __init__(
        self,
        *,
        name: str = None,
        id: str = None,
        service: str = None,
        tags: 'Tags' = None,
        account: str = None,
        status: str = None,
        total_count: int = None,
        pass_count: int = None,
        failure_count: int = None,
        error_count: int = None,
        completed_count: int = None,
    ) -> None:
        """
        Initialize a ResourceSummaryItem object.

        :param str name: (optional) The resource name.
        :param str id: (optional) The resource ID.
        :param str service: (optional) The service that is managing the resource.
        :param Tags tags: (optional) The collection of different types of tags.
        :param str account: (optional) The account that owns the resource.
        :param str status: (optional) The allowed values of an aggregated status
               for controls, specifications, assessments, and resources.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        """
        self.name = name
        self.id = id
        self.service = service
        self.tags = tags
        self.account = account
        self.status = status
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.completed_count = completed_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceSummaryItem':
        """Initialize a ResourceSummaryItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'service' in _dict:
            args['service'] = _dict.get('service')
        if 'tags' in _dict:
            args['tags'] = Tags.from_dict(_dict.get('tags'))
        if 'account' in _dict:
            args['account'] = _dict.get('account')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'pass_count' in _dict:
            args['pass_count'] = _dict.get('pass_count')
        if 'failure_count' in _dict:
            args['failure_count'] = _dict.get('failure_count')
        if 'error_count' in _dict:
            args['error_count'] = _dict.get('error_count')
        if 'completed_count' in _dict:
            args['completed_count'] = _dict.get('completed_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceSummaryItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service
        if hasattr(self, 'tags') and self.tags is not None:
            if isinstance(self.tags, dict):
                _dict['tags'] = self.tags
            else:
                _dict['tags'] = self.tags.to_dict()
        if hasattr(self, 'account') and self.account is not None:
            _dict['account'] = self.account
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'pass_count') and self.pass_count is not None:
            _dict['pass_count'] = self.pass_count
        if hasattr(self, 'failure_count') and self.failure_count is not None:
            _dict['failure_count'] = self.failure_count
        if hasattr(self, 'error_count') and self.error_count is not None:
            _dict['error_count'] = self.error_count
        if hasattr(self, 'completed_count') and self.completed_count is not None:
            _dict['completed_count'] = self.completed_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceSummaryItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceSummaryItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceSummaryItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The allowed values of an aggregated status for controls, specifications,
        assessments, and resources.
        """

        COMPLIANT = 'compliant'
        NOT_COMPLIANT = 'not_compliant'
        UNABLE_TO_PERFORM = 'unable_to_perform'
        USER_EVALUATION_REQUIRED = 'user_evaluation_required'



class Rule:
    """
    The rule response that corresponds to an account instance.

    :attr datetime created_on: The date when the rule was created.
    :attr str created_by: The user who created the rule.
    :attr datetime updated_on: The date when the rule was modified.
    :attr str updated_by: The user who modified the rule.
    :attr str id: The rule ID.
    :attr str account_id: The account ID.
    :attr str description: The details of a rule's response.
    :attr str type: The rule type (allowable values are `user_defined` or
          `system_defined`).
    :attr str version: The version number of a rule.
    :attr Import import_: (optional) The collection of import parameters.
    :attr Target target: The rule target.
    :attr RequiredConfig required_config: The required configurations.
    :attr List[str] labels: The list of labels.
    """

    def __init__(
        self,
        created_on: datetime,
        created_by: str,
        updated_on: datetime,
        updated_by: str,
        id: str,
        account_id: str,
        description: str,
        type: str,
        version: str,
        target: 'Target',
        required_config: 'RequiredConfig',
        labels: List[str],
        *,
        import_: 'Import' = None,
    ) -> None:
        """
        Initialize a Rule object.

        :param datetime created_on: The date when the rule was created.
        :param str created_by: The user who created the rule.
        :param datetime updated_on: The date when the rule was modified.
        :param str updated_by: The user who modified the rule.
        :param str id: The rule ID.
        :param str account_id: The account ID.
        :param str description: The details of a rule's response.
        :param str type: The rule type (allowable values are `user_defined` or
               `system_defined`).
        :param str version: The version number of a rule.
        :param Target target: The rule target.
        :param RequiredConfig required_config: The required configurations.
        :param List[str] labels: The list of labels.
        :param Import import_: (optional) The collection of import parameters.
        """
        self.created_on = created_on
        self.created_by = created_by
        self.updated_on = updated_on
        self.updated_by = updated_by
        self.id = id
        self.account_id = account_id
        self.description = description
        self.type = type
        self.version = version
        self.import_ = import_
        self.target = target
        self.required_config = required_config
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Rule':
        """Initialize a Rule object from a json dictionary."""
        args = {}
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        else:
            raise ValueError('Required property \'created_on\' not present in Rule JSON')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in Rule JSON')
        if 'updated_on' in _dict:
            args['updated_on'] = string_to_datetime(_dict.get('updated_on'))
        else:
            raise ValueError('Required property \'updated_on\' not present in Rule JSON')
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        else:
            raise ValueError('Required property \'updated_by\' not present in Rule JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Rule JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in Rule JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in Rule JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in Rule JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in Rule JSON')
        if 'import' in _dict:
            args['import_'] = Import.from_dict(_dict.get('import'))
        if 'target' in _dict:
            args['target'] = Target.from_dict(_dict.get('target'))
        else:
            raise ValueError('Required property \'target\' not present in Rule JSON')
        if 'required_config' in _dict:
            args['required_config'] = _dict.get('required_config')
        else:
            raise ValueError('Required property \'required_config\' not present in Rule JSON')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        else:
            raise ValueError('Required property \'labels\' not present in Rule JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Rule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'import_') and self.import_ is not None:
            if isinstance(self.import_, dict):
                _dict['import'] = self.import_
            else:
                _dict['import'] = self.import_.to_dict()
        if hasattr(self, 'target') and self.target is not None:
            if isinstance(self.target, dict):
                _dict['target'] = self.target
            else:
                _dict['target'] = self.target.to_dict()
        if hasattr(self, 'required_config') and self.required_config is not None:
            if isinstance(self.required_config, dict):
                _dict['required_config'] = self.required_config
            else:
                _dict['required_config'] = self.required_config.to_dict()
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Rule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The rule type (allowable values are `user_defined` or `system_defined`).
        """

        USER_DEFINED = 'user_defined'
        SYSTEM_DEFINED = 'system_defined'



class RuleInfo:
    """
    The rule.

    :attr str id: (optional) The rule ID.
    :attr str type: (optional) The rule type.
    :attr str description: (optional) The rule description.
    :attr str version: (optional) The rule version.
    :attr str account_id: (optional) The rule account ID.
    :attr str created_on: (optional) The date when the rule was created.
    :attr str created_by: (optional) The ID of the user who created the rule.
    :attr str updated_on: (optional) The date when the rule was updated.
    :attr str updated_by: (optional) The ID of the user who updated the rule.
    :attr List[str] labels: (optional) The rule labels.
    """

    def __init__(
        self,
        *,
        id: str = None,
        type: str = None,
        description: str = None,
        version: str = None,
        account_id: str = None,
        created_on: str = None,
        created_by: str = None,
        updated_on: str = None,
        updated_by: str = None,
        labels: List[str] = None,
    ) -> None:
        """
        Initialize a RuleInfo object.

        :param str id: (optional) The rule ID.
        :param str type: (optional) The rule type.
        :param str description: (optional) The rule description.
        :param str version: (optional) The rule version.
        :param str account_id: (optional) The rule account ID.
        :param str created_on: (optional) The date when the rule was created.
        :param str created_by: (optional) The ID of the user who created the rule.
        :param str updated_on: (optional) The date when the rule was updated.
        :param str updated_by: (optional) The ID of the user who updated the rule.
        :param List[str] labels: (optional) The rule labels.
        """
        self.id = id
        self.type = type
        self.description = description
        self.version = version
        self.account_id = account_id
        self.created_on = created_on
        self.created_by = created_by
        self.updated_on = updated_on
        self.updated_by = updated_by
        self.labels = labels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleInfo':
        """Initialize a RuleInfo object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RulesPageBase:
    """
    Page common fields.

    :attr int limit: The requested page limit.
    :attr int total_count: The total number of resources in the collection.
    :attr PageHRefFirst first: A page reference.
    :attr PageHRefNext next: (optional) A page reference.
    :attr List[Rule] rules: (optional) The collection of rules that correspond to an
          account instance. Maximum of 100/500 custom rules per stand-alone/enterprise
          account.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        first: 'PageHRefFirst',
        *,
        next: 'PageHRefNext' = None,
        rules: List['Rule'] = None,
    ) -> None:
        """
        Initialize a RulesPageBase object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources in the collection.
        :param PageHRefFirst first: A page reference.
        :param PageHRefNext next: (optional) A page reference.
        :param List[Rule] rules: (optional) The collection of rules that correspond
               to an account instance. Maximum of 100/500 custom rules per
               stand-alone/enterprise account.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RulesPageBase':
        """Initialize a RulesPageBase object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in RulesPageBase JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in RulesPageBase JSON')
        if 'first' in _dict:
            args['first'] = PageHRefFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in RulesPageBase JSON')
        if 'next' in _dict:
            args['next'] = PageHRefNext.from_dict(_dict.get('next'))
        if 'rules' in _dict:
            args['rules'] = [Rule.from_dict(v) for v in _dict.get('rules')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RulesPageBase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'rules') and self.rules is not None:
            rules_list = []
            for v in self.rules:
                if isinstance(v, dict):
                    rules_list.append(v)
                else:
                    rules_list.append(v.to_dict())
            _dict['rules'] = rules_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RulesPageBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RulesPageBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RulesPageBase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Scan:
    """
    The response schema for creating a scan.

    :attr str id: (optional) The scan ID.
    :attr str account_id: (optional) The account ID.
    :attr str attachment_id: (optional) The attachment ID of a profile.
    :attr str report_id: (optional) The report ID.
    :attr str status: (optional) The status of the scan.
    :attr str last_scan_time: (optional) The last scan time.
    :attr str next_scan_time: (optional) The next scan time.
    :attr str scan_type: (optional) The type of scan.
    :attr int occurence: (optional) The occurrence of the scan.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        attachment_id: str = None,
        report_id: str = None,
        status: str = None,
        last_scan_time: str = None,
        next_scan_time: str = None,
        scan_type: str = None,
        occurence: int = None,
    ) -> None:
        """
        Initialize a Scan object.

        :param str id: (optional) The scan ID.
        :param str account_id: (optional) The account ID.
        :param str attachment_id: (optional) The attachment ID of a profile.
        :param str report_id: (optional) The report ID.
        :param str status: (optional) The status of the scan.
        :param str last_scan_time: (optional) The last scan time.
        :param str next_scan_time: (optional) The next scan time.
        :param str scan_type: (optional) The type of scan.
        :param int occurence: (optional) The occurrence of the scan.
        """
        self.id = id
        self.account_id = account_id
        self.attachment_id = attachment_id
        self.report_id = report_id
        self.status = status
        self.last_scan_time = last_scan_time
        self.next_scan_time = next_scan_time
        self.scan_type = scan_type
        self.occurence = occurence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Scan':
        """Initialize a Scan object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'attachment_id' in _dict:
            args['attachment_id'] = _dict.get('attachment_id')
        if 'report_id' in _dict:
            args['report_id'] = _dict.get('report_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'last_scan_time' in _dict:
            args['last_scan_time'] = _dict.get('last_scan_time')
        if 'next_scan_time' in _dict:
            args['next_scan_time'] = _dict.get('next_scan_time')
        if 'scan_type' in _dict:
            args['scan_type'] = _dict.get('scan_type')
        if 'occurence' in _dict:
            args['occurence'] = _dict.get('occurence')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Scan object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'attachment_id') and self.attachment_id is not None:
            _dict['attachment_id'] = self.attachment_id
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'last_scan_time') and self.last_scan_time is not None:
            _dict['last_scan_time'] = self.last_scan_time
        if hasattr(self, 'next_scan_time') and self.next_scan_time is not None:
            _dict['next_scan_time'] = self.next_scan_time
        if hasattr(self, 'scan_type') and self.scan_type is not None:
            _dict['scan_type'] = self.scan_type
        if hasattr(self, 'occurence') and self.occurence is not None:
            _dict['occurence'] = self.occurence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Scan object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Scan') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Scan') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the scan.
        """

        COMPLETED = 'completed'
        IN_PROGRESS = 'in_progress'


    class ScanTypeEnum(str, Enum):
        """
        The type of scan.
        """

        ONDEMAND = 'ondemand'
        SCHEDULED = 'scheduled'



class ScopeProperty:
    """
    The properties that are supported for scoping by this attachment.

    :attr str name: (optional) The property name.
    :attr str value: (optional) The property value.
    """

    def __init__(
        self,
        *,
        name: str = None,
        value: str = None,
    ) -> None:
        """
        Initialize a ScopeProperty object.

        :param str name: (optional) The property name.
        :param str value: (optional) The property value.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopeProperty':
        """Initialize a ScopeProperty object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopeProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScopeProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopeProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopeProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Settings:
    """
    The settings.

    :attr EventNotifications event_notifications: (optional) The Event Notifications
          settings.
    :attr ObjectStorage object_storage: (optional) The Cloud Object Storage
          settings.
    """

    def __init__(
        self,
        *,
        event_notifications: 'EventNotifications' = None,
        object_storage: 'ObjectStorage' = None,
    ) -> None:
        """
        Initialize a Settings object.

        :param EventNotifications event_notifications: (optional) The Event
               Notifications settings.
        :param ObjectStorage object_storage: (optional) The Cloud Object Storage
               settings.
        """
        self.event_notifications = event_notifications
        self.object_storage = object_storage

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Settings':
        """Initialize a Settings object from a json dictionary."""
        args = {}
        if 'event_notifications' in _dict:
            args['event_notifications'] = EventNotifications.from_dict(_dict.get('event_notifications'))
        if 'object_storage' in _dict:
            args['object_storage'] = ObjectStorage.from_dict(_dict.get('object_storage'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Settings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event_notifications') and self.event_notifications is not None:
            if isinstance(self.event_notifications, dict):
                _dict['event_notifications'] = self.event_notifications
            else:
                _dict['event_notifications'] = self.event_notifications.to_dict()
        if hasattr(self, 'object_storage') and self.object_storage is not None:
            if isinstance(self.object_storage, dict):
                _dict['object_storage'] = self.object_storage
            else:
                _dict['object_storage'] = self.object_storage.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Settings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Settings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Settings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Tags:
    """
    The collection of different types of tags.

    :attr List[str] user: (optional) The collection of user tags.
    :attr List[str] access: (optional) The collection of access tags.
    :attr List[str] service: (optional) The collection of service tags.
    """

    def __init__(
        self,
        *,
        user: List[str] = None,
        access: List[str] = None,
        service: List[str] = None,
    ) -> None:
        """
        Initialize a Tags object.

        :param List[str] user: (optional) The collection of user tags.
        :param List[str] access: (optional) The collection of access tags.
        :param List[str] service: (optional) The collection of service tags.
        """
        self.user = user
        self.access = access
        self.service = service

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tags':
        """Initialize a Tags object from a json dictionary."""
        args = {}
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'access' in _dict:
            args['access'] = _dict.get('access')
        if 'service' in _dict:
            args['service'] = _dict.get('service')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tags object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'access') and self.access is not None:
            _dict['access'] = self.access
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tags object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tags') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tags') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Target:
    """
    The rule target.

    :attr str service_name: The target service name.
    :attr str service_display_name: (optional) The display name of the target
          service.
    :attr str resource_kind: The target resource kind.
    :attr List[AdditionalTargetAttribute] additional_target_attributes: (optional)
          The list of targets supported properties.
    """

    def __init__(
        self,
        service_name: str,
        resource_kind: str,
        *,
        service_display_name: str = None,
        additional_target_attributes: List['AdditionalTargetAttribute'] = None,
    ) -> None:
        """
        Initialize a Target object.

        :param str service_name: The target service name.
        :param str resource_kind: The target resource kind.
        :param str service_display_name: (optional) The display name of the target
               service.
        :param List[AdditionalTargetAttribute] additional_target_attributes:
               (optional) The list of targets supported properties.
        """
        self.service_name = service_name
        self.service_display_name = service_display_name
        self.resource_kind = resource_kind
        self.additional_target_attributes = additional_target_attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Target':
        """Initialize a Target object from a json dictionary."""
        args = {}
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        else:
            raise ValueError('Required property \'service_name\' not present in Target JSON')
        if 'service_display_name' in _dict:
            args['service_display_name'] = _dict.get('service_display_name')
        if 'resource_kind' in _dict:
            args['resource_kind'] = _dict.get('resource_kind')
        else:
            raise ValueError('Required property \'resource_kind\' not present in Target JSON')
        if 'additional_target_attributes' in _dict:
            args['additional_target_attributes'] = [AdditionalTargetAttribute.from_dict(v) for v in _dict.get('additional_target_attributes')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Target object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'service_display_name') and self.service_display_name is not None:
            _dict['service_display_name'] = self.service_display_name
        if hasattr(self, 'resource_kind') and self.resource_kind is not None:
            _dict['resource_kind'] = self.resource_kind
        if hasattr(self, 'additional_target_attributes') and self.additional_target_attributes is not None:
            additional_target_attributes_list = []
            for v in self.additional_target_attributes:
                if isinstance(v, dict):
                    additional_target_attributes_list.append(v)
                else:
                    additional_target_attributes_list.append(v.to_dict())
            _dict['additional_target_attributes'] = additional_target_attributes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Target object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Target') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Target') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetInfo:
    """
    The evaluation target.

    :attr str id: (optional) The target ID.
    :attr str account_id: (optional) The target account ID.
    :attr str resource_crn: (optional) The target resource CRN.
    :attr str resource_name: (optional) The target resource name.
    :attr str service_name: (optional) The target service name.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        resource_crn: str = None,
        resource_name: str = None,
        service_name: str = None,
    ) -> None:
        """
        Initialize a TargetInfo object.

        :param str id: (optional) The target ID.
        :param str account_id: (optional) The target account ID.
        :param str resource_crn: (optional) The target resource CRN.
        :param str resource_name: (optional) The target resource name.
        :param str service_name: (optional) The target service name.
        """
        self.id = id
        self.account_id = account_id
        self.resource_crn = resource_crn
        self.resource_name = resource_name
        self.service_name = service_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetInfo':
        """Initialize a TargetInfo object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'resource_crn' in _dict:
            args['resource_crn'] = _dict.get('resource_crn')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'resource_crn') and self.resource_crn is not None:
            _dict['resource_crn'] = self.resource_crn
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TestEvent:
    """
    The details of a test event response.

    :attr bool success: The indication of whether the event was received by Event
          Notifications.
    """

    def __init__(
        self,
        success: bool,
    ) -> None:
        """
        Initialize a TestEvent object.

        :param bool success: The indication of whether the event was received by
               Event Notifications.
        """
        self.success = success

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TestEvent':
        """Initialize a TestEvent object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in TestEvent JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TestEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TestEvent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TestEvent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TestEvent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigItemsRequiredConfigAnd(RequiredConfigItems):
    """
    RequiredConfigItemsRequiredConfigAnd.

    :attr str description: (optional) The required config description.
    :attr List[RequiredConfigItems] and_: (optional) The `AND` required
          configurations.
    """

    def __init__(
        self,
        *,
        description: str = None,
        and_: List['RequiredConfigItems'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigItemsRequiredConfigAnd object.

        :param str description: (optional) The required config description.
        :param List[RequiredConfigItems] and_: (optional) The `AND` required
               configurations.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.and_ = and_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigItemsRequiredConfigAnd':
        """Initialize a RequiredConfigItemsRequiredConfigAnd object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'and' in _dict:
            args['and_'] = _dict.get('and')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigItemsRequiredConfigAnd object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'and_') and self.and_ is not None:
            and_list = []
            for v in self.and_:
                if isinstance(v, dict):
                    and_list.append(v)
                else:
                    and_list.append(v.to_dict())
            _dict['and'] = and_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigItemsRequiredConfigAnd object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigItemsRequiredConfigAnd') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigItemsRequiredConfigAnd') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigItemsRequiredConfigBase(RequiredConfigItems):
    """
    The required configuration base object.

    :attr str description: (optional) The required config description.
    :attr str property: The property.
    :attr str operator: The operator.
    :attr object value: (optional) Schema for any JSON type.
    """

    def __init__(
        self,
        property: str,
        operator: str,
        *,
        description: str = None,
        value: object = None,
    ) -> None:
        """
        Initialize a RequiredConfigItemsRequiredConfigBase object.

        :param str property: The property.
        :param str operator: The operator.
        :param str description: (optional) The required config description.
        :param object value: (optional) Schema for any JSON type.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigItemsRequiredConfigBase':
        """Initialize a RequiredConfigItemsRequiredConfigBase object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'property' in _dict:
            args['property'] = _dict.get('property')
        else:
            raise ValueError('Required property \'property\' not present in RequiredConfigItemsRequiredConfigBase JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RequiredConfigItemsRequiredConfigBase JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigItemsRequiredConfigBase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigItemsRequiredConfigBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigItemsRequiredConfigBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigItemsRequiredConfigBase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator.
        """

        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        STRING_CONTAINS = 'string_contains'
        STRING_NOT_CONTAINS = 'string_not_contains'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        STRINGS_IN_LIST = 'strings_in_list'
        STRINGS_ALLOWED = 'strings_allowed'
        STRINGS_REQUIRED = 'strings_required'
        IPS_IN_RANGE = 'ips_in_range'
        IPS_EQUALS = 'ips_equals'
        IPS_NOT_EQUALS = 'ips_not_equals'
        DAYS_LESS_THAN = 'days_less_than'



class RequiredConfigItemsRequiredConfigOr(RequiredConfigItems):
    """
    The `OR` required configurations.

    :attr str description: (optional) The required config description.
    :attr List[RequiredConfigItems] or_: (optional) The `OR` required
          configurations.
    """

    def __init__(
        self,
        *,
        description: str = None,
        or_: List['RequiredConfigItems'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigItemsRequiredConfigOr object.

        :param str description: (optional) The required config description.
        :param List[RequiredConfigItems] or_: (optional) The `OR` required
               configurations.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.or_ = or_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigItemsRequiredConfigOr':
        """Initialize a RequiredConfigItemsRequiredConfigOr object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'or' in _dict:
            args['or_'] = _dict.get('or')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigItemsRequiredConfigOr object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'or_') and self.or_ is not None:
            or_list = []
            for v in self.or_:
                if isinstance(v, dict):
                    or_list.append(v)
                else:
                    or_list.append(v.to_dict())
            _dict['or'] = or_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigItemsRequiredConfigOr object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigItemsRequiredConfigOr') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigItemsRequiredConfigOr') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigRequiredConfigAnd(RequiredConfig):
    """
    RequiredConfigRequiredConfigAnd.

    :attr str description: (optional) The required config description.
    :attr List[RequiredConfigItems] and_: (optional) The `AND` required
          configurations.
    """

    def __init__(
        self,
        *,
        description: str = None,
        and_: List['RequiredConfigItems'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigRequiredConfigAnd object.

        :param str description: (optional) The required config description.
        :param List[RequiredConfigItems] and_: (optional) The `AND` required
               configurations.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.and_ = and_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigRequiredConfigAnd':
        """Initialize a RequiredConfigRequiredConfigAnd object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'and' in _dict:
            args['and_'] = _dict.get('and')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigRequiredConfigAnd object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'and_') and self.and_ is not None:
            and_list = []
            for v in self.and_:
                if isinstance(v, dict):
                    and_list.append(v)
                else:
                    and_list.append(v.to_dict())
            _dict['and'] = and_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigRequiredConfigAnd object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigRequiredConfigAnd') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigRequiredConfigAnd') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigRequiredConfigBase(RequiredConfig):
    """
    The required configuration base object.

    :attr str description: (optional) The required config description.
    :attr str property: The property.
    :attr str operator: The operator.
    :attr object value: (optional) Schema for any JSON type.
    """

    def __init__(
        self,
        property: str,
        operator: str,
        *,
        description: str = None,
        value: object = None,
    ) -> None:
        """
        Initialize a RequiredConfigRequiredConfigBase object.

        :param str property: The property.
        :param str operator: The operator.
        :param str description: (optional) The required config description.
        :param object value: (optional) Schema for any JSON type.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigRequiredConfigBase':
        """Initialize a RequiredConfigRequiredConfigBase object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'property' in _dict:
            args['property'] = _dict.get('property')
        else:
            raise ValueError('Required property \'property\' not present in RequiredConfigRequiredConfigBase JSON')
        if 'operator' in _dict:
            args['operator'] = _dict.get('operator')
        else:
            raise ValueError('Required property \'operator\' not present in RequiredConfigRequiredConfigBase JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigRequiredConfigBase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'property') and self.property is not None:
            _dict['property'] = self.property
        if hasattr(self, 'operator') and self.operator is not None:
            _dict['operator'] = self.operator
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigRequiredConfigBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigRequiredConfigBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigRequiredConfigBase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator.
        """

        STRING_EQUALS = 'string_equals'
        STRING_NOT_EQUALS = 'string_not_equals'
        STRING_MATCH = 'string_match'
        STRING_NOT_MATCH = 'string_not_match'
        STRING_CONTAINS = 'string_contains'
        STRING_NOT_CONTAINS = 'string_not_contains'
        NUM_EQUALS = 'num_equals'
        NUM_NOT_EQUALS = 'num_not_equals'
        NUM_LESS_THAN = 'num_less_than'
        NUM_LESS_THAN_EQUALS = 'num_less_than_equals'
        NUM_GREATER_THAN = 'num_greater_than'
        NUM_GREATER_THAN_EQUALS = 'num_greater_than_equals'
        IS_EMPTY = 'is_empty'
        IS_NOT_EMPTY = 'is_not_empty'
        IS_TRUE = 'is_true'
        IS_FALSE = 'is_false'
        STRINGS_IN_LIST = 'strings_in_list'
        STRINGS_ALLOWED = 'strings_allowed'
        STRINGS_REQUIRED = 'strings_required'
        IPS_IN_RANGE = 'ips_in_range'
        IPS_EQUALS = 'ips_equals'
        IPS_NOT_EQUALS = 'ips_not_equals'
        DAYS_LESS_THAN = 'days_less_than'



class RequiredConfigRequiredConfigOr(RequiredConfig):
    """
    The `OR` required configurations.

    :attr str description: (optional) The required config description.
    :attr List[RequiredConfigItems] or_: (optional) The `OR` required
          configurations.
    """

    def __init__(
        self,
        *,
        description: str = None,
        or_: List['RequiredConfigItems'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigRequiredConfigOr object.

        :param str description: (optional) The required config description.
        :param List[RequiredConfigItems] or_: (optional) The `OR` required
               configurations.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.or_ = or_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigRequiredConfigOr':
        """Initialize a RequiredConfigRequiredConfigOr object from a json dictionary."""
        args = {}
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'or' in _dict:
            args['or_'] = _dict.get('or')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigRequiredConfigOr object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'or_') and self.or_ is not None:
            or_list = []
            for v in self.or_:
                if isinstance(v, dict):
                    or_list.append(v)
                else:
                    or_list.append(v.to_dict())
            _dict['or'] = or_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigRequiredConfigOr object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigRequiredConfigOr') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigRequiredConfigOr') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

##############################################################################
# Pagers
##############################################################################


class ControlLibrariesPager:
    """
    ControlLibrariesPager can be used to simplify the use of the "list_control_libraries" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
        control_library_type: str = None,
    ) -> None:
        """
        Initialize a ControlLibrariesPager object.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The field that indicates how many resources to
               return, unless the response is the last page of resources.
        :param str control_library_type: (optional) The field that indicate how you
               want the resources to be filtered by.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._limit = limit
        self._control_library_type = control_library_type

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ControlLibraryItem.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_control_libraries(
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            limit=self._limit,
            control_library_type=self._control_library_type,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('control_libraries')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ControlLibraryItem.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ProfilesPager:
    """
    ProfilesPager can be used to simplify the use of the "list_profiles" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
        profile_type: str = None,
    ) -> None:
        """
        Initialize a ProfilesPager object.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request, and repeated in a response header for
               the corresponding response. The same value is used for downstream requests,
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str profile_type: (optional) The field that indicate how you want
               the resources to be filtered by.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._limit = limit
        self._profile_type = profile_type

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ProfileItem.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_profiles(
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            limit=self._limit,
            profile_type=self._profile_type,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('profiles')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ProfileItem.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class AttachmentsPager:
    """
    AttachmentsPager can be used to simplify the use of the "list_attachments" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        profile_id: str,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a AttachmentsPager object.
        :param str profile_id: The profile ID.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._profile_id = profile_id
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of AttachmentItem.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_attachments(
            profile_id=self._profile_id,
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('attachments')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of AttachmentItem.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class AttachmentsAccountPager:
    """
    AttachmentsAccountPager can be used to simplify the use of the "list_attachments_account" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        x_correlation_id: str = None,
        x_request_id: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a AttachmentsAccountPager object.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header for the
               corresponding response. The same value is not used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of AttachmentItem.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_attachments_account(
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('attachments')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of AttachmentItem.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ReportsPager:
    """
    ReportsPager can be used to simplify the use of the "list_reports" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        x_correlation_id: str = None,
        x_request_id: str = None,
        attachment_id: str = None,
        group_id: str = None,
        profile_id: str = None,
        type: str = None,
        limit: int = None,
        sort: str = None,
    ) -> None:
        """
        Initialize a ReportsPager object.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str attachment_id: (optional) The ID of the attachment.
        :param str group_id: (optional) The report group ID.
        :param str profile_id: (optional) The ID of the profile.
        :param str type: (optional) The type of the scan.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param str sort: (optional) This field sorts results by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._attachment_id = attachment_id
        self._group_id = group_id
        self._profile_id = profile_id
        self._type = type
        self._limit = limit
        self._sort = sort

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Report.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_reports(
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            attachment_id=self._attachment_id,
            group_id=self._group_id,
            profile_id=self._profile_id,
            type=self._type,
            limit=self._limit,
            sort=self._sort,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = get_query_param(next_page_link.get('href'), 'start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('reports')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Report.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ReportEvaluationsPager:
    """
    ReportEvaluationsPager can be used to simplify the use of the "list_report_evaluations" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        report_id: str,
        x_correlation_id: str = None,
        x_request_id: str = None,
        assessment_id: str = None,
        component_id: str = None,
        target_id: str = None,
        target_name: str = None,
        status: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a ReportEvaluationsPager object.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str assessment_id: (optional) The ID of the assessment.
        :param str component_id: (optional) The ID of component.
        :param str target_id: (optional) The ID of the evaluation target.
        :param str target_name: (optional) The name of the evaluation target.
        :param str status: (optional) The evaluation status value.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._report_id = report_id
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._assessment_id = assessment_id
        self._component_id = component_id
        self._target_id = target_id
        self._target_name = target_name
        self._status = status
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Evaluation.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_report_evaluations(
            report_id=self._report_id,
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            assessment_id=self._assessment_id,
            component_id=self._component_id,
            target_id=self._target_id,
            target_name=self._target_name,
            status=self._status,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = get_query_param(next_page_link.get('href'), 'start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('evaluations')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Evaluation.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ReportResourcesPager:
    """
    ReportResourcesPager can be used to simplify the use of the "list_report_resources" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        report_id: str,
        x_correlation_id: str = None,
        x_request_id: str = None,
        id: str = None,
        resource_name: str = None,
        account_id: str = None,
        component_id: str = None,
        status: str = None,
        sort: str = None,
        limit: int = None,
    ) -> None:
        """
        Initialize a ReportResourcesPager object.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str x_correlation_id: (optional) The supplied or generated value of
               this header is logged for a request and repeated in a response header for
               the corresponding response. The same value is used for downstream requests
               and retries of those requests. If a value of this header is not supplied in
               a request, the service generates a random (version 4) UUID.
        :param str x_request_id: (optional) The supplied or generated value of this
               header is logged for a request and repeated in a response header  for the
               corresponding response.  The same value is not used for downstream requests
               and retries of those requests.  If a value of this header is not supplied
               in a request, the service generates a random (version 4) UUID.
        :param str id: (optional) The ID of the resource.
        :param str resource_name: (optional) The name of the resource.
        :param str account_id: (optional) The ID of the account owning a resource.
        :param str component_id: (optional) The ID of component.
        :param str status: (optional) The compliance status value.
        :param str sort: (optional) This field sorts resources by using a valid
               sort field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._report_id = report_id
        self._x_correlation_id = x_correlation_id
        self._x_request_id = x_request_id
        self._id = id
        self._resource_name = resource_name
        self._account_id = account_id
        self._component_id = component_id
        self._status = status
        self._sort = sort
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Resource.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_report_resources(
            report_id=self._report_id,
            x_correlation_id=self._x_correlation_id,
            x_request_id=self._x_request_id,
            id=self._id,
            resource_name=self._resource_name,
            account_id=self._account_id,
            component_id=self._component_id,
            status=self._status,
            sort=self._sort,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = get_query_param(next_page_link.get('href'), 'start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('resources')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Resource.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
