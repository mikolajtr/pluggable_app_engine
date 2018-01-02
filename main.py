from app_context import AppContext

if __name__ == '__main__':
    app_context = AppContext()
    print("State: %s" % app_context.state)
    print("Config: %s" % app_context.config)
    print("Loaded plugins: %s" % list(app_context.plugins.keys()))
    print("All set, app started.")