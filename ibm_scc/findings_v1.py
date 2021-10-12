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

# IBM OpenAPI SDK Code Generator Version: 3.40.0-910cf8c2-20211006-154754
 
"""
The Findings API is used to find and display occurrences of security issues in your IBM
Cloud account by using the artifact metadata specification. Findings are summarized in
cards in the Security and Compliance Center that allow you to see the security status of
your account at a glance and start an investigation into any potential issues.

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, TextIO, Union
import json
import sys

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class FindingsV1(BaseService):
    """The Findings V1 service."""

    DEFAULT_SERVICE_URL = 'https://us-south.secadvisor.cloud.ibm.com/findings'
    DEFAULT_SERVICE_NAME = 'findings'

    @classmethod
    def new_instance(cls,
                     account_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'FindingsV1':
        """
        Return a new client for the Findings service using the specified parameters
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

    def __init__(self,
                 account_id: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Findings service.

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
    # graph
    #########################


    def post_graph(self,
        body: Union[str, TextIO],
        *,
        content_type: str = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Query findings.

        Query findings by using the GraphQL query language. For more information about
        using GraphQL, see the [GraphQL documentation](https://graphql.org/learn/).

        :param str body: Body for query findings.
        :param str content_type: (optional) The type of the input.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if body is None:
            raise ValueError('body must be provided')
        headers = {
            'Content-Type': content_type,
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_graph')
        headers.update(sdk_headers)

        if isinstance(body, dict):
            data = json.dumps(body)
            if content_type is None:
                headers['Content-Type'] = 'application/json'
        else:
            data = body

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/graph'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # notes
    #########################


    def list_providers(self,
        *,
        transaction_id: str = None,
        limit: int = None,
        skip: int = None,
        start_provider_id: str = None,
        end_provider_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List providers.

        List all of the providers for a specified account.

        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param int limit: (optional) The number of documents that you want to
               return.
        :param int skip: (optional) The offset is the index of the item from which
               you want to start returning data from. Default is 0.
        :param str start_provider_id: (optional) The first provider ID included in
               the result, sorted in ascending order. If not provided, this parameter is
               ignored.
        :param str end_provider_id: (optional) The last provider ID included in the
               result, sorted in ascending order. If not provided, this parameter is
               ignored.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiListProvidersResponse` object
        """

        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_providers')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'skip': skip,
            'start_provider_id': start_provider_id,
            'end_provider_id': end_provider_id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id']
        path_param_values = self.encode_path_vars(self.account_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_note(self,
        provider_id: str,
        short_description: str,
        long_description: str,
        kind: str,
        id: str,
        reported_by: 'Reporter',
        *,
        related_url: List['ApiNoteRelatedUrl'] = None,
        create_time: datetime = None,
        update_time: datetime = None,
        shared: bool = None,
        finding: 'FindingType' = None,
        kpi: 'KpiType' = None,
        card: 'Card' = None,
        section: 'Section' = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a note.

        Register a new finding type with the Security and Compliance Center.
        A successful request creates a note with a high-level description of a particular
        type of finding. To learn more about creating notes to register findings, see
        [Custom findings](/docs/security-advisor?topic=security-advisor-setup_custom).

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str short_description: A one sentence description of your note.
        :param str long_description: A more detailed description of your note.
        :param str kind: The type of note. Use this field to filter notes and
               occurences by kind.
                - FINDING&#58; The note and occurrence represent a finding.
                - KPI&#58; The note and occurrence represent a KPI value.
                - CARD&#58; The note represents a card showing findings and related metric
               values.
                - CARD_CONFIGURED&#58; The note represents a card configured for a user
               account.
                - SECTION&#58; The note represents a section in a dashboard.
        :param str id: The ID of the note.
        :param Reporter reported_by: The entity reporting a note.
        :param List[ApiNoteRelatedUrl] related_url: (optional)
        :param datetime create_time: (optional) Output only. The time this note was
               created. This field can be used as a filter in list requests.
        :param datetime update_time: (optional) Output only. The time this note was
               last updated. This field can be used as a filter in list requests.
        :param bool shared: (optional) True if this note can be shared by multiple
               accounts.
        :param FindingType finding: (optional) FindingType provides details about a
               finding note.
        :param KpiType kpi: (optional) KpiType provides details about a KPI note.
        :param Card card: (optional) Card provides details about a card kind of
               note.
        :param Section section: (optional) Card provides details about a card kind
               of note.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiNote` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if short_description is None:
            raise ValueError('short_description must be provided')
        if long_description is None:
            raise ValueError('long_description must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        if reported_by is None:
            raise ValueError('reported_by must be provided')
        reported_by = convert_model(reported_by)
        if related_url is not None:
            related_url = [convert_model(x) for x in related_url]
        if create_time is not None:
            create_time = datetime_to_string(create_time)
        if update_time is not None:
            update_time = datetime_to_string(update_time)
        if finding is not None:
            finding = convert_model(finding)
        if kpi is not None:
            kpi = convert_model(kpi)
        if card is not None:
            card = convert_model(card)
        if section is not None:
            section = convert_model(section)
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_note')
        headers.update(sdk_headers)

        data = {
            'short_description': short_description,
            'long_description': long_description,
            'kind': kind,
            'id': id,
            'reported_by': reported_by,
            'related_url': related_url,
            'create_time': create_time,
            'update_time': update_time,
            'shared': shared,
            'finding': finding,
            'kpi': kpi,
            'card': card,
            'section': section
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/notes'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_notes(self,
        provider_id: str,
        *,
        transaction_id: str = None,
        page_size: int = None,
        page_token: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List notes.

        List all of the available notes for a specific provider.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param int page_size: (optional) Number of notes to return in the list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiListNotesResponse` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_notes')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/notes'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_note(self,
        provider_id: str,
        note_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a note by provider.

        Get the details of the note that is associated with a specified note ID and
        provider ID.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiNote` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_note')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'note_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, note_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/notes/{note_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_note(self,
        provider_id: str,
        note_id: str,
        short_description: str,
        long_description: str,
        kind: str,
        id: str,
        reported_by: 'Reporter',
        *,
        related_url: List['ApiNoteRelatedUrl'] = None,
        create_time: datetime = None,
        update_time: datetime = None,
        shared: bool = None,
        finding: 'FindingType' = None,
        kpi: 'KpiType' = None,
        card: 'Card' = None,
        section: 'Section' = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a note.

        Update a note that already exists in your account.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str short_description: A one sentence description of your note.
        :param str long_description: A more detailed description of your note.
        :param str kind: The type of note. Use this field to filter notes and
               occurences by kind.
                - FINDING&#58; The note and occurrence represent a finding.
                - KPI&#58; The note and occurrence represent a KPI value.
                - CARD&#58; The note represents a card showing findings and related metric
               values.
                - CARD_CONFIGURED&#58; The note represents a card configured for a user
               account.
                - SECTION&#58; The note represents a section in a dashboard.
        :param str id: The ID of the note.
        :param Reporter reported_by: The entity reporting a note.
        :param List[ApiNoteRelatedUrl] related_url: (optional)
        :param datetime create_time: (optional) Output only. The time this note was
               created. This field can be used as a filter in list requests.
        :param datetime update_time: (optional) Output only. The time this note was
               last updated. This field can be used as a filter in list requests.
        :param bool shared: (optional) True if this note can be shared by multiple
               accounts.
        :param FindingType finding: (optional) FindingType provides details about a
               finding note.
        :param KpiType kpi: (optional) KpiType provides details about a KPI note.
        :param Card card: (optional) Card provides details about a card kind of
               note.
        :param Section section: (optional) Card provides details about a card kind
               of note.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiNote` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')
        if short_description is None:
            raise ValueError('short_description must be provided')
        if long_description is None:
            raise ValueError('long_description must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        if reported_by is None:
            raise ValueError('reported_by must be provided')
        reported_by = convert_model(reported_by)
        if related_url is not None:
            related_url = [convert_model(x) for x in related_url]
        if create_time is not None:
            create_time = datetime_to_string(create_time)
        if update_time is not None:
            update_time = datetime_to_string(update_time)
        if finding is not None:
            finding = convert_model(finding)
        if kpi is not None:
            kpi = convert_model(kpi)
        if card is not None:
            card = convert_model(card)
        if section is not None:
            section = convert_model(section)
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_note')
        headers.update(sdk_headers)

        data = {
            'short_description': short_description,
            'long_description': long_description,
            'kind': kind,
            'id': id,
            'reported_by': reported_by,
            'related_url': related_url,
            'create_time': create_time,
            'update_time': update_time,
            'shared': shared,
            'finding': finding,
            'kpi': kpi,
            'card': card,
            'section': section
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'note_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, note_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/notes/{note_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_note(self,
        provider_id: str,
        note_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a note.

        Delete a note with the ID and provider ID that you specify.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_note')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'note_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, note_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/notes/{note_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_occurrence_note(self,
        provider_id: str,
        occurrence_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a note by occurrence.

        Get a note that is associated with the occurrence ID that you specify.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiNote` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_occurrence_note')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'occurrence_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, occurrence_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/occurrences/{occurrence_id}/note'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # occurrences
    #########################


    def create_occurrence(self,
        provider_id: str,
        note_name: str,
        kind: str,
        id: str,
        *,
        resource_url: str = None,
        remediation: str = None,
        context: 'Context' = None,
        finding: 'Finding' = None,
        kpi: 'Kpi' = None,
        reference_data: object = None,
        transaction_id: str = None,
        replace_if_exists: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create an occurrence.

        Create an occurrence to denote the existence of a particular type of finding.
        An occurrence describes provider-specific details of a note and contains
        vulnerability details, remediation steps, and other general information.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str note_name: An analysis note associated with this image, in the
               form "{account_id}/providers/{provider_id}/notes/{note_id}" This field can
               be used as a filter in list requests.
        :param str kind: The type of note. Use this field to filter notes and
               occurences by kind.
                - FINDING&#58; The note and occurrence represent a finding.
                - KPI&#58; The note and occurrence represent a KPI value.
                - CARD&#58; The note represents a card showing findings and related metric
               values.
                - CARD_CONFIGURED&#58; The note represents a card configured for a user
               account.
                - SECTION&#58; The note represents a section in a dashboard.
        :param str id: The id of the occurrence.
        :param str resource_url: (optional) The unique URL of the resource, image
               or the container, for which the `Occurrence` applies. For example,
               https://gcr.io/provider/image@sha256:foo. This field can be used as a
               filter in list requests.
        :param str remediation: (optional) A description of actions that can be
               taken to remedy the `Note`.
        :param Context context: (optional)
        :param Finding finding: (optional) Finding provides details about a finding
               occurrence.
        :param Kpi kpi: (optional) Kpi provides details about a KPI occurrence.
        :param object reference_data: (optional) Additional data for the finding,
               like AT event etc.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param bool replace_if_exists: (optional) When set to true, an existing
               occurrence is replaced rather than duplicated.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiOccurrence` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_name is None:
            raise ValueError('note_name must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        if context is not None:
            context = convert_model(context)
        if finding is not None:
            finding = convert_model(finding)
        if kpi is not None:
            kpi = convert_model(kpi)
        headers = {
            'Transaction-Id': transaction_id,
            'Replace-If-Exists': replace_if_exists
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_occurrence')
        headers.update(sdk_headers)

        data = {
            'note_name': note_name,
            'kind': kind,
            'id': id,
            'resource_url': resource_url,
            'remediation': remediation,
            'context': context,
            'finding': finding,
            'kpi': kpi,
            'reference_data': reference_data
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/occurrences'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_occurrences(self,
        provider_id: str,
        *,
        transaction_id: str = None,
        page_size: int = None,
        page_token: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List occurrences.

        List all of the occurrences that are associated with the provider ID that you
        specify.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param int page_size: (optional) Number of notes to return in the list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiListOccurrencesResponse` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_occurrences')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/occurrences'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def list_note_occurrences(self,
        provider_id: str,
        note_id: str,
        *,
        transaction_id: str = None,
        page_size: int = None,
        page_token: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List occurrences by note.

        Get a list of occurrences that are associated with a specific note.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str note_id: Second part of note `name`:
               providers/{provider_id}/notes/{note_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param int page_size: (optional) Number of notes to return in the list.
        :param str page_token: (optional) Token to provide to skip to a particular
               spot in the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiListNoteOccurrencesResponse` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if note_id is None:
            raise ValueError('note_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_note_occurrences')
        headers.update(sdk_headers)

        params = {
            'page_size': page_size,
            'page_token': page_token
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'note_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, note_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/notes/{note_id}/occurrences'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_occurrence(self,
        provider_id: str,
        occurrence_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a specific occurrence.

        Get the details of a specific occurrence by specifying the ID and provider ID.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiOccurrence` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_occurrence')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'occurrence_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, occurrence_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/occurrences/{occurrence_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_occurrence(self,
        provider_id: str,
        occurrence_id: str,
        note_name: str,
        kind: str,
        id: str,
        *,
        resource_url: str = None,
        remediation: str = None,
        context: 'Context' = None,
        finding: 'Finding' = None,
        kpi: 'Kpi' = None,
        reference_data: object = None,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an occurrence.

        Update an occurrence that already exists in your account.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str note_name: An analysis note associated with this image, in the
               form "{account_id}/providers/{provider_id}/notes/{note_id}" This field can
               be used as a filter in list requests.
        :param str kind: The type of note. Use this field to filter notes and
               occurences by kind.
                - FINDING&#58; The note and occurrence represent a finding.
                - KPI&#58; The note and occurrence represent a KPI value.
                - CARD&#58; The note represents a card showing findings and related metric
               values.
                - CARD_CONFIGURED&#58; The note represents a card configured for a user
               account.
                - SECTION&#58; The note represents a section in a dashboard.
        :param str id: The id of the occurrence.
        :param str resource_url: (optional) The unique URL of the resource, image
               or the container, for which the `Occurrence` applies. For example,
               https://gcr.io/provider/image@sha256:foo. This field can be used as a
               filter in list requests.
        :param str remediation: (optional) A description of actions that can be
               taken to remedy the `Note`.
        :param Context context: (optional)
        :param Finding finding: (optional) Finding provides details about a finding
               occurrence.
        :param Kpi kpi: (optional) Kpi provides details about a KPI occurrence.
        :param object reference_data: (optional) Additional data for the finding,
               like AT event etc.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApiOccurrence` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')
        if note_name is None:
            raise ValueError('note_name must be provided')
        if kind is None:
            raise ValueError('kind must be provided')
        if id is None:
            raise ValueError('id must be provided')
        if context is not None:
            context = convert_model(context)
        if finding is not None:
            finding = convert_model(finding)
        if kpi is not None:
            kpi = convert_model(kpi)
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_occurrence')
        headers.update(sdk_headers)

        data = {
            'note_name': note_name,
            'kind': kind,
            'id': id,
            'resource_url': resource_url,
            'remediation': remediation,
            'context': context,
            'finding': finding,
            'kpi': kpi,
            'reference_data': reference_data
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'occurrence_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, occurrence_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/occurrences/{occurrence_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_occurrence(self,
        provider_id: str,
        occurrence_id: str,
        *,
        transaction_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an occurrence.

        Delete an occurrence by specifying the occurrence ID and provider ID.

        :param str provider_id: Part of the parent. This field contains the
               provider ID. For example: providers/{provider_id}.
        :param str occurrence_id: Second part of occurrence `name`:
               providers/{provider_id}/occurrences/{occurrence_id}.
        :param str transaction_id: (optional) The transaction ID for the request in
               UUID v4 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if occurrence_id is None:
            raise ValueError('occurrence_id must be provided')
        headers = {
            'Transaction-Id': transaction_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_occurrence')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['account_id', 'provider_id', 'occurrence_id']
        path_param_values = self.encode_path_vars(self.account_id, provider_id, occurrence_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{account_id}/providers/{provider_id}/occurrences/{occurrence_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


class PostGraphEnums:
    """
    Enums for post_graph parameters.
    """

    class ContentType(str, Enum):
        """
        The type of the input.
        """
        APPLICATION_JSON = 'application/json'
        APPLICATION_GRAPHQL = 'application/graphql'


##############################################################################
# Models
##############################################################################


class Card():
    """
    Card provides details about a card kind of note.

    :attr str section: The section this card belongs to.
    :attr str title: The title of this card.
    :attr str subtitle: The subtitle of this card.
    :attr int order: (optional) The order of the card in which it will appear on SA
          dashboard in the mentioned section.
    :attr List[str] finding_note_names: The finding note names associated to this
          card.
    :attr bool requires_configuration: (optional)
    :attr str badge_text: (optional) The text associated to the card's badge.
    :attr str badge_image: (optional) The base64 content of the image associated to
          the card's badge.
    :attr List[CardElement] elements: The elements of this card.
    """

    def __init__(self,
                 section: str,
                 title: str,
                 subtitle: str,
                 finding_note_names: List[str],
                 elements: List['CardElement'],
                 *,
                 order: int = None,
                 requires_configuration: bool = None,
                 badge_text: str = None,
                 badge_image: str = None) -> None:
        """
        Initialize a Card object.

        :param str section: The section this card belongs to.
        :param str title: The title of this card.
        :param str subtitle: The subtitle of this card.
        :param List[str] finding_note_names: The finding note names associated to
               this card.
        :param List[CardElement] elements: The elements of this card.
        :param int order: (optional) The order of the card in which it will appear
               on SA dashboard in the mentioned section.
        :param bool requires_configuration: (optional)
        :param str badge_text: (optional) The text associated to the card's badge.
        :param str badge_image: (optional) The base64 content of the image
               associated to the card's badge.
        """
        self.section = section
        self.title = title
        self.subtitle = subtitle
        self.order = order
        self.finding_note_names = finding_note_names
        self.requires_configuration = requires_configuration
        self.badge_text = badge_text
        self.badge_image = badge_image
        self.elements = elements

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Card':
        """Initialize a Card object from a json dictionary."""
        args = {}
        if 'section' in _dict:
            args['section'] = _dict.get('section')
        else:
            raise ValueError('Required property \'section\' not present in Card JSON')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError('Required property \'title\' not present in Card JSON')
        if 'subtitle' in _dict:
            args['subtitle'] = _dict.get('subtitle')
        else:
            raise ValueError('Required property \'subtitle\' not present in Card JSON')
        if 'order' in _dict:
            args['order'] = _dict.get('order')
        if 'finding_note_names' in _dict:
            args['finding_note_names'] = _dict.get('finding_note_names')
        else:
            raise ValueError('Required property \'finding_note_names\' not present in Card JSON')
        if 'requires_configuration' in _dict:
            args['requires_configuration'] = _dict.get('requires_configuration')
        if 'badge_text' in _dict:
            args['badge_text'] = _dict.get('badge_text')
        if 'badge_image' in _dict:
            args['badge_image'] = _dict.get('badge_image')
        if 'elements' in _dict:
            args['elements'] = [CardElement.from_dict(x) for x in _dict.get('elements')]
        else:
            raise ValueError('Required property \'elements\' not present in Card JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Card object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'section') and self.section is not None:
            _dict['section'] = self.section
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'subtitle') and self.subtitle is not None:
            _dict['subtitle'] = self.subtitle
        if hasattr(self, 'order') and self.order is not None:
            _dict['order'] = self.order
        if hasattr(self, 'finding_note_names') and self.finding_note_names is not None:
            _dict['finding_note_names'] = self.finding_note_names
        if hasattr(self, 'requires_configuration') and self.requires_configuration is not None:
            _dict['requires_configuration'] = self.requires_configuration
        if hasattr(self, 'badge_text') and self.badge_text is not None:
            _dict['badge_text'] = self.badge_text
        if hasattr(self, 'badge_image') and self.badge_image is not None:
            _dict['badge_image'] = self.badge_image
        if hasattr(self, 'elements') and self.elements is not None:
            _dict['elements'] = [x.to_dict() for x in self.elements]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Card object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Card') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Card') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CardElement():
    """
    CardElement provides details about the elements of a Card.

    """

    def __init__(self) -> None:
        """
        Initialize a CardElement object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['CardElementNumericCardElement', 'CardElementBreakdownCardElement', 'CardElementTimeSeriesCardElement']))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CardElement':
        """Initialize a CardElement object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = ("Cannot convert dictionary into an instance of base class 'CardElement'. " +
                "The discriminator value should map to a valid subclass: {1}").format(
                  ", ".join(['CardElementNumericCardElement', 'CardElementBreakdownCardElement', 'CardElementTimeSeriesCardElement']))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a CardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['NUMERIC'] = 'CardElementNumericCardElement'
        mapping['BREAKDOWN'] = 'CardElementBreakdownCardElement'
        mapping['TIME_SERIES'] = 'CardElementTimeSeriesCardElement'
        disc_value = _dict.get('kind')
        if disc_value is None:
            raise ValueError('Discriminator property \'kind\' not found in CardElement JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)

class Context():
    """
    Context.

    :attr str region: (optional) The IBM Cloud region.
    :attr str resource_crn: (optional) The resource CRN (e.g. certificate CRN, image
          CRN).
    :attr str resource_id: (optional) The resource ID, in case the CRN is not
          available.
    :attr str resource_name: (optional) The user-friendly resource name.
    :attr str resource_type: (optional) The resource type name (e.g. Pod, Cluster,
          Certificate, Image).
    :attr str service_crn: (optional) The service CRN (e.g. CertMgr Instance CRN).
    :attr str service_name: (optional) The service name (e.g. CertMgr).
    :attr str environment_name: (optional) The name of the environment the
          occurrence applies to.
    :attr str component_name: (optional) The name of the component the occurrence
          applies to.
    :attr str toolchain_id: (optional) The id of the toolchain the occurrence
          applies to.
    """

    def __init__(self,
                 *,
                 region: str = None,
                 resource_crn: str = None,
                 resource_id: str = None,
                 resource_name: str = None,
                 resource_type: str = None,
                 service_crn: str = None,
                 service_name: str = None,
                 environment_name: str = None,
                 component_name: str = None,
                 toolchain_id: str = None) -> None:
        """
        Initialize a Context object.

        :param str region: (optional) The IBM Cloud region.
        :param str resource_crn: (optional) The resource CRN (e.g. certificate CRN,
               image CRN).
        :param str resource_id: (optional) The resource ID, in case the CRN is not
               available.
        :param str resource_name: (optional) The user-friendly resource name.
        :param str resource_type: (optional) The resource type name (e.g. Pod,
               Cluster, Certificate, Image).
        :param str service_crn: (optional) The service CRN (e.g. CertMgr Instance
               CRN).
        :param str service_name: (optional) The service name (e.g. CertMgr).
        :param str environment_name: (optional) The name of the environment the
               occurrence applies to.
        :param str component_name: (optional) The name of the component the
               occurrence applies to.
        :param str toolchain_id: (optional) The id of the toolchain the occurrence
               applies to.
        """
        self.region = region
        self.resource_crn = resource_crn
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.service_crn = service_crn
        self.service_name = service_name
        self.environment_name = environment_name
        self.component_name = component_name
        self.toolchain_id = toolchain_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Context':
        """Initialize a Context object from a json dictionary."""
        args = {}
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'resource_crn' in _dict:
            args['resource_crn'] = _dict.get('resource_crn')
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'service_crn' in _dict:
            args['service_crn'] = _dict.get('service_crn')
        if 'service_name' in _dict:
            args['service_name'] = _dict.get('service_name')
        if 'environment_name' in _dict:
            args['environment_name'] = _dict.get('environment_name')
        if 'component_name' in _dict:
            args['component_name'] = _dict.get('component_name')
        if 'toolchain_id' in _dict:
            args['toolchain_id'] = _dict.get('toolchain_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Context object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'resource_crn') and self.resource_crn is not None:
            _dict['resource_crn'] = self.resource_crn
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'service_crn') and self.service_crn is not None:
            _dict['service_crn'] = self.service_crn
        if hasattr(self, 'service_name') and self.service_name is not None:
            _dict['service_name'] = self.service_name
        if hasattr(self, 'environment_name') and self.environment_name is not None:
            _dict['environment_name'] = self.environment_name
        if hasattr(self, 'component_name') and self.component_name is not None:
            _dict['component_name'] = self.component_name
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Context object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Context') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Context') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DataTransferred():
    """
    It provides details about data transferred between clients and servers.

    :attr int client_bytes: (optional) The number of client bytes transferred.
    :attr int server_bytes: (optional) The number of server bytes transferred.
    :attr int client_packets: (optional) The number of client packets transferred.
    :attr int server_packets: (optional) The number of server packets transferred.
    """

    def __init__(self,
                 *,
                 client_bytes: int = None,
                 server_bytes: int = None,
                 client_packets: int = None,
                 server_packets: int = None) -> None:
        """
        Initialize a DataTransferred object.

        :param int client_bytes: (optional) The number of client bytes transferred.
        :param int server_bytes: (optional) The number of server bytes transferred.
        :param int client_packets: (optional) The number of client packets
               transferred.
        :param int server_packets: (optional) The number of server packets
               transferred.
        """
        self.client_bytes = client_bytes
        self.server_bytes = server_bytes
        self.client_packets = client_packets
        self.server_packets = server_packets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DataTransferred':
        """Initialize a DataTransferred object from a json dictionary."""
        args = {}
        if 'client_bytes' in _dict:
            args['client_bytes'] = _dict.get('client_bytes')
        if 'server_bytes' in _dict:
            args['server_bytes'] = _dict.get('server_bytes')
        if 'client_packets' in _dict:
            args['client_packets'] = _dict.get('client_packets')
        if 'server_packets' in _dict:
            args['server_packets'] = _dict.get('server_packets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DataTransferred object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_bytes') and self.client_bytes is not None:
            _dict['client_bytes'] = self.client_bytes
        if hasattr(self, 'server_bytes') and self.server_bytes is not None:
            _dict['server_bytes'] = self.server_bytes
        if hasattr(self, 'client_packets') and self.client_packets is not None:
            _dict['client_packets'] = self.client_packets
        if hasattr(self, 'server_packets') and self.server_packets is not None:
            _dict['server_packets'] = self.server_packets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DataTransferred object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DataTransferred') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DataTransferred') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Finding():
    """
    Finding provides details about a finding occurrence.

    :attr str severity: (optional) Note provider-assigned severity/impact ranking
          - LOW&#58; Low Impact
          - MEDIUM&#58; Medium Impact
          - HIGH&#58; High Impact
          - CRITICAL&#58; Critical Impact.
    :attr str certainty: (optional) Note provider-assigned confidence on the
          validity of an occurrence
          - LOW&#58; Low Certainty
          - MEDIUM&#58; Medium Certainty
          - HIGH&#58; High Certainty.
    :attr List[RemediationStep] next_steps: (optional) Remediation steps for the
          issues reported in this finding. They override the note's next steps.
    :attr NetworkConnection network_connection: (optional) It provides details about
          a network connection.
    :attr DataTransferred data_transferred: (optional) It provides details about
          data transferred between clients and servers.
    """

    def __init__(self,
                 *,
                 severity: str = None,
                 certainty: str = None,
                 next_steps: List['RemediationStep'] = None,
                 network_connection: 'NetworkConnection' = None,
                 data_transferred: 'DataTransferred' = None) -> None:
        """
        Initialize a Finding object.

        :param str severity: (optional) Note provider-assigned severity/impact
               ranking
               - LOW&#58; Low Impact
               - MEDIUM&#58; Medium Impact
               - HIGH&#58; High Impact
               - CRITICAL&#58; Critical Impact.
        :param str certainty: (optional) Note provider-assigned confidence on the
               validity of an occurrence
               - LOW&#58; Low Certainty
               - MEDIUM&#58; Medium Certainty
               - HIGH&#58; High Certainty.
        :param List[RemediationStep] next_steps: (optional) Remediation steps for
               the issues reported in this finding. They override the note's next steps.
        :param NetworkConnection network_connection: (optional) It provides details
               about a network connection.
        :param DataTransferred data_transferred: (optional) It provides details
               about data transferred between clients and servers.
        """
        self.severity = severity
        self.certainty = certainty
        self.next_steps = next_steps
        self.network_connection = network_connection
        self.data_transferred = data_transferred

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Finding':
        """Initialize a Finding object from a json dictionary."""
        args = {}
        if 'severity' in _dict:
            args['severity'] = _dict.get('severity')
        if 'certainty' in _dict:
            args['certainty'] = _dict.get('certainty')
        if 'next_steps' in _dict:
            args['next_steps'] = [RemediationStep.from_dict(x) for x in _dict.get('next_steps')]
        if 'network_connection' in _dict:
            args['network_connection'] = NetworkConnection.from_dict(_dict.get('network_connection'))
        if 'data_transferred' in _dict:
            args['data_transferred'] = DataTransferred.from_dict(_dict.get('data_transferred'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Finding object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity
        if hasattr(self, 'certainty') and self.certainty is not None:
            _dict['certainty'] = self.certainty
        if hasattr(self, 'next_steps') and self.next_steps is not None:
            _dict['next_steps'] = [x.to_dict() for x in self.next_steps]
        if hasattr(self, 'network_connection') and self.network_connection is not None:
            _dict['network_connection'] = self.network_connection.to_dict()
        if hasattr(self, 'data_transferred') and self.data_transferred is not None:
            _dict['data_transferred'] = self.data_transferred.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Finding object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Finding') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Finding') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SeverityEnum(str, Enum):
        """
        Note provider-assigned severity/impact ranking
        - LOW&#58; Low Impact
        - MEDIUM&#58; Medium Impact
        - HIGH&#58; High Impact
        - CRITICAL&#58; Critical Impact.
        """
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGH = 'HIGH'
        CRITICAL = 'CRITICAL'


    class CertaintyEnum(str, Enum):
        """
        Note provider-assigned confidence on the validity of an occurrence
        - LOW&#58; Low Certainty
        - MEDIUM&#58; Medium Certainty
        - HIGH&#58; High Certainty.
        """
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGH = 'HIGH'


class FindingType():
    """
    FindingType provides details about a finding note.

    :attr str severity: Note provider-assigned severity/impact ranking
          - LOW&#58; Low Impact
          - MEDIUM&#58; Medium Impact
          - HIGH&#58; High Impact
          - CRITICAL&#58; Critical Impact.
    :attr List[RemediationStep] next_steps: (optional) Common remediation steps for
          the finding of this type.
    """

    def __init__(self,
                 severity: str,
                 *,
                 next_steps: List['RemediationStep'] = None) -> None:
        """
        Initialize a FindingType object.

        :param str severity: Note provider-assigned severity/impact ranking
               - LOW&#58; Low Impact
               - MEDIUM&#58; Medium Impact
               - HIGH&#58; High Impact
               - CRITICAL&#58; Critical Impact.
        :param List[RemediationStep] next_steps: (optional) Common remediation
               steps for the finding of this type.
        """
        self.severity = severity
        self.next_steps = next_steps

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FindingType':
        """Initialize a FindingType object from a json dictionary."""
        args = {}
        if 'severity' in _dict:
            args['severity'] = _dict.get('severity')
        else:
            raise ValueError('Required property \'severity\' not present in FindingType JSON')
        if 'next_steps' in _dict:
            args['next_steps'] = [RemediationStep.from_dict(x) for x in _dict.get('next_steps')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FindingType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['severity'] = self.severity
        if hasattr(self, 'next_steps') and self.next_steps is not None:
            _dict['next_steps'] = [x.to_dict() for x in self.next_steps]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FindingType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FindingType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FindingType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SeverityEnum(str, Enum):
        """
        Note provider-assigned severity/impact ranking
        - LOW&#58; Low Impact
        - MEDIUM&#58; Medium Impact
        - HIGH&#58; High Impact
        - CRITICAL&#58; Critical Impact.
        """
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGH = 'HIGH'
        CRITICAL = 'CRITICAL'


class Kpi():
    """
    Kpi provides details about a KPI occurrence.

    :attr float value: The value of this KPI.
    :attr float total: (optional) The total value of this KPI.
    """

    def __init__(self,
                 value: float,
                 *,
                 total: float = None) -> None:
        """
        Initialize a Kpi object.

        :param float value: The value of this KPI.
        :param float total: (optional) The total value of this KPI.
        """
        self.value = value
        self.total = total

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Kpi':
        """Initialize a Kpi object from a json dictionary."""
        args = {}
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Kpi JSON')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Kpi object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Kpi object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Kpi') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Kpi') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class KpiType():
    """
    KpiType provides details about a KPI note.

    :attr str severity: (optional)
    :attr str aggregation_type: The aggregation type of the KPI values. - SUM&#58; A
          single-value metrics aggregation type that sums up numeric values
            that are extracted from KPI occurrences.
    """

    def __init__(self,
                 aggregation_type: str,
                 *,
                 severity: str = None) -> None:
        """
        Initialize a KpiType object.

        :param str aggregation_type: The aggregation type of the KPI values. -
               SUM&#58; A single-value metrics aggregation type that sums up numeric
               values
                 that are extracted from KPI occurrences.
        :param str severity: (optional)
        """
        self.severity = severity
        self.aggregation_type = aggregation_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KpiType':
        """Initialize a KpiType object from a json dictionary."""
        args = {}
        if 'Severity' in _dict:
            args['severity'] = _dict.get('Severity')
        if 'aggregation_type' in _dict:
            args['aggregation_type'] = _dict.get('aggregation_type')
        else:
            raise ValueError('Required property \'aggregation_type\' not present in KpiType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KpiType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'severity') and self.severity is not None:
            _dict['Severity'] = self.severity
        if hasattr(self, 'aggregation_type') and self.aggregation_type is not None:
            _dict['aggregation_type'] = self.aggregation_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KpiType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'KpiType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KpiType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SeverityEnum(str, Enum):
        """
        severity.
        """
        LOW = 'LOW'
        MEDIUM = 'MEDIUM'
        HIGH = 'HIGH'
        CRITICAL = 'CRITICAL'


    class AggregationTypeEnum(str, Enum):
        """
        The aggregation type of the KPI values. - SUM&#58; A single-value metrics
        aggregation type that sums up numeric values
          that are extracted from KPI occurrences.
        """
        SUM = 'SUM'


class NetworkConnection():
    """
    It provides details about a network connection.

    :attr str direction: (optional) The direction of this network connection.
    :attr str protocol: (optional) The protocol of this network connection.
    :attr SocketAddress client: (optional) It provides details about a socket
          address.
    :attr SocketAddress server: (optional) It provides details about a socket
          address.
    """

    def __init__(self,
                 *,
                 direction: str = None,
                 protocol: str = None,
                 client: 'SocketAddress' = None,
                 server: 'SocketAddress' = None) -> None:
        """
        Initialize a NetworkConnection object.

        :param str direction: (optional) The direction of this network connection.
        :param str protocol: (optional) The protocol of this network connection.
        :param SocketAddress client: (optional) It provides details about a socket
               address.
        :param SocketAddress server: (optional) It provides details about a socket
               address.
        """
        self.direction = direction
        self.protocol = protocol
        self.client = client
        self.server = server

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NetworkConnection':
        """Initialize a NetworkConnection object from a json dictionary."""
        args = {}
        if 'direction' in _dict:
            args['direction'] = _dict.get('direction')
        if 'protocol' in _dict:
            args['protocol'] = _dict.get('protocol')
        if 'client' in _dict:
            args['client'] = SocketAddress.from_dict(_dict.get('client'))
        if 'server' in _dict:
            args['server'] = SocketAddress.from_dict(_dict.get('server'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NetworkConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'direction') and self.direction is not None:
            _dict['direction'] = self.direction
        if hasattr(self, 'protocol') and self.protocol is not None:
            _dict['protocol'] = self.protocol
        if hasattr(self, 'client') and self.client is not None:
            _dict['client'] = self.client.to_dict()
        if hasattr(self, 'server') and self.server is not None:
            _dict['server'] = self.server.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NetworkConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NetworkConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NetworkConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RemediationStep():
    """
    A remediation step description and associated URL.

    :attr str title: (optional) Title of this next step.
    :attr str url: (optional) The URL associated to this next steps.
    """

    def __init__(self,
                 *,
                 title: str = None,
                 url: str = None) -> None:
        """
        Initialize a RemediationStep object.

        :param str title: (optional) Title of this next step.
        :param str url: (optional) The URL associated to this next steps.
        """
        self.title = title
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RemediationStep':
        """Initialize a RemediationStep object from a json dictionary."""
        args = {}
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RemediationStep object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RemediationStep object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RemediationStep') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RemediationStep') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Reporter():
    """
    The entity reporting a note.

    :attr str id: The id of this reporter.
    :attr str title: The title of this reporter.
    :attr str url: (optional) The url of this reporter.
    """

    def __init__(self,
                 id: str,
                 title: str,
                 *,
                 url: str = None) -> None:
        """
        Initialize a Reporter object.

        :param str id: The id of this reporter.
        :param str title: The title of this reporter.
        :param str url: (optional) The url of this reporter.
        """
        self.id = id
        self.title = title
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Reporter':
        """Initialize a Reporter object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Reporter JSON')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError('Required property \'title\' not present in Reporter JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Reporter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Reporter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Reporter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Reporter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Section():
    """
    Card provides details about a card kind of note.

    :attr str title: The title of this section.
    :attr str image: The image of this section.
    """

    def __init__(self,
                 title: str,
                 image: str) -> None:
        """
        Initialize a Section object.

        :param str title: The title of this section.
        :param str image: The image of this section.
        """
        self.title = title
        self.image = image

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Section':
        """Initialize a Section object from a json dictionary."""
        args = {}
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError('Required property \'title\' not present in Section JSON')
        if 'image' in _dict:
            args['image'] = _dict.get('image')
        else:
            raise ValueError('Required property \'image\' not present in Section JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Section object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Section object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Section') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Section') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SocketAddress():
    """
    It provides details about a socket address.

    :attr str address: The IP address of this socket address.
    :attr int port: (optional) The port number of this socket address.
    """

    def __init__(self,
                 address: str,
                 *,
                 port: int = None) -> None:
        """
        Initialize a SocketAddress object.

        :param str address: The IP address of this socket address.
        :param int port: (optional) The port number of this socket address.
        """
        self.address = address
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SocketAddress':
        """Initialize a SocketAddress object from a json dictionary."""
        args = {}
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        else:
            raise ValueError('Required property \'address\' not present in SocketAddress JSON')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SocketAddress object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SocketAddress object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SocketAddress') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SocketAddress') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ValueType():
    """
    the value type of a card element.

    """

    def __init__(self) -> None:
        """
        Initialize a ValueType object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['ValueTypeKpiValueType', 'ValueTypeFindingCountValueType']))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValueType':
        """Initialize a ValueType object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = ("Cannot convert dictionary into an instance of base class 'ValueType'. " +
                "The discriminator value should map to a valid subclass: {1}").format(
                  ", ".join(['ValueTypeKpiValueType', 'ValueTypeFindingCountValueType']))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a ValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['KPI'] = 'ValueTypeKpiValueType'
        mapping['FINDING_COUNT'] = 'ValueTypeFindingCountValueType'
        disc_value = _dict.get('kind')
        if disc_value is None:
            raise ValueError('Discriminator property \'kind\' not found in ValueType JSON')
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)

class ApiListNoteOccurrencesResponse():
    """
    Response including listed occurrences for a note.

    :attr List[ApiOccurrence] occurrences: (optional) The occurrences attached to
          the specified note.
    :attr str next_page_token: (optional) Token to receive the next page of notes.
    """

    def __init__(self,
                 *,
                 occurrences: List['ApiOccurrence'] = None,
                 next_page_token: str = None) -> None:
        """
        Initialize a ApiListNoteOccurrencesResponse object.

        :param List[ApiOccurrence] occurrences: (optional) The occurrences attached
               to the specified note.
        :param str next_page_token: (optional) Token to receive the next page of
               notes.
        """
        self.occurrences = occurrences
        self.next_page_token = next_page_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListNoteOccurrencesResponse':
        """Initialize a ApiListNoteOccurrencesResponse object from a json dictionary."""
        args = {}
        if 'occurrences' in _dict:
            args['occurrences'] = [ApiOccurrence.from_dict(x) for x in _dict.get('occurrences')]
        if 'next_page_token' in _dict:
            args['next_page_token'] = _dict.get('next_page_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListNoteOccurrencesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'occurrences') and self.occurrences is not None:
            _dict['occurrences'] = [x.to_dict() for x in self.occurrences]
        if hasattr(self, 'next_page_token') and self.next_page_token is not None:
            _dict['next_page_token'] = self.next_page_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListNoteOccurrencesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiListNoteOccurrencesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListNoteOccurrencesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiListNotesResponse():
    """
    Response including listed notes.

    :attr List[ApiNote] notes: (optional) The occurrences requested.
    :attr str next_page_token: (optional) The next pagination token in the list
          response. It should be used as page_token for the following request. An empty
          value means no more result.
    """

    def __init__(self,
                 *,
                 notes: List['ApiNote'] = None,
                 next_page_token: str = None) -> None:
        """
        Initialize a ApiListNotesResponse object.

        :param List[ApiNote] notes: (optional) The occurrences requested.
        :param str next_page_token: (optional) The next pagination token in the
               list response. It should be used as page_token for the following request.
               An empty value means no more result.
        """
        self.notes = notes
        self.next_page_token = next_page_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListNotesResponse':
        """Initialize a ApiListNotesResponse object from a json dictionary."""
        args = {}
        if 'notes' in _dict:
            args['notes'] = [ApiNote.from_dict(x) for x in _dict.get('notes')]
        if 'next_page_token' in _dict:
            args['next_page_token'] = _dict.get('next_page_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListNotesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'notes') and self.notes is not None:
            _dict['notes'] = [x.to_dict() for x in self.notes]
        if hasattr(self, 'next_page_token') and self.next_page_token is not None:
            _dict['next_page_token'] = self.next_page_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListNotesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiListNotesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListNotesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiListOccurrencesResponse():
    """
    Response including listed active occurrences.

    :attr List[ApiOccurrence] occurrences: (optional) The occurrences requested.
    :attr str next_page_token: (optional) The next pagination token in the list
          response. It should be used as
          `page_token` for the following request. An empty value means no more results.
    """

    def __init__(self,
                 *,
                 occurrences: List['ApiOccurrence'] = None,
                 next_page_token: str = None) -> None:
        """
        Initialize a ApiListOccurrencesResponse object.

        :param List[ApiOccurrence] occurrences: (optional) The occurrences
               requested.
        :param str next_page_token: (optional) The next pagination token in the
               list response. It should be used as
               `page_token` for the following request. An empty value means no more
               results.
        """
        self.occurrences = occurrences
        self.next_page_token = next_page_token

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListOccurrencesResponse':
        """Initialize a ApiListOccurrencesResponse object from a json dictionary."""
        args = {}
        if 'occurrences' in _dict:
            args['occurrences'] = [ApiOccurrence.from_dict(x) for x in _dict.get('occurrences')]
        if 'next_page_token' in _dict:
            args['next_page_token'] = _dict.get('next_page_token')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListOccurrencesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'occurrences') and self.occurrences is not None:
            _dict['occurrences'] = [x.to_dict() for x in self.occurrences]
        if hasattr(self, 'next_page_token') and self.next_page_token is not None:
            _dict['next_page_token'] = self.next_page_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListOccurrencesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiListOccurrencesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListOccurrencesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiListProvidersResponse():
    """
    A list of providers is returned.

    :attr List[ApiProvider] providers: (optional) The providers requested.
    :attr int limit: (optional) The number of elements returned in the current
          instance. The default is 200.
    :attr int skip: (optional) The offset is the index of the item from which you
          want to start returning data from. The default is 0.
    :attr int total_count: (optional) The total number of providers available.
    """

    def __init__(self,
                 *,
                 providers: List['ApiProvider'] = None,
                 limit: int = None,
                 skip: int = None,
                 total_count: int = None) -> None:
        """
        Initialize a ApiListProvidersResponse object.

        :param List[ApiProvider] providers: (optional) The providers requested.
        :param int limit: (optional) The number of elements returned in the current
               instance. The default is 200.
        :param int skip: (optional) The offset is the index of the item from which
               you want to start returning data from. The default is 0.
        :param int total_count: (optional) The total number of providers available.
        """
        self.providers = providers
        self.limit = limit
        self.skip = skip
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiListProvidersResponse':
        """Initialize a ApiListProvidersResponse object from a json dictionary."""
        args = {}
        if 'providers' in _dict:
            args['providers'] = [ApiProvider.from_dict(x) for x in _dict.get('providers')]
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'skip' in _dict:
            args['skip'] = _dict.get('skip')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiListProvidersResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'providers') and self.providers is not None:
            _dict['providers'] = [x.to_dict() for x in self.providers]
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'skip') and self.skip is not None:
            _dict['skip'] = self.skip
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiListProvidersResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiListProvidersResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiListProvidersResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiNote():
    """
    Provides a detailed description of a note.

    :attr str short_description: A one sentence description of your note.
    :attr str long_description: A more detailed description of your note.
    :attr str kind: The type of note. Use this field to filter notes and occurences
          by kind.
           - FINDING&#58; The note and occurrence represent a finding.
           - KPI&#58; The note and occurrence represent a KPI value.
           - CARD&#58; The note represents a card showing findings and related metric
          values.
           - CARD_CONFIGURED&#58; The note represents a card configured for a user
          account.
           - SECTION&#58; The note represents a section in a dashboard.
    :attr List[ApiNoteRelatedUrl] related_url: (optional)
    :attr datetime create_time: (optional) Output only. The time this note was
          created. This field can be used as a filter in list requests.
    :attr datetime update_time: (optional) Output only. The time this note was last
          updated. This field can be used as a filter in list requests.
    :attr str id: The ID of the note.
    :attr bool shared: (optional) True if this note can be shared by multiple
          accounts.
    :attr Reporter reported_by: The entity reporting a note.
    :attr FindingType finding: (optional) FindingType provides details about a
          finding note.
    :attr KpiType kpi: (optional) KpiType provides details about a KPI note.
    :attr Card card: (optional) Card provides details about a card kind of note.
    :attr Section section: (optional) Card provides details about a card kind of
          note.
    """

    def __init__(self,
                 short_description: str,
                 long_description: str,
                 kind: str,
                 id: str,
                 reported_by: 'Reporter',
                 *,
                 related_url: List['ApiNoteRelatedUrl'] = None,
                 create_time: datetime = None,
                 update_time: datetime = None,
                 shared: bool = None,
                 finding: 'FindingType' = None,
                 kpi: 'KpiType' = None,
                 card: 'Card' = None,
                 section: 'Section' = None) -> None:
        """
        Initialize a ApiNote object.

        :param str short_description: A one sentence description of your note.
        :param str long_description: A more detailed description of your note.
        :param str kind: The type of note. Use this field to filter notes and
               occurences by kind.
                - FINDING&#58; The note and occurrence represent a finding.
                - KPI&#58; The note and occurrence represent a KPI value.
                - CARD&#58; The note represents a card showing findings and related metric
               values.
                - CARD_CONFIGURED&#58; The note represents a card configured for a user
               account.
                - SECTION&#58; The note represents a section in a dashboard.
        :param str id: The ID of the note.
        :param Reporter reported_by: The entity reporting a note.
        :param List[ApiNoteRelatedUrl] related_url: (optional)
        :param datetime create_time: (optional) Output only. The time this note was
               created. This field can be used as a filter in list requests.
        :param datetime update_time: (optional) Output only. The time this note was
               last updated. This field can be used as a filter in list requests.
        :param bool shared: (optional) True if this note can be shared by multiple
               accounts.
        :param FindingType finding: (optional) FindingType provides details about a
               finding note.
        :param KpiType kpi: (optional) KpiType provides details about a KPI note.
        :param Card card: (optional) Card provides details about a card kind of
               note.
        :param Section section: (optional) Card provides details about a card kind
               of note.
        """
        self.short_description = short_description
        self.long_description = long_description
        self.kind = kind
        self.related_url = related_url
        self.create_time = create_time
        self.update_time = update_time
        self.id = id
        self.shared = shared
        self.reported_by = reported_by
        self.finding = finding
        self.kpi = kpi
        self.card = card
        self.section = section

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiNote':
        """Initialize a ApiNote object from a json dictionary."""
        args = {}
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        else:
            raise ValueError('Required property \'short_description\' not present in ApiNote JSON')
        if 'long_description' in _dict:
            args['long_description'] = _dict.get('long_description')
        else:
            raise ValueError('Required property \'long_description\' not present in ApiNote JSON')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in ApiNote JSON')
        if 'related_url' in _dict:
            args['related_url'] = [ApiNoteRelatedUrl.from_dict(x) for x in _dict.get('related_url')]
        if 'create_time' in _dict:
            args['create_time'] = string_to_datetime(_dict.get('create_time'))
        if 'update_time' in _dict:
            args['update_time'] = string_to_datetime(_dict.get('update_time'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiNote JSON')
        if 'shared' in _dict:
            args['shared'] = _dict.get('shared')
        if 'reported_by' in _dict:
            args['reported_by'] = Reporter.from_dict(_dict.get('reported_by'))
        else:
            raise ValueError('Required property \'reported_by\' not present in ApiNote JSON')
        if 'finding' in _dict:
            args['finding'] = FindingType.from_dict(_dict.get('finding'))
        if 'kpi' in _dict:
            args['kpi'] = KpiType.from_dict(_dict.get('kpi'))
        if 'card' in _dict:
            args['card'] = Card.from_dict(_dict.get('card'))
        if 'section' in _dict:
            args['section'] = Section.from_dict(_dict.get('section'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiNote object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        if hasattr(self, 'long_description') and self.long_description is not None:
            _dict['long_description'] = self.long_description
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'related_url') and self.related_url is not None:
            _dict['related_url'] = [x.to_dict() for x in self.related_url]
        if hasattr(self, 'create_time') and self.create_time is not None:
            _dict['create_time'] = datetime_to_string(self.create_time)
        if hasattr(self, 'update_time') and self.update_time is not None:
            _dict['update_time'] = datetime_to_string(self.update_time)
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'shared') and self.shared is not None:
            _dict['shared'] = self.shared
        if hasattr(self, 'reported_by') and self.reported_by is not None:
            _dict['reported_by'] = self.reported_by.to_dict()
        if hasattr(self, 'finding') and self.finding is not None:
            _dict['finding'] = self.finding.to_dict()
        if hasattr(self, 'kpi') and self.kpi is not None:
            _dict['kpi'] = self.kpi.to_dict()
        if hasattr(self, 'card') and self.card is not None:
            _dict['card'] = self.card.to_dict()
        if hasattr(self, 'section') and self.section is not None:
            _dict['section'] = self.section.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiNote object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiNote') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiNote') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        The type of note. Use this field to filter notes and occurences by kind.
         - FINDING&#58; The note and occurrence represent a finding.
         - KPI&#58; The note and occurrence represent a KPI value.
         - CARD&#58; The note represents a card showing findings and related metric
        values.
         - CARD_CONFIGURED&#58; The note represents a card configured for a user account.
         - SECTION&#58; The note represents a section in a dashboard.
        """
        FINDING = 'FINDING'
        KPI = 'KPI'
        CARD = 'CARD'
        CARD_CONFIGURED = 'CARD_CONFIGURED'
        SECTION = 'SECTION'


class ApiNoteRelatedUrl():
    """
    Metadata for any related URL information.

    :attr str label: Label to describe usage of the URL.
    :attr str url: The URL that you want to associate with the note.
    """

    def __init__(self,
                 label: str,
                 url: str) -> None:
        """
        Initialize a ApiNoteRelatedUrl object.

        :param str label: Label to describe usage of the URL.
        :param str url: The URL that you want to associate with the note.
        """
        self.label = label
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiNoteRelatedUrl':
        """Initialize a ApiNoteRelatedUrl object from a json dictionary."""
        args = {}
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        else:
            raise ValueError('Required property \'label\' not present in ApiNoteRelatedUrl JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in ApiNoteRelatedUrl JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiNoteRelatedUrl object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiNoteRelatedUrl object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiNoteRelatedUrl') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiNoteRelatedUrl') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApiOccurrence():
    """
    `Occurrence` includes information about analysis occurrences for an image.

    :attr str resource_url: (optional) The unique URL of the resource, image or the
          container, for which the `Occurrence` applies. For example,
          https://gcr.io/provider/image@sha256:foo. This field can be used as a filter in
          list requests.
    :attr str note_name: An analysis note associated with this image, in the form
          "{account_id}/providers/{provider_id}/notes/{note_id}" This field can be used as
          a filter in list requests.
    :attr str kind: The type of note. Use this field to filter notes and occurences
          by kind.
           - FINDING&#58; The note and occurrence represent a finding.
           - KPI&#58; The note and occurrence represent a KPI value.
           - CARD&#58; The note represents a card showing findings and related metric
          values.
           - CARD_CONFIGURED&#58; The note represents a card configured for a user
          account.
           - SECTION&#58; The note represents a section in a dashboard.
    :attr str remediation: (optional) A description of actions that can be taken to
          remedy the `Note`.
    :attr datetime create_time: (optional) Output only. The time this `Occurrence`
          was created.
    :attr datetime update_time: (optional) Output only. The time this `Occurrence`
          was last updated.
    :attr str id: The id of the occurrence.
    :attr Context context: (optional)
    :attr Finding finding: (optional) Finding provides details about a finding
          occurrence.
    :attr Kpi kpi: (optional) Kpi provides details about a KPI occurrence.
    :attr object reference_data: (optional) Additional data for the finding, like AT
          event etc.
    """

    def __init__(self,
                 note_name: str,
                 kind: str,
                 id: str,
                 *,
                 resource_url: str = None,
                 remediation: str = None,
                 create_time: datetime = None,
                 update_time: datetime = None,
                 context: 'Context' = None,
                 finding: 'Finding' = None,
                 kpi: 'Kpi' = None,
                 reference_data: object = None) -> None:
        """
        Initialize a ApiOccurrence object.

        :param str note_name: An analysis note associated with this image, in the
               form "{account_id}/providers/{provider_id}/notes/{note_id}" This field can
               be used as a filter in list requests.
        :param str kind: The type of note. Use this field to filter notes and
               occurences by kind.
                - FINDING&#58; The note and occurrence represent a finding.
                - KPI&#58; The note and occurrence represent a KPI value.
                - CARD&#58; The note represents a card showing findings and related metric
               values.
                - CARD_CONFIGURED&#58; The note represents a card configured for a user
               account.
                - SECTION&#58; The note represents a section in a dashboard.
        :param str id: The id of the occurrence.
        :param str resource_url: (optional) The unique URL of the resource, image
               or the container, for which the `Occurrence` applies. For example,
               https://gcr.io/provider/image@sha256:foo. This field can be used as a
               filter in list requests.
        :param str remediation: (optional) A description of actions that can be
               taken to remedy the `Note`.
        :param Context context: (optional)
        :param Finding finding: (optional) Finding provides details about a finding
               occurrence.
        :param Kpi kpi: (optional) Kpi provides details about a KPI occurrence.
        :param object reference_data: (optional) Additional data for the finding,
               like AT event etc.
        """
        self.resource_url = resource_url
        self.note_name = note_name
        self.kind = kind
        self.remediation = remediation
        self.create_time = create_time
        self.update_time = update_time
        self.id = id
        self.context = context
        self.finding = finding
        self.kpi = kpi
        self.reference_data = reference_data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiOccurrence':
        """Initialize a ApiOccurrence object from a json dictionary."""
        args = {}
        if 'resource_url' in _dict:
            args['resource_url'] = _dict.get('resource_url')
        if 'note_name' in _dict:
            args['note_name'] = _dict.get('note_name')
        else:
            raise ValueError('Required property \'note_name\' not present in ApiOccurrence JSON')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in ApiOccurrence JSON')
        if 'remediation' in _dict:
            args['remediation'] = _dict.get('remediation')
        if 'create_time' in _dict:
            args['create_time'] = string_to_datetime(_dict.get('create_time'))
        if 'update_time' in _dict:
            args['update_time'] = string_to_datetime(_dict.get('update_time'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiOccurrence JSON')
        if 'context' in _dict:
            args['context'] = Context.from_dict(_dict.get('context'))
        if 'finding' in _dict:
            args['finding'] = Finding.from_dict(_dict.get('finding'))
        if 'kpi' in _dict:
            args['kpi'] = Kpi.from_dict(_dict.get('kpi'))
        if 'reference_data' in _dict:
            args['reference_data'] = _dict.get('reference_data')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiOccurrence object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_url') and self.resource_url is not None:
            _dict['resource_url'] = self.resource_url
        if hasattr(self, 'note_name') and self.note_name is not None:
            _dict['note_name'] = self.note_name
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'remediation') and self.remediation is not None:
            _dict['remediation'] = self.remediation
        if hasattr(self, 'create_time') and getattr(self, 'create_time') is not None:
            _dict['create_time'] = datetime_to_string(getattr(self, 'create_time'))
        if hasattr(self, 'update_time') and getattr(self, 'update_time') is not None:
            _dict['update_time'] = datetime_to_string(getattr(self, 'update_time'))
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context.to_dict()
        if hasattr(self, 'finding') and self.finding is not None:
            _dict['finding'] = self.finding.to_dict()
        if hasattr(self, 'kpi') and self.kpi is not None:
            _dict['kpi'] = self.kpi.to_dict()
        if hasattr(self, 'reference_data') and self.reference_data is not None:
            _dict['reference_data'] = self.reference_data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiOccurrence object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiOccurrence') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiOccurrence') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        The type of note. Use this field to filter notes and occurences by kind.
         - FINDING&#58; The note and occurrence represent a finding.
         - KPI&#58; The note and occurrence represent a KPI value.
         - CARD&#58; The note represents a card showing findings and related metric
        values.
         - CARD_CONFIGURED&#58; The note represents a card configured for a user account.
         - SECTION&#58; The note represents a section in a dashboard.
        """
        FINDING = 'FINDING'
        KPI = 'KPI'
        CARD = 'CARD'
        CARD_CONFIGURED = 'CARD_CONFIGURED'
        SECTION = 'SECTION'


class ApiProvider():
    """
    Provides a detailed description of a provider.

    :attr str name: The name of the provider in the form
          '{account_id}/providers/{provider_id}'.
    :attr str id: The ID of the provider.
    """

    def __init__(self,
                 name: str,
                 id: str) -> None:
        """
        Initialize a ApiProvider object.

        :param str name: The name of the provider in the form
               '{account_id}/providers/{provider_id}'.
        :param str id: The ID of the provider.
        """
        self.name = name
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApiProvider':
        """Initialize a ApiProvider object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ApiProvider JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ApiProvider JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApiProvider object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApiProvider object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApiProvider') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApiProvider') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CardElementBreakdownCardElement(CardElement):
    """
    A card element with a breakdown of values.

    :attr str text: The text of this card element.
    :attr str kind: Kind of element
          - NUMERIC&#58; Single numeric value
          - BREAKDOWN&#58; Breakdown of numeric values
          - TIME_SERIES&#58; Time-series of numeric values.
    :attr str default_time_range: (optional) The default time range of this card
          element.
    :attr List[ValueType] value_types: the value types associated to this card
          element.
    """

    def __init__(self,
                 text: str,
                 kind: str,
                 value_types: List['ValueType'],
                 *,
                 default_time_range: str = None) -> None:
        """
        Initialize a CardElementBreakdownCardElement object.

        :param str text: The text of this card element.
        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param List[ValueType] value_types: the value types associated to this card
               element.
        :param str default_time_range: (optional) The default time range of this
               card element.
        """
        # pylint: disable=super-init-not-called
        self.text = text
        self.kind = kind
        self.default_time_range = default_time_range
        self.value_types = value_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CardElementBreakdownCardElement':
        """Initialize a CardElementBreakdownCardElement object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in CardElementBreakdownCardElement JSON')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in CardElementBreakdownCardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        if 'value_types' in _dict:
            args['value_types'] = [ValueType.from_dict(x) for x in _dict.get('value_types')]
        else:
            raise ValueError('Required property \'value_types\' not present in CardElementBreakdownCardElement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CardElementBreakdownCardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        if hasattr(self, 'value_types') and self.value_types is not None:
            _dict['value_types'] = [x.to_dict() for x in self.value_types]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CardElementBreakdownCardElement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CardElementBreakdownCardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CardElementBreakdownCardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = 'NUMERIC'
        BREAKDOWN = 'BREAKDOWN'
        TIME_SERIES = 'TIME_SERIES'


class CardElementNumericCardElement(CardElement):
    """
    A card element with a single numeric value".

    :attr str text: The text of this card element.
    :attr str kind: Kind of element
          - NUMERIC&#58; Single numeric value
          - BREAKDOWN&#58; Breakdown of numeric values
          - TIME_SERIES&#58; Time-series of numeric values.
    :attr str default_time_range: (optional) The default time range of this card
          element.
    :attr NumericCardElementValueType value_type:
    """

    def __init__(self,
                 text: str,
                 kind: str,
                 value_type: 'NumericCardElementValueType',
                 *,
                 default_time_range: str = None) -> None:
        """
        Initialize a CardElementNumericCardElement object.

        :param str text: The text of this card element.
        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param NumericCardElementValueType value_type:
        :param str default_time_range: (optional) The default time range of this
               card element.
        """
        # pylint: disable=super-init-not-called
        self.text = text
        self.kind = kind
        self.default_time_range = default_time_range
        self.value_type = value_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CardElementNumericCardElement':
        """Initialize a CardElementNumericCardElement object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in CardElementNumericCardElement JSON')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in CardElementNumericCardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        if 'value_type' in _dict:
            args['value_type'] = NumericCardElementValueType.from_dict(_dict.get('value_type'))
        else:
            raise ValueError('Required property \'value_type\' not present in CardElementNumericCardElement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CardElementNumericCardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        if hasattr(self, 'value_type') and self.value_type is not None:
            _dict['value_type'] = self.value_type.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CardElementNumericCardElement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CardElementNumericCardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CardElementNumericCardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = 'NUMERIC'
        BREAKDOWN = 'BREAKDOWN'
        TIME_SERIES = 'TIME_SERIES'


class CardElementTimeSeriesCardElement(CardElement):
    """
    A card element with a time series chart.

    :attr str text: The text of this card element.
    :attr str default_interval: (optional) The default interval of the time series.
    :attr str kind: Kind of element
          - NUMERIC&#58; Single numeric value
          - BREAKDOWN&#58; Breakdown of numeric values
          - TIME_SERIES&#58; Time-series of numeric values.
    :attr str default_time_range: (optional) The default time range of this card
          element.
    :attr List[ValueType] value_types: the value types associated to this card
          element.
    """

    def __init__(self,
                 text: str,
                 kind: str,
                 value_types: List['ValueType'],
                 *,
                 default_interval: str = None,
                 default_time_range: str = None) -> None:
        """
        Initialize a CardElementTimeSeriesCardElement object.

        :param str text: The text of this card element.
        :param str kind: Kind of element
               - NUMERIC&#58; Single numeric value
               - BREAKDOWN&#58; Breakdown of numeric values
               - TIME_SERIES&#58; Time-series of numeric values.
        :param List[ValueType] value_types: the value types associated to this card
               element.
        :param str default_interval: (optional) The default interval of the time
               series.
        :param str default_time_range: (optional) The default time range of this
               card element.
        """
        # pylint: disable=super-init-not-called
        self.text = text
        self.default_interval = default_interval
        self.kind = kind
        self.default_time_range = default_time_range
        self.value_types = value_types

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CardElementTimeSeriesCardElement':
        """Initialize a CardElementTimeSeriesCardElement object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in CardElementTimeSeriesCardElement JSON')
        if 'default_interval' in _dict:
            args['default_interval'] = _dict.get('default_interval')
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in CardElementTimeSeriesCardElement JSON')
        if 'default_time_range' in _dict:
            args['default_time_range'] = _dict.get('default_time_range')
        if 'value_types' in _dict:
            args['value_types'] = [ValueType.from_dict(x) for x in _dict.get('value_types')]
        else:
            raise ValueError('Required property \'value_types\' not present in CardElementTimeSeriesCardElement JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CardElementTimeSeriesCardElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'default_interval') and self.default_interval is not None:
            _dict['default_interval'] = self.default_interval
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'default_time_range') and self.default_time_range is not None:
            _dict['default_time_range'] = self.default_time_range
        if hasattr(self, 'value_types') and self.value_types is not None:
            _dict['value_types'] = [x.to_dict() for x in self.value_types]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CardElementTimeSeriesCardElement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CardElementTimeSeriesCardElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CardElementTimeSeriesCardElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        Kind of element
        - NUMERIC&#58; Single numeric value
        - BREAKDOWN&#58; Breakdown of numeric values
        - TIME_SERIES&#58; Time-series of numeric values.
        """
        NUMERIC = 'NUMERIC'
        BREAKDOWN = 'BREAKDOWN'
        TIME_SERIES = 'TIME_SERIES'


class NumericCardElementValueType(ValueType):
    """
    NumericCardElementValueType.

    """

    def __init__(self) -> None:
        """
        Initialize a NumericCardElementValueType object.

        """
        # pylint: disable=super-init-not-called

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NumericCardElementValueType':
        """Initialize a NumericCardElementValueType object from a json dictionary."""
        return cls(**_dict)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NumericCardElementValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        return vars(self)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NumericCardElementValueType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NumericCardElementValueType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NumericCardElementValueType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ValueTypeFindingCountValueType(ValueType):
    """
    ValueTypeFindingCountValueType.

    :attr str kind: Kind of element - FINDING_COUNT&#58; Kind of value derived from
          a count of finding occurrences.
    :attr List[str] finding_note_names: the names of the finding note associated
          that act as filters for counting the occurrences.
    :attr str text: The text of this element type.
    """

    def __init__(self,
                 kind: str,
                 finding_note_names: List[str],
                 text: str) -> None:
        """
        Initialize a ValueTypeFindingCountValueType object.

        :param str kind: Kind of element - FINDING_COUNT&#58; Kind of value derived
               from a count of finding occurrences.
        :param List[str] finding_note_names: the names of the finding note
               associated that act as filters for counting the occurrences.
        :param str text: The text of this element type.
        """
        # pylint: disable=super-init-not-called
        self.kind = kind
        self.finding_note_names = finding_note_names
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValueTypeFindingCountValueType':
        """Initialize a ValueTypeFindingCountValueType object from a json dictionary."""
        args = {}
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in ValueTypeFindingCountValueType JSON')
        if 'finding_note_names' in _dict:
            args['finding_note_names'] = _dict.get('finding_note_names')
        else:
            raise ValueError('Required property \'finding_note_names\' not present in ValueTypeFindingCountValueType JSON')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ValueTypeFindingCountValueType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueTypeFindingCountValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'finding_note_names') and self.finding_note_names is not None:
            _dict['finding_note_names'] = self.finding_note_names
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ValueTypeFindingCountValueType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ValueTypeFindingCountValueType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValueTypeFindingCountValueType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        Kind of element - FINDING_COUNT&#58; Kind of value derived from a count of finding
        occurrences.
        """
        FINDING_COUNT = 'FINDING_COUNT'


class ValueTypeKpiValueType(ValueType):
    """
    ValueTypeKpiValueType.

    :attr str kind: Kind of element
          - KPI&#58; Kind of value derived from a KPI occurrence.
    :attr str kpi_note_name: The name of the kpi note associated to the occurrence
          with the value for this card element value type.
    :attr str text: The text of this element type.
    """

    def __init__(self,
                 kind: str,
                 kpi_note_name: str,
                 text: str) -> None:
        """
        Initialize a ValueTypeKpiValueType object.

        :param str kind: Kind of element
               - KPI&#58; Kind of value derived from a KPI occurrence.
        :param str kpi_note_name: The name of the kpi note associated to the
               occurrence with the value for this card element value type.
        :param str text: The text of this element type.
        """
        # pylint: disable=super-init-not-called
        self.kind = kind
        self.kpi_note_name = kpi_note_name
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValueTypeKpiValueType':
        """Initialize a ValueTypeKpiValueType object from a json dictionary."""
        args = {}
        if 'kind' in _dict:
            args['kind'] = _dict.get('kind')
        else:
            raise ValueError('Required property \'kind\' not present in ValueTypeKpiValueType JSON')
        if 'kpi_note_name' in _dict:
            args['kpi_note_name'] = _dict.get('kpi_note_name')
        else:
            raise ValueError('Required property \'kpi_note_name\' not present in ValueTypeKpiValueType JSON')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ValueTypeKpiValueType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueTypeKpiValueType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'kpi_note_name') and self.kpi_note_name is not None:
            _dict['kpi_note_name'] = self.kpi_note_name
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ValueTypeKpiValueType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ValueTypeKpiValueType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValueTypeKpiValueType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        Kind of element
        - KPI&#58; Kind of value derived from a KPI occurrence.
        """
        KPI = 'KPI'

