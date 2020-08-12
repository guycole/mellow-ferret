#!/bin/bash
#
# Title: pytest.sh
# Description: invoke pytest
# Development Environment: OS X 10.11.6
# Author: G.S. Cole (guy at shastrax dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
export PYTHONPATH=$HOME/IdeaProjects/mellow-ferret/src
#echo $PYTHONPATH
#
source ./src/venv/bin/activate
#
pytest tests/*.py
#
#if [[ $1 = "apigw" ]];
#then
#    echo "integration test"
#    pytest tests/integration_v01/*.py;
#else
#    echo "unit test"
#    pytest tests/unit_v01/*.py
#fi
#