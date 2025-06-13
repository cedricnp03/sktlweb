from setuptools import setup, find_packages

setup(
    name='sktlweb',  # Name of your project
    version='0.1',  # Version of your project
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[  # List any dependencies your project needs
        # Example: 'numpy', 'requests', etc.
    ],
    entry_points={  # Optional: if your project has command-line tools
        'console_scripts': [
            'sktlweb-cli = sktlweb.cli:main',  # Replace with your actual CLI function
        ],
    },
    include_package_data=True,  # Optional: include non-Python files, e.g., templates, static files
    author='Cedric',
    author_email='cedricnp03@gmail.com',
    description='sktl website',
    long_description=open('README.md').read(),  # Read from a README file for more details
    long_description_content_type='text/markdown',  # If your README is markdown
    url='https://github.com/cedricnp03/sktlweb',  # URL to your project repository
    classifiers=[  # Optional: category labels for your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

