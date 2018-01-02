import json
import sys

from threading import Thread
from importlib import import_module

class AppContext:
    def __init__(self, config_path='config.json', state=dict()):
        self.config = self.parse_config(config_path)
        self.state = dict(state)
        self.plugins = dict()

        modules_path = self.config['modules_path']
        modules_list = self.config['modules']

        sys.path.append(modules_path)

        self.load_plugins(modules_list)

    def parse_config(self, config_path):
        with open(config_path, 'r') as file:
            return json.loads(file.read())

    def load_plugins(self, modules_list):
        for name in modules_list:
            self.plugins[name] = import_module(name)
            thread = Thread(target=self.plugins[name].initialize_module, args=(self,))
            thread.start()
