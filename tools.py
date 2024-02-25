import os
import sys
from langchain.tools import tool
import subprocess
# from pymarkdown.api import PyMarkdownApi, PyMarkdownApiException

@tool("write_data")
def write_data(file_path: str, text: str) -> None:
    """
      Writes `text` to a file at `file_path`, overwriting if it exists.

      Parameters:
      - file_path (str): Path and name of the file.
      - text (str): Text to be written to the file.

      Returns:
      - None
    """
    with open(file_path, 'w+') as f:
        f.write(text)

@tool("test_run_tool")
def test_run_tool(file_path: str) -> str:
    """
    A tool to review puml files for PlantUML syntax errors.

    Parameters:
    - file_path: The path to the puml file to be reviewed.

    Returns:
    - validation_results: A list of validation results
    and suggestions on how to fix them.
    - "" if no errors
    """

    print("\n\nValidating puml syntax...\n\n" + file_path)

    try:
        result = subprocess.run(['plantuml', file_path], capture_output=True, text=True, check=True)
        if result.stdout:
            print("Validation successful. Output:")
            print(result.stdout)
            return result.stdout
        else:
            print("Validation successful no errors")
            return ""


    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred while trying to validate the PUML file: {e}\n"
        if e.stderr:  # Check if there is any stderr output
            error_message += f"Error output: {e.stderr}"
            print(error_message)
        else:
            error_message += "No error output available."
            print(error_message)
        return error_message
