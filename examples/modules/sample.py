def initialize_module(app_context):
    app_context.state['something'] = "It's a me, MARIO!"
    print(app_context.state['something'])
