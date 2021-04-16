[![Build Status](https://travis.ibm.com/CloudEngineering/python-sdk-template.svg?token=eW5FVD71iyte6tTby8gr&branch=main)](https://travis.ibm.com/CloudEngineering/python-sdk-template)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud Security & Compliance Center Python SDK Version 0.0.1

Python client library to interact with various [IBM Cloud Security & Compliance Center APIs](https://cloud.ibm.com/apidocs/security-and-compliance-center).

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

The IBM Cloud MySDK Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name
--- | ---
[FindingsApiV1](https://cloud.ibm.com/apidocs/security-and-compliance-center/findings) | FindingsApiV1
[NotificationsApiV1](https://cloud.ibm.com/apidocs/security-and-compliance-center/notifications) | NotificationsApiV1
[ConfigurationGovernanceApiV1](https://cloud.ibm.com/apidocs/security-and-compliance-center/configuration-governance) | ConfigurationGovernanceApiV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.6 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "security-and-compliance-center-sdk>=0.0.1"
```

or

```bash
easy_install --upgrade "security-and-compliance-center-sdk>=0.0.1"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/ibm-cloud-security/scc-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.ibm.com/CloudEngineering/python-sdk-template/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.ibm.com/CloudEngineering/python-sdk-template/blob/main/LICENSE).
