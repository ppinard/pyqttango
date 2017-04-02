""""""

# Standard library modules.
import os

# Third party modules.
from setuptools import setup, find_packages

# Local modules.
import versioneer

# Globals and constants variables.
BASEDIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BASEDIR, 'README.rst'), 'r') as fp:
    LONG_DESCRIPTION = fp.read()

PACKAGES = find_packages()
PACKAGE_DATA = {}

INSTALL_REQUIRES = ['PyQt5']
EXTRAS_REQUIRE = {'develop': ['nose', 'coverage']}

CMDCLASS = versioneer.get_cmdclass()

setup(name="pyqttango",
      version=versioneer.get_version(),
      url='https://github.com/ppinard/pyqttango',
      description="Qt resource file with Tango freedesktop.org icons",
      author="Philippe T. Pinard",
      author_email="philippe.pinard@gmail.com",
      license="GPL v3",
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent'],

      packages=PACKAGES,
      package_data=PACKAGE_DATA,

      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,

      cmdclass=CMDCLASS,

      test_suite='nose.collector',
)

