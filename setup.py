# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('requirements.txt', 'r') as f:
      setup_requires = f.readlines()

setup(name='torched',
      version='0.0.1',
      description='MR/PyTorch Playground',
      author='Pasquale Minervini',
      author_email='p.minervini@ucl.ac.uk',
      url='https://github.com/pminervini/torched',
      test_suite='tests',
      license='MIT',
      install_requires=setup_requires,
      setup_requires=setup_requires,
      tests_require=setup_requires,
      classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules'
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      packages=find_packages(),
      keywords='pytorch natural language processing nlp machine reading mr nlu')
