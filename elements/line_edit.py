from elements.native_object import NativeObject


class NativeLineEdit(NativeObject):

    def type_text(self, text):
        self.object.set_text(text)
