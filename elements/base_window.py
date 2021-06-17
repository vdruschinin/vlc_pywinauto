from functools import cached_property


class NativeBaseWindow:

    def __init__(self, controller, object_name: dict = None, parent: dict = None):
        self.controller = controller
        self.object_name = object_name
        self.parent = parent

    @cached_property
    def object(self):
        return self.controller.get_main_window(self.object_name)

    def get_element(self, parent: object, object_name: dict):
        return self.controller.get_object(parent, object_name)

    def get_frame(self):
        if self.parent:
            return self.get_element(self.parent, self.object_name)
        return self.object

    def wait_until_appears(self, timeout: int = 5):
        self.get_frame().wait('ready', timeout=timeout)
        return self
