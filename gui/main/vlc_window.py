from pathlib import Path

from pywinauto import keyboard

import constants
from controller import PywinautoController
from elements.base_window import NativeBaseWindow
from elements.button import NativeButton
from gui.dialogs.open_files import NativeOpenFilesDialog
from gui.dialogs.settings import VlcSettingDialog
from gui.dialogs.time import VlcTimeDialog
from objects_map import names


class VlcPlayer(NativeBaseWindow):
    """
    It's handle UI of VLC media player v.3.0.14
    """

    def __init__(self, process_name: str = 'vlc'):
        self._pause_button = NativeButton(self, names.vlc_pause_button)
        self._fullscreen_button = NativeButton(self, names.vlc_fullscreen_button)
        self._controller = PywinautoController(process_name)
        self.install_path = Path.home() / 'AppData' / 'Roaming' / 'vlc'
        self.settings_file_path = self.install_path / 'vlcrc'
        super().__init__(self._controller, names.vlc_main_window)

    @staticmethod
    def settings(method_to_decorate):
        def wrapper(*args):
            self = args[0]
            self.set_locale()
            if Path(self.settings_file_path).exists():
                self.configure_app_file()
                result = method_to_decorate(*args)
            else:
                result = method_to_decorate(*args)
                self.configure_app()
            self.object.maximize()
            return result

        return wrapper

    def get_app_launcher_path(self) -> str:
        # TODO: add method to work with registry
        # return get_reg_key_value('', constants.VLC_PLAYER_HLM_PATH)
        pass

    @settings
    def start(self):
        app_dir = self.get_app_launcher_path()
        self._controller.start(app_dir)
        self._controller.attach()
        self._controller.wait_for_app_loaded(self.object_name)
        return self

    def configure_app_file(self):
        settings_options = ['video-title-show=0\n',
                            'qt-fs-controller=0\n',
                            'qt-updates-notif=0\n']

        with open(self.settings_file_path, "r+") as file:
            options = file.readlines()
            if list(set(options) & set(settings_options)):
                return
            file.writelines(settings_options)

    def set_locale(self, locale: str = 'en'):
        """Should be used before start app."""
        # TODO: add method to work with registry
        # try:
        #     delete_reg_key_value('Lang', constants.VLC_PLAYER_HCU_PATH)
        # except AssertionError as ex:
        #     pass
        # set_reg_key_value('Lang', 'REG_SZ', locale, constants.VLC_PLAYER_HCU_PATH)
        pass

    def configure_app(self):
        settings = self.open_settings()
        settings.show_controls = False
        settings.updates_notifier = False
        settings.open_subtitles_tab()
        settings.show_title = False
        settings.save()

    @staticmethod
    def stop():
        # TODO: add method to work with process
        # terminate_process(None, 'vlc')
        pass

    def open_media_dialog(self) -> NativeOpenFilesDialog:
        # Native type Ctrl+O
        keyboard.send_keys('^o')
        return NativeOpenFilesDialog(self._controller)

    def open_files(self, path):
        file_dialog = self.open_media_dialog()
        file_dialog.open_file(path)
        return self

    def pause_video(self):
        self._pause_button.click()
        return self

    def scroll_to_begin(self):
        # Native type Ctrl+T
        keyboard.send_keys('^t')

        VlcTimeDialog(self.controller, self.object).wait_until_appears().reset_time()
        return self

    def open_in_fullscreen(self):
        self._fullscreen_button.click()
        return self

    def open_settings(self):
        # Native type Ctrl+P
        keyboard.send_keys('^p')
        return VlcSettingDialog(self.controller, self.object)
