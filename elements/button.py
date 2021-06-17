from elements.native_object import NativeObject


class NativeButton(NativeObject):

    def click(self):
        self.object.click_input()
