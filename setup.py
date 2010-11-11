from setuptools import setup, find_packages
import os

version = open('collective/jqcookie/version.txt').read().strip()
maintainer = 'Victor baumann'

setup(name='collective.jqcookie',
      version=version,
      description="" + \
          'Collective jqcookie Package (Maintainer: %s)' % maintainer,
      long_description=open("README.txt").read() + "\n" + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='jquery cookie',
      author='%s, 4teamwork GmbH'  % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='http://psc.4teamwork.ch/oss/collective/collective.jqcookie/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
