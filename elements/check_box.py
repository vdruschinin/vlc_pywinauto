from elements.native_object import NativeObject


class NativeCheckBox(NativeObject):

    @property
    def is_checked(self) -> int:
        return self.object.get_toggle_state()

    def set(self, value):
        if value != self.object.get_toggle_state():
            self.object.click()
