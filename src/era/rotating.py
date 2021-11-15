import logging
import re
import shutil
from datetime import datetime

module_logger = logging.getLogger(__name__)


class FolderRotator:

    def __init__(self, base_dir, prefix='') -> None:
        self.base_dir = base_dir
        self.prefix = prefix
        self.pattern = f'{self.prefix}[0-9]{{8}}_[0-9]{{6}}'

        self._class_logger = logging.getLogger(__name__).getChild(self.__class__.__name__)

    #: Make dir Methods
    def _get_new_download_dir_path(self, date_format):
        today = datetime.today()
        download_dir = self.base_dir / f'{self.prefix}{today.strftime(date_format)}'
        return download_dir

    def _make_new_download_dir(self, download_dir_path, exist_ok):
        self._class_logger.debug(f'Attempting to create new directory {download_dir_path}')
        try:
            download_dir_path.mkdir(exist_ok=exist_ok)
        except FileNotFoundError as error:
            raise FileNotFoundError(f'Base directory {self.base_dir} does not exist.') from error
        else:
            self._class_logger.debug(f'Successfully created {download_dir_path}')
            return download_dir_path

    def create_download_dir(self, date_format='%Y%m%d_%H%M%S', exist_ok=False):
        download_dir = self._get_new_download_dir_path(date_format)
        created_dir_path = self._make_new_download_dir(download_dir, exist_ok)
        return created_dir_path

    #: Rotator Methods
    def _get_all_but_n_most_recent_folder_paths(self, custom_pattern=None, max_folder_count=10):
        if custom_pattern:
            self.pattern = custom_pattern
        folder_paths = [path for path in self.base_dir.iterdir() if re.match(self.pattern, path.stem)]
        return sorted(folder_paths)[-max_folder_count:]

    def _delete_old_folders(self, folder_paths_to_delete):
        deleted_folders = []
        for folder in folder_paths_to_delete:
            try:
                self._class_logger.debug(f'Attempting to delete {folder}')
                shutil.rmtree(folder)
            except Exception:
                pass
            else:
                self._class_logger.debug(f'Successfully deleted {folder}')
                deleted_folders.append(folder)

        return deleted_folders

    def rotate_download_dirs(self, custom_pattern=None, max_folder_count=10):
        folder_paths_to_delete = self._get_all_but_n_most_recent_folder_paths(custom_pattern, max_folder_count)
        deleted_folders = self._delete_old_folders(folder_paths_to_delete)

        return deleted_folders
