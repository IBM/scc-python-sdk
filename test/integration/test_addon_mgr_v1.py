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
Integration Tests for AddonMgrV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_scc.addon_mgr_v1 import *

account_id = "testString"

# Config file name
config_file = "addon_mgr_v1.env"


class TestAddonMgrV1:
    """
    Integration Test Class for AddonMgrV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            cls.addon_mgr_service = AddonMgrV1.new_instance(account_id=account_id)
            assert cls.addon_mgr_service is not None

            cls.config = read_external_sources(AddonMgrV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.addon_mgr_service.enable_retries()

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_add_network_insights_cos_details_v2(self):

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {
            "cos_instance": "testString",
            "bucket_name": "testString",
            "description": "testString",
            "type": "network-insights",
            "cos_bucket_url": "testString",
        }

        add_network_insights_cos_details_v2_response = (
            self.addon_mgr_service.add_network_insights_cos_details_v2(
                region_id="testString",
                cos_details=[cos_details_v2_cos_details_item_model],
            )
        )

        assert add_network_insights_cos_details_v2_response.get_status_code() == 200

    @needscredentials
    def test_add_activity_insights_cos_details_v2(self):

        # Construct a dict representation of a CosDetailsV2CosDetailsItem model
        cos_details_v2_cos_details_item_model = {
            "cos_instance": "testString",
            "bucket_name": "testString",
            "description": "testString",
            "type": "network-insights",
            "cos_bucket_url": "testString",
        }

        add_activity_insights_cos_details_v2_response = (
            self.addon_mgr_service.add_activity_insights_cos_details_v2(
                region_id="testString",
                cos_details=[cos_details_v2_cos_details_item_model],
            )
        )

        assert add_activity_insights_cos_details_v2_response.get_status_code() == 200

    @needscredentials
    def test_disable_insights_v2(self):

        disable_insights_v2_response = self.addon_mgr_service.disable_insights_v2(
            region_id="testString",
            network_insights=True,
            activity_insights=True,
        )

        assert disable_insights_v2_response.get_status_code() == 200

    @needscredentials
    def test_enable_insights_v2(self):

        enable_insights_v2_response = self.addon_mgr_service.enable_insights_v2(
            region_id="testString",
            network_insights=True,
            activity_insights=True,
        )

        assert enable_insights_v2_response.get_status_code() == 200

    @needscredentials
    def test_get_supported_insights_v2(self):

        get_supported_insights_v2_response = (
            self.addon_mgr_service.get_supported_insights_v2()
        )

        assert get_supported_insights_v2_response.get_status_code() == 200
        all_insights = get_supported_insights_v2_response.get_result()
        assert all_insights is not None

    @needscredentials
    def test_test_ai_findings_v2(self):

        test_ai_findings_v2_response = self.addon_mgr_service.test_ai_findings_v2(
            region_id="testString"
        )

        assert test_ai_findings_v2_response.get_status_code() == 200

    @needscredentials
    def test_delete_network_insights_cos_details_v2(self):

        delete_network_insights_cos_details_v2_response = (
            self.addon_mgr_service.delete_network_insights_cos_details_v2(
                ids=["testString"],
            )
        )

        assert delete_network_insights_cos_details_v2_response.get_status_code() == 200

    @needscredentials
    def test_delete_activity_insights_cos_details_v2(self):

        delete_activity_insights_cos_details_v2_response = (
            self.addon_mgr_service.delete_activity_insights_cos_details_v2(
                ids=["testString"],
            )
        )

        assert delete_activity_insights_cos_details_v2_response.get_status_code() == 200
