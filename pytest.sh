#!/bin/bash
#
# Title: pytest.sh
# Description: invoke pytest
# Development Environment:Ubuntu 18
# Author:Guy Cole (guycole at gmail dot com)
#
#PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
export PYTHONPATH=$HOME/IdeaProjects/mellow-ferret/src
export PYTHONPATH=$HOME/github/mellow-ferret/src
#echo $PYTHONPATH
#
source ./src/venv/bin/activate
#
pytest tests/*.py
#
