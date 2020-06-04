#! /bin/bash -e

# workaround to have conda working
eval "$(conda shell.bash hook)"

environment_header=$(head -n 1 environment.yml)
environment_name=${environment_header/name: /}

conda activate "${environment_name}"

echo "Running Black..."
black .

echo "Running Flake8..."
flake8 .

echo "Running pyDocStyle..."
pydocstyle .

echo "Running MyPy..."
mypy src

echo "Congratulations! All went well."