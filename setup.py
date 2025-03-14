from setuptools import setup, find_packages

setup(
    name='underdoc',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'httpx',
    ],
    entry_points={
        'console_scripts': [
            'underdoc = underdoc.cli:cli',
        ],
    },
    author='Clarence Ho',
    author_email='clarence@underdoc.io',
    description='CLI for interacting with UnderDoc API SaaS.',
    url='https://underdoc.io',
)
