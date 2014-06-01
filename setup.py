#!/usr/bin/env python
""" setup script for ivoing package """
import sys
from os.path import join as pjoin

# For some commands, use setuptools.
if len(set(('develop', 'bdist_egg', 'bdist_rpm', 'bdist', 'bdist_dumb',
            'install_egg_info', 'egg_info', 'easy_install', 'bdist_wheel',
            'bdist_mpkg')).intersection(sys.argv)) > 0:
    import setuptools

from distutils.core import setup

setup(name='ivoing',
      version='0.1a',
      description='Tools for working with Ivo website',
      author='Matthew Brett',
      maintainer='Matthew Brett',
      author_email='matthew.brett@gmail.com',
      url='http://github.com/matthew-brett/ivo-tools',
      packages=['ivoing', 'ivoing.tests'],
      scripts = [pjoin('scripts', f) for f in ('ivo-rename.py',)],
      license='BSD license',
      classifiers = ["Environment :: Console",
                     'License :: OSI Approved :: BSD License',
                     'Programming Language :: Python',
                     'Development Status :: 3 - Alpha'],
      long_description = open('README.rst', 'rt').read(),
     )
