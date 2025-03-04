from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt", "r") as f:
        # return [line.strip() for line in f if line.strip() and not line.startswith("#")]
        reqs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        return reqs


install_reqs = read_requirements()

setup(
    name="ezmapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=install_reqs,
    include_package_data=True,
    author="Jennat Aboabdo",
    author_email="Aboabdo.Jennat@epa.gov",
    description="A tool to map and manipulate data columns into OECD Harmonized Templates.",
    python_requires=">=3.8",
)
