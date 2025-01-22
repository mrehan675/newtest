from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sand_ht/__init__.py
from sand_ht import __version__ as version

setup(
	name="sand_ht",
	version=version,
	description="sand_ht",
	author="sand_ht",
	author_email="rehan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
