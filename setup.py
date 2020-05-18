from setuptools import setup, find_packages

setup(
    name='ssm',
    version='0.1',
    license='MIT',
    description = 'A simplistic CLI that works with AWS Systems Manager Parameter Store',
    author='Eyal Stoler',
    author_email='eyalstoler@gmail.com',
    url='https://github.com/eyalstoler/ssm-simple-cli',
    download_url='https://github.com/eyalstoler/ssm-simple-cli/archive/v_01.tar.gz',  # I explain this later on
    keywords=['python', 'cli', 'aws-cli', 'ssm', 'ssm-cli'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'boto3',
        'pyperclip'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points='''
        [console_scripts]
        ssm=cli.src.ssm_cli:cli
    ''',
)