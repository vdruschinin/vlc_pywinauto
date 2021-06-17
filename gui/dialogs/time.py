from elements.base_window import NativeBaseWindow
from elements.button import NativeButton
from objects_map import names


class VlcTimeDialog(NativeBaseWindow):

    def __init__(self, controller, parent):
        self._reset_time_button = NativeButton(self, names.vlc_time_dialog_reset_time_button)
        self._go_button = NativeButton(self, names.vlc_time_dialog_go_button)
        super(VlcTimeDialog, self).__init__(controller, names.vlc_time_dialog, parent)

    def reset_time(self):
        self._reset_time_button.click()
        self._go_button.click()
