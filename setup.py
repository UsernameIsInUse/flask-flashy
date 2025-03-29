from setuptools import setup
from pathlib import Path

setup(
  name='flask-flashy',
  version='0.2.1',
  description="Custom flash system allowing custom keyword arguments for Flask.",
  url='https://github.com/UsernameIsInUse/flask-flashy',
  author='Alex Chichester',
  author_email='alexcchichester@gmail.com',
  license='BSD 3-clause',
  packages=['flask_flashy'],
  install_requires=['Flask'],
  long_description = (Path(__file__).parent / "README.md").read_text(),
  long_description_content_type='text/markdown',
  
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.12',
  ]
)