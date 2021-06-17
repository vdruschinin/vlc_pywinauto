from elements.base_window import NativeBaseWindow
from elements.button import NativeButton
from elements.check_box import NativeCheckBox
from objects_map import names


class VlcSettingDialog(NativeBaseWindow):

    def __init__(self, controller, parent):
        super(VlcSettingDialog, self).__init__(controller, names.vlc_settings_dialog, parent)
        self._update_notifier_check_box = NativeCheckBox(
            self, names.vlc_setting_update_notifier_checkbox)
        self._show_controls_check_box = NativeCheckBox(
            self, names.vlc_setting_show_controllers_in_full_screen)
        self._subtitles_button = NativeButton(self, names.vlc_settings_subtitles_tab_button)
        self._show_title_check_box = NativeCheckBox(self, names.vlc_settings_show_title_check_box)
        self._save_button = NativeButton(self, names.vlx_settings_save_button)

    @property
    def show_controls(self):
        return self._show_controls_check_box.is_checked

    @show_controls.setter
    def show_controls(self, value: bool):
        self._show_controls_check_box.set(value)

    @property
    def updates_notifier(self):
        return self._update_notifier_check_box.is_checked

    @updates_notifier.setter
    def updates_notifier(self, value: bool):
        self._update_notifier_check_box.set(value)

    @property
    def show_title(self):
        return self._show_title_check_box.is_checked

    @show_title.setter
    def show_title(self, value):
        self._show_title_check_box.set(value)

    def open_subtitles_tab(self):
        self._subtitles_button.click()

    def save(self):
        self._save_button.click()
