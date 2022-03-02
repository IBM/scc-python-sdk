# coding: utf-8

# (C) Copyright IBM Corp. 2022.
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

# IBM OpenAPI SDK Code Generator Version: 3.46.0-a4e29da0-20220224-210428
 
"""
The Addon Manager API

API Version: 1.0.0
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

class AddonMgrV1(BaseService):
    """The AddonMgr V1 service."""

    DEFAULT_SERVICE_URL = 'https://us-south.secadvisor.cloud.ibm.com/addonmgr'
    DEFAULT_SERVICE_NAME = 'addon_mgr'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://us-south.secadvisor.cloud.ibm.com/addonmgr',
        'us-east': 'https://us-south.secadvisor.cloud.ibm.com/addonmgr',
        'eu-gb': 'https://eu-gb.secadvisor.cloud.ibm.com/addonmgr',
        'eu-de': 'https://eu.compliance.cloud.ibm.com/si/addonmgr',
    }

    @classmethod
    def new_instance(cls,
                     account_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'AddonMgrV1':
        """
        Return a new client for the AddonMgr service using the specified parameters
               and external configuration.

        :param str account_id: Account ID.
        """
        if account_id is None:
            raise ValueError('account_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            account_id,
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

    def __init__(self,
                 account_id: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the AddonMgr service.

        :param str account_id: Account ID.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if account_id is None:
            raise ValueError('account_id must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.account_id = account_id


    #########################
    # addonManagerCos
    #########################


    def add_network_insights_cos_details_v2(self,
        region_id: str,
        cos_details: List['CosDetailsV2CosDetailsItem'],
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add cos details.

        Addcos details.

        :param str region_id: Region for example - us-south, eu-gb.
        :param List[CosDetailsV2CosDetailsItem] cos_details:
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if region_id is None:
            raise ValueError('region_id must be provided')
        if cos_details is None:
            raise ValueError('cos_details must be provided')
        cos_details = [convert_model(x) for x in cos_details]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_network_insights_cos_details_v2')
        headers.update(sdk_headers)

        data = {
            'region_id': region_id,
            'cos_details': cos_details
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/network-insights/cos'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_network_insights_cos_details_v2(self,
        *,
        ids: List[str] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete cos details.

        Delete NA cos details.

        :param List[str] ids: (optional) Array of Ids of COS entries.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_network_insights_cos_details_v2')
        headers.update(sdk_headers)

        data = {
            'ids': ids
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/network-insights/cos'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def add_activity_insights_cos_details_v2(self,
        region_id: str,
        cos_details: List['CosDetailsV2CosDetailsItem'],
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add cos details.

        Addcos details.

        :param str region_id: Region for example - us-south, eu-gb.
        :param List[CosDetailsV2CosDetailsItem] cos_details:
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if region_id is None:
            raise ValueError('region_id must be provided')
        if cos_details is None:
            raise ValueError('cos_details must be provided')
        cos_details = [convert_model(x) for x in cos_details]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_activity_insights_cos_details_v2')
        headers.update(sdk_headers)

        data = {
            'region_id': region_id,
            'cos_details': cos_details
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/activity-insights/cos'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_activity_insights_cos_details_v2(self,
        *,
        ids: List[str] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete cos details.

        Delete AT cos details.

        :param List[str] ids: (optional) Array of Ids of COS entries.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_activity_insights_cos_details_v2')
        headers.update(sdk_headers)

        data = {
            'ids': ids
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/activity-insights/cos'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # addonManagerDisable
    #########################


    def disable_insights_v2(self,
        region_id: str,
        *,
        network_insights: bool = None,
        activity_insights: bool = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Disable add-on.

        Disable add-on.

        :param str region_id: Region id for example - us.
        :param bool network_insights: (optional)
        :param bool activity_insights: (optional)
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if region_id is None:
            raise ValueError('region_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='disable_insights_v2')
        headers.update(sdk_headers)

        data = {
            'region_id': region_id,
            'network-insights': network_insights,
            'activity-insights': activity_insights
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/disable'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # addonManagerEnable
    #########################


    def enable_insights_v2(self,
        region_id: str,
        *,
        network_insights: bool = None,
        activity_insights: bool = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Enable add-on.

        Enable add-on.

        :param str region_id: Region id for example - us.
        :param bool network_insights: (optional)
        :param bool activity_insights: (optional)
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if region_id is None:
            raise ValueError('region_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='enable_insights_v2')
        headers.update(sdk_headers)

        data = {
            'region_id': region_id,
            'network-insights': network_insights,
            'activity-insights': activity_insights
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/enable'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # addonManagerInsights
    #########################


    def get_supported_insights_v2(self,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Fetch supported insights.

        Retrieve insights details.

        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AllInsights` object
        """

        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_supported_insights_v2')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/insights'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # addonManagerTestFindings
    #########################


    def test_ai_findings_v2(self,
        region_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        test findings for activity-insights.

        Test findings for activity-insights.

        :param str region_id: Region for example - us-south, eu-gb.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if region_id is None:
            raise ValueError('region_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='test_ai_findings_v2')
        headers.update(sdk_headers)

        data = {
            'region_id': region_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/addons/{account_id}/activity-insights/test-ai-findings'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AllInsights():
    """
    AllInsights.

    :attr List[str] type: (optional)
    """

    def __init__(self,
                 *,
                 type: List[str] = None) -> None:
        """
        Initialize a AllInsights object.

        :param List[str] type: (optional)
        """
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllInsights':
        """Initialize a AllInsights object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllInsights object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllInsights object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllInsights') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllInsights') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Insights type.
        """
        NETWORK_INSIGHTS = 'network-insights'
        ACTIVITY_INSIGHTS = 'activity-insights'


class CosDetailsV2CosDetailsItem():
    """
    CosDetailsV2CosDetailsItem.

    :attr str cos_instance:
    :attr str bucket_name:
    :attr str description:
    :attr str type: Insights type.
    :attr str cos_bucket_url: cos bucket url.
    """

    def __init__(self,
                 cos_instance: str,
                 bucket_name: str,
                 description: str,
                 type: str,
                 cos_bucket_url: str) -> None:
        """
        Initialize a CosDetailsV2CosDetailsItem object.

        :param str cos_instance:
        :param str bucket_name:
        :param str description:
        :param str type: Insights type.
        :param str cos_bucket_url: cos bucket url.
        """
        self.cos_instance = cos_instance
        self.bucket_name = bucket_name
        self.description = description
        self.type = type
        self.cos_bucket_url = cos_bucket_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CosDetailsV2CosDetailsItem':
        """Initialize a CosDetailsV2CosDetailsItem object from a json dictionary."""
        args = {}
        if 'cos_instance' in _dict:
            args['cos_instance'] = _dict.get('cos_instance')
        else:
            raise ValueError('Required property \'cos_instance\' not present in CosDetailsV2CosDetailsItem JSON')
        if 'bucket_name' in _dict:
            args['bucket_name'] = _dict.get('bucket_name')
        else:
            raise ValueError('Required property \'bucket_name\' not present in CosDetailsV2CosDetailsItem JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in CosDetailsV2CosDetailsItem JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in CosDetailsV2CosDetailsItem JSON')
        if 'cos_bucket_url' in _dict:
            args['cos_bucket_url'] = _dict.get('cos_bucket_url')
        else:
            raise ValueError('Required property \'cos_bucket_url\' not present in CosDetailsV2CosDetailsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CosDetailsV2CosDetailsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cos_instance') and self.cos_instance is not None:
            _dict['cos_instance'] = self.cos_instance
        if hasattr(self, 'bucket_name') and self.bucket_name is not None:
            _dict['bucket_name'] = self.bucket_name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'cos_bucket_url') and self.cos_bucket_url is not None:
            _dict['cos_bucket_url'] = self.cos_bucket_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CosDetailsV2CosDetailsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CosDetailsV2CosDetailsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CosDetailsV2CosDetailsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Insights type.
        """
        NETWORK_INSIGHTS = 'network-insights'
        ACTIVITY_INSIGHTS = 'activity-insights'

