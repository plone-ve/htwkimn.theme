from setuptools import setup, find_packages
import os

version = '1.0.11'

setup(name='htwkimn.theme',
      version=version,
      description="A responsive Diazo theme for mobile-friendly websites with Plone 4. As child theme, it extends the responsive plonetheme.onegov and aims for easy development with small or fast changing teams - like at the faculty IMN of the University of Applied Sience Leipzig (HTWK), Germany.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='theme responsive diazo plonetheme.onegov university',
      author='Lars Kosubek',
      author_email='post@larskosubek.com',
      url='https://github.com/lkosubek/htwkimn.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['htwkimn'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Plone>=4.3.3',
        'plonetheme.onegov>=1.5.3',
        'ftw.footer',
        'ftw.mobilenavigation',
        'ftw.contentpage>=1.11.3',
        'ftw.contenttemplates',
        'ftw.contentmenu',
        'six>=1.4.1',
        'simplelayout.base>=4.0.5',
        'ftw.upgrade>=1.14.4'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
