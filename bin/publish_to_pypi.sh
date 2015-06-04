#!/bin/bash -x
set -o errexit -o pipefail

# move the dcos package
cd /dcos-node

TAG_VERSION=`cat tag-version`

# replace SNAPSHOT with tagged version
sed -i "s/version = 'SNAPSHOT'/version = '$TAG_VERSION'/g" myriad/__init__.py

# copy generated pypirc configuration to correct location
cp .pypirc ~/.pypirc

make clean env
source env/bin/activate
env/bin/python setup.py bdist_wheel upload
echo "Wheel should now be online at: https://pypi.python.org/pypi/dcos_myriad"
deactivate
