# pygins
pygins is very simple example of plugin system for Python app. It can be called a framework, because it forces specific approach for app development.

The main basis of pygins is treating plugins as modules. To add new plugin, just place your module or package in your `modules` directory  and add its name to `modules` path in config file (`config.json` by default). 

The entry point of your module (or package) is `initialize_module()` function. It takes only 1 argument: the `AppContext` object. `AppContext` represents all data in your application. It lets you to have access to application configuration (and customize your plugins behavior without modifying plugin code) and application state.

There are sample plugins in `modules` directory. Launch the `main.py` script to check how it works.

pygins was tested for Python 3.5.3