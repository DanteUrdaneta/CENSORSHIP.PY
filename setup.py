from setuptools import setup, find_packages

with open("README.md", "r") as f:
  description = f.read()

setup(
  name = "censorship.py",
  version = "0.1",
  packages= find_packages(),
  include_package_data=True,
  install_requires=[
    'pydub',
    'sentence-transformers',
    'faster-whisper',
  ],
  long_description=description,
  long_description_content_type="text/markdown",
  author="NestorDante",
  author_email="nestor.d.urdaneta@gmail.com", 
) 
