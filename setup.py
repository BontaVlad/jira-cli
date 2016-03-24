from setuptools import setup

setup(
    name='jira-cli',
    version='0.1',
    py_modules=['jira_cli'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        jira-cli=jira_cli:cli
    ''',
)
