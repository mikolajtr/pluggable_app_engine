import sys

from threading import Thread
from importlib import import_module

class AppContext:
    def __init__(self, config, state):
        self.config = config
        self.state = state
        self.plugins = {}

        modules_path = self.config['modules_path']
        modules_list = self.config['modules']

        sys.path.append(modules_path)

        self.load_plugins(modules_list)

    def load_plugins(self, modules_list):
        for name in modules_list:
            self.plugins[name] = import_module(name)
            thread = Thread(target=self.plugins[name].initialize_module, args=(self,))
            thread.start()
