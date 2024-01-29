#!/bin/bash
set -euo pipefail
echo "${SCC_ENV}" | base64 -d >> security_and_compliance_center_api_v3.env
python -m pytest tests/integration
