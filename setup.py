#!/usr/bin/env python3

# +------------------------+			   
# | Created with Sailboat  |
# |                        |
# | Do not edit this file  |
# | directly. Instead  	   |			   
# | you should edit the	   |			   
# | `sailboat.toml` file.  |			   
# +------------------------+	

import setuptools

try:
	with open("README.md", "r") as fh:
		long_description = fh.read()
except FileNotFoundError:
	long_description = """
	# Golfity
	
	### Contributors
	- Cole Wilson
	### Contact
	<cole@colewilson.xyz>
	"""

options = {
	"name": "golfity",
	"version": "0.0.3",
	"scripts": [],
	"entry_points": {'console_scripts': ['parity=golfity.__main__:_main']},
	"author": "Cole Wilson",
	"author_email": "cole@colewilson.xyz",
	"description": "",
	"long_description": long_description,
	"long_description_content_type": "text/markdown",
	"url": "https://github.com/cole-wilson/parity",
	"packages": setuptools.find_packages(),
	"install_requires": ['typing', 'adicity'],
	"classifiers": ["Programming Language :: Python :: 3"],
	"python_requires": '>=3.6',
	"package_data": {"": ['*.p'], },
	"license": "none",
	"keywords": '',
	"setup_requires": ['wheel'],
}

custom_options = {}

if __name__ == "__main__":
	setuptools.setup(**custom_options, **options)