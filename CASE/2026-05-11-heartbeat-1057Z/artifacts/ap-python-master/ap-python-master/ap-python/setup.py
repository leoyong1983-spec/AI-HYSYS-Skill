import setuptools

setuptools.setup(
    name='ap-python',
    version='1.0.1',
    description='python automation for aspen plus family products',
    license="MIT Licence",
    author="bshao",
    author_email="bshao@163.com",
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 3'],
    install_requires=['pypiwin32'],
)
