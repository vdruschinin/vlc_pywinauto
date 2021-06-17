class NativeObject:

    def __init__(self, parent, object_name):
        self.parent = parent
        self.object_name = object_name

    @property
    def object(self):
        return self.parent.get_element(self.parent.get_frame(), self.object_name)
