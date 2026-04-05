import subprocess
import tempfile

def run_code(user_code, input_data):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
            temp.write(user_code.encode())
            temp.flush()

            result = subprocess.run(
                ["python", temp.name],
                input=input_data,
                text=True,
                capture_output=True,
                timeout=3
            )

            if result.stderr:
                return result.stderr.strip()

            return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Execution Timed Out"

def check_output(user_output, expected_output):
    return user_output.strip() == expected_output.strip()
