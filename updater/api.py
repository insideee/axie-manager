import requests
import os
from packaging import version
from packaging.version import Version
import warnings
import shutil
import tempfile

# import package
import src


class Updater:
    def __init__(self, url_version=None, url_update=None):
        self.url_update = url_update
        self.remote_version = requests.get(url_version).text.rstrip('\n')
        self.local_version = self.get_local_version()
        self.filepath = os.path.dirname(src.__file__)

        self.need_update = self.get_version_status()

    def get_local_version(self) -> str:
        valid_version = self.local_version_validator()
        vers = str()

        if valid_version:
            vers = src.__version__
        else:
            warnings.warn('Not a valid version or the version file was corrupted')

        return vers

    @staticmethod
    def local_version_validator() -> bool:

        vers = src.__version__
        version_obj = version.parse(vers)
        if not isinstance(version_obj, Version):
            valid_version = False
        else:
            valid_version = True

        return valid_version

    def get_version_status(self) -> str:
        remote_v = version.parse(self.remote_version)
        local_v = version.parse(self.local_version)
        status = str()

        if local_v < remote_v:
            status = True
        elif local_v == remote_v:
            status = False

        return status

    def update_src(self):

        # make a temp directory
        with tempfile.TemporaryDirectory() as tmp:

            # download the new zip and save
            r = requests.get(self.url_update, allow_redirects=True)
            rm_download = os.path.join(tmp, 'src.zip')
            open(rm_download, 'wb').write(r.content)

            # make a backup (work on this in the future)
            rm_backup = os.path.join(tmp, 'src_backup')
            shutil.make_archive(rm_backup, 'zip', self.filepath)

            shutil.rmtree(self.filepath)
            shutil.unpack_archive(rm_download, self.filepath, 'zip')
