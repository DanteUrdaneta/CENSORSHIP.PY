from setuptools import setup, find_packages

setup(
  name="censorship.py",
  version="0.1",
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'pydub',
    'sentence-transformers',
    'faster-whisper',	]
)