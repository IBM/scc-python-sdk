# coding: utf-8

# (C) Copyright IBM Corp. 2021.
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

# IBM OpenAPI SDK Code Generator Version: 3.30.0-bd714324-20210406-200538
 
"""
notifications-api
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

class NotificationsApiV1(BaseService):
    """The Notifications API V1 service."""

    DEFAULT_SERVICE_URL = 'https://notifications-api.cloud.ibm.com/notifications'
    DEFAULT_SERVICE_NAME = 'notifications_api'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'NotificationsApiV1':
        """
        Return a new client for the Notifications API service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Notifications API service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # notificationChannel
    #########################


    def list_all_channels(self,
        account_id: str,
        *,
        transaction_id: str = None,
        limit: int = None,
        skip: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        list all channels.

        list all channels under this account.

        :param str account_id: Account ID.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param int limit: (optional) Limit the number of the returned documents to
               the specified number.
        :param int skip: (optional) The offset is the index of the item from which
               you want to start returning data from. Default is 0.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListChannelsResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_channels')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'skip': skip
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_notification_channel(self,
        account_id: str,
        name: str,
        type: str,
        endpoint: str,
        *,
        description: str = None,
        severity: List[str] = None,
        enabled: bool = None,
        alert_source: List['NotificationChannelAlertSourceItem'] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        create notification channel.

        create notification channel.

        :param str account_id: Account ID.
        :param str name:
        :param str type: Type of callback URL.
        :param str endpoint: The callback URL which receives the notification.
        :param str description: (optional) A one sentence description of this
               `Channel`.
        :param List[str] severity: (optional) Severity of the notification to be
               received.
        :param bool enabled: (optional) Channel is enabled or not. Default is
               disabled.
        :param List[NotificationChannelAlertSourceItem] alert_source: (optional)
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateChannelsResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if endpoint is None:
            raise ValueError('endpoint must be provided')
        if alert_source is not None:
            alert_source = [convert_model(x) for x in alert_source]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_notification_channel')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'endpoint': endpoint,
            'description': description,
            'severity': severity,
            'enabled': enabled,
            'alert_source': alert_source
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_notification_channels(self,
        account_id: str,
        request_body: List[str],
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        bulk delete of channels.

        bulk delete of channels.

        :param str account_id: Account ID.
        :param List[str] request_body: Body for bulk delete notification channels.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BulkDeleteChannelsResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if request_body is None:
            raise ValueError('request_body must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_notification_channels')
        headers.update(sdk_headers)

        data = json.dumps(request_body)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_notification_channel(self,
        account_id: str,
        channel_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        delete the details of a specific channel.

        delete the details of a specific channel.

        :param str account_id: Account ID.
        :param str channel_id: Channel ID.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteChannelResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if channel_id is None:
            raise ValueError('channel_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_notification_channel')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'channel_id']
        path_param_values = self.encode_path_vars(account_id, channel_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels/{channel_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_notification_channel(self,
        account_id: str,
        channel_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        get the details of a specific channel.

        get the details of a specific channel.

        :param str account_id: Account ID.
        :param str channel_id: Channel ID.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetChannelResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if channel_id is None:
            raise ValueError('channel_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_notification_channel')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'channel_id']
        path_param_values = self.encode_path_vars(account_id, channel_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels/{channel_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_notification_channel(self,
        account_id: str,
        channel_id: str,
        name: str,
        type: str,
        endpoint: str,
        *,
        description: str = None,
        severity: List[str] = None,
        enabled: bool = None,
        alert_source: List['NotificationChannelAlertSourceItem'] = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        update notification channel.

        update notification channel.

        :param str account_id: Account ID.
        :param str channel_id: Channel ID.
        :param str name:
        :param str type: Type of callback URL.
        :param str endpoint: The callback URL which receives the notification.
        :param str description: (optional) A one sentence description of this
               `Channel`.
        :param List[str] severity: (optional) Severity of the notification to be
               received.
        :param bool enabled: (optional) Channel is enabled or not. Default is
               disabled.
        :param List[NotificationChannelAlertSourceItem] alert_source: (optional)
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UpdateChannelResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if channel_id is None:
            raise ValueError('channel_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if endpoint is None:
            raise ValueError('endpoint must be provided')
        if alert_source is not None:
            alert_source = [convert_model(x) for x in alert_source]
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_notification_channel')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'endpoint': endpoint,
            'description': description,
            'severity': severity,
            'enabled': enabled,
            'alert_source': alert_source
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'channel_id']
        path_param_values = self.encode_path_vars(account_id, channel_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels/{channel_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def test_notification_channel(self,
        account_id: str,
        channel_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        test notification channel.

        test a nofication channel under this account.

        :param str account_id: Account ID.
        :param str channel_id: Channel ID.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TestChannelResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        if channel_id is None:
            raise ValueError('channel_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='test_notification_channel')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'channel_id']
        path_param_values = self.encode_path_vars(account_id, channel_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/channels/{channel_id}/test'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_public_key(self,
        account_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        fetch notifications public key.

        fetch public key to decrypt messages in notification payload.

        :param str account_id: Account ID.
        :param str transaction_id: (optional) The transaction id for the request in
               uuid v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PublicKeyResponse` object
        """

        if account_id is None:
            raise ValueError('account_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_public_key')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/notifications/public_key'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ChannelResponseDefinitionAlertSourceItem():
    """
    The alert sources. They identify the providers and their finding types which makes the
    findings available to Security Advisor.

    :attr str provider_name: (optional) Below is a list of builtin providers that
          you can select in addition to the ones you obtain by calling Findings API
          /v1/{account_id}/providers :
           | provider_name | The source they represent |
           |-----|-----|
           | VA  | Vulnerable image findings|
           | NA  | Network Insights findings|
           | ATA | Activity Insights findings|
           | CERT | Certificate Manager findings|
           | ALL | Special provider name to represent all the providers. Its mutually
          exclusive with other providers meaning either you choose ALL or you don't|.
    :attr List[str] finding_types: (optional) An array of the finding types of the
          provider_name or "ALL" to specify all finding types under that provider Below is
          a list of supported finding types for each built in providers
          | provider_name | Supported finding types |
          |-----|-----|
          | VA  | "image_with_vulnerabilities", "image_with_config_issues"|
          | NA  | "anonym_server", "malware_server", "bot_server", "miner_server",
          "server_suspected_ratio", "server_response", "data_extrusion",
          "server_weaponized_total"|
          | ATA | "appid", "cos", "iks", "iam", "kms", "cert", "account", "app"|
          | CERT | "expired_cert", "expiring_1day_cert", "expiring_10day_cert",
          "expiring_30day_cert", "expiring_60day_cert", "expiring_90day_cert"|
          | ALL | "ALL"|.
    """

    def __init__(self,
                 *,
                 provider_name: str = None,
                 finding_types: List[str] = None) -> None:
        """
        Initialize a ChannelResponseDefinitionAlertSourceItem object.

        :param str provider_name: (optional) Below is a list of builtin providers
               that you can select in addition to the ones you obtain by calling Findings
               API /v1/{account_id}/providers :
                | provider_name | The source they represent |
                |-----|-----|
                | VA  | Vulnerable image findings|
                | NA  | Network Insights findings|
                | ATA | Activity Insights findings|
                | CERT | Certificate Manager findings|
                | ALL | Special provider name to represent all the providers. Its mutually
               exclusive with other providers meaning either you choose ALL or you don't|.
        :param List[str] finding_types: (optional) An array of the finding types of
               the provider_name or "ALL" to specify all finding types under that provider
               Below is a list of supported finding types for each built in providers
               | provider_name | Supported finding types |
               |-----|-----|
               | VA  | "image_with_vulnerabilities", "image_with_config_issues"|
               | NA  | "anonym_server", "malware_server", "bot_server", "miner_server",
               "server_suspected_ratio", "server_response", "data_extrusion",
               "server_weaponized_total"|
               | ATA | "appid", "cos", "iks", "iam", "kms", "cert", "account", "app"|
               | CERT | "expired_cert", "expiring_1day_cert", "expiring_10day_cert",
               "expiring_30day_cert", "expiring_60day_cert", "expiring_90day_cert"|
               | ALL | "ALL"|.
        """
        self.provider_name = provider_name
        self.finding_types = finding_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelResponseDefinitionAlertSourceItem':
        """Initialize a ChannelResponseDefinitionAlertSourceItem object from a json dictionary."""
        args = {}
        if 'provider_name' in _dict:
            args['provider_name'] = _dict.get('provider_name')
        if 'finding_types' in _dict:
            args['finding_types'] = _dict.get('finding_types')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChannelResponseDefinitionAlertSourceItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_name') and self.provider_name is not None:
            _dict['provider_name'] = self.provider_name
        if hasattr(self, 'finding_types') and self.finding_types is not None:
            _dict['finding_types'] = self.finding_types
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChannelResponseDefinitionAlertSourceItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChannelResponseDefinitionAlertSourceItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChannelResponseDefinitionAlertSourceItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChannelResponseDefinitionSeverity():
    """
    Severity of the notification.

    :attr bool critical: (optional) Critical Severity.
    :attr bool high: (optional) High Severity.
    :attr bool medium: (optional) Medium Severity.
    :attr bool low: (optional) Low Severity.
    """

    def __init__(self,
                 *,
                 critical: bool = None,
                 high: bool = None,
                 medium: bool = None,
                 low: bool = None) -> None:
        """
        Initialize a ChannelResponseDefinitionSeverity object.

        :param bool critical: (optional) Critical Severity.
        :param bool high: (optional) High Severity.
        :param bool medium: (optional) Medium Severity.
        :param bool low: (optional) Low Severity.
        """
        self.critical = critical
        self.high = high
        self.medium = medium
        self.low = low

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelResponseDefinitionSeverity':
        """Initialize a ChannelResponseDefinitionSeverity object from a json dictionary."""
        args = {}
        if 'critical' in _dict:
            args['critical'] = _dict.get('critical')
        if 'high' in _dict:
            args['high'] = _dict.get('high')
        if 'medium' in _dict:
            args['medium'] = _dict.get('medium')
        if 'low' in _dict:
            args['low'] = _dict.get('low')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChannelResponseDefinitionSeverity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'critical') and self.critical is not None:
            _dict['critical'] = self.critical
        if hasattr(self, 'high') and self.high is not None:
            _dict['high'] = self.high
        if hasattr(self, 'medium') and self.medium is not None:
            _dict['medium'] = self.medium
        if hasattr(self, 'low') and self.low is not None:
            _dict['low'] = self.low
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChannelResponseDefinitionSeverity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChannelResponseDefinitionSeverity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChannelResponseDefinitionSeverity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationChannelAlertSourceItem():
    """
    The alert sources. They identify the providers and their finding types which makes the
    findings available to Security Advisor.

    :attr str provider_name: Below is a list of builtin providers that you can
          select in addition to the ones you obtain by calling Findings API
          /v1/{account_id}/providers :
           | provider_name | The source they represent |
           |-----|-----|
           | VA  | Vulnerable image findings|
           | NA  | Network Insights findings|
           | ATA | Activity Insights findings|
           | CERT | Certificate Manager findings|
           | ALL | Special provider name to represent all the providers. Its mutually
          exclusive with other providers meaning either you choose ALL or you don't|.
    :attr List[str] finding_types: (optional) An array of the finding types of the
          provider_name or "ALL" to specify all finding types under that provider Below is
          a list of supported finding types for each built in providers
          | provider_name | Supported finding types |
          |-----|-----|
          | VA  | "image_with_vulnerabilities", "image_with_config_issues"|
          | NA  | "anonym_server", "malware_server", "bot_server", "miner_server",
          "server_suspected_ratio", "server_response", "data_extrusion",
          "server_weaponized_total"|
          | ATA | "appid", "cos", "iks", "iam", "kms", "cert", "account", "app"|
          | CERT | "expired_cert", "expiring_1day_cert", "expiring_10day_cert",
          "expiring_30day_cert", "expiring_60day_cert", "expiring_90day_cert"|
          | ALL | "ALL"|.
    """

    def __init__(self,
                 provider_name: str,
                 *,
                 finding_types: List[str] = None) -> None:
        """
        Initialize a NotificationChannelAlertSourceItem object.

        :param str provider_name: Below is a list of builtin providers that you can
               select in addition to the ones you obtain by calling Findings API
               /v1/{account_id}/providers :
                | provider_name | The source they represent |
                |-----|-----|
                | VA  | Vulnerable image findings|
                | NA  | Network Insights findings|
                | ATA | Activity Insights findings|
                | CERT | Certificate Manager findings|
                | ALL | Special provider name to represent all the providers. Its mutually
               exclusive with other providers meaning either you choose ALL or you don't|.
        :param List[str] finding_types: (optional) An array of the finding types of
               the provider_name or "ALL" to specify all finding types under that provider
               Below is a list of supported finding types for each built in providers
               | provider_name | Supported finding types |
               |-----|-----|
               | VA  | "image_with_vulnerabilities", "image_with_config_issues"|
               | NA  | "anonym_server", "malware_server", "bot_server", "miner_server",
               "server_suspected_ratio", "server_response", "data_extrusion",
               "server_weaponized_total"|
               | ATA | "appid", "cos", "iks", "iam", "kms", "cert", "account", "app"|
               | CERT | "expired_cert", "expiring_1day_cert", "expiring_10day_cert",
               "expiring_30day_cert", "expiring_60day_cert", "expiring_90day_cert"|
               | ALL | "ALL"|.
        """
        self.provider_name = provider_name
        self.finding_types = finding_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationChannelAlertSourceItem':
        """Initialize a NotificationChannelAlertSourceItem object from a json dictionary."""
        args = {}
        if 'provider_name' in _dict:
            args['provider_name'] = _dict.get('provider_name')
        else:
            raise ValueError('Required property \'provider_name\' not present in NotificationChannelAlertSourceItem JSON')
        if 'finding_types' in _dict:
            args['finding_types'] = _dict.get('finding_types')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationChannelAlertSourceItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_name') and self.provider_name is not None:
            _dict['provider_name'] = self.provider_name
        if hasattr(self, 'finding_types') and self.finding_types is not None:
            _dict['finding_types'] = self.finding_types
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NotificationChannelAlertSourceItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationChannelAlertSourceItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationChannelAlertSourceItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BulkDeleteChannelsResponse():
    """
    Response of all deleted channels.

    :attr str message: (optional) response message.
    """

    def __init__(self,
                 *,
                 message: str = None) -> None:
        """
        Initialize a BulkDeleteChannelsResponse object.

        :param str message: (optional) response message.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkDeleteChannelsResponse':
        """Initialize a BulkDeleteChannelsResponse object from a json dictionary."""
        args = {}
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkDeleteChannelsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkDeleteChannelsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkDeleteChannelsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkDeleteChannelsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChannelResponseDefinition():
    """
    Response including channels.

    :attr str channel_id: (optional) unique id of the channel.
    :attr str name: (optional)
    :attr str description: (optional) A one sentence description of this `Channel`.
    :attr str type: (optional) Type of callback URL.
    :attr ChannelResponseDefinitionSeverity severity: (optional) Severity of the
          notification.
    :attr str endpoint: (optional) The callback URL which receives the notification.
    :attr bool enabled: (optional) Channel is enabled or not. Default is disabled.
    :attr List[ChannelResponseDefinitionAlertSourceItem] alert_source: (optional)
    :attr str frequency: (optional)
    """

    def __init__(self,
                 *,
                 channel_id: str = None,
                 name: str = None,
                 description: str = None,
                 type: str = None,
                 severity: 'ChannelResponseDefinitionSeverity' = None,
                 endpoint: str = None,
                 enabled: bool = None,
                 alert_source: List['ChannelResponseDefinitionAlertSourceItem'] = None,
                 frequency: str = None) -> None:
        """
        Initialize a ChannelResponseDefinition object.

        :param str channel_id: (optional) unique id of the channel.
        :param str name: (optional)
        :param str description: (optional) A one sentence description of this
               `Channel`.
        :param str type: (optional) Type of callback URL.
        :param ChannelResponseDefinitionSeverity severity: (optional) Severity of
               the notification.
        :param str endpoint: (optional) The callback URL which receives the
               notification.
        :param bool enabled: (optional) Channel is enabled or not. Default is
               disabled.
        :param List[ChannelResponseDefinitionAlertSourceItem] alert_source:
               (optional)
        :param str frequency: (optional)
        """
        self.channel_id = channel_id
        self.name = name
        self.description = description
        self.type = type
        self.severity = severity
        self.endpoint = endpoint
        self.enabled = enabled
        self.alert_source = alert_source
        self.frequency = frequency

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelResponseDefinition':
        """Initialize a ChannelResponseDefinition object from a json dictionary."""
        args = {}
        if 'channel_id' in _dict:
            args['channel_id'] = _dict.get('channel_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'severity' in _dict:
            args['severity'] = ChannelResponseDefinitionSeverity.from_dict(_dict.get('severity'))
        if 'endpoint' in _dict:
            args['endpoint'] = _dict.get('endpoint')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'alert_source' in _dict:
            args['alert_source'] = [ChannelResponseDefinitionAlertSourceItem.from_dict(x) for x in _dict.get('alert_source')]
        if 'frequency' in _dict:
            args['frequency'] = _dict.get('frequency')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChannelResponseDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel_id') and self.channel_id is not None:
            _dict['channel_id'] = self.channel_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity.to_dict()
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'alert_source') and self.alert_source is not None:
            _dict['alert_source'] = [x.to_dict() for x in self.alert_source]
        if hasattr(self, 'frequency') and self.frequency is not None:
            _dict['frequency'] = self.frequency
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChannelResponseDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChannelResponseDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChannelResponseDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Type of callback URL.
        """
        WEBHOOK = 'Webhook'


class CreateChannelsResponse():
    """
    Response of created channel.

    :attr str channel_id: (optional) id of the created channel.
    :attr int status_code: (optional) response code.
    """

    def __init__(self,
                 *,
                 channel_id: str = None,
                 status_code: int = None) -> None:
        """
        Initialize a CreateChannelsResponse object.

        :param str channel_id: (optional) id of the created channel.
        :param int status_code: (optional) response code.
        """
        self.channel_id = channel_id
        self.status_code = status_code

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateChannelsResponse':
        """Initialize a CreateChannelsResponse object from a json dictionary."""
        args = {}
        if 'channel_id' in _dict:
            args['channel_id'] = _dict.get('channel_id')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateChannelsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel_id') and self.channel_id is not None:
            _dict['channel_id'] = self.channel_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateChannelsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateChannelsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateChannelsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteChannelResponse():
    """
    Response of deleted channel.

    :attr str channel_id: (optional) id of the created channel.
    :attr str message: (optional) response message.
    """

    def __init__(self,
                 *,
                 channel_id: str = None,
                 message: str = None) -> None:
        """
        Initialize a DeleteChannelResponse object.

        :param str channel_id: (optional) id of the created channel.
        :param str message: (optional) response message.
        """
        self.channel_id = channel_id
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteChannelResponse':
        """Initialize a DeleteChannelResponse object from a json dictionary."""
        args = {}
        if 'channel_id' in _dict:
            args['channel_id'] = _dict.get('channel_id')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteChannelResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel_id') and self.channel_id is not None:
            _dict['channel_id'] = self.channel_id
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteChannelResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteChannelResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteChannelResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetChannelResponse():
    """
    Response of get channel.

    :attr ChannelResponseDefinition channel: (optional) Response including channels.
    """

    def __init__(self,
                 *,
                 channel: 'ChannelResponseDefinition' = None) -> None:
        """
        Initialize a GetChannelResponse object.

        :param ChannelResponseDefinition channel: (optional) Response including
               channels.
        """
        self.channel = channel

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetChannelResponse':
        """Initialize a GetChannelResponse object from a json dictionary."""
        args = {}
        if 'channel' in _dict:
            args['channel'] = ChannelResponseDefinition.from_dict(_dict.get('channel'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetChannelResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel') and self.channel is not None:
            _dict['channel'] = self.channel.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetChannelResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetChannelResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetChannelResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListChannelsResponse():
    """
    Response including channels.

    :attr List[ChannelResponseDefinition] channels: (optional)
    """

    def __init__(self,
                 *,
                 channels: List['ChannelResponseDefinition'] = None) -> None:
        """
        Initialize a ListChannelsResponse object.

        :param List[ChannelResponseDefinition] channels: (optional)
        """
        self.channels = channels

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListChannelsResponse':
        """Initialize a ListChannelsResponse object from a json dictionary."""
        args = {}
        if 'channels' in _dict:
            args['channels'] = [ChannelResponseDefinition.from_dict(x) for x in _dict.get('channels')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListChannelsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channels') and self.channels is not None:
            _dict['channels'] = [x.to_dict() for x in self.channels]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListChannelsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListChannelsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListChannelsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PublicKeyResponse():
    """
    PublicKeyResponse.

    :attr str public_key:
    """

    def __init__(self,
                 public_key: str) -> None:
        """
        Initialize a PublicKeyResponse object.

        :param str public_key:
        """
        self.public_key = public_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PublicKeyResponse':
        """Initialize a PublicKeyResponse object from a json dictionary."""
        args = {}
        if 'public_key' in _dict:
            args['public_key'] = _dict.get('public_key')
        else:
            raise ValueError('Required property \'public_key\' not present in PublicKeyResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PublicKeyResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'public_key') and self.public_key is not None:
            _dict['public_key'] = self.public_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PublicKeyResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PublicKeyResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PublicKeyResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TestChannelResponse():
    """
    Response of deleted channel.

    :attr str test: (optional) response status.
    """

    def __init__(self,
                 *,
                 test: str = None) -> None:
        """
        Initialize a TestChannelResponse object.

        :param str test: (optional) response status.
        """
        self.test = test

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TestChannelResponse':
        """Initialize a TestChannelResponse object from a json dictionary."""
        args = {}
        if 'test' in _dict:
            args['test'] = _dict.get('test')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TestChannelResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'test') and self.test is not None:
            _dict['test'] = self.test
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TestChannelResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TestChannelResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TestChannelResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UpdateChannelResponse():
    """
    Response of updated channel.

    :attr str channel_id: (optional) id of the updated channel.
    :attr int status_code: (optional) response code.
    """

    def __init__(self,
                 *,
                 channel_id: str = None,
                 status_code: int = None) -> None:
        """
        Initialize a UpdateChannelResponse object.

        :param str channel_id: (optional) id of the updated channel.
        :param int status_code: (optional) response code.
        """
        self.channel_id = channel_id
        self.status_code = status_code

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateChannelResponse':
        """Initialize a UpdateChannelResponse object from a json dictionary."""
        args = {}
        if 'channel_id' in _dict:
            args['channel_id'] = _dict.get('channel_id')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateChannelResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel_id') and self.channel_id is not None:
            _dict['channel_id'] = self.channel_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateChannelResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateChannelResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateChannelResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
