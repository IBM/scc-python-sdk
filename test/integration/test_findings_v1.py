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
Integration Tests for FindingsV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_scc.findings_v1 import *
import logging
import time

# Config file name
config_file = 'findings_v1.env'
account_id = os.getenv("ACCOUNT_ID")
provider_id = os.getenv("PROVIDER_ID", "sdk-it")
testString = "testString"
identifier = "py-{0}".format(str(time.time()).split(".")[0])

class TestFindingsV1():
    """
    Integration Test Class for FindingsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.findings_service = FindingsV1.new_instance(
                account_id=account_id
                )
            assert cls.findings_service is not None

            cls.config = read_external_sources(
                FindingsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    @classmethod
    def teardown_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.findings_service = FindingsV1.new_instance(
                account_id=account_id,
                )
            assert cls.findings_service is not None

            cls.config = read_external_sources(
                FindingsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')
        print(f"cleaning up account: {account_id} with provider: {provider_id}\n")
        list_notes_response = cls.findings_service.list_notes(
            provider_id=provider_id,
        )
        for note in list_notes_response.get_result()["notes"]:
            parts = note["id"].split("-")
            if f"{parts[len(parts)-2]}-{parts[len(parts)-1]}" == identifier:
                cls.findings_service.delete_note(
                    provider_id=provider_id,
                    note_id=note["id"],
                )
        list_occurrences_response = cls.findings_service.list_occurrences(
            provider_id=provider_id,
        )
        for occurrence in list_occurrences_response.get_result()["occurrences"]:
            parts = occurrence["id"].split("-")
            if f"{parts[len(parts)-2]}-{parts[len(parts)-1]}" == identifier:
                cls.findings_service.delete_occurrence(
                    provider_id=provider_id,
                    occurrence_id=occurrence["id"],
                )
        print("cleanup was successful\n")

        list_providers_response = cls.findings_service.list_providers(
        )
        for provider in list_providers_response.get_result()["providers"]:
            if provider["id"] == provider_id:
                print(f"seems like account has some resources left even after a successful cleanup, please consider manual cleanup for account: {account_id} and provider: {provider_id}\n")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_post_graph(self):

        post_graph_response = self.findings_service.post_graph(
            body='{notes{id}}',
            content_type='application/graphql',
        )

        assert post_graph_response.get_status_code() == 200

    @needscredentials
    def test_create_note_finding(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {
            'label': testString,
            'url': testString
        }

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a FindingType model
        finding_type_model = {
            'severity': 'LOW',
            'next_steps': [remediation_step_model]
        }

        create_note_response = self.findings_service.create_note(
            provider_id=provider_id,
            short_description=testString,
            long_description=testString,
            kind='FINDING',
            id=f'finding-note-{identifier}',
            reported_by=reporter_model,
            related_url=[api_note_related_url_model],
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            finding=finding_type_model,
        )

        assert create_note_response.get_status_code() == 200
        api_note = create_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_create_note_kpi(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a KpiType model
        kpi_type_model = {
            'aggregation_type': 'SUM'
        }

        create_note_response = self.findings_service.create_note(
            provider_id=provider_id,
            short_description=testString,
            long_description=testString,
            kind='KPI',
            id=f'kpi-note-{identifier}',
            reported_by=reporter_model,
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            kpi=kpi_type_model,
        )

        assert create_note_response.get_status_code() == 200
        api_note = create_note_response.get_result()
        assert api_note is not None

    # Note (CARD)
    @needscredentials
    def test_create_note_card(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {
            'kind': 'FINDING_COUNT',
            'finding_note_names': [testString],
            'text': testString
        }

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {
            'text': testString,
            'default_interval': testString,
            'kind': 'TIME_SERIES',
            'default_time_range': '1d',
            'value_types': [value_type_model]
        }

        # Construct a dict representation of a Card model
        card_model = {
            'section': testString,
            'title': testString,
            'subtitle': testString,
            'finding_note_names': [testString],
            'requires_configuration': True,
            'badge_text': testString,
            'badge_image': testString,
            'elements': [card_element_model]
        }

        create_note_response = self.findings_service.create_note(
            provider_id=provider_id,
            short_description=testString,
            long_description=testString,
            kind='CARD',
            id=f'card-note-{identifier}',
            reported_by=reporter_model,
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            card=card_model,
        )

        assert create_note_response.get_status_code() == 200
        api_note = create_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_create_note_section(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a Section model
        section_model = {
            'title': testString,
            'image': testString
        }

        create_note_response = self.findings_service.create_note(
            provider_id=provider_id,
            short_description=testString,
            long_description=testString,
            kind='SECTION',
            id=f'section-note-{identifier}',
            reported_by=reporter_model,
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            section=section_model,
        )

        assert create_note_response.get_status_code() == 200
        api_note = create_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_list_notes(self):

        list_notes_response = self.findings_service.list_notes(
            provider_id=provider_id,
        )

        assert list_notes_response.get_status_code() == 200
        api_list_notes_response = list_notes_response.get_result()
        assert api_list_notes_response is not None

    @needscredentials
    def test_get_note(self):

        get_note_response = self.findings_service.get_note(
            provider_id=provider_id,
            note_id=f'section-note-{identifier}',
        )

        assert get_note_response.get_status_code() == 200
        api_note = get_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_update_note_finding(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a ApiNoteRelatedUrl model
        api_note_related_url_model = {
            'label': testString,
            'url': testString
        }

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a FindingType model
        finding_type_model = {
            'severity': 'LOW',
            'next_steps': [remediation_step_model]
        }

        update_note_response = self.findings_service.update_note(
            provider_id=provider_id,
            note_id=f'finding-note-{identifier}',
            short_description=testString,
            long_description=testString,
            kind='FINDING',
            id=f'finding-note-{identifier}',
            reported_by=reporter_model,
            related_url=[api_note_related_url_model],
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            finding=finding_type_model,
        )

        assert update_note_response.get_status_code() == 200
        api_note = update_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_update_note_kpi(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a KpiType model
        kpi_type_model = {
            'aggregation_type': 'SUM'
        }

        update_note_response = self.findings_service.update_note(
            provider_id=provider_id,
            note_id=f'kpi-note-{identifier}',
            short_description=testString,
            long_description=testString,
            kind='KPI',
            id=f'kpi-note-{identifier}',
            reported_by=reporter_model,
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            kpi=kpi_type_model,
        )

        assert update_note_response.get_status_code() == 200
        api_note = update_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_update_note_card(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a ValueTypeFindingCountValueType model
        value_type_model = {
            'kind': 'FINDING_COUNT',
            'finding_note_names': [testString],
            'text': testString
        }

        # Construct a dict representation of a CardElementTimeSeriesCardElement model
        card_element_model = {
            'text': testString,
            'default_interval': testString,
            'kind': 'TIME_SERIES',
            'default_time_range': '1d',
            'value_types': [value_type_model]
        }

        # Construct a dict representation of a Card model
        card_model = {
            'section': testString,
            'title': testString,
            'subtitle': testString,
            'finding_note_names': [testString],
            'requires_configuration': True,
            'badge_text': testString,
            'badge_image': testString,
            'elements': [card_element_model]
        }

        update_note_response = self.findings_service.update_note(
            provider_id=provider_id,
            note_id=f'card-note-{identifier}',
            short_description=testString,
            long_description=testString,
            kind='CARD',
            id=f'card-note-{identifier}',
            reported_by=reporter_model,
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            card=card_model,
        )

        assert update_note_response.get_status_code() == 200
        api_note = update_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_update_note_section(self):

        # Construct a dict representation of a Reporter model
        reporter_model = {
            'id': testString,
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a Section model
        section_model = {
            'title': testString,
            'image': testString
        }

        update_note_response = self.findings_service.update_note(
            provider_id=provider_id,
            note_id=f'section-note-{identifier}',
            short_description=testString,
            long_description=testString,
            kind='SECTION',
            id=f'section-note-{identifier}',
            reported_by=reporter_model,
            expiration_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            shared=True,
            section=section_model,
        )

        assert update_note_response.get_status_code() == 200
        api_note = update_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_create_occurrence_finding(self):

        # Construct a dict representation of a Context model
        context_model = {
            'region': testString,
            'resource_crn': testString,
            'resource_id': testString,
            'resource_name': testString,
            'resource_type': testString,
            'service_crn': testString,
            'service_name': testString,
            'environment_name': testString,
            'component_name': testString,
            'toolchain_id': testString
        }

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {
            'address': testString,
            'port': 38
        }

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {
            'direction': testString,
            'protocol': testString,
            'client': socket_address_model,
            'server': socket_address_model
        }

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {
            'client_bytes': 38,
            'server_bytes': 38,
            'client_packets': 38,
            'server_packets': 38
        }

        # Construct a dict representation of a Finding model
        finding_model = {
            'severity': 'LOW',
            'certainty': 'LOW',
            'next_steps': [remediation_step_model],
            'network_connection': network_connection_model,
            'data_transferred': data_transferred_model
        }

        create_occurrence_response = self.findings_service.create_occurrence(
            provider_id=provider_id,
            note_name="{0}/providers/{1}/notes/finding-note-{2}".format(account_id, provider_id, identifier),
            kind='FINDING',
            id=f'finding-occurrence-{identifier}',
            resource_url=testString,
            remediation=testString,
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            context=context_model,
            finding=finding_model,
            replace_if_exists=True,
        )

        assert create_occurrence_response.get_status_code() == 200
        api_occurrence = create_occurrence_response.get_result()
        assert api_occurrence is not None

    @needscredentials
    def test_create_occurrence_kpi(self):

        # Construct a dict representation of a Context model
        context_model = {
            'region': testString,
            'resource_crn': testString,
            'resource_id': testString,
            'resource_name': testString,
            'resource_type': testString,
            'service_crn': testString,
            'service_name': testString,
            'environment_name': testString,
            'component_name': testString,
            'toolchain_id': testString
        }

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a SocketAddress model
        socket_address_model = {
            'address': testString,
            'port': 38
        }

        # Construct a dict representation of a NetworkConnection model
        network_connection_model = {
            'direction': testString,
            'protocol': testString,
            'client': socket_address_model,
            'server': socket_address_model
        }

        # Construct a dict representation of a DataTransferred model
        data_transferred_model = {
            'client_bytes': 38,
            'server_bytes': 38,
            'client_packets': 38,
            'server_packets': 38
        }

        # Construct a dict representation of a Finding model
        finding_model = {
            'severity': 'LOW',
            'certainty': 'LOW',
            'next_steps': [remediation_step_model],
            'network_connection': network_connection_model,
            'data_transferred': data_transferred_model
        }

        # Construct a dict representation of a Kpi model
        kpi_model = {
            'value': 72.5,
            'total': 72.5
        }

        create_occurrence_response = self.findings_service.create_occurrence(
            provider_id=provider_id,
            note_name="{0}/providers/{1}/notes/kpi-note-{2}".format(account_id, provider_id, identifier),
            kind='KPI',
            id=f'kpi-occurrence-{identifier}',
            resource_url=testString,
            remediation=testString,
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            context=context_model,
            kpi=kpi_model,
            replace_if_exists=True,
        )

        assert create_occurrence_response.get_status_code() == 200
        api_occurrence = create_occurrence_response.get_result()
        assert api_occurrence is not None

    @needscredentials
    def test_get_occurrence_note(self):

        get_occurrence_note_response = self.findings_service.get_occurrence_note(
            provider_id=provider_id,
            occurrence_id=f'kpi-occurrence-{identifier}',
        )

        assert get_occurrence_note_response.get_status_code() == 200
        api_note = get_occurrence_note_response.get_result()
        assert api_note is not None

    @needscredentials
    def test_list_occurrences(self):

        list_occurrences_response = self.findings_service.list_occurrences(
            provider_id=provider_id,
        )

        assert list_occurrences_response.get_status_code() == 200
        api_list_occurrences_response = list_occurrences_response.get_result()
        assert api_list_occurrences_response is not None

    @needscredentials
    def test_list_note_occurrences(self):

        list_note_occurrences_response = self.findings_service.list_note_occurrences(
            provider_id=provider_id,
            note_id=f'finding-note-{identifier}',
        )

        assert list_note_occurrences_response.get_status_code() == 200
        api_list_note_occurrences_response = list_note_occurrences_response.get_result()
        assert api_list_note_occurrences_response is not None

    @needscredentials
    def test_get_occurrence(self):

        get_occurrence_response = self.findings_service.get_occurrence(
            provider_id=provider_id,
            occurrence_id=f'finding-occurrence-{identifier}',
        )

        assert get_occurrence_response.get_status_code() == 200
        api_list_occurrences_response = get_occurrence_response.get_result()
        assert api_list_occurrences_response is not None

    @needscredentials
    def test_update_occurrence_finding(self):

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a Finding model
        finding_model = {
            'severity': 'LOW',
            'certainty': 'LOW',
            'next_steps': [remediation_step_model],
        }

        update_occurrence_response = self.findings_service.update_occurrence(
            provider_id=provider_id,
            note_name="{0}/providers/{1}/notes/finding-note-{2}".format(account_id, provider_id, identifier),
            kind='FINDING',
            id=f'finding-occurrence-{identifier}',
            occurrence_id=f'finding-occurrence-{identifier}',
            resource_url=testString,
            remediation=testString,
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            finding=finding_model,
        )

        assert update_occurrence_response.get_status_code() == 200
        api_occurrence = update_occurrence_response.get_result()
        assert api_occurrence is not None

    @needscredentials
    def test_update_occurrence_kpi(self):

        # Construct a dict representation of a RemediationStep model
        remediation_step_model = {
            'title': testString,
            'url': testString
        }

        # Construct a dict representation of a Kpi model
        kpi_model = {
            'value': 72.5,
            'total': 72.5
        }

        update_occurrence_response = self.findings_service.update_occurrence(
            provider_id=provider_id,
            note_name="{0}/providers/{1}/notes/kpi-note-{2}".format(account_id, provider_id, identifier),
            kind='KPI',
            id=f'kpi-occurrence-{identifier}',
            occurrence_id=f'kpi-occurrence-{identifier}',
            resource_url=testString,
            remediation=testString,
            create_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            update_time=string_to_datetime('2019-01-01T12:00:00.000Z'),
            kpi=kpi_model,
        )

        assert update_occurrence_response.get_status_code() == 200
        api_occurrence = update_occurrence_response.get_result()
        assert api_occurrence is not None

    @needscredentials
    def test_list_providers(self):

        list_providers_response = self.findings_service.list_providers()

        assert list_providers_response.get_status_code() == 200
        api_list_providers_response = list_providers_response.get_result()
        assert api_list_providers_response is not None

    @needscredentials
    def test_delete_occurrence(self):

        delete_occurrence_response = self.findings_service.delete_occurrence(
            provider_id=provider_id,
            occurrence_id=f'kpi-occurrence-{identifier}',
        )

        assert delete_occurrence_response.get_status_code() == 200

    @needscredentials
    def test_delete_note(self):

        delete_note_response = self.findings_service.delete_note(
            provider_id=provider_id,
            note_id=f'section-note-{identifier}',
        )

        assert delete_note_response.get_status_code() == 200
