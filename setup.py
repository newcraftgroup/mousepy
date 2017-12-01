# Copyright 2017 NEWCRAFT GROUP B.V.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering :: Information Analysis',
]

setup(
    name="mousepy",
    version="0.0.9",
    description="A wrapper for the Mouseflow API.",
    url="https://github.com/newcraftgroup/mousepy",
    author='NEWCRAFT',
    author_email='admin.tech@newcraftgroup.com',
    license='Apache 2.0',
    classifiers=classifiers,
    keywords=['api', 'wrapper', 'mouseflow', 'analytics', 'data'],
    download_url='https://github.com/newcraftgroup/mousepy/archive/v0.0.9.tar.gz',
    packages=find_packages(exclude=['docs']),
    install_requires=["requests"],
)
