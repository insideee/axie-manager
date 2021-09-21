import requests
import os
from packaging import version
from packaging.version import Version
import sys
import shutil
import tempfile
import importlib
from datetime import datetime
import warnings

from updater.config import UPDATE_DIRNAME, URL_CHECK_VERSION, URL_UPDATED_FILES


class Updater:

    def __init__(self, url_version=URL_CHECK_VERSION, url_update=URL_UPDATED_FILES) -> None:

        self.log_counter = 0
        self.log_header = None
        self.log_end = 'Done, moving on'
        self.update_dir = None

        self.url_update = url_update
        self.remote_version = requests.get(url_version).text.rstrip('\n')

        self.filepath = os.getcwd() + f'/{UPDATE_DIRNAME}'
        self.valid_src = self.local_source_validator()

        self.valid_version = self.local_version_validator(self.valid_src)
        self.local_version = self.get_local_version(self.valid_version)
        self.update_needed = self.check_version_update(self.remote_version, self.local_version)

        self.log_var = self.get_log()

    def local_source_validator(self) -> bool:
        """Check if source directory exist and return it

        """

        # check dir exist
        target_dir = os.getcwd()
        local_dir_list = [f for f in os.listdir(target_dir) if os.path.isdir(target_dir)]

        if UPDATE_DIRNAME in local_dir_list:
            self.log(f'{UPDATE_DIRNAME} directory found')
        else:
            self.log(f'{UPDATE_DIRNAME} directory missing')
            self.log(f'Need to create new {UPDATE_DIRNAME}')
            return False

        # import module if only dir exist
        self.import_module()
        return True

    def local_version_validator(self, valid_src: bool) -> bool:
        """If not valid source return false, 
           if valid check if version is valid too
        """

        if valid_src:
            vers = self.update_dir.__version__
            version_obj = version.parse(vers)
            if isinstance(version_obj, Version):
                return True

        return False

    def get_local_version(self, valid_version: bool) -> str:
        """Get the local version if valid version, 
           if not return string empty
        """

        vers = str()

        if valid_version:
            vers = self.update_dir.__version__
        else:
            if os.path.isdir(os.getcwd() + f'/{UPDATE_DIRNAME}'):
                self.log(f'Not a valid version, the version file is corrupted')
                self.log(f'Need to Update {UPDATE_DIRNAME}')

        return vers

    def check_version_update(self, remote_v: str, local_v: str) -> bool:
        """Check if need update source
        """

        status = str()

        if local_v < remote_v:
            self.log(f'App outdated')
            local_v_status = 'nonexistent' if local_v == '' else f'{local_v}'
            self.log(f'App version is {local_v_status} and repo version is {remote_v}')
            status = True

        elif local_v == remote_v:
            self.log('App up to date')
            self.log(self.log_end)
            status = False

        return status

    def update_src(self) -> None:
        """Update source
        """

        self.log(f'Updating {UPDATE_DIRNAME}')
        # make a temp directory
        with tempfile.TemporaryDirectory() as tmp:

            # download the new zip and save
            self.log(f'Downloading new {UPDATE_DIRNAME}')
            r = requests.get(self.url_update, allow_redirects=True)
            download = os.path.join(tmp, 'src.zip')
            open(download, 'wb').write(r.content)
            self.log(f'Downloaded version is {self.remote_version} and app version is {self.update_dir.__version__}')

            # make a backup (work on this in the future)
            rm_backup = os.path.join(tmp, 'src_backup')
            shutil.make_archive(rm_backup, 'zip', self.filepath)

            self.log(f'Extracting and replacing {UPDATE_DIRNAME}')
            shutil.rmtree(self.filepath)            
            shutil.unpack_archive(download, self.filepath, 'zip')

            self.reload_module()
            self.valid_version = True
            self.local_version = self.update_dir.__version__

            self.log(f'App version is now {self.local_version}')
            self.log(self.log_end)

    def create_src(self) -> None:
        """Create missing source
        """

        with tempfile.TemporaryDirectory() as tmp:
            
            self.log(f'Downloading new {UPDATE_DIRNAME}')
            r = requests.get(URL_UPDATED_FILES, allow_redirects=True)
            download = os.path.join(tmp, 'src.zip')
            open(download, 'wb').write(r.content)

            self.log(f'Extracting and replacing {UPDATE_DIRNAME}')
            pathdir =  os.getcwd() + '/src'
            shutil.unpack_archive(download, pathdir, 'zip')
            
            self.log('Src replaced')

    def log(self, text: str):
        """Log creation handle
        """

        time_now = datetime.now()
        formatted_datetime = time_now.strftime('%Y-%m-%d %H:%M')
        formatted_time = time_now.strftime('%H:%M:%S')
        self.log_header = f'Starting log at {formatted_datetime}'

        # check if log exist:
        log_path = os.path.dirname(__file__) + '/update.log'
        if not os.path.isfile(log_path):
            open(log_path, 'x')
            if self.log_counter == 0:
                with open(log_path, 'r+') as log:
                    log.write(self.log_header)        
        else:
            with open(log_path, 'r+') as log:
                lines = log.readlines()
                if len(lines) > 0:
                    if self.log_counter == 0:
                        for i in range(0, 3):
                            log.write('\n')
                        
                        log.write(self.log_header)            

        with open(log_path, 'a') as log:
            log.write(f'\n{formatted_time}: {text}')

        self.log_counter += 1

    def get_log(self) -> list:
        """Get the current log, format and return it
        """

        log_path = os.path.dirname(__file__) + '/update.log'

        if not os.path.isfile(log_path):
            warnings.warn('Log file missing')
        else:
            with open(log_path, 'r+') as log:
                lines = [line.rstrip('\n') for line in log.readlines() if line != '\n']
                start_point = lines[1].find(' ', lines[1].find(':')) + 1
                start_index = lines.index(self.log_header)+1

                lines = [line[start_point:] for line in lines[start_index:]]

        return lines

    def import_module(self) -> None:
        """Import module handle
        """
        self.update_dir = importlib.import_module(UPDATE_DIRNAME)
        sys.modules[UPDATE_DIRNAME + '._version'] = self.update_dir
        sys.modules[UPDATE_DIRNAME] = self.update_dir

    def reload_module(self):
        """Reload module handle
        """       
        del sys.modules[UPDATE_DIRNAME + '._version']
        del sys.modules[UPDATE_DIRNAME]

        self.update_dir = importlib.import_module(UPDATE_DIRNAME)
