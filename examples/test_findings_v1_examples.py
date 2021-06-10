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
Examples for FindingsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import os
import pytest
from ibm_scc.findings_v1 import *

account_id = 'testString'

#
# This file provides an example of how to use the Findings service.
#
# The following configuration properties are assumed to be defined:
# FINDINGS_URL=<service base url>
# FINDINGS_AUTH_TYPE=iam
# FINDINGS_APIKEY=<IAM apikey>
# FINDINGS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'findings_v1.env'

findings_service = None

config = None


##############################################################################
# Start of Examples for Service: FindingsV1
##############################################################################
# region
class TestFindingsV1Examples():
    """
    Example Test Class for FindingsV1
    """

    @classmethod
    def setup_class(cls):
        global findings_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            findings_service = FindingsV1.new_instance(
                account_id=account_id
            )

            # end-common
            assert findings_service is not None

            # Load the configuration
            global config
            config = read_external_sources(FindingsV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_post_graph_example(self):
        """
        post_graph request example
        """
        try:
            # begin-postGraph

            response = findings_service.post_graph(
                body='testString'
            )

            # end-postGraph
            print('\npost_graph() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_note_example(self):
        """
        create_note request example
        """
        try:
            print('\ncreate_note() result:')
            # begin-createNote

            reporter_model = {
                'id': 'testString',
                'title': 'testString',
            }

            api_note = findings_service.create_note(
                provider_id='testString',
                short_description='testString',
                long_description='testString',
                kind='FINDING',
                id='testString',
                reported_by=reporter_model
            ).get_result()

            print(json.dumps(api_note, indent=2))

            # end-createNote

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_notes_example(self):
        """
        list_notes request example
        """
        try:
            print('\nlist_notes() result:')
            # begin-listNotes

            api_list_notes_response = findings_service.list_notes(
                provider_id='testString'
            ).get_result()

            print(json.dumps(api_list_notes_response, indent=2))

            # end-listNotes

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_note_example(self):
        """
        get_note request example
        """
        try:
            print('\nget_note() result:')
            # begin-getNote

            api_note = findings_service.get_note(
                provider_id='testString',
                note_id='testString'
            ).get_result()

            print(json.dumps(api_note, indent=2))

            # end-getNote

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_note_example(self):
        """
        update_note request example
        """
        try:
            print('\nupdate_note() result:')
            # begin-updateNote

            reporter_model = {
                'id': 'testString',
                'title': 'testString',
            }

            api_note = findings_service.update_note(
                provider_id='testString',
                note_id='testString',
                short_description='testString',
                long_description='testString',
                kind='FINDING',
                id='testString',
                reported_by=reporter_model
            ).get_result()

            print(json.dumps(api_note, indent=2))

            # end-updateNote

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_occurrence_note_example(self):
        """
        get_occurrence_note request example
        """
        try:
            print('\nget_occurrence_note() result:')
            # begin-getOccurrenceNote

            api_note = findings_service.get_occurrence_note(
                provider_id='testString',
                occurrence_id='testString'
            ).get_result()

            print(json.dumps(api_note, indent=2))

            # end-getOccurrenceNote

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_occurrence_example(self):
        """
        create_occurrence request example
        """
        try:
            print('\ncreate_occurrence() result:')
            # begin-createOccurrence

            api_occurrence = findings_service.create_occurrence(
                provider_id='testString',
                note_name='testString',
                kind='FINDING',
                id='testString'
            ).get_result()

            print(json.dumps(api_occurrence, indent=2))

            # end-createOccurrence

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_occurrences_example(self):
        """
        list_occurrences request example
        """
        try:
            print('\nlist_occurrences() result:')
            # begin-listOccurrences

            api_list_occurrences_response = findings_service.list_occurrences(
                provider_id='testString'
            ).get_result()

            print(json.dumps(api_list_occurrences_response, indent=2))

            # end-listOccurrences

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_note_occurrences_example(self):
        """
        list_note_occurrences request example
        """
        try:
            print('\nlist_note_occurrences() result:')
            # begin-listNoteOccurrences

            api_list_note_occurrences_response = findings_service.list_note_occurrences(
                provider_id='testString',
                note_id='testString'
            ).get_result()

            print(json.dumps(api_list_note_occurrences_response, indent=2))

            # end-listNoteOccurrences

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_occurrence_example(self):
        """
        get_occurrence request example
        """
        try:
            print('\nget_occurrence() result:')
            # begin-getOccurrence

            api_list_occurrences_response = findings_service.get_occurrence(
                provider_id='testString',
                occurrence_id='testString'
            ).get_result()

            print(json.dumps(api_list_occurrences_response, indent=2))

            # end-getOccurrence

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_occurrence_example(self):
        """
        update_occurrence request example
        """
        try:
            print('\nupdate_occurrence() result:')
            # begin-updateOccurrence

            api_occurrence = findings_service.update_occurrence(
                provider_id='testString',
                occurrence_id='testString',
                note_name='testString',
                kind='FINDING',
                id='testString'
            ).get_result()

            print(json.dumps(api_occurrence, indent=2))

            # end-updateOccurrence

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_providers_example(self):
        """
        list_providers request example
        """
        try:
            print('\nlist_providers() result:')
            # begin-listProviders

            api_list_providers_response = findings_service.list_providers().get_result()

            print(json.dumps(api_list_providers_response, indent=2))

            # end-listProviders

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_occurrence_example(self):
        """
        delete_occurrence request example
        """
        try:
            # begin-deleteOccurrence

            response = findings_service.delete_occurrence(
                provider_id='testString',
                occurrence_id='testString'
            )

            # end-deleteOccurrence
            print('\ndelete_occurrence() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_note_example(self):
        """
        delete_note request example
        """
        try:
            # begin-deleteNote

            response = findings_service.delete_note(
                provider_id='testString',
                note_id='testString'
            )

            # end-deleteNote
            print('\ndelete_note() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: FindingsV1
##############################################################################
