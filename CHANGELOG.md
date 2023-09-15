# [4.0.0](https://github.com/IBM/scc-python-sdk/compare/v3.0.0...v4.0.0) (2023-09-15)


### Performance Improvements

* **SCC:** Releasing SCC v2 Python SDK ([9471fdc](https://github.com/IBM/scc-python-sdk/commit/9471fdc46456c371c0fa014514a3437e00f8e917))


### BREAKING CHANGES

* **SCC:** SCC v2 Python SDK

Signed-off-by: Gaurav Goswami <gouravgoswami48@gmail.com>

# [3.0.0](https://github.com/IBM/scc-python-sdk/compare/v2.0.0...v3.0.0) (2022-08-04)


### Bug Fixes

* **FindingsAPI:** deprecated ([e4fa001](https://github.com/IBM/scc-python-sdk/commit/e4fa0014c33c65fe559ad41d3ab101968a0f34c5))


* Merge pull request #34 from IBM/si-deprecation ([8ec9c21](https://github.com/IBM/scc-python-sdk/commit/8ec9c21e9acc608443064a126455568a0ee8cb9f)), closes [#34](https://github.com/IBM/scc-python-sdk/issues/34)


### BREAKING CHANGES

* Deprecating Security Insights
* **FindingsAPI:** deprecating Security Insights

# [2.0.0](https://github.com/IBM/scc-python-sdk/compare/v1.1.2...v2.0.0) (2021-12-20)


* Merge pull request #32 from IBM/deprecate ([a9bd032](https://github.com/IBM/scc-python-sdk/commit/a9bd032957f8e4bcc8c8aba9b9703edaf37af1d9)), closes [#32](https://github.com/IBM/scc-python-sdk/issues/32)


### BREAKING CHANGES

* deprecating NotificationsAPI

## [1.1.2](https://github.com/IBM/scc-python-sdk/compare/v1.1.1...v1.1.2) (2021-12-10)


### Bug Fixes

* **FindingsAPI:** getOccurrence should not return list ([f5a9c7f](https://github.com/IBM/scc-python-sdk/commit/f5a9c7fcc8c761401a6b0507b259ed64dc72eb12))

## [1.1.1](https://github.com/IBM/scc-python-sdk/compare/v1.1.0...v1.1.1) (2021-10-12)


### Bug Fixes

* **Findings:** createTime and updateTime in NoteOptions ([71c4027](https://github.com/IBM/scc-python-sdk/commit/71c4027c385e01ad07d26f90aedaee8124bb0015))

# [1.1.0](https://github.com/IBM/scc-python-sdk/compare/v1.0.0...v1.1.0) (2021-10-11)


### Bug Fixes

* **SemanticRelease:** latest SR needs node version >= 14.17 ([5056a2d](https://github.com/IBM/scc-python-sdk/commit/5056a2df197da9b7c556b1c0f7467483384a9e9e))


### Features

* **kpi severity:** Add severity for kpi ([e0ea982](https://github.com/IBM/scc-python-sdk/commit/e0ea982180263abf5b58aa377f1d3ebe7a0f0bdf))

# [1.0.0](https://github.com/IBM/scc-python-sdk/compare/v0.0.15...v1.0.0) (2021-06-30)


* Merge pull request #21 from IBM/major ([04bc0fa](https://github.com/IBM/scc-python-sdk/commit/04bc0fa87019807d88a6b266227854af1517404c)), closes [#21](https://github.com/IBM/scc-python-sdk/issues/21)


### BREAKING CHANGES

* Major release for GA

## [0.0.15](https://github.com/IBM/scc-python-sdk/compare/v0.0.14...v0.0.15) (2021-06-25)


### Bug Fixes

* **SDK:** regeneration after content review ([fb8f030](https://github.com/IBM/scc-python-sdk/commit/fb8f0304ec143013699a5a257adbc7f8f14448be))
* **SDK:** TransactionID parameter to comply with findingsapi ([80cacfa](https://github.com/IBM/scc-python-sdk/commit/80cacfadbb9ca32be6359852666b3b9b0fc1970e))

## [0.0.14](https://github.com/IBM/scc-python-sdk/compare/v0.0.13...v0.0.14) (2021-06-21)


### Bug Fixes

* **pdoc:** install dependencies before generating pydoc ([362b9f6](https://github.com/IBM/scc-python-sdk/commit/362b9f6c6de0a338acdb780cb429664d3a0c14dc))

## [0.0.13](https://github.com/IBM/scc-python-sdk/compare/v0.0.12...v0.0.13) (2021-06-18)


### Bug Fixes

* **PyPi:** redirection issue while publishing ([69e8651](https://github.com/IBM/scc-python-sdk/commit/69e8651721f9efa15a89d4955b8ea7c39e299523))

## [0.0.12](https://github.com/IBM/scc-python-sdk/compare/v0.0.11...v0.0.12) (2021-06-18)


### Bug Fixes

* **PyPi:** build project before publishing ([476bb6e](https://github.com/IBM/scc-python-sdk/commit/476bb6e60b84930f92e4a05de96c7d2a209c3a9a))

## [0.0.11](https://github.com/IBM/scc-python-sdk/compare/v0.0.10...v0.0.11) (2021-06-18)


### Bug Fixes

* **GithubAction:** workflow altered ([306c588](https://github.com/IBM/scc-python-sdk/commit/306c588b8e1c46de1179fb017d843340291ed36d))

## [0.0.10](https://github.com/IBM/scc-python-sdk/compare/v0.0.9...v0.0.10) (2021-06-14)


### Bug Fixes

* **ITs:** config-gov ITs fixed ([07e4dd3](https://github.com/IBM/scc-python-sdk/commit/07e4dd398004e57d56c458430a00c057a9722cda))

## [0.0.9](https://github.com/IBM/scc-python-sdk/compare/v0.0.8...v0.0.9) (2021-06-14)


### Bug Fixes

* **SDK:** release with common FID ([7cc0ab0](https://github.com/IBM/scc-python-sdk/commit/7cc0ab0bf382dba70c73e5bd1c3992e336ad11b8))

## [0.0.8](https://github.com/IBM/scc-python-sdk/compare/v0.0.7...v0.0.8) (2021-06-11)


### Bug Fixes

* **listProviders:** Addressed api definition review comments ([9c1f8e5](https://github.com/IBM/scc-python-sdk/commit/9c1f8e5ce5183aed046432d76688c7fa46a97f91))

## [0.0.7](https://github.com/IBM/scc-python-sdk/compare/v0.0.6...v0.0.7) (2021-06-07)


### Bug Fixes

* **PyPI:** releasing new version ([d2795b4](https://github.com/IBM/scc-python-sdk/commit/d2795b46ad07363f4402db0a039a2be703ffa6b4))

## [0.0.6](https://github.com/IBM/scc-python-sdk/compare/v0.0.5...v0.0.6) (2021-06-07)


### Bug Fixes

* **SDK:** IBM Cloud SCC Python SDK ([926aa3a](https://github.com/IBM/scc-python-sdk/commit/926aa3af40ad73aa5d302df704b5a5dee57b7e14))

## [0.0.5](https://github.com/IBM/scc-python-sdk/compare/v0.0.4...v0.0.5) (2021-06-02)


### Bug Fixes

* **FINDINGS ITs:** removed order from card note, to resolve conflict ([09ce3c3](https://github.com/IBM/scc-python-sdk/commit/09ce3c332a878164d8317dd131a671cee668f121))
* **SemanticRelease:** skip CI ops on SR commits ([848c267](https://github.com/IBM/scc-python-sdk/commit/848c267b403da9fd69258b3842a4daeffb5c2f2d))

## [0.0.4](https://github.com/IBM/scc-python-sdk/compare/v0.0.3...v0.0.4) (2021-06-02)


### Bug Fixes

* **SDK:** IBM Cloud SCC Python SDK ([1754a4c](https://github.com/IBM/scc-python-sdk/commit/1754a4c6d808ebaa194df4a51166a3a2b83150be))
* **SDK:** IBM Cloud SCC Python SDK ([970acae](https://github.com/IBM/scc-python-sdk/commit/970acaeb0b081918d283df0cfad27af30e67e8db))
* **TestScript:** ITs script should exit with error code for test failure ([b6cd3ab](https://github.com/IBM/scc-python-sdk/commit/b6cd3ab142ea8628af4ccf0cd175449459c79b7a))

## [0.0.3](https://github.com/IBM/scc-python-sdk/compare/v0.0.2...v0.0.3) (2021-05-27)


### Bug Fixes

* **TRI:** region based service url feature added ([35e711c](https://github.com/IBM/scc-python-sdk/commit/35e711c7b62b841a612801996b3c612953ed6960))
* **TRI:** region based service url feature added ([ca562a8](https://github.com/IBM/scc-python-sdk/commit/ca562a8503e5063dec2394d139854ebd3b87df36))

## [0.0.2](https://github.com/IBM/scc-python-sdk/compare/v0.0.1...v0.0.2) (2021-04-27)


### Bug Fixes

* **IBM Cloud SCC:** first release ([167a813](https://github.com/IBM/scc-python-sdk/commit/167a8138d0c78142dbad2e4defdef5cd53e5da1e))
* **IBM Cloud SCC:** first release ([8da4e3a](https://github.com/IBM/scc-python-sdk/commit/8da4e3ac72659864d94c913bed6dee3c8d0fb058))
