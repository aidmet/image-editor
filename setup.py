from setuptools import setup, find_packages

setup(
    name='image-editor',
    version='0.1',
    description='A simple image editing library with drawing tools and effects',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
)