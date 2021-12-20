[![CI/CD Pipeline](https://github.com/IBM/scc-python-sdk/actions/workflows/main.yaml/badge.svg)](https://github.com/IBM/scc-python-sdk/actions/workflows/main.yaml)
[![PyDoc](https://img.shields.io/static/v1?label=pydoc&message=latest&color=blue)](http://IBM.github.io/scc-python-sdk)
[![Release](https://img.shields.io/github/v/release/IBM/scc-python-sdk)](https://img.shields.io/github/v/release/IBM/scc-python-sdk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibm-platform-services)](https://pypi.org/project/ibm-scc/)
[![PyPi](https://badge.fury.io/py/ibm-scc.svg)](https://pypi.python.org/pypi/ibm-scc/)
[![PyPi](https://img.shields.io/pypi/dw/ibm-scc.svg)](https://pypi.python.org/pypi/ibm-scc/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a87748d845549d045483/test_coverage)](https://codeclimate.com/github/IBM/scc-python-sdk/test_coverage)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud Security & Compliance Center Python SDK Version 2.0.0

Python client library to interact with various [IBM Cloud Security & Compliance Center APIs](https://cloud.ibm.com/docs?tab=api-docs&category=platform_services%2Csecurity).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Security & Compliance Center Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Module Name | Imported Class Name
--- | --- | ---
[Findings](https://cloud.ibm.com/apidocs/security-compliance/findings) | findings_v1 | FindingsV1
[Configuration Governance](https://cloud.ibm.com/apidocs/security-compliance/config) | configuration_governance_v1 | ConfigurationGovernanceV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.6 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-scc>=2.0.0"
```

or

```bash
easy_install --upgrade "ibm-scc>=2.0.0"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/scc-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.ibm.com/CloudEngineering/python-sdk-template/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.ibm.com/CloudEngineering/python-sdk-template/blob/main/LICENSE).
