#!/bin/bash

# create our virtual env
python -m virtualenv venv
source venv/bin/activate

# install our deps
pip install -r requirements.txt

# run our test files
echo "create performance"
python create_perf.py

echo "create hierarchy"
python create_hier.py

echo "create top and bottom"
python create_tb.py

echo "create e-mail"
python create_mail.py
