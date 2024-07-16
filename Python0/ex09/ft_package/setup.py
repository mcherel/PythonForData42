# setup.py
# This file is used to configure the setup and installation
# of the ft_package module.
# It includes metadata about the package, such as its name,
# version, author, and license.


from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mcherel/ft_package",
    author="mcherel",
    author_email="mcherel-@student.42.fr",
    licence="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approuved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
