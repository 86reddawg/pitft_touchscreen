from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='pitft_touchscreen',
   version='0.3',
   description='Touchscreen handling with evdev',
   license="GNU",
   long_description=long_description,
   author='Przemo Firszt',
   author_email='przemo@firszt.eu',
   url="https://github.com/86reddawg/pitft_touchscreen/",
   py_modules = ['pitft_touchscreen'],
   install_requires=['evdev'], #external packages as dependencies

)