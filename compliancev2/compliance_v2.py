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

# IBM OpenAPI SDK Code Generator Version: 3.72.0-5d70f2bb-20230511-203609

"""
The SCC Phoenix Compliance APIs.

API Version: 2.0.0
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class ComplianceV2(BaseService):
    """The Compliance V2 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'compliance'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'ComplianceV2':
        """
        Return a new client for the Compliance service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Compliance service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Profile APIs
    #########################

    def create_profile(
        self,
        instance_id: str,
        *,
        profile_name: str = None,
        profile_description: str = None,
        profile_type: str = None,
        profile_version: str = None,
        latest: bool = None,
        version_group_label: str = None,
        controls: List['ProfileControlsInRequest'] = None,
        default_parameters: List['DefaultParameters'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom profile.

        Create a user-defined custom profile.

        :param str instance_id: Instance id.
        :param str profile_name: (optional) Name of the Profile.
        :param str profile_description: (optional) Description of the profile.
        :param str profile_type: (optional) Type of the profile.
        :param str profile_version: (optional) Version of the profile.
        :param bool latest: (optional) If Latest is enabled or not.
        :param str version_group_label: (optional) The version group label of the
               profile.
        :param List[ProfileControlsInRequest] controls: (optional) Controls in the
               profile.
        :param List[DefaultParameters] default_parameters: (optional) default
               parameters of the profile.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if controls is not None:
            controls = [convert_model(x) for x in controls]
        if default_parameters is not None:
            default_parameters = [convert_model(x) for x in default_parameters]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_profile',
        )
        headers.update(sdk_headers)

        data = {
            'profile_name': profile_name,
            'profile_description': profile_description,
            'profile_type': profile_type,
            'profile_version': profile_version,
            'latest': latest,
            'version_group_label': version_group_label,
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_profiles(
        self,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all predefined and user's custom profiles.

        Get all predefined and user's custom profiles.

        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetAllProfilesRespBody` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_profiles',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def add_profile(
        self,
        profiles_id: str,
        instance_id: str,
        *,
        profile_name: str = None,
        profile_description: str = None,
        profile_type: str = None,
        profile_version: str = None,
        latest: bool = None,
        version_group_label: str = None,
        controls: List['ProfileControlsInRequest'] = None,
        default_parameters: List['DefaultParameters'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a custom profile.

        Update a user-defined custom profile.

        :param str profiles_id: The profile ID.
        :param str instance_id: Instance id.
        :param str profile_name: (optional) Name of the Profile.
        :param str profile_description: (optional) Description of the profile.
        :param str profile_type: (optional) Type of the profile.
        :param str profile_version: (optional) Version of the profile.
        :param bool latest: (optional) If Latest is enabled or not.
        :param str version_group_label: (optional) The version group label of the
               profile.
        :param List[ProfileControlsInRequest] controls: (optional) Controls in the
               profile.
        :param List[DefaultParameters] default_parameters: (optional) default
               parameters of the profile.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileResponse` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if controls is not None:
            controls = [convert_model(x) for x in controls]
        if default_parameters is not None:
            default_parameters = [convert_model(x) for x in default_parameters]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='add_profile',
        )
        headers.update(sdk_headers)

        data = {
            'profile_name': profile_name,
            'profile_description': profile_description,
            'profile_type': profile_type,
            'profile_version': profile_version,
            'latest': latest,
            'version_group_label': version_group_label,
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

        path_param_keys = ['profiles_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_profile(
        self,
        profiles_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a profile.

        Retrieve a profile by specifying the profile ID.

        :param str profiles_id: The profile ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileResponse` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_profile',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_profile(
        self,
        profiles_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom profile.

        Delete a custom profile by specifying the profile ID.

        :param str profiles_id: The profile ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileResponse` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_custom_profile',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile_parameters(
        self,
        profiles_id: str,
        instance_id: str,
        *,
        id: str = None,
        default_parameters: List['DefaultParameters'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update custom profile parameters.

        Update the parameters of a custom profile.

        :param str profiles_id: The profile ID.
        :param str instance_id: Instance id.
        :param str id: (optional) id of parameter.
        :param List[DefaultParameters] default_parameters: (optional) default
               parameters.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileDefaultParametersResponse` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if default_parameters is not None:
            default_parameters = [convert_model(x) for x in default_parameters]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_profile_parameters',
        )
        headers.update(sdk_headers)

        data = {
            'id': id,
            'default_parameters': default_parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/parameters'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Attachment APIs
    #########################

    def create_attachment(
        self,
        profiles_id: str,
        instance_id: str,
        *,
        attachments: List['AttachmentPayload'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an attachment.

        Create an attachment to link to a profile.

        :param str profiles_id: The profile ID.
        :param str instance_id: Instance id.
        :param List[AttachmentPayload] attachments: (optional) the attachments of a
               profile.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentProfileResponse` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if attachments is not None:
            attachments = [convert_model(x) for x in attachments]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_attachment',
        )
        headers.update(sdk_headers)

        data = {
            'attachments': attachments,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def check_profile_attachmnets(
        self,
        profiles_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all attachments.

        Retrieve all attachments that are linked to a profile.

        :param str profiles_id: The profile ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetAllAttachmnetsForProfileRespBody` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='check_profile_attachmnets',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_profile_attachmnet(
        self,
        profiles_id: str,
        attachment_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an attachment for a profile.

        Retrieve an attachment that is linked to a profile by specifying the attachment
        ID.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentPayload` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_profile_attachmnet',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile_attachment(
        self,
        profiles_id: str,
        attachment_id: str,
        instance_id: str,
        *,
        id: str = None,
        account_id: str = None,
        included_scope: 'ScopePayload' = None,
        exclusions: List['ScopePayload'] = None,
        created_by: str = None,
        created_on: str = None,
        updated_by: str = None,
        updated_on: str = None,
        status: str = None,
        attachment_parameters: List['ParameterDetails'] = None,
        attachment_notifications: 'AttachmentsNotificationsPayload' = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an attachment.

        Update an attachment that is linked to a profile.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str instance_id: Instance id.
        :param str id: (optional) attachment id.
        :param str account_id: (optional) account id.
        :param ScopePayload included_scope: (optional) scope payload.
        :param List[ScopePayload] exclusions: (optional) exclusions.
        :param str created_by: (optional) created by.
        :param str created_on: (optional) created on.
        :param str updated_by: (optional) updated by.
        :param str updated_on: (optional) updated on.
        :param str status: (optional) status.
        :param List[ParameterDetails] attachment_parameters: (optional) attachment
               parameters.
        :param AttachmentsNotificationsPayload attachment_notifications: (optional)
               payload of the attachments notifications.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentPayload` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if included_scope is not None:
            included_scope = convert_model(included_scope)
        if exclusions is not None:
            exclusions = [convert_model(x) for x in exclusions]
        if attachment_parameters is not None:
            attachment_parameters = [convert_model(x) for x in attachment_parameters]
        if attachment_notifications is not None:
            attachment_notifications = convert_model(attachment_notifications)
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_profile_attachment',
        )
        headers.update(sdk_headers)

        data = {
            'id': id,
            'account_id': account_id,
            'included_scope': included_scope,
            'exclusions': exclusions,
            'created_by': created_by,
            'created_on': created_on,
            'updated_by': updated_by,
            'updated_on': updated_on,
            'status': status,
            'attachment_parameters': attachment_parameters,
            'attachment_notifications': attachment_notifications,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_profile_attachmnet(
        self,
        profiles_id: str,
        attachment_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an attachment.

        Delete an attachment that is linked to a profile.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AttachmentPayload` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_profile_attachmnet',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_attachment_parameters(
        self,
        profiles_id: str,
        attachment_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get attachment's parameters.

        Get attachment's parameters.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ParameterDetails` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_attachment_parameters',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}/parameters'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_attachment(
        self,
        profiles_id: str,
        attachment_id: str,
        instance_id: str,
        *,
        parameter_name: str = None,
        parameter_display_name: str = None,
        parameter_type: str = None,
        parameter_value: str = None,
        assessment_type: str = None,
        assessment_id: str = None,
        parameters: List['ParameterInfo'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update parameters for an attachment.

        Update parameters for an attachment.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str instance_id: Instance id.
        :param str parameter_name: (optional) The name of the parameter.
        :param str parameter_display_name: (optional) The display name of the
               parameter.
        :param str parameter_type: (optional) the type of the parameter.
        :param str parameter_value: (optional) The value of the parameter.
        :param str assessment_type: (optional) The assessment type of the
               parameter.
        :param str assessment_id: (optional) The Assessment ID of the parameter.
        :param List[ParameterInfo] parameters: (optional) Parameters.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ParameterDetails` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if parameters is not None:
            parameters = [convert_model(x) for x in parameters]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_attachment',
        )
        headers.update(sdk_headers)

        data = {
            'parameter_name': parameter_name,
            'parameter_display_name': parameter_display_name,
            'parameter_type': parameter_type,
            'parameter_value': parameter_value,
            'assessment_type': assessment_type,
            'assessment_id': assessment_id,
            'parameters': parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}/parameters'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_parameters_by_name(
        self,
        profiles_id: str,
        attachment_id: str,
        parameter_name: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get parameters by name.

        Get parametes by name.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str parameter_name: The parameter name.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ParameterDetails` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not parameter_name:
            raise ValueError('parameter_name must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_parameters_by_name',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'parameter_name', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, parameter_name, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}/parameters/{parameter_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_attachmnet_parameters_by_name(
        self,
        profiles_id: str,
        attachment_id: str,
        parameter_name: str,
        instance_id: str,
        *,
        new_parameter_name: str = None,
        new_parameter_display_name: str = None,
        new_parameter_type: str = None,
        new_parameter_value: str = None,
        new_assessment_type: str = None,
        new_assessment_id: str = None,
        new_parameters: List['ParameterInfo'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update parameter by name.

        Update parameter by name.

        :param str profiles_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str parameter_name: The parameter name.
        :param str instance_id: Instance id.
        :param str new_parameter_name: (optional) The name of the parameter.
        :param str new_parameter_display_name: (optional) The display name of the
               parameter.
        :param str new_parameter_type: (optional) the type of the parameter.
        :param str new_parameter_value: (optional) The value of the parameter.
        :param str new_assessment_type: (optional) The assessment type of the
               parameter.
        :param str new_assessment_id: (optional) The Assessment ID of the
               parameter.
        :param List[ParameterInfo] new_parameters: (optional) Parameters.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ParameterDetails` object
        """

        if not profiles_id:
            raise ValueError('profiles_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if not parameter_name:
            raise ValueError('parameter_name must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if new_parameters is not None:
            new_parameters = [convert_model(x) for x in new_parameters]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_attachmnet_parameters_by_name',
        )
        headers.update(sdk_headers)

        data = {
            'parameter_name': new_parameter_name,
            'parameter_display_name': new_parameter_display_name,
            'parameter_type': new_parameter_type,
            'parameter_value': new_parameter_value,
            'assessment_type': new_assessment_type,
            'assessment_id': new_assessment_id,
            'parameters': new_parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['profiles_id', 'attachment_id', 'parameter_name', 'instance_id']
        path_param_values = self.encode_path_vars(profiles_id, attachment_id, parameter_name, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profiles_id}/attachments/{attachment_id}/parameters/{parameter_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Control Library APIs
    #########################

    def create_custom_control_library(
        self,
        instance_id: str,
        *,
        id: str = None,
        account_id: str = None,
        control_library_name: str = None,
        control_library_description: str = None,
        control_library_type: str = None,
        version_group_label: str = None,
        control_library_version: str = None,
        latest: bool = None,
        controls_count: int = None,
        controls: List['ControlsInControlLibRequestPayload'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom control library.

        Create a custom control library.

        :param str instance_id: Instance id.
        :param str id: (optional) Control Library ID.
        :param str account_id: (optional) Account ID.
        :param str control_library_name: (optional) Control Library name.
        :param str control_library_description: (optional) Control Library
               Description.
        :param str control_library_type: (optional) Control Library Type.
        :param str version_group_label: (optional) Version group label.
        :param str control_library_version: (optional) Control Library Version.
        :param bool latest: (optional) Latest.
        :param int controls_count: (optional) Number of controls.
        :param List[ControlsInControlLibRequestPayload] controls: (optional)
               Controls.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryRequest` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if controls is not None:
            controls = [convert_model(x) for x in controls]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_custom_control_library',
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
            'latest': latest,
            'controls_count': controls_count,
            'controls': controls,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_control_libraries(
        self,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all control libraries.

        Retrieve all the control libraries, including predefined and custom libraries.

        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetAllControlLibrariesRespBody` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_control_libraries',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries'.format(**path_param_dict)
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
        instance_id: str,
        *,
        id: str = None,
        account_id: str = None,
        control_library_name: str = None,
        control_library_description: str = None,
        control_library_type: str = None,
        version_group_label: str = None,
        control_library_version: str = None,
        latest: bool = None,
        controls_count: int = None,
        controls: List['ControlsInControlLibRequestPayload'] = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update custom control library.

        Update a custom control library by specifying the control library ID.

        :param str control_libraries_id: The control library ID.
        :param str instance_id: Instance id.
        :param str id: (optional) Control Library ID.
        :param str account_id: (optional) Account ID.
        :param str control_library_name: (optional) Control Library name.
        :param str control_library_description: (optional) Control Library
               Description.
        :param str control_library_type: (optional) Control Library Type.
        :param str version_group_label: (optional) Version group label.
        :param str control_library_version: (optional) Control Library Version.
        :param bool latest: (optional) Latest.
        :param int controls_count: (optional) Number of controls.
        :param List[ControlsInControlLibRequestPayload] controls: (optional)
               Controls.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryRequest` object
        """

        if not control_libraries_id:
            raise ValueError('control_libraries_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        if controls is not None:
            controls = [convert_model(x) for x in controls]
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
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
            'latest': latest,
            'controls_count': controls_count,
            'controls': controls,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['control_libraries_id', 'instance_id']
        path_param_values = self.encode_path_vars(control_libraries_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries/{control_libraries_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_control_library(
        self,
        control_libraries_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get control library by id.

        Get control library by id.

        :param str control_libraries_id: The control library ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryRequest` object
        """

        if not control_libraries_id:
            raise ValueError('control_libraries_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_control_library',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['control_libraries_id', 'instance_id']
        path_param_values = self.encode_path_vars(control_libraries_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries/{control_libraries_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_controllibrary(
        self,
        control_libraries_id: str,
        instance_id: str,
        *,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete custom control library.

        Delete custom control library.

        :param str control_libraries_id: The control library ID.
        :param str instance_id: Instance id.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryRequest` object
        """

        if not control_libraries_id:
            raise ValueError('control_libraries_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_custom_controllibrary',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['control_libraries_id', 'instance_id']
        path_param_values = self.encode_path_vars(control_libraries_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries/{control_libraries_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Scan API
    #########################

    def create_scan(
        self,
        instance_id: str,
        *,
        attachment_id: str = None,
        transaction_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a scan.

        Create a scan.

        :param str instance_id: Instance id.
        :param str attachment_id: (optional) Attachment ID.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateScanResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {
            'Transaction-Id': transaction_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scans'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AttachmentPayload:
    """
    The attachment details of a profile.

    :attr str id: (optional) attachment id.
    :attr str account_id: (optional) account id.
    :attr ScopePayload included_scope: (optional) scope payload.
    :attr List[ScopePayload] exclusions: (optional) exclusions.
    :attr str created_by: (optional) created by.
    :attr str created_on: (optional) created on.
    :attr str updated_by: (optional) updated by.
    :attr str updated_on: (optional) updated on.
    :attr str status: (optional) status.
    :attr List[ParameterDetails] attachment_parameters: (optional) attachment
          parameters.
    :attr AttachmentsNotificationsPayload attachment_notifications: (optional)
          payload of the attachments notifications.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        included_scope: 'ScopePayload' = None,
        exclusions: List['ScopePayload'] = None,
        created_by: str = None,
        created_on: str = None,
        updated_by: str = None,
        updated_on: str = None,
        status: str = None,
        attachment_parameters: List['ParameterDetails'] = None,
        attachment_notifications: 'AttachmentsNotificationsPayload' = None,
    ) -> None:
        """
        Initialize a AttachmentPayload object.

        :param str id: (optional) attachment id.
        :param str account_id: (optional) account id.
        :param ScopePayload included_scope: (optional) scope payload.
        :param List[ScopePayload] exclusions: (optional) exclusions.
        :param str created_by: (optional) created by.
        :param str created_on: (optional) created on.
        :param str updated_by: (optional) updated by.
        :param str updated_on: (optional) updated on.
        :param str status: (optional) status.
        :param List[ParameterDetails] attachment_parameters: (optional) attachment
               parameters.
        :param AttachmentsNotificationsPayload attachment_notifications: (optional)
               payload of the attachments notifications.
        """
        self.id = id
        self.account_id = account_id
        self.included_scope = included_scope
        self.exclusions = exclusions
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.status = status
        self.attachment_parameters = attachment_parameters
        self.attachment_notifications = attachment_notifications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentPayload':
        """Initialize a AttachmentPayload object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'included_scope' in _dict:
            args['included_scope'] = ScopePayload.from_dict(_dict.get('included_scope'))
        if 'exclusions' in _dict:
            args['exclusions'] = [ScopePayload.from_dict(v) for v in _dict.get('exclusions')]
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'attachment_parameters' in _dict:
            args['attachment_parameters'] = [ParameterDetails.from_dict(v) for v in _dict.get('attachment_parameters')]
        if 'attachment_notifications' in _dict:
            args['attachment_notifications'] = AttachmentsNotificationsPayload.from_dict(_dict.get('attachment_notifications'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentPayload object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'included_scope') and self.included_scope is not None:
            if isinstance(self.included_scope, dict):
                _dict['included_scope'] = self.included_scope
            else:
                _dict['included_scope'] = self.included_scope.to_dict()
        if hasattr(self, 'exclusions') and self.exclusions is not None:
            exclusions_list = []
            for v in self.exclusions:
                if isinstance(v, dict):
                    exclusions_list.append(v)
                else:
                    exclusions_list.append(v.to_dict())
            _dict['exclusions'] = exclusions_list
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'attachment_parameters') and self.attachment_parameters is not None:
            attachment_parameters_list = []
            for v in self.attachment_parameters:
                if isinstance(v, dict):
                    attachment_parameters_list.append(v)
                else:
                    attachment_parameters_list.append(v.to_dict())
            _dict['attachment_parameters'] = attachment_parameters_list
        if hasattr(self, 'attachment_notifications') and self.attachment_notifications is not None:
            if isinstance(self.attachment_notifications, dict):
                _dict['attachment_notifications'] = self.attachment_notifications
            else:
                _dict['attachment_notifications'] = self.attachment_notifications.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentPayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentPayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentPayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        status.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'



class AttachmentProfileRequest:
    """
    request body of attachments of a profile.

    :attr List[AttachmentPayload] attachments: (optional) the attachments of a
          profile.
    """

    def __init__(
        self,
        *,
        attachments: List['AttachmentPayload'] = None,
    ) -> None:
        """
        Initialize a AttachmentProfileRequest object.

        :param List[AttachmentPayload] attachments: (optional) the attachments of a
               profile.
        """
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentProfileRequest':
        """Initialize a AttachmentProfileRequest object from a json dictionary."""
        args = {}
        if 'attachments' in _dict:
            args['attachments'] = [AttachmentPayload.from_dict(v) for v in _dict.get('attachments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentProfileRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        """Return a `str` version of this AttachmentProfileRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentProfileRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentProfileRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentProfileResponse:
    """
    Response body for attachment profile.

    :attr str profile_id: (optional) Profile id.
    :attr List[AttachmentResponse] attachments: (optional) List of attachments.
    """

    def __init__(
        self,
        *,
        profile_id: str = None,
        attachments: List['AttachmentResponse'] = None,
    ) -> None:
        """
        Initialize a AttachmentProfileResponse object.

        :param str profile_id: (optional) Profile id.
        :param List[AttachmentResponse] attachments: (optional) List of
               attachments.
        """
        self.profile_id = profile_id
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentProfileResponse':
        """Initialize a AttachmentProfileResponse object from a json dictionary."""
        args = {}
        if 'profile_id' in _dict:
            args['profile_id'] = _dict.get('profile_id')
        if 'attachments' in _dict:
            args['attachments'] = [AttachmentResponse.from_dict(v) for v in _dict.get('attachments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentProfileResponse object from a json dictionary."""
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
        """Return a `str` version of this AttachmentProfileResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentProfileResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentProfileResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentResponse:
    """
    attachment details for profile.

    :attr str id: (optional) Attachment id.
    :attr str account_id: (optional) Account id.
    :attr ScopePayload included_scope: (optional) scope payload.
    :attr List[ScopePayload] exclusions: (optional) Excluded scopes.
    :attr str created_by: (optional) Created by.
    :attr str created_on: (optional) Created on.
    :attr str updated_by: (optional) Updated by.
    :attr str updated_on: (optional) Updated on.
    :attr str status: (optional) Status.
    :attr List[ParameterDetails] attachment_parameters: (optional) Attachment
          parameters.
    :attr str last_scan: (optional) Last scan id.
    :attr str last_scan_status: (optional) Last scan status.
    :attr str last_scan_time: (optional) Last scan time.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        included_scope: 'ScopePayload' = None,
        exclusions: List['ScopePayload'] = None,
        created_by: str = None,
        created_on: str = None,
        updated_by: str = None,
        updated_on: str = None,
        status: str = None,
        attachment_parameters: List['ParameterDetails'] = None,
        last_scan: str = None,
        last_scan_status: str = None,
        last_scan_time: str = None,
    ) -> None:
        """
        Initialize a AttachmentResponse object.

        :param str id: (optional) Attachment id.
        :param str account_id: (optional) Account id.
        :param ScopePayload included_scope: (optional) scope payload.
        :param List[ScopePayload] exclusions: (optional) Excluded scopes.
        :param str created_by: (optional) Created by.
        :param str created_on: (optional) Created on.
        :param str updated_by: (optional) Updated by.
        :param str updated_on: (optional) Updated on.
        :param str status: (optional) Status.
        :param List[ParameterDetails] attachment_parameters: (optional) Attachment
               parameters.
        :param str last_scan: (optional) Last scan id.
        :param str last_scan_status: (optional) Last scan status.
        :param str last_scan_time: (optional) Last scan time.
        """
        self.id = id
        self.account_id = account_id
        self.included_scope = included_scope
        self.exclusions = exclusions
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.status = status
        self.attachment_parameters = attachment_parameters
        self.last_scan = last_scan
        self.last_scan_status = last_scan_status
        self.last_scan_time = last_scan_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentResponse':
        """Initialize a AttachmentResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'included_scope' in _dict:
            args['included_scope'] = ScopePayload.from_dict(_dict.get('included_scope'))
        if 'exclusions' in _dict:
            args['exclusions'] = [ScopePayload.from_dict(v) for v in _dict.get('exclusions')]
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'attachment_parameters' in _dict:
            args['attachment_parameters'] = [ParameterDetails.from_dict(v) for v in _dict.get('attachment_parameters')]
        if 'last_scan' in _dict:
            args['last_scan'] = _dict.get('last_scan')
        if 'last_scan_status' in _dict:
            args['last_scan_status'] = _dict.get('last_scan_status')
        if 'last_scan_time' in _dict:
            args['last_scan_time'] = _dict.get('last_scan_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'included_scope') and self.included_scope is not None:
            if isinstance(self.included_scope, dict):
                _dict['included_scope'] = self.included_scope
            else:
                _dict['included_scope'] = self.included_scope.to_dict()
        if hasattr(self, 'exclusions') and self.exclusions is not None:
            exclusions_list = []
            for v in self.exclusions:
                if isinstance(v, dict):
                    exclusions_list.append(v)
                else:
                    exclusions_list.append(v.to_dict())
            _dict['exclusions'] = exclusions_list
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'attachment_parameters') and self.attachment_parameters is not None:
            attachment_parameters_list = []
            for v in self.attachment_parameters:
                if isinstance(v, dict):
                    attachment_parameters_list.append(v)
                else:
                    attachment_parameters_list.append(v.to_dict())
            _dict['attachment_parameters'] = attachment_parameters_list
        if hasattr(self, 'last_scan') and self.last_scan is not None:
            _dict['last_scan'] = self.last_scan
        if hasattr(self, 'last_scan_status') and self.last_scan_status is not None:
            _dict['last_scan_status'] = self.last_scan_status
        if hasattr(self, 'last_scan_time') and self.last_scan_time is not None:
            _dict['last_scan_time'] = self.last_scan_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AttachmentResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlDocs:
    """
    Control Docs.

    :attr str control_docs_id: (optional) ID of Control Docs.
    :attr str control_docs_type: (optional) Type of Control Docs.
    """

    def __init__(
        self,
        *,
        control_docs_id: str = None,
        control_docs_type: str = None,
    ) -> None:
        """
        Initialize a ControlDocs object.

        :param str control_docs_id: (optional) ID of Control Docs.
        :param str control_docs_type: (optional) Type of Control Docs.
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


class ControlLibraryListResponse:
    """
    ControlLibraryListResponse.

    :attr str id: (optional) The ID of the control library.
    :attr str account_id: (optional) Account ID.
    :attr str control_library_name: (optional) The Control Library Name.
    :attr str control_library_description: (optional) Control Library Description.
    :attr str control_library_type: (optional) Control Library Type.
    :attr str created_on: (optional) Created On.
    :attr str created_by: (optional) Created By.
    :attr str updated_on: (optional) Updated ON.
    :attr str updated_by: (optional) Updated By.
    :attr str version_group_label: (optional) Version Group Label.
    :attr str control_library_version: (optional) Control Library Version.
    :attr bool latest: (optional) Latest.
    :attr int controls_count: (optional) Number of controls.
    """

    def __init__(
        self,
        *,
        id: str = None,
        account_id: str = None,
        control_library_name: str = None,
        control_library_description: str = None,
        control_library_type: str = None,
        created_on: str = None,
        created_by: str = None,
        updated_on: str = None,
        updated_by: str = None,
        version_group_label: str = None,
        control_library_version: str = None,
        latest: bool = None,
        controls_count: int = None,
    ) -> None:
        """
        Initialize a ControlLibraryListResponse object.

        :param str id: (optional) The ID of the control library.
        :param str account_id: (optional) Account ID.
        :param str control_library_name: (optional) The Control Library Name.
        :param str control_library_description: (optional) Control Library
               Description.
        :param str control_library_type: (optional) Control Library Type.
        :param str created_on: (optional) Created On.
        :param str created_by: (optional) Created By.
        :param str updated_on: (optional) Updated ON.
        :param str updated_by: (optional) Updated By.
        :param str version_group_label: (optional) Version Group Label.
        :param str control_library_version: (optional) Control Library Version.
        :param bool latest: (optional) Latest.
        :param int controls_count: (optional) Number of controls.
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
    def from_dict(cls, _dict: Dict) -> 'ControlLibraryListResponse':
        """Initialize a ControlLibraryListResponse object from a json dictionary."""
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
            args['created_on'] = _dict.get('created_on')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
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
        """Initialize a ControlLibraryListResponse object from a json dictionary."""
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
            _dict['created_on'] = self.created_on
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
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
        """Return a `str` version of this ControlLibraryListResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlLibraryListResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlLibraryListResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlLibraryRequest:
    """
    Request payload of the Control Library.

    :attr str id: (optional) Control Library ID.
    :attr str account_id: (optional) Account ID.
    :attr str control_library_name: (optional) Control Library name.
    :attr str control_library_description: (optional) Control Library Description.
    :attr str control_library_type: (optional) Control Library Type.
    :attr str version_group_label: (optional) Version group label.
    :attr str control_library_version: (optional) Control Library Version.
    :attr bool latest: (optional) Latest.
    :attr int controls_count: (optional) Number of controls.
    :attr List[ControlsInControlLibRequestPayload] controls: (optional) Controls.
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
        latest: bool = None,
        controls_count: int = None,
        controls: List['ControlsInControlLibRequestPayload'] = None,
    ) -> None:
        """
        Initialize a ControlLibraryRequest object.

        :param str id: (optional) Control Library ID.
        :param str account_id: (optional) Account ID.
        :param str control_library_name: (optional) Control Library name.
        :param str control_library_description: (optional) Control Library
               Description.
        :param str control_library_type: (optional) Control Library Type.
        :param str version_group_label: (optional) Version group label.
        :param str control_library_version: (optional) Control Library Version.
        :param bool latest: (optional) Latest.
        :param int controls_count: (optional) Number of controls.
        :param List[ControlsInControlLibRequestPayload] controls: (optional)
               Controls.
        """
        self.id = id
        self.account_id = account_id
        self.control_library_name = control_library_name
        self.control_library_description = control_library_description
        self.control_library_type = control_library_type
        self.version_group_label = version_group_label
        self.control_library_version = control_library_version
        self.latest = latest
        self.controls_count = controls_count
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibraryRequest':
        """Initialize a ControlLibraryRequest object from a json dictionary."""
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
        if 'latest' in _dict:
            args['latest'] = _dict.get('latest')
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        if 'controls' in _dict:
            args['controls'] = [ControlsInControlLibRequestPayload.from_dict(v) for v in _dict.get('controls')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlLibraryRequest object from a json dictionary."""
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
        if hasattr(self, 'latest') and self.latest is not None:
            _dict['latest'] = self.latest
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
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
        """Return a `str` version of this ControlLibraryRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlLibraryRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlLibraryRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ControlLibraryTypeEnum(str, Enum):
        """
        Control Library Type.
        """

        PREDEFINED = 'predefined'
        CUSTOM = 'custom'



class ControlSpecifications:
    """
    The control specifications for a control library.

    :attr str id: (optional) Control Specification ID.
    :attr str responsibility: (optional) Responsibility.
    :attr str component_id: (optional) Component ID.
    :attr str environment: (optional) Environment of control specifications.
    :attr str description: (optional) Description of control specifications.
    :attr int assessments_count: (optional) Number of Assessment.
    :attr List[ImplementationPayload] assessments: (optional) Assessments.
    """

    def __init__(
        self,
        *,
        id: str = None,
        responsibility: str = None,
        component_id: str = None,
        environment: str = None,
        description: str = None,
        assessments_count: int = None,
        assessments: List['ImplementationPayload'] = None,
    ) -> None:
        """
        Initialize a ControlSpecifications object.

        :param str id: (optional) Control Specification ID.
        :param str responsibility: (optional) Responsibility.
        :param str component_id: (optional) Component ID.
        :param str environment: (optional) Environment of control specifications.
        :param str description: (optional) Description of control specifications.
        :param int assessments_count: (optional) Number of Assessment.
        :param List[ImplementationPayload] assessments: (optional) Assessments.
        """
        self.id = id
        self.responsibility = responsibility
        self.component_id = component_id
        self.environment = environment
        self.description = description
        self.assessments_count = assessments_count
        self.assessments = assessments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSpecifications':
        """Initialize a ControlSpecifications object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'responsibility' in _dict:
            args['responsibility'] = _dict.get('responsibility')
        if 'component_id' in _dict:
            args['component_id'] = _dict.get('component_id')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'assessments_count' in _dict:
            args['assessments_count'] = _dict.get('assessments_count')
        if 'assessments' in _dict:
            args['assessments'] = [ImplementationPayload.from_dict(v) for v in _dict.get('assessments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlSpecifications object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'responsibility') and self.responsibility is not None:
            _dict['responsibility'] = self.responsibility
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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
        Responsibility.
        """

        USER = 'user'



class ControlsInControlLibRequestPayload:
    """
    The control details of a control library.

    :attr str control_name: (optional) The ID of the control library that contains
          the profile.
    :attr str control_id: (optional) The control name.
    :attr str control_description: (optional) The control description.
    :attr str control_category: (optional) control category.
    :attr str control_parent: (optional) control parent.
    :attr str control_severity: (optional) Control severity.
    :attr List[str] control_tags: (optional) Control Tags.
    :attr List[ControlSpecifications] control_specifications: (optional) control
          specifications.
    :attr ControlDocs control_docs: (optional) Control Docs.
    :attr str status: (optional) Status.
    """

    def __init__(
        self,
        *,
        control_name: str = None,
        control_id: str = None,
        control_description: str = None,
        control_category: str = None,
        control_parent: str = None,
        control_severity: str = None,
        control_tags: List[str] = None,
        control_specifications: List['ControlSpecifications'] = None,
        control_docs: 'ControlDocs' = None,
        status: str = None,
    ) -> None:
        """
        Initialize a ControlsInControlLibRequestPayload object.

        :param str control_name: (optional) The ID of the control library that
               contains the profile.
        :param str control_id: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_category: (optional) control category.
        :param str control_parent: (optional) control parent.
        :param str control_severity: (optional) Control severity.
        :param List[str] control_tags: (optional) Control Tags.
        :param List[ControlSpecifications] control_specifications: (optional)
               control specifications.
        :param ControlDocs control_docs: (optional) Control Docs.
        :param str status: (optional) Status.
        """
        self.control_name = control_name
        self.control_id = control_id
        self.control_description = control_description
        self.control_category = control_category
        self.control_parent = control_parent
        self.control_severity = control_severity
        self.control_tags = control_tags
        self.control_specifications = control_specifications
        self.control_docs = control_docs
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlsInControlLibRequestPayload':
        """Initialize a ControlsInControlLibRequestPayload object from a json dictionary."""
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
        if 'control_severity' in _dict:
            args['control_severity'] = _dict.get('control_severity')
        if 'control_tags' in _dict:
            args['control_tags'] = _dict.get('control_tags')
        if 'control_specifications' in _dict:
            args['control_specifications'] = [ControlSpecifications.from_dict(v) for v in _dict.get('control_specifications')]
        if 'control_docs' in _dict:
            args['control_docs'] = ControlDocs.from_dict(_dict.get('control_docs'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlsInControlLibRequestPayload object from a json dictionary."""
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
        if hasattr(self, 'control_severity') and self.control_severity is not None:
            _dict['control_severity'] = self.control_severity
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
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlsInControlLibRequestPayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlsInControlLibRequestPayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlsInControlLibRequestPayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'



class CreateScanResponse:
    """
    Response schema for creating a scan.

    :attr str id: (optional) Scan ID.
    :attr str account_id: (optional) Account ID.
    :attr str attachment_id: (optional) Attachment ID.
    :attr str report_id: (optional) Report ID.
    :attr str status: (optional) Status.
    :attr str last_scan_time: (optional) Last Scan Time.
    :attr str next_scan_time: (optional) Next Scan Time.
    :attr str scan_type: (optional) Type of Scan.
    :attr int occurence: (optional) Occurance of Scan.
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
        Initialize a CreateScanResponse object.

        :param str id: (optional) Scan ID.
        :param str account_id: (optional) Account ID.
        :param str attachment_id: (optional) Attachment ID.
        :param str report_id: (optional) Report ID.
        :param str status: (optional) Status.
        :param str last_scan_time: (optional) Last Scan Time.
        :param str next_scan_time: (optional) Next Scan Time.
        :param str scan_type: (optional) Type of Scan.
        :param int occurence: (optional) Occurance of Scan.
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
    def from_dict(cls, _dict: Dict) -> 'CreateScanResponse':
        """Initialize a CreateScanResponse object from a json dictionary."""
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
        """Initialize a CreateScanResponse object from a json dictionary."""
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
        """Return a `str` version of this CreateScanResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateScanResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateScanResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefaultParameters:
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
        Initialize a DefaultParameters object.

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
    def from_dict(cls, _dict: Dict) -> 'DefaultParameters':
        """Initialize a DefaultParameters object from a json dictionary."""
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
        """Initialize a DefaultParameters object from a json dictionary."""
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
        """Return a `str` version of this DefaultParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ParameterTypeEnum(str, Enum):
        """
        The parameter type.
        """

        NUMERIC = 'numeric'
        STRING_LIST = 'string_list'



class ImplementationPayload:
    """
    The implementation details of a control library.

    :attr str assessment_id: (optional) Assessment ID.
    :attr str assessment_method: (optional) Method of Assessment.
    :attr str assessment_type: (optional) Type of Assessment.
    :attr str assessment_description: (optional) Description of Assessment.
    :attr int parameter_count: (optional) Parameter Count.
    :attr List[ParameterInfo] parameters: (optional) Parameters.
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
        Initialize a ImplementationPayload object.

        :param str assessment_id: (optional) Assessment ID.
        :param str assessment_method: (optional) Method of Assessment.
        :param str assessment_type: (optional) Type of Assessment.
        :param str assessment_description: (optional) Description of Assessment.
        :param int parameter_count: (optional) Parameter Count.
        :param List[ParameterInfo] parameters: (optional) Parameters.
        """
        self.assessment_id = assessment_id
        self.assessment_method = assessment_method
        self.assessment_type = assessment_type
        self.assessment_description = assessment_description
        self.parameter_count = parameter_count
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImplementationPayload':
        """Initialize a ImplementationPayload object from a json dictionary."""
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
        """Initialize a ImplementationPayload object from a json dictionary."""
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
        """Return a `str` version of this ImplementationPayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImplementationPayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImplementationPayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PageRefFirst:
    """
    Reference page first.

    :attr str href: (optional) Reference URL.
    """

    def __init__(
        self,
        *,
        href: str = None,
    ) -> None:
        """
        Initialize a PageRefFirst object.

        :param str href: (optional) Reference URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRefFirst':
        """Initialize a PageRefFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRefFirst object from a json dictionary."""
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
        """Return a `str` version of this PageRefFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRefFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRefFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PageRefNext:
    """
    Reference page next.

    :attr str href: (optional) Reference URL.
    :attr str start: (optional) Reference start.
    """

    def __init__(
        self,
        *,
        href: str = None,
        start: str = None,
    ) -> None:
        """
        Initialize a PageRefNext object.

        :param str href: (optional) Reference URL.
        :param str start: (optional) Reference start.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageRefNext':
        """Initialize a PageRefNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PageRefNext object from a json dictionary."""
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
        """Return a `str` version of this PageRefNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PageRefNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PageRefNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ParameterDetails:
    """
    The details of the parameter.

    :attr str parameter_name: (optional) The name of the parameter.
    :attr str parameter_display_name: (optional) The display name of the parameter.
    :attr str parameter_type: (optional) the type of the parameter.
    :attr str parameter_value: (optional) The value of the parameter.
    :attr str assessment_type: (optional) The assessment type of the parameter.
    :attr str assessment_id: (optional) The Assessment ID of the parameter.
    :attr List[ParameterInfo] parameters: (optional) Parameters.
    """

    def __init__(
        self,
        *,
        parameter_name: str = None,
        parameter_display_name: str = None,
        parameter_type: str = None,
        parameter_value: str = None,
        assessment_type: str = None,
        assessment_id: str = None,
        parameters: List['ParameterInfo'] = None,
    ) -> None:
        """
        Initialize a ParameterDetails object.

        :param str parameter_name: (optional) The name of the parameter.
        :param str parameter_display_name: (optional) The display name of the
               parameter.
        :param str parameter_type: (optional) the type of the parameter.
        :param str parameter_value: (optional) The value of the parameter.
        :param str assessment_type: (optional) The assessment type of the
               parameter.
        :param str assessment_id: (optional) The Assessment ID of the parameter.
        :param List[ParameterInfo] parameters: (optional) Parameters.
        """
        self.parameter_name = parameter_name
        self.parameter_display_name = parameter_display_name
        self.parameter_type = parameter_type
        self.parameter_value = parameter_value
        self.assessment_type = assessment_type
        self.assessment_id = assessment_id
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ParameterDetails':
        """Initialize a ParameterDetails object from a json dictionary."""
        args = {}
        if 'parameter_name' in _dict:
            args['parameter_name'] = _dict.get('parameter_name')
        if 'parameter_display_name' in _dict:
            args['parameter_display_name'] = _dict.get('parameter_display_name')
        if 'parameter_type' in _dict:
            args['parameter_type'] = _dict.get('parameter_type')
        if 'parameter_value' in _dict:
            args['parameter_value'] = _dict.get('parameter_value')
        if 'assessment_type' in _dict:
            args['assessment_type'] = _dict.get('assessment_type')
        if 'assessment_id' in _dict:
            args['assessment_id'] = _dict.get('assessment_id')
        if 'parameters' in _dict:
            args['parameters'] = [ParameterInfo.from_dict(v) for v in _dict.get('parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ParameterDetails object from a json dictionary."""
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
        if hasattr(self, 'assessment_type') and self.assessment_type is not None:
            _dict['assessment_type'] = self.assessment_type
        if hasattr(self, 'assessment_id') and self.assessment_id is not None:
            _dict['assessment_id'] = self.assessment_id
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
        """Return a `str` version of this ParameterDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ParameterDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ParameterDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ParameterTypeEnum(str, Enum):
        """
        the type of the parameter.
        """

        NUMERIC = 'numeric'
        STRING_LIST = 'string_list'



class ParameterInfo:
    """
    The parameters details.

    :attr str parameter_name: (optional) Parameter Name.
    :attr str parameter_display_name: (optional) Parameter Display Name.
    :attr str parameter_type: (optional) Parameter Type.
    """

    def __init__(
        self,
        *,
        parameter_name: str = None,
        parameter_display_name: str = None,
        parameter_type: str = None,
    ) -> None:
        """
        Initialize a ParameterInfo object.

        :param str parameter_name: (optional) Parameter Name.
        :param str parameter_display_name: (optional) Parameter Display Name.
        :param str parameter_type: (optional) Parameter Type.
        """
        self.parameter_name = parameter_name
        self.parameter_display_name = parameter_display_name
        self.parameter_type = parameter_type

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
        Parameter Type.
        """

        NUMERIC = 'numeric'
        STRING_LIST = 'string_list'



class ProfileControlsInRequest:
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
        Initialize a ProfileControlsInRequest object.

        :param str control_library_id: (optional) The ID of the control library
               that contains the profile.
        :param str control_id: (optional) The control ID.
        """
        self.control_library_id = control_library_id
        self.control_id = control_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileControlsInRequest':
        """Initialize a ProfileControlsInRequest object from a json dictionary."""
        args = {}
        if 'control_library_id' in _dict:
            args['control_library_id'] = _dict.get('control_library_id')
        if 'control_id' in _dict:
            args['control_id'] = _dict.get('control_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileControlsInRequest object from a json dictionary."""
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
        """Return a `str` version of this ProfileControlsInRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileControlsInRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileControlsInRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileControlsInResponse:
    """
    The control details for a profile.

    :attr str control_library_id: (optional) The ID of the control library that
          contains a profile.
    :attr str control_id: (optional) control id.
    :attr str control_library_version: (optional) control library version.
    :attr str control_name: (optional) The control name.
    :attr str control_description: (optional) The control description.
    :attr str control_severity: (optional) The control severity.
    :attr str control_category: (optional) The control category.
    :attr str control_parent: (optional) The control parent.
    :attr ControlDocs control_docs: (optional) Control Docs.
    :attr List[ControlSpecifications] control_specifications: (optional) control
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
        control_severity: str = None,
        control_category: str = None,
        control_parent: str = None,
        control_docs: 'ControlDocs' = None,
        control_specifications: List['ControlSpecifications'] = None,
    ) -> None:
        """
        Initialize a ProfileControlsInResponse object.

        :param str control_library_id: (optional) The ID of the control library
               that contains a profile.
        :param str control_id: (optional) control id.
        :param str control_library_version: (optional) control library version.
        :param str control_name: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_severity: (optional) The control severity.
        :param str control_category: (optional) The control category.
        :param str control_parent: (optional) The control parent.
        :param ControlDocs control_docs: (optional) Control Docs.
        :param List[ControlSpecifications] control_specifications: (optional)
               control specifications.
        """
        self.control_library_id = control_library_id
        self.control_id = control_id
        self.control_library_version = control_library_version
        self.control_name = control_name
        self.control_description = control_description
        self.control_severity = control_severity
        self.control_category = control_category
        self.control_parent = control_parent
        self.control_docs = control_docs
        self.control_specifications = control_specifications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileControlsInResponse':
        """Initialize a ProfileControlsInResponse object from a json dictionary."""
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
        if 'control_severity' in _dict:
            args['control_severity'] = _dict.get('control_severity')
        if 'control_category' in _dict:
            args['control_category'] = _dict.get('control_category')
        if 'control_parent' in _dict:
            args['control_parent'] = _dict.get('control_parent')
        if 'control_docs' in _dict:
            args['control_docs'] = ControlDocs.from_dict(_dict.get('control_docs'))
        if 'control_specifications' in _dict:
            args['control_specifications'] = [ControlSpecifications.from_dict(v) for v in _dict.get('control_specifications')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileControlsInResponse object from a json dictionary."""
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
        if hasattr(self, 'control_severity') and self.control_severity is not None:
            _dict['control_severity'] = self.control_severity
        if hasattr(self, 'control_category') and self.control_category is not None:
            _dict['control_category'] = self.control_category
        if hasattr(self, 'control_parent') and self.control_parent is not None:
            _dict['control_parent'] = self.control_parent
        if hasattr(self, 'control_docs') and self.control_docs is not None:
            if isinstance(self.control_docs, dict):
                _dict['control_docs'] = self.control_docs
            else:
                _dict['control_docs'] = self.control_docs.to_dict()
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
        """Return a `str` version of this ProfileControlsInResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileControlsInResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileControlsInResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileDefaultParametersResponse:
    """
    The default parameters of a profile.

    :attr str id: (optional) id of parameter.
    :attr List[DefaultParameters] default_parameters: (optional) default parameters.
    """

    def __init__(
        self,
        *,
        id: str = None,
        default_parameters: List['DefaultParameters'] = None,
    ) -> None:
        """
        Initialize a ProfileDefaultParametersResponse object.

        :param str id: (optional) id of parameter.
        :param List[DefaultParameters] default_parameters: (optional) default
               parameters.
        """
        self.id = id
        self.default_parameters = default_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileDefaultParametersResponse':
        """Initialize a ProfileDefaultParametersResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'default_parameters' in _dict:
            args['default_parameters'] = [DefaultParameters.from_dict(v) for v in _dict.get('default_parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileDefaultParametersResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
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
        """Return a `str` version of this ProfileDefaultParametersResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileDefaultParametersResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileDefaultParametersResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileResponse:
    """
    Response body of the Profile.

    :attr str id: (optional) Profile ID.
    :attr str profile_name: (optional) Profile name.
    :attr str profile_description: (optional) Profile Description.
    :attr str profile_type: (optional) Profile Type.
    :attr str profile_version: (optional) Profile Version.
    :attr str version_group_label: (optional) Version Group Label.
    :attr bool latest: (optional) Latest.
    :attr str created_by: (optional) Created By.
    :attr str created_on: (optional) Created On.
    :attr str updated_by: (optional) Updated by.
    :attr str updated_on: (optional) Updated On.
    :attr int controls_count: (optional) Number of Controls.
    :attr int attachments_count: (optional) Number of attachments.
    :attr List[ProfileControlsInResponse] controls: (optional) Control IDs.
    :attr List[DefaultParameters] default_parameters: (optional) The default
          parameters of a profile.
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
        created_on: str = None,
        updated_by: str = None,
        updated_on: str = None,
        controls_count: int = None,
        attachments_count: int = None,
        controls: List['ProfileControlsInResponse'] = None,
        default_parameters: List['DefaultParameters'] = None,
    ) -> None:
        """
        Initialize a ProfileResponse object.

        :param str id: (optional) Profile ID.
        :param str profile_name: (optional) Profile name.
        :param str profile_description: (optional) Profile Description.
        :param str profile_type: (optional) Profile Type.
        :param str profile_version: (optional) Profile Version.
        :param str version_group_label: (optional) Version Group Label.
        :param bool latest: (optional) Latest.
        :param str created_by: (optional) Created By.
        :param str created_on: (optional) Created On.
        :param str updated_by: (optional) Updated by.
        :param str updated_on: (optional) Updated On.
        :param int controls_count: (optional) Number of Controls.
        :param int attachments_count: (optional) Number of attachments.
        :param List[ProfileControlsInResponse] controls: (optional) Control IDs.
        :param List[DefaultParameters] default_parameters: (optional) The default
               parameters of a profile.
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
        self.controls = controls
        self.default_parameters = default_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileResponse':
        """Initialize a ProfileResponse object from a json dictionary."""
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
            args['created_on'] = _dict.get('created_on')
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        if 'attachments_count' in _dict:
            args['attachments_count'] = _dict.get('attachments_count')
        if 'controls' in _dict:
            args['controls'] = [ProfileControlsInResponse.from_dict(v) for v in _dict.get('controls')]
        if 'default_parameters' in _dict:
            args['default_parameters'] = [DefaultParameters.from_dict(v) for v in _dict.get('default_parameters')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileResponse object from a json dictionary."""
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
            _dict['created_on'] = self.created_on
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
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
        """Return a `str` version of this ProfileResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ScopePayload:
    """
    scope payload.

    :attr str scope_id: (optional) scope id.
    :attr str scope_type: (optional) Scope type.
    """

    def __init__(
        self,
        *,
        scope_id: str = None,
        scope_type: str = None,
    ) -> None:
        """
        Initialize a ScopePayload object.

        :param str scope_id: (optional) scope id.
        :param str scope_type: (optional) Scope type.
        """
        self.scope_id = scope_id
        self.scope_type = scope_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopePayload':
        """Initialize a ScopePayload object from a json dictionary."""
        args = {}
        if 'scope_id' in _dict:
            args['scope_id'] = _dict.get('scope_id')
        if 'scope_type' in _dict:
            args['scope_type'] = _dict.get('scope_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopePayload object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scope_id') and self.scope_id is not None:
            _dict['scope_id'] = self.scope_id
        if hasattr(self, 'scope_type') and self.scope_type is not None:
            _dict['scope_type'] = self.scope_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScopePayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopePayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopePayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentsNotificationsPayload:
    """
    payload of the attachments notifications.

    :attr bool enabled: (optional) enabled notifications.
    :attr FailedControls controls: (optional) failed controls.
    """

    def __init__(
        self,
        *,
        enabled: bool = None,
        controls: 'FailedControls' = None,
    ) -> None:
        """
        Initialize a AttachmentsNotificationsPayload object.

        :param bool enabled: (optional) enabled notifications.
        :param FailedControls controls: (optional) failed controls.
        """
        self.enabled = enabled
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentsNotificationsPayload':
        """Initialize a AttachmentsNotificationsPayload object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'controls' in _dict:
            args['controls'] = FailedControls.from_dict(_dict.get('controls'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentsNotificationsPayload object from a json dictionary."""
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
        """Return a `str` version of this AttachmentsNotificationsPayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentsNotificationsPayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentsNotificationsPayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FailedControls:
    """
    failed controls.

    :attr int threshold_limit: (optional) threshold limit.
    :attr List[str] failed_control_ids: (optional) failed control ids.
    """

    def __init__(
        self,
        *,
        threshold_limit: int = None,
        failed_control_ids: List[str] = None,
    ) -> None:
        """
        Initialize a FailedControls object.

        :param int threshold_limit: (optional) threshold limit.
        :param List[str] failed_control_ids: (optional) failed control ids.
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


class GetAllAttachmnetsForProfileRespBody:
    """
    All the attachments present in a profile.

    :attr int total_count: (optional) Number of attachments.
    :attr int limit: (optional) Limit on Attachments.
    :attr PageRefFirst first: (optional) Reference page first.
    :attr PageRefNext next: (optional) Reference page next.
    :attr str profile_id: (optional) Profile ID.
    :attr str account_id: (optional) Account ID.
    :attr List[ControlLibraryListResponse] control_libraries: (optional) The Control
          Library ID.
    :attr List[AttachmentProfileRequest] attachments: (optional) the attachments of
          a profile.
    """

    def __init__(
        self,
        *,
        total_count: int = None,
        limit: int = None,
        first: 'PageRefFirst' = None,
        next: 'PageRefNext' = None,
        profile_id: str = None,
        account_id: str = None,
        control_libraries: List['ControlLibraryListResponse'] = None,
        attachments: List['AttachmentProfileRequest'] = None,
    ) -> None:
        """
        Initialize a GetAllAttachmnetsForProfileRespBody object.

        :param int total_count: (optional) Number of attachments.
        :param int limit: (optional) Limit on Attachments.
        :param PageRefFirst first: (optional) Reference page first.
        :param PageRefNext next: (optional) Reference page next.
        :param str profile_id: (optional) Profile ID.
        :param str account_id: (optional) Account ID.
        :param List[ControlLibraryListResponse] control_libraries: (optional) The
               Control Library ID.
        :param List[AttachmentProfileRequest] attachments: (optional) the
               attachments of a profile.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.next = next
        self.profile_id = profile_id
        self.account_id = account_id
        self.control_libraries = control_libraries
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAllAttachmnetsForProfileRespBody':
        """Initialize a GetAllAttachmnetsForProfileRespBody object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first' in _dict:
            args['first'] = PageRefFirst.from_dict(_dict.get('first'))
        if 'next' in _dict:
            args['next'] = PageRefNext.from_dict(_dict.get('next'))
        if 'profile_id' in _dict:
            args['profile_id'] = _dict.get('profile_id')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'control_libraries' in _dict:
            args['control_libraries'] = [ControlLibraryListResponse.from_dict(v) for v in _dict.get('control_libraries')]
        if 'attachments' in _dict:
            args['attachments'] = [AttachmentProfileRequest.from_dict(v) for v in _dict.get('attachments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAllAttachmnetsForProfileRespBody object from a json dictionary."""
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
        if hasattr(self, 'profile_id') and self.profile_id is not None:
            _dict['profile_id'] = self.profile_id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'control_libraries') and self.control_libraries is not None:
            control_libraries_list = []
            for v in self.control_libraries:
                if isinstance(v, dict):
                    control_libraries_list.append(v)
                else:
                    control_libraries_list.append(v.to_dict())
            _dict['control_libraries'] = control_libraries_list
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
        """Return a `str` version of this GetAllAttachmnetsForProfileRespBody object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAllAttachmnetsForProfileRespBody') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAllAttachmnetsForProfileRespBody') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetAllControlLibrariesRespBody:
    """
    response body of control libraries.

    :attr int total_count: (optional) number of control libraries.
    :attr int limit: (optional) limit.
    :attr PageRefFirst first: (optional) Reference page first.
    :attr PageRefNext next: (optional) Reference page next.
    :attr List[ControlLibraryListResponse] control_libraries: (optional) control
          libraries.
    """

    def __init__(
        self,
        *,
        total_count: int = None,
        limit: int = None,
        first: 'PageRefFirst' = None,
        next: 'PageRefNext' = None,
        control_libraries: List['ControlLibraryListResponse'] = None,
    ) -> None:
        """
        Initialize a GetAllControlLibrariesRespBody object.

        :param int total_count: (optional) number of control libraries.
        :param int limit: (optional) limit.
        :param PageRefFirst first: (optional) Reference page first.
        :param PageRefNext next: (optional) Reference page next.
        :param List[ControlLibraryListResponse] control_libraries: (optional)
               control libraries.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.next = next
        self.control_libraries = control_libraries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAllControlLibrariesRespBody':
        """Initialize a GetAllControlLibrariesRespBody object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first' in _dict:
            args['first'] = PageRefFirst.from_dict(_dict.get('first'))
        if 'next' in _dict:
            args['next'] = PageRefNext.from_dict(_dict.get('next'))
        if 'control_libraries' in _dict:
            args['control_libraries'] = [ControlLibraryListResponse.from_dict(v) for v in _dict.get('control_libraries')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAllControlLibrariesRespBody object from a json dictionary."""
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
        """Return a `str` version of this GetAllControlLibrariesRespBody object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAllControlLibrariesRespBody') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAllControlLibrariesRespBody') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GetAllProfilesRespBody:
    """
    Response body of get All profiles.

    :attr int total_count: (optional) Number of profiles.
    :attr int limit: (optional) limit.
    :attr PageRefFirst first: (optional) Reference page first.
    :attr PageRefNext next: (optional) Reference page next.
    :attr List[ListProfilesResponseStructure] profiles: (optional) Profiles.
    """

    def __init__(
        self,
        *,
        total_count: int = None,
        limit: int = None,
        first: 'PageRefFirst' = None,
        next: 'PageRefNext' = None,
        profiles: List['ListProfilesResponseStructure'] = None,
    ) -> None:
        """
        Initialize a GetAllProfilesRespBody object.

        :param int total_count: (optional) Number of profiles.
        :param int limit: (optional) limit.
        :param PageRefFirst first: (optional) Reference page first.
        :param PageRefNext next: (optional) Reference page next.
        :param List[ListProfilesResponseStructure] profiles: (optional) Profiles.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.next = next
        self.profiles = profiles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetAllProfilesRespBody':
        """Initialize a GetAllProfilesRespBody object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'first' in _dict:
            args['first'] = PageRefFirst.from_dict(_dict.get('first'))
        if 'next' in _dict:
            args['next'] = PageRefNext.from_dict(_dict.get('next'))
        if 'profiles' in _dict:
            args['profiles'] = [ListProfilesResponseStructure.from_dict(v) for v in _dict.get('profiles')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetAllProfilesRespBody object from a json dictionary."""
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
        """Return a `str` version of this GetAllProfilesRespBody object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetAllProfilesRespBody') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetAllProfilesRespBody') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListProfilesResponseStructure:
    """
    ListProfilesResponseStructure.

    :attr str id: (optional) id of the profile.
    :attr str profile_name: (optional) name of the profile.
    :attr str profile_description: (optional) description of the profile.
    :attr str profile_type: (optional) type of the profile.
    :attr str profile_version: (optional) version of the profile.
    :attr str version_group_label: (optional) version group label.
    :attr bool latest: (optional) latest.
    :attr str created_by: (optional) created by.
    :attr str created_on: (optional) created on.
    :attr str updated_by: (optional) updated by.
    :attr str updated_on: (optional) updated on.
    :attr int controls_count: (optional) No of controls.
    :attr int attachments_count: (optional) No of attachments.
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
        created_on: str = None,
        updated_by: str = None,
        updated_on: str = None,
        controls_count: int = None,
        attachments_count: int = None,
    ) -> None:
        """
        Initialize a ListProfilesResponseStructure object.

        :param str id: (optional) id of the profile.
        :param str profile_name: (optional) name of the profile.
        :param str profile_description: (optional) description of the profile.
        :param str profile_type: (optional) type of the profile.
        :param str profile_version: (optional) version of the profile.
        :param str version_group_label: (optional) version group label.
        :param bool latest: (optional) latest.
        :param str created_by: (optional) created by.
        :param str created_on: (optional) created on.
        :param str updated_by: (optional) updated by.
        :param str updated_on: (optional) updated on.
        :param int controls_count: (optional) No of controls.
        :param int attachments_count: (optional) No of attachments.
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
    def from_dict(cls, _dict: Dict) -> 'ListProfilesResponseStructure':
        """Initialize a ListProfilesResponseStructure object from a json dictionary."""
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
            args['created_on'] = _dict.get('created_on')
        if 'updated_by' in _dict:
            args['updated_by'] = _dict.get('updated_by')
        if 'updated_on' in _dict:
            args['updated_on'] = _dict.get('updated_on')
        if 'controls_count' in _dict:
            args['controls_count'] = _dict.get('controls_count')
        if 'attachments_count' in _dict:
            args['attachments_count'] = _dict.get('attachments_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListProfilesResponseStructure object from a json dictionary."""
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
            _dict['created_on'] = self.created_on
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = self.updated_on
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
        if hasattr(self, 'attachments_count') and self.attachments_count is not None:
            _dict['attachments_count'] = self.attachments_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListProfilesResponseStructure object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListProfilesResponseStructure') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListProfilesResponseStructure') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
