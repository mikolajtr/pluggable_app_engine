import json

from pluggable_app_engine import AppContext

if __name__ == '__main__':
    config_path = 'config.json'
    with open(config_path, 'r') as file:
        config = json.loads(file.read())
    state = {}

    app_context = AppContext(config, state)
    print("State: %s" % app_context.state)
    print("Config: %s" % app_context.config)
    print("Loaded plugins: %s" % list(app_context.plugins.keys()))
    print("All set, app started.")