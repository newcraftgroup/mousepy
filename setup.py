from setuptools import setup, find_packages

setup(
    name="nci-omniture-mouseflow",
    version="0.0.4",
    description="Forwards adobe omniture segments to mouseflow",
    url="https://github.com/conversioncompany/nci-omniture-mouseflow",
    author='Newcraft',
    author_email='cedric.le.varlet@newcraftgroup.com',
    license='',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='development adobe omniture',
    packages=find_packages(exclude=['config', 'manage', 'docs', 'tests*', 'export']),
    install_requires=["pandas", "texttable", "requests"],
)
