pip uninstall ap-python --y
REM python setup.py bdist_wheel --plat-name win_amd64
python setup.py bdist_wheel
pushd dist
pip install ap_python-1.0.1-py3-none-any.whl
popd

REM publish package to PYPI
REM twine upload  dist/*