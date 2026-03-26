from setuptools import setup, find_packages

setup(
	name='vkama',
	version='0.1.0',
	author='Sargis Kazaryan',
	author_email='yujniybro@example.com',
	description='Minimal Python library for VK API (sync)',
	long_description=open('README.md', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/yasargis/vkama',
	packages=find_packages(),
	install_requires=[
		'requests>=2.28.0'
	],
	python_requires='>=3.7',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)