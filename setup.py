from codecs import open as codecs_open
from setuptools import setup, find_packages


with codecs_open('README', encoding='utf-8') as f:
    long_description = f.read()


setup(name='prelurn',
      version='0.0.1',
      description=u"Preprocessing helper for machine learning on tabular data",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Jotham Apaloo",
      author_email='jotham.apaloo@tesera.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      prelurn=prelurn.scripts.cli:cli
      """
      )
