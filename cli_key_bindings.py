from prompt_toolkit.key_binding import KeyBindings

def get_custom_key_bindings():
    key_bindings = KeyBindings()

    @key_bindings.add('c-q')
    def _(event):
        """
        Pressing Ctrl-Q will exit the application.
        """
        event.app.exit()

    return key_bindings
