import subprocess
import tempfile

def run_code(user_code, input_data):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp.write(user_code.encode())
        temp.flush()

        result = subprocess.run(
            ["python", temp.name],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5
        )

        return result.stdout.strip()

def check_output(user_output, expected_output):
    return user_output.strip() == expected_output.strip()
