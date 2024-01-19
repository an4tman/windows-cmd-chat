import os
import subprocess
import sys

def detect_shell_environment():
    possible_shells = ['powershell', 'cmd']
    shell_environment = None

    if 'PWSH' in os.environ or 'PSModulePath' in os.environ:
        shell_environment = 'powershell'
    elif 'COMSPEC' in os.environ and 'cmd.exe' in os.environ['COMSPEC'].lower():
        shell_environment = 'cmd'

    if shell_environment is None:
        try:
            output = subprocess.check_output(['echo', '%COMSPEC%'], shell=True).decode().strip()
            if 'cmd.exe' in output:
                shell_environment = 'cmd'
        except subprocess.SubprocessError:
            pass
        if shell_environment is None and sys.platform == 'win32':
            shell_path = os.path.expandvars('%COMSPEC%')
            if 'powershell' in shell_path:
                shell_environment = 'powershell'
            elif 'cmd.exe' in shell_path:
                shell_environment = 'cmd'
    if shell_environment is None:
        shell_environment = 'cmd'
    return shell_environment

if __name__ == "__main__":
    detected_shell = detect_shell_environment()
    print(f"Detected shell environment: {detected_shell}")