# !/bin/sh


# install dependencies
pip install pandas
install numpy
python -m pip install pytest
pip install pytest-cov
pip install mypy
pip install matplotlib
pip install scikit-learn

# print options
echo ' -RUN PIPELINE: python main.py'
echo ' -TEST: python -m pytest'
echo ' -COVERAGE: python -m pytest --cov=src'