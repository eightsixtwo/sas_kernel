#!/usr/bin/env python3
#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from sas_kernel import __version__


setup(name='SAS_kernel',
      version=__version__,
      description='A SAS kernel for Jupyter',
      long_description=open('README.rst', 'rb').read().decode('utf-8'),
      author='Jared Dean',
      license='Apache Software License',
      author_email='jared.dean@sas.com',
      url='https://github.com/sassoftware/sas_kernel',
      packages=find_packages(),
      package_data={'': ['*.js', '*.md', '*.yaml', '*.css'], 'sas_kernel': ['data/*.json', 'data/*.png']},
      install_requires=['saspy>=1.2.2', 'pygments', "metakernel>=0.18.0", "jupyter_client >=4.4.0",
                        "ipython>=4.0.0"
                        ],
      classifiers=['Framework :: IPython',
                   'License :: OSI Approved :: Apache Software License',
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Topic :: System :: Shells"]
      )
