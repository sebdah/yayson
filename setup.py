""" Setup script for PyPI """
from setuptools import setup


setup(
    name='yayson',
    version='0.3.0',
    license='Apache License, Version 2.0',
    description='Get colorized and indented JSON in the terminal',
    author='Sebastian Dahlgren',
    author_email='sebastian.dahlgren@gmail.com',
    url='http://sebdah.github.com/yayson/',
    keywords="color colorized json indented beautiful pretty",
    platforms=['Any'],
    scripts=['yayson'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'colorama >= 0.2.5'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
