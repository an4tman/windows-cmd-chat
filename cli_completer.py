from prompt_toolkit.completion import Completer, Completion

class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        # Your logic for completions
        yield Completion('completion', start_position=-1)
