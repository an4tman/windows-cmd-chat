import os
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from command_executor import CommandExecutor, read_output
from cli_completer import MyCustomCompleter
from env_vars_prompt import get_formatted_prompt
from openai_integration import send_message_to_gpt4
from env_detect import detect_shell_environment

def start_cli_session():
    history = FileHistory(os.path.expanduser('~/.command_line_agent_history'))
    from cli_key_bindings import get_custom_key_bindings
    
    session = PromptSession(
        history=history,
        auto_suggest=AutoSuggestFromHistory(),
        completer=MyCustomCompleter(),
        key_bindings=get_custom_key_bindings()
    )

    detected_shell = detect_shell_environment()
    executor = CommandExecutor(detected_shell)

    while True:
        try:
            prompt_str = get_formatted_prompt()
            user_input = session.prompt(prompt_str)
            if user_input.lower() == "exit":
                break

            if user_input.startswith('!'):
                command = user_input[1:].strip()
                process, output_queue = executor.execute_command(command)

                if process is None and output_queue is None:
                    continue  # The command was cancelled, so skip to the next iteration

                while True:
                    output = read_output(output_queue)
                    if output:
                        print(output, end='')
                    if process.poll() is not None:
                        break

                output = read_output(output_queue)
                if output:
                    print(output, end='')
                continue

            response = send_message_to_gpt4(user_input)
            if response:
                print(f"GPT-4: {response}")
            else:
                print("Failed to get a response from GPT-4.")
        except (KeyboardInterrupt, EOFError):
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    start_cli_session()
