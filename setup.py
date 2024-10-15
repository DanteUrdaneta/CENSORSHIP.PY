from setuptools import setup, find_packages

with open("README.md", "r") as f:
  d = f.read()

setup(
  name = "censorship.py",
  version = "0.16",
  packages= find_packages(),
  include_package_data=True,
  install_requires=[
    'pydub',
    'sentence-transformers',
    'faster-whisper',
  ],
  description= "Censorship Audio is a Python library that allows you to censor specific words in an audio file based on a given list of words.",
  long_description=d,
  long_description_content_type="text/markdown",
  author="NestorDante",
  author_email="nestor.d.urdaneta@gmail.com", 
) 
