#!/bin/bash

set -euo pipefail

curl https://us-south.functions.appdomain.cloud/api/v1/web/e6b54af6-ab44-4149-a8e4-e906dcc58136/default/secadvstg-location-shift.json
echo "${CONFIGURATION_GOVERNANCE_ENV}" | base64 -d >> configuration_governance_v1.env
python -m pytest test/integration
