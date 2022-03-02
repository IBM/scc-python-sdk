# -*- coding: utf-8 -*-
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

"""
Unit Tests for AddonMgrV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_scc.addon_mgr_v1 import *

account_id = 'testString'

_service = AddonMgrV1(
    authenticator=NoAuthAuthenticator(),
    account_id=account_id
)

_base_url = 'https://us-south.secadvisor.cloud.ibm.com/addonmgr'
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


def test_get_service_url_for_region():
    """
    get_service_url_for_region()
    """
    assert AddonMgrV1.get_service_url_for_region('INVALID_REGION') is None
    assert AddonMgrV1.get_service_url_for_region('us-south') == 'https://us-south.secadvisor.cloud.ibm.com/addonmgr'
    assert AddonMgrV1.get_service_url_for_region('us-east') == 'https://us-south.secadvisor.cloud.ibm.com/addonmgr'
    assert AddonMgrV1.get_service_url_for_region('eu-gb') == 'https://eu-gb.secadvisor.cloud.ibm.com/addonmgr'
    assert AddonMgrV1.get_service_url_for_region('eu-de') == 'https://eu.compliance.cloud.ibm.com/si/addonmgr'


##############################################################################
# Start of Service: AddonManagerCos
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AddonMgrV1.new_instance(
            account_id=account_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AddonMgrV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=account_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AddonMgrV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='account_id must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=None,
            )
class TestAddNetworkInsightsCosDetailsV2():
    """
    Test Class for add_network_insights_cos_details_v2
    """

    @responses.activate
    def test_add_network_insights_cos_details_v2_all_params(self):
        """
        add_network_insights_cos_details_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/network-insights/cos')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {}
        cos_details_v2_cos_details_item_model['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model['description'] = 'testString'
        cos_details_v2_cos_details_item_model['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model['cos_bucket_url'] = 'testString'

        # Set up parameter values
        region_id = 'testString'
        cos_details = [cos_details_v2_cos_details_item_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.add_network_insights_cos_details_v2(
            region_id,
            cos_details,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['cos_details'] == [cos_details_v2_cos_details_item_model]

    def test_add_network_insights_cos_details_v2_all_params_with_retries(self):
        # Enable retries and run test_add_network_insights_cos_details_v2_all_params.
        _service.enable_retries()
        self.test_add_network_insights_cos_details_v2_all_params()

        # Disable retries and run test_add_network_insights_cos_details_v2_all_params.
        _service.disable_retries()
        self.test_add_network_insights_cos_details_v2_all_params()

    @responses.activate
    def test_add_network_insights_cos_details_v2_required_params(self):
        """
        test_add_network_insights_cos_details_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/network-insights/cos')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {}
        cos_details_v2_cos_details_item_model['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model['description'] = 'testString'
        cos_details_v2_cos_details_item_model['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model['cos_bucket_url'] = 'testString'

        # Set up parameter values
        region_id = 'testString'
        cos_details = [cos_details_v2_cos_details_item_model]

        # Invoke method
        response = _service.add_network_insights_cos_details_v2(
            region_id,
            cos_details,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['cos_details'] == [cos_details_v2_cos_details_item_model]

    def test_add_network_insights_cos_details_v2_required_params_with_retries(self):
        # Enable retries and run test_add_network_insights_cos_details_v2_required_params.
        _service.enable_retries()
        self.test_add_network_insights_cos_details_v2_required_params()

        # Disable retries and run test_add_network_insights_cos_details_v2_required_params.
        _service.disable_retries()
        self.test_add_network_insights_cos_details_v2_required_params()

    @responses.activate
    def test_add_network_insights_cos_details_v2_value_error(self):
        """
        test_add_network_insights_cos_details_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/network-insights/cos')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {}
        cos_details_v2_cos_details_item_model['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model['description'] = 'testString'
        cos_details_v2_cos_details_item_model['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model['cos_bucket_url'] = 'testString'

        # Set up parameter values
        region_id = 'testString'
        cos_details = [cos_details_v2_cos_details_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "region_id": region_id,
            "cos_details": cos_details,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_network_insights_cos_details_v2(**req_copy)


    def test_add_network_insights_cos_details_v2_value_error_with_retries(self):
        # Enable retries and run test_add_network_insights_cos_details_v2_value_error.
        _service.enable_retries()
        self.test_add_network_insights_cos_details_v2_value_error()

        # Disable retries and run test_add_network_insights_cos_details_v2_value_error.
        _service.disable_retries()
        self.test_add_network_insights_cos_details_v2_value_error()

class TestDeleteNetworkInsightsCosDetailsV2():
    """
    Test Class for delete_network_insights_cos_details_v2
    """

    @responses.activate
    def test_delete_network_insights_cos_details_v2_all_params(self):
        """
        delete_network_insights_cos_details_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/network-insights/cos')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        ids = ['testString']
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_network_insights_cos_details_v2(
            ids=ids,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ids'] == ['testString']

    def test_delete_network_insights_cos_details_v2_all_params_with_retries(self):
        # Enable retries and run test_delete_network_insights_cos_details_v2_all_params.
        _service.enable_retries()
        self.test_delete_network_insights_cos_details_v2_all_params()

        # Disable retries and run test_delete_network_insights_cos_details_v2_all_params.
        _service.disable_retries()
        self.test_delete_network_insights_cos_details_v2_all_params()

    @responses.activate
    def test_delete_network_insights_cos_details_v2_required_params(self):
        """
        test_delete_network_insights_cos_details_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/network-insights/cos')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        ids = ['testString']

        # Invoke method
        response = _service.delete_network_insights_cos_details_v2(
            ids=ids,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ids'] == ['testString']

    def test_delete_network_insights_cos_details_v2_required_params_with_retries(self):
        # Enable retries and run test_delete_network_insights_cos_details_v2_required_params.
        _service.enable_retries()
        self.test_delete_network_insights_cos_details_v2_required_params()

        # Disable retries and run test_delete_network_insights_cos_details_v2_required_params.
        _service.disable_retries()
        self.test_delete_network_insights_cos_details_v2_required_params()

    @responses.activate
    def test_delete_network_insights_cos_details_v2_value_error(self):
        """
        test_delete_network_insights_cos_details_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/network-insights/cos')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        ids = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_network_insights_cos_details_v2(**req_copy)


    def test_delete_network_insights_cos_details_v2_value_error_with_retries(self):
        # Enable retries and run test_delete_network_insights_cos_details_v2_value_error.
        _service.enable_retries()
        self.test_delete_network_insights_cos_details_v2_value_error()

        # Disable retries and run test_delete_network_insights_cos_details_v2_value_error.
        _service.disable_retries()
        self.test_delete_network_insights_cos_details_v2_value_error()

class TestAddActivityInsightsCosDetailsV2():
    """
    Test Class for add_activity_insights_cos_details_v2
    """

    @responses.activate
    def test_add_activity_insights_cos_details_v2_all_params(self):
        """
        add_activity_insights_cos_details_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/cos')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {}
        cos_details_v2_cos_details_item_model['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model['description'] = 'testString'
        cos_details_v2_cos_details_item_model['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model['cos_bucket_url'] = 'testString'

        # Set up parameter values
        region_id = 'testString'
        cos_details = [cos_details_v2_cos_details_item_model]
        transaction_id = 'testString'

        # Invoke method
        response = _service.add_activity_insights_cos_details_v2(
            region_id,
            cos_details,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['cos_details'] == [cos_details_v2_cos_details_item_model]

    def test_add_activity_insights_cos_details_v2_all_params_with_retries(self):
        # Enable retries and run test_add_activity_insights_cos_details_v2_all_params.
        _service.enable_retries()
        self.test_add_activity_insights_cos_details_v2_all_params()

        # Disable retries and run test_add_activity_insights_cos_details_v2_all_params.
        _service.disable_retries()
        self.test_add_activity_insights_cos_details_v2_all_params()

    @responses.activate
    def test_add_activity_insights_cos_details_v2_required_params(self):
        """
        test_add_activity_insights_cos_details_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/cos')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {}
        cos_details_v2_cos_details_item_model['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model['description'] = 'testString'
        cos_details_v2_cos_details_item_model['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model['cos_bucket_url'] = 'testString'

        # Set up parameter values
        region_id = 'testString'
        cos_details = [cos_details_v2_cos_details_item_model]

        # Invoke method
        response = _service.add_activity_insights_cos_details_v2(
            region_id,
            cos_details,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['cos_details'] == [cos_details_v2_cos_details_item_model]

    def test_add_activity_insights_cos_details_v2_required_params_with_retries(self):
        # Enable retries and run test_add_activity_insights_cos_details_v2_required_params.
        _service.enable_retries()
        self.test_add_activity_insights_cos_details_v2_required_params()

        # Disable retries and run test_add_activity_insights_cos_details_v2_required_params.
        _service.disable_retries()
        self.test_add_activity_insights_cos_details_v2_required_params()

    @responses.activate
    def test_add_activity_insights_cos_details_v2_value_error(self):
        """
        test_add_activity_insights_cos_details_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/cos')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {}
        cos_details_v2_cos_details_item_model['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model['description'] = 'testString'
        cos_details_v2_cos_details_item_model['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model['cos_bucket_url'] = 'testString'

        # Set up parameter values
        region_id = 'testString'
        cos_details = [cos_details_v2_cos_details_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "region_id": region_id,
            "cos_details": cos_details,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_activity_insights_cos_details_v2(**req_copy)


    def test_add_activity_insights_cos_details_v2_value_error_with_retries(self):
        # Enable retries and run test_add_activity_insights_cos_details_v2_value_error.
        _service.enable_retries()
        self.test_add_activity_insights_cos_details_v2_value_error()

        # Disable retries and run test_add_activity_insights_cos_details_v2_value_error.
        _service.disable_retries()
        self.test_add_activity_insights_cos_details_v2_value_error()

class TestDeleteActivityInsightsCosDetailsV2():
    """
    Test Class for delete_activity_insights_cos_details_v2
    """

    @responses.activate
    def test_delete_activity_insights_cos_details_v2_all_params(self):
        """
        delete_activity_insights_cos_details_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/cos')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        ids = ['testString']
        transaction_id = 'testString'

        # Invoke method
        response = _service.delete_activity_insights_cos_details_v2(
            ids=ids,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ids'] == ['testString']

    def test_delete_activity_insights_cos_details_v2_all_params_with_retries(self):
        # Enable retries and run test_delete_activity_insights_cos_details_v2_all_params.
        _service.enable_retries()
        self.test_delete_activity_insights_cos_details_v2_all_params()

        # Disable retries and run test_delete_activity_insights_cos_details_v2_all_params.
        _service.disable_retries()
        self.test_delete_activity_insights_cos_details_v2_all_params()

    @responses.activate
    def test_delete_activity_insights_cos_details_v2_required_params(self):
        """
        test_delete_activity_insights_cos_details_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/cos')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        ids = ['testString']

        # Invoke method
        response = _service.delete_activity_insights_cos_details_v2(
            ids=ids,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ids'] == ['testString']

    def test_delete_activity_insights_cos_details_v2_required_params_with_retries(self):
        # Enable retries and run test_delete_activity_insights_cos_details_v2_required_params.
        _service.enable_retries()
        self.test_delete_activity_insights_cos_details_v2_required_params()

        # Disable retries and run test_delete_activity_insights_cos_details_v2_required_params.
        _service.disable_retries()
        self.test_delete_activity_insights_cos_details_v2_required_params()

    @responses.activate
    def test_delete_activity_insights_cos_details_v2_value_error(self):
        """
        test_delete_activity_insights_cos_details_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/cos')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        ids = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_activity_insights_cos_details_v2(**req_copy)


    def test_delete_activity_insights_cos_details_v2_value_error_with_retries(self):
        # Enable retries and run test_delete_activity_insights_cos_details_v2_value_error.
        _service.enable_retries()
        self.test_delete_activity_insights_cos_details_v2_value_error()

        # Disable retries and run test_delete_activity_insights_cos_details_v2_value_error.
        _service.disable_retries()
        self.test_delete_activity_insights_cos_details_v2_value_error()

# endregion
##############################################################################
# End of Service: AddonManagerCos
##############################################################################

##############################################################################
# Start of Service: AddonManagerDisable
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AddonMgrV1.new_instance(
            account_id=account_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AddonMgrV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=account_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AddonMgrV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='account_id must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=None,
            )
class TestDisableInsightsV2():
    """
    Test Class for disable_insights_v2
    """

    @responses.activate
    def test_disable_insights_v2_all_params(self):
        """
        disable_insights_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/disable')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'
        network_insights = True
        activity_insights = True
        transaction_id = 'testString'

        # Invoke method
        response = _service.disable_insights_v2(
            region_id,
            network_insights=network_insights,
            activity_insights=activity_insights,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['network-insights'] == True
        assert req_body['activity-insights'] == True

    def test_disable_insights_v2_all_params_with_retries(self):
        # Enable retries and run test_disable_insights_v2_all_params.
        _service.enable_retries()
        self.test_disable_insights_v2_all_params()

        # Disable retries and run test_disable_insights_v2_all_params.
        _service.disable_retries()
        self.test_disable_insights_v2_all_params()

    @responses.activate
    def test_disable_insights_v2_required_params(self):
        """
        test_disable_insights_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/disable')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'
        network_insights = True
        activity_insights = True

        # Invoke method
        response = _service.disable_insights_v2(
            region_id,
            network_insights=network_insights,
            activity_insights=activity_insights,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['network-insights'] == True
        assert req_body['activity-insights'] == True

    def test_disable_insights_v2_required_params_with_retries(self):
        # Enable retries and run test_disable_insights_v2_required_params.
        _service.enable_retries()
        self.test_disable_insights_v2_required_params()

        # Disable retries and run test_disable_insights_v2_required_params.
        _service.disable_retries()
        self.test_disable_insights_v2_required_params()

    @responses.activate
    def test_disable_insights_v2_value_error(self):
        """
        test_disable_insights_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/disable')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'
        network_insights = True
        activity_insights = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "region_id": region_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.disable_insights_v2(**req_copy)


    def test_disable_insights_v2_value_error_with_retries(self):
        # Enable retries and run test_disable_insights_v2_value_error.
        _service.enable_retries()
        self.test_disable_insights_v2_value_error()

        # Disable retries and run test_disable_insights_v2_value_error.
        _service.disable_retries()
        self.test_disable_insights_v2_value_error()

# endregion
##############################################################################
# End of Service: AddonManagerDisable
##############################################################################

##############################################################################
# Start of Service: AddonManagerEnable
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AddonMgrV1.new_instance(
            account_id=account_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AddonMgrV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=account_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AddonMgrV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='account_id must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=None,
            )
class TestEnableInsightsV2():
    """
    Test Class for enable_insights_v2
    """

    @responses.activate
    def test_enable_insights_v2_all_params(self):
        """
        enable_insights_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/enable')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'
        network_insights = True
        activity_insights = True
        transaction_id = 'testString'

        # Invoke method
        response = _service.enable_insights_v2(
            region_id,
            network_insights=network_insights,
            activity_insights=activity_insights,
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['network-insights'] == True
        assert req_body['activity-insights'] == True

    def test_enable_insights_v2_all_params_with_retries(self):
        # Enable retries and run test_enable_insights_v2_all_params.
        _service.enable_retries()
        self.test_enable_insights_v2_all_params()

        # Disable retries and run test_enable_insights_v2_all_params.
        _service.disable_retries()
        self.test_enable_insights_v2_all_params()

    @responses.activate
    def test_enable_insights_v2_required_params(self):
        """
        test_enable_insights_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/enable')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'
        network_insights = True
        activity_insights = True

        # Invoke method
        response = _service.enable_insights_v2(
            region_id,
            network_insights=network_insights,
            activity_insights=activity_insights,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'
        assert req_body['network-insights'] == True
        assert req_body['activity-insights'] == True

    def test_enable_insights_v2_required_params_with_retries(self):
        # Enable retries and run test_enable_insights_v2_required_params.
        _service.enable_retries()
        self.test_enable_insights_v2_required_params()

        # Disable retries and run test_enable_insights_v2_required_params.
        _service.disable_retries()
        self.test_enable_insights_v2_required_params()

    @responses.activate
    def test_enable_insights_v2_value_error(self):
        """
        test_enable_insights_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/enable')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'
        network_insights = True
        activity_insights = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "region_id": region_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.enable_insights_v2(**req_copy)


    def test_enable_insights_v2_value_error_with_retries(self):
        # Enable retries and run test_enable_insights_v2_value_error.
        _service.enable_retries()
        self.test_enable_insights_v2_value_error()

        # Disable retries and run test_enable_insights_v2_value_error.
        _service.disable_retries()
        self.test_enable_insights_v2_value_error()

# endregion
##############################################################################
# End of Service: AddonManagerEnable
##############################################################################

##############################################################################
# Start of Service: AddonManagerInsights
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AddonMgrV1.new_instance(
            account_id=account_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AddonMgrV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=account_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AddonMgrV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='account_id must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=None,
            )
class TestGetSupportedInsightsV2():
    """
    Test Class for get_supported_insights_v2
    """

    @responses.activate
    def test_get_supported_insights_v2_all_params(self):
        """
        get_supported_insights_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/insights')
        mock_response = '{"type": ["network-insights"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        transaction_id = 'testString'

        # Invoke method
        response = _service.get_supported_insights_v2(
            transaction_id=transaction_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_supported_insights_v2_all_params_with_retries(self):
        # Enable retries and run test_get_supported_insights_v2_all_params.
        _service.enable_retries()
        self.test_get_supported_insights_v2_all_params()

        # Disable retries and run test_get_supported_insights_v2_all_params.
        _service.disable_retries()
        self.test_get_supported_insights_v2_all_params()

    @responses.activate
    def test_get_supported_insights_v2_required_params(self):
        """
        test_get_supported_insights_v2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/insights')
        mock_response = '{"type": ["network-insights"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_supported_insights_v2()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_supported_insights_v2_required_params_with_retries(self):
        # Enable retries and run test_get_supported_insights_v2_required_params.
        _service.enable_retries()
        self.test_get_supported_insights_v2_required_params()

        # Disable retries and run test_get_supported_insights_v2_required_params.
        _service.disable_retries()
        self.test_get_supported_insights_v2_required_params()

    @responses.activate
    def test_get_supported_insights_v2_value_error(self):
        """
        test_get_supported_insights_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/insights')
        mock_response = '{"type": ["network-insights"]}'
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
                _service.get_supported_insights_v2(**req_copy)


    def test_get_supported_insights_v2_value_error_with_retries(self):
        # Enable retries and run test_get_supported_insights_v2_value_error.
        _service.enable_retries()
        self.test_get_supported_insights_v2_value_error()

        # Disable retries and run test_get_supported_insights_v2_value_error.
        _service.disable_retries()
        self.test_get_supported_insights_v2_value_error()

# endregion
##############################################################################
# End of Service: AddonManagerInsights
##############################################################################

##############################################################################
# Start of Service: AddonManagerTestFindings
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AddonMgrV1.new_instance(
            account_id=account_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AddonMgrV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=account_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AddonMgrV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='account_id must be provided'):
            service = AddonMgrV1.new_instance(
                account_id=None,
            )
class TestTestAiFindingsV2():
    """
    Test Class for test_ai_findings_v2
    """

    @responses.activate
    def test_test_ai_findings_v2_all_params(self):
        """
        test_ai_findings_v2()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/test-ai-findings')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'

        # Invoke method
        response = _service.test_ai_findings_v2(
            region_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['region_id'] == 'testString'

    def test_test_ai_findings_v2_all_params_with_retries(self):
        # Enable retries and run test_test_ai_findings_v2_all_params.
        _service.enable_retries()
        self.test_test_ai_findings_v2_all_params()

        # Disable retries and run test_test_ai_findings_v2_all_params.
        _service.disable_retries()
        self.test_test_ai_findings_v2_all_params()

    @responses.activate
    def test_test_ai_findings_v2_value_error(self):
        """
        test_test_ai_findings_v2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/addons/testString/activity-insights/test-ai-findings')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        region_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "region_id": region_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.test_ai_findings_v2(**req_copy)


    def test_test_ai_findings_v2_value_error_with_retries(self):
        # Enable retries and run test_test_ai_findings_v2_value_error.
        _service.enable_retries()
        self.test_test_ai_findings_v2_value_error()

        # Disable retries and run test_test_ai_findings_v2_value_error.
        _service.disable_retries()
        self.test_test_ai_findings_v2_value_error()

# endregion
##############################################################################
# End of Service: AddonManagerTestFindings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AllInsights():
    """
    Test Class for AllInsights
    """

    def test_all_insights_serialization(self):
        """
        Test serialization/deserialization for AllInsights
        """

        # Construct a json representation of a AllInsights model
        all_insights_model_json = {}
        all_insights_model_json['type'] = ['network-insights']

        # Construct a model instance of AllInsights by calling from_dict on the json representation
        all_insights_model = AllInsights.from_dict(all_insights_model_json)
        assert all_insights_model != False

        # Construct a model instance of AllInsights by calling from_dict on the json representation
        all_insights_model_dict = AllInsights.from_dict(all_insights_model_json).__dict__
        all_insights_model2 = AllInsights(**all_insights_model_dict)

        # Verify the model instances are equivalent
        assert all_insights_model == all_insights_model2

        # Convert model instance back to dict and verify no loss of data
        all_insights_model_json2 = all_insights_model.to_dict()
        assert all_insights_model_json2 == all_insights_model_json

class TestModel_CosDetailsV2CosDetailsItem():
    """
    Test Class for CosDetailsV2CosDetailsItem
    """

    def test_cos_details_v2_cos_details_item_serialization(self):
        """
        Test serialization/deserialization for CosDetailsV2CosDetailsItem
        """

        # Construct a json representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model_json = {}
        cos_details_v2_cos_details_item_model_json['cos_instance'] = 'testString'
        cos_details_v2_cos_details_item_model_json['bucket_name'] = 'testString'
        cos_details_v2_cos_details_item_model_json['description'] = 'testString'
        cos_details_v2_cos_details_item_model_json['type'] = 'network-insights'
        cos_details_v2_cos_details_item_model_json['cos_bucket_url'] = 'testString'

        # Construct a model instance of CosDetailsV2CosDetailsItem by calling from_dict on the json representation
        cos_details_v2_cos_details_item_model = CosDetailsV2CosDetailsItem.from_dict(cos_details_v2_cos_details_item_model_json)
        assert cos_details_v2_cos_details_item_model != False

        # Construct a model instance of CosDetailsV2CosDetailsItem by calling from_dict on the json representation
        cos_details_v2_cos_details_item_model_dict = CosDetailsV2CosDetailsItem.from_dict(cos_details_v2_cos_details_item_model_json).__dict__
        cos_details_v2_cos_details_item_model2 = CosDetailsV2CosDetailsItem(**cos_details_v2_cos_details_item_model_dict)

        # Verify the model instances are equivalent
        assert cos_details_v2_cos_details_item_model == cos_details_v2_cos_details_item_model2

        # Convert model instance back to dict and verify no loss of data
        cos_details_v2_cos_details_item_model_json2 = cos_details_v2_cos_details_item_model.to_dict()
        assert cos_details_v2_cos_details_item_model_json2 == cos_details_v2_cos_details_item_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
