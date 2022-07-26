from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.3'
DESCRIPTION = 'Convert all csv files in a folder to a diccionary of dataframe and more'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# Setting up
setup(
    name="wikiframe",
    version=VERSION,
    author="MasamioNakada",
    author_email="nakada2130@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'python-dateutil','pytz','six','chardet'],
    keywords=['pandas', 'read_csv', 'automated', 'dataframe', 'csv', 'etl','extract'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)