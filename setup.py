from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='3scale-auth0-wrapper',
      version='0.1',
      description='Wrapper between 3scale and auth0',
      author='Jakub Smadiš',
      author_email='jakub.smadis@gmail.com',
      maintainer='Jakub Smadiš',
      url='https://github.com/jsmadis/3scale-auth0-wrapper',
      packages=find_packages(exclude=("tests",)),
      long_description=long_description,
      long_description_content_type='text/markdown',
      include_package_data=True,
      install_requires=[
        'Flask', 'python-dotenv', 'requests'
    ],
      entry_points={},
      classifiers=[
          "Programming Language :: Python :: 3",
          'Programming Language :: Python :: 3.7',
          "Operating System :: OS Independent",
          "License :: OSI Approved :: Apache Software License",
          'Intended Audience :: Developers',
          'Topic :: Utilities',
      ],
      )
