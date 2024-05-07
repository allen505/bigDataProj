#!/bin/bash

conda create -n bigdata python==3.10
source activate bigdata
echo "Activated Conda env $CONDA_PREFIX"

pip install jupyter
pip install pandas
pip install numpy
pip install pymongo
pip install py7zr

echo "************************"
echo "Installed all the dependencies"