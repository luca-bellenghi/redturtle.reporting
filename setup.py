from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='redturtle.reporting',
      version=version,
      description="Reporting application",
      long_description=open("README.txt").read() + "\n" +
                  open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['redturtle'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'Products.PloneFormGen',
          'uwosh.pfg.d2c',
          'collective.geo.bundle',
          'Products.DataGridField',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
