from setuptools import setup, find_packages

setup(
	packages = find_packages(),
	name = 'fython',
	description = 'Fython is Fortran with a Python syntax.',
	
	author = 'Nicolas Essis-Breton',
	author_email = 'contact@nicolasessisbreton.com',

	url = 'https://github.com/nicolasessisbreton/fython',

	license = 'Apache License 2.0',

	platform = 'Linux',

	install_requires = ['ply >=3.7', 'networkx >=1.10', 'tabulate >=0.7.5'],

	version = '1.0',
)