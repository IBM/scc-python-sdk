# -*- coding: utf-8 -*-
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

"""
Unit Tests for FindingsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_scc.findings_v1 import *

account_id = 'testString'

_service = FindingsV1(
    authenticator=NoAuthAuthenticator(),
    account_id=account_id
    )

_base_url = 'https://us-south.secadvisor.cloud.ibm.com/findings'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: FindingsGraph
##############################################################################
# region

class TestPostGraph():
    """
    Test Class for post_graph
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_graph_all_params(self):
        """
        post_graph()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/graph')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        body = 'testString'
        content_type = 'application/json'
        transaction_id = 'testString'

        # Invoke method
        response = _service.post_graph(
            body,
            content_type=content_type,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params


    @responses.activate
    def test_post_graph_required_params(self):
        """
        test_post_graph_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/graph')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        body = 'testString'

        # Invoke method
        response = _service.post_graph(
            body,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params


    @responses.activate
    def test_post_graph_value_error(self):
        """
        test_post_graph_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/graph')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        body = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.post_graph(**req_copy)



# endregion
##############################################################################
# End of Service: FindingsGraph
##############################################################################

##############################################################################
# Start of Service: FindingsNotes
##############################################################################
# region

class TestCreateNote():
    """
    Test Class for create_note
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_note_all_params(self):
        """
        create_note()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Reporter model
        reporter_model = {}
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {}
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a FindingType model
        finding_type_model = {}
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        # Construct a dict representation of a KpiType model
        kpi_type_model = {}
        kpi_type_model['aggregation_type'] = 'SUM'

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {}
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {}
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a dict representation of a Card model
        card_model = {}
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        # Construct a dict representation of a Section model
        section_model = {}
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Set up parameter values
        provider_id = 'testString'
        short_description = 'testString'
        long_description = 'testString'
        kind = 'FINDING'
        id = 'testString'
        reported_by = reporter_model
        related_url = [api_note_related_url_model]
        expiration_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        shared = True
        finding = finding_type_model
        kpi = kpi_type_model
        card = card_model
        section = section_model
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_note(
            provider_id,
            short_description,
            long_description,
            kind,
            id,
            reported_by,
            related_url=related_url,
            expiration_time=expiration_time,
            shared=shared,
            finding=finding,
            kpi=kpi,
            card=card,
            section=section,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['short_description'] == 'testString'
        assert req_body['long_description'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['reported_by'] == reporter_model
        assert req_body['related_url'] == [api_note_related_url_model]
        assert req_body['expiration_time'] == "2019-01-01T12:00:00Z"
        assert req_body['shared'] == True
        assert req_body['finding'] == finding_type_model
        assert req_body['kpi'] == kpi_type_model
        assert req_body['card'] == card_model
        assert req_body['section'] == section_model


    @responses.activate
    def test_create_note_required_params(self):
        """
        test_create_note_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Reporter model
        reporter_model = {}
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {}
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a FindingType model
        finding_type_model = {}
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        # Construct a dict representation of a KpiType model
        kpi_type_model = {}
        kpi_type_model['aggregation_type'] = 'SUM'

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {}
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {}
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a dict representation of a Card model
        card_model = {}
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        # Construct a dict representation of a Section model
        section_model = {}
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Set up parameter values
        provider_id = 'testString'
        short_description = 'testString'
        long_description = 'testString'
        kind = 'FINDING'
        id = 'testString'
        reported_by = reporter_model
        related_url = [api_note_related_url_model]
        expiration_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        shared = True
        finding = finding_type_model
        kpi = kpi_type_model
        card = card_model
        section = section_model

        # Invoke method
        response = _service.create_note(
            provider_id,
            short_description,
            long_description,
            kind,
            id,
            reported_by,
            related_url=related_url,
            expiration_time=expiration_time,
            shared=shared,
            finding=finding,
            kpi=kpi,
            card=card,
            section=section,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['short_description'] == 'testString'
        assert req_body['long_description'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['reported_by'] == reporter_model
        assert req_body['related_url'] == [api_note_related_url_model]
        assert req_body['expiration_time'] == "2019-01-01T12:00:00Z"
        assert req_body['shared'] == True
        assert req_body['finding'] == finding_type_model
        assert req_body['kpi'] == kpi_type_model
        assert req_body['card'] == card_model
        assert req_body['section'] == section_model


    @responses.activate
    def test_create_note_value_error(self):
        """
        test_create_note_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Reporter model
        reporter_model = {}
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {}
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a FindingType model
        finding_type_model = {}
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        # Construct a dict representation of a KpiType model
        kpi_type_model = {}
        kpi_type_model['aggregation_type'] = 'SUM'

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {}
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {}
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a dict representation of a Card model
        card_model = {}
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        # Construct a dict representation of a Section model
        section_model = {}
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Set up parameter values
        provider_id = 'testString'
        short_description = 'testString'
        long_description = 'testString'
        kind = 'FINDING'
        id = 'testString'
        reported_by = reporter_model
        related_url = [api_note_related_url_model]
        expiration_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        shared = True
        finding = finding_type_model
        kpi = kpi_type_model
        card = card_model
        section = section_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "short_description": short_description,
            "long_description": long_description,
            "kind": kind,
            "id": id,
            "reported_by": reported_by,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_note(**req_copy)



class TestListNotes():
    """
    Test Class for list_notes
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_notes_all_params(self):
        """
        list_notes()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes')
        mock_response = '{"notes": [{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        transaction_id = 'testString'
        page_size = 2
        page_token = 'testString'

        # Invoke method
        response = _service.list_notes(
            provider_id,
            transaction_id=transaction_id,
            page_size=page_size,
            page_token=page_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_size={}'.format(page_size) in query_string
        assert 'page_token={}'.format(page_token) in query_string


    @responses.activate
    def test_list_notes_required_params(self):
        """
        test_list_notes_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes')
        mock_response = '{"notes": [{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'

        # Invoke method
        response = _service.list_notes(
            provider_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_notes_value_error(self):
        """
        test_list_notes_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes')
        mock_response = '{"notes": [{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_notes(**req_copy)



class TestGetNote():
    """
    Test Class for get_note
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_note_all_params(self):
        """
        get_note()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_note(
            provider_id,
            note_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_note_required_params(self):
        """
        test_get_note_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'

        # Invoke method
        response = _service.get_note(
            provider_id,
            note_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_note_value_error(self):
        """
        test_get_note_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "note_id": note_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_note(**req_copy)



class TestUpdateNote():
    """
    Test Class for update_note
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_note_all_params(self):
        """
        update_note()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Reporter model
        reporter_model = {}
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {}
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a FindingType model
        finding_type_model = {}
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        # Construct a dict representation of a KpiType model
        kpi_type_model = {}
        kpi_type_model['aggregation_type'] = 'SUM'

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {}
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {}
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a dict representation of a Card model
        card_model = {}
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        # Construct a dict representation of a Section model
        section_model = {}
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'
        short_description = 'testString'
        long_description = 'testString'
        kind = 'FINDING'
        id = 'testString'
        reported_by = reporter_model
        related_url = [api_note_related_url_model]
        expiration_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        shared = True
        finding = finding_type_model
        kpi = kpi_type_model
        card = card_model
        section = section_model
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_note(
            provider_id,
            note_id,
            short_description,
            long_description,
            kind,
            id,
            reported_by,
            related_url=related_url,
            expiration_time=expiration_time,
            shared=shared,
            finding=finding,
            kpi=kpi,
            card=card,
            section=section,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['short_description'] == 'testString'
        assert req_body['long_description'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['reported_by'] == reporter_model
        assert req_body['related_url'] == [api_note_related_url_model]
        assert req_body['expiration_time'] == "2019-01-01T12:00:00Z"
        assert req_body['shared'] == True
        assert req_body['finding'] == finding_type_model
        assert req_body['kpi'] == kpi_type_model
        assert req_body['card'] == card_model
        assert req_body['section'] == section_model


    @responses.activate
    def test_update_note_required_params(self):
        """
        test_update_note_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Reporter model
        reporter_model = {}
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {}
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a FindingType model
        finding_type_model = {}
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        # Construct a dict representation of a KpiType model
        kpi_type_model = {}
        kpi_type_model['aggregation_type'] = 'SUM'

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {}
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {}
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a dict representation of a Card model
        card_model = {}
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        # Construct a dict representation of a Section model
        section_model = {}
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'
        short_description = 'testString'
        long_description = 'testString'
        kind = 'FINDING'
        id = 'testString'
        reported_by = reporter_model
        related_url = [api_note_related_url_model]
        expiration_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        shared = True
        finding = finding_type_model
        kpi = kpi_type_model
        card = card_model
        section = section_model

        # Invoke method
        response = _service.update_note(
            provider_id,
            note_id,
            short_description,
            long_description,
            kind,
            id,
            reported_by,
            related_url=related_url,
            expiration_time=expiration_time,
            shared=shared,
            finding=finding,
            kpi=kpi,
            card=card,
            section=section,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['short_description'] == 'testString'
        assert req_body['long_description'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['reported_by'] == reporter_model
        assert req_body['related_url'] == [api_note_related_url_model]
        assert req_body['expiration_time'] == "2019-01-01T12:00:00Z"
        assert req_body['shared'] == True
        assert req_body['finding'] == finding_type_model
        assert req_body['kpi'] == kpi_type_model
        assert req_body['card'] == card_model
        assert req_body['section'] == section_model


    @responses.activate
    def test_update_note_value_error(self):
        """
        test_update_note_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Reporter model
        reporter_model = {}
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {}
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a FindingType model
        finding_type_model = {}
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        # Construct a dict representation of a KpiType model
        kpi_type_model = {}
        kpi_type_model['aggregation_type'] = 'SUM'

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {}
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {}
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a dict representation of a Card model
        card_model = {}
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        # Construct a dict representation of a Section model
        section_model = {}
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'
        short_description = 'testString'
        long_description = 'testString'
        kind = 'FINDING'
        id = 'testString'
        reported_by = reporter_model
        related_url = [api_note_related_url_model]
        expiration_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        shared = True
        finding = finding_type_model
        kpi = kpi_type_model
        card = card_model
        section = section_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "note_id": note_id,
            "short_description": short_description,
            "long_description": long_description,
            "kind": kind,
            "id": id,
            "reported_by": reported_by,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_note(**req_copy)



class TestDeleteNote():
    """
    Test Class for delete_note
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_note_all_params(self):
        """
        delete_note()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_note(
            provider_id,
            note_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_note_required_params(self):
        """
        test_delete_note_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'

        # Invoke method
        response = _service.delete_note(
            provider_id,
            note_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_note_value_error(self):
        """
        test_delete_note_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "note_id": note_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_note(**req_copy)



class TestGetOccurrenceNote():
    """
    Test Class for get_occurrence_note
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_occurrence_note_all_params(self):
        """
        get_occurrence_note()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString/note')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_occurrence_note(
            provider_id,
            occurrence_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_occurrence_note_required_params(self):
        """
        test_get_occurrence_note_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString/note')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'

        # Invoke method
        response = _service.get_occurrence_note(
            provider_id,
            occurrence_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_occurrence_note_value_error(self):
        """
        test_get_occurrence_note_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString/note')
        mock_response = '{"short_description": "short_description", "long_description": "long_description", "kind": "FINDING", "related_url": [{"label": "label", "url": "url"}], "expiration_time": "2019-01-01T12:00:00.000Z", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "shared": true, "reported_by": {"id": "id", "title": "title", "url": "url"}, "finding": {"severity": "LOW", "next_steps": [{"title": "title", "url": "url"}]}, "kpi": {"aggregation_type": "SUM"}, "card": {"section": "section", "title": "title", "subtitle": "subtitle", "order": 1, "finding_note_names": ["finding_note_names"], "requires_configuration": true, "badge_text": "badge_text", "badge_image": "badge_image", "elements": [{"text": "text", "default_interval": "default_interval", "kind": "TIME_SERIES", "default_time_range": "1d", "value_types": [{"kind": "FINDING_COUNT", "finding_note_names": ["finding_note_names"], "text": "text"}]}]}, "section": {"title": "title", "image": "image"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "occurrence_id": occurrence_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_occurrence_note(**req_copy)



# endregion
##############################################################################
# End of Service: FindingsNotes
##############################################################################

##############################################################################
# Start of Service: FindingsOccurrences
##############################################################################
# region

class TestCreateOccurrence():
    """
    Test Class for create_occurrence
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_occurrence_all_params(self):
        """
        create_occurrence()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences')
        mock_response = '{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {}
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {}
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {}
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a dict representation of a Finding model
        finding_model = {}
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        # Construct a dict representation of a Kpi model
        kpi_model = {}
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Set up parameter values
        provider_id = 'testString'
        note_name = 'testString'
        kind = 'FINDING'
        id = 'testString'
        resource_url = 'testString'
        remediation = 'testString'
        context = context_model
        finding = finding_model
        kpi = kpi_model
        reference_data = { 'foo': 'bar' }
        replace_if_exists = True
        transaction_id = 'testString'

        # Invoke method
        response = _service.create_occurrence(
            provider_id,
            note_name,
            kind,
            id,
            resource_url=resource_url,
            remediation=remediation,
            context=context,
            finding=finding,
            kpi=kpi,
            reference_data=reference_data,
            replace_if_exists=replace_if_exists,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['note_name'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['resource_url'] == 'testString'
        assert req_body['remediation'] == 'testString'
        assert req_body['context'] == context_model
        assert req_body['finding'] == finding_model
        assert req_body['kpi'] == kpi_model
        assert req_body['reference_data'] == { 'foo': 'bar' }


    @responses.activate
    def test_create_occurrence_required_params(self):
        """
        test_create_occurrence_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences')
        mock_response = '{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {}
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {}
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {}
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a dict representation of a Finding model
        finding_model = {}
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        # Construct a dict representation of a Kpi model
        kpi_model = {}
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Set up parameter values
        provider_id = 'testString'
        note_name = 'testString'
        kind = 'FINDING'
        id = 'testString'
        resource_url = 'testString'
        remediation = 'testString'
        context = context_model
        finding = finding_model
        kpi = kpi_model
        reference_data = { 'foo': 'bar' }

        # Invoke method
        response = _service.create_occurrence(
            provider_id,
            note_name,
            kind,
            id,
            resource_url=resource_url,
            remediation=remediation,
            context=context,
            finding=finding,
            kpi=kpi,
            reference_data=reference_data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['note_name'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['resource_url'] == 'testString'
        assert req_body['remediation'] == 'testString'
        assert req_body['context'] == context_model
        assert req_body['finding'] == finding_model
        assert req_body['kpi'] == kpi_model
        assert req_body['reference_data'] == { 'foo': 'bar' }


    @responses.activate
    def test_create_occurrence_value_error(self):
        """
        test_create_occurrence_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences')
        mock_response = '{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {}
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {}
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {}
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a dict representation of a Finding model
        finding_model = {}
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        # Construct a dict representation of a Kpi model
        kpi_model = {}
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Set up parameter values
        provider_id = 'testString'
        note_name = 'testString'
        kind = 'FINDING'
        id = 'testString'
        resource_url = 'testString'
        remediation = 'testString'
        context = context_model
        finding = finding_model
        kpi = kpi_model
        reference_data = { 'foo': 'bar' }

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "note_name": note_name,
            "kind": kind,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_occurrence(**req_copy)



class TestListOccurrences():
    """
    Test Class for list_occurrences
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_occurrences_all_params(self):
        """
        list_occurrences()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        transaction_id = 'testString'
        page_size = 2
        page_token = 'testString'

        # Invoke method
        response = _service.list_occurrences(
            provider_id,
            transaction_id=transaction_id,
            page_size=page_size,
            page_token=page_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_size={}'.format(page_size) in query_string
        assert 'page_token={}'.format(page_token) in query_string


    @responses.activate
    def test_list_occurrences_required_params(self):
        """
        test_list_occurrences_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'

        # Invoke method
        response = _service.list_occurrences(
            provider_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_occurrences_value_error(self):
        """
        test_list_occurrences_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_occurrences(**req_copy)



class TestListNoteOccurrences():
    """
    Test Class for list_note_occurrences
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_note_occurrences_all_params(self):
        """
        list_note_occurrences()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString/occurrences')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'
        transaction_id = 'testString'
        page_size = 2
        page_token = 'testString'

        # Invoke method
        response = _service.list_note_occurrences(
            provider_id,
            note_id,
            transaction_id=transaction_id,
            page_size=page_size,
            page_token=page_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_size={}'.format(page_size) in query_string
        assert 'page_token={}'.format(page_token) in query_string


    @responses.activate
    def test_list_note_occurrences_required_params(self):
        """
        test_list_note_occurrences_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString/occurrences')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'

        # Invoke method
        response = _service.list_note_occurrences(
            provider_id,
            note_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_note_occurrences_value_error(self):
        """
        test_list_note_occurrences_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/notes/testString/occurrences')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        note_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "note_id": note_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_note_occurrences(**req_copy)



class TestGetOccurrence():
    """
    Test Class for get_occurrence
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_occurrence_all_params(self):
        """
        get_occurrence()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_occurrence(
            provider_id,
            occurrence_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_occurrence_required_params(self):
        """
        test_get_occurrence_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'

        # Invoke method
        response = _service.get_occurrence(
            provider_id,
            occurrence_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_occurrence_value_error(self):
        """
        test_get_occurrence_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        mock_response = '{"occurrences": [{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}], "next_page_token": "next_page_token"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "occurrence_id": occurrence_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_occurrence(**req_copy)



class TestUpdateOccurrence():
    """
    Test Class for update_occurrence
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_occurrence_all_params(self):
        """
        update_occurrence()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        mock_response = '{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {}
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {}
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {}
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a dict representation of a Finding model
        finding_model = {}
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        # Construct a dict representation of a Kpi model
        kpi_model = {}
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'
        note_name = 'testString'
        kind = 'FINDING'
        id = 'testString'
        resource_url = 'testString'
        remediation = 'testString'
        context = context_model
        finding = finding_model
        kpi = kpi_model
        reference_data = { 'foo': 'bar' }
        transaction_id = 'testString'

        # Invoke method
        response = _service.update_occurrence(
            provider_id,
            occurrence_id,
            note_name,
            kind,
            id,
            resource_url=resource_url,
            remediation=remediation,
            context=context,
            finding=finding,
            kpi=kpi,
            reference_data=reference_data,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['note_name'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['resource_url'] == 'testString'
        assert req_body['remediation'] == 'testString'
        assert req_body['context'] == context_model
        assert req_body['finding'] == finding_model
        assert req_body['kpi'] == kpi_model
        assert req_body['reference_data'] == { 'foo': 'bar' }


    @responses.activate
    def test_update_occurrence_required_params(self):
        """
        test_update_occurrence_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        mock_response = '{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {}
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {}
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {}
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a dict representation of a Finding model
        finding_model = {}
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        # Construct a dict representation of a Kpi model
        kpi_model = {}
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'
        note_name = 'testString'
        kind = 'FINDING'
        id = 'testString'
        resource_url = 'testString'
        remediation = 'testString'
        context = context_model
        finding = finding_model
        kpi = kpi_model
        reference_data = { 'foo': 'bar' }

        # Invoke method
        response = _service.update_occurrence(
            provider_id,
            occurrence_id,
            note_name,
            kind,
            id,
            resource_url=resource_url,
            remediation=remediation,
            context=context,
            finding=finding,
            kpi=kpi,
            reference_data=reference_data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['note_name'] == 'testString'
        assert req_body['kind'] == 'FINDING'
        assert req_body['id'] == 'testString'
        assert req_body['resource_url'] == 'testString'
        assert req_body['remediation'] == 'testString'
        assert req_body['context'] == context_model
        assert req_body['finding'] == finding_model
        assert req_body['kpi'] == kpi_model
        assert req_body['reference_data'] == { 'foo': 'bar' }


    @responses.activate
    def test_update_occurrence_value_error(self):
        """
        test_update_occurrence_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        mock_response = '{"resource_url": "resource_url", "note_name": "note_name", "kind": "FINDING", "remediation": "remediation", "create_time": "2019-01-01T12:00:00.000Z", "update_time": "2019-01-01T12:00:00.000Z", "id": "id", "context": {"region": "region", "resource_crn": "resource_crn", "resource_id": "resource_id", "resource_name": "resource_name", "resource_type": "resource_type", "service_crn": "service_crn", "service_name": "service_name", "environment_name": "environment_name", "component_name": "component_name", "toolchain_id": "toolchain_id"}, "finding": {"severity": "LOW", "certainty": "LOW", "next_steps": [{"title": "title", "url": "url"}], "network_connection": {"direction": "direction", "protocol": "protocol", "client": {"address": "address", "port": 4}, "server": {"address": "address", "port": 4}}, "data_transferred": {"client_bytes": 12, "server_bytes": 12, "client_packets": 14, "server_packets": 14}}, "kpi": {"value": 5, "total": 5}, "reference_data": {"anyKey": "anyValue"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {}
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {}
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {}
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {}
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a dict representation of a Finding model
        finding_model = {}
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        # Construct a dict representation of a Kpi model
        kpi_model = {}
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'
        note_name = 'testString'
        kind = 'FINDING'
        id = 'testString'
        resource_url = 'testString'
        remediation = 'testString'
        context = context_model
        finding = finding_model
        kpi = kpi_model
        reference_data = { 'foo': 'bar' }

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "occurrence_id": occurrence_id,
            "note_name": note_name,
            "kind": kind,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_occurrence(**req_copy)



class TestDeleteOccurrence():
    """
    Test Class for delete_occurrence
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_occurrence_all_params(self):
        """
        delete_occurrence()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_occurrence(
            provider_id,
            occurrence_id,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_occurrence_required_params(self):
        """
        test_delete_occurrence_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'

        # Invoke method
        response = _service.delete_occurrence(
            provider_id,
            occurrence_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_occurrence_value_error(self):
        """
        test_delete_occurrence_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers/testString/occurrences/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        provider_id = 'testString'
        occurrence_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "occurrence_id": occurrence_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_occurrence(**req_copy)



# endregion
##############################################################################
# End of Service: FindingsOccurrences
##############################################################################

##############################################################################
# Start of Service: FindingsProviders
##############################################################################
# region

class TestListProviders():
    """
    Test Class for list_providers
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_providers_all_params(self):
        """
        list_providers()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers')
        mock_response = '{"providers": [{"name": "name", "id": "id"}], "limit": 5, "skip": 4, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transaction_id = 'testString'
        limit = 2
        skip = 38
        start_provider_id = 'testString'
        end_provider_id = 'testString'

        # Invoke method
        response = _service.list_providers(
            transaction_id=transaction_id,
            limit=limit,
            skip=skip,
            start_provider_id=start_provider_id,
            end_provider_id=end_provider_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'skip={}'.format(skip) in query_string
        assert 'start_provider_id={}'.format(start_provider_id) in query_string
        assert 'end_provider_id={}'.format(end_provider_id) in query_string


    @responses.activate
    def test_list_providers_required_params(self):
        """
        test_list_providers_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers')
        mock_response = '{"providers": [{"name": "name", "id": "id"}], "limit": 5, "skip": 4, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_providers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_providers_value_error(self):
        """
        test_list_providers_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/providers')
        mock_response = '{"providers": [{"name": "name", "id": "id"}], "limit": 5, "skip": 4, "total_count": 11}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_providers(**req_copy)



# endregion
##############################################################################
# End of Service: FindingsProviders
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestCard():
    """
    Test Class for Card
    """

    def test_card_serialization(self):
        """
        Test serialization/deserialization for Card
        """

        # Construct dict forms of any model objects needed in order to build this model.

        value_type_model = {} # ValueTypeFindingCountValueType
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        card_element_model = {} # CardElementTimeSeriesCardElement
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        # Construct a json representation of a Card model
        card_model_json = {}
        card_model_json['section'] = 'testString'
        card_model_json['title'] = 'testString'
        card_model_json['subtitle'] = 'testString'
        card_model_json['order'] = 1
        card_model_json['finding_note_names'] = ['testString']
        card_model_json['requires_configuration'] = True
        card_model_json['badge_text'] = 'testString'
        card_model_json['badge_image'] = 'testString'
        card_model_json['elements'] = [card_element_model]

        # Construct a model instance of Card by calling from_dict on the json representation
        card_model = Card.from_dict(card_model_json)
        assert card_model != False

        # Construct a model instance of Card by calling from_dict on the json representation
        card_model_dict = Card.from_dict(card_model_json).__dict__
        card_model2 = Card(**card_model_dict)

        # Verify the model instances are equivalent
        assert card_model == card_model2

        # Convert model instance back to dict and verify no loss of data
        card_model_json2 = card_model.to_dict()
        assert card_model_json2 == card_model_json

class TestContext():
    """
    Test Class for Context
    """

    def test_context_serialization(self):
        """
        Test serialization/deserialization for Context
        """

        # Construct a json representation of a Context model
        context_model_json = {}
        context_model_json['region'] = 'testString'
        context_model_json['resource_crn'] = 'testString'
        context_model_json['resource_id'] = 'testString'
        context_model_json['resource_name'] = 'testString'
        context_model_json['resource_type'] = 'testString'
        context_model_json['service_crn'] = 'testString'
        context_model_json['service_name'] = 'testString'
        context_model_json['environment_name'] = 'testString'
        context_model_json['component_name'] = 'testString'
        context_model_json['toolchain_id'] = 'testString'

        # Construct a model instance of Context by calling from_dict on the json representation
        context_model = Context.from_dict(context_model_json)
        assert context_model != False

        # Construct a model instance of Context by calling from_dict on the json representation
        context_model_dict = Context.from_dict(context_model_json).__dict__
        context_model2 = Context(**context_model_dict)

        # Verify the model instances are equivalent
        assert context_model == context_model2

        # Convert model instance back to dict and verify no loss of data
        context_model_json2 = context_model.to_dict()
        assert context_model_json2 == context_model_json

class TestDataTransferred():
    """
    Test Class for DataTransferred
    """

    def test_data_transferred_serialization(self):
        """
        Test serialization/deserialization for DataTransferred
        """

        # Construct a json representation of a DataTransferred model
        data_transferred_model_json = {}
        data_transferred_model_json['client_bytes'] = 38
        data_transferred_model_json['server_bytes'] = 38
        data_transferred_model_json['client_packets'] = 38
        data_transferred_model_json['server_packets'] = 38

        # Construct a model instance of DataTransferred by calling from_dict on the json representation
        data_transferred_model = DataTransferred.from_dict(data_transferred_model_json)
        assert data_transferred_model != False

        # Construct a model instance of DataTransferred by calling from_dict on the json representation
        data_transferred_model_dict = DataTransferred.from_dict(data_transferred_model_json).__dict__
        data_transferred_model2 = DataTransferred(**data_transferred_model_dict)

        # Verify the model instances are equivalent
        assert data_transferred_model == data_transferred_model2

        # Convert model instance back to dict and verify no loss of data
        data_transferred_model_json2 = data_transferred_model.to_dict()
        assert data_transferred_model_json2 == data_transferred_model_json

class TestFinding():
    """
    Test Class for Finding
    """

    def test_finding_serialization(self):
        """
        Test serialization/deserialization for Finding
        """

        # Construct dict forms of any model objects needed in order to build this model.

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        socket_address_model = {} # SocketAddress
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        network_connection_model = {} # NetworkConnection
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        data_transferred_model = {} # DataTransferred
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        # Construct a json representation of a Finding model
        finding_model_json = {}
        finding_model_json['severity'] = 'LOW'
        finding_model_json['certainty'] = 'LOW'
        finding_model_json['next_steps'] = [remediation_step_model]
        finding_model_json['network_connection'] = network_connection_model
        finding_model_json['data_transferred'] = data_transferred_model

        # Construct a model instance of Finding by calling from_dict on the json representation
        finding_model = Finding.from_dict(finding_model_json)
        assert finding_model != False

        # Construct a model instance of Finding by calling from_dict on the json representation
        finding_model_dict = Finding.from_dict(finding_model_json).__dict__
        finding_model2 = Finding(**finding_model_dict)

        # Verify the model instances are equivalent
        assert finding_model == finding_model2

        # Convert model instance back to dict and verify no loss of data
        finding_model_json2 = finding_model.to_dict()
        assert finding_model_json2 == finding_model_json

class TestFindingType():
    """
    Test Class for FindingType
    """

    def test_finding_type_serialization(self):
        """
        Test serialization/deserialization for FindingType
        """

        # Construct dict forms of any model objects needed in order to build this model.

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        # Construct a json representation of a FindingType model
        finding_type_model_json = {}
        finding_type_model_json['severity'] = 'LOW'
        finding_type_model_json['next_steps'] = [remediation_step_model]

        # Construct a model instance of FindingType by calling from_dict on the json representation
        finding_type_model = FindingType.from_dict(finding_type_model_json)
        assert finding_type_model != False

        # Construct a model instance of FindingType by calling from_dict on the json representation
        finding_type_model_dict = FindingType.from_dict(finding_type_model_json).__dict__
        finding_type_model2 = FindingType(**finding_type_model_dict)

        # Verify the model instances are equivalent
        assert finding_type_model == finding_type_model2

        # Convert model instance back to dict and verify no loss of data
        finding_type_model_json2 = finding_type_model.to_dict()
        assert finding_type_model_json2 == finding_type_model_json

class TestKpi():
    """
    Test Class for Kpi
    """

    def test_kpi_serialization(self):
        """
        Test serialization/deserialization for Kpi
        """

        # Construct a json representation of a Kpi model
        kpi_model_json = {}
        kpi_model_json['value'] = 72.5
        kpi_model_json['total'] = 72.5

        # Construct a model instance of Kpi by calling from_dict on the json representation
        kpi_model = Kpi.from_dict(kpi_model_json)
        assert kpi_model != False

        # Construct a model instance of Kpi by calling from_dict on the json representation
        kpi_model_dict = Kpi.from_dict(kpi_model_json).__dict__
        kpi_model2 = Kpi(**kpi_model_dict)

        # Verify the model instances are equivalent
        assert kpi_model == kpi_model2

        # Convert model instance back to dict and verify no loss of data
        kpi_model_json2 = kpi_model.to_dict()
        assert kpi_model_json2 == kpi_model_json

class TestKpiType():
    """
    Test Class for KpiType
    """

    def test_kpi_type_serialization(self):
        """
        Test serialization/deserialization for KpiType
        """

        # Construct a json representation of a KpiType model
        kpi_type_model_json = {}
        kpi_type_model_json['aggregation_type'] = 'SUM'

        # Construct a model instance of KpiType by calling from_dict on the json representation
        kpi_type_model = KpiType.from_dict(kpi_type_model_json)
        assert kpi_type_model != False

        # Construct a model instance of KpiType by calling from_dict on the json representation
        kpi_type_model_dict = KpiType.from_dict(kpi_type_model_json).__dict__
        kpi_type_model2 = KpiType(**kpi_type_model_dict)

        # Verify the model instances are equivalent
        assert kpi_type_model == kpi_type_model2

        # Convert model instance back to dict and verify no loss of data
        kpi_type_model_json2 = kpi_type_model.to_dict()
        assert kpi_type_model_json2 == kpi_type_model_json

class TestNetworkConnection():
    """
    Test Class for NetworkConnection
    """

    def test_network_connection_serialization(self):
        """
        Test serialization/deserialization for NetworkConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        socket_address_model = {} # SocketAddress
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        # Construct a json representation of a NetworkConnection model
        network_connection_model_json = {}
        network_connection_model_json['direction'] = 'testString'
        network_connection_model_json['protocol'] = 'testString'
        network_connection_model_json['client'] = socket_address_model
        network_connection_model_json['server'] = socket_address_model

        # Construct a model instance of NetworkConnection by calling from_dict on the json representation
        network_connection_model = NetworkConnection.from_dict(network_connection_model_json)
        assert network_connection_model != False

        # Construct a model instance of NetworkConnection by calling from_dict on the json representation
        network_connection_model_dict = NetworkConnection.from_dict(network_connection_model_json).__dict__
        network_connection_model2 = NetworkConnection(**network_connection_model_dict)

        # Verify the model instances are equivalent
        assert network_connection_model == network_connection_model2

        # Convert model instance back to dict and verify no loss of data
        network_connection_model_json2 = network_connection_model.to_dict()
        assert network_connection_model_json2 == network_connection_model_json

class TestRemediationStep():
    """
    Test Class for RemediationStep
    """

    def test_remediation_step_serialization(self):
        """
        Test serialization/deserialization for RemediationStep
        """

        # Construct a json representation of a RemediationStep model
        remediation_step_model_json = {}
        remediation_step_model_json['title'] = 'testString'
        remediation_step_model_json['url'] = 'testString'

        # Construct a model instance of RemediationStep by calling from_dict on the json representation
        remediation_step_model = RemediationStep.from_dict(remediation_step_model_json)
        assert remediation_step_model != False

        # Construct a model instance of RemediationStep by calling from_dict on the json representation
        remediation_step_model_dict = RemediationStep.from_dict(remediation_step_model_json).__dict__
        remediation_step_model2 = RemediationStep(**remediation_step_model_dict)

        # Verify the model instances are equivalent
        assert remediation_step_model == remediation_step_model2

        # Convert model instance back to dict and verify no loss of data
        remediation_step_model_json2 = remediation_step_model.to_dict()
        assert remediation_step_model_json2 == remediation_step_model_json

class TestReporter():
    """
    Test Class for Reporter
    """

    def test_reporter_serialization(self):
        """
        Test serialization/deserialization for Reporter
        """

        # Construct a json representation of a Reporter model
        reporter_model_json = {}
        reporter_model_json['id'] = 'testString'
        reporter_model_json['title'] = 'testString'
        reporter_model_json['url'] = 'testString'

        # Construct a model instance of Reporter by calling from_dict on the json representation
        reporter_model = Reporter.from_dict(reporter_model_json)
        assert reporter_model != False

        # Construct a model instance of Reporter by calling from_dict on the json representation
        reporter_model_dict = Reporter.from_dict(reporter_model_json).__dict__
        reporter_model2 = Reporter(**reporter_model_dict)

        # Verify the model instances are equivalent
        assert reporter_model == reporter_model2

        # Convert model instance back to dict and verify no loss of data
        reporter_model_json2 = reporter_model.to_dict()
        assert reporter_model_json2 == reporter_model_json

class TestSection():
    """
    Test Class for Section
    """

    def test_section_serialization(self):
        """
        Test serialization/deserialization for Section
        """

        # Construct a json representation of a Section model
        section_model_json = {}
        section_model_json['title'] = 'testString'
        section_model_json['image'] = 'testString'

        # Construct a model instance of Section by calling from_dict on the json representation
        section_model = Section.from_dict(section_model_json)
        assert section_model != False

        # Construct a model instance of Section by calling from_dict on the json representation
        section_model_dict = Section.from_dict(section_model_json).__dict__
        section_model2 = Section(**section_model_dict)

        # Verify the model instances are equivalent
        assert section_model == section_model2

        # Convert model instance back to dict and verify no loss of data
        section_model_json2 = section_model.to_dict()
        assert section_model_json2 == section_model_json

class TestSocketAddress():
    """
    Test Class for SocketAddress
    """

    def test_socket_address_serialization(self):
        """
        Test serialization/deserialization for SocketAddress
        """

        # Construct a json representation of a SocketAddress model
        socket_address_model_json = {}
        socket_address_model_json['address'] = 'testString'
        socket_address_model_json['port'] = 38

        # Construct a model instance of SocketAddress by calling from_dict on the json representation
        socket_address_model = SocketAddress.from_dict(socket_address_model_json)
        assert socket_address_model != False

        # Construct a model instance of SocketAddress by calling from_dict on the json representation
        socket_address_model_dict = SocketAddress.from_dict(socket_address_model_json).__dict__
        socket_address_model2 = SocketAddress(**socket_address_model_dict)

        # Verify the model instances are equivalent
        assert socket_address_model == socket_address_model2

        # Convert model instance back to dict and verify no loss of data
        socket_address_model_json2 = socket_address_model.to_dict()
        assert socket_address_model_json2 == socket_address_model_json

class TestApiListNoteOccurrencesResponse():
    """
    Test Class for ApiListNoteOccurrencesResponse
    """

    def test_api_list_note_occurrences_response_serialization(self):
        """
        Test serialization/deserialization for ApiListNoteOccurrencesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        context_model = {} # Context
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        socket_address_model = {} # SocketAddress
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        network_connection_model = {} # NetworkConnection
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        data_transferred_model = {} # DataTransferred
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        finding_model = {} # Finding
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        kpi_model = {} # Kpi
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        api_occurrence_model = {} # ApiOccurrence
        api_occurrence_model['resource_url'] = 'testString'
        api_occurrence_model['note_name'] = 'testString'
        api_occurrence_model['kind'] = 'FINDING'
        api_occurrence_model['remediation'] = 'testString'
        api_occurrence_model['create_time'] = "2019-01-01T12:00:00Z"
        api_occurrence_model['update_time'] = "2019-01-01T12:00:00Z"
        api_occurrence_model['id'] = 'testString'
        api_occurrence_model['context'] = context_model
        api_occurrence_model['finding'] = finding_model
        api_occurrence_model['kpi'] = kpi_model
        api_occurrence_model['reference_data'] = { 'foo': 'bar' }

        # Construct a json representation of a ApiListNoteOccurrencesResponse model
        api_list_note_occurrences_response_model_json = {}
        api_list_note_occurrences_response_model_json['occurrences'] = [api_occurrence_model]
        api_list_note_occurrences_response_model_json['next_page_token'] = 'testString'

        # Construct a model instance of ApiListNoteOccurrencesResponse by calling from_dict on the json representation
        api_list_note_occurrences_response_model = ApiListNoteOccurrencesResponse.from_dict(api_list_note_occurrences_response_model_json)
        assert api_list_note_occurrences_response_model != False

        # Construct a model instance of ApiListNoteOccurrencesResponse by calling from_dict on the json representation
        api_list_note_occurrences_response_model_dict = ApiListNoteOccurrencesResponse.from_dict(api_list_note_occurrences_response_model_json).__dict__
        api_list_note_occurrences_response_model2 = ApiListNoteOccurrencesResponse(**api_list_note_occurrences_response_model_dict)

        # Verify the model instances are equivalent
        assert api_list_note_occurrences_response_model == api_list_note_occurrences_response_model2

        # Convert model instance back to dict and verify no loss of data
        api_list_note_occurrences_response_model_json2 = api_list_note_occurrences_response_model.to_dict()
        assert api_list_note_occurrences_response_model_json2 == api_list_note_occurrences_response_model_json

class TestApiListNotesResponse():
    """
    Test Class for ApiListNotesResponse
    """

    def test_api_list_notes_response_serialization(self):
        """
        Test serialization/deserialization for ApiListNotesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_note_related_url_model = {} # ApiNoteRelatedUrl
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        reporter_model = {} # Reporter
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        finding_type_model = {} # FindingType
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        kpi_type_model = {} # KpiType
        kpi_type_model['aggregation_type'] = 'SUM'

        value_type_model = {} # ValueTypeFindingCountValueType
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        card_element_model = {} # CardElementTimeSeriesCardElement
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        card_model = {} # Card
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        section_model = {} # Section
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        api_note_model = {} # ApiNote
        api_note_model['short_description'] = 'testString'
        api_note_model['long_description'] = 'testString'
        api_note_model['kind'] = 'FINDING'
        api_note_model['related_url'] = [api_note_related_url_model]
        api_note_model['expiration_time'] = "2019-01-01T12:00:00Z"
        api_note_model['create_time'] = "2019-01-01T12:00:00Z"
        api_note_model['update_time'] = "2019-01-01T12:00:00Z"
        api_note_model['id'] = 'testString'
        api_note_model['shared'] = True
        api_note_model['reported_by'] = reporter_model
        api_note_model['finding'] = finding_type_model
        api_note_model['kpi'] = kpi_type_model
        api_note_model['card'] = card_model
        api_note_model['section'] = section_model

        # Construct a json representation of a ApiListNotesResponse model
        api_list_notes_response_model_json = {}
        api_list_notes_response_model_json['notes'] = [api_note_model]
        api_list_notes_response_model_json['next_page_token'] = 'testString'

        # Construct a model instance of ApiListNotesResponse by calling from_dict on the json representation
        api_list_notes_response_model = ApiListNotesResponse.from_dict(api_list_notes_response_model_json)
        assert api_list_notes_response_model != False

        # Construct a model instance of ApiListNotesResponse by calling from_dict on the json representation
        api_list_notes_response_model_dict = ApiListNotesResponse.from_dict(api_list_notes_response_model_json).__dict__
        api_list_notes_response_model2 = ApiListNotesResponse(**api_list_notes_response_model_dict)

        # Verify the model instances are equivalent
        assert api_list_notes_response_model == api_list_notes_response_model2

        # Convert model instance back to dict and verify no loss of data
        api_list_notes_response_model_json2 = api_list_notes_response_model.to_dict()
        assert api_list_notes_response_model_json2 == api_list_notes_response_model_json

class TestApiListOccurrencesResponse():
    """
    Test Class for ApiListOccurrencesResponse
    """

    def test_api_list_occurrences_response_serialization(self):
        """
        Test serialization/deserialization for ApiListOccurrencesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        context_model = {} # Context
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        socket_address_model = {} # SocketAddress
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        network_connection_model = {} # NetworkConnection
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        data_transferred_model = {} # DataTransferred
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        finding_model = {} # Finding
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        kpi_model = {} # Kpi
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        api_occurrence_model = {} # ApiOccurrence
        api_occurrence_model['resource_url'] = 'testString'
        api_occurrence_model['note_name'] = 'testString'
        api_occurrence_model['kind'] = 'FINDING'
        api_occurrence_model['remediation'] = 'testString'
        api_occurrence_model['create_time'] = "2019-01-01T12:00:00Z"
        api_occurrence_model['update_time'] = "2019-01-01T12:00:00Z"
        api_occurrence_model['id'] = 'testString'
        api_occurrence_model['context'] = context_model
        api_occurrence_model['finding'] = finding_model
        api_occurrence_model['kpi'] = kpi_model
        api_occurrence_model['reference_data'] = { 'foo': 'bar' }

        # Construct a json representation of a ApiListOccurrencesResponse model
        api_list_occurrences_response_model_json = {}
        api_list_occurrences_response_model_json['occurrences'] = [api_occurrence_model]
        api_list_occurrences_response_model_json['next_page_token'] = 'testString'

        # Construct a model instance of ApiListOccurrencesResponse by calling from_dict on the json representation
        api_list_occurrences_response_model = ApiListOccurrencesResponse.from_dict(api_list_occurrences_response_model_json)
        assert api_list_occurrences_response_model != False

        # Construct a model instance of ApiListOccurrencesResponse by calling from_dict on the json representation
        api_list_occurrences_response_model_dict = ApiListOccurrencesResponse.from_dict(api_list_occurrences_response_model_json).__dict__
        api_list_occurrences_response_model2 = ApiListOccurrencesResponse(**api_list_occurrences_response_model_dict)

        # Verify the model instances are equivalent
        assert api_list_occurrences_response_model == api_list_occurrences_response_model2

        # Convert model instance back to dict and verify no loss of data
        api_list_occurrences_response_model_json2 = api_list_occurrences_response_model.to_dict()
        assert api_list_occurrences_response_model_json2 == api_list_occurrences_response_model_json

class TestApiListProvidersResponse():
    """
    Test Class for ApiListProvidersResponse
    """

    def test_api_list_providers_response_serialization(self):
        """
        Test serialization/deserialization for ApiListProvidersResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_provider_model = {} # ApiProvider
        api_provider_model['name'] = 'testString'
        api_provider_model['id'] = 'testString'

        # Construct a json representation of a ApiListProvidersResponse model
        api_list_providers_response_model_json = {}
        api_list_providers_response_model_json['providers'] = [api_provider_model]
        api_list_providers_response_model_json['limit'] = 38
        api_list_providers_response_model_json['skip'] = 38
        api_list_providers_response_model_json['total_count'] = 38

        # Construct a model instance of ApiListProvidersResponse by calling from_dict on the json representation
        api_list_providers_response_model = ApiListProvidersResponse.from_dict(api_list_providers_response_model_json)
        assert api_list_providers_response_model != False

        # Construct a model instance of ApiListProvidersResponse by calling from_dict on the json representation
        api_list_providers_response_model_dict = ApiListProvidersResponse.from_dict(api_list_providers_response_model_json).__dict__
        api_list_providers_response_model2 = ApiListProvidersResponse(**api_list_providers_response_model_dict)

        # Verify the model instances are equivalent
        assert api_list_providers_response_model == api_list_providers_response_model2

        # Convert model instance back to dict and verify no loss of data
        api_list_providers_response_model_json2 = api_list_providers_response_model.to_dict()
        assert api_list_providers_response_model_json2 == api_list_providers_response_model_json

class TestApiNote():
    """
    Test Class for ApiNote
    """

    def test_api_note_serialization(self):
        """
        Test serialization/deserialization for ApiNote
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_note_related_url_model = {} # ApiNoteRelatedUrl
        api_note_related_url_model['label'] = 'testString'
        api_note_related_url_model['url'] = 'testString'

        reporter_model = {} # Reporter
        reporter_model['id'] = 'testString'
        reporter_model['title'] = 'testString'
        reporter_model['url'] = 'testString'

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        finding_type_model = {} # FindingType
        finding_type_model['severity'] = 'LOW'
        finding_type_model['next_steps'] = [remediation_step_model]

        kpi_type_model = {} # KpiType
        kpi_type_model['aggregation_type'] = 'SUM'

        value_type_model = {} # ValueTypeFindingCountValueType
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        card_element_model = {} # CardElementTimeSeriesCardElement
        card_element_model['text'] = 'testString'
        card_element_model['default_interval'] = 'testString'
        card_element_model['kind'] = 'TIME_SERIES'
        card_element_model['default_time_range'] = '1d'
        card_element_model['value_types'] = [value_type_model]

        card_model = {} # Card
        card_model['section'] = 'testString'
        card_model['title'] = 'testString'
        card_model['subtitle'] = 'testString'
        card_model['order'] = 1
        card_model['finding_note_names'] = ['testString']
        card_model['requires_configuration'] = True
        card_model['badge_text'] = 'testString'
        card_model['badge_image'] = 'testString'
        card_model['elements'] = [card_element_model]

        section_model = {} # Section
        section_model['title'] = 'testString'
        section_model['image'] = 'testString'

        # Construct a json representation of a ApiNote model
        api_note_model_json = {}
        api_note_model_json['short_description'] = 'testString'
        api_note_model_json['long_description'] = 'testString'
        api_note_model_json['kind'] = 'FINDING'
        api_note_model_json['related_url'] = [api_note_related_url_model]
        api_note_model_json['expiration_time'] = "2019-01-01T12:00:00Z"
        api_note_model_json['create_time'] = "2019-01-01T12:00:00Z"
        api_note_model_json['update_time'] = "2019-01-01T12:00:00Z"
        api_note_model_json['id'] = 'testString'
        api_note_model_json['shared'] = True
        api_note_model_json['reported_by'] = reporter_model
        api_note_model_json['finding'] = finding_type_model
        api_note_model_json['kpi'] = kpi_type_model
        api_note_model_json['card'] = card_model
        api_note_model_json['section'] = section_model

        # Construct a model instance of ApiNote by calling from_dict on the json representation
        api_note_model = ApiNote.from_dict(api_note_model_json)
        assert api_note_model != False

        # Construct a model instance of ApiNote by calling from_dict on the json representation
        api_note_model_dict = ApiNote.from_dict(api_note_model_json).__dict__
        api_note_model2 = ApiNote(**api_note_model_dict)

        # Verify the model instances are equivalent
        assert api_note_model == api_note_model2

        # Convert model instance back to dict and verify no loss of data
        api_note_model_json2 = api_note_model.to_dict()
        assert api_note_model_json2 == api_note_model_json

class TestApiNoteRelatedUrl():
    """
    Test Class for ApiNoteRelatedUrl
    """

    def test_api_note_related_url_serialization(self):
        """
        Test serialization/deserialization for ApiNoteRelatedUrl
        """

        # Construct a json representation of a ApiNoteRelatedUrl model
        api_note_related_url_model_json = {}
        api_note_related_url_model_json['label'] = 'testString'
        api_note_related_url_model_json['url'] = 'testString'

        # Construct a model instance of ApiNoteRelatedUrl by calling from_dict on the json representation
        api_note_related_url_model = ApiNoteRelatedUrl.from_dict(api_note_related_url_model_json)
        assert api_note_related_url_model != False

        # Construct a model instance of ApiNoteRelatedUrl by calling from_dict on the json representation
        api_note_related_url_model_dict = ApiNoteRelatedUrl.from_dict(api_note_related_url_model_json).__dict__
        api_note_related_url_model2 = ApiNoteRelatedUrl(**api_note_related_url_model_dict)

        # Verify the model instances are equivalent
        assert api_note_related_url_model == api_note_related_url_model2

        # Convert model instance back to dict and verify no loss of data
        api_note_related_url_model_json2 = api_note_related_url_model.to_dict()
        assert api_note_related_url_model_json2 == api_note_related_url_model_json

class TestApiOccurrence():
    """
    Test Class for ApiOccurrence
    """

    def test_api_occurrence_serialization(self):
        """
        Test serialization/deserialization for ApiOccurrence
        """

        # Construct dict forms of any model objects needed in order to build this model.

        context_model = {} # Context
        context_model['region'] = 'testString'
        context_model['resource_crn'] = 'testString'
        context_model['resource_id'] = 'testString'
        context_model['resource_name'] = 'testString'
        context_model['resource_type'] = 'testString'
        context_model['service_crn'] = 'testString'
        context_model['service_name'] = 'testString'
        context_model['environment_name'] = 'testString'
        context_model['component_name'] = 'testString'
        context_model['toolchain_id'] = 'testString'

        remediation_step_model = {} # RemediationStep
        remediation_step_model['title'] = 'testString'
        remediation_step_model['url'] = 'testString'

        socket_address_model = {} # SocketAddress
        socket_address_model['address'] = 'testString'
        socket_address_model['port'] = 38

        network_connection_model = {} # NetworkConnection
        network_connection_model['direction'] = 'testString'
        network_connection_model['protocol'] = 'testString'
        network_connection_model['client'] = socket_address_model
        network_connection_model['server'] = socket_address_model

        data_transferred_model = {} # DataTransferred
        data_transferred_model['client_bytes'] = 38
        data_transferred_model['server_bytes'] = 38
        data_transferred_model['client_packets'] = 38
        data_transferred_model['server_packets'] = 38

        finding_model = {} # Finding
        finding_model['severity'] = 'LOW'
        finding_model['certainty'] = 'LOW'
        finding_model['next_steps'] = [remediation_step_model]
        finding_model['network_connection'] = network_connection_model
        finding_model['data_transferred'] = data_transferred_model

        kpi_model = {} # Kpi
        kpi_model['value'] = 72.5
        kpi_model['total'] = 72.5

        # Construct a json representation of a ApiOccurrence model
        api_occurrence_model_json = {}
        api_occurrence_model_json['resource_url'] = 'testString'
        api_occurrence_model_json['note_name'] = 'testString'
        api_occurrence_model_json['kind'] = 'FINDING'
        api_occurrence_model_json['remediation'] = 'testString'
        api_occurrence_model_json['create_time'] = "2019-01-01T12:00:00Z"
        api_occurrence_model_json['update_time'] = "2019-01-01T12:00:00Z"
        api_occurrence_model_json['id'] = 'testString'
        api_occurrence_model_json['context'] = context_model
        api_occurrence_model_json['finding'] = finding_model
        api_occurrence_model_json['kpi'] = kpi_model
        api_occurrence_model_json['reference_data'] = { 'foo': 'bar' }

        # Construct a model instance of ApiOccurrence by calling from_dict on the json representation
        api_occurrence_model = ApiOccurrence.from_dict(api_occurrence_model_json)
        assert api_occurrence_model != False

        # Construct a model instance of ApiOccurrence by calling from_dict on the json representation
        api_occurrence_model_dict = ApiOccurrence.from_dict(api_occurrence_model_json).__dict__
        api_occurrence_model2 = ApiOccurrence(**api_occurrence_model_dict)

        # Verify the model instances are equivalent
        assert api_occurrence_model == api_occurrence_model2

        # Convert model instance back to dict and verify no loss of data
        api_occurrence_model_json2 = api_occurrence_model.to_dict()
        assert api_occurrence_model_json2 == api_occurrence_model_json

class TestApiProvider():
    """
    Test Class for ApiProvider
    """

    def test_api_provider_serialization(self):
        """
        Test serialization/deserialization for ApiProvider
        """

        # Construct a json representation of a ApiProvider model
        api_provider_model_json = {}
        api_provider_model_json['name'] = 'testString'
        api_provider_model_json['id'] = 'testString'

        # Construct a model instance of ApiProvider by calling from_dict on the json representation
        api_provider_model = ApiProvider.from_dict(api_provider_model_json)
        assert api_provider_model != False

        # Construct a model instance of ApiProvider by calling from_dict on the json representation
        api_provider_model_dict = ApiProvider.from_dict(api_provider_model_json).__dict__
        api_provider_model2 = ApiProvider(**api_provider_model_dict)

        # Verify the model instances are equivalent
        assert api_provider_model == api_provider_model2

        # Convert model instance back to dict and verify no loss of data
        api_provider_model_json2 = api_provider_model.to_dict()
        assert api_provider_model_json2 == api_provider_model_json

class TestCardElementBreakdownCardElement():
    """
    Test Class for CardElementBreakdownCardElement
    """

    def test_card_element_breakdown_card_element_serialization(self):
        """
        Test serialization/deserialization for CardElementBreakdownCardElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        value_type_model = {} # ValueTypeFindingCountValueType
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a json representation of a CardElementBreakdownCardElement model
        card_element_breakdown_card_element_model_json = {}
        card_element_breakdown_card_element_model_json['text'] = 'testString'
        card_element_breakdown_card_element_model_json['kind'] = 'BREAKDOWN'
        card_element_breakdown_card_element_model_json['default_time_range'] = '1d'
        card_element_breakdown_card_element_model_json['value_types'] = [value_type_model]

        # Construct a model instance of CardElementBreakdownCardElement by calling from_dict on the json representation
        card_element_breakdown_card_element_model = CardElementBreakdownCardElement.from_dict(card_element_breakdown_card_element_model_json)
        assert card_element_breakdown_card_element_model != False

        # Construct a model instance of CardElementBreakdownCardElement by calling from_dict on the json representation
        card_element_breakdown_card_element_model_dict = CardElementBreakdownCardElement.from_dict(card_element_breakdown_card_element_model_json).__dict__
        card_element_breakdown_card_element_model2 = CardElementBreakdownCardElement(**card_element_breakdown_card_element_model_dict)

        # Verify the model instances are equivalent
        assert card_element_breakdown_card_element_model == card_element_breakdown_card_element_model2

        # Convert model instance back to dict and verify no loss of data
        card_element_breakdown_card_element_model_json2 = card_element_breakdown_card_element_model.to_dict()
        assert card_element_breakdown_card_element_model_json2 == card_element_breakdown_card_element_model_json

class TestCardElementNumericCardElement():
    """
    Test Class for CardElementNumericCardElement
    """

    def test_card_element_numeric_card_element_serialization(self):
        """
        Test serialization/deserialization for CardElementNumericCardElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        numeric_card_element_value_type_model = {} # NumericCardElementValueType

        # Construct a json representation of a CardElementNumericCardElement model
        card_element_numeric_card_element_model_json = {}
        card_element_numeric_card_element_model_json['text'] = 'testString'
        card_element_numeric_card_element_model_json['kind'] = 'NUMERIC'
        card_element_numeric_card_element_model_json['default_time_range'] = '1d'
        card_element_numeric_card_element_model_json['value_type'] = numeric_card_element_value_type_model

        # Construct a model instance of CardElementNumericCardElement by calling from_dict on the json representation
        card_element_numeric_card_element_model = CardElementNumericCardElement.from_dict(card_element_numeric_card_element_model_json)
        assert card_element_numeric_card_element_model != False

        # Construct a model instance of CardElementNumericCardElement by calling from_dict on the json representation
        card_element_numeric_card_element_model_dict = CardElementNumericCardElement.from_dict(card_element_numeric_card_element_model_json).__dict__
        card_element_numeric_card_element_model2 = CardElementNumericCardElement(**card_element_numeric_card_element_model_dict)

        # Verify the model instances are equivalent
        assert card_element_numeric_card_element_model == card_element_numeric_card_element_model2

        # Convert model instance back to dict and verify no loss of data
        card_element_numeric_card_element_model_json2 = card_element_numeric_card_element_model.to_dict()
        assert card_element_numeric_card_element_model_json2 == card_element_numeric_card_element_model_json

class TestCardElementTimeSeriesCardElement():
    """
    Test Class for CardElementTimeSeriesCardElement
    """

    def test_card_element_time_series_card_element_serialization(self):
        """
        Test serialization/deserialization for CardElementTimeSeriesCardElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        value_type_model = {} # ValueTypeFindingCountValueType
        value_type_model['kind'] = 'FINDING_COUNT'
        value_type_model['finding_note_names'] = ['testString']
        value_type_model['text'] = 'testString'

        # Construct a json representation of a CardElementTimeSeriesCardElement model
        card_element_time_series_card_element_model_json = {}
        card_element_time_series_card_element_model_json['text'] = 'testString'
        card_element_time_series_card_element_model_json['default_interval'] = 'testString'
        card_element_time_series_card_element_model_json['kind'] = 'TIME_SERIES'
        card_element_time_series_card_element_model_json['default_time_range'] = '1d'
        card_element_time_series_card_element_model_json['value_types'] = [value_type_model]

        # Construct a model instance of CardElementTimeSeriesCardElement by calling from_dict on the json representation
        card_element_time_series_card_element_model = CardElementTimeSeriesCardElement.from_dict(card_element_time_series_card_element_model_json)
        assert card_element_time_series_card_element_model != False

        # Construct a model instance of CardElementTimeSeriesCardElement by calling from_dict on the json representation
        card_element_time_series_card_element_model_dict = CardElementTimeSeriesCardElement.from_dict(card_element_time_series_card_element_model_json).__dict__
        card_element_time_series_card_element_model2 = CardElementTimeSeriesCardElement(**card_element_time_series_card_element_model_dict)

        # Verify the model instances are equivalent
        assert card_element_time_series_card_element_model == card_element_time_series_card_element_model2

        # Convert model instance back to dict and verify no loss of data
        card_element_time_series_card_element_model_json2 = card_element_time_series_card_element_model.to_dict()
        assert card_element_time_series_card_element_model_json2 == card_element_time_series_card_element_model_json

class TestNumericCardElementValueType():
    """
    Test Class for NumericCardElementValueType
    """

    def test_numeric_card_element_value_type_serialization(self):
        """
        Test serialization/deserialization for NumericCardElementValueType
        """

        # Construct a json representation of a NumericCardElementValueType model
        numeric_card_element_value_type_model_json = {}

        # Construct a model instance of NumericCardElementValueType by calling from_dict on the json representation
        numeric_card_element_value_type_model = NumericCardElementValueType.from_dict(numeric_card_element_value_type_model_json)
        assert numeric_card_element_value_type_model != False

        # Construct a model instance of NumericCardElementValueType by calling from_dict on the json representation
        numeric_card_element_value_type_model_dict = NumericCardElementValueType.from_dict(numeric_card_element_value_type_model_json).__dict__
        numeric_card_element_value_type_model2 = NumericCardElementValueType(**numeric_card_element_value_type_model_dict)

        # Verify the model instances are equivalent
        assert numeric_card_element_value_type_model == numeric_card_element_value_type_model2

        # Convert model instance back to dict and verify no loss of data
        numeric_card_element_value_type_model_json2 = numeric_card_element_value_type_model.to_dict()
        assert numeric_card_element_value_type_model_json2 == numeric_card_element_value_type_model_json

class TestValueTypeFindingCountValueType():
    """
    Test Class for ValueTypeFindingCountValueType
    """

    def test_value_type_finding_count_value_type_serialization(self):
        """
        Test serialization/deserialization for ValueTypeFindingCountValueType
        """

        # Construct a json representation of a ValueTypeFindingCountValueType model
        value_type_finding_count_value_type_model_json = {}
        value_type_finding_count_value_type_model_json['kind'] = 'FINDING_COUNT'
        value_type_finding_count_value_type_model_json['finding_note_names'] = ['testString']
        value_type_finding_count_value_type_model_json['text'] = 'testString'

        # Construct a model instance of ValueTypeFindingCountValueType by calling from_dict on the json representation
        value_type_finding_count_value_type_model = ValueTypeFindingCountValueType.from_dict(value_type_finding_count_value_type_model_json)
        assert value_type_finding_count_value_type_model != False

        # Construct a model instance of ValueTypeFindingCountValueType by calling from_dict on the json representation
        value_type_finding_count_value_type_model_dict = ValueTypeFindingCountValueType.from_dict(value_type_finding_count_value_type_model_json).__dict__
        value_type_finding_count_value_type_model2 = ValueTypeFindingCountValueType(**value_type_finding_count_value_type_model_dict)

        # Verify the model instances are equivalent
        assert value_type_finding_count_value_type_model == value_type_finding_count_value_type_model2

        # Convert model instance back to dict and verify no loss of data
        value_type_finding_count_value_type_model_json2 = value_type_finding_count_value_type_model.to_dict()
        assert value_type_finding_count_value_type_model_json2 == value_type_finding_count_value_type_model_json

class TestValueTypeKpiValueType():
    """
    Test Class for ValueTypeKpiValueType
    """

    def test_value_type_kpi_value_type_serialization(self):
        """
        Test serialization/deserialization for ValueTypeKpiValueType
        """

        # Construct a json representation of a ValueTypeKpiValueType model
        value_type_kpi_value_type_model_json = {}
        value_type_kpi_value_type_model_json['kind'] = 'KPI'
        value_type_kpi_value_type_model_json['kpi_note_name'] = 'testString'
        value_type_kpi_value_type_model_json['text'] = 'testString'

        # Construct a model instance of ValueTypeKpiValueType by calling from_dict on the json representation
        value_type_kpi_value_type_model = ValueTypeKpiValueType.from_dict(value_type_kpi_value_type_model_json)
        assert value_type_kpi_value_type_model != False

        # Construct a model instance of ValueTypeKpiValueType by calling from_dict on the json representation
        value_type_kpi_value_type_model_dict = ValueTypeKpiValueType.from_dict(value_type_kpi_value_type_model_json).__dict__
        value_type_kpi_value_type_model2 = ValueTypeKpiValueType(**value_type_kpi_value_type_model_dict)

        # Verify the model instances are equivalent
        assert value_type_kpi_value_type_model == value_type_kpi_value_type_model2

        # Convert model instance back to dict and verify no loss of data
        value_type_kpi_value_type_model_json2 = value_type_kpi_value_type_model.to_dict()
        assert value_type_kpi_value_type_model_json2 == value_type_kpi_value_type_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
