from .helper import say_hello

def initialize_module(app_context):
    app_context.state["name"] = "Mikołaj"
    say_hello(app_context.state["name"])