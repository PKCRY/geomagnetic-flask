import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Geomagnetic Thunder"
    version="0.0.1",
    author="Nicholas Card",
    author_email="nickcard2000@gmail.com",
    url="https://github.com/pk_cry/GeomagneticThunder",
    description="This is a text based adventure game that will be run with flaskr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
