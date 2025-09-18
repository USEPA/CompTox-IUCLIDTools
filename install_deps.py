"""Install XSD files etc."""
import os
import re
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from dotenv import load_dotenv

load_dotenv()


def install_deps():
    """Install missing .xsd files."""
    print("Path to IUCLID .xsd, phrases.xml, etc.:")
    print(f"  {os.environ['EZMAPPER_IUCLID_FORMAT']=}")
    print("Host path to IUCLID .xsd, phrases.xml, etc. (Docker only):")
    print(f"  {os.environ['EZMAPPER_IUCLID_FORMAT_SRC']=}")
    print("Repo. for IUCLID .xsd, phrases.xml, etc.:")
    repo = re.sub("/.*@", "/(token)@", os.environ["EZMAPPER_IUCLID_FORMAT_REPO"])
    print(f"  os.environ['EZMAPPER_IUCLID_FORMAT_REPO']='{repo}'")

    phrases = list(
        Path(os.environ["EZMAPPER_IUCLID_FORMAT"]).glob(
            "**/Phrases.xml", case_sensitive=False
        )
    )
    if phrases:
        print(f"Found {phrases[0]}, skipping download.")
        sys.exit(0)

    with TemporaryDirectory() as tmp_folder:
        subprocess.run(
            ["git", "clone", os.environ['EZMAPPER_IUCLID_FORMAT_REPO'], tmp_folder]
        )
        outpath = Path(os.environ["EZMAPPER_IUCLID_FORMAT"])
        outpath.mkdir(exist_ok=True, parents=True)
        zips = Path(tmp_folder).glob("**/*.zip", case_sensitive=False)
        for zipfile in zips:
            print(zipfile)
            version = outpath / str(zipfile.name).replace("format.zip", "").strip(
                " _"
            ).replace(" ", "_")
            version.mkdir(exist_ok=True, parents=True)
            for c in version.name:
                print(c, ord(c))
            print(version)
            with ZipFile(zipfile) as zippy:
                for info in zippy.infolist():
                    print(info)
                    zippy.extract(info, path=version)


if __name__ == "__main__":
    install_deps()
