import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_beaker',
    'decorator',
    'zope.interface',
    ]

setup(name='TeachProgramming',
      version='0.1',
      description='A dynamic website to showcase cool programming activities',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Allan Callaghan',
      author_email='calaldees@gmail.com',
      url='calaldees.dreamhosters.com',
      keywords='web pylons pyramid teach learn',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='teachprogramming',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = teachprogramming:main
      [console_scripts]
      populate_TeachProgramming = teachprogramming.scripts.populate:main
      """,
      )
