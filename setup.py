from setuptools import setup, find_packages

setup(
    name="classification_using_lstm",
    license="MIT",
    version="0.0.7",
    description="Project has been completed.",
    author="Avnish Yadav",
    packages=find_packages(),
    install_requires= ["Flask",
    "gunicorn",
    "pyyaml",
    "tensorflow-datasets"]
)