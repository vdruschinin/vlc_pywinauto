from elements.base_window import NativeBaseWindow
from elements.button import NativeButton
from elements.line_edit import NativeLineEdit
from objects_map import names


class NativeOpenFilesDialog(NativeBaseWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.file_name_edit = NativeLineEdit(self, names.open_file_file_name_edit)
        self.open_button = NativeButton(self, names.open_file_open_button)

    def open_file(self, file_path):
        self.file_name_edit.type_text(file_path)
        self.open_button.click()
