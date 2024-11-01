from setuptools import setup, find_packages

setup(
    name='DFServer',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['DFServer.DFServer.py','DFServer.DFBaseServer.py'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-socketio'
    ]
)