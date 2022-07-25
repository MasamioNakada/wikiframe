from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Convert all csv files in a folder to a diccionary of dataframe'
LONG_DESCRIPTION = 'This package scan all the .csv files in a folder a convert into a dataframe, It is accept different csv delimiter and encodings.'

# Setting up
setup(
    name="wiki-tools",
    version=VERSION,
    author="MasamioNakada",
    author_email="nakada2130@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'python-dateutil','pytz','six'],
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