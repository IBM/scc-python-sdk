#!/bin/bash
set -e

print_usage () {
    echo "
usage:
   ./prepare_project.sh [-n SDK_PACKAGE_NAME] [-d \"Project Description\"] [-g GIT_URL] [-s SDK_NAME] [-a AUTHOR_EMAIL] [-c SERVICE_CATEGORY] [-h]
where:
   -n: specify the project's main package directory name (e.g. ibm_platform_services)
   -d: specify project description string (e.g. \"IBM Cloud Platform Services Python SDK\")
   -g: specify the git url (e.g. https://github.com/IBM/platform-services-python-sdk)
   -s: specify sdk name string (e.g. \"Platform Services\")
   -a: specify the author's email address (e.g. email@ibm.com)
   -c: specify the service category (e.g. platform-services)
   -h: view usage instructions
"
}

# Parse flags and arguments
while getopts 'n:p:d:g:s:a:c:h' flag; do
  case "${flag}" in
    n) SDK_PACKAGE_NAME=${OPTARG} ;;
    d) PROJECT_DESCRIPTION=${OPTARG} ;;
    g) PROJECT_GIT_URL=${OPTARG} ;;
    s) SDK_NAME=${OPTARG} ;;
    a) AUTHOR_EMAIL=${OPTARG} ;;
    c) SERVICE_CATEGORY=${OPTARG} ;;
    *) print_usage
        exit 1 ;;
  esac
done

if [[ -z "$SDK_PACKAGE_NAME" || -z "$PROJECT_DESCRIPTION" || -z "$PROJECT_GIT_URL" || -z "$SDK_NAME" || -z "$AUTHOR_EMAIL" || -z "$SERVICE_CATEGORY" ]]; then
    printf "Please provide all required inputs.\n\n"
    print_usage

else

    printf "\n>>>>> Project Initialization In Progress...\n\t SDK_PACKAGE_PACKAGE_NAME: ${SDK_PACKAGE_NAME}\n\t PROJECT_DESCRIPTION: ${PROJECT_DESCRIPTION}\n\t PROJECT_GIT_URL: ${PROJECT_GIT_URL}\n\t SDK_NAME: ${SDK_NAME}\n\t AUTHOR_EMAIL: ${AUTHOR_EMAIL}\n\t SERVICE_CATEGORY: ${SERVICE_CATEGORY}\n"

    # Remove sample files
    rm test/integration/test_example_service_v1.py
    rm test/unit/test_example_service_v1.py
    rm mysdk/example_service_v1.py
    printf "\n>>>>> Example Service files removed."

    # Update directory name
    if [[ $SDK_PACKAGE_NAME != "mysdk" ]]; then
        mv mysdk $SDK_PACKAGE_NAME
        printf "\n>>>>> Directory structure updated."
    fi

    # Update gitignore
    sed -i.bak 's/^example-service/# example-service/' .gitignore
    rm .gitignore.bak
    printf "\n>>>>> .gitignore updated."

    # Update .travis.yml
    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' .travis.yml
    sed -i.bak '/After creating your SDK/d' .travis.yml
    sed -i.bak '/# uncomment this/d' .travis.yml
    sed -i.bak "/# matrix:/,/#     - python: 3.8/s/^# //g" .travis.yml
    sed -i.bak '/# remove this entire/,/setup_and_generate.sh/d' .travis.yml
    rm .travis.yml.bak
    printf "\n>>>>> .travis.yml updated."

    # Update supplemental files
    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' pylint.sh
    rm pylint.sh.bak
    printf "\n>>>>> pylint.sh updated."

    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' .bumpversion.cfg
    rm .bumpversion.cfg.bak
    printf "\n>>>>> .bumpversion.cfg updated."

    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' tox.ini
    rm tox.ini.bak
    printf "\n>>>>> tox.ini updated."

    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' $SDK_PACKAGE_NAME/version.py
    rm $SDK_PACKAGE_NAME/version.py.bak
    printf "\n>>>>> ${SDK_PACKAGE_NAME}/version.py updated."

    # Update python initialization files
    SDK_AGENT="$( sed 's~.*/.*/~~' <<< "$PROJECT_GIT_URL" )"
    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' $SDK_PACKAGE_NAME/common.py
    sed -i.bak 's/my-python-sdk/'${SDK_AGENT}'/' $SDK_PACKAGE_NAME/common.py
    rm $SDK_PACKAGE_NAME/common.py.bak
    printf "\n>>>>> ${SDK_PACKAGE_NAME}/common.py updated."

    sed -i.bak 's/my-python-sdk/'${SDK_AGENT}'/' test/unit/test_common.py
    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' test/unit/test_common.py
    rm test/unit/test_common.py.bak
    printf "\n>>>>> test/unit/test_common.py updated."

    sed -i.bak "s/Python client library for the IBM Cloud MySDK Services/${PROJECT_DESCRIPTION}/" $SDK_PACKAGE_NAME/__init__.py
    sed -i.bak "s/from .example_service_v1 import ExampleServiceV1/# from .example_service_v1 import ExampleServiceV1/" $SDK_PACKAGE_NAME/__init__.py
    rm $SDK_PACKAGE_NAME/__init__.py.bak
    printf "\n>>>>> ${SDK_PACKAGE_NAME}/__init__.py updated."

    sed -i.bak "s~https://github.com/mysdk/python-sdk~${PROJECT_GIT_URL}~" setup.py
    sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' setup.py
    sed -i.bak "s/Python client library for IBM Cloud MYSDK Services/${PROJECT_DESCRIPTION}/" setup.py
    sed -i.bak 's/devxsdk@us.ibm.com/'${AUTHOR_EMAIL}'/' setup.py
    rm setup.py.bak
    printf "\n>>>>> setup.py updated."

    # Update documentation
    sed -i.bak "s/^# .*/# ${PROJECT_DESCRIPTION}/" README.md
    sed -i.bak "s/travis.ibm.com/travis-ci.com/" README.md
    sed -i.bak "s/MySDK Service/${SDK_NAME}/" README.md
    sed -i.bak "s/MySDK/${SDK_NAME}/" README.md
    PYPI_NAME="$( sed 's~_~-~g' <<< "$SDK_PACKAGE_NAME" )"
    sed -i.bak "s/mysdk/${PYPI_NAME}/" README.md
    sed -i.bak "s/<service-category>/${SERVICE_CATEGORY}/" README.md
    sed -i.bak "s~<github-repo-url>~${PROJECT_GIT_URL}~" README.md
    sed -i.bak "s~https://github.ibm.com/CloudEngineering/python-sdk-template~${PROJECT_GIT_URL}~" README.md
    sed -i.bak "s~^\[Example Service\].*~<!-- [Example Service](https://cloud.ibm.com/apidocs/example-service) | exampleservicev1 -->~" README.md
    GH_SLUG="$( sed 's~.*.com/~~' <<< "$PROJECT_GIT_URL" )"
    sed -i.bak "s~CloudEngineering/python-sdk-template~${GH_SLUG}~g" README.md

    rm README.md.bak
    printf "\n>>>>> README.md updated."

    sed -i.bak "s~<github-repo-url>~${PROJECT_GIT_URL}~" CONTRIBUTING.md
    rm CONTRIBUTING.md.bak
    printf "\n>>>>> CONTRIBUTING.md updated."

    printf "\n>>>>> Project Initialized Successfully!\n"
fi
