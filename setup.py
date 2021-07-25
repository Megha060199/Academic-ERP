from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in insd_erpnext/__init__.py
from insd_erpnext import __version__ as version

setup(
	name='insd_erpnext',
	version=version,
	description='Management of Academics domain',
	author='INSD',
	author_email='info@insdindia.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
