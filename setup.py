from codecs import open as codecs_open
from setuptools import setup, find_packages


with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='prelurn',
      version='1.0.0',
      description=u"Preprocessing helper for machine learning on tabular data",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Jotham Apaloo",
      author_email='jotham.apaloo@tesera.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      include_package_data=True,
      package_data={
          'prelurn': ['data/*'],
      },
      install_requires=[
          'click>=6.6',
          'pandas>=0.18.0',
          'boto>=2.40.0',
      ],
      extras_require={
          'test': ['pytest==2.9.1'],
          'dev': ['pytest==2.9.1', 'sphinx==1.4.1'],
      },
      entry_points="""
      [console_scripts]
      prelurn=prelurn.scripts.cli:cli
      """
      )
