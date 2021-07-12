import os
import toml
import zipfile
import shutil

DEST = "dist/workshop/universal"
config = toml.load("config.toml")
shutil.rmtree(DEST, ignore_errors=True)
os.makedirs(DEST, exist_ok=True)
zip_source = zipfile.ZipFile("dist/v{}.scs".format(config["version"]))
for zipped_files in zip_source.namelist():
    zip_source.extract(zipped_files, DEST)
os.system("start steam://rungameid/421800")
