from pywinauto import Application


class PywinautoController:

    def __init__(self, process_name, backend="uia"):
        self.process_name = process_name
        self.backend = backend
        self.app = None

    def start(self, path: str):
        Application(backend=self.backend).start_(path)

    def attach(self):
        self.app = Application(backend=self.backend).connect(path=self.process_name)

    def get_main_window(self, object_name: dict = None):
        if object_name:
            return self.app.window(**object_name)
        return self.app.window(found_index=0)

    def get_object(self, parent, object_name):
        return parent.child_window(**object_name)

    def wait_for_app_loaded(self, time_out=10):
        self.get_main_window().wait('ready', timeout=time_out)
