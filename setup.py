from setuptools import find_packages, setup

setup(name='ranges',
      description='Generate various kinds of ranges, either in whatever Python \
            data type is appropriate or as a list of strings that retain all   \
            the various quirks of your start, stop and step arguments.',
      long_description=open('README.md').read(),
      author='Stijn Debrouwere',
      author_email='stijn@debrouwere.org',
      url='http://stdbrouw.github.com/python-ranges/',
      download_url='http://www.github.com/stdbrouw/python-ranges/tarball/master',
      version='0.2',
      license='MIT',
      packages=find_packages(),
      keywords='data range utilities',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Text Processing',
                   'Topic :: Utilities'],
      )
