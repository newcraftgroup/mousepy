from setuptools import setup, find_packages

setup(
    name="nci-python-mouseflow",
    version="0.0.8",
    description="Client library for Mouseflow's API",
    url="https://github.com/conversioncompany/nci-python-mouseflow",
    author='Newcraft',
    author_email='cedric.le.varlet@newcraftgroup.com',
    license='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='api mouseflow',
    packages=find_packages(exclude=['docs']),
    install_requires=["requests"],
)
