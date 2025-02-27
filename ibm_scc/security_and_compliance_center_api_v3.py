# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.98.0-8be2046a-20241205-162752

"""
The Security and Compliance Center API reference.

"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class SecurityAndComplianceCenterApiV3(BaseService):
    """The Security and Compliance Center API V3 service."""

    DEFAULT_SERVICE_URL = 'https://us-south.compliance.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'security_and_compliance_center_api'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://us-south.compliance.cloud.ibm.com', # Dallas region
        'eu-de': 'https://eu-de.compliance.cloud.ibm.com', # Frankfurt region
        'eu-fr2': 'https://eu-fr2.compliance.cloud.ibm.com', # Frankfurt region(Restricted)
        'ca-tor': 'https://ca-tor.compliance.cloud.ibm.com', # Toronto region
        'au-syd': 'https://au-syd.compliance.cloud.ibm.com', # Sydney region
        'eu-es': 'https://eu-es.compliance.cloud.ibm.com', # Madrid region
    }

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
    def get_service_url_for_region(
        cls,
        region: str,
    ) -> str:
        """
        Returns the service URL associated with the specified region.
        :param str region: a string representing the region
        :return: The service URL associated with the specified region or None
                 if no mapping for the region exists
        :rtype: str
        """
        return cls.REGIONAL_ENDPOINTS.get(region, None)

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
    # attachment
    #########################

    def list_instance_attachments(
        self,
        instance_id: str,
        *,
        account_id: Optional[str] = None,
        version_group_label: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        direction: Optional[str] = None,
        start: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all instance attachments.

        Retrieve all instance attachments.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str account_id: (optional) The user account ID.
        :param str version_group_label: (optional) The profile version group label.
        :param int limit: (optional) The number of items that are retrieved in a
               collection.
        :param str sort: (optional) The sorted collection of attachments. The
               available values are `created_on` and `scope_type`.
        :param str direction: (optional) The collection of attachments that is
               sorted in ascending order. To sort the collection in descending order, use
               the `DESC` schema.
        :param str start: (optional) The reference to the first item in the results
               page. Take the value from the `next` field that is in the response from the
               previous page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachmentCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_instance_attachments',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
            'version_group_label': version_group_label,
            'limit': limit,
            'sort': sort,
            'direction': direction,
            'start': start,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_profile_attachment(
        self,
        instance_id: str,
        profile_id: str,
        attachments: List['ProfileAttachmentBase'],
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an attachment.

        Create an attachment to link to a profile.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param List[ProfileAttachmentBase] attachments: The Prototype to create a
               profile attachment.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachmentResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if attachments is None:
            raise ValueError('attachments must be provided')
        attachments = [convert_model(x) for x in attachments]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_profile_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

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

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_profile_attachment(
        self,
        instance_id: str,
        profile_id: str,
        attachment_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an attachment.

        Retrieve an attachment that is linked to a profile by specifying the attachment
        ID.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachment` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_profile_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id', 'attachment_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile_attachment(
        self,
        instance_id: str,
        profile_id: str,
        attachment_id: str,
        attachments: List['ProfileAttachmentBase'],
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an attachment.

        Update an attachment that is linked to a profile.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param List[ProfileAttachmentBase] attachments: The Prototype to create a
               profile attachment.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachment` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if attachments is None:
            raise ValueError('attachments must be provided')
        attachments = [convert_model(x) for x in attachments]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_profile_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

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

        path_param_keys = ['instance_id', 'profile_id', 'attachment_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_profile_attachment(
        self,
        instance_id: str,
        profile_id: str,
        attachment_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an attachment.

        Delete an attachment that is linked to a profile.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachment` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_profile_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id', 'attachment_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/attachments/{attachment_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def upgrade_attachment(
        self,
        instance_id: str,
        profile_id: str,
        attachment_id: str,
        attachment_parameters: List['Parameter'],
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Upgrade an attachment.

        Upgrade an attachment to the latest version of a profile.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str attachment_id: The attachment ID.
        :param List[Parameter] attachment_parameters: The attachment_parameters to
               set for a Profile Attachment.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachment` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if not attachment_id:
            raise ValueError('attachment_id must be provided')
        if attachment_parameters is None:
            raise ValueError('attachment_parameters must be provided')
        attachment_parameters = [convert_model(x) for x in attachment_parameters]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='upgrade_attachment',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'attachment_parameters': attachment_parameters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id', 'attachment_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id, attachment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/attachments/{attachment_id}/upgrade'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_scan(
        self,
        instance_id: str,
        *,
        attachment_id: Optional[str] = None,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a scan.

        Create a scan to evaluate your resources.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule. If your attachment exists, but you don't want to wait for the
        next  scan to see your posture, you can initiate an on-demand scan. For more
        information, see [Running a scan on
        demand](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources#scan-ondemand-api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str attachment_id: (optional) The ID of the profile attachment.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateScanResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_scan',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

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
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # controlLibrary
    #########################

    def create_custom_control_library(
        self,
        instance_id: str,
        control_library_name: str,
        control_library_description: str,
        control_library_type: str,
        control_library_version: str,
        controls: List['ControlPrototype'],
        *,
        account_id: Optional[str] = None,
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
        libraries](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-custom-library).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str control_library_name: The name of the control library.
        :param str control_library_description: Details of the control library.
        :param str control_library_type: Details that the control library is a user
               made(custom) or Security Compliance Center(predefined).
        :param str control_library_version: The revision number of the control
               library.
        :param List[ControlPrototype] controls: The list of rules that the control
               library attempts to adhere to.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if control_library_name is None:
            raise ValueError('control_library_name must be provided')
        if control_library_description is None:
            raise ValueError('control_library_description must be provided')
        if control_library_type is None:
            raise ValueError('control_library_type must be provided')
        if control_library_version is None:
            raise ValueError('control_library_version must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        controls = [convert_model(x) for x in controls]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_custom_control_library',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'control_library_name': control_library_name,
            'control_library_description': control_library_description,
            'control_library_type': control_library_type,
            'control_library_version': control_library_version,
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
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_control_libraries(
        self,
        instance_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all control libraries.

        Retrieve all the control libraries, including predefined, and custom libraries.
        With Security and Compliance Center, you can create a custom control library that
        is specific to your organization's needs.  You define the controls and
        specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. A specification is
        a defined requirement that is specific to a component. An assessment, or several,
        are mapped to each specification with a detailed evaluation that is done to check
        whether the specification is compliant. For more information, see [Creating custom
        libraries](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-custom-library).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibraryCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_control_libraries',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

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
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_custom_control_library(
        self,
        instance_id: str,
        control_library_id: str,
        control_library_name: str,
        control_library_description: str,
        control_library_type: str,
        control_library_version: str,
        controls: List['ControlPrototype'],
        *,
        bss_account: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a custom control library.

        Update a custom control library by specifying its ID.
        With Security and Compliance Center, you can create a custom control library that
        is specific to your organization's needs.  You define the controls and
        specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. A specification is
        a defined requirement that is specific to a component. An assessment, or several,
        are mapped to each specification with a detailed evaluation that is done to check
        whether the specification is compliant. For more information, see [Creating custom
        libraries](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-custom-library).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str control_library_id: The predefined control library ID.
        :param str control_library_name: The name of the control library.
        :param str control_library_description: Details of the control library.
        :param str control_library_type: Details that the control library is a user
               made(custom) or Security Compliance Center(predefined).
        :param str control_library_version: The revision number of the control
               library.
        :param List[ControlPrototype] controls: The list of rules that the control
               library attempts to adhere to.
        :param str bss_account: (optional) The account id tied to billing.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not control_library_id:
            raise ValueError('control_library_id must be provided')
        if control_library_name is None:
            raise ValueError('control_library_name must be provided')
        if control_library_description is None:
            raise ValueError('control_library_description must be provided')
        if control_library_type is None:
            raise ValueError('control_library_type must be provided')
        if control_library_version is None:
            raise ValueError('control_library_version must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        controls = [convert_model(x) for x in controls]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_custom_control_library',
        )
        headers.update(sdk_headers)

        params = {
            'bss_account': bss_account,
        }

        data = {
            'control_library_name': control_library_name,
            'control_library_description': control_library_description,
            'control_library_type': control_library_type,
            'control_library_version': control_library_version,
            'controls': controls,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'control_library_id']
        path_param_values = self.encode_path_vars(instance_id, control_library_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries/{control_library_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_control_library(
        self,
        instance_id: str,
        control_library_id: str,
        *,
        account_id: Optional[str] = None,
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
        libraries](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-custom-library).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str control_library_id: The predefined control library ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not control_library_id:
            raise ValueError('control_library_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_control_library',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'control_library_id']
        path_param_values = self.encode_path_vars(instance_id, control_library_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries/{control_library_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_control_library(
        self,
        instance_id: str,
        control_library_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom control library.

        Delete a custom control library by specifying its ID.
        With Security and Compliance Center, you can create a custom control library that
        is specific to your organization's needs.  You define the controls and
        specifications before you map previously created assessments. Each control has
        several specifications  and assessments that are mapped to it. A specification is
        a defined requirement that is specific to a component. An assessment, or several,
        are mapped to each specification with a detailed evaluation that is done to check
        whether the specification is compliant. For more information, see [Creating custom
        libraries](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-custom-library).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str control_library_id: The predefined control library ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ControlLibrary` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not control_library_id:
            raise ValueError('control_library_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_custom_control_library',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'control_library_id']
        path_param_values = self.encode_path_vars(instance_id, control_library_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/control_libraries/{control_library_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # profile
    #########################

    def create_profile(
        self,
        instance_id: str,
        controls: List['ProfileControlsPrototype'],
        default_parameters: List['DefaultParameters'],
        *,
        profile_name: Optional[str] = None,
        profile_description: Optional[str] = None,
        profile_version: Optional[str] = None,
        latest: Optional[bool] = None,
        version_group_label: Optional[str] = None,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom profile.

        Create a user-defined custom profile.
        With Security and Compliance Center, you can create  a profile that is specific to
        your usecase, by using an existing library as a starting point.  For more
        information, see [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param List[ProfileControlsPrototype] controls: List of controls associated
               with the profile.
        :param List[DefaultParameters] default_parameters: The default values when
               using the profile.
        :param str profile_name: (optional) The name of the profile.
        :param str profile_description: (optional) A description of what the
               profile should represent.
        :param str profile_version: (optional) The version of the profile.
        :param bool latest: (optional) Determines if the profile is up to date with
               the latest revisions.
        :param str version_group_label: (optional) The unique identifier of the
               revision.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        if default_parameters is None:
            raise ValueError('default_parameters must be provided')
        controls = [convert_model(x) for x in controls]
        default_parameters = [convert_model(x) for x in default_parameters]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_profile',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'controls': controls,
            'default_parameters': default_parameters,
            'profile_name': profile_name,
            'profile_description': profile_description,
            'profile_version': profile_version,
            'latest': latest,
            'version_group_label': version_group_label,
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
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_profiles(
        self,
        instance_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all profiles.

        Retrieve all profiles, including predefined and custom profiles.
        With Security and Compliance Center, you can take advantage of predefined profiles
         that are curated based on industry standards. Or you can choose  to create one
        that is specific to your usecase by using an existing library as a starting point.
        For more information, see [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_profiles',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

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
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile(
        self,
        instance_id: str,
        profile_id: str,
        controls: List['ProfileControlsPrototype'],
        default_parameters: List['DefaultParameters'],
        *,
        profile_name: Optional[str] = None,
        profile_description: Optional[str] = None,
        profile_version: Optional[str] = None,
        latest: Optional[bool] = None,
        version_group_label: Optional[str] = None,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a custom profile.

        Update the details of a user-defined profile.
        With Security and Compliance Center, you can create  a profile that is specific to
        your usecase, by using an existing library as a starting point.  For more
        information, see [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param List[ProfileControlsPrototype] controls: List of controls associated
               with the profile.
        :param List[DefaultParameters] default_parameters: The default values when
               using the profile.
        :param str profile_name: (optional) The name of the profile.
        :param str profile_description: (optional) A description of what the
               profile should represent.
        :param str profile_version: (optional) The version of the profile.
        :param bool latest: (optional) Determines if the profile is up to date with
               the latest revisions.
        :param str version_group_label: (optional) The unique identifier of the
               revision.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if controls is None:
            raise ValueError('controls must be provided')
        if default_parameters is None:
            raise ValueError('default_parameters must be provided')
        controls = [convert_model(x) for x in controls]
        default_parameters = [convert_model(x) for x in default_parameters]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_profile',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'controls': controls,
            'default_parameters': default_parameters,
            'profile_name': profile_name,
            'profile_description': profile_description,
            'profile_version': profile_version,
            'latest': latest,
            'version_group_label': version_group_label,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_profile(
        self,
        instance_id: str,
        profile_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a profile.

        Retrieve a profile by specifying the profile ID.
        With Security and Compliance Center, you can utilize predefined profiles  that are
        curated based on industry standards. Or you can choose  to create one that is
        specific to your usecase, by using an existing library as a starting point. For
        more information, see [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_profile',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_profile(
        self,
        instance_id: str,
        profile_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom profile.

        Delete a custom profile by specifying the profile ID.
        With Security and Compliance Center, you can utilize predefined profiles  that are
        curated based on industry standards. Or you can choose  to create one that is
        specific to your usecase, by using an existing library as a starting point. For
        more information, see [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Profile` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_custom_profile',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_profile_parameters(
        self,
        instance_id: str,
        profile_id: str,
        default_parameters: List['DefaultParameters'],
        *,
        id: Optional[str] = None,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update custom profile parameters.

        Update the parameters of a custom profile.
        With Security and Compliance Center, you can utilize predefined profiles  that are
        curated based on industry standards. Or you can choose  to create one that is
        specific to your usecase, by using an existing library as a starting point. For
        more information, see [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param List[DefaultParameters] default_parameters: list of parameters given
               by default.
        :param str id: (optional) The ID of the Profile.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileDefaultParametersResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        if default_parameters is None:
            raise ValueError('default_parameters must be provided')
        default_parameters = [convert_model(x) for x in default_parameters]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_profile_parameters',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        data = {
            'default_parameters': default_parameters,
            'id': id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/parameters'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_profile_parameters(
        self,
        instance_id: str,
        profile_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List profile parameters for a given profile.

        List the parameters used in the Profile.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileDefaultParametersResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_profile_parameters',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/parameters'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def compare_profiles(
        self,
        instance_id: str,
        profile_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Compare profiles.

        Compare the version of the profile that you're currently using with your
        attachment to the most recent profile version.  By comparing them, you can view
        what controls were added, removed, or modified. For more information, see
        [Building custom
        profiles](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-build-custom-profiles&interface=api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ComparePredefinedProfilesResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='compare_profiles',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/compare'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def list_profile_attachments(
        self,
        instance_id: str,
        profile_id: str,
        *,
        account_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all attachments linked to a specific profile.

        Retrieve all attachments that are linked to a profile.
        With Security and Compliance Center, you can evaluate your resources  on a
        recurring schedule or you can initiate a scan at any time. To evaluate your
        resources, you create an attachment.  An attachment is the association between the
        set of resources that you want to evaluate  and a profile that contains the
        specific controls that you want to use. For more information, see [Running an
        evaluation for IBM
        Cloud](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scan-resources).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str profile_id: The profile ID.
        :param str account_id: (optional) The user account ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProfileAttachmentCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not profile_id:
            raise ValueError('profile_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_profile_attachments',
        )
        headers.update(sdk_headers)

        params = {
            'account_id': account_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'profile_id']
        path_param_values = self.encode_path_vars(instance_id, profile_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/profiles/{profile_id}/attachments'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # providerType
    #########################

    def list_provider_types(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List provider types.

        List all the registered provider types or integrations such as Workload Protection
        available to connect to Security and Compliance Center.  For more information
        about connecting Workload Protection with the Security and Compliance Center, see
        [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_provider_type_by_id(
        self,
        instance_id: str,
        provider_type_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a provider type.

        Retrieve a provider type by specifying its ID. For more information about
        integrations, see [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str provider_type_id: The provider type ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderType` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'provider_type_id']
        path_param_values = self.encode_path_vars(instance_id, provider_type_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types/{provider_type_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # providerTypeInstance
    #########################

    def create_provider_type_instance(
        self,
        instance_id: str,
        provider_type_id: str,
        *,
        name: Optional[str] = None,
        attributes: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a provider type instance.

        Create an instance of a provider type. For more information about integrations,
        see [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str provider_type_id: The provider type ID.
        :param str name: (optional) The provider type instance name.
        :param dict attributes: (optional) The attributes for connecting to the
               provider type instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstance` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'provider_type_id']
        path_param_values = self.encode_path_vars(instance_id, provider_type_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types/{provider_type_id}/provider_type_instances'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_provider_type_instances(
        self,
        instance_id: str,
        provider_type_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List instances of a specific provider type.

        Retrieve all instances of a provider type. For more information about
        integrations, see [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str provider_type_id: The provider type ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstanceCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'provider_type_id']
        path_param_values = self.encode_path_vars(instance_id, provider_type_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types/{provider_type_id}/provider_type_instances'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_provider_type_instance(
        self,
        instance_id: str,
        provider_type_id: str,
        provider_type_instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a provider type instance.

        Retrieve a provider type instance by specifying the provider type ID, and Security
        and Compliance Center instance ID. For more information about integrations, see
        [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str provider_type_id: The provider type ID.
        :param str provider_type_instance_id: The provider type instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstance` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        if not provider_type_instance_id:
            raise ValueError('provider_type_instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'provider_type_id', 'provider_type_instance_id']
        path_param_values = self.encode_path_vars(instance_id, provider_type_id, provider_type_instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types/{provider_type_id}/provider_type_instances/{provider_type_instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_provider_type_instance(
        self,
        instance_id: str,
        provider_type_id: str,
        provider_type_instance_id: str,
        *,
        name: Optional[str] = None,
        attributes: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a provider type instance.

        Update a provider type instance. For more information about integrations, see
        [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str provider_type_id: The provider type ID.
        :param str provider_type_instance_id: The provider type instance ID.
        :param str name: (optional) The provider type instance name.
        :param dict attributes: (optional) The attributes for connecting to the
               provider type instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderTypeInstance` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        if not provider_type_instance_id:
            raise ValueError('provider_type_instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'provider_type_id', 'provider_type_instance_id']
        path_param_values = self.encode_path_vars(instance_id, provider_type_id, provider_type_instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types/{provider_type_id}/provider_type_instances/{provider_type_instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_provider_type_instance(
        self,
        instance_id: str,
        provider_type_id: str,
        provider_type_instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a provider type instance.

        Remove a provider type instance. For more information about integrations, see
        [Connecting Workload
        Protection](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-setup-workload-protection).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str provider_type_id: The provider type ID.
        :param str provider_type_instance_id: The provider type instance ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not provider_type_id:
            raise ValueError('provider_type_id must be provided')
        if not provider_type_instance_id:
            raise ValueError('provider_type_instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_provider_type_instance',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'provider_type_id', 'provider_type_instance_id']
        path_param_values = self.encode_path_vars(instance_id, provider_type_id, provider_type_instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/provider_types/{provider_type_id}/provider_type_instances/{provider_type_instance_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # report
    #########################

    def get_latest_reports(
        self,
        instance_id: str,
        *,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List latest reports.

        Retrieve the latest reports, which are grouped by profile ID, scope ID, and
        attachment ID. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str sort: (optional) This field sorts results by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportLatest` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/latest'.format(**path_param_dict)
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
        instance_id: str,
        *,
        attachment_id: Optional[str] = None,
        group_id: Optional[str] = None,
        profile_id: Optional[str] = None,
        type: Optional[str] = None,
        start: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List reports.

        Retrieve a page of reports that are filtered by the specified parameters. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
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
        :rtype: DetailedResponse with `dict` result representing a `ReportCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports'.format(**path_param_dict)
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
        instance_id: str,
        *,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a report.

        Retrieve a specified report and filter the report details by the specified scope
        ID and/or subscope ID. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str report_id: The ID of the scan that is associated with a report.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Report` object
        """

        if not report_id:
            raise ValueError('report_id must be provided')
        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report',
        )
        headers.update(sdk_headers)

        params = {
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['report_id', 'instance_id']
        path_param_values = self.encode_path_vars(report_id, instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_summary(
        self,
        instance_id: str,
        report_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a report summary.

        Retrieve the complete summarized information for a report. For more information,
        see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportSummary` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/summary'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_download_file(
        self,
        instance_id: str,
        report_id: str,
        *,
        accept: Optional[str] = None,
        exclude_summary: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report evaluation details.

        Download a .csv file to inspect the evaluation details of a specified report. For
        more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str accept: (optional) The type of the response: application/csv or
               application/pdf.
        :param bool exclude_summary: (optional) The indication of whether report
               summary metadata must be excluded.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {
            'Accept': accept,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_download_file',
        )
        headers.update(sdk_headers)

        params = {
            'exclude_summary': exclude_summary,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/download'.format(**path_param_dict)
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
        instance_id: str,
        report_id: str,
        *,
        control_id: Optional[str] = None,
        control_name: Optional[str] = None,
        control_description: Optional[str] = None,
        control_category: Optional[str] = None,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report controls.

        Retrieve a sorted and filtered list of controls for the specified report. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str control_id: (optional) The ID of the control.
        :param str control_name: (optional) The name of the control.
        :param str control_description: (optional) The description of the control.
        :param str control_category: (optional) A control category value.
        :param str status: (optional) The compliance status value.
        :param str sort: (optional) This field sorts controls by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportControls` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
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
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/controls'.format(**path_param_dict)
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
        instance_id: str,
        report_id: str,
        rule_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a report rule.

        Retrieve the rule by specifying the report ID and rule ID. For more information,
        see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str rule_id: The ID of a rule/assessment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleInfo` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'report_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, report_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_report_evaluations(
        self,
        instance_id: str,
        report_id: str,
        *,
        assessment_id: Optional[str] = None,
        assessment_method: Optional[str] = None,
        component_id: Optional[str] = None,
        target_id: Optional[str] = None,
        target_env: Optional[str] = None,
        target_name: Optional[str] = None,
        status: Optional[str] = None,
        start: Optional[str] = None,
        limit: Optional[int] = None,
        sort: Optional[str] = None,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List report evaluations.

        Get a paginated list of evaluations for the specified report. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str assessment_id: (optional) The ID of the assessment.
        :param str assessment_method: (optional) The assessment method.
        :param str component_id: (optional) The ID of component.
        :param str target_id: (optional) The ID of the evaluation target.
        :param str target_env: (optional) The environment of the evaluation target.
        :param str target_name: (optional) The name of the evaluation target.
        :param str status: (optional) The evaluation status value.
        :param str start: (optional) The indication of what resource to start the
               page on.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param str sort: (optional) This field sorts results by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EvaluationPage` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_report_evaluations',
        )
        headers.update(sdk_headers)

        params = {
            'assessment_id': assessment_id,
            'assessment_method': assessment_method,
            'component_id': component_id,
            'target_id': target_id,
            'target_env': target_env,
            'target_name': target_name,
            'status': status,
            'start': start,
            'limit': limit,
            'sort': sort,
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/evaluations'.format(**path_param_dict)
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
        instance_id: str,
        report_id: str,
        *,
        id: Optional[str] = None,
        resource_name: Optional[str] = None,
        account_id: Optional[str] = None,
        component_id: Optional[str] = None,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        start: Optional[str] = None,
        limit: Optional[int] = None,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List report resources.

        Get a paginated list of resources for the specified report. For more information,
        see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str id: (optional) The ID of the resource.
        :param str resource_name: (optional) The name of the resource.
        :param str account_id: (optional) The user account ID.
        :param str component_id: (optional) The ID of component.
        :param str status: (optional) The compliance status value.
        :param str sort: (optional) This field sorts resources by using a valid
               sort field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param str start: (optional) The indication of what resource to start the
               page on.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourcePage` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
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
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/resources'.format(**path_param_dict)
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
        instance_id: str,
        report_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List report tags.

        Retrieve a list of tags for the specified report. For more information, see
        [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportTags` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/tags'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_report_violations_drift(
        self,
        instance_id: str,
        report_id: str,
        *,
        scan_time_duration: Optional[int] = None,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get report violations drift.

        Get a list of report violation data points for the specified report and time
        frame. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param int scan_time_duration: (optional) The duration of the `scan_time`
               timestamp in number of days.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReportViolationsDrift` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_report_violations_drift',
        )
        headers.update(sdk_headers)

        params = {
            'scan_time_duration': scan_time_duration,
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/violations_drift'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def list_scan_reports(
        self,
        instance_id: str,
        report_id: str,
        *,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List scan reports.

        Get a list of scan reports and view the status of report generation in progress.
        For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScanReportCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_scan_reports',
        )
        headers.update(sdk_headers)

        params = {
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/scan_reports'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_scan_report(
        self,
        instance_id: str,
        report_id: str,
        format: str,
        *,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a scan report.

        Create a scan report for a specific scope or sub-scope. For more information, see
        [Defining custom
        rules](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str format: The enum of different report format types.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the sub-scope.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateScanReport` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        if format is None:
            raise ValueError('format must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_scan_report',
        )
        headers.update(sdk_headers)

        data = {
            'format': format,
            'scope_id': scope_id,
            'subscope_id': subscope_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id']
        path_param_values = self.encode_path_vars(instance_id, report_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/scan_reports'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scan_report(
        self,
        instance_id: str,
        report_id: str,
        job_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a scan report.

        Retrieve the scan report by specifying the ID. For more information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str job_id: The ID of the scan_result.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScanReport` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        if not job_id:
            raise ValueError('job_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_scan_report',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'report_id', 'job_id']
        path_param_values = self.encode_path_vars(instance_id, report_id, job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/scan_reports/{job_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scan_report_download_file(
        self,
        instance_id: str,
        report_id: str,
        job_id: str,
        *,
        accept: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a scan report details.

        Download the scan report with evaluation details for the specified ID. For more
        information, see [Viewing
        results](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-results).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str job_id: The ID of the scan_result.
        :param str accept: (optional) The type of the response: application/csv or
               application/pdf.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not report_id:
            raise ValueError('report_id must be provided')
        if not job_id:
            raise ValueError('job_id must be provided')
        headers = {
            'Accept': accept,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_scan_report_download_file',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'report_id', 'job_id']
        path_param_values = self.encode_path_vars(instance_id, report_id, job_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/reports/{report_id}/scan_reports/{job_id}/download'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # rule
    #########################

    def list_rules(
        self,
        instance_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        type: Optional[str] = None,
        search: Optional[str] = None,
        service_name: Optional[str] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all rules.

        Retrieve all the rules that you use to target the exact configuration properties
        that you need to ensure are compliant. For more information, see [Defining custom
        rules](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param str type: (optional) The list of only user-defined, or
               system-defined rules.
        :param str search: (optional) The indication of whether to search for rules
               with a specific string string in the name, description, or labels.
        :param str service_name: (optional) Searches for rules targeting
               corresponding service.
        :param str sort: (optional) Field used to sort rules. Rules can be sorted
               in ascending or descending order.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_rules',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
            'type': type,
            'search': search,
            'service_name': service_name,
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/rules'.format(**path_param_dict)
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
        instance_id: str,
        description: str,
        target: 'RuleTargetPrototype',
        required_config: 'RequiredConfig',
        *,
        version: Optional[str] = None,
        import_: Optional['Import'] = None,
        labels: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a custom rule.

        Create a custom rule to to target the exact configuration properties  that you
        need to evaluate your resources for compliance. For more information, see
        [Defining custom
        rules](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str description: The rule description.
        :param RuleTargetPrototype target: The rule target.
        :param RequiredConfig required_config: The required configurations for a
               Rule.
        :param str version: (optional) The rule version number.
        :param Import import_: (optional) The collection of import parameters.
        :param List[str] labels: (optional) The list of labels that correspond to a
               rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
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
        headers = {}
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/rules'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_rule(
        self,
        instance_id: str,
        rule_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a custom rule.

        Retrieve a rule that you created to evaluate your resources.  For more
        information, see [Defining custom
        rules](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str rule_id: The ID of a rule/assessment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_rule(
        self,
        instance_id: str,
        rule_id: str,
        if_match: str,
        description: str,
        target: 'RuleTargetPrototype',
        required_config: 'RequiredConfig',
        *,
        version: Optional[str] = None,
        import_: Optional['Import'] = None,
        labels: Optional[List[str]] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a custom rule.

        Update a custom rule that you use to target the exact configuration properties
        that you need to evaluate your resources for compliance. For more information, see
        [Defining custom
        rules](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str rule_id: The ID of a rule/assessment.
        :param str if_match: This field compares a supplied `Etag` value with the
               version that is stored for the requested resource. If the values match, the
               server allows the request method to continue.
               To find the `Etag` value, run a GET request on the resource that you want
               to modify, and check the response headers.
        :param str description: The rule description.
        :param RuleTargetPrototype target: The rule target.
        :param RequiredConfig required_config: The required configurations for a
               Rule.
        :param str version: (optional) The rule version number.
        :param Import import_: (optional) The collection of import parameters.
        :param List[str] labels: (optional) The list of labels that correspond to a
               rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
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

        path_param_keys = ['instance_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_rule(
        self,
        instance_id: str,
        rule_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a custom rule.

        Delete a custom rule that you no longer require to evaluate your resources. For
        more information, see [Defining custom
        rules](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-rules-define).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str rule_id: The ID of a rule/assessment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # scope
    #########################

    def create_scope(
        self,
        instance_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
        properties: Optional[List['ScopeProperty']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a scope.

        Create a scope.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str name: (optional) The scope name.
        :param str description: (optional) The scope description.
        :param str environment: (optional) The scope environment.
        :param List[ScopeProperty] properties: (optional) The properties that are
               supported for scoping by this environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Scope` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if properties is not None:
            properties = [convert_model(x) for x in properties]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_scope',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'environment': environment,
            'properties': properties,
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
        url = '/instances/{instance_id}/v3/scopes'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_scopes(
        self,
        instance_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all scopes.

        Get all scopes.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param str name: (optional) determine name of scope returned in response.
        :param str description: (optional) determine descriptions of scope returned
               in response.
        :param str environment: (optional) determine environment of scopes returned
               in response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScopeCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_scopes',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
            'name': name,
            'description': description,
            'environment': environment,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_scope(
        self,
        instance_id: str,
        scope_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a scope.

        Update the details of a scope.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param str name: (optional) The scope name.
        :param str description: (optional) The scope description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Scope` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='update_scope',
        )
        headers.update(sdk_headers)

        data = {
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

        path_param_keys = ['instance_id', 'scope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_scope(
        self,
        instance_id: str,
        scope_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a scope.

        Get a scope by specifying the scope ID.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Scope` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_scope',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'scope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_scope(
        self,
        instance_id: str,
        scope_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a scope.

        Delete a scope by specifying the scope ID.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_scope',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'scope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_subscope(
        self,
        instance_id: str,
        scope_id: str,
        subscopes: List['ScopePrototype'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a subscope.

        Create a subscope.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param List[ScopePrototype] subscopes: The array of subscopes.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SubScopeResponse` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        if subscopes is None:
            raise ValueError('subscopes must be provided')
        subscopes = [convert_model(x) for x in subscopes]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_subscope',
        )
        headers.update(sdk_headers)

        data = {
            'subscopes': subscopes,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'scope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}/subscopes'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_subscopes(
        self,
        instance_id: str,
        scope_id: str,
        *,
        limit: Optional[int] = None,
        start: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all subscopes.

        Get all subscopes.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str start: (optional) Determine what resource to start the page on
               or after.
        :param str name: (optional) determine name of subscope returned in
               response.
        :param str description: (optional) determine descriptions of subscopes
               returned in response.
        :param str environment: (optional) determine environment of subscopes
               returned in response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SubScopeCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_subscopes',
        )
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start,
            'name': name,
            'description': description,
            'environment': environment,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'scope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}/subscopes'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_subscope(
        self,
        instance_id: str,
        scope_id: str,
        subscope_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a subscope.

        Get the subscope details.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param str subscope_id: The ID of the scope being targeted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SubScope` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        if not subscope_id:
            raise ValueError('subscope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_subscope',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'scope_id', 'subscope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id, subscope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}/subscopes/{subscope_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_subscope(
        self,
        instance_id: str,
        scope_id: str,
        subscope_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a subscope.

        Update the subscope details.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param str subscope_id: The ID of the scope being targeted.
        :param str name: (optional) The scope name.
        :param str description: (optional) The scope description.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SubScope` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        if not subscope_id:
            raise ValueError('subscope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='update_subscope',
        )
        headers.update(sdk_headers)

        data = {
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

        path_param_keys = ['instance_id', 'scope_id', 'subscope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id, subscope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}/subscopes/{subscope_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_subscope(
        self,
        instance_id: str,
        scope_id: str,
        subscope_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a subscope.

        Delete the subscope by specifying the subscope ID.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param str subscope_id: The ID of the scope being targeted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not scope_id:
            raise ValueError('scope_id must be provided')
        if not subscope_id:
            raise ValueError('subscope_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_subscope',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'scope_id', 'subscope_id']
        path_param_values = self.encode_path_vars(instance_id, scope_id, subscope_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/scopes/{scope_id}/subscopes/{subscope_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # service
    #########################

    def list_services(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List services.

        List all the services that you use to evaluate the configuration of your resources
        for security and compliance.
        [Learn
        more](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scannable-components).

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServiceCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_services',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v3/services'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_service(
        self,
        services_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a service.

        Retrieve a service configuration that you monitor. [Learn
        more](https://cloud.ibm.com/docs/security-compliance?topic=security-compliance-scannable-components).

        :param str services_name: The name of the corresponding service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Service` object
        """

        if not services_name:
            raise ValueError('services_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_service',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['services_name']
        path_param_values = self.encode_path_vars(services_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/services/{services_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # setting
    #########################

    def get_settings(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List settings.

        Retrieve the settings of your service instance.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Settings` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/settings'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_settings(
        self,
        instance_id: str,
        *,
        object_storage: Optional['ObjectStoragePrototype'] = None,
        event_notifications: Optional['EventNotificationsPrototype'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update settings.

        Update the settings of your service instance.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param ObjectStoragePrototype object_storage: (optional) The payload to
               connect a Cloud Object Storage instance to an Security and Compliance
               Center instance.
        :param EventNotificationsPrototype event_notifications: (optional) The
               payload to connect an Event Notification instance with a Security and
               Compliance Center instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Settings` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if object_storage is not None:
            object_storage = convert_model(object_storage)
        if event_notifications is not None:
            event_notifications = convert_model(event_notifications)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='update_settings',
        )
        headers.update(sdk_headers)

        data = {
            'object_storage': object_storage,
            'event_notifications': event_notifications,
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
        url = '/instances/{instance_id}/v3/settings'.format(**path_param_dict)
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
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a test event.

        Send a test event to your Event Notifications instance to ensure that the events
        that are generated  by Security and Compliance Center are being forwarded to Event
        Notifications. For more information, see [Enabling event
        notifications](/docs/security-compliance?topic=security-compliance-event-notifications#event-notifications-test-api).

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TestEvent` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/test_event'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # target
    #########################

    def create_target(
        self,
        instance_id: str,
        account_id: str,
        trusted_profile_id: str,
        name: str,
        *,
        credentials: Optional[List['Credential']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a target.

        Creates a target to scan against.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str account_id: The target account ID.
        :param str trusted_profile_id: The trusted profile ID.
        :param str name: The target name.
        :param List[Credential] credentials: (optional) Customer credential to
               access for a specific service to scan.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Target` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        if trusted_profile_id is None:
            raise ValueError('trusted_profile_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if credentials is not None:
            credentials = [convert_model(x) for x in credentials]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='create_target',
        )
        headers.update(sdk_headers)

        data = {
            'account_id': account_id,
            'trusted_profile_id': trusted_profile_id,
            'name': name,
            'credentials': credentials,
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
        url = '/instances/{instance_id}/v3/targets'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_targets(
        self,
        instance_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of targets with pagination.

        Returns a list of targets.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TargetCollection` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='list_targets',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/targets'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_target(
        self,
        instance_id: str,
        target_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a target by ID.

        Retrieves a target by its ID association.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str target_id: The target ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Target` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not target_id:
            raise ValueError('target_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='get_target',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'target_id']
        path_param_values = self.encode_path_vars(instance_id, target_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/targets/{target_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_target(
        self,
        instance_id: str,
        target_id: str,
        account_id: str,
        trusted_profile_id: str,
        name: str,
        *,
        credentials: Optional[List['Credential']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        replace a target by ID.

        Updates a target by its ID.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str target_id: The target ID.
        :param str account_id: The target account ID.
        :param str trusted_profile_id: The trusted profile ID.
        :param str name: The target name.
        :param List[Credential] credentials: (optional) Customer credential to
               access for a specific service to scan.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Target` object
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not target_id:
            raise ValueError('target_id must be provided')
        if account_id is None:
            raise ValueError('account_id must be provided')
        if trusted_profile_id is None:
            raise ValueError('trusted_profile_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if credentials is not None:
            credentials = [convert_model(x) for x in credentials]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='replace_target',
        )
        headers.update(sdk_headers)

        data = {
            'account_id': account_id,
            'trusted_profile_id': trusted_profile_id,
            'name': name,
            'credentials': credentials,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'target_id']
        path_param_values = self.encode_path_vars(instance_id, target_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/targets/{target_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_target(
        self,
        instance_id: str,
        target_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a target by ID.

        Deletes a target by the ID.

        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str target_id: The target ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not instance_id:
            raise ValueError('instance_id must be provided')
        if not target_id:
            raise ValueError('target_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V3',
            operation_id='delete_target',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'target_id']
        path_param_values = self.encode_path_vars(instance_id, target_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/v3/targets/{target_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


class ListInstanceAttachmentsEnums:
    """
    Enums for list_instance_attachments parameters.
    """

    class Sort(str, Enum):
        """
        The sorted collection of attachments. The available values are `created_on` and
        `scope_type`.
        """

        CREATED_ON = 'created_on'
        SCOPE_TYPE = 'scope_type'
    class Direction(str, Enum):
        """
        The collection of attachments that is sorted in ascending order. To sort the
        collection in descending order, use the `DESC` schema.
        """

        DESC = 'desc'
        ASC = 'asc'


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


class GetReportDownloadFileEnums:
    """
    Enums for get_report_download_file parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/csv or application/pdf.
        """

        APPLICATION_CSV = 'application/csv'
        APPLICATION_PDF = 'application/pdf'


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
        NOT_APPLICABLE = 'not_applicable'
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
        NOT_APPLICABLE = 'not_applicable'
    class Sort(str, Enum):
        """
        This field sorts resources by using a valid sort field. To learn more, see
        [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        """

        ACCOUNT_ID = 'account_id'
        COMPONENT_ID = 'component_id'
        RESOURCE_NAME = 'resource_name'
        STATUS = 'status'


class GetScanReportDownloadFileEnums:
    """
    Enums for get_scan_report_download_file parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/csv or application/pdf.
        """

        APPLICATION_CSV = 'application/csv'
        APPLICATION_PDF = 'application/pdf'


class ListRulesEnums:
    """
    Enums for list_rules parameters.
    """

    class Type(str, Enum):
        """
        The list of only user-defined, or system-defined rules.
        """

        USER_DEFINED = 'user_defined'
        SYSTEM_DEFINED = 'system_defined'
    class Sort(str, Enum):
        """
        Field used to sort rules. Rules can be sorted in ascending or descending order.
        """

        DESCRIPTION = 'description'
        SERVICE_DISPLAY_NAME = 'service_display_name'
        TYPE = 'type'
        UPDATED_ON = 'updated_on'


##############################################################################
# Models
##############################################################################


class Account:
    """
    The account that is associated with a report.

    :param str id: (optional) The account ID.
    :param str name: (optional) The account name.
    :param str type: (optional) The account type.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
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
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
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


class AdditionalDetails:
    """
    Extended information for a report.

    :param str created_by: (optional) Identifies which entity created a report.
    :param List[str] labels: (optional) Classification for a report.
    :param List[Link] links: (optional) URL.
    """

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        labels: Optional[List[str]] = None,
        links: Optional[List['Link']] = None,
    ) -> None:
        """
        Initialize a AdditionalDetails object.

        :param str created_by: (optional) Identifies which entity created a report.
        :param List[str] labels: (optional) Classification for a report.
        :param List[Link] links: (optional) URL.
        """
        self.created_by = created_by
        self.labels = labels
        self.links = links

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AdditionalDetails':
        """Initialize a AdditionalDetails object from a json dictionary."""
        args = {}
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
        if (links := _dict.get('links')) is not None:
            args['links'] = [Link.from_dict(v) for v in links]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AdditionalDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'links') and self.links is not None:
            links_list = []
            for v in self.links:
                if isinstance(v, dict):
                    links_list.append(v)
                else:
                    links_list.append(v.to_dict())
            _dict['links'] = links_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AdditionalDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AdditionalDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AdditionalDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AdditionalProperty:
    """
    AdditionalProperty.

    :param str type: An additional property that indicates the type of the attribute
          in various formats (text, url, secret, label, masked).
    :param str display_name: The name of the attribute that is displayed in the UI.
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
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in AdditionalProperty JSON')
        if (display_name := _dict.get('display_name')) is not None:
            args['display_name'] = display_name
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

    :param str name: (optional) The additional target attribute name.
    :param str operator: The operator.
    :param object value: (optional)
    """

    def __init__(
        self,
        operator: str,
        *,
        name: Optional[str] = None,
        value: Optional[object] = None,
    ) -> None:
        """
        Initialize a AdditionalTargetAttribute object.

        :param str operator: The operator.
        :param str name: (optional) The additional target attribute name.
        :param object value: (optional)
        """
        self.name = name
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AdditionalTargetAttribute':
        """Initialize a AdditionalTargetAttribute object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (operator := _dict.get('operator')) is not None:
            args['operator'] = operator
        else:
            raise ValueError('Required property \'operator\' not present in AdditionalTargetAttribute JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
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

    :param str assessment_id: (optional) The assessment ID.
    :param str assessment_type: (optional) The assessment type.
    :param str assessment_method: (optional) The assessment method.
    :param str assessment_description: (optional) The assessment description.
    :param int parameter_count: (optional) The number of parameters of this
          assessment.
    :param List[Parameter] parameters: The list of parameters of this assessment.
    """

    def __init__(
        self,
        parameters: List['Parameter'],
        *,
        assessment_id: Optional[str] = None,
        assessment_type: Optional[str] = None,
        assessment_method: Optional[str] = None,
        assessment_description: Optional[str] = None,
        parameter_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a Assessment object.

        :param List[Parameter] parameters: The list of parameters of this
               assessment.
        :param str assessment_id: (optional) The assessment ID.
        :param str assessment_type: (optional) The assessment type.
        :param str assessment_method: (optional) The assessment method.
        :param str assessment_description: (optional) The assessment description.
        :param int parameter_count: (optional) The number of parameters of this
               assessment.
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
        if (assessment_id := _dict.get('assessment_id')) is not None:
            args['assessment_id'] = assessment_id
        if (assessment_type := _dict.get('assessment_type')) is not None:
            args['assessment_type'] = assessment_type
        if (assessment_method := _dict.get('assessment_method')) is not None:
            args['assessment_method'] = assessment_method
        if (assessment_description := _dict.get('assessment_description')) is not None:
            args['assessment_description'] = assessment_description
        if (parameter_count := _dict.get('parameter_count')) is not None:
            args['parameter_count'] = parameter_count
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = [Parameter.from_dict(v) for v in parameters]
        else:
            raise ValueError('Required property \'parameters\' not present in Assessment JSON')
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


class AssessmentPrototype:
    """
    The necessary fields to include a rule/assessment.

    :param str assessment_id: (optional) The ID of the rule to target. A list of
          rules can be obtained from the list_rules method.
    :param str assessment_description: (optional) Details on the intent of the rule
          for an assessment.
    """

    def __init__(
        self,
        *,
        assessment_id: Optional[str] = None,
        assessment_description: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssessmentPrototype object.

        :param str assessment_id: (optional) The ID of the rule to target. A list
               of rules can be obtained from the list_rules method.
        :param str assessment_description: (optional) Details on the intent of the
               rule for an assessment.
        """
        self.assessment_id = assessment_id
        self.assessment_description = assessment_description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssessmentPrototype':
        """Initialize a AssessmentPrototype object from a json dictionary."""
        args = {}
        if (assessment_id := _dict.get('assessment_id')) is not None:
            args['assessment_id'] = assessment_id
        if (assessment_description := _dict.get('assessment_description')) is not None:
            args['assessment_description'] = assessment_description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssessmentPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assessment_id') and self.assessment_id is not None:
            _dict['assessment_id'] = self.assessment_id
        if hasattr(self, 'assessment_description') and self.assessment_description is not None:
            _dict['assessment_description'] = self.assessment_description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssessmentPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssessmentPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssessmentPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssessmentWithStats:
    """
    The control specification assessment.

    :param str assessment_id: (optional) The assessment ID.
    :param str assessment_type: (optional) The assessment type.
    :param str assessment_method: (optional) The assessment method.
    :param str assessment_description: (optional) The assessment description.
    :param int parameter_count: (optional) The number of parameters of this
          assessment.
    :param List[Parameter] parameters: (optional) The list of parameters of this
          assessment.
    :param int total_count: (optional) The total number of evaluations.
    :param int pass_count: (optional) The number of passed evaluations.
    :param int failure_count: (optional) The number of failed evaluations.
    :param int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :param int completed_count: (optional) The total number of completed
          evaluations.
    """

    def __init__(
        self,
        *,
        assessment_id: Optional[str] = None,
        assessment_type: Optional[str] = None,
        assessment_method: Optional[str] = None,
        assessment_description: Optional[str] = None,
        parameter_count: Optional[int] = None,
        parameters: Optional[List['Parameter']] = None,
        total_count: Optional[int] = None,
        pass_count: Optional[int] = None,
        failure_count: Optional[int] = None,
        error_count: Optional[int] = None,
        completed_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a AssessmentWithStats object.

        :param str assessment_id: (optional) The assessment ID.
        :param str assessment_type: (optional) The assessment type.
        :param str assessment_method: (optional) The assessment method.
        :param str assessment_description: (optional) The assessment description.
        :param int parameter_count: (optional) The number of parameters of this
               assessment.
        :param List[Parameter] parameters: (optional) The list of parameters of
               this assessment.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        """
        self.assessment_id = assessment_id
        self.assessment_type = assessment_type
        self.assessment_method = assessment_method
        self.assessment_description = assessment_description
        self.parameter_count = parameter_count
        self.parameters = parameters
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.completed_count = completed_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssessmentWithStats':
        """Initialize a AssessmentWithStats object from a json dictionary."""
        args = {}
        if (assessment_id := _dict.get('assessment_id')) is not None:
            args['assessment_id'] = assessment_id
        if (assessment_type := _dict.get('assessment_type')) is not None:
            args['assessment_type'] = assessment_type
        if (assessment_method := _dict.get('assessment_method')) is not None:
            args['assessment_method'] = assessment_method
        if (assessment_description := _dict.get('assessment_description')) is not None:
            args['assessment_description'] = assessment_description
        if (parameter_count := _dict.get('parameter_count')) is not None:
            args['parameter_count'] = parameter_count
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = [Parameter.from_dict(v) for v in parameters]
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (pass_count := _dict.get('pass_count')) is not None:
            args['pass_count'] = pass_count
        if (failure_count := _dict.get('failure_count')) is not None:
            args['failure_count'] = failure_count
        if (error_count := _dict.get('error_count')) is not None:
            args['error_count'] = error_count
        if (completed_count := _dict.get('completed_count')) is not None:
            args['completed_count'] = completed_count
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssessmentWithStats object from a json dictionary."""
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
        """Return a `str` version of this AssessmentWithStats object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssessmentWithStats') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssessmentWithStats') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Attachment:
    """
    The attachment that is associated with a report.

    :param str id: (optional) The attachment ID.
    :param str name: (optional) The name of the attachment.
    :param str description: (optional) The description of the attachment.
    :param str schedule: (optional) The attachment schedule.
    :param object scope: (optional) Deprecated: (deprecated) The scope associated
          with the report.
    :param List[Scope] scopes: (optional) The report's scopes based on the caller's
          access permissions.
    :param AttachmentNotifications notifications: (optional) The notification
          configuration of the attachment.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        schedule: Optional[str] = None,
        scope: Optional[object] = None,
        scopes: Optional[List['Scope']] = None,
        notifications: Optional['AttachmentNotifications'] = None,
    ) -> None:
        """
        Initialize a Attachment object.

        :param str id: (optional) The attachment ID.
        :param str name: (optional) The name of the attachment.
        :param str description: (optional) The description of the attachment.
        :param str schedule: (optional) The attachment schedule.
        :param object scope: (optional) Deprecated: (deprecated) The scope
               associated with the report.
        :param List[Scope] scopes: (optional) The report's scopes based on the
               caller's access permissions.
        :param AttachmentNotifications notifications: (optional) The notification
               configuration of the attachment.
        """
        self.id = id
        self.name = name
        self.description = description
        self.schedule = schedule
        self.scope = scope
        self.scopes = scopes
        self.notifications = notifications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Attachment':
        """Initialize a Attachment object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (schedule := _dict.get('schedule')) is not None:
            args['schedule'] = schedule
        if (scope := _dict.get('scope')) is not None:
            args['scope'] = scope
        if (scopes := _dict.get('scopes')) is not None:
            args['scopes'] = [Scope.from_dict(v) for v in scopes]
        if (notifications := _dict.get('notifications')) is not None:
            args['notifications'] = AttachmentNotifications.from_dict(notifications)
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
            _dict['scope'] = self.scope
        if hasattr(self, 'scopes') and self.scopes is not None:
            scopes_list = []
            for v in self.scopes:
                if isinstance(v, dict):
                    scopes_list.append(v)
                else:
                    scopes_list.append(v.to_dict())
            _dict['scopes'] = scopes_list
        if hasattr(self, 'notifications') and self.notifications is not None:
            if isinstance(self.notifications, dict):
                _dict['notifications'] = self.notifications
            else:
                _dict['notifications'] = self.notifications.to_dict()
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


class AttachmentNotifications:
    """
    The notification configuration of the attachment.

    :param bool enabled: (optional) Shows if the notification is enabled or
          disabled.
    :param AttachmentNotificationsControls controls: (optional) The controls
          associated with an AttachmentNotification.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        controls: Optional['AttachmentNotificationsControls'] = None,
    ) -> None:
        """
        Initialize a AttachmentNotifications object.

        :param bool enabled: (optional) Shows if the notification is enabled or
               disabled.
        :param AttachmentNotificationsControls controls: (optional) The controls
               associated with an AttachmentNotification.
        """
        self.enabled = enabled
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentNotifications':
        """Initialize a AttachmentNotifications object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (controls := _dict.get('controls')) is not None:
            args['controls'] = AttachmentNotificationsControls.from_dict(controls)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentNotifications object from a json dictionary."""
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
        """Return a `str` version of this AttachmentNotifications object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentNotifications') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentNotifications') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AttachmentNotificationsControls:
    """
    The controls associated with an AttachmentNotification.

    :param int threshold_limit: (optional) The maximum number of not compliant
          controls before a notification is triggered.
    :param List[str] failed_control_ids: List of controls that triggers a
          notification should a scan fail.
    """

    def __init__(
        self,
        failed_control_ids: List[str],
        *,
        threshold_limit: Optional[int] = None,
    ) -> None:
        """
        Initialize a AttachmentNotificationsControls object.

        :param List[str] failed_control_ids: List of controls that triggers a
               notification should a scan fail.
        :param int threshold_limit: (optional) The maximum number of not compliant
               controls before a notification is triggered.
        """
        self.threshold_limit = threshold_limit
        self.failed_control_ids = failed_control_ids

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AttachmentNotificationsControls':
        """Initialize a AttachmentNotificationsControls object from a json dictionary."""
        args = {}
        if (threshold_limit := _dict.get('threshold_limit')) is not None:
            args['threshold_limit'] = threshold_limit
        if (failed_control_ids := _dict.get('failed_control_ids')) is not None:
            args['failed_control_ids'] = failed_control_ids
        else:
            raise ValueError('Required property \'failed_control_ids\' not present in AttachmentNotificationsControls JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AttachmentNotificationsControls object from a json dictionary."""
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
        """Return a `str` version of this AttachmentNotificationsControls object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AttachmentNotificationsControls') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AttachmentNotificationsControls') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ComparePredefinedProfilesResponse:
    """
    The predefined profile comparison response.

    :param CompareProfileResponse current_predefined_version: (optional) Shows a
          change in the Profile.
    :param CompareProfileResponse latest_predefined_version: (optional) Shows a
          change in the Profile.
    :param ControlChanges controls_changes: (optional) Shows details of the controls
          that were changed.
    :param DefaultParametersChanges default_parameters_changes: (optional) Shows
          details of the parameters that were changed.
    """

    def __init__(
        self,
        *,
        current_predefined_version: Optional['CompareProfileResponse'] = None,
        latest_predefined_version: Optional['CompareProfileResponse'] = None,
        controls_changes: Optional['ControlChanges'] = None,
        default_parameters_changes: Optional['DefaultParametersChanges'] = None,
    ) -> None:
        """
        Initialize a ComparePredefinedProfilesResponse object.

        :param CompareProfileResponse current_predefined_version: (optional) Shows
               a change in the Profile.
        :param CompareProfileResponse latest_predefined_version: (optional) Shows a
               change in the Profile.
        :param ControlChanges controls_changes: (optional) Shows details of the
               controls that were changed.
        :param DefaultParametersChanges default_parameters_changes: (optional)
               Shows details of the parameters that were changed.
        """
        self.current_predefined_version = current_predefined_version
        self.latest_predefined_version = latest_predefined_version
        self.controls_changes = controls_changes
        self.default_parameters_changes = default_parameters_changes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComparePredefinedProfilesResponse':
        """Initialize a ComparePredefinedProfilesResponse object from a json dictionary."""
        args = {}
        if (current_predefined_version := _dict.get('current_predefined_version')) is not None:
            args['current_predefined_version'] = CompareProfileResponse.from_dict(current_predefined_version)
        if (latest_predefined_version := _dict.get('latest_predefined_version')) is not None:
            args['latest_predefined_version'] = CompareProfileResponse.from_dict(latest_predefined_version)
        if (controls_changes := _dict.get('controls_changes')) is not None:
            args['controls_changes'] = ControlChanges.from_dict(controls_changes)
        if (default_parameters_changes := _dict.get('default_parameters_changes')) is not None:
            args['default_parameters_changes'] = DefaultParametersChanges.from_dict(default_parameters_changes)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComparePredefinedProfilesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'current_predefined_version') and self.current_predefined_version is not None:
            if isinstance(self.current_predefined_version, dict):
                _dict['current_predefined_version'] = self.current_predefined_version
            else:
                _dict['current_predefined_version'] = self.current_predefined_version.to_dict()
        if hasattr(self, 'latest_predefined_version') and self.latest_predefined_version is not None:
            if isinstance(self.latest_predefined_version, dict):
                _dict['latest_predefined_version'] = self.latest_predefined_version
            else:
                _dict['latest_predefined_version'] = self.latest_predefined_version.to_dict()
        if hasattr(self, 'controls_changes') and self.controls_changes is not None:
            if isinstance(self.controls_changes, dict):
                _dict['controls_changes'] = self.controls_changes
            else:
                _dict['controls_changes'] = self.controls_changes.to_dict()
        if hasattr(self, 'default_parameters_changes') and self.default_parameters_changes is not None:
            if isinstance(self.default_parameters_changes, dict):
                _dict['default_parameters_changes'] = self.default_parameters_changes
            else:
                _dict['default_parameters_changes'] = self.default_parameters_changes.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComparePredefinedProfilesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComparePredefinedProfilesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComparePredefinedProfilesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CompareProfileResponse:
    """
    Shows a change in the Profile.

    :param str id: (optional) The ID of the profile.
    :param str profile_name: (optional) The name of the profile.
    :param str profile_description: (optional) A description of what the profile
          should represent.
    :param str profile_type: The type of profile, either predefined or custom.
    :param str profile_version: (optional) The version of the profile.
    :param str version_group_label: (optional) The unique identifier of the profile
          revision.
    :param bool latest: (optional) Determines if the profile is up to date with the
          latest revisions.
    :param str created_by: (optional) User who created the profile.
    :param datetime created_on: (optional) The date when the profile was created, in
          date-time format.
    :param str updated_by: (optional) User who made the latest changes to the
          profile.
    :param datetime updated_on: (optional) The date when the profile was last
          updated, in date-time format.
    :param int controls_count: (optional) Number of controls in the profile.
    """

    def __init__(
        self,
        profile_type: str,
        *,
        id: Optional[str] = None,
        profile_name: Optional[str] = None,
        profile_description: Optional[str] = None,
        profile_version: Optional[str] = None,
        version_group_label: Optional[str] = None,
        latest: Optional[bool] = None,
        created_by: Optional[str] = None,
        created_on: Optional[datetime] = None,
        updated_by: Optional[str] = None,
        updated_on: Optional[datetime] = None,
        controls_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a CompareProfileResponse object.

        :param str profile_type: The type of profile, either predefined or custom.
        :param str id: (optional) The ID of the profile.
        :param str profile_name: (optional) The name of the profile.
        :param str profile_description: (optional) A description of what the
               profile should represent.
        :param str profile_version: (optional) The version of the profile.
        :param str version_group_label: (optional) The unique identifier of the
               profile revision.
        :param bool latest: (optional) Determines if the profile is up to date with
               the latest revisions.
        :param str created_by: (optional) User who created the profile.
        :param datetime created_on: (optional) The date when the profile was
               created, in date-time format.
        :param str updated_by: (optional) User who made the latest changes to the
               profile.
        :param datetime updated_on: (optional) The date when the profile was last
               updated, in date-time format.
        :param int controls_count: (optional) Number of controls in the profile.
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

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CompareProfileResponse':
        """Initialize a CompareProfileResponse object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (profile_name := _dict.get('profile_name')) is not None:
            args['profile_name'] = profile_name
        if (profile_description := _dict.get('profile_description')) is not None:
            args['profile_description'] = profile_description
        if (profile_type := _dict.get('profile_type')) is not None:
            args['profile_type'] = profile_type
        else:
            raise ValueError('Required property \'profile_type\' not present in CompareProfileResponse JSON')
        if (profile_version := _dict.get('profile_version')) is not None:
            args['profile_version'] = profile_version
        if (version_group_label := _dict.get('version_group_label')) is not None:
            args['version_group_label'] = version_group_label
        if (latest := _dict.get('latest')) is not None:
            args['latest'] = latest
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        if (controls_count := _dict.get('controls_count')) is not None:
            args['controls_count'] = controls_count
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CompareProfileResponse object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CompareProfileResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CompareProfileResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CompareProfileResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProfileTypeEnum(str, Enum):
        """
        The type of profile, either predefined or custom.
        """

        CUSTOM = 'custom'
        PREDEFINED = 'predefined'



class ComplianceScore:
    """
    The compliance score.

    :param int passed: (optional) The number of successful evaluations.
    :param int total_count: (optional) The total number of evaluations.
    :param int percent: (optional) The percentage of successful evaluations.
    """

    def __init__(
        self,
        *,
        passed: Optional[int] = None,
        total_count: Optional[int] = None,
        percent: Optional[int] = None,
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
        if (passed := _dict.get('passed')) is not None:
            args['passed'] = passed
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (percent := _dict.get('percent')) is not None:
            args['percent'] = percent
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

    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of checks.
    :param int compliant_count: (optional) The number of compliant checks.
    :param int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :param int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :param int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :param int not_applicable_count: (optional) The number of not applicable (with
          no evaluations) checks.
    """

    def __init__(
        self,
        status: str,
        *,
        total_count: Optional[int] = None,
        compliant_count: Optional[int] = None,
        not_compliant_count: Optional[int] = None,
        unable_to_perform_count: Optional[int] = None,
        user_evaluation_required_count: Optional[int] = None,
        not_applicable_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ComplianceStats object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param int not_applicable_count: (optional) The number of not applicable
               (with no evaluations) checks.
        """
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.not_applicable_count = not_applicable_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComplianceStats':
        """Initialize a ComplianceStats object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ComplianceStats JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (compliant_count := _dict.get('compliant_count')) is not None:
            args['compliant_count'] = compliant_count
        if (not_compliant_count := _dict.get('not_compliant_count')) is not None:
            args['not_compliant_count'] = not_compliant_count
        if (unable_to_perform_count := _dict.get('unable_to_perform_count')) is not None:
            args['unable_to_perform_count'] = unable_to_perform_count
        if (user_evaluation_required_count := _dict.get('user_evaluation_required_count')) is not None:
            args['user_evaluation_required_count'] = user_evaluation_required_count
        if (not_applicable_count := _dict.get('not_applicable_count')) is not None:
            args['not_applicable_count'] = not_applicable_count
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
        if hasattr(self, 'not_applicable_count') and self.not_applicable_count is not None:
            _dict['not_applicable_count'] = self.not_applicable_count
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
        NOT_APPLICABLE = 'not_applicable'



class ComplianceStatsWithNonCompliant:
    """
    The compliance stats.

    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of checks.
    :param int compliant_count: (optional) The number of compliant checks.
    :param int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :param int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :param int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :param int not_applicable_count: (optional) The number of not applicable (with
          no evaluations) checks.
    :param List[ControlSummary] not_compliant_controls: (optional) The list of non
          compliant controls.
    """

    def __init__(
        self,
        status: str,
        *,
        total_count: Optional[int] = None,
        compliant_count: Optional[int] = None,
        not_compliant_count: Optional[int] = None,
        unable_to_perform_count: Optional[int] = None,
        user_evaluation_required_count: Optional[int] = None,
        not_applicable_count: Optional[int] = None,
        not_compliant_controls: Optional[List['ControlSummary']] = None,
    ) -> None:
        """
        Initialize a ComplianceStatsWithNonCompliant object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param int not_applicable_count: (optional) The number of not applicable
               (with no evaluations) checks.
        :param List[ControlSummary] not_compliant_controls: (optional) The list of
               non compliant controls.
        """
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.not_applicable_count = not_applicable_count
        self.not_compliant_controls = not_compliant_controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ComplianceStatsWithNonCompliant':
        """Initialize a ComplianceStatsWithNonCompliant object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ComplianceStatsWithNonCompliant JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (compliant_count := _dict.get('compliant_count')) is not None:
            args['compliant_count'] = compliant_count
        if (not_compliant_count := _dict.get('not_compliant_count')) is not None:
            args['not_compliant_count'] = not_compliant_count
        if (unable_to_perform_count := _dict.get('unable_to_perform_count')) is not None:
            args['unable_to_perform_count'] = unable_to_perform_count
        if (user_evaluation_required_count := _dict.get('user_evaluation_required_count')) is not None:
            args['user_evaluation_required_count'] = user_evaluation_required_count
        if (not_applicable_count := _dict.get('not_applicable_count')) is not None:
            args['not_applicable_count'] = not_applicable_count
        if (not_compliant_controls := _dict.get('not_compliant_controls')) is not None:
            args['not_compliant_controls'] = [ControlSummary.from_dict(v) for v in not_compliant_controls]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ComplianceStatsWithNonCompliant object from a json dictionary."""
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
        if hasattr(self, 'not_applicable_count') and self.not_applicable_count is not None:
            _dict['not_applicable_count'] = self.not_applicable_count
        if hasattr(self, 'not_compliant_controls') and self.not_compliant_controls is not None:
            not_compliant_controls_list = []
            for v in self.not_compliant_controls:
                if isinstance(v, dict):
                    not_compliant_controls_list.append(v)
                else:
                    not_compliant_controls_list.append(v.to_dict())
            _dict['not_compliant_controls'] = not_compliant_controls_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ComplianceStatsWithNonCompliant object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ComplianceStatsWithNonCompliant') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ComplianceStatsWithNonCompliant') -> bool:
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
        NOT_APPLICABLE = 'not_applicable'



class ConditionItem:
    """
    ConditionItem.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ConditionItem object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['ConditionItemConditionBase', 'ConditionItemConditionList', 'ConditionItemConditionSubRule'])
        )
        raise Exception(msg)


class ConfigurationInformationPoints:
    """
    The service configuration information.

    :param str type: (optional) The information type.
    :param List[Endpoint] endpoints: (optional) The service configurations
          endpoints.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        endpoints: Optional[List['Endpoint']] = None,
    ) -> None:
        """
        Initialize a ConfigurationInformationPoints object.

        :param str type: (optional) The information type.
        :param List[Endpoint] endpoints: (optional) The service configurations
               endpoints.
        """
        self.type = type
        self.endpoints = endpoints

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConfigurationInformationPoints':
        """Initialize a ConfigurationInformationPoints object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (endpoints := _dict.get('endpoints')) is not None:
            args['endpoints'] = [Endpoint.from_dict(v) for v in endpoints]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConfigurationInformationPoints object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'endpoints') and self.endpoints is not None:
            endpoints_list = []
            for v in self.endpoints:
                if isinstance(v, dict):
                    endpoints_list.append(v)
                else:
                    endpoints_list.append(v.to_dict())
            _dict['endpoints'] = endpoints_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConfigurationInformationPoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConfigurationInformationPoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConfigurationInformationPoints') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Control:
    """
    A technical, administrative, or physical safeguard designed to meet a set of defined
    security and privacy requirements.

    :param str control_name: (optional) The ID of the control library that contains
          the profile.
    :param str control_id: (optional) The control name.
    :param str control_description: (optional) The control description.
    :param str control_category: (optional) The association of the control.
    :param str control_parent: (optional) The ID of the parent control.
    :param str control_severity: (optional) Details how important a control is
          should it fail.
    :param List[str] control_tags: tags associated with a control.
    :param List[ControlSpecification] control_specifications: List of control
          specifications associated with the control.
    :param ControlDoc control_docs: (optional) References to a control
          documentation.
    :param str status: (optional) Determines if a control will be evaluated or not.
    """

    def __init__(
        self,
        control_tags: List[str],
        control_specifications: List['ControlSpecification'],
        *,
        control_name: Optional[str] = None,
        control_id: Optional[str] = None,
        control_description: Optional[str] = None,
        control_category: Optional[str] = None,
        control_parent: Optional[str] = None,
        control_severity: Optional[str] = None,
        control_docs: Optional['ControlDoc'] = None,
        status: Optional[str] = None,
    ) -> None:
        """
        Initialize a Control object.

        :param List[str] control_tags: tags associated with a control.
        :param List[ControlSpecification] control_specifications: List of control
               specifications associated with the control.
        :param str control_name: (optional) The ID of the control library that
               contains the profile.
        :param str control_id: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_category: (optional) The association of the control.
        :param str control_parent: (optional) The ID of the parent control.
        :param str control_severity: (optional) Details how important a control is
               should it fail.
        :param ControlDoc control_docs: (optional) References to a control
               documentation.
        :param str status: (optional) Determines if a control will be evaluated or
               not.
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
    def from_dict(cls, _dict: Dict) -> 'Control':
        """Initialize a Control object from a json dictionary."""
        args = {}
        if (control_name := _dict.get('control_name')) is not None:
            args['control_name'] = control_name
        if (control_id := _dict.get('control_id')) is not None:
            args['control_id'] = control_id
        if (control_description := _dict.get('control_description')) is not None:
            args['control_description'] = control_description
        if (control_category := _dict.get('control_category')) is not None:
            args['control_category'] = control_category
        if (control_parent := _dict.get('control_parent')) is not None:
            args['control_parent'] = control_parent
        if (control_severity := _dict.get('control_severity')) is not None:
            args['control_severity'] = control_severity
        if (control_tags := _dict.get('control_tags')) is not None:
            args['control_tags'] = control_tags
        else:
            raise ValueError('Required property \'control_tags\' not present in Control JSON')
        if (control_specifications := _dict.get('control_specifications')) is not None:
            args['control_specifications'] = [ControlSpecification.from_dict(v) for v in control_specifications]
        else:
            raise ValueError('Required property \'control_specifications\' not present in Control JSON')
        if (control_docs := _dict.get('control_docs')) is not None:
            args['control_docs'] = ControlDoc.from_dict(control_docs)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Control object from a json dictionary."""
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
        """Return a `str` version of this Control object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Control') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Control') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlChanges:
    """
    Shows details of the controls that were changed.

    :param int total_added: (optional) How many controls were added.
    :param int total_removed: (optional) How many controls were removed.
    :param int total_updated: (optional) How many controls were updated.
    :param List[ProfileControlsInResponse] added: A list of controls that were
          added.
    :param List[ProfileControlsInResponse] removed: A list of controls that were
          removed.
    :param List[ControlChangesUpdated] updated: A list of controls that were
          updated.
    """

    def __init__(
        self,
        added: List['ProfileControlsInResponse'],
        removed: List['ProfileControlsInResponse'],
        updated: List['ControlChangesUpdated'],
        *,
        total_added: Optional[int] = None,
        total_removed: Optional[int] = None,
        total_updated: Optional[int] = None,
    ) -> None:
        """
        Initialize a ControlChanges object.

        :param List[ProfileControlsInResponse] added: A list of controls that were
               added.
        :param List[ProfileControlsInResponse] removed: A list of controls that
               were removed.
        :param List[ControlChangesUpdated] updated: A list of controls that were
               updated.
        :param int total_added: (optional) How many controls were added.
        :param int total_removed: (optional) How many controls were removed.
        :param int total_updated: (optional) How many controls were updated.
        """
        self.total_added = total_added
        self.total_removed = total_removed
        self.total_updated = total_updated
        self.added = added
        self.removed = removed
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlChanges':
        """Initialize a ControlChanges object from a json dictionary."""
        args = {}
        if (total_added := _dict.get('total_added')) is not None:
            args['total_added'] = total_added
        if (total_removed := _dict.get('total_removed')) is not None:
            args['total_removed'] = total_removed
        if (total_updated := _dict.get('total_updated')) is not None:
            args['total_updated'] = total_updated
        if (added := _dict.get('added')) is not None:
            args['added'] = [ProfileControlsInResponse.from_dict(v) for v in added]
        else:
            raise ValueError('Required property \'added\' not present in ControlChanges JSON')
        if (removed := _dict.get('removed')) is not None:
            args['removed'] = [ProfileControlsInResponse.from_dict(v) for v in removed]
        else:
            raise ValueError('Required property \'removed\' not present in ControlChanges JSON')
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = [ControlChangesUpdated.from_dict(v) for v in updated]
        else:
            raise ValueError('Required property \'updated\' not present in ControlChanges JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlChanges object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_added') and self.total_added is not None:
            _dict['total_added'] = self.total_added
        if hasattr(self, 'total_removed') and self.total_removed is not None:
            _dict['total_removed'] = self.total_removed
        if hasattr(self, 'total_updated') and self.total_updated is not None:
            _dict['total_updated'] = self.total_updated
        if hasattr(self, 'added') and self.added is not None:
            added_list = []
            for v in self.added:
                if isinstance(v, dict):
                    added_list.append(v)
                else:
                    added_list.append(v.to_dict())
            _dict['added'] = added_list
        if hasattr(self, 'removed') and self.removed is not None:
            removed_list = []
            for v in self.removed:
                if isinstance(v, dict):
                    removed_list.append(v)
                else:
                    removed_list.append(v.to_dict())
            _dict['removed'] = removed_list
        if hasattr(self, 'updated') and self.updated is not None:
            updated_list = []
            for v in self.updated:
                if isinstance(v, dict):
                    updated_list.append(v)
                else:
                    updated_list.append(v.to_dict())
            _dict['updated'] = updated_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlChanges object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlChanges') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlChanges') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlChangesUpdated:
    """
    Shows the difference in the Controls.

    :param ProfileControlsInResponse current: (optional) The control details for a
          profile.
    :param ProfileControlsInResponse latest: (optional) The control details for a
          profile.
    """

    def __init__(
        self,
        *,
        current: Optional['ProfileControlsInResponse'] = None,
        latest: Optional['ProfileControlsInResponse'] = None,
    ) -> None:
        """
        Initialize a ControlChangesUpdated object.

        :param ProfileControlsInResponse current: (optional) The control details
               for a profile.
        :param ProfileControlsInResponse latest: (optional) The control details for
               a profile.
        """
        self.current = current
        self.latest = latest

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlChangesUpdated':
        """Initialize a ControlChangesUpdated object from a json dictionary."""
        args = {}
        if (current := _dict.get('current')) is not None:
            args['current'] = ProfileControlsInResponse.from_dict(current)
        if (latest := _dict.get('latest')) is not None:
            args['latest'] = ProfileControlsInResponse.from_dict(latest)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlChangesUpdated object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'current') and self.current is not None:
            if isinstance(self.current, dict):
                _dict['current'] = self.current
            else:
                _dict['current'] = self.current.to_dict()
        if hasattr(self, 'latest') and self.latest is not None:
            if isinstance(self.latest, dict):
                _dict['latest'] = self.latest
            else:
                _dict['latest'] = self.latest.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlChangesUpdated object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlChangesUpdated') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlChangesUpdated') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlDoc:
    """
    References to a control documentation.

    :param str control_docs_id: (optional) The ID of the control doc.
    :param str control_docs_type: (optional) The type of the control doc.
    """

    def __init__(
        self,
        *,
        control_docs_id: Optional[str] = None,
        control_docs_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ControlDoc object.

        :param str control_docs_id: (optional) The ID of the control doc.
        :param str control_docs_type: (optional) The type of the control doc.
        """
        self.control_docs_id = control_docs_id
        self.control_docs_type = control_docs_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlDoc':
        """Initialize a ControlDoc object from a json dictionary."""
        args = {}
        if (control_docs_id := _dict.get('control_docs_id')) is not None:
            args['control_docs_id'] = control_docs_id
        if (control_docs_type := _dict.get('control_docs_type')) is not None:
            args['control_docs_type'] = control_docs_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlDoc object from a json dictionary."""
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
        """Return a `str` version of this ControlDoc object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlDoc') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlDoc') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlLibrary:
    """
    A Control Library.

    :param str control_library_name: (optional) The name of the control library.
    :param str control_library_description: (optional) Details of the control
          library.
    :param str control_library_type: Details that the control library is a user
          made(custom) or Security Compliance Center(predefined).
    :param str control_library_version: (optional) The revision number of the
          control library.
    :param List[Control] controls: The list of rules that the control library
          attempts to adhere to.
    :param str id: (optional) The ID of the control library.
    :param str account_id: (optional) The ID of the account associated with the
          creation of the control library.
    :param str version_group_label: (optional) The ETag or version of the Control
          Library.
    :param bool latest: (optional) Shows if the Control Library is the latest.
    :param str created_by: (optional) The ID of the creator of the Control Library.
    :param datetime created_on: (optional) The date-time of the creation.
    :param str updated_by: (optional) The ID of the user who made the last update.
    :param datetime updated_on: (optional) The date-time of the update.
    :param bool hierarchy_enabled: (optional) Determines if the control library has
          any hierarchy.
    :param int controls_count: (optional) The count of controls tied to the control
          library.
    :param int control_parents_count: (optional) THe count of control parents in the
          control library.
    """

    def __init__(
        self,
        control_library_type: str,
        controls: List['Control'],
        *,
        control_library_name: Optional[str] = None,
        control_library_description: Optional[str] = None,
        control_library_version: Optional[str] = None,
        id: Optional[str] = None,
        account_id: Optional[str] = None,
        version_group_label: Optional[str] = None,
        latest: Optional[bool] = None,
        created_by: Optional[str] = None,
        created_on: Optional[datetime] = None,
        updated_by: Optional[str] = None,
        updated_on: Optional[datetime] = None,
        hierarchy_enabled: Optional[bool] = None,
        controls_count: Optional[int] = None,
        control_parents_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ControlLibrary object.

        :param str control_library_type: Details that the control library is a user
               made(custom) or Security Compliance Center(predefined).
        :param List[Control] controls: The list of rules that the control library
               attempts to adhere to.
        :param str control_library_name: (optional) The name of the control
               library.
        :param str control_library_description: (optional) Details of the control
               library.
        :param str control_library_version: (optional) The revision number of the
               control library.
        :param str id: (optional) The ID of the control library.
        :param str account_id: (optional) The ID of the account associated with the
               creation of the control library.
        :param str version_group_label: (optional) The ETag or version of the
               Control Library.
        :param bool latest: (optional) Shows if the Control Library is the latest.
        :param str created_by: (optional) The ID of the creator of the Control
               Library.
        :param datetime created_on: (optional) The date-time of the creation.
        :param str updated_by: (optional) The ID of the user who made the last
               update.
        :param datetime updated_on: (optional) The date-time of the update.
        :param bool hierarchy_enabled: (optional) Determines if the control library
               has any hierarchy.
        :param int controls_count: (optional) The count of controls tied to the
               control library.
        :param int control_parents_count: (optional) THe count of control parents
               in the control library.
        """
        self.control_library_name = control_library_name
        self.control_library_description = control_library_description
        self.control_library_type = control_library_type
        self.control_library_version = control_library_version
        self.controls = controls
        self.id = id
        self.account_id = account_id
        self.version_group_label = version_group_label
        self.latest = latest
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.hierarchy_enabled = hierarchy_enabled
        self.controls_count = controls_count
        self.control_parents_count = control_parents_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibrary':
        """Initialize a ControlLibrary object from a json dictionary."""
        args = {}
        if (control_library_name := _dict.get('control_library_name')) is not None:
            args['control_library_name'] = control_library_name
        if (control_library_description := _dict.get('control_library_description')) is not None:
            args['control_library_description'] = control_library_description
        if (control_library_type := _dict.get('control_library_type')) is not None:
            args['control_library_type'] = control_library_type
        else:
            raise ValueError('Required property \'control_library_type\' not present in ControlLibrary JSON')
        if (control_library_version := _dict.get('control_library_version')) is not None:
            args['control_library_version'] = control_library_version
        if (controls := _dict.get('controls')) is not None:
            args['controls'] = [Control.from_dict(v) for v in controls]
        else:
            raise ValueError('Required property \'controls\' not present in ControlLibrary JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (version_group_label := _dict.get('version_group_label')) is not None:
            args['version_group_label'] = version_group_label
        if (latest := _dict.get('latest')) is not None:
            args['latest'] = latest
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        if (hierarchy_enabled := _dict.get('hierarchy_enabled')) is not None:
            args['hierarchy_enabled'] = hierarchy_enabled
        if (controls_count := _dict.get('controls_count')) is not None:
            args['controls_count'] = controls_count
        if (control_parents_count := _dict.get('control_parents_count')) is not None:
            args['control_parents_count'] = control_parents_count
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlLibrary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_library_name') and self.control_library_name is not None:
            _dict['control_library_name'] = self.control_library_name
        if hasattr(self, 'control_library_description') and self.control_library_description is not None:
            _dict['control_library_description'] = self.control_library_description
        if hasattr(self, 'control_library_type') and self.control_library_type is not None:
            _dict['control_library_type'] = self.control_library_type
        if hasattr(self, 'control_library_version') and self.control_library_version is not None:
            _dict['control_library_version'] = self.control_library_version
        if hasattr(self, 'controls') and self.controls is not None:
            controls_list = []
            for v in self.controls:
                if isinstance(v, dict):
                    controls_list.append(v)
                else:
                    controls_list.append(v.to_dict())
            _dict['controls'] = controls_list
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
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
        if hasattr(self, 'hierarchy_enabled') and self.hierarchy_enabled is not None:
            _dict['hierarchy_enabled'] = self.hierarchy_enabled
        if hasattr(self, 'controls_count') and self.controls_count is not None:
            _dict['controls_count'] = self.controls_count
        if hasattr(self, 'control_parents_count') and self.control_parents_count is not None:
            _dict['control_parents_count'] = self.control_parents_count
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
        Details that the control library is a user made(custom) or Security Compliance
        Center(predefined).
        """

        CUSTOM = 'custom'
        PREDEFINED = 'predefined'



class ControlLibraryCollection:
    """
    A list of control libraries.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[ControlLibrary] control_libraries: The list of control libraries.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        control_libraries: List['ControlLibrary'],
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
    ) -> None:
        """
        Initialize a ControlLibraryCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param List[ControlLibrary] control_libraries: The list of control
               libraries.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.control_libraries = control_libraries

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlLibraryCollection':
        """Initialize a ControlLibraryCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ControlLibraryCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ControlLibraryCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (control_libraries := _dict.get('control_libraries')) is not None:
            args['control_libraries'] = [ControlLibrary.from_dict(v) for v in control_libraries]
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


class ControlPrototype:
    """
    The payload to instantiate a control.

    :param str control_name: The ID of the control library that contains the
          profile.
    :param str control_description: The control description.
    :param str control_category: The association of the control.
    :param bool control_requirement: true if the control can be automated, false if
          the control cannot.
    :param str control_parent: (optional) The ID of the parent control.
    :param List[ControlSpecificationPrototype] control_specifications: List of
          control specifications associated with the control.
    :param ControlDoc control_docs: (optional) References to a control
          documentation.
    :param str status: (optional) Details if a control library can be used or not.
    """

    def __init__(
        self,
        control_name: str,
        control_description: str,
        control_category: str,
        control_requirement: bool,
        control_specifications: List['ControlSpecificationPrototype'],
        *,
        control_parent: Optional[str] = None,
        control_docs: Optional['ControlDoc'] = None,
        status: Optional[str] = None,
    ) -> None:
        """
        Initialize a ControlPrototype object.

        :param str control_name: The ID of the control library that contains the
               profile.
        :param str control_description: The control description.
        :param str control_category: The association of the control.
        :param bool control_requirement: true if the control can be automated,
               false if the control cannot.
        :param List[ControlSpecificationPrototype] control_specifications: List of
               control specifications associated with the control.
        :param str control_parent: (optional) The ID of the parent control.
        :param ControlDoc control_docs: (optional) References to a control
               documentation.
        :param str status: (optional) Details if a control library can be used or
               not.
        """
        self.control_name = control_name
        self.control_description = control_description
        self.control_category = control_category
        self.control_requirement = control_requirement
        self.control_parent = control_parent
        self.control_specifications = control_specifications
        self.control_docs = control_docs
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlPrototype':
        """Initialize a ControlPrototype object from a json dictionary."""
        args = {}
        if (control_name := _dict.get('control_name')) is not None:
            args['control_name'] = control_name
        else:
            raise ValueError('Required property \'control_name\' not present in ControlPrototype JSON')
        if (control_description := _dict.get('control_description')) is not None:
            args['control_description'] = control_description
        else:
            raise ValueError('Required property \'control_description\' not present in ControlPrototype JSON')
        if (control_category := _dict.get('control_category')) is not None:
            args['control_category'] = control_category
        else:
            raise ValueError('Required property \'control_category\' not present in ControlPrototype JSON')
        if (control_requirement := _dict.get('control_requirement')) is not None:
            args['control_requirement'] = control_requirement
        else:
            raise ValueError('Required property \'control_requirement\' not present in ControlPrototype JSON')
        if (control_parent := _dict.get('control_parent')) is not None:
            args['control_parent'] = control_parent
        if (control_specifications := _dict.get('control_specifications')) is not None:
            args['control_specifications'] = [ControlSpecificationPrototype.from_dict(v) for v in control_specifications]
        else:
            raise ValueError('Required property \'control_specifications\' not present in ControlPrototype JSON')
        if (control_docs := _dict.get('control_docs')) is not None:
            args['control_docs'] = ControlDoc.from_dict(control_docs)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_name') and self.control_name is not None:
            _dict['control_name'] = self.control_name
        if hasattr(self, 'control_description') and self.control_description is not None:
            _dict['control_description'] = self.control_description
        if hasattr(self, 'control_category') and self.control_category is not None:
            _dict['control_category'] = self.control_category
        if hasattr(self, 'control_requirement') and self.control_requirement is not None:
            _dict['control_requirement'] = self.control_requirement
        if hasattr(self, 'control_parent') and self.control_parent is not None:
            _dict['control_parent'] = self.control_parent
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
        """Return a `str` version of this ControlPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlSpecification:
    """
    A statement that defines a security/privacy requirement for a Control.

    :param str id: (optional) The ID of the control.
    :param str responsibility: (optional) Details which party is responsible for the
          implementation of a specification.
    :param str component_id: (optional) The ID of the component.
    :param str component_name: (optional) The name of the component.
    :param str component_type: (optional) The type of component that will use the
          specification.
    :param str environment: (optional) The cloud provider the specification is
          targeting.
    :param str description: (optional) Information about the Control Specification.
    :param int assessments_count: (optional) The number of rules tied to the
          specification.
    :param List[Assessment] assessments: The detailed list of rules associated with
          the Specification.
    """

    def __init__(
        self,
        assessments: List['Assessment'],
        *,
        id: Optional[str] = None,
        responsibility: Optional[str] = None,
        component_id: Optional[str] = None,
        component_name: Optional[str] = None,
        component_type: Optional[str] = None,
        environment: Optional[str] = None,
        description: Optional[str] = None,
        assessments_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ControlSpecification object.

        :param List[Assessment] assessments: The detailed list of rules associated
               with the Specification.
        :param str id: (optional) The ID of the control.
        :param str responsibility: (optional) Details which party is responsible
               for the implementation of a specification.
        :param str component_id: (optional) The ID of the component.
        :param str component_name: (optional) The name of the component.
        :param str component_type: (optional) The type of component that will use
               the specification.
        :param str environment: (optional) The cloud provider the specification is
               targeting.
        :param str description: (optional) Information about the Control
               Specification.
        :param int assessments_count: (optional) The number of rules tied to the
               specification.
        """
        self.id = id
        self.responsibility = responsibility
        self.component_id = component_id
        self.component_name = component_name
        self.component_type = component_type
        self.environment = environment
        self.description = description
        self.assessments_count = assessments_count
        self.assessments = assessments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSpecification':
        """Initialize a ControlSpecification object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (responsibility := _dict.get('responsibility')) is not None:
            args['responsibility'] = responsibility
        if (component_id := _dict.get('component_id')) is not None:
            args['component_id'] = component_id
        if (component_name := _dict.get('component_name')) is not None:
            args['component_name'] = component_name
        if (component_type := _dict.get('component_type')) is not None:
            args['component_type'] = component_type
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (assessments_count := _dict.get('assessments_count')) is not None:
            args['assessments_count'] = assessments_count
        if (assessments := _dict.get('assessments')) is not None:
            args['assessments'] = [Assessment.from_dict(v) for v in assessments]
        else:
            raise ValueError('Required property \'assessments\' not present in ControlSpecification JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlSpecification object from a json dictionary."""
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
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
        if hasattr(self, 'component_type') and self.component_type is not None:
            _dict['component_type'] = self.component_type
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
        """Return a `str` version of this ControlSpecification object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlSpecification') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlSpecification') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlSpecificationPrototype:
    """
    The necessary fields to instantiate a Control Specification.

    :param str component_id: (optional) The ID of the component. The component_id
          can be found from the 'service_name' using the Get Services method.
    :param str environment: (optional) The cloud provider the specification is
          targeting.
    :param str control_specification_id: (optional) The ID of the control
          specification to give when creating the control_specification.
    :param str control_specification_description: (optional) Information about the
          Control Specification.
    :param List[AssessmentPrototype] assessments: (optional) The detailed list of
          rules associated with the Specification.
    """

    def __init__(
        self,
        *,
        component_id: Optional[str] = None,
        environment: Optional[str] = None,
        control_specification_id: Optional[str] = None,
        control_specification_description: Optional[str] = None,
        assessments: Optional[List['AssessmentPrototype']] = None,
    ) -> None:
        """
        Initialize a ControlSpecificationPrototype object.

        :param str component_id: (optional) The ID of the component. The
               component_id can be found from the 'service_name' using the Get Services
               method.
        :param str environment: (optional) The cloud provider the specification is
               targeting.
        :param str control_specification_id: (optional) The ID of the control
               specification to give when creating the control_specification.
        :param str control_specification_description: (optional) Information about
               the Control Specification.
        :param List[AssessmentPrototype] assessments: (optional) The detailed list
               of rules associated with the Specification.
        """
        self.component_id = component_id
        self.environment = environment
        self.control_specification_id = control_specification_id
        self.control_specification_description = control_specification_description
        self.assessments = assessments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSpecificationPrototype':
        """Initialize a ControlSpecificationPrototype object from a json dictionary."""
        args = {}
        if (component_id := _dict.get('component_id')) is not None:
            args['component_id'] = component_id
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (control_specification_id := _dict.get('control_specification_id')) is not None:
            args['control_specification_id'] = control_specification_id
        if (control_specification_description := _dict.get('control_specification_description')) is not None:
            args['control_specification_description'] = control_specification_description
        if (assessments := _dict.get('assessments')) is not None:
            args['assessments'] = [AssessmentPrototype.from_dict(v) for v in assessments]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlSpecificationPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'control_specification_id') and self.control_specification_id is not None:
            _dict['control_specification_id'] = self.control_specification_id
        if hasattr(self, 'control_specification_description') and self.control_specification_description is not None:
            _dict['control_specification_description'] = self.control_specification_description
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
        """Return a `str` version of this ControlSpecificationPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlSpecificationPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlSpecificationPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class EnvironmentEnum(str, Enum):
        """
        The cloud provider the specification is targeting.
        """

        IBM_CLOUD = 'ibm-cloud'



class ControlSpecificationWithStats:
    """
    The control specification with compliance stats.

    :param str control_specification_id: (optional) The control specification ID.
    :param str control_specification_description: (optional) The component
          description.
    :param str component_id: (optional) The component ID.
    :param str component_name: (optional) The components name.
    :param str environment: (optional) The environment.
    :param str responsibility: (optional) The responsibility for managing control
          specifications.
    :param List[AssessmentWithStats] assessments: (optional) The list of
          assessments.
    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of checks.
    :param int compliant_count: (optional) The number of compliant checks.
    :param int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :param int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :param int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :param int not_applicable_count: (optional) The number of not applicable (with
          no evaluations) checks.
    """

    def __init__(
        self,
        status: str,
        *,
        control_specification_id: Optional[str] = None,
        control_specification_description: Optional[str] = None,
        component_id: Optional[str] = None,
        component_name: Optional[str] = None,
        environment: Optional[str] = None,
        responsibility: Optional[str] = None,
        assessments: Optional[List['AssessmentWithStats']] = None,
        total_count: Optional[int] = None,
        compliant_count: Optional[int] = None,
        not_compliant_count: Optional[int] = None,
        unable_to_perform_count: Optional[int] = None,
        user_evaluation_required_count: Optional[int] = None,
        not_applicable_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ControlSpecificationWithStats object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param str control_specification_id: (optional) The control specification
               ID.
        :param str control_specification_description: (optional) The component
               description.
        :param str component_id: (optional) The component ID.
        :param str component_name: (optional) The components name.
        :param str environment: (optional) The environment.
        :param str responsibility: (optional) The responsibility for managing
               control specifications.
        :param List[AssessmentWithStats] assessments: (optional) The list of
               assessments.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param int not_applicable_count: (optional) The number of not applicable
               (with no evaluations) checks.
        """
        self.control_specification_id = control_specification_id
        self.control_specification_description = control_specification_description
        self.component_id = component_id
        self.component_name = component_name
        self.environment = environment
        self.responsibility = responsibility
        self.assessments = assessments
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.not_applicable_count = not_applicable_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSpecificationWithStats':
        """Initialize a ControlSpecificationWithStats object from a json dictionary."""
        args = {}
        if (control_specification_id := _dict.get('control_specification_id')) is not None:
            args['control_specification_id'] = control_specification_id
        if (control_specification_description := _dict.get('control_specification_description')) is not None:
            args['control_specification_description'] = control_specification_description
        if (component_id := _dict.get('component_id')) is not None:
            args['component_id'] = component_id
        if (component_name := _dict.get('component_name')) is not None:
            args['component_name'] = component_name
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (responsibility := _dict.get('responsibility')) is not None:
            args['responsibility'] = responsibility
        if (assessments := _dict.get('assessments')) is not None:
            args['assessments'] = [AssessmentWithStats.from_dict(v) for v in assessments]
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ControlSpecificationWithStats JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (compliant_count := _dict.get('compliant_count')) is not None:
            args['compliant_count'] = compliant_count
        if (not_compliant_count := _dict.get('not_compliant_count')) is not None:
            args['not_compliant_count'] = not_compliant_count
        if (unable_to_perform_count := _dict.get('unable_to_perform_count')) is not None:
            args['unable_to_perform_count'] = unable_to_perform_count
        if (user_evaluation_required_count := _dict.get('user_evaluation_required_count')) is not None:
            args['user_evaluation_required_count'] = user_evaluation_required_count
        if (not_applicable_count := _dict.get('not_applicable_count')) is not None:
            args['not_applicable_count'] = not_applicable_count
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
        if hasattr(self, 'control_specification_description') and self.control_specification_description is not None:
            _dict['control_specification_description'] = self.control_specification_description
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
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
        if hasattr(self, 'not_applicable_count') and self.not_applicable_count is not None:
            _dict['not_applicable_count'] = self.not_applicable_count
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
        NOT_APPLICABLE = 'not_applicable'



class ControlSummary:
    """
    The summary of the control.

    :param str id: (optional) The controls ID.
    :param str control_name: (optional) The controls name.
    :param str control_description: (optional) The controls description.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        control_name: Optional[str] = None,
        control_description: Optional[str] = None,
    ) -> None:
        """
        Initialize a ControlSummary object.

        :param str id: (optional) The controls ID.
        :param str control_name: (optional) The controls name.
        :param str control_description: (optional) The controls description.
        """
        self.id = id
        self.control_name = control_name
        self.control_description = control_description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlSummary':
        """Initialize a ControlSummary object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (control_name := _dict.get('control_name')) is not None:
            args['control_name'] = control_name
        if (control_description := _dict.get('control_description')) is not None:
            args['control_description'] = control_description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'control_name') and self.control_name is not None:
            _dict['control_name'] = self.control_name
        if hasattr(self, 'control_description') and self.control_description is not None:
            _dict['control_description'] = self.control_description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ControlSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ControlSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ControlSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ControlWithStats:
    """
    The control with compliance stats.

    :param str report_id: (optional) The report ID.
    :param str home_account_id: (optional) The home account ID.
    :param str id: (optional) The control ID.
    :param str control_library_id: (optional) The control library ID.
    :param str control_library_version: (optional) The control library version.
    :param str control_name: (optional) The control name.
    :param str control_description: (optional) The control description.
    :param str control_category: (optional) The control category.
    :param List[ControlSpecificationWithStats] control_specifications: (optional)
          The list of specifications that are on the page.
    :param Tags resource_tags: (optional) The collection of different types of tags.
    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of checks.
    :param int compliant_count: (optional) The number of compliant checks.
    :param int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :param int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :param int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :param int not_applicable_count: (optional) The number of not applicable (with
          no evaluations) checks.
    """

    def __init__(
        self,
        status: str,
        *,
        report_id: Optional[str] = None,
        home_account_id: Optional[str] = None,
        id: Optional[str] = None,
        control_library_id: Optional[str] = None,
        control_library_version: Optional[str] = None,
        control_name: Optional[str] = None,
        control_description: Optional[str] = None,
        control_category: Optional[str] = None,
        control_specifications: Optional[List['ControlSpecificationWithStats']] = None,
        resource_tags: Optional['Tags'] = None,
        total_count: Optional[int] = None,
        compliant_count: Optional[int] = None,
        not_compliant_count: Optional[int] = None,
        unable_to_perform_count: Optional[int] = None,
        user_evaluation_required_count: Optional[int] = None,
        not_applicable_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ControlWithStats object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param str report_id: (optional) The report ID.
        :param str home_account_id: (optional) The home account ID.
        :param str id: (optional) The control ID.
        :param str control_library_id: (optional) The control library ID.
        :param str control_library_version: (optional) The control library version.
        :param str control_name: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_category: (optional) The control category.
        :param List[ControlSpecificationWithStats] control_specifications:
               (optional) The list of specifications that are on the page.
        :param Tags resource_tags: (optional) The collection of different types of
               tags.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param int not_applicable_count: (optional) The number of not applicable
               (with no evaluations) checks.
        """
        self.report_id = report_id
        self.home_account_id = home_account_id
        self.id = id
        self.control_library_id = control_library_id
        self.control_library_version = control_library_version
        self.control_name = control_name
        self.control_description = control_description
        self.control_category = control_category
        self.control_specifications = control_specifications
        self.resource_tags = resource_tags
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.not_applicable_count = not_applicable_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ControlWithStats':
        """Initialize a ControlWithStats object from a json dictionary."""
        args = {}
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (control_library_id := _dict.get('control_library_id')) is not None:
            args['control_library_id'] = control_library_id
        if (control_library_version := _dict.get('control_library_version')) is not None:
            args['control_library_version'] = control_library_version
        if (control_name := _dict.get('control_name')) is not None:
            args['control_name'] = control_name
        if (control_description := _dict.get('control_description')) is not None:
            args['control_description'] = control_description
        if (control_category := _dict.get('control_category')) is not None:
            args['control_category'] = control_category
        if (control_specifications := _dict.get('control_specifications')) is not None:
            args['control_specifications'] = [ControlSpecificationWithStats.from_dict(v) for v in control_specifications]
        if (resource_tags := _dict.get('resource_tags')) is not None:
            args['resource_tags'] = Tags.from_dict(resource_tags)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ControlWithStats JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (compliant_count := _dict.get('compliant_count')) is not None:
            args['compliant_count'] = compliant_count
        if (not_compliant_count := _dict.get('not_compliant_count')) is not None:
            args['not_compliant_count'] = not_compliant_count
        if (unable_to_perform_count := _dict.get('unable_to_perform_count')) is not None:
            args['unable_to_perform_count'] = unable_to_perform_count
        if (user_evaluation_required_count := _dict.get('user_evaluation_required_count')) is not None:
            args['user_evaluation_required_count'] = user_evaluation_required_count
        if (not_applicable_count := _dict.get('not_applicable_count')) is not None:
            args['not_applicable_count'] = not_applicable_count
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ControlWithStats object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
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
        if hasattr(self, 'control_specifications') and self.control_specifications is not None:
            control_specifications_list = []
            for v in self.control_specifications:
                if isinstance(v, dict):
                    control_specifications_list.append(v)
                else:
                    control_specifications_list.append(v.to_dict())
            _dict['control_specifications'] = control_specifications_list
        if hasattr(self, 'resource_tags') and self.resource_tags is not None:
            if isinstance(self.resource_tags, dict):
                _dict['resource_tags'] = self.resource_tags
            else:
                _dict['resource_tags'] = self.resource_tags.to_dict()
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
        if hasattr(self, 'not_applicable_count') and self.not_applicable_count is not None:
            _dict['not_applicable_count'] = self.not_applicable_count
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
        NOT_APPLICABLE = 'not_applicable'



class CreateScanReport:
    """
    The scan report ID.

    :param str id: (optional) The scan report ID.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateScanReport object.

        :param str id: (optional) The scan report ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateScanReport':
        """Initialize a CreateScanReport object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateScanReport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateScanReport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateScanReport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateScanReport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateScanResponse:
    """
    The response that details the whether starting a scan was successful.

    :param str id: (optional) The ID of the scan generated.
    :param str account_id: (optional) The ID of the account associated with the
          scan.
    :param str attachment_id: (optional) The ID of the profile attachment associated
          with the scan.
    :param str report_id: (optional) The ID of the report associated with the scan.
    :param str status: (optional) Details the state of a scan.
    :param datetime last_scan_time: (optional) The last time a scan was performed.
    :param datetime next_scan_time: (optional) The next time a scan will be
          triggered.
    :param str scan_type: (optional) Shows how a scan gets triggered.
    :param int occurence: (optional) The number of times the scan appeared.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        account_id: Optional[str] = None,
        attachment_id: Optional[str] = None,
        report_id: Optional[str] = None,
        status: Optional[str] = None,
        last_scan_time: Optional[datetime] = None,
        next_scan_time: Optional[datetime] = None,
        scan_type: Optional[str] = None,
        occurence: Optional[int] = None,
    ) -> None:
        """
        Initialize a CreateScanResponse object.

        :param str id: (optional) The ID of the scan generated.
        :param str account_id: (optional) The ID of the account associated with the
               scan.
        :param str attachment_id: (optional) The ID of the profile attachment
               associated with the scan.
        :param str report_id: (optional) The ID of the report associated with the
               scan.
        :param str status: (optional) Details the state of a scan.
        :param datetime last_scan_time: (optional) The last time a scan was
               performed.
        :param datetime next_scan_time: (optional) The next time a scan will be
               triggered.
        :param str scan_type: (optional) Shows how a scan gets triggered.
        :param int occurence: (optional) The number of times the scan appeared.
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
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (attachment_id := _dict.get('attachment_id')) is not None:
            args['attachment_id'] = attachment_id
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (last_scan_time := _dict.get('last_scan_time')) is not None:
            args['last_scan_time'] = string_to_datetime(last_scan_time)
        if (next_scan_time := _dict.get('next_scan_time')) is not None:
            args['next_scan_time'] = string_to_datetime(next_scan_time)
        if (scan_type := _dict.get('scan_type')) is not None:
            args['scan_type'] = scan_type
        if (occurence := _dict.get('occurence')) is not None:
            args['occurence'] = occurence
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
            _dict['last_scan_time'] = datetime_to_string(self.last_scan_time)
        if hasattr(self, 'next_scan_time') and self.next_scan_time is not None:
            _dict['next_scan_time'] = datetime_to_string(self.next_scan_time)
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


class Credential:
    """
    Credential.

    :param str secret_crn: The CRN of the secret.
    :param List[Resource] resources: Credential having service name and instance
          crn.
    """

    def __init__(
        self,
        secret_crn: str,
        resources: List['Resource'],
    ) -> None:
        """
        Initialize a Credential object.

        :param str secret_crn: The CRN of the secret.
        :param List[Resource] resources: Credential having service name and
               instance crn.
        """
        self.secret_crn = secret_crn
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Credential':
        """Initialize a Credential object from a json dictionary."""
        args = {}
        if (secret_crn := _dict.get('secret_crn')) is not None:
            args['secret_crn'] = secret_crn
        else:
            raise ValueError('Required property \'secret_crn\' not present in Credential JSON')
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [Resource.from_dict(v) for v in resources]
        else:
            raise ValueError('Required property \'resources\' not present in Credential JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Credential object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'secret_crn') and self.secret_crn is not None:
            _dict['secret_crn'] = self.secret_crn
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
        """Return a `str` version of this Credential object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Credential') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Credential') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CredentialResponse:
    """
    CredentialResponse.

    :param str type: The type of the credential.
    :param str secret_crn: The CRN of the secret.
    :param str secret_name: (optional) The name of the secret.
    :param List[Resource] resources: Credential having service name and instance
          crn.
    """

    def __init__(
        self,
        type: str,
        secret_crn: str,
        resources: List['Resource'],
        *,
        secret_name: Optional[str] = None,
    ) -> None:
        """
        Initialize a CredentialResponse object.

        :param str type: The type of the credential.
        :param str secret_crn: The CRN of the secret.
        :param List[Resource] resources: Credential having service name and
               instance crn.
        :param str secret_name: (optional) The name of the secret.
        """
        self.type = type
        self.secret_crn = secret_crn
        self.secret_name = secret_name
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CredentialResponse':
        """Initialize a CredentialResponse object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in CredentialResponse JSON')
        if (secret_crn := _dict.get('secret_crn')) is not None:
            args['secret_crn'] = secret_crn
        else:
            raise ValueError('Required property \'secret_crn\' not present in CredentialResponse JSON')
        if (secret_name := _dict.get('secret_name')) is not None:
            args['secret_name'] = secret_name
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [Resource.from_dict(v) for v in resources]
        else:
            raise ValueError('Required property \'resources\' not present in CredentialResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CredentialResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'secret_crn') and self.secret_crn is not None:
            _dict['secret_crn'] = self.secret_crn
        if hasattr(self, 'secret_name') and self.secret_name is not None:
            _dict['secret_name'] = self.secret_name
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
        """Return a `str` version of this CredentialResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CredentialResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CredentialResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefaultParameters:
    """
    The parameters of the profile that are inherently set by the profile.

    :param str assessment_type: (optional) The type of the implementation.
    :param str assessment_id: (optional) The implementation ID of the parameter.
    :param str parameter_name: (optional) The parameter's name.
    :param str parameter_default_value: (optional) The default value of the
          parameter.
    :param str parameter_display_name: (optional) The parameter display name.
    :param str parameter_type: (optional) The parameter type.
    """

    def __init__(
        self,
        *,
        assessment_type: Optional[str] = None,
        assessment_id: Optional[str] = None,
        parameter_name: Optional[str] = None,
        parameter_default_value: Optional[str] = None,
        parameter_display_name: Optional[str] = None,
        parameter_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a DefaultParameters object.

        :param str assessment_type: (optional) The type of the implementation.
        :param str assessment_id: (optional) The implementation ID of the
               parameter.
        :param str parameter_name: (optional) The parameter's name.
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
        if (assessment_type := _dict.get('assessment_type')) is not None:
            args['assessment_type'] = assessment_type
        if (assessment_id := _dict.get('assessment_id')) is not None:
            args['assessment_id'] = assessment_id
        if (parameter_name := _dict.get('parameter_name')) is not None:
            args['parameter_name'] = parameter_name
        if (parameter_default_value := _dict.get('parameter_default_value')) is not None:
            args['parameter_default_value'] = parameter_default_value
        if (parameter_display_name := _dict.get('parameter_display_name')) is not None:
            args['parameter_display_name'] = parameter_display_name
        if (parameter_type := _dict.get('parameter_type')) is not None:
            args['parameter_type'] = parameter_type
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


class DefaultParametersChanges:
    """
    Shows details of the parameters that were changed.

    :param int total_added: (optional) Number of parameters added.
    :param int total_removed: (optional) Number of parameters removed.
    :param int total_updated: (optional) Number of parameters updated.
    :param List[DefaultParameters] added: List of parameters added.
    :param List[DefaultParameters] removed: List of parameters removed.
    :param List[DefaultParametersDifference] updated: List of parameters updated.
    """

    def __init__(
        self,
        added: List['DefaultParameters'],
        removed: List['DefaultParameters'],
        updated: List['DefaultParametersDifference'],
        *,
        total_added: Optional[int] = None,
        total_removed: Optional[int] = None,
        total_updated: Optional[int] = None,
    ) -> None:
        """
        Initialize a DefaultParametersChanges object.

        :param List[DefaultParameters] added: List of parameters added.
        :param List[DefaultParameters] removed: List of parameters removed.
        :param List[DefaultParametersDifference] updated: List of parameters
               updated.
        :param int total_added: (optional) Number of parameters added.
        :param int total_removed: (optional) Number of parameters removed.
        :param int total_updated: (optional) Number of parameters updated.
        """
        self.total_added = total_added
        self.total_removed = total_removed
        self.total_updated = total_updated
        self.added = added
        self.removed = removed
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultParametersChanges':
        """Initialize a DefaultParametersChanges object from a json dictionary."""
        args = {}
        if (total_added := _dict.get('total_added')) is not None:
            args['total_added'] = total_added
        if (total_removed := _dict.get('total_removed')) is not None:
            args['total_removed'] = total_removed
        if (total_updated := _dict.get('total_updated')) is not None:
            args['total_updated'] = total_updated
        if (added := _dict.get('added')) is not None:
            args['added'] = [DefaultParameters.from_dict(v) for v in added]
        else:
            raise ValueError('Required property \'added\' not present in DefaultParametersChanges JSON')
        if (removed := _dict.get('removed')) is not None:
            args['removed'] = [DefaultParameters.from_dict(v) for v in removed]
        else:
            raise ValueError('Required property \'removed\' not present in DefaultParametersChanges JSON')
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = [DefaultParametersDifference.from_dict(v) for v in updated]
        else:
            raise ValueError('Required property \'updated\' not present in DefaultParametersChanges JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultParametersChanges object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_added') and self.total_added is not None:
            _dict['total_added'] = self.total_added
        if hasattr(self, 'total_removed') and self.total_removed is not None:
            _dict['total_removed'] = self.total_removed
        if hasattr(self, 'total_updated') and self.total_updated is not None:
            _dict['total_updated'] = self.total_updated
        if hasattr(self, 'added') and self.added is not None:
            added_list = []
            for v in self.added:
                if isinstance(v, dict):
                    added_list.append(v)
                else:
                    added_list.append(v.to_dict())
            _dict['added'] = added_list
        if hasattr(self, 'removed') and self.removed is not None:
            removed_list = []
            for v in self.removed:
                if isinstance(v, dict):
                    removed_list.append(v)
                else:
                    removed_list.append(v.to_dict())
            _dict['removed'] = removed_list
        if hasattr(self, 'updated') and self.updated is not None:
            updated_list = []
            for v in self.updated:
                if isinstance(v, dict):
                    updated_list.append(v)
                else:
                    updated_list.append(v.to_dict())
            _dict['updated'] = updated_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultParametersChanges object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultParametersChanges') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultParametersChanges') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefaultParametersDifference:
    """
    Details the difference between the current parameters compared to the latest.

    :param DefaultParameters current: (optional) The parameters of the profile that
          are inherently set by the profile.
    :param DefaultParameters latest: (optional) The parameters of the profile that
          are inherently set by the profile.
    """

    def __init__(
        self,
        *,
        current: Optional['DefaultParameters'] = None,
        latest: Optional['DefaultParameters'] = None,
    ) -> None:
        """
        Initialize a DefaultParametersDifference object.

        :param DefaultParameters current: (optional) The parameters of the profile
               that are inherently set by the profile.
        :param DefaultParameters latest: (optional) The parameters of the profile
               that are inherently set by the profile.
        """
        self.current = current
        self.latest = latest

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefaultParametersDifference':
        """Initialize a DefaultParametersDifference object from a json dictionary."""
        args = {}
        if (current := _dict.get('current')) is not None:
            args['current'] = DefaultParameters.from_dict(current)
        if (latest := _dict.get('latest')) is not None:
            args['latest'] = DefaultParameters.from_dict(latest)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefaultParametersDifference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'current') and self.current is not None:
            if isinstance(self.current, dict):
                _dict['current'] = self.current
            else:
                _dict['current'] = self.current.to_dict()
        if hasattr(self, 'latest') and self.latest is not None:
            if isinstance(self.latest, dict):
                _dict['latest'] = self.latest
            else:
                _dict['latest'] = self.latest.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefaultParametersDifference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefaultParametersDifference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefaultParametersDifference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Endpoint:
    """
    The service configurations endpoint.

    :param str host: (optional) The endpoint host.
    :param str path: (optional) The endpoint path.
    :param str region: (optional) The endpoint region.
    :param int advisory_call_limit: (optional) The endpoints advisory call limit.
    """

    def __init__(
        self,
        *,
        host: Optional[str] = None,
        path: Optional[str] = None,
        region: Optional[str] = None,
        advisory_call_limit: Optional[int] = None,
    ) -> None:
        """
        Initialize a Endpoint object.

        :param str host: (optional) The endpoint host.
        :param str path: (optional) The endpoint path.
        :param str region: (optional) The endpoint region.
        :param int advisory_call_limit: (optional) The endpoints advisory call
               limit.
        """
        self.host = host
        self.path = path
        self.region = region
        self.advisory_call_limit = advisory_call_limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Endpoint':
        """Initialize a Endpoint object from a json dictionary."""
        args = {}
        if (host := _dict.get('host')) is not None:
            args['host'] = host
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (region := _dict.get('region')) is not None:
            args['region'] = region
        if (advisory_call_limit := _dict.get('advisory_call_limit')) is not None:
            args['advisory_call_limit'] = advisory_call_limit
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Endpoint object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'advisory_call_limit') and self.advisory_call_limit is not None:
            _dict['advisory_call_limit'] = self.advisory_call_limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Endpoint object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Endpoint') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Endpoint') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EvalStats:
    """
    The evaluation stats.

    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of evaluations.
    :param int pass_count: (optional) The number of passed evaluations.
    :param int failure_count: (optional) The number of failed evaluations.
    :param int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :param int skipped_count: (optional) The number of assessments with no
          corresponding evaluations.
    :param int completed_count: (optional) The total number of completed
          evaluations.
    """

    def __init__(
        self,
        status: str,
        *,
        total_count: Optional[int] = None,
        pass_count: Optional[int] = None,
        failure_count: Optional[int] = None,
        error_count: Optional[int] = None,
        skipped_count: Optional[int] = None,
        completed_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a EvalStats object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int skipped_count: (optional) The number of assessments with no
               corresponding evaluations.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        """
        self.status = status
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.skipped_count = skipped_count
        self.completed_count = completed_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvalStats':
        """Initialize a EvalStats object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in EvalStats JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (pass_count := _dict.get('pass_count')) is not None:
            args['pass_count'] = pass_count
        if (failure_count := _dict.get('failure_count')) is not None:
            args['failure_count'] = failure_count
        if (error_count := _dict.get('error_count')) is not None:
            args['error_count'] = error_count
        if (skipped_count := _dict.get('skipped_count')) is not None:
            args['skipped_count'] = skipped_count
        if (completed_count := _dict.get('completed_count')) is not None:
            args['completed_count'] = completed_count
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
        if hasattr(self, 'skipped_count') and self.skipped_count is not None:
            _dict['skipped_count'] = self.skipped_count
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
        NOT_APPLICABLE = 'not_applicable'



class Evaluation:
    """
    The evaluation of a control specification assessment.

    :param str report_id: (optional) The ID of the report that is associated to the
          evaluation.
    :param str home_account_id: (optional) The ID of the home account.
    :param str component_id: (optional) The component ID.
    :param str component_name: (optional) The components name.
    :param Assessment assessment: (optional) The control specification assessment.
    :param str evaluate_time: (optional) The time when the evaluation was made.
    :param TargetInfo target: (optional) The evaluation target.
    :param str status: The allowed values of an evaluation status.
    :param str reason: (optional) The reason for the evaluation failure.
    :param EvaluationDetails details: (optional) A list of details related to the
          Evaluation.
    :param str evaluated_by: (optional) By whom the evaluation was made for erictree
          results.
    """

    def __init__(
        self,
        status: str,
        *,
        report_id: Optional[str] = None,
        home_account_id: Optional[str] = None,
        component_id: Optional[str] = None,
        component_name: Optional[str] = None,
        assessment: Optional['Assessment'] = None,
        evaluate_time: Optional[str] = None,
        target: Optional['TargetInfo'] = None,
        reason: Optional[str] = None,
        details: Optional['EvaluationDetails'] = None,
        evaluated_by: Optional[str] = None,
    ) -> None:
        """
        Initialize a Evaluation object.

        :param str status: The allowed values of an evaluation status.
        :param str report_id: (optional) The ID of the report that is associated to
               the evaluation.
        :param str home_account_id: (optional) The ID of the home account.
        :param str component_id: (optional) The component ID.
        :param str component_name: (optional) The components name.
        :param Assessment assessment: (optional) The control specification
               assessment.
        :param str evaluate_time: (optional) The time when the evaluation was made.
        :param TargetInfo target: (optional) The evaluation target.
        :param str reason: (optional) The reason for the evaluation failure.
        :param EvaluationDetails details: (optional) A list of details related to
               the Evaluation.
        :param str evaluated_by: (optional) By whom the evaluation was made for
               erictree results.
        """
        self.report_id = report_id
        self.home_account_id = home_account_id
        self.component_id = component_id
        self.component_name = component_name
        self.assessment = assessment
        self.evaluate_time = evaluate_time
        self.target = target
        self.status = status
        self.reason = reason
        self.details = details
        self.evaluated_by = evaluated_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Evaluation':
        """Initialize a Evaluation object from a json dictionary."""
        args = {}
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (component_id := _dict.get('component_id')) is not None:
            args['component_id'] = component_id
        if (component_name := _dict.get('component_name')) is not None:
            args['component_name'] = component_name
        if (assessment := _dict.get('assessment')) is not None:
            args['assessment'] = Assessment.from_dict(assessment)
        if (evaluate_time := _dict.get('evaluate_time')) is not None:
            args['evaluate_time'] = evaluate_time
        if (target := _dict.get('target')) is not None:
            args['target'] = TargetInfo.from_dict(target)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in Evaluation JSON')
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (details := _dict.get('details')) is not None:
            args['details'] = EvaluationDetails.from_dict(details)
        if (evaluated_by := _dict.get('evaluated_by')) is not None:
            args['evaluated_by'] = evaluated_by
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Evaluation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
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
        if hasattr(self, 'evaluated_by') and self.evaluated_by is not None:
            _dict['evaluated_by'] = self.evaluated_by
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



class EvaluationDetails:
    """
    A list of details related to the Evaluation.

    :param List[EvaluationProperty] properties: (optional) Details the evaluations
          that were incorrect.
    :param EvaluationProviderInfo provider_info: (optional) The source provider of
          the evaluation.
    """

    def __init__(
        self,
        *,
        properties: Optional[List['EvaluationProperty']] = None,
        provider_info: Optional['EvaluationProviderInfo'] = None,
    ) -> None:
        """
        Initialize a EvaluationDetails object.

        :param List[EvaluationProperty] properties: (optional) Details the
               evaluations that were incorrect.
        :param EvaluationProviderInfo provider_info: (optional) The source provider
               of the evaluation.
        """
        self.properties = properties
        self.provider_info = provider_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvaluationDetails':
        """Initialize a EvaluationDetails object from a json dictionary."""
        args = {}
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [EvaluationProperty.from_dict(v) for v in properties]
        if (provider_info := _dict.get('provider_info')) is not None:
            args['provider_info'] = EvaluationProviderInfo.from_dict(provider_info)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvaluationDetails object from a json dictionary."""
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
        if hasattr(self, 'provider_info') and self.provider_info is not None:
            if isinstance(self.provider_info, dict):
                _dict['provider_info'] = self.provider_info
            else:
                _dict['provider_info'] = self.provider_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EvaluationDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EvaluationDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EvaluationDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EvaluationPage:
    """
    The page of assessment evaluations.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param str report_id: (optional) The ID of the report.
    :param str home_account_id: (optional) The ID of the home account.
    :param List[Evaluation] evaluations: (optional) The list of evaluations that are
          on the page.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
        report_id: Optional[str] = None,
        home_account_id: Optional[str] = None,
        evaluations: Optional[List['Evaluation']] = None,
    ) -> None:
        """
        Initialize a EvaluationPage object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        :param str report_id: (optional) The ID of the report.
        :param str home_account_id: (optional) The ID of the home account.
        :param List[Evaluation] evaluations: (optional) The list of evaluations
               that are on the page.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.report_id = report_id
        self.home_account_id = home_account_id
        self.evaluations = evaluations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvaluationPage':
        """Initialize a EvaluationPage object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in EvaluationPage JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in EvaluationPage JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (evaluations := _dict.get('evaluations')) is not None:
            args['evaluations'] = [Evaluation.from_dict(v) for v in evaluations]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvaluationPage object from a json dictionary."""
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
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
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


class EvaluationProperty:
    """
    An aspect of the evaluation.

    :param str property: (optional) The attribute of the resource.
    :param str property_description: (optional) An explanation of the resourcer.
    :param str operator: The operator used during the evaluation.
    :param object expected_value: (optional)
    :param object found_value: (optional)
    """

    def __init__(
        self,
        operator: str,
        *,
        property: Optional[str] = None,
        property_description: Optional[str] = None,
        expected_value: Optional[object] = None,
        found_value: Optional[object] = None,
    ) -> None:
        """
        Initialize a EvaluationProperty object.

        :param str operator: The operator used during the evaluation.
        :param str property: (optional) The attribute of the resource.
        :param str property_description: (optional) An explanation of the
               resourcer.
        :param object expected_value: (optional)
        :param object found_value: (optional)
        """
        self.property = property
        self.property_description = property_description
        self.operator = operator
        self.expected_value = expected_value
        self.found_value = found_value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvaluationProperty':
        """Initialize a EvaluationProperty object from a json dictionary."""
        args = {}
        if (property := _dict.get('property')) is not None:
            args['property'] = property
        if (property_description := _dict.get('property_description')) is not None:
            args['property_description'] = property_description
        if (operator := _dict.get('operator')) is not None:
            args['operator'] = operator
        else:
            raise ValueError('Required property \'operator\' not present in EvaluationProperty JSON')
        if (expected_value := _dict.get('expected_value')) is not None:
            args['expected_value'] = expected_value
        if (found_value := _dict.get('found_value')) is not None:
            args['found_value'] = found_value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvaluationProperty object from a json dictionary."""
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
        """Return a `str` version of this EvaluationProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EvaluationProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EvaluationProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OperatorEnum(str, Enum):
        """
        The operator used during the evaluation.
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



class EvaluationProviderInfo:
    """
    The source provider of the evaluation.

    :param str provider_type: (optional) Details the source of the evaluation.
    """

    def __init__(
        self,
        *,
        provider_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a EvaluationProviderInfo object.

        :param str provider_type: (optional) Details the source of the evaluation.
        """
        self.provider_type = provider_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EvaluationProviderInfo':
        """Initialize a EvaluationProviderInfo object from a json dictionary."""
        args = {}
        if (provider_type := _dict.get('provider_type')) is not None:
            args['provider_type'] = provider_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EvaluationProviderInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_type') and self.provider_type is not None:
            _dict['provider_type'] = self.provider_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EvaluationProviderInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EvaluationProviderInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EvaluationProviderInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EventNotifications:
    """
    The Event Notifications settings.

    :param str instance_crn: (optional) The Event Notifications instance CRN.
    :param datetime updated_on: (optional) The date when the Event Notifications
          connection was updated.
    :param str source_id: (optional) The connected Security and Compliance Center
          instance CRN.
    :param str source_description: (optional) The description of the source of the
          Event Notifications.
    :param str source_name: (optional) The name of the source of the Event
          Notifications.
    """

    def __init__(
        self,
        *,
        instance_crn: Optional[str] = None,
        updated_on: Optional[datetime] = None,
        source_id: Optional[str] = None,
        source_description: Optional[str] = None,
        source_name: Optional[str] = None,
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
        if (instance_crn := _dict.get('instance_crn')) is not None:
            args['instance_crn'] = instance_crn
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        if (source_id := _dict.get('source_id')) is not None:
            args['source_id'] = source_id
        if (source_description := _dict.get('source_description')) is not None:
            args['source_description'] = source_description
        if (source_name := _dict.get('source_name')) is not None:
            args['source_name'] = source_name
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


class EventNotificationsPrototype:
    """
    The payload to connect an Event Notification instance with a Security and Compliance
    Center instance.

    :param str instance_crn: (optional) The CRN of the Event Notification instance
          to connect.
    :param str source_description: (optional) The description of the source of the
          Event Notifications.
    :param str source_name: (optional) The name of the source of the Event
          Notifications.
    """

    def __init__(
        self,
        *,
        instance_crn: Optional[str] = None,
        source_description: Optional[str] = None,
        source_name: Optional[str] = None,
    ) -> None:
        """
        Initialize a EventNotificationsPrototype object.

        :param str instance_crn: (optional) The CRN of the Event Notification
               instance to connect.
        :param str source_description: (optional) The description of the source of
               the Event Notifications.
        :param str source_name: (optional) The name of the source of the Event
               Notifications.
        """
        self.instance_crn = instance_crn
        self.source_description = source_description
        self.source_name = source_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EventNotificationsPrototype':
        """Initialize a EventNotificationsPrototype object from a json dictionary."""
        args = {}
        if (instance_crn := _dict.get('instance_crn')) is not None:
            args['instance_crn'] = instance_crn
        if (source_description := _dict.get('source_description')) is not None:
            args['source_description'] = source_description
        if (source_name := _dict.get('source_name')) is not None:
            args['source_name'] = source_name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EventNotificationsPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
        if hasattr(self, 'source_description') and self.source_description is not None:
            _dict['source_description'] = self.source_description
        if hasattr(self, 'source_name') and self.source_name is not None:
            _dict['source_name'] = self.source_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EventNotificationsPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EventNotificationsPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EventNotificationsPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Import:
    """
    The collection of import parameters.

    :param List[RuleParameter] parameters: (optional) The list of import parameters.
    """

    def __init__(
        self,
        *,
        parameters: Optional[List['RuleParameter']] = None,
    ) -> None:
        """
        Initialize a Import object.

        :param List[RuleParameter] parameters: (optional) The list of import
               parameters.
        """
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Import':
        """Initialize a Import object from a json dictionary."""
        args = {}
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = [RuleParameter.from_dict(v) for v in parameters]
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

    :param str text: (optional) The text of the label.
    :param str tip: (optional) The text to be shown when user hover overs the label.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        tip: Optional[str] = None,
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
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (tip := _dict.get('tip')) is not None:
            args['tip'] = tip
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
    The last scan performed on a profile attachment.

    :param str id: (optional) The ID of the last scan.
    :param str status: (optional) Details the state of the last scan.
    :param datetime time: (optional) The last time the scan ran.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        status: Optional[str] = None,
        time: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a LastScan object.

        :param str id: (optional) The ID of the last scan.
        :param str status: (optional) Details the state of the last scan.
        :param datetime time: (optional) The last time the scan ran.
        """
        self.id = id
        self.status = status
        self.time = time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LastScan':
        """Initialize a LastScan object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (time := _dict.get('time')) is not None:
            args['time'] = string_to_datetime(time)
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


class Link:
    """
    Link.

    :param str description: (optional)
    :param str href: (optional) URL.
    """

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a Link object.

        :param str description: (optional)
        :param str href: (optional) URL.
        """
        self.description = description
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Link':
        """Initialize a Link object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Link object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Link object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Link') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Link') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MultiCloudScopePayload:
    """
    MultiCloudScopePayload.

    :param str id: (optional) The ID of the scope.
    :param str environment: (optional) The environment that relates to this scope.
    :param List[ScopeProperty] properties: The properties supported for scoping by
          this environment.
    """

    def __init__(
        self,
        properties: List['ScopeProperty'],
        *,
        id: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> None:
        """
        Initialize a MultiCloudScopePayload object.

        :param List[ScopeProperty] properties: The properties supported for scoping
               by this environment.
        :param str id: (optional) The ID of the scope.
        :param str environment: (optional) The environment that relates to this
               scope.
        """
        self.id = id
        self.environment = environment
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MultiCloudScopePayload':
        """Initialize a MultiCloudScopePayload object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        else:
            raise ValueError('Required property \'properties\' not present in MultiCloudScopePayload JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MultiCloudScopePayload object from a json dictionary."""
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
        """Return a `str` version of this MultiCloudScopePayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MultiCloudScopePayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MultiCloudScopePayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectStorage:
    """
    The Cloud Object Storage settings.

    :param str instance_crn: (optional) The connected Cloud Object Storage instance
          CRN.
    :param str bucket: (optional) The connected Cloud Object Storage bucket name.
    :param str bucket_location: (optional) The connected Cloud Object Storage bucket
          location.
    :param str bucket_endpoint: (optional) The connected Cloud Object Storage bucket
          endpoint.
    :param datetime updated_on: (optional) The date when the bucket connection was
          updated.
    """

    def __init__(
        self,
        *,
        instance_crn: Optional[str] = None,
        bucket: Optional[str] = None,
        bucket_location: Optional[str] = None,
        bucket_endpoint: Optional[str] = None,
        updated_on: Optional[datetime] = None,
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
        if (instance_crn := _dict.get('instance_crn')) is not None:
            args['instance_crn'] = instance_crn
        if (bucket := _dict.get('bucket')) is not None:
            args['bucket'] = bucket
        if (bucket_location := _dict.get('bucket_location')) is not None:
            args['bucket_location'] = bucket_location
        if (bucket_endpoint := _dict.get('bucket_endpoint')) is not None:
            args['bucket_endpoint'] = bucket_endpoint
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
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


class ObjectStoragePrototype:
    """
    The payload to connect a Cloud Object Storage instance to an Security and Compliance
    Center instance.

    :param str bucket: (optional) The connected Cloud Object Storage bucket name.
    :param str instance_crn: (optional) The connected Cloud Object Storage instance
          CRN.
    """

    def __init__(
        self,
        *,
        bucket: Optional[str] = None,
        instance_crn: Optional[str] = None,
    ) -> None:
        """
        Initialize a ObjectStoragePrototype object.

        :param str bucket: (optional) The connected Cloud Object Storage bucket
               name.
        :param str instance_crn: (optional) The connected Cloud Object Storage
               instance CRN.
        """
        self.bucket = bucket
        self.instance_crn = instance_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectStoragePrototype':
        """Initialize a ObjectStoragePrototype object from a json dictionary."""
        args = {}
        if (bucket := _dict.get('bucket')) is not None:
            args['bucket'] = bucket
        if (instance_crn := _dict.get('instance_crn')) is not None:
            args['instance_crn'] = instance_crn
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectStoragePrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'bucket') and self.bucket is not None:
            _dict['bucket'] = self.bucket
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectStoragePrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ObjectStoragePrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectStoragePrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PageHRefFirst:
    """
    A page reference.

    :param str href: The URL for the first page.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a PageHRefFirst object.

        :param str href: The URL for the first page.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageHRefFirst':
        """Initialize a PageHRefFirst object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
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

    :param str href: The URL for the next page.
    :param str start: (optional) The token of the next page, when it's present.
    """

    def __init__(
        self,
        href: str,
        *,
        start: Optional[str] = None,
    ) -> None:
        """
        Initialize a PageHRefNext object.

        :param str href: The URL for the next page.
        :param str start: (optional) The token of the next page, when it's present.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PageHRefNext':
        """Initialize a PageHRefNext object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in PageHRefNext JSON')
        if (start := _dict.get('start')) is not None:
            args['start'] = start
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


class Parameter:
    """
    The details of a parameter used during an assessment.

    :param str assessment_type: (optional) The type of evaluation.
    :param str assessment_id: (optional) The ID of the assessment.
    :param str parameter_name: (optional) The parameter name.
    :param str parameter_display_name: (optional) The parameter display name.
    :param str parameter_type: (optional) The parameter type.
    :param object parameter_value: (optional)
    """

    def __init__(
        self,
        *,
        assessment_type: Optional[str] = None,
        assessment_id: Optional[str] = None,
        parameter_name: Optional[str] = None,
        parameter_display_name: Optional[str] = None,
        parameter_type: Optional[str] = None,
        parameter_value: Optional[object] = None,
    ) -> None:
        """
        Initialize a Parameter object.

        :param str assessment_type: (optional) The type of evaluation.
        :param str assessment_id: (optional) The ID of the assessment.
        :param str parameter_name: (optional) The parameter name.
        :param str parameter_display_name: (optional) The parameter display name.
        :param str parameter_type: (optional) The parameter type.
        :param object parameter_value: (optional)
        """
        self.assessment_type = assessment_type
        self.assessment_id = assessment_id
        self.parameter_name = parameter_name
        self.parameter_display_name = parameter_display_name
        self.parameter_type = parameter_type
        self.parameter_value = parameter_value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Parameter':
        """Initialize a Parameter object from a json dictionary."""
        args = {}
        if (assessment_type := _dict.get('assessment_type')) is not None:
            args['assessment_type'] = assessment_type
        if (assessment_id := _dict.get('assessment_id')) is not None:
            args['assessment_id'] = assessment_id
        if (parameter_name := _dict.get('parameter_name')) is not None:
            args['parameter_name'] = parameter_name
        if (parameter_display_name := _dict.get('parameter_display_name')) is not None:
            args['parameter_display_name'] = parameter_display_name
        if (parameter_type := _dict.get('parameter_type')) is not None:
            args['parameter_type'] = parameter_type
        if (parameter_value := _dict.get('parameter_value')) is not None:
            args['parameter_value'] = parameter_value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Parameter object from a json dictionary."""
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


class Profile:
    """
    A group of controls that are related to a compliance objective.

    :param str id: (optional) The ID of the profile.
    :param str profile_name: (optional) The name of the profile.
    :param str instance_id: (optional) The ID of the Security and Compliance Center
          instance who owns the profile.
    :param bool hierarchy_enabled: (optional) Determines if the profile can be set
          to a hierarchy.
    :param str profile_description: (optional) A description of what the profile
          should represent.
    :param str profile_type: The type of profile, either predefined or custom.
    :param str profile_version: (optional) The version of the profile.
    :param str version_group_label: (optional) The unique identifier of the
          revision.
    :param bool latest: (optional) Determines if the profile is up to date with the
          latest revisions.
    :param str created_by: (optional) User who created the profile.
    :param datetime created_on: (optional) The date when the profile was created, in
          date-time format.
    :param str updated_by: (optional) User who made the latest changes to the
          profile.
    :param datetime updated_on: (optional) The date when the profile was last
          updated, in date-time format.
    :param int controls_count: (optional) The number of controls contained in the
          profile.
    :param int attachments_count: (optional) The number of attachments associated
          with the profile.
    :param List[ProfileControlsInResponse] controls: The list of controls.
    :param List[DefaultParameters] default_parameters: The default parameters of the
          profile.
    """

    def __init__(
        self,
        profile_type: str,
        controls: List['ProfileControlsInResponse'],
        default_parameters: List['DefaultParameters'],
        *,
        id: Optional[str] = None,
        profile_name: Optional[str] = None,
        instance_id: Optional[str] = None,
        hierarchy_enabled: Optional[bool] = None,
        profile_description: Optional[str] = None,
        profile_version: Optional[str] = None,
        version_group_label: Optional[str] = None,
        latest: Optional[bool] = None,
        created_by: Optional[str] = None,
        created_on: Optional[datetime] = None,
        updated_by: Optional[str] = None,
        updated_on: Optional[datetime] = None,
        controls_count: Optional[int] = None,
        attachments_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a Profile object.

        :param str profile_type: The type of profile, either predefined or custom.
        :param List[ProfileControlsInResponse] controls: The list of controls.
        :param List[DefaultParameters] default_parameters: The default parameters
               of the profile.
        :param str id: (optional) The ID of the profile.
        :param str profile_name: (optional) The name of the profile.
        :param str instance_id: (optional) The ID of the Security and Compliance
               Center instance who owns the profile.
        :param bool hierarchy_enabled: (optional) Determines if the profile can be
               set to a hierarchy.
        :param str profile_description: (optional) A description of what the
               profile should represent.
        :param str profile_version: (optional) The version of the profile.
        :param str version_group_label: (optional) The unique identifier of the
               revision.
        :param bool latest: (optional) Determines if the profile is up to date with
               the latest revisions.
        :param str created_by: (optional) User who created the profile.
        :param datetime created_on: (optional) The date when the profile was
               created, in date-time format.
        :param str updated_by: (optional) User who made the latest changes to the
               profile.
        :param datetime updated_on: (optional) The date when the profile was last
               updated, in date-time format.
        :param int controls_count: (optional) The number of controls contained in
               the profile.
        :param int attachments_count: (optional) The number of attachments
               associated with the profile.
        """
        self.id = id
        self.profile_name = profile_name
        self.instance_id = instance_id
        self.hierarchy_enabled = hierarchy_enabled
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
    def from_dict(cls, _dict: Dict) -> 'Profile':
        """Initialize a Profile object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (profile_name := _dict.get('profile_name')) is not None:
            args['profile_name'] = profile_name
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        if (hierarchy_enabled := _dict.get('hierarchy_enabled')) is not None:
            args['hierarchy_enabled'] = hierarchy_enabled
        if (profile_description := _dict.get('profile_description')) is not None:
            args['profile_description'] = profile_description
        if (profile_type := _dict.get('profile_type')) is not None:
            args['profile_type'] = profile_type
        else:
            raise ValueError('Required property \'profile_type\' not present in Profile JSON')
        if (profile_version := _dict.get('profile_version')) is not None:
            args['profile_version'] = profile_version
        if (version_group_label := _dict.get('version_group_label')) is not None:
            args['version_group_label'] = version_group_label
        if (latest := _dict.get('latest')) is not None:
            args['latest'] = latest
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        if (controls_count := _dict.get('controls_count')) is not None:
            args['controls_count'] = controls_count
        if (attachments_count := _dict.get('attachments_count')) is not None:
            args['attachments_count'] = attachments_count
        if (controls := _dict.get('controls')) is not None:
            args['controls'] = [ProfileControlsInResponse.from_dict(v) for v in controls]
        else:
            raise ValueError('Required property \'controls\' not present in Profile JSON')
        if (default_parameters := _dict.get('default_parameters')) is not None:
            args['default_parameters'] = [DefaultParameters.from_dict(v) for v in default_parameters]
        else:
            raise ValueError('Required property \'default_parameters\' not present in Profile JSON')
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
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'hierarchy_enabled') and self.hierarchy_enabled is not None:
            _dict['hierarchy_enabled'] = self.hierarchy_enabled
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
        The type of profile, either predefined or custom.
        """

        CUSTOM = 'custom'
        PREDEFINED = 'predefined'



class ProfileAttachment:
    """
    The configuration set when starting a scan against a profile.

    :param List[Parameter] attachment_parameters: The parameters associated with the
          profile attachment.
    :param str description: The details to describe the profile attachment.
    :param str name: The name of the Profile Attachment.
    :param AttachmentNotifications notifications: The notification configuration of
          the attachment.
    :param str schedule: Details how often a scan from a profile attachment is ran.
    :param List[MultiCloudScopePayload] scope: A list of scopes associated with a
          profile attachment.
    :param str status: Details the state of a profile attachment.
    :param str account_id: (optional) The ID of the account.
    :param str created_by: (optional) User who created the profile attachment.
    :param datetime created_on: (optional) The date-time that the profile attachment
          was created.
    :param str id: (optional) The ID of the profile attachment.
    :param str instance_id: (optional) The ID of the associated Security and
          Compliance Center instance.
    :param LastScan last_scan: (optional) The last scan performed on a profile
          attachment.
    :param datetime next_scan_time: (optional) The date-time for next scan.
    :param str profile_id: (optional) The ID of the profile.
    :param str updated_by: (optional) User who made the latest changes to the
          profile attachment.
    :param datetime updated_on: (optional) The date when the profile was last
          updated, in date-time format.
    """

    def __init__(
        self,
        attachment_parameters: List['Parameter'],
        description: str,
        name: str,
        notifications: 'AttachmentNotifications',
        schedule: str,
        scope: List['MultiCloudScopePayload'],
        status: str,
        *,
        account_id: Optional[str] = None,
        created_by: Optional[str] = None,
        created_on: Optional[datetime] = None,
        id: Optional[str] = None,
        instance_id: Optional[str] = None,
        last_scan: Optional['LastScan'] = None,
        next_scan_time: Optional[datetime] = None,
        profile_id: Optional[str] = None,
        updated_by: Optional[str] = None,
        updated_on: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a ProfileAttachment object.

        :param List[Parameter] attachment_parameters: The parameters associated
               with the profile attachment.
        :param str description: The details to describe the profile attachment.
        :param str name: The name of the Profile Attachment.
        :param AttachmentNotifications notifications: The notification
               configuration of the attachment.
        :param str schedule: Details how often a scan from a profile attachment is
               ran.
        :param List[MultiCloudScopePayload] scope: A list of scopes associated with
               a profile attachment.
        :param str status: Details the state of a profile attachment.
        :param str account_id: (optional) The ID of the account.
        :param str created_by: (optional) User who created the profile attachment.
        :param datetime created_on: (optional) The date-time that the profile
               attachment was created.
        :param str id: (optional) The ID of the profile attachment.
        :param str instance_id: (optional) The ID of the associated Security and
               Compliance Center instance.
        :param LastScan last_scan: (optional) The last scan performed on a profile
               attachment.
        :param datetime next_scan_time: (optional) The date-time for next scan.
        :param str profile_id: (optional) The ID of the profile.
        :param str updated_by: (optional) User who made the latest changes to the
               profile attachment.
        :param datetime updated_on: (optional) The date when the profile was last
               updated, in date-time format.
        """
        self.attachment_parameters = attachment_parameters
        self.description = description
        self.name = name
        self.notifications = notifications
        self.schedule = schedule
        self.scope = scope
        self.status = status
        self.account_id = account_id
        self.created_by = created_by
        self.created_on = created_on
        self.id = id
        self.instance_id = instance_id
        self.last_scan = last_scan
        self.next_scan_time = next_scan_time
        self.profile_id = profile_id
        self.updated_by = updated_by
        self.updated_on = updated_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileAttachment':
        """Initialize a ProfileAttachment object from a json dictionary."""
        args = {}
        if (attachment_parameters := _dict.get('attachment_parameters')) is not None:
            args['attachment_parameters'] = [Parameter.from_dict(v) for v in attachment_parameters]
        else:
            raise ValueError('Required property \'attachment_parameters\' not present in ProfileAttachment JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ProfileAttachment JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ProfileAttachment JSON')
        if (notifications := _dict.get('notifications')) is not None:
            args['notifications'] = AttachmentNotifications.from_dict(notifications)
        else:
            raise ValueError('Required property \'notifications\' not present in ProfileAttachment JSON')
        if (schedule := _dict.get('schedule')) is not None:
            args['schedule'] = schedule
        else:
            raise ValueError('Required property \'schedule\' not present in ProfileAttachment JSON')
        if (scope := _dict.get('scope')) is not None:
            args['scope'] = [MultiCloudScopePayload.from_dict(v) for v in scope]
        else:
            raise ValueError('Required property \'scope\' not present in ProfileAttachment JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ProfileAttachment JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        if (last_scan := _dict.get('last_scan')) is not None:
            args['last_scan'] = LastScan.from_dict(last_scan)
        if (next_scan_time := _dict.get('next_scan_time')) is not None:
            args['next_scan_time'] = string_to_datetime(next_scan_time)
        if (profile_id := _dict.get('profile_id')) is not None:
            args['profile_id'] = profile_id
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileAttachment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachment_parameters') and self.attachment_parameters is not None:
            attachment_parameters_list = []
            for v in self.attachment_parameters:
                if isinstance(v, dict):
                    attachment_parameters_list.append(v)
                else:
                    attachment_parameters_list.append(v.to_dict())
            _dict['attachment_parameters'] = attachment_parameters_list
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'notifications') and self.notifications is not None:
            if isinstance(self.notifications, dict):
                _dict['notifications'] = self.notifications
            else:
                _dict['notifications'] = self.notifications.to_dict()
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
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'last_scan') and self.last_scan is not None:
            if isinstance(self.last_scan, dict):
                _dict['last_scan'] = self.last_scan
            else:
                _dict['last_scan'] = self.last_scan.to_dict()
        if hasattr(self, 'next_scan_time') and self.next_scan_time is not None:
            _dict['next_scan_time'] = datetime_to_string(self.next_scan_time)
        if hasattr(self, 'profile_id') and self.profile_id is not None:
            _dict['profile_id'] = self.profile_id
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileAttachment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileAttachment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileAttachment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ScheduleEnum(str, Enum):
        """
        Details how often a scan from a profile attachment is ran.
        """

        DAILY = 'daily'
        EVERY_7_DAYS = 'every_7_days'
        EVERY_30_DAYS = 'every_30_days'


    class StatusEnum(str, Enum):
        """
        Details the state of a profile attachment.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'



class ProfileAttachmentBase:
    """
    The prototype for creating a Profile attachment.

    :param List[Parameter] attachment_parameters: The parameters associated with the
          profile attachment.
    :param str description: The details to describe the profile attachment.
    :param str name: The name of the Profile Attachment.
    :param AttachmentNotifications notifications: The notification configuration of
          the attachment.
    :param str schedule: Details how often a scan from a profile attachment is ran.
    :param List[MultiCloudScopePayload] scope: A list of scopes associated with a
          profile attachment.
    :param str status: Details the state of a profile attachment.
    """

    def __init__(
        self,
        attachment_parameters: List['Parameter'],
        description: str,
        name: str,
        notifications: 'AttachmentNotifications',
        schedule: str,
        scope: List['MultiCloudScopePayload'],
        status: str,
    ) -> None:
        """
        Initialize a ProfileAttachmentBase object.

        :param List[Parameter] attachment_parameters: The parameters associated
               with the profile attachment.
        :param str description: The details to describe the profile attachment.
        :param str name: The name of the Profile Attachment.
        :param AttachmentNotifications notifications: The notification
               configuration of the attachment.
        :param str schedule: Details how often a scan from a profile attachment is
               ran.
        :param List[MultiCloudScopePayload] scope: A list of scopes associated with
               a profile attachment.
        :param str status: Details the state of a profile attachment.
        """
        self.attachment_parameters = attachment_parameters
        self.description = description
        self.name = name
        self.notifications = notifications
        self.schedule = schedule
        self.scope = scope
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileAttachmentBase':
        """Initialize a ProfileAttachmentBase object from a json dictionary."""
        args = {}
        if (attachment_parameters := _dict.get('attachment_parameters')) is not None:
            args['attachment_parameters'] = [Parameter.from_dict(v) for v in attachment_parameters]
        else:
            raise ValueError('Required property \'attachment_parameters\' not present in ProfileAttachmentBase JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ProfileAttachmentBase JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ProfileAttachmentBase JSON')
        if (notifications := _dict.get('notifications')) is not None:
            args['notifications'] = AttachmentNotifications.from_dict(notifications)
        else:
            raise ValueError('Required property \'notifications\' not present in ProfileAttachmentBase JSON')
        if (schedule := _dict.get('schedule')) is not None:
            args['schedule'] = schedule
        else:
            raise ValueError('Required property \'schedule\' not present in ProfileAttachmentBase JSON')
        if (scope := _dict.get('scope')) is not None:
            args['scope'] = [MultiCloudScopePayload.from_dict(v) for v in scope]
        else:
            raise ValueError('Required property \'scope\' not present in ProfileAttachmentBase JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ProfileAttachmentBase JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileAttachmentBase object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'attachment_parameters') and self.attachment_parameters is not None:
            attachment_parameters_list = []
            for v in self.attachment_parameters:
                if isinstance(v, dict):
                    attachment_parameters_list.append(v)
                else:
                    attachment_parameters_list.append(v.to_dict())
            _dict['attachment_parameters'] = attachment_parameters_list
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'notifications') and self.notifications is not None:
            if isinstance(self.notifications, dict):
                _dict['notifications'] = self.notifications
            else:
                _dict['notifications'] = self.notifications.to_dict()
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
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProfileAttachmentBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileAttachmentBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileAttachmentBase') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ScheduleEnum(str, Enum):
        """
        Details how often a scan from a profile attachment is ran.
        """

        DAILY = 'daily'
        EVERY_7_DAYS = 'every_7_days'
        EVERY_30_DAYS = 'every_30_days'


    class StatusEnum(str, Enum):
        """
        Details the state of a profile attachment.
        """

        ENABLED = 'enabled'
        DISABLED = 'disabled'



class ProfileAttachmentCollection:
    """
    A list of ProfileAttachment tied to a profile or instance.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[ProfileAttachment] attachments: List of attachments.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        attachments: List['ProfileAttachment'],
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
    ) -> None:
        """
        Initialize a ProfileAttachmentCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param List[ProfileAttachment] attachments: List of attachments.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileAttachmentCollection':
        """Initialize a ProfileAttachmentCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ProfileAttachmentCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ProfileAttachmentCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = [ProfileAttachment.from_dict(v) for v in attachments]
        else:
            raise ValueError('Required property \'attachments\' not present in ProfileAttachmentCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileAttachmentCollection object from a json dictionary."""
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
        """Return a `str` version of this ProfileAttachmentCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileAttachmentCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileAttachmentCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileAttachmentResponse:
    """
    ProfileAttachmentResponse.

    :param str profile_id: (optional) The ID of the profile.
    :param List[ProfileAttachment] attachments: List of profile attachments
          associated with profile.
    """

    def __init__(
        self,
        attachments: List['ProfileAttachment'],
        *,
        profile_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProfileAttachmentResponse object.

        :param List[ProfileAttachment] attachments: List of profile attachments
               associated with profile.
        :param str profile_id: (optional) The ID of the profile.
        """
        self.profile_id = profile_id
        self.attachments = attachments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileAttachmentResponse':
        """Initialize a ProfileAttachmentResponse object from a json dictionary."""
        args = {}
        if (profile_id := _dict.get('profile_id')) is not None:
            args['profile_id'] = profile_id
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = [ProfileAttachment.from_dict(v) for v in attachments]
        else:
            raise ValueError('Required property \'attachments\' not present in ProfileAttachmentResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileAttachmentResponse object from a json dictionary."""
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
        """Return a `str` version of this ProfileAttachmentResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProfileAttachmentResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProfileAttachmentResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProfileCollection:
    """
    Show a list of Profiles.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[Profile] profiles: A list of profiles.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        profiles: List['Profile'],
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
    ) -> None:
        """
        Initialize a ProfileCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param List[Profile] profiles: A list of profiles.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.profiles = profiles

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileCollection':
        """Initialize a ProfileCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ProfileCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ProfileCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (profiles := _dict.get('profiles')) is not None:
            args['profiles'] = [Profile.from_dict(v) for v in profiles]
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


class ProfileControlsInResponse:
    """
    The control details for a profile.

    :param bool control_requirement: (optional) Determines if the control needs to
          pass during evaluation.
    :param str control_library_id: (optional) The ID of the control library that
          contains a profile.
    :param str control_id: (optional) The control ID.
    :param str control_library_version: (optional) The control library version.
    :param str control_name: (optional) The control name.
    :param str control_description: (optional) The control description.
    :param str control_severity: (optional) The control severity.
    :param str control_category: (optional) The control category.
    :param str control_parent: (optional) The control parent.
    :param ControlDoc control_docs: (optional) References to a control
          documentation.
    :param List[ControlSpecification] control_specifications: List of control
          specifications in a profile.
    """

    def __init__(
        self,
        control_specifications: List['ControlSpecification'],
        *,
        control_requirement: Optional[bool] = None,
        control_library_id: Optional[str] = None,
        control_id: Optional[str] = None,
        control_library_version: Optional[str] = None,
        control_name: Optional[str] = None,
        control_description: Optional[str] = None,
        control_severity: Optional[str] = None,
        control_category: Optional[str] = None,
        control_parent: Optional[str] = None,
        control_docs: Optional['ControlDoc'] = None,
    ) -> None:
        """
        Initialize a ProfileControlsInResponse object.

        :param List[ControlSpecification] control_specifications: List of control
               specifications in a profile.
        :param bool control_requirement: (optional) Determines if the control needs
               to pass during evaluation.
        :param str control_library_id: (optional) The ID of the control library
               that contains a profile.
        :param str control_id: (optional) The control ID.
        :param str control_library_version: (optional) The control library version.
        :param str control_name: (optional) The control name.
        :param str control_description: (optional) The control description.
        :param str control_severity: (optional) The control severity.
        :param str control_category: (optional) The control category.
        :param str control_parent: (optional) The control parent.
        :param ControlDoc control_docs: (optional) References to a control
               documentation.
        """
        self.control_requirement = control_requirement
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
        if (control_requirement := _dict.get('control_requirement')) is not None:
            args['control_requirement'] = control_requirement
        if (control_library_id := _dict.get('control_library_id')) is not None:
            args['control_library_id'] = control_library_id
        if (control_id := _dict.get('control_id')) is not None:
            args['control_id'] = control_id
        if (control_library_version := _dict.get('control_library_version')) is not None:
            args['control_library_version'] = control_library_version
        if (control_name := _dict.get('control_name')) is not None:
            args['control_name'] = control_name
        if (control_description := _dict.get('control_description')) is not None:
            args['control_description'] = control_description
        if (control_severity := _dict.get('control_severity')) is not None:
            args['control_severity'] = control_severity
        if (control_category := _dict.get('control_category')) is not None:
            args['control_category'] = control_category
        if (control_parent := _dict.get('control_parent')) is not None:
            args['control_parent'] = control_parent
        if (control_docs := _dict.get('control_docs')) is not None:
            args['control_docs'] = ControlDoc.from_dict(control_docs)
        if (control_specifications := _dict.get('control_specifications')) is not None:
            args['control_specifications'] = [ControlSpecification.from_dict(v) for v in control_specifications]
        else:
            raise ValueError('Required property \'control_specifications\' not present in ProfileControlsInResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProfileControlsInResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'control_requirement') and self.control_requirement is not None:
            _dict['control_requirement'] = self.control_requirement
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


class ProfileControlsPrototype:
    """
    The control details of a profile.

    :param str control_library_id: (optional) The ID of the control library that
          contains the profile.
    :param str control_id: (optional) The control ID.
    """

    def __init__(
        self,
        *,
        control_library_id: Optional[str] = None,
        control_id: Optional[str] = None,
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
        if (control_library_id := _dict.get('control_library_id')) is not None:
            args['control_library_id'] = control_library_id
        if (control_id := _dict.get('control_id')) is not None:
            args['control_id'] = control_id
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


class ProfileDefaultParametersResponse:
    """
    The default parameters of a profile.

    :param str id: (optional) The ID of the Profile.
    :param List[DefaultParameters] default_parameters: list of parameters given by
          default.
    """

    def __init__(
        self,
        default_parameters: List['DefaultParameters'],
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProfileDefaultParametersResponse object.

        :param List[DefaultParameters] default_parameters: list of parameters given
               by default.
        :param str id: (optional) The ID of the Profile.
        """
        self.id = id
        self.default_parameters = default_parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProfileDefaultParametersResponse':
        """Initialize a ProfileDefaultParametersResponse object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (default_parameters := _dict.get('default_parameters')) is not None:
            args['default_parameters'] = [DefaultParameters.from_dict(v) for v in default_parameters]
        else:
            raise ValueError('Required property \'default_parameters\' not present in ProfileDefaultParametersResponse JSON')
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


class ProfileInfo:
    """
    The profile information.

    :param str id: (optional) The profile ID.
    :param str name: (optional) The profile name.
    :param str version: (optional) The profile version.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
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
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (version := _dict.get('version')) is not None:
            args['version'] = version
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


class ProviderType:
    """
    The provider type item.

    :param str id: The unique identifier of the provider type.
    :param str type: The type of the provider type.
    :param str name: The name of the provider type.
    :param str description: The provider type description.
    :param bool s2s_enabled: A boolean that indicates whether the provider type is
          s2s-enabled.
    :param int instance_limit: The maximum number of instances that can be created
          for the provider type.
    :param str mode: The mode that is used to get results from provider (`PUSH` or
          `PULL`).
    :param str data_type: The format of the results that a provider supports.
    :param str icon: The icon of a provider in .svg format that is encoded as a
          base64 string.
    :param LabelType label: (optional) The label that is associated with the
          provider type.
    :param dict attributes: The attributes that are required when you're creating an
          instance of a provider type. The attributes field can have multiple  keys in its
          value. Each of those keys has a value  object that includes the type, and
          display name as keys. For example, `{type:"", display_name:""}`.
          **NOTE;** If the provider type is s2s-enabled, which means that if the
          `s2s_enabled` field is set to `true`, then a CRN field of type text is required
          in the attributes value object.
    :param datetime created_at: (optional) Time at which resource was created.
    :param datetime updated_at: (optional) Time at which resource was updated.
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
        label: Optional['LabelType'] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a ProviderType object.

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
    def from_dict(cls, _dict: Dict) -> 'ProviderType':
        """Initialize a ProviderType object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ProviderType JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in ProviderType JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ProviderType JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ProviderType JSON')
        if (s2s_enabled := _dict.get('s2s_enabled')) is not None:
            args['s2s_enabled'] = s2s_enabled
        else:
            raise ValueError('Required property \'s2s_enabled\' not present in ProviderType JSON')
        if (instance_limit := _dict.get('instance_limit')) is not None:
            args['instance_limit'] = instance_limit
        else:
            raise ValueError('Required property \'instance_limit\' not present in ProviderType JSON')
        if (mode := _dict.get('mode')) is not None:
            args['mode'] = mode
        else:
            raise ValueError('Required property \'mode\' not present in ProviderType JSON')
        if (data_type := _dict.get('data_type')) is not None:
            args['data_type'] = data_type
        else:
            raise ValueError('Required property \'data_type\' not present in ProviderType JSON')
        if (icon := _dict.get('icon')) is not None:
            args['icon'] = icon
        else:
            raise ValueError('Required property \'icon\' not present in ProviderType JSON')
        if (label := _dict.get('label')) is not None:
            args['label'] = LabelType.from_dict(label)
        if (attributes := _dict.get('attributes')) is not None:
            args['attributes'] = {k: AdditionalProperty.from_dict(v) for k, v in attributes.items()}
        else:
            raise ValueError('Required property \'attributes\' not present in ProviderType JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderType object from a json dictionary."""
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
        """Return a `str` version of this ProviderType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypeCollection:
    """
    The provider types collection.

    :param List[ProviderType] provider_types: (optional) The array of provder type.
    """

    def __init__(
        self,
        *,
        provider_types: Optional[List['ProviderType']] = None,
    ) -> None:
        """
        Initialize a ProviderTypeCollection object.

        :param List[ProviderType] provider_types: (optional) The array of provder
               type.
        """
        self.provider_types = provider_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypeCollection':
        """Initialize a ProviderTypeCollection object from a json dictionary."""
        args = {}
        if (provider_types := _dict.get('provider_types')) is not None:
            args['provider_types'] = [ProviderType.from_dict(v) for v in provider_types]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypeCollection object from a json dictionary."""
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
        """Return a `str` version of this ProviderTypeCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypeCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypeCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypeInstance:
    """
    A provider type instance.

    :param str id: (optional) The unique identifier of the provider type instance.
    :param str type: (optional) The type of the provider type.
    :param str name: (optional) The name of the provider type instance.
    :param dict attributes: (optional) The attributes for connecting to the provider
          type instance.
    :param datetime created_at: (optional) Time at which resource was created.
    :param datetime updated_at: (optional) Time at which resource was updated.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        name: Optional[str] = None,
        attributes: Optional[dict] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a ProviderTypeInstance object.

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
    def from_dict(cls, _dict: Dict) -> 'ProviderTypeInstance':
        """Initialize a ProviderTypeInstance object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (attributes := _dict.get('attributes')) is not None:
            args['attributes'] = attributes
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypeInstance object from a json dictionary."""
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
        """Return a `str` version of this ProviderTypeInstance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypeInstance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypeInstance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderTypeInstanceCollection:
    """
    Provider types instances response.

    :param List[ProviderTypeInstance] provider_type_instances: (optional) The array
          of instances for all provider types.
    """

    def __init__(
        self,
        *,
        provider_type_instances: Optional[List['ProviderTypeInstance']] = None,
    ) -> None:
        """
        Initialize a ProviderTypeInstanceCollection object.

        :param List[ProviderTypeInstance] provider_type_instances: (optional) The
               array of instances for all provider types.
        """
        self.provider_type_instances = provider_type_instances

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderTypeInstanceCollection':
        """Initialize a ProviderTypeInstanceCollection object from a json dictionary."""
        args = {}
        if (provider_type_instances := _dict.get('provider_type_instances')) is not None:
            args['provider_type_instances'] = [ProviderTypeInstance.from_dict(v) for v in provider_type_instances]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderTypeInstanceCollection object from a json dictionary."""
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
        """Return a `str` version of this ProviderTypeInstanceCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderTypeInstanceCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderTypeInstanceCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Report:
    """
    The report.

    :param str id: The ID of the report.
    :param str type: The type of the scan.
    :param str group_id: The group ID that is associated with the report. The group
          ID combines profile, scope, and attachment IDs.
    :param str created_on: The date when the report was created.
    :param str scan_time: The date when the scan was run.
    :param str cos_object: The Cloud Object Storage object that is associated with
          the report.
    :param str instance_id: The ID of the Security and Compliance Center instance.
    :param Account account: The account that is associated with a report.
    :param ProfileInfo profile: The profile information.
    :param ScopeID scope: The scope ID that is associated with a report. Attributes
          for this object will be blank if the report has multiple scopes tied to the
          report.
    :param Attachment attachment: The attachment that is associated with a report.
    :param ComplianceStatsWithNonCompliant controls_summary: The compliance stats.
    :param EvalStats evaluations_summary: The evaluation stats.
    :param Tags tags: The collection of different types of tags.
    :param List[ReportScope] scopes: The scopes used in the report.
    :param AdditionalDetails additional_details: Extended information for a report.
    """

    def __init__(
        self,
        id: str,
        type: str,
        group_id: str,
        created_on: str,
        scan_time: str,
        cos_object: str,
        instance_id: str,
        account: 'Account',
        profile: 'ProfileInfo',
        scope: 'ScopeID',
        attachment: 'Attachment',
        controls_summary: 'ComplianceStatsWithNonCompliant',
        evaluations_summary: 'EvalStats',
        tags: 'Tags',
        scopes: List['ReportScope'],
        additional_details: 'AdditionalDetails',
    ) -> None:
        """
        Initialize a Report object.

        :param str id: The ID of the report.
        :param str type: The type of the scan.
        :param str group_id: The group ID that is associated with the report. The
               group ID combines profile, scope, and attachment IDs.
        :param str created_on: The date when the report was created.
        :param str scan_time: The date when the scan was run.
        :param str cos_object: The Cloud Object Storage object that is associated
               with the report.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param Account account: The account that is associated with a report.
        :param ProfileInfo profile: The profile information.
        :param ScopeID scope: The scope ID that is associated with a report.
               Attributes for this object will be blank if the report has multiple scopes
               tied to the report.
        :param Attachment attachment: The attachment that is associated with a
               report.
        :param ComplianceStatsWithNonCompliant controls_summary: The compliance
               stats.
        :param EvalStats evaluations_summary: The evaluation stats.
        :param Tags tags: The collection of different types of tags.
        :param List[ReportScope] scopes: The scopes used in the report.
        :param AdditionalDetails additional_details: Extended information for a
               report.
        """
        self.id = id
        self.type = type
        self.group_id = group_id
        self.created_on = created_on
        self.scan_time = scan_time
        self.cos_object = cos_object
        self.instance_id = instance_id
        self.account = account
        self.profile = profile
        self.scope = scope
        self.attachment = attachment
        self.controls_summary = controls_summary
        self.evaluations_summary = evaluations_summary
        self.tags = tags
        self.scopes = scopes
        self.additional_details = additional_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Report':
        """Initialize a Report object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Report JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in Report JSON')
        if (group_id := _dict.get('group_id')) is not None:
            args['group_id'] = group_id
        else:
            raise ValueError('Required property \'group_id\' not present in Report JSON')
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = created_on
        else:
            raise ValueError('Required property \'created_on\' not present in Report JSON')
        if (scan_time := _dict.get('scan_time')) is not None:
            args['scan_time'] = scan_time
        else:
            raise ValueError('Required property \'scan_time\' not present in Report JSON')
        if (cos_object := _dict.get('cos_object')) is not None:
            args['cos_object'] = cos_object
        else:
            raise ValueError('Required property \'cos_object\' not present in Report JSON')
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        else:
            raise ValueError('Required property \'instance_id\' not present in Report JSON')
        if (account := _dict.get('account')) is not None:
            args['account'] = Account.from_dict(account)
        else:
            raise ValueError('Required property \'account\' not present in Report JSON')
        if (profile := _dict.get('profile')) is not None:
            args['profile'] = ProfileInfo.from_dict(profile)
        else:
            raise ValueError('Required property \'profile\' not present in Report JSON')
        if (scope := _dict.get('scope')) is not None:
            args['scope'] = ScopeID.from_dict(scope)
        else:
            raise ValueError('Required property \'scope\' not present in Report JSON')
        if (attachment := _dict.get('attachment')) is not None:
            args['attachment'] = Attachment.from_dict(attachment)
        else:
            raise ValueError('Required property \'attachment\' not present in Report JSON')
        if (controls_summary := _dict.get('controls_summary')) is not None:
            args['controls_summary'] = ComplianceStatsWithNonCompliant.from_dict(controls_summary)
        else:
            raise ValueError('Required property \'controls_summary\' not present in Report JSON')
        if (evaluations_summary := _dict.get('evaluations_summary')) is not None:
            args['evaluations_summary'] = EvalStats.from_dict(evaluations_summary)
        else:
            raise ValueError('Required property \'evaluations_summary\' not present in Report JSON')
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = Tags.from_dict(tags)
        else:
            raise ValueError('Required property \'tags\' not present in Report JSON')
        if (scopes := _dict.get('scopes')) is not None:
            args['scopes'] = [ReportScope.from_dict(v) for v in scopes]
        else:
            raise ValueError('Required property \'scopes\' not present in Report JSON')
        if (additional_details := _dict.get('additional_details')) is not None:
            args['additional_details'] = AdditionalDetails.from_dict(additional_details)
        else:
            raise ValueError('Required property \'additional_details\' not present in Report JSON')
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
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'group_id') and self.group_id is not None:
            _dict['group_id'] = self.group_id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'scan_time') and self.scan_time is not None:
            _dict['scan_time'] = self.scan_time
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
        if hasattr(self, 'scope') and self.scope is not None:
            if isinstance(self.scope, dict):
                _dict['scope'] = self.scope
            else:
                _dict['scope'] = self.scope.to_dict()
        if hasattr(self, 'attachment') and self.attachment is not None:
            if isinstance(self.attachment, dict):
                _dict['attachment'] = self.attachment
            else:
                _dict['attachment'] = self.attachment.to_dict()
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
        if hasattr(self, 'tags') and self.tags is not None:
            if isinstance(self.tags, dict):
                _dict['tags'] = self.tags
            else:
                _dict['tags'] = self.tags.to_dict()
        if hasattr(self, 'scopes') and self.scopes is not None:
            scopes_list = []
            for v in self.scopes:
                if isinstance(v, dict):
                    scopes_list.append(v)
                else:
                    scopes_list.append(v.to_dict())
            _dict['scopes'] = scopes_list
        if hasattr(self, 'additional_details') and self.additional_details is not None:
            if isinstance(self.additional_details, dict):
                _dict['additional_details'] = self.additional_details
            else:
                _dict['additional_details'] = self.additional_details.to_dict()
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


class ReportCollection:
    """
    The page of reports.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param str home_account_id: (optional) The ID of the home account.
    :param List[Report] reports: (optional) The list of reports that are on the
          page.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
        home_account_id: Optional[str] = None,
        reports: Optional[List['Report']] = None,
    ) -> None:
        """
        Initialize a ReportCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        :param str home_account_id: (optional) The ID of the home account.
        :param List[Report] reports: (optional) The list of reports that are on the
               page.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.home_account_id = home_account_id
        self.reports = reports

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportCollection':
        """Initialize a ReportCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ReportCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ReportCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (reports := _dict.get('reports')) is not None:
            args['reports'] = [Report.from_dict(v) for v in reports]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportCollection object from a json dictionary."""
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
        """Return a `str` version of this ReportCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportControls:
    """
    The list of controls.

    :param str report_id: (optional) The ID of the report.
    :param str home_account_id: (optional) The ID of the home account.
    :param List[ControlWithStats] controls: (optional) The list of controls that are
          in the report.
    """

    def __init__(
        self,
        *,
        report_id: Optional[str] = None,
        home_account_id: Optional[str] = None,
        controls: Optional[List['ControlWithStats']] = None,
    ) -> None:
        """
        Initialize a ReportControls object.

        :param str report_id: (optional) The ID of the report.
        :param str home_account_id: (optional) The ID of the home account.
        :param List[ControlWithStats] controls: (optional) The list of controls
               that are in the report.
        """
        self.report_id = report_id
        self.home_account_id = home_account_id
        self.controls = controls

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportControls':
        """Initialize a ReportControls object from a json dictionary."""
        args = {}
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (controls := _dict.get('controls')) is not None:
            args['controls'] = [ControlWithStats.from_dict(v) for v in controls]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportControls object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
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


class ReportLatest:
    """
    The response body of the `get_latest_reports` operation.

    :param str home_account_id: (optional) The ID of the home account.
    :param ComplianceStats controls_summary: (optional) The compliance stats.
    :param EvalStats evaluations_summary: (optional) The evaluation stats.
    :param ComplianceScore score: (optional) The compliance score.
    :param List[Report] reports: (optional) The list of reports.
    """

    def __init__(
        self,
        *,
        home_account_id: Optional[str] = None,
        controls_summary: Optional['ComplianceStats'] = None,
        evaluations_summary: Optional['EvalStats'] = None,
        score: Optional['ComplianceScore'] = None,
        reports: Optional[List['Report']] = None,
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
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (controls_summary := _dict.get('controls_summary')) is not None:
            args['controls_summary'] = ComplianceStats.from_dict(controls_summary)
        if (evaluations_summary := _dict.get('evaluations_summary')) is not None:
            args['evaluations_summary'] = EvalStats.from_dict(evaluations_summary)
        if (score := _dict.get('score')) is not None:
            args['score'] = ComplianceScore.from_dict(score)
        if (reports := _dict.get('reports')) is not None:
            args['reports'] = [Report.from_dict(v) for v in reports]
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


class ReportScope:
    """
    The scopes used in the report.

    :param str id: The ID of the scope used.
    :param str name: The name of the scope used.
    :param str href: The url to a report concerning the specified scope.
    """

    def __init__(
        self,
        id: str,
        name: str,
        href: str,
    ) -> None:
        """
        Initialize a ReportScope object.

        :param str id: The ID of the scope used.
        :param str name: The name of the scope used.
        :param str href: The url to a report concerning the specified scope.
        """
        self.id = id
        self.name = name
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportScope':
        """Initialize a ReportScope object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ReportScope JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ReportScope JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in ReportScope JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReportScope object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReportScope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReportScope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReportScope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReportSummary:
    """
    The report summary.

    :param str report_id: (optional) The ID of the report.
    :param str isntance_id: (optional) Instance ID.
    :param Account account: (optional) The account that is associated with a report.
    :param ComplianceScore score: (optional) The compliance score.
    :param EvalStats evaluations: (optional) The evaluation stats.
    :param ComplianceStats controls: (optional) The compliance stats.
    :param ResourceSummary resources: (optional) The resource summary.
    """

    def __init__(
        self,
        *,
        report_id: Optional[str] = None,
        isntance_id: Optional[str] = None,
        account: Optional['Account'] = None,
        score: Optional['ComplianceScore'] = None,
        evaluations: Optional['EvalStats'] = None,
        controls: Optional['ComplianceStats'] = None,
        resources: Optional['ResourceSummary'] = None,
    ) -> None:
        """
        Initialize a ReportSummary object.

        :param str report_id: (optional) The ID of the report.
        :param str isntance_id: (optional) Instance ID.
        :param Account account: (optional) The account that is associated with a
               report.
        :param ComplianceScore score: (optional) The compliance score.
        :param EvalStats evaluations: (optional) The evaluation stats.
        :param ComplianceStats controls: (optional) The compliance stats.
        :param ResourceSummary resources: (optional) The resource summary.
        """
        self.report_id = report_id
        self.isntance_id = isntance_id
        self.account = account
        self.score = score
        self.evaluations = evaluations
        self.controls = controls
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportSummary':
        """Initialize a ReportSummary object from a json dictionary."""
        args = {}
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (isntance_id := _dict.get('isntance_id')) is not None:
            args['isntance_id'] = isntance_id
        if (account := _dict.get('account')) is not None:
            args['account'] = Account.from_dict(account)
        if (score := _dict.get('score')) is not None:
            args['score'] = ComplianceScore.from_dict(score)
        if (evaluations := _dict.get('evaluations')) is not None:
            args['evaluations'] = EvalStats.from_dict(evaluations)
        if (controls := _dict.get('controls')) is not None:
            args['controls'] = ComplianceStats.from_dict(controls)
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = ResourceSummary.from_dict(resources)
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
        if hasattr(self, 'evaluations') and self.evaluations is not None:
            if isinstance(self.evaluations, dict):
                _dict['evaluations'] = self.evaluations
            else:
                _dict['evaluations'] = self.evaluations.to_dict()
        if hasattr(self, 'controls') and self.controls is not None:
            if isinstance(self.controls, dict):
                _dict['controls'] = self.controls
            else:
                _dict['controls'] = self.controls.to_dict()
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

    :param str report_id: (optional) The ID of the report.
    :param Tags tags: (optional) The collection of different types of tags.
    """

    def __init__(
        self,
        *,
        report_id: Optional[str] = None,
        tags: Optional['Tags'] = None,
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
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = Tags.from_dict(tags)
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

    :param str report_id: (optional) The ID of the report.
    :param str report_group_id: (optional) The group ID that is associated with the
          report. The group ID combines profile, scope, and attachment IDs.
    :param str scan_time: (optional) The date when the scan was run.
    :param ComplianceStats controls_summary: (optional) The compliance stats.
    """

    def __init__(
        self,
        *,
        report_id: Optional[str] = None,
        report_group_id: Optional[str] = None,
        scan_time: Optional[str] = None,
        controls_summary: Optional['ComplianceStats'] = None,
    ) -> None:
        """
        Initialize a ReportViolationDataPoint object.

        :param str report_id: (optional) The ID of the report.
        :param str report_group_id: (optional) The group ID that is associated with
               the report. The group ID combines profile, scope, and attachment IDs.
        :param str scan_time: (optional) The date when the scan was run.
        :param ComplianceStats controls_summary: (optional) The compliance stats.
        """
        self.report_id = report_id
        self.report_group_id = report_group_id
        self.scan_time = scan_time
        self.controls_summary = controls_summary

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportViolationDataPoint':
        """Initialize a ReportViolationDataPoint object from a json dictionary."""
        args = {}
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (report_group_id := _dict.get('report_group_id')) is not None:
            args['report_group_id'] = report_group_id
        if (scan_time := _dict.get('scan_time')) is not None:
            args['scan_time'] = scan_time
        if (controls_summary := _dict.get('controls_summary')) is not None:
            args['controls_summary'] = ComplianceStats.from_dict(controls_summary)
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
        if hasattr(self, 'controls_summary') and self.controls_summary is not None:
            if isinstance(self.controls_summary, dict):
                _dict['controls_summary'] = self.controls_summary
            else:
                _dict['controls_summary'] = self.controls_summary.to_dict()
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

    :param str home_account_id: (optional) The ID of the home account.
    :param str report_group_id: (optional) The ID of the report group.
    :param List[ReportViolationDataPoint] data_points: (optional) The list of report
          violations data points.
    """

    def __init__(
        self,
        *,
        home_account_id: Optional[str] = None,
        report_group_id: Optional[str] = None,
        data_points: Optional[List['ReportViolationDataPoint']] = None,
    ) -> None:
        """
        Initialize a ReportViolationsDrift object.

        :param str home_account_id: (optional) The ID of the home account.
        :param str report_group_id: (optional) The ID of the report group.
        :param List[ReportViolationDataPoint] data_points: (optional) The list of
               report violations data points.
        """
        self.home_account_id = home_account_id
        self.report_group_id = report_group_id
        self.data_points = data_points

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReportViolationsDrift':
        """Initialize a ReportViolationsDrift object from a json dictionary."""
        args = {}
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (report_group_id := _dict.get('report_group_id')) is not None:
            args['report_group_id'] = report_group_id
        if (data_points := _dict.get('data_points')) is not None:
            args['data_points'] = [ReportViolationDataPoint.from_dict(v) for v in data_points]
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
        if hasattr(self, 'report_group_id') and self.report_group_id is not None:
            _dict['report_group_id'] = self.report_group_id
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
    The required configurations for a Rule.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a RequiredConfig object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['RequiredConfigConditionBase', 'RequiredConfigConditionList', 'RequiredConfigConditionSubRule'])
        )
        raise Exception(msg)


class Resource:
    """
    The resource.

    :param str report_id: (optional) The ID of the report.
    :param str home_account_id: (optional) The ID of the home account.
    :param str id: (optional) The resource CRN.
    :param str resource_name: (optional) The resource name.
    :param Account account: (optional) The account that is associated with a report.
    :param str component_id: (optional) The ID of the component.
    :param str component_name: (optional) The name of the component.
    :param str environment: (optional) The environment.
    :param Tags tags: (optional) The collection of different types of tags.
    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of evaluations.
    :param int pass_count: (optional) The number of passed evaluations.
    :param int failure_count: (optional) The number of failed evaluations.
    :param int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :param int skipped_count: (optional) The number of assessments with no
          corresponding evaluations.
    :param int completed_count: (optional) The total number of completed
          evaluations.
    :param str service_name: (optional) The name of the service.
    :param str instance_crn: (optional) The instance CRN.
    """

    def __init__(
        self,
        status: str,
        *,
        report_id: Optional[str] = None,
        home_account_id: Optional[str] = None,
        id: Optional[str] = None,
        resource_name: Optional[str] = None,
        account: Optional['Account'] = None,
        component_id: Optional[str] = None,
        component_name: Optional[str] = None,
        environment: Optional[str] = None,
        tags: Optional['Tags'] = None,
        total_count: Optional[int] = None,
        pass_count: Optional[int] = None,
        failure_count: Optional[int] = None,
        error_count: Optional[int] = None,
        skipped_count: Optional[int] = None,
        completed_count: Optional[int] = None,
        service_name: Optional[str] = None,
        instance_crn: Optional[str] = None,
    ) -> None:
        """
        Initialize a Resource object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param str report_id: (optional) The ID of the report.
        :param str home_account_id: (optional) The ID of the home account.
        :param str id: (optional) The resource CRN.
        :param str resource_name: (optional) The resource name.
        :param Account account: (optional) The account that is associated with a
               report.
        :param str component_id: (optional) The ID of the component.
        :param str component_name: (optional) The name of the component.
        :param str environment: (optional) The environment.
        :param Tags tags: (optional) The collection of different types of tags.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int skipped_count: (optional) The number of assessments with no
               corresponding evaluations.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        :param str service_name: (optional) The name of the service.
        :param str instance_crn: (optional) The instance CRN.
        """
        self.report_id = report_id
        self.home_account_id = home_account_id
        self.id = id
        self.resource_name = resource_name
        self.account = account
        self.component_id = component_id
        self.component_name = component_name
        self.environment = environment
        self.tags = tags
        self.status = status
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.skipped_count = skipped_count
        self.completed_count = completed_count
        self.service_name = service_name
        self.instance_crn = instance_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (resource_name := _dict.get('resource_name')) is not None:
            args['resource_name'] = resource_name
        if (account := _dict.get('account')) is not None:
            args['account'] = Account.from_dict(account)
        if (component_id := _dict.get('component_id')) is not None:
            args['component_id'] = component_id
        if (component_name := _dict.get('component_name')) is not None:
            args['component_name'] = component_name
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = Tags.from_dict(tags)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in Resource JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (pass_count := _dict.get('pass_count')) is not None:
            args['pass_count'] = pass_count
        if (failure_count := _dict.get('failure_count')) is not None:
            args['failure_count'] = failure_count
        if (error_count := _dict.get('error_count')) is not None:
            args['error_count'] = error_count
        if (skipped_count := _dict.get('skipped_count')) is not None:
            args['skipped_count'] = skipped_count
        if (completed_count := _dict.get('completed_count')) is not None:
            args['completed_count'] = completed_count
        if (service_name := _dict.get('service_name')) is not None:
            args['service_name'] = service_name
        if (instance_crn := _dict.get('instance_crn')) is not None:
            args['instance_crn'] = instance_crn
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
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'account') and self.account is not None:
            if isinstance(self.account, dict):
                _dict['account'] = self.account
            else:
                _dict['account'] = self.account.to_dict()
        if hasattr(self, 'component_id') and self.component_id is not None:
            _dict['component_id'] = self.component_id
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'tags') and self.tags is not None:
            if isinstance(self.tags, dict):
                _dict['tags'] = self.tags
            else:
                _dict['tags'] = self.tags.to_dict()
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
        if hasattr(self, 'skipped_count') and self.skipped_count is not None:
            _dict['skipped_count'] = self.skipped_count
        if hasattr(self, 'completed_count') and self.completed_count is not None:
            _dict['completed_count'] = self.completed_count
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
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
        NOT_APPLICABLE = 'not_applicable'



class ResourcePage:
    """
    The page of resource evaluation summaries.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param str report_id: (optional) The ID of the report.
    :param str home_account_id: (optional) The ID of the home account.
    :param List[Resource] resources: (optional) The list of resource evaluation
          summaries that are on the page.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
        report_id: Optional[str] = None,
        home_account_id: Optional[str] = None,
        resources: Optional[List['Resource']] = None,
    ) -> None:
        """
        Initialize a ResourcePage object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        :param str report_id: (optional) The ID of the report.
        :param str home_account_id: (optional) The ID of the home account.
        :param List[Resource] resources: (optional) The list of resource evaluation
               summaries that are on the page.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.report_id = report_id
        self.home_account_id = home_account_id
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourcePage':
        """Initialize a ResourcePage object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ResourcePage JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ResourcePage JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (report_id := _dict.get('report_id')) is not None:
            args['report_id'] = report_id
        if (home_account_id := _dict.get('home_account_id')) is not None:
            args['home_account_id'] = home_account_id
        if (resources := _dict.get('resources')) is not None:
            args['resources'] = [Resource.from_dict(v) for v in resources]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourcePage object from a json dictionary."""
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
        if hasattr(self, 'report_id') and self.report_id is not None:
            _dict['report_id'] = self.report_id
        if hasattr(self, 'home_account_id') and self.home_account_id is not None:
            _dict['home_account_id'] = self.home_account_id
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

    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of checks.
    :param int compliant_count: (optional) The number of compliant checks.
    :param int not_compliant_count: (optional) The number of checks that are not
          compliant.
    :param int unable_to_perform_count: (optional) The number of checks that are
          unable to perform.
    :param int user_evaluation_required_count: (optional) The number of checks that
          require a user evaluation.
    :param int not_applicable_count: (optional) The number of not applicable (with
          no evaluations) checks.
    :param List[ResourceSummaryItem] top_failed: (optional) The top 10 resources
          that have the most failures.
    """

    def __init__(
        self,
        status: str,
        *,
        total_count: Optional[int] = None,
        compliant_count: Optional[int] = None,
        not_compliant_count: Optional[int] = None,
        unable_to_perform_count: Optional[int] = None,
        user_evaluation_required_count: Optional[int] = None,
        not_applicable_count: Optional[int] = None,
        top_failed: Optional[List['ResourceSummaryItem']] = None,
    ) -> None:
        """
        Initialize a ResourceSummary object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param int total_count: (optional) The total number of checks.
        :param int compliant_count: (optional) The number of compliant checks.
        :param int not_compliant_count: (optional) The number of checks that are
               not compliant.
        :param int unable_to_perform_count: (optional) The number of checks that
               are unable to perform.
        :param int user_evaluation_required_count: (optional) The number of checks
               that require a user evaluation.
        :param int not_applicable_count: (optional) The number of not applicable
               (with no evaluations) checks.
        :param List[ResourceSummaryItem] top_failed: (optional) The top 10
               resources that have the most failures.
        """
        self.status = status
        self.total_count = total_count
        self.compliant_count = compliant_count
        self.not_compliant_count = not_compliant_count
        self.unable_to_perform_count = unable_to_perform_count
        self.user_evaluation_required_count = user_evaluation_required_count
        self.not_applicable_count = not_applicable_count
        self.top_failed = top_failed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceSummary':
        """Initialize a ResourceSummary object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ResourceSummary JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (compliant_count := _dict.get('compliant_count')) is not None:
            args['compliant_count'] = compliant_count
        if (not_compliant_count := _dict.get('not_compliant_count')) is not None:
            args['not_compliant_count'] = not_compliant_count
        if (unable_to_perform_count := _dict.get('unable_to_perform_count')) is not None:
            args['unable_to_perform_count'] = unable_to_perform_count
        if (user_evaluation_required_count := _dict.get('user_evaluation_required_count')) is not None:
            args['user_evaluation_required_count'] = user_evaluation_required_count
        if (not_applicable_count := _dict.get('not_applicable_count')) is not None:
            args['not_applicable_count'] = not_applicable_count
        if (top_failed := _dict.get('top_failed')) is not None:
            args['top_failed'] = [ResourceSummaryItem.from_dict(v) for v in top_failed]
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
        if hasattr(self, 'not_applicable_count') and self.not_applicable_count is not None:
            _dict['not_applicable_count'] = self.not_applicable_count
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
        NOT_APPLICABLE = 'not_applicable'



class ResourceSummaryItem:
    """
    The resource summary item.

    :param str id: (optional) The resource ID.
    :param str name: (optional) The resource name.
    :param str account: (optional) The account that owns the resource.
    :param str service: (optional) The service that is managing the resource.
    :param str service_display_name: (optional) The services display name that is
          managing the resource.
    :param Tags tags: (optional) The collection of different types of tags.
    :param str status: The allowed values of an aggregated status for controls,
          specifications, assessments, and resources.
    :param int total_count: (optional) The total number of evaluations.
    :param int pass_count: (optional) The number of passed evaluations.
    :param int failure_count: (optional) The number of failed evaluations.
    :param int error_count: (optional) The number of evaluations that started, but
          did not finish, and ended with errors.
    :param int skipped_count: (optional) The number of assessments with no
          corresponding evaluations.
    :param int completed_count: (optional) The total number of completed
          evaluations.
    """

    def __init__(
        self,
        status: str,
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        account: Optional[str] = None,
        service: Optional[str] = None,
        service_display_name: Optional[str] = None,
        tags: Optional['Tags'] = None,
        total_count: Optional[int] = None,
        pass_count: Optional[int] = None,
        failure_count: Optional[int] = None,
        error_count: Optional[int] = None,
        skipped_count: Optional[int] = None,
        completed_count: Optional[int] = None,
    ) -> None:
        """
        Initialize a ResourceSummaryItem object.

        :param str status: The allowed values of an aggregated status for controls,
               specifications, assessments, and resources.
        :param str id: (optional) The resource ID.
        :param str name: (optional) The resource name.
        :param str account: (optional) The account that owns the resource.
        :param str service: (optional) The service that is managing the resource.
        :param str service_display_name: (optional) The services display name that
               is managing the resource.
        :param Tags tags: (optional) The collection of different types of tags.
        :param int total_count: (optional) The total number of evaluations.
        :param int pass_count: (optional) The number of passed evaluations.
        :param int failure_count: (optional) The number of failed evaluations.
        :param int error_count: (optional) The number of evaluations that started,
               but did not finish, and ended with errors.
        :param int skipped_count: (optional) The number of assessments with no
               corresponding evaluations.
        :param int completed_count: (optional) The total number of completed
               evaluations.
        """
        self.id = id
        self.name = name
        self.account = account
        self.service = service
        self.service_display_name = service_display_name
        self.tags = tags
        self.status = status
        self.total_count = total_count
        self.pass_count = pass_count
        self.failure_count = failure_count
        self.error_count = error_count
        self.skipped_count = skipped_count
        self.completed_count = completed_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceSummaryItem':
        """Initialize a ResourceSummaryItem object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (account := _dict.get('account')) is not None:
            args['account'] = account
        if (service := _dict.get('service')) is not None:
            args['service'] = service
        if (service_display_name := _dict.get('service_display_name')) is not None:
            args['service_display_name'] = service_display_name
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = Tags.from_dict(tags)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ResourceSummaryItem JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        if (pass_count := _dict.get('pass_count')) is not None:
            args['pass_count'] = pass_count
        if (failure_count := _dict.get('failure_count')) is not None:
            args['failure_count'] = failure_count
        if (error_count := _dict.get('error_count')) is not None:
            args['error_count'] = error_count
        if (skipped_count := _dict.get('skipped_count')) is not None:
            args['skipped_count'] = skipped_count
        if (completed_count := _dict.get('completed_count')) is not None:
            args['completed_count'] = completed_count
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceSummaryItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'account') and self.account is not None:
            _dict['account'] = self.account
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service
        if hasattr(self, 'service_display_name') and self.service_display_name is not None:
            _dict['service_display_name'] = self.service_display_name
        if hasattr(self, 'tags') and self.tags is not None:
            if isinstance(self.tags, dict):
                _dict['tags'] = self.tags
            else:
                _dict['tags'] = self.tags.to_dict()
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
        if hasattr(self, 'skipped_count') and self.skipped_count is not None:
            _dict['skipped_count'] = self.skipped_count
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
        NOT_APPLICABLE = 'not_applicable'



class Rule:
    """
    The rule response that corresponds to an account instance.

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
    :param Import import_: (optional) The collection of import parameters.
    :param RuleTarget target: The rule target.
    :param RequiredConfig required_config: The required configurations for a Rule.
    :param List[str] labels: The list of labels.
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
        target: 'RuleTarget',
        required_config: 'RequiredConfig',
        labels: List[str],
        *,
        import_: Optional['Import'] = None,
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
        :param RuleTarget target: The rule target.
        :param RequiredConfig required_config: The required configurations for a
               Rule.
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
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        else:
            raise ValueError('Required property \'created_on\' not present in Rule JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in Rule JSON')
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        else:
            raise ValueError('Required property \'updated_on\' not present in Rule JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        else:
            raise ValueError('Required property \'updated_by\' not present in Rule JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Rule JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in Rule JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in Rule JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in Rule JSON')
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in Rule JSON')
        if (import_ := _dict.get('import')) is not None:
            args['import_'] = Import.from_dict(import_)
        if (target := _dict.get('target')) is not None:
            args['target'] = RuleTarget.from_dict(target)
        else:
            raise ValueError('Required property \'target\' not present in Rule JSON')
        if (required_config := _dict.get('required_config')) is not None:
            args['required_config'] = required_config
        else:
            raise ValueError('Required property \'required_config\' not present in Rule JSON')
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
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



class RuleCollection:
    """
    The page of rules.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[Rule] rules: (optional) The collection of rules that correspond to
          an account instance. Maximum of 100/500 custom rules per stand-alone/enterprise
          account.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
        rules: Optional[List['Rule']] = None,
    ) -> None:
        """
        Initialize a RuleCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param PageHRefFirst first: (optional) A page reference.
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
    def from_dict(cls, _dict: Dict) -> 'RuleCollection':
        """Initialize a RuleCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in RuleCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in RuleCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (rules := _dict.get('rules')) is not None:
            args['rules'] = [Rule.from_dict(v) for v in rules]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleCollection object from a json dictionary."""
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
        """Return a `str` version of this RuleCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleInfo:
    """
    The rule.

    :param str id: (optional) The rule ID.
    :param str type: (optional) The rule type.
    :param str description: (optional) The rule description.
    :param str version: (optional) The rule version.
    :param str account_id: (optional) The rule account ID.
    :param datetime created_on: (optional) The date when the rule was created.
    :param str created_by: (optional) The ID of the user who created the rule.
    :param datetime updated_on: (optional) The date when the rule was updated.
    :param str updated_by: (optional) The ID of the user who updated the rule.
    :param List[str] labels: (optional) The rule labels.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        description: Optional[str] = None,
        version: Optional[str] = None,
        account_id: Optional[str] = None,
        created_on: Optional[datetime] = None,
        created_by: Optional[str] = None,
        updated_on: Optional[datetime] = None,
        updated_by: Optional[str] = None,
        labels: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a RuleInfo object.

        :param str id: (optional) The rule ID.
        :param str type: (optional) The rule type.
        :param str description: (optional) The rule description.
        :param str version: (optional) The rule version.
        :param str account_id: (optional) The rule account ID.
        :param datetime created_on: (optional) The date when the rule was created.
        :param str created_by: (optional) The ID of the user who created the rule.
        :param datetime updated_on: (optional) The date when the rule was updated.
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
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        if (labels := _dict.get('labels')) is not None:
            args['labels'] = labels
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
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
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


class RuleParameter:
    """
    The rule import parameter.

    :param str name: (optional) The import parameter name.
    :param str display_name: (optional) The display name of the property.
    :param str description: (optional) The propery description.
    :param str type: The property type.
    """

    def __init__(
        self,
        type: str,
        *,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuleParameter object.

        :param str type: The property type.
        :param str name: (optional) The import parameter name.
        :param str display_name: (optional) The display name of the property.
        :param str description: (optional) The propery description.
        """
        self.name = name
        self.display_name = display_name
        self.description = description
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleParameter':
        """Initialize a RuleParameter object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (display_name := _dict.get('display_name')) is not None:
            args['display_name'] = display_name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in RuleParameter JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleParameter object from a json dictionary."""
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
        """Return a `str` version of this RuleParameter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleParameter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleParameter') -> bool:
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



class RuleProperty:
    """
    The supported config property.

    :param str name: (optional) The property name.
    :param str description: (optional) The property description.
    :param str type: The operator kind used when evaluating a property.
    """

    def __init__(
        self,
        type: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuleProperty object.

        :param str type: The operator kind used when evaluating a property.
        :param str name: (optional) The property name.
        :param str description: (optional) The property description.
        """
        self.name = name
        self.description = description
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleProperty':
        """Initialize a RuleProperty object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in RuleProperty JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The operator kind used when evaluating a property.
        """

        STRING = 'string'
        NUMERIC = 'numeric'
        GENERAL = 'general'
        BOOLEAN = 'boolean'
        STRING_LIST = 'string_list'
        IP_LIST = 'ip_list'
        TIMESTAMP = 'timestamp'



class RuleTarget:
    """
    The rule target.

    :param str service_name: The target service name.
    :param str service_display_name: (optional) The display name of the target
          service.
    :param str resource_kind: The target resource kind.
    :param List[AdditionalTargetAttribute] additional_target_attributes: (optional)
          The additional target attributes used to filter to a subset of resources.
    :param str ref: (optional) The name of target when used in a rule.
    """

    def __init__(
        self,
        service_name: str,
        resource_kind: str,
        *,
        service_display_name: Optional[str] = None,
        additional_target_attributes: Optional[List['AdditionalTargetAttribute']] = None,
        ref: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuleTarget object.

        :param str service_name: The target service name.
        :param str resource_kind: The target resource kind.
        :param str service_display_name: (optional) The display name of the target
               service.
        :param List[AdditionalTargetAttribute] additional_target_attributes:
               (optional) The additional target attributes used to filter to a subset of
               resources.
        :param str ref: (optional) The name of target when used in a rule.
        """
        self.service_name = service_name
        self.service_display_name = service_display_name
        self.resource_kind = resource_kind
        self.additional_target_attributes = additional_target_attributes
        self.ref = ref

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleTarget':
        """Initialize a RuleTarget object from a json dictionary."""
        args = {}
        if (service_name := _dict.get('service_name')) is not None:
            args['service_name'] = service_name
        else:
            raise ValueError('Required property \'service_name\' not present in RuleTarget JSON')
        if (service_display_name := _dict.get('service_display_name')) is not None:
            args['service_display_name'] = service_display_name
        if (resource_kind := _dict.get('resource_kind')) is not None:
            args['resource_kind'] = resource_kind
        else:
            raise ValueError('Required property \'resource_kind\' not present in RuleTarget JSON')
        if (additional_target_attributes := _dict.get('additional_target_attributes')) is not None:
            args['additional_target_attributes'] = [AdditionalTargetAttribute.from_dict(v) for v in additional_target_attributes]
        if (ref := _dict.get('ref')) is not None:
            args['ref'] = ref
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleTarget object from a json dictionary."""
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
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleTarget object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleTarget') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleTarget') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleTargetPrototype:
    """
    The rule target.

    :param str service_name: The target service name.
    :param str resource_kind: The target resource kind.
    :param List[AdditionalTargetAttribute] additional_target_attributes: (optional)
          The additional target attributes used to filter to a subset of resources.
    """

    def __init__(
        self,
        service_name: str,
        resource_kind: str,
        *,
        additional_target_attributes: Optional[List['AdditionalTargetAttribute']] = None,
    ) -> None:
        """
        Initialize a RuleTargetPrototype object.

        :param str service_name: The target service name.
        :param str resource_kind: The target resource kind.
        :param List[AdditionalTargetAttribute] additional_target_attributes:
               (optional) The additional target attributes used to filter to a subset of
               resources.
        """
        self.service_name = service_name
        self.resource_kind = resource_kind
        self.additional_target_attributes = additional_target_attributes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleTargetPrototype':
        """Initialize a RuleTargetPrototype object from a json dictionary."""
        args = {}
        if (service_name := _dict.get('service_name')) is not None:
            args['service_name'] = service_name
        else:
            raise ValueError('Required property \'service_name\' not present in RuleTargetPrototype JSON')
        if (resource_kind := _dict.get('resource_kind')) is not None:
            args['resource_kind'] = resource_kind
        else:
            raise ValueError('Required property \'resource_kind\' not present in RuleTargetPrototype JSON')
        if (additional_target_attributes := _dict.get('additional_target_attributes')) is not None:
            args['additional_target_attributes'] = [AdditionalTargetAttribute.from_dict(v) for v in additional_target_attributes]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleTargetPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
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
        """Return a `str` version of this RuleTargetPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleTargetPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleTargetPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ScanReport:
    """
    A report detailing the evaluations related to a specific control.

    :param str id: (optional) The ID of the scan report.
    :param str scan_id: (optional) The ID of the scan.
    :param str instance_id: (optional) The ID of the Security and Compliance Center
          instance.
    :param str scope_id: (optional) The ID of the scope.
    :param str subscope_id: (optional) The ID of the sub-scope.
    :param str status: The enum of different scan report status.
    :param datetime created_on: (optional) The date when the report was created.
    :param str format: The file type of the report.
    :param str href: (optional) The URL of the scan report.
    """

    def __init__(
        self,
        status: str,
        format: str,
        *,
        id: Optional[str] = None,
        scan_id: Optional[str] = None,
        instance_id: Optional[str] = None,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        created_on: Optional[datetime] = None,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a ScanReport object.

        :param str status: The enum of different scan report status.
        :param str format: The file type of the report.
        :param str id: (optional) The ID of the scan report.
        :param str scan_id: (optional) The ID of the scan.
        :param str instance_id: (optional) The ID of the Security and Compliance
               Center instance.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the sub-scope.
        :param datetime created_on: (optional) The date when the report was
               created.
        :param str href: (optional) The URL of the scan report.
        """
        self.id = id
        self.scan_id = scan_id
        self.instance_id = instance_id
        self.scope_id = scope_id
        self.subscope_id = subscope_id
        self.status = status
        self.created_on = created_on
        self.format = format
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScanReport':
        """Initialize a ScanReport object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (scan_id := _dict.get('scan_id')) is not None:
            args['scan_id'] = scan_id
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        if (scope_id := _dict.get('scope_id')) is not None:
            args['scope_id'] = scope_id
        if (subscope_id := _dict.get('subscope_id')) is not None:
            args['subscope_id'] = subscope_id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in ScanReport JSON')
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (format := _dict.get('format')) is not None:
            args['format'] = format
        else:
            raise ValueError('Required property \'format\' not present in ScanReport JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScanReport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'scan_id') and self.scan_id is not None:
            _dict['scan_id'] = self.scan_id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'scope_id') and self.scope_id is not None:
            _dict['scope_id'] = self.scope_id
        if hasattr(self, 'subscope_id') and self.subscope_id is not None:
            _dict['subscope_id'] = self.subscope_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'format') and self.format is not None:
            _dict['format'] = self.format
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScanReport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScanReport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScanReport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The enum of different scan report status.
        """

        PENDING = 'pending'
        IN_PROGRESS = 'in_progress'
        ERROR = 'error'
        COMPLETED = 'completed'
        DELETED = 'deleted'


    class FormatEnum(str, Enum):
        """
        The file type of the report.
        """

        CSV = 'csv'
        PDF = 'pdf'



class ScanReportCollection:
    """
    The page of scan reports.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param str scope_id: (optional) The id of the requested scope.
    :param str subscope_id: (optional) The id of the requested subscope.
    :param List[ScanReport] scan_reports: (optional) The list of scan reports.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
        scope_id: Optional[str] = None,
        subscope_id: Optional[str] = None,
        scan_reports: Optional[List['ScanReport']] = None,
    ) -> None:
        """
        Initialize a ScanReportCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        :param str scope_id: (optional) The id of the requested scope.
        :param str subscope_id: (optional) The id of the requested subscope.
        :param List[ScanReport] scan_reports: (optional) The list of scan reports.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.scope_id = scope_id
        self.subscope_id = subscope_id
        self.scan_reports = scan_reports

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScanReportCollection':
        """Initialize a ScanReportCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ScanReportCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ScanReportCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (scope_id := _dict.get('scope_id')) is not None:
            args['scope_id'] = scope_id
        if (subscope_id := _dict.get('subscope_id')) is not None:
            args['subscope_id'] = subscope_id
        if (scan_reports := _dict.get('scan_reports')) is not None:
            args['scan_reports'] = [ScanReport.from_dict(v) for v in scan_reports]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScanReportCollection object from a json dictionary."""
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
        if hasattr(self, 'scope_id') and self.scope_id is not None:
            _dict['scope_id'] = self.scope_id
        if hasattr(self, 'subscope_id') and self.subscope_id is not None:
            _dict['subscope_id'] = self.subscope_id
        if hasattr(self, 'scan_reports') and self.scan_reports is not None:
            scan_reports_list = []
            for v in self.scan_reports:
                if isinstance(v, dict):
                    scan_reports_list.append(v)
                else:
                    scan_reports_list.append(v.to_dict())
            _dict['scan_reports'] = scan_reports_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScanReportCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScanReportCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScanReportCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Scope:
    """
    The group of resources that you want to evaluate. In the new API-based architecture, a
    scope can be an Enterprise, Account group, Account, or Resource group.

    :param str id: The ID of the scope.
    :param str name: The scope name.
    :param str description: The scope description.
    :param str environment: The scope environment. This value details what cloud
          provider the scope targets.
    :param List[ScopeProperty] properties: The properties that are supported for
          scoping by this environment.
    :param str account_id: The ID of the account associated with the scope.
    :param str instance_id: The ID of the instance associated with the scope.
    :param str created_by: The identifier of the account or service ID who created
          the scope.
    :param datetime created_on: The date when the scope was created.
    :param str updated_by: The ID of the user or service ID who updated the scope.
    :param datetime updated_on: The date when the scope was updated.
    :param float attachment_count: The number of attachments tied to the scope.
    """

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        environment: str,
        properties: List['ScopeProperty'],
        account_id: str,
        instance_id: str,
        created_by: str,
        created_on: datetime,
        updated_by: str,
        updated_on: datetime,
        attachment_count: float,
    ) -> None:
        """
        Initialize a Scope object.

        :param str id: The ID of the scope.
        :param str name: The scope name.
        :param str description: The scope description.
        :param str environment: The scope environment. This value details what
               cloud provider the scope targets.
        :param List[ScopeProperty] properties: The properties that are supported
               for scoping by this environment.
        :param str account_id: The ID of the account associated with the scope.
        :param str instance_id: The ID of the instance associated with the scope.
        :param str created_by: The identifier of the account or service ID who
               created the scope.
        :param datetime created_on: The date when the scope was created.
        :param str updated_by: The ID of the user or service ID who updated the
               scope.
        :param datetime updated_on: The date when the scope was updated.
        :param float attachment_count: The number of attachments tied to the scope.
        """
        self.id = id
        self.name = name
        self.description = description
        self.environment = environment
        self.properties = properties
        self.account_id = account_id
        self.instance_id = instance_id
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on
        self.attachment_count = attachment_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Scope':
        """Initialize a Scope object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Scope JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Scope JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in Scope JSON')
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        else:
            raise ValueError('Required property \'environment\' not present in Scope JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        else:
            raise ValueError('Required property \'properties\' not present in Scope JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in Scope JSON')
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        else:
            raise ValueError('Required property \'instance_id\' not present in Scope JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in Scope JSON')
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        else:
            raise ValueError('Required property \'created_on\' not present in Scope JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        else:
            raise ValueError('Required property \'updated_by\' not present in Scope JSON')
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        else:
            raise ValueError('Required property \'updated_on\' not present in Scope JSON')
        if (attachment_count := _dict.get('attachment_count')) is not None:
            args['attachment_count'] = attachment_count
        else:
            raise ValueError('Required property \'attachment_count\' not present in Scope JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Scope object from a json dictionary."""
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
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
        if hasattr(self, 'attachment_count') and self.attachment_count is not None:
            _dict['attachment_count'] = self.attachment_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Scope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Scope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Scope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ScopeCollection:
    """
    A list of scopes.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[Scope] scopes: The array of scopes.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        scopes: List['Scope'],
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
    ) -> None:
        """
        Initialize a ScopeCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param List[Scope] scopes: The array of scopes.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.scopes = scopes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopeCollection':
        """Initialize a ScopeCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in ScopeCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in ScopeCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (scopes := _dict.get('scopes')) is not None:
            args['scopes'] = [Scope.from_dict(v) for v in scopes]
        else:
            raise ValueError('Required property \'scopes\' not present in ScopeCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopeCollection object from a json dictionary."""
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
        if hasattr(self, 'scopes') and self.scopes is not None:
            scopes_list = []
            for v in self.scopes:
                if isinstance(v, dict):
                    scopes_list.append(v)
                else:
                    scopes_list.append(v.to_dict())
            _dict['scopes'] = scopes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScopeCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopeCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopeCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ScopeID:
    """
    The scope ID that is associated with a report. Attributes for this object will be
    blank if the report has multiple scopes tied to the report.

    :param str id: (optional) The scope ID.
    :param str type: (optional) The scope type.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ScopeID object.

        :param str id: (optional) The scope ID.
        :param str type: (optional) The scope type.
        """
        self.id = id
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopeID':
        """Initialize a ScopeID object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopeID object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScopeID object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopeID') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopeID') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ScopeProperty:
    """
    ScopeProperty.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ScopeProperty object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['ScopePropertyScopeType', 'ScopePropertyScopeId', 'ScopePropertyExclusions'])
        )
        raise Exception(msg)


class ScopePropertyExclusionItem:
    """
    Any exclusion to be defined in the scope.

    :param str scope_id: (optional)
    :param str scope_type: The type of scope it targets
          The scope values are as followed:
          - enterprise: The scope targets an enterprise account
          - enterprise.account_group: The scope targets an account group within an
          enterprise
          - enterprise.account: The scope targets an account within an enterprise
          - account: The scope targets an account not tied to an enterprise
          - account.resource_group: The scope targets a resource group within an account.
    """

    def __init__(
        self,
        scope_type: str,
        *,
        scope_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ScopePropertyExclusionItem object.

        :param str scope_type: The type of scope it targets
               The scope values are as followed:
               - enterprise: The scope targets an enterprise account
               - enterprise.account_group: The scope targets an account group within an
               enterprise
               - enterprise.account: The scope targets an account within an enterprise
               - account: The scope targets an account not tied to an enterprise
               - account.resource_group: The scope targets a resource group within an
               account.
        :param str scope_id: (optional)
        """
        self.scope_id = scope_id
        self.scope_type = scope_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopePropertyExclusionItem':
        """Initialize a ScopePropertyExclusionItem object from a json dictionary."""
        args = {}
        if (scope_id := _dict.get('scope_id')) is not None:
            args['scope_id'] = scope_id
        if (scope_type := _dict.get('scope_type')) is not None:
            args['scope_type'] = scope_type
        else:
            raise ValueError('Required property \'scope_type\' not present in ScopePropertyExclusionItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopePropertyExclusionItem object from a json dictionary."""
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
        """Return a `str` version of this ScopePropertyExclusionItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopePropertyExclusionItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopePropertyExclusionItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ScopeTypeEnum(str, Enum):
        """
        The type of scope it targets
        The scope values are as followed:
        - enterprise: The scope targets an enterprise account
        - enterprise.account_group: The scope targets an account group within an
        enterprise
        - enterprise.account: The scope targets an account within an enterprise
        - account: The scope targets an account not tied to an enterprise
        - account.resource_group: The scope targets a resource group within an account.
        """

        ENTERPRISE = 'enterprise'
        ENTERPRISE_ACCOUNT_GROUP = 'enterprise.account_group'
        ENTERPRISE_ACCOUNT = 'enterprise.account'
        ACCOUNT = 'account'
        ACCOUNT_RESOURCE_GROUP = 'account.resource_group'



class ScopePrototype:
    """
    The request body to make a Scope.

    :param str name: (optional) The scope name.
    :param str description: (optional) The scope description.
    :param str environment: (optional) The scope environment.
    :param List[ScopeProperty] properties: (optional) The properties that are
          supported for scoping by this environment.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
        properties: Optional[List['ScopeProperty']] = None,
    ) -> None:
        """
        Initialize a ScopePrototype object.

        :param str name: (optional) The scope name.
        :param str description: (optional) The scope description.
        :param str environment: (optional) The scope environment.
        :param List[ScopeProperty] properties: (optional) The properties that are
               supported for scoping by this environment.
        """
        self.name = name
        self.description = description
        self.environment = environment
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopePrototype':
        """Initialize a ScopePrototype object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopePrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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
        """Return a `str` version of this ScopePrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopePrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopePrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Service:
    """
    The response body for creating a service instance.

    :param datetime created_on: The service creation date.
    :param str created_by: The service author.
    :param datetime updated_on: The date when the service was modified.
    :param str updated_by: The user who modified the service.
    :param str service_name: The service name.
    :param str service_display_name: (optional) The display name of the service.
    :param str description: The service description.
    :param bool monitoring_enabled: The indication of whether monitoring is enabled.
    :param bool enforcement_enabled: The indication of whether enforcement is
          enabled.
    :param bool service_listing_enabled: The indication of whether service listing
          is enabled.
    :param ConfigurationInformationPoints config_information_point: The service
          configuration information.
    :param List[SupportedConfigs] supported_configs: The supported configurations.
    """

    def __init__(
        self,
        created_on: datetime,
        created_by: str,
        updated_on: datetime,
        updated_by: str,
        service_name: str,
        description: str,
        monitoring_enabled: bool,
        enforcement_enabled: bool,
        service_listing_enabled: bool,
        config_information_point: 'ConfigurationInformationPoints',
        supported_configs: List['SupportedConfigs'],
        *,
        service_display_name: Optional[str] = None,
    ) -> None:
        """
        Initialize a Service object.

        :param datetime created_on: The service creation date.
        :param str created_by: The service author.
        :param datetime updated_on: The date when the service was modified.
        :param str updated_by: The user who modified the service.
        :param str service_name: The service name.
        :param str description: The service description.
        :param bool monitoring_enabled: The indication of whether monitoring is
               enabled.
        :param bool enforcement_enabled: The indication of whether enforcement is
               enabled.
        :param bool service_listing_enabled: The indication of whether service
               listing is enabled.
        :param ConfigurationInformationPoints config_information_point: The service
               configuration information.
        :param List[SupportedConfigs] supported_configs: The supported
               configurations.
        :param str service_display_name: (optional) The display name of the
               service.
        """
        self.created_on = created_on
        self.created_by = created_by
        self.updated_on = updated_on
        self.updated_by = updated_by
        self.service_name = service_name
        self.service_display_name = service_display_name
        self.description = description
        self.monitoring_enabled = monitoring_enabled
        self.enforcement_enabled = enforcement_enabled
        self.service_listing_enabled = service_listing_enabled
        self.config_information_point = config_information_point
        self.supported_configs = supported_configs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Service':
        """Initialize a Service object from a json dictionary."""
        args = {}
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        else:
            raise ValueError('Required property \'created_on\' not present in Service JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        else:
            raise ValueError('Required property \'created_by\' not present in Service JSON')
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        else:
            raise ValueError('Required property \'updated_on\' not present in Service JSON')
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        else:
            raise ValueError('Required property \'updated_by\' not present in Service JSON')
        if (service_name := _dict.get('service_name')) is not None:
            args['service_name'] = service_name
        else:
            raise ValueError('Required property \'service_name\' not present in Service JSON')
        if (service_display_name := _dict.get('service_display_name')) is not None:
            args['service_display_name'] = service_display_name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in Service JSON')
        if (monitoring_enabled := _dict.get('monitoring_enabled')) is not None:
            args['monitoring_enabled'] = monitoring_enabled
        else:
            raise ValueError('Required property \'monitoring_enabled\' not present in Service JSON')
        if (enforcement_enabled := _dict.get('enforcement_enabled')) is not None:
            args['enforcement_enabled'] = enforcement_enabled
        else:
            raise ValueError('Required property \'enforcement_enabled\' not present in Service JSON')
        if (service_listing_enabled := _dict.get('service_listing_enabled')) is not None:
            args['service_listing_enabled'] = service_listing_enabled
        else:
            raise ValueError('Required property \'service_listing_enabled\' not present in Service JSON')
        if (config_information_point := _dict.get('config_information_point')) is not None:
            args['config_information_point'] = ConfigurationInformationPoints.from_dict(config_information_point)
        else:
            raise ValueError('Required property \'config_information_point\' not present in Service JSON')
        if (supported_configs := _dict.get('supported_configs')) is not None:
            args['supported_configs'] = [SupportedConfigs.from_dict(v) for v in supported_configs]
        else:
            raise ValueError('Required property \'supported_configs\' not present in Service JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Service object from a json dictionary."""
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
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'service_display_name') and self.service_display_name is not None:
            _dict['service_display_name'] = self.service_display_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'monitoring_enabled') and self.monitoring_enabled is not None:
            _dict['monitoring_enabled'] = self.monitoring_enabled
        if hasattr(self, 'enforcement_enabled') and self.enforcement_enabled is not None:
            _dict['enforcement_enabled'] = self.enforcement_enabled
        if hasattr(self, 'service_listing_enabled') and self.service_listing_enabled is not None:
            _dict['service_listing_enabled'] = self.service_listing_enabled
        if hasattr(self, 'config_information_point') and self.config_information_point is not None:
            if isinstance(self.config_information_point, dict):
                _dict['config_information_point'] = self.config_information_point
            else:
                _dict['config_information_point'] = self.config_information_point.to_dict()
        if hasattr(self, 'supported_configs') and self.supported_configs is not None:
            supported_configs_list = []
            for v in self.supported_configs:
                if isinstance(v, dict):
                    supported_configs_list.append(v)
                else:
                    supported_configs_list.append(v.to_dict())
            _dict['supported_configs'] = supported_configs_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Service object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Service') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Service') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceCollection:
    """
    The services.

    :param List[Service] services: (optional) The list of services.
    """

    def __init__(
        self,
        *,
        services: Optional[List['Service']] = None,
    ) -> None:
        """
        Initialize a ServiceCollection object.

        :param List[Service] services: (optional) The list of services.
        """
        self.services = services

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceCollection':
        """Initialize a ServiceCollection object from a json dictionary."""
        args = {}
        if (services := _dict.get('services')) is not None:
            args['services'] = [Service.from_dict(v) for v in services]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'services') and self.services is not None:
            services_list = []
            for v in self.services:
                if isinstance(v, dict):
                    services_list.append(v)
                else:
                    services_list.append(v.to_dict())
            _dict['services'] = services_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Settings:
    """
    The settings.

    :param EventNotifications event_notifications: (optional) The Event
          Notifications settings.
    :param ObjectStorage object_storage: (optional) The Cloud Object Storage
          settings.
    """

    def __init__(
        self,
        *,
        event_notifications: Optional['EventNotifications'] = None,
        object_storage: Optional['ObjectStorage'] = None,
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
        if (event_notifications := _dict.get('event_notifications')) is not None:
            args['event_notifications'] = EventNotifications.from_dict(event_notifications)
        if (object_storage := _dict.get('object_storage')) is not None:
            args['object_storage'] = ObjectStorage.from_dict(object_storage)
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


class SubRule:
    """
    A rule within a rule used in the requiredConfig.

    :param RuleTarget target: (optional) The rule target.
    :param RequiredConfig required_config: (optional) The required configurations
          for a Rule.
    """

    def __init__(
        self,
        *,
        target: Optional['RuleTarget'] = None,
        required_config: Optional['RequiredConfig'] = None,
    ) -> None:
        """
        Initialize a SubRule object.

        :param RuleTarget target: (optional) The rule target.
        :param RequiredConfig required_config: (optional) The required
               configurations for a Rule.
        """
        self.target = target
        self.required_config = required_config

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubRule':
        """Initialize a SubRule object from a json dictionary."""
        args = {}
        if (target := _dict.get('target')) is not None:
            args['target'] = RuleTarget.from_dict(target)
        if (required_config := _dict.get('required_config')) is not None:
            args['required_config'] = required_config
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubRule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubRule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubRule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubRule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SubScope:
    """
    A segment of a scope. Subscopes are used to ensure that the members of your teams who
    review results only have access to the information regarding the instances that they
    have access to.

    :param str id: (optional) The Subscope ID.
    :param str name: (optional) The name of the Subscope.
    :param str description: (optional) Text to describe the Subscope.
    :param str environment: (optional) The virtual space where applications can be
          deployed and managed.
    :param List[ScopeProperty] properties: Additional attributes that are supported
          for scoping by this environment.
    """

    def __init__(
        self,
        properties: List['ScopeProperty'],
        *,
        id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> None:
        """
        Initialize a SubScope object.

        :param List[ScopeProperty] properties: Additional attributes that are
               supported for scoping by this environment.
        :param str id: (optional) The Subscope ID.
        :param str name: (optional) The name of the Subscope.
        :param str description: (optional) Text to describe the Subscope.
        :param str environment: (optional) The virtual space where applications can
               be deployed and managed.
        """
        self.id = id
        self.name = name
        self.description = description
        self.environment = environment
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubScope':
        """Initialize a SubScope object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        else:
            raise ValueError('Required property \'properties\' not present in SubScope JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubScope object from a json dictionary."""
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
        """Return a `str` version of this SubScope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubScope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubScope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SubScopeCollection:
    """
    The response body of the subscopes.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[SubScope] subscopes: The array of subscopes.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        subscopes: List['SubScope'],
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
    ) -> None:
        """
        Initialize a SubScopeCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param List[SubScope] subscopes: The array of subscopes.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.subscopes = subscopes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubScopeCollection':
        """Initialize a SubScopeCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in SubScopeCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in SubScopeCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (subscopes := _dict.get('subscopes')) is not None:
            args['subscopes'] = [SubScope.from_dict(v) for v in subscopes]
        else:
            raise ValueError('Required property \'subscopes\' not present in SubScopeCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubScopeCollection object from a json dictionary."""
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
        if hasattr(self, 'subscopes') and self.subscopes is not None:
            subscopes_list = []
            for v in self.subscopes:
                if isinstance(v, dict):
                    subscopes_list.append(v)
                else:
                    subscopes_list.append(v.to_dict())
            _dict['subscopes'] = subscopes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubScopeCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubScopeCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubScopeCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SubScopeResponse:
    """
    The response body of the subscope.

    :param List[SubScope] subscopes: The array of subscopes.
    """

    def __init__(
        self,
        subscopes: List['SubScope'],
    ) -> None:
        """
        Initialize a SubScopeResponse object.

        :param List[SubScope] subscopes: The array of subscopes.
        """
        self.subscopes = subscopes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SubScopeResponse':
        """Initialize a SubScopeResponse object from a json dictionary."""
        args = {}
        if (subscopes := _dict.get('subscopes')) is not None:
            args['subscopes'] = [SubScope.from_dict(v) for v in subscopes]
        else:
            raise ValueError('Required property \'subscopes\' not present in SubScopeResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SubScopeResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'subscopes') and self.subscopes is not None:
            subscopes_list = []
            for v in self.subscopes:
                if isinstance(v, dict):
                    subscopes_list.append(v)
                else:
                    subscopes_list.append(v.to_dict())
            _dict['subscopes'] = subscopes_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SubScopeResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SubScopeResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SubScopeResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SupportedConfigs:
    """
    The location information of supported configurations.

    :param str resource_kind: (optional) The supported config resource kind.
    :param List[AdditionalTargetAttribute] additional_target_attributes: (optional)
          The supported config list of additional target attributes.
    :param List[RuleProperty] properties: (optional) The supported config list
          properties.
    :param str description: (optional) The supported config description.
    :param bool cip_requires_service_instance: (optional) The indication of whether
          the configuration information point (CIP) requires a service instance.
    :param bool resource_group_support: (optional) The supported config resource
          group support.
    :param bool tagging_support: (optional) The supported config tagging support.
    :param bool inherit_tags: (optional) The supported config inherited tags.
    """

    def __init__(
        self,
        *,
        resource_kind: Optional[str] = None,
        additional_target_attributes: Optional[List['AdditionalTargetAttribute']] = None,
        properties: Optional[List['RuleProperty']] = None,
        description: Optional[str] = None,
        cip_requires_service_instance: Optional[bool] = None,
        resource_group_support: Optional[bool] = None,
        tagging_support: Optional[bool] = None,
        inherit_tags: Optional[bool] = None,
    ) -> None:
        """
        Initialize a SupportedConfigs object.

        :param str resource_kind: (optional) The supported config resource kind.
        :param List[AdditionalTargetAttribute] additional_target_attributes:
               (optional) The supported config list of additional target attributes.
        :param List[RuleProperty] properties: (optional) The supported config list
               properties.
        :param str description: (optional) The supported config description.
        :param bool cip_requires_service_instance: (optional) The indication of
               whether the configuration information point (CIP) requires a service
               instance.
        :param bool resource_group_support: (optional) The supported config
               resource group support.
        :param bool tagging_support: (optional) The supported config tagging
               support.
        :param bool inherit_tags: (optional) The supported config inherited tags.
        """
        self.resource_kind = resource_kind
        self.additional_target_attributes = additional_target_attributes
        self.properties = properties
        self.description = description
        self.cip_requires_service_instance = cip_requires_service_instance
        self.resource_group_support = resource_group_support
        self.tagging_support = tagging_support
        self.inherit_tags = inherit_tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SupportedConfigs':
        """Initialize a SupportedConfigs object from a json dictionary."""
        args = {}
        if (resource_kind := _dict.get('resource_kind')) is not None:
            args['resource_kind'] = resource_kind
        if (additional_target_attributes := _dict.get('additional_target_attributes')) is not None:
            args['additional_target_attributes'] = [AdditionalTargetAttribute.from_dict(v) for v in additional_target_attributes]
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [RuleProperty.from_dict(v) for v in properties]
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (cip_requires_service_instance := _dict.get('cip_requires_service_instance')) is not None:
            args['cip_requires_service_instance'] = cip_requires_service_instance
        if (resource_group_support := _dict.get('resource_group_support')) is not None:
            args['resource_group_support'] = resource_group_support
        if (tagging_support := _dict.get('tagging_support')) is not None:
            args['tagging_support'] = tagging_support
        if (inherit_tags := _dict.get('inherit_tags')) is not None:
            args['inherit_tags'] = inherit_tags
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SupportedConfigs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'cip_requires_service_instance') and self.cip_requires_service_instance is not None:
            _dict['cip_requires_service_instance'] = self.cip_requires_service_instance
        if hasattr(self, 'resource_group_support') and self.resource_group_support is not None:
            _dict['resource_group_support'] = self.resource_group_support
        if hasattr(self, 'tagging_support') and self.tagging_support is not None:
            _dict['tagging_support'] = self.tagging_support
        if hasattr(self, 'inherit_tags') and self.inherit_tags is not None:
            _dict['inherit_tags'] = self.inherit_tags
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SupportedConfigs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SupportedConfigs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SupportedConfigs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Tags:
    """
    The collection of different types of tags.

    :param List[str] user: (optional) The collection of user tags.
    :param List[str] access: (optional) The collection of access tags.
    :param List[str] service: (optional) The collection of service tags.
    """

    def __init__(
        self,
        *,
        user: Optional[List[str]] = None,
        access: Optional[List[str]] = None,
        service: Optional[List[str]] = None,
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
        if (user := _dict.get('user')) is not None:
            args['user'] = user
        if (access := _dict.get('access')) is not None:
            args['access'] = access
        if (service := _dict.get('service')) is not None:
            args['service'] = service
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
    The details of the target account.

    :param str id: The UUID of the target.
    :param str account_id: The target account ID.
    :param str trusted_profile_id: The trusted profile ID.
    :param str name: The target name.
    :param List[CredentialResponse] credentials: List of credentials.
    :param str created_by: (optional) The user ID who created the target.
    :param datetime created_on: (optional) The time when the target was created.
    :param str updated_by: (optional) The user ID who updated the target.
    :param datetime updated_on: (optional) The time when the target was updated.
    """

    def __init__(
        self,
        id: str,
        account_id: str,
        trusted_profile_id: str,
        name: str,
        credentials: List['CredentialResponse'],
        *,
        created_by: Optional[str] = None,
        created_on: Optional[datetime] = None,
        updated_by: Optional[str] = None,
        updated_on: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Target object.

        :param str id: The UUID of the target.
        :param str account_id: The target account ID.
        :param str trusted_profile_id: The trusted profile ID.
        :param str name: The target name.
        :param List[CredentialResponse] credentials: List of credentials.
        :param str created_by: (optional) The user ID who created the target.
        :param datetime created_on: (optional) The time when the target was
               created.
        :param str updated_by: (optional) The user ID who updated the target.
        :param datetime updated_on: (optional) The time when the target was
               updated.
        """
        self.id = id
        self.account_id = account_id
        self.trusted_profile_id = trusted_profile_id
        self.name = name
        self.credentials = credentials
        self.created_by = created_by
        self.created_on = created_on
        self.updated_by = updated_by
        self.updated_on = updated_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Target':
        """Initialize a Target object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Target JSON')
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        else:
            raise ValueError('Required property \'account_id\' not present in Target JSON')
        if (trusted_profile_id := _dict.get('trusted_profile_id')) is not None:
            args['trusted_profile_id'] = trusted_profile_id
        else:
            raise ValueError('Required property \'trusted_profile_id\' not present in Target JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Target JSON')
        if (credentials := _dict.get('credentials')) is not None:
            args['credentials'] = [CredentialResponse.from_dict(v) for v in credentials]
        else:
            raise ValueError('Required property \'credentials\' not present in Target JSON')
        if (created_by := _dict.get('created_by')) is not None:
            args['created_by'] = created_by
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = string_to_datetime(created_on)
        if (updated_by := _dict.get('updated_by')) is not None:
            args['updated_by'] = updated_by
        if (updated_on := _dict.get('updated_on')) is not None:
            args['updated_on'] = string_to_datetime(updated_on)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Target object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'trusted_profile_id') and self.trusted_profile_id is not None:
            _dict['trusted_profile_id'] = self.trusted_profile_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'credentials') and self.credentials is not None:
            credentials_list = []
            for v in self.credentials:
                if isinstance(v, dict):
                    credentials_list.append(v)
                else:
                    credentials_list.append(v.to_dict())
            _dict['credentials'] = credentials_list
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'updated_by') and self.updated_by is not None:
            _dict['updated_by'] = self.updated_by
        if hasattr(self, 'updated_on') and self.updated_on is not None:
            _dict['updated_on'] = datetime_to_string(self.updated_on)
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


class TargetCollection:
    """
    The target list collection.

    :param int limit: The requested page limit.
    :param int total_count: The total number of resources that are in the
          collection.
    :param PageHRefFirst first: (optional) A page reference.
    :param PageHRefNext next: (optional) A page reference.
    :param List[Target] targets: The details of the target account.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        targets: List['Target'],
        *,
        first: Optional['PageHRefFirst'] = None,
        next: Optional['PageHRefNext'] = None,
    ) -> None:
        """
        Initialize a TargetCollection object.

        :param int limit: The requested page limit.
        :param int total_count: The total number of resources that are in the
               collection.
        :param List[Target] targets: The details of the target account.
        :param PageHRefFirst first: (optional) A page reference.
        :param PageHRefNext next: (optional) A page reference.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetCollection':
        """Initialize a TargetCollection object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in TargetCollection JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
        else:
            raise ValueError('Required property \'total_count\' not present in TargetCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = PageHRefFirst.from_dict(first)
        if (next := _dict.get('next')) is not None:
            args['next'] = PageHRefNext.from_dict(next)
        if (targets := _dict.get('targets')) is not None:
            args['targets'] = [Target.from_dict(v) for v in targets]
        else:
            raise ValueError('Required property \'targets\' not present in TargetCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetCollection object from a json dictionary."""
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
        if hasattr(self, 'targets') and self.targets is not None:
            targets_list = []
            for v in self.targets:
                if isinstance(v, dict):
                    targets_list.append(v)
                else:
                    targets_list.append(v.to_dict())
            _dict['targets'] = targets_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetInfo:
    """
    The evaluation target.

    :param str id: (optional) The target ID.
    :param str account_id: (optional) The target account ID.
    :param str service_name: (optional) The target service name.
    :param str service_display_name: (optional) The target service display name.
    :param str resource_crn: (optional) The target resource CRN.
    :param str resource_name: (optional) The target resource name.
    :param Tags tags: (optional) The collection of different types of tags.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        account_id: Optional[str] = None,
        service_name: Optional[str] = None,
        service_display_name: Optional[str] = None,
        resource_crn: Optional[str] = None,
        resource_name: Optional[str] = None,
        tags: Optional['Tags'] = None,
    ) -> None:
        """
        Initialize a TargetInfo object.

        :param str id: (optional) The target ID.
        :param str account_id: (optional) The target account ID.
        :param str service_name: (optional) The target service name.
        :param str service_display_name: (optional) The target service display
               name.
        :param str resource_crn: (optional) The target resource CRN.
        :param str resource_name: (optional) The target resource name.
        :param Tags tags: (optional) The collection of different types of tags.
        """
        self.id = id
        self.account_id = account_id
        self.service_name = service_name
        self.service_display_name = service_display_name
        self.resource_crn = resource_crn
        self.resource_name = resource_name
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetInfo':
        """Initialize a TargetInfo object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (account_id := _dict.get('account_id')) is not None:
            args['account_id'] = account_id
        if (service_name := _dict.get('service_name')) is not None:
            args['service_name'] = service_name
        if (service_display_name := _dict.get('service_display_name')) is not None:
            args['service_display_name'] = service_display_name
        if (resource_crn := _dict.get('resource_crn')) is not None:
            args['resource_crn'] = resource_crn
        if (resource_name := _dict.get('resource_name')) is not None:
            args['resource_name'] = resource_name
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = Tags.from_dict(tags)
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
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'service_display_name') and self.service_display_name is not None:
            _dict['service_display_name'] = self.service_display_name
        if hasattr(self, 'resource_crn') and self.resource_crn is not None:
            _dict['resource_crn'] = self.resource_crn
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
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

    :param bool success: The indication of whether the event was received by Event
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
        if (success := _dict.get('success')) is not None:
            args['success'] = success
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


class ConditionItemConditionBase(ConditionItem):
    """
    The required configuration base object.

    :param str description: (optional) The required config description.
    :param str property: The property.
    :param str operator: The operator.
    :param object value: (optional)
    """

    def __init__(
        self,
        property: str,
        operator: str,
        *,
        description: Optional[str] = None,
        value: Optional[object] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionBase object.

        :param str property: The property.
        :param str operator: The operator.
        :param str description: (optional) The required config description.
        :param object value: (optional)
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionBase':
        """Initialize a ConditionItemConditionBase object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (property := _dict.get('property')) is not None:
            args['property'] = property
        else:
            raise ValueError('Required property \'property\' not present in ConditionItemConditionBase JSON')
        if (operator := _dict.get('operator')) is not None:
            args['operator'] = operator
        else:
            raise ValueError('Required property \'operator\' not present in ConditionItemConditionBase JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionBase object from a json dictionary."""
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
        """Return a `str` version of this ConditionItemConditionBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionBase') -> bool:
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



class ConditionItemConditionList(ConditionItem):
    """
    A list of required configurations.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ConditionItemConditionList object.

        """
        # pylint: disable=super-init-not-called
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['ConditionItemConditionListConditionListConditionOr', 'ConditionItemConditionListConditionListConditionAnd'])
        )
        raise Exception(msg)


class ConditionItemConditionSubRule(ConditionItem):
    """
    ConditionItemConditionSubRule.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ConditionItemConditionSubRule object.

        """
        # pylint: disable=super-init-not-called
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['ConditionItemConditionSubRuleConditionSubRuleConditionAny', 'ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf', 'ConditionItemConditionSubRuleConditionSubRuleConditionAll', 'ConditionItemConditionSubRuleConditionSubRuleConditionAllIf'])
        )
        raise Exception(msg)


class RequiredConfigConditionBase(RequiredConfig):
    """
    The required configuration base object.

    :param str description: (optional) The required config description.
    :param str property: The property.
    :param str operator: The operator.
    :param object value: (optional)
    """

    def __init__(
        self,
        property: str,
        operator: str,
        *,
        description: Optional[str] = None,
        value: Optional[object] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionBase object.

        :param str property: The property.
        :param str operator: The operator.
        :param str description: (optional) The required config description.
        :param object value: (optional)
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.property = property
        self.operator = operator
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionBase':
        """Initialize a RequiredConfigConditionBase object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (property := _dict.get('property')) is not None:
            args['property'] = property
        else:
            raise ValueError('Required property \'property\' not present in RequiredConfigConditionBase JSON')
        if (operator := _dict.get('operator')) is not None:
            args['operator'] = operator
        else:
            raise ValueError('Required property \'operator\' not present in RequiredConfigConditionBase JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionBase object from a json dictionary."""
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
        """Return a `str` version of this RequiredConfigConditionBase object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionBase') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionBase') -> bool:
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



class RequiredConfigConditionList(RequiredConfig):
    """
    A list of required configurations.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a RequiredConfigConditionList object.

        """
        # pylint: disable=super-init-not-called
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['RequiredConfigConditionListConditionListConditionOr', 'RequiredConfigConditionListConditionListConditionAnd'])
        )
        raise Exception(msg)


class RequiredConfigConditionSubRule(RequiredConfig):
    """
    RequiredConfigConditionSubRule.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a RequiredConfigConditionSubRule object.

        """
        # pylint: disable=super-init-not-called
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['RequiredConfigConditionSubRuleConditionSubRuleConditionAny', 'RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf', 'RequiredConfigConditionSubRuleConditionSubRuleConditionAll', 'RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf'])
        )
        raise Exception(msg)


class ScopePropertyExclusions(ScopeProperty):
    """
    Any exclusions or resources that should not be part of the scope. Has to be the same
    type as the one specified.

    :param str name: The key that denotes the user is declaring the exclusions.
    :param List[ScopePropertyExclusionItem] value:
    """

    def __init__(
        self,
        name: str,
        value: List['ScopePropertyExclusionItem'],
    ) -> None:
        """
        Initialize a ScopePropertyExclusions object.

        :param str name: The key that denotes the user is declaring the exclusions.
        :param List[ScopePropertyExclusionItem] value:
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopePropertyExclusions':
        """Initialize a ScopePropertyExclusions object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ScopePropertyExclusions JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = [ScopePropertyExclusionItem.from_dict(v) for v in value]
        else:
            raise ValueError('Required property \'value\' not present in ScopePropertyExclusions JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopePropertyExclusions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            value_list = []
            for v in self.value:
                if isinstance(v, dict):
                    value_list.append(v)
                else:
                    value_list.append(v.to_dict())
            _dict['value'] = value_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ScopePropertyExclusions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopePropertyExclusions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopePropertyExclusions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        The key that denotes the user is declaring the exclusions.
        """

        EXCLUSIONS = 'exclusions'



class ScopePropertyScopeId(ScopeProperty):
    """
    The value of the identifier that correlates to scope type. If ScopePropertyScopeType
    schema uses the value enterprise.account_group, the value should be the identifier or
    ID of the account_group within the enterprise.

    :param str name: The key for the scope property.
    :param str value: (optional) The identifier for the scope_type specified.
    """

    def __init__(
        self,
        name: str,
        *,
        value: Optional[str] = None,
    ) -> None:
        """
        Initialize a ScopePropertyScopeId object.

        :param str name: The key for the scope property.
        :param str value: (optional) The identifier for the scope_type specified.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopePropertyScopeId':
        """Initialize a ScopePropertyScopeId object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ScopePropertyScopeId JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopePropertyScopeId object from a json dictionary."""
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
        """Return a `str` version of this ScopePropertyScopeId object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopePropertyScopeId') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopePropertyScopeId') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        The key for the scope property.
        """

        SCOPE_ID = 'scope_id'



class ScopePropertyScopeType(ScopeProperty):
    """
    Attribute that details what kind of type of scope.

    :param str name: key to say the attribute targets the scope type.
    :param str value: The type of scope it targets
          The scope values are as followed:
          - enterprise: The scope targets an enterprise account
          - enterprise.account_group: The scope targets an account group within an
          enterprise
          - enterprise.account: The scope targets an account within an enterprise
          - account: The scope targets an account not tied to an enterprise
          - account.resource_group: The scope targets a resource group within an account.
    """

    def __init__(
        self,
        name: str,
        value: str,
    ) -> None:
        """
        Initialize a ScopePropertyScopeType object.

        :param str name: key to say the attribute targets the scope type.
        :param str value: The type of scope it targets
               The scope values are as followed:
               - enterprise: The scope targets an enterprise account
               - enterprise.account_group: The scope targets an account group within an
               enterprise
               - enterprise.account: The scope targets an account within an enterprise
               - account: The scope targets an account not tied to an enterprise
               - account.resource_group: The scope targets a resource group within an
               account.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScopePropertyScopeType':
        """Initialize a ScopePropertyScopeType object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ScopePropertyScopeType JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError('Required property \'value\' not present in ScopePropertyScopeType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScopePropertyScopeType object from a json dictionary."""
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
        """Return a `str` version of this ScopePropertyScopeType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScopePropertyScopeType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScopePropertyScopeType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        key to say the attribute targets the scope type.
        """

        SCOPE_TYPE = 'scope_type'


    class ValueEnum(str, Enum):
        """
        The type of scope it targets
        The scope values are as followed:
        - enterprise: The scope targets an enterprise account
        - enterprise.account_group: The scope targets an account group within an
        enterprise
        - enterprise.account: The scope targets an account within an enterprise
        - account: The scope targets an account not tied to an enterprise
        - account.resource_group: The scope targets a resource group within an account.
        """

        ACCOUNT = 'account'
        ACCOUNT_RESOURCE_GROUP = 'account.resource_group'
        ENTERPRISE = 'enterprise'
        ENTERPRISE_ACCOUNT_GROUP = 'enterprise.account_group'
        ENTERPRISE_ACCOUNT = 'enterprise.account'



class ConditionItemConditionListConditionListConditionAnd(ConditionItemConditionList):
    """
    ConditionItemConditionListConditionListConditionAnd.

    :param str description: (optional) The required config description.
    :param List[ConditionItem] and_: (optional) A list of required configurations
          where all items should evaluate to true.
    """

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        and_: Optional[List['ConditionItem']] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionListConditionListConditionAnd object.

        :param str description: (optional) The required config description.
        :param List[ConditionItem] and_: (optional) A list of required
               configurations where all items should evaluate to true.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.and_ = and_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionListConditionListConditionAnd':
        """Initialize a ConditionItemConditionListConditionListConditionAnd object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (and_ := _dict.get('and')) is not None:
            args['and_'] = and_
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionListConditionListConditionAnd object from a json dictionary."""
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
        """Return a `str` version of this ConditionItemConditionListConditionListConditionAnd object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionListConditionListConditionAnd') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionListConditionListConditionAnd') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConditionItemConditionListConditionListConditionOr(ConditionItemConditionList):
    """
    The `OR` required configurations.

    :param str description: (optional) The required config description.
    :param List[ConditionItem] or_: (optional) A list of required configurations
          where one item should evaluate to true.
    """

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        or_: Optional[List['ConditionItem']] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionListConditionListConditionOr object.

        :param str description: (optional) The required config description.
        :param List[ConditionItem] or_: (optional) A list of required
               configurations where one item should evaluate to true.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.or_ = or_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionListConditionListConditionOr':
        """Initialize a ConditionItemConditionListConditionListConditionOr object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (or_ := _dict.get('or')) is not None:
            args['or_'] = or_
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionListConditionListConditionOr object from a json dictionary."""
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
        """Return a `str` version of this ConditionItemConditionListConditionListConditionOr object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionListConditionListConditionOr') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionListConditionListConditionOr') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConditionItemConditionSubRuleConditionSubRuleConditionAll(ConditionItemConditionSubRule):
    """
    A subrule using the 'all' operator.

    :param SubRule all: (optional) A rule within a rule used in the requiredConfig.
    """

    def __init__(
        self,
        *,
        all: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAll object.

        :param SubRule all: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.all = all

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionSubRuleConditionSubRuleConditionAll':
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAll object from a json dictionary."""
        args = {}
        if (all := _dict.get('all')) is not None:
            args['all'] = SubRule.from_dict(all)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAll object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'all') and self.all is not None:
            if isinstance(self.all, dict):
                _dict['all'] = self.all
            else:
                _dict['all'] = self.all.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConditionItemConditionSubRuleConditionSubRuleConditionAll object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAll') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAll') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConditionItemConditionSubRuleConditionSubRuleConditionAllIf(ConditionItemConditionSubRule):
    """
    A subrule using the 'all_ifexists' operator.

    :param SubRule all_ifexists: (optional) A rule within a rule used in the
          requiredConfig.
    """

    def __init__(
        self,
        *,
        all_ifexists: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAllIf object.

        :param SubRule all_ifexists: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.all_ifexists = all_ifexists

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionSubRuleConditionSubRuleConditionAllIf':
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAllIf object from a json dictionary."""
        args = {}
        if (all_ifexists := _dict.get('all_ifexists')) is not None:
            args['all_ifexists'] = SubRule.from_dict(all_ifexists)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAllIf object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'all_ifexists') and self.all_ifexists is not None:
            if isinstance(self.all_ifexists, dict):
                _dict['all_ifexists'] = self.all_ifexists
            else:
                _dict['all_ifexists'] = self.all_ifexists.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConditionItemConditionSubRuleConditionSubRuleConditionAllIf object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAllIf') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAllIf') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConditionItemConditionSubRuleConditionSubRuleConditionAny(ConditionItemConditionSubRule):
    """
    A subrule using the 'any' operator.

    :param SubRule any: (optional) A rule within a rule used in the requiredConfig.
    """

    def __init__(
        self,
        *,
        any: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAny object.

        :param SubRule any: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.any = any

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionSubRuleConditionSubRuleConditionAny':
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAny object from a json dictionary."""
        args = {}
        if (any := _dict.get('any')) is not None:
            args['any'] = SubRule.from_dict(any)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAny object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'any') and self.any is not None:
            if isinstance(self.any, dict):
                _dict['any'] = self.any
            else:
                _dict['any'] = self.any.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConditionItemConditionSubRuleConditionSubRuleConditionAny object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAny') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAny') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf(ConditionItemConditionSubRule):
    """
    A subrule using the 'any_ifexists' operator.

    :param SubRule any_ifexists: (optional) A rule within a rule used in the
          requiredConfig.
    """

    def __init__(
        self,
        *,
        any_ifexists: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf object.

        :param SubRule any_ifexists: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.any_ifexists = any_ifexists

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf':
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf object from a json dictionary."""
        args = {}
        if (any_ifexists := _dict.get('any_ifexists')) is not None:
            args['any_ifexists'] = SubRule.from_dict(any_ifexists)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'any_ifexists') and self.any_ifexists is not None:
            if isinstance(self.any_ifexists, dict):
                _dict['any_ifexists'] = self.any_ifexists
            else:
                _dict['any_ifexists'] = self.any_ifexists.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConditionItemConditionSubRuleConditionSubRuleConditionAnyIf') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigConditionListConditionListConditionAnd(RequiredConfigConditionList):
    """
    RequiredConfigConditionListConditionListConditionAnd.

    :param str description: (optional) The required config description.
    :param List[ConditionItem] and_: (optional) A list of required configurations
          where all items should evaluate to true.
    """

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        and_: Optional[List['ConditionItem']] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionListConditionListConditionAnd object.

        :param str description: (optional) The required config description.
        :param List[ConditionItem] and_: (optional) A list of required
               configurations where all items should evaluate to true.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.and_ = and_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionListConditionListConditionAnd':
        """Initialize a RequiredConfigConditionListConditionListConditionAnd object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (and_ := _dict.get('and')) is not None:
            args['and_'] = and_
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionListConditionListConditionAnd object from a json dictionary."""
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
        """Return a `str` version of this RequiredConfigConditionListConditionListConditionAnd object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionListConditionListConditionAnd') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionListConditionListConditionAnd') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigConditionListConditionListConditionOr(RequiredConfigConditionList):
    """
    The `OR` required configurations.

    :param str description: (optional) The required config description.
    :param List[ConditionItem] or_: (optional) A list of required configurations
          where one item should evaluate to true.
    """

    def __init__(
        self,
        *,
        description: Optional[str] = None,
        or_: Optional[List['ConditionItem']] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionListConditionListConditionOr object.

        :param str description: (optional) The required config description.
        :param List[ConditionItem] or_: (optional) A list of required
               configurations where one item should evaluate to true.
        """
        # pylint: disable=super-init-not-called
        self.description = description
        self.or_ = or_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionListConditionListConditionOr':
        """Initialize a RequiredConfigConditionListConditionListConditionOr object from a json dictionary."""
        args = {}
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (or_ := _dict.get('or')) is not None:
            args['or_'] = or_
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionListConditionListConditionOr object from a json dictionary."""
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
        """Return a `str` version of this RequiredConfigConditionListConditionListConditionOr object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionListConditionListConditionOr') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionListConditionListConditionOr') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigConditionSubRuleConditionSubRuleConditionAll(RequiredConfigConditionSubRule):
    """
    A subrule using the 'all' operator.

    :param SubRule all: (optional) A rule within a rule used in the requiredConfig.
    """

    def __init__(
        self,
        *,
        all: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAll object.

        :param SubRule all: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.all = all

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionSubRuleConditionSubRuleConditionAll':
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAll object from a json dictionary."""
        args = {}
        if (all := _dict.get('all')) is not None:
            args['all'] = SubRule.from_dict(all)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAll object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'all') and self.all is not None:
            if isinstance(self.all, dict):
                _dict['all'] = self.all
            else:
                _dict['all'] = self.all.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigConditionSubRuleConditionSubRuleConditionAll object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAll') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAll') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf(RequiredConfigConditionSubRule):
    """
    A subrule using the 'all_ifexists' operator.

    :param SubRule all_ifexists: (optional) A rule within a rule used in the
          requiredConfig.
    """

    def __init__(
        self,
        *,
        all_ifexists: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf object.

        :param SubRule all_ifexists: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.all_ifexists = all_ifexists

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf':
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf object from a json dictionary."""
        args = {}
        if (all_ifexists := _dict.get('all_ifexists')) is not None:
            args['all_ifexists'] = SubRule.from_dict(all_ifexists)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'all_ifexists') and self.all_ifexists is not None:
            if isinstance(self.all_ifexists, dict):
                _dict['all_ifexists'] = self.all_ifexists
            else:
                _dict['all_ifexists'] = self.all_ifexists.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAllIf') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigConditionSubRuleConditionSubRuleConditionAny(RequiredConfigConditionSubRule):
    """
    A subrule using the 'any' operator.

    :param SubRule any: (optional) A rule within a rule used in the requiredConfig.
    """

    def __init__(
        self,
        *,
        any: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAny object.

        :param SubRule any: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.any = any

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionSubRuleConditionSubRuleConditionAny':
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAny object from a json dictionary."""
        args = {}
        if (any := _dict.get('any')) is not None:
            args['any'] = SubRule.from_dict(any)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAny object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'any') and self.any is not None:
            if isinstance(self.any, dict):
                _dict['any'] = self.any
            else:
                _dict['any'] = self.any.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigConditionSubRuleConditionSubRuleConditionAny object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAny') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAny') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf(RequiredConfigConditionSubRule):
    """
    A subrule using the 'any_ifexists' operator.

    :param SubRule any_ifexists: (optional) A rule within a rule used in the
          requiredConfig.
    """

    def __init__(
        self,
        *,
        any_ifexists: Optional['SubRule'] = None,
    ) -> None:
        """
        Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf object.

        :param SubRule any_ifexists: (optional) A rule within a rule used in the
               requiredConfig.
        """
        # pylint: disable=super-init-not-called
        self.any_ifexists = any_ifexists

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf':
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf object from a json dictionary."""
        args = {}
        if (any_ifexists := _dict.get('any_ifexists')) is not None:
            args['any_ifexists'] = SubRule.from_dict(any_ifexists)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'any_ifexists') and self.any_ifexists is not None:
            if isinstance(self.any_ifexists, dict):
                _dict['any_ifexists'] = self.any_ifexists
            else:
                _dict['any_ifexists'] = self.any_ifexists.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequiredConfigConditionSubRuleConditionSubRuleConditionAnyIf') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

##############################################################################
# Pagers
##############################################################################


class InstanceAttachmentsPager:
    """
    InstanceAttachmentsPager can be used to simplify the use of the "list_instance_attachments" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        instance_id: str,
        account_id: str = None,
        version_group_label: str = None,
        limit: int = None,
        sort: str = None,
        direction: str = None,
    ) -> None:
        """
        Initialize a InstanceAttachmentsPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str account_id: (optional) The user account ID.
        :param str version_group_label: (optional) The profile version group label.
        :param int limit: (optional) The number of items that are retrieved in a
               collection.
        :param str sort: (optional) The sorted collection of attachments. The
               available values are `created_on` and `scope_type`.
        :param str direction: (optional) The collection of attachments that is
               sorted in ascending order. To sort the collection in descending order, use
               the `DESC` schema.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._instance_id = instance_id
        self._account_id = account_id
        self._version_group_label = version_group_label
        self._limit = limit
        self._sort = sort
        self._direction = direction

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ProfileAttachment.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_instance_attachments(
            instance_id=self._instance_id,
            account_id=self._account_id,
            version_group_label=self._version_group_label,
            limit=self._limit,
            sort=self._sort,
            direction=self._direction,
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
        :return: A List[dict], where each element is a dict that represents an instance of ProfileAttachment.
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
        instance_id: str,
        attachment_id: str = None,
        group_id: str = None,
        profile_id: str = None,
        type: str = None,
        limit: int = None,
        sort: str = None,
    ) -> None:
        """
        Initialize a ReportsPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
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
        self._instance_id = instance_id
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
            instance_id=self._instance_id,
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
            next = next_page_link.get('start')
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
        instance_id: str,
        report_id: str,
        assessment_id: str = None,
        assessment_method: str = None,
        component_id: str = None,
        target_id: str = None,
        target_env: str = None,
        target_name: str = None,
        status: str = None,
        limit: int = None,
        sort: str = None,
        scope_id: str = None,
        subscope_id: str = None,
    ) -> None:
        """
        Initialize a ReportEvaluationsPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str assessment_id: (optional) The ID of the assessment.
        :param str assessment_method: (optional) The assessment method.
        :param str component_id: (optional) The ID of component.
        :param str target_id: (optional) The ID of the evaluation target.
        :param str target_env: (optional) The environment of the evaluation target.
        :param str target_name: (optional) The name of the evaluation target.
        :param str status: (optional) The evaluation status value.
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param str sort: (optional) This field sorts results by using a valid sort
               field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._instance_id = instance_id
        self._report_id = report_id
        self._assessment_id = assessment_id
        self._assessment_method = assessment_method
        self._component_id = component_id
        self._target_id = target_id
        self._target_env = target_env
        self._target_name = target_name
        self._status = status
        self._limit = limit
        self._sort = sort
        self._scope_id = scope_id
        self._subscope_id = subscope_id

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
            instance_id=self._instance_id,
            report_id=self._report_id,
            assessment_id=self._assessment_id,
            assessment_method=self._assessment_method,
            component_id=self._component_id,
            target_id=self._target_id,
            target_env=self._target_env,
            target_name=self._target_name,
            status=self._status,
            limit=self._limit,
            sort=self._sort,
            scope_id=self._scope_id,
            subscope_id=self._subscope_id,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
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
        instance_id: str,
        report_id: str,
        id: str = None,
        resource_name: str = None,
        account_id: str = None,
        component_id: str = None,
        status: str = None,
        sort: str = None,
        limit: int = None,
        scope_id: str = None,
        subscope_id: str = None,
    ) -> None:
        """
        Initialize a ReportResourcesPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str report_id: The ID of the scan that is associated with a report.
        :param str id: (optional) The ID of the resource.
        :param str resource_name: (optional) The name of the resource.
        :param str account_id: (optional) The user account ID.
        :param str component_id: (optional) The ID of component.
        :param str status: (optional) The compliance status value.
        :param str sort: (optional) This field sorts resources by using a valid
               sort field. To learn more, see
               [Sorting](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-sorting).
        :param int limit: (optional) The indication of many resources to return,
               unless the response is  the last page of resources.
        :param str scope_id: (optional) The ID of the scope.
        :param str subscope_id: (optional) The ID of the subscope.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._instance_id = instance_id
        self._report_id = report_id
        self._id = id
        self._resource_name = resource_name
        self._account_id = account_id
        self._component_id = component_id
        self._status = status
        self._sort = sort
        self._limit = limit
        self._scope_id = scope_id
        self._subscope_id = subscope_id

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
            instance_id=self._instance_id,
            report_id=self._report_id,
            id=self._id,
            resource_name=self._resource_name,
            account_id=self._account_id,
            component_id=self._component_id,
            status=self._status,
            sort=self._sort,
            limit=self._limit,
            scope_id=self._scope_id,
            subscope_id=self._subscope_id,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
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


class RulesPager:
    """
    RulesPager can be used to simplify the use of the "list_rules" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        instance_id: str,
        limit: int = None,
        type: str = None,
        search: str = None,
        service_name: str = None,
        sort: str = None,
    ) -> None:
        """
        Initialize a RulesPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str type: (optional) The list of only user-defined, or
               system-defined rules.
        :param str search: (optional) The indication of whether to search for rules
               with a specific string string in the name, description, or labels.
        :param str service_name: (optional) Searches for rules targeting
               corresponding service.
        :param str sort: (optional) Field used to sort rules. Rules can be sorted
               in ascending or descending order.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._instance_id = instance_id
        self._limit = limit
        self._type = type
        self._search = search
        self._service_name = service_name
        self._sort = sort

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Rule.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_rules(
            instance_id=self._instance_id,
            limit=self._limit,
            type=self._type,
            search=self._search,
            service_name=self._service_name,
            sort=self._sort,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('rules')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Rule.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class ScopesPager:
    """
    ScopesPager can be used to simplify the use of the "list_scopes" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        instance_id: str,
        limit: int = None,
        name: str = None,
        description: str = None,
        environment: str = None,
    ) -> None:
        """
        Initialize a ScopesPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str name: (optional) determine name of scope returned in response.
        :param str description: (optional) determine descriptions of scope returned
               in response.
        :param str environment: (optional) determine environment of scopes returned
               in response.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._instance_id = instance_id
        self._limit = limit
        self._name = name
        self._description = description
        self._environment = environment

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of Scope.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_scopes(
            instance_id=self._instance_id,
            limit=self._limit,
            name=self._name,
            description=self._description,
            environment=self._environment,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('scopes')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of Scope.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results


class SubscopesPager:
    """
    SubscopesPager can be used to simplify the use of the "list_subscopes" method.
    """

    def __init__(
        self,
        *,
        client: SecurityAndComplianceCenterApiV3,
        instance_id: str,
        scope_id: str,
        limit: int = None,
        name: str = None,
        description: str = None,
        environment: str = None,
    ) -> None:
        """
        Initialize a SubscopesPager object.
        :param str instance_id: The ID of the Security and Compliance Center
               instance.
        :param str scope_id: The ID of the scope being targeted.
        :param int limit: (optional) The indication of how many resources to
               return, unless the response is the last page of resources.
        :param str name: (optional) determine name of subscope returned in
               response.
        :param str description: (optional) determine descriptions of subscopes
               returned in response.
        :param str environment: (optional) determine environment of subscopes
               returned in response.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._instance_id = instance_id
        self._scope_id = scope_id
        self._limit = limit
        self._name = name
        self._description = description
        self._environment = environment

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of SubScope.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_subscopes(
            instance_id=self._instance_id,
            scope_id=self._scope_id,
            limit=self._limit,
            name=self._name,
            description=self._description,
            environment=self._environment,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('subscopes')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of SubScope.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
