# Command-Line-Agent

The Command-Line-Agent is a python-based utility designed to enable interaction with GPT-4 via command line interface (CLI). Using your OpenAI API key, you can send PowerShell or cmd.exe commands directly to your machine, view the output in real-time, and have a chat-based interface directly within your terminal.

## Features

- Command-line based chat interface with future support for a GUI.
- Environment detection to ensure commands are suited for the correct shell.
- Real-time output display from the executed commands.
- Utilizes environment variables to tailor interactions.

## Prerequisites

Before you can run the Command-Line-Agent, you will need:

- Python 3.x installed on your system.
- An active OpenAI API key set as an environment variable `OPENAI_API_KEY`.

## Technologies

- Python
- OpenAI API (GPT-4)
- LangChain
- psutil
- os
- subprocess
- cmd
- readline/prompt_toolkit
- colorama
- requests

## Installation

Follow these steps to set up the Command-Line-Agent on your local system:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd path-to-repository

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# Unix/MacOS:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt
```

## Usage

Start the command-line agent by executing the following command in your terminal:

```bash
python cli.py
```

Use `!` prefix for executing direct shell commands (e.g., `!dir` or `!ls`). To exit the CLI, type `exit` or use the keyboard shortcut `Ctrl-Q`.

## Configuration

*Set your OpenAI API key as an environment variable named `OPENAI_API_KEY` before starting the agent.*

## Contributing

Your contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.