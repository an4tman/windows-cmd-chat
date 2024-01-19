import subprocess
import threading
import queue

class CommandExecutor:
    def __init__(self, shell_env):
        self.shell_env = shell_env
        self.execution_queue = queue.Queue()

    from dangerous_commands import DANGEROUS_COMMANDS
    from prompt_toolkit import prompt
    
    def is_dangerous_command(self, command):
        return any(dangerous_cmd in command for dangerous_cmd in DANGEROUS_COMMANDS)
    
    def _execute_command_without_confirmation(self, command):
        if self.shell_env == 'powershell':
            command = ["powershell", "-Command", command]
        else:
            command = ["cmd.exe", "/C", command]
    
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            encoding='utf-8',
            errors='replace'
        )
    
        threading.Thread(target=self._enqueue_output, args=(process.stdout, self.execution_queue)).start()
    
        return process, self.execution_queue
    
    def execute_command(self, command):
        if self.is_dangerous_command(command):
            confirmation = prompt('This command may alter system state or files. Are you sure you want to execute it? (yes/no): ')
            if confirmation.lower() not in ['yes', 'y']:
                print("Command execution cancelled.")
                return None, None
        return self._execute_command_without_confirmation(command)

    def _enqueue_output(self, out, queue):
        try:
            for line in iter(out.readline, ''):
                queue.put(line)
            out.close()
        except ValueError:
            pass

def read_output(queue):
    output_lines = []
    while not queue.empty():
        line = queue.get_nowait()
        if line:
            output_lines.append(line)
    return ''.join(output_lines)