from flask import Flask, request, jsonify
from executor import run_code, check_output

app = Flask(__name__)

TEST_INPUT = "2 7 11 15\n9"
EXPECTED_OUTPUT = "0 1"

@app.route("/")
def home():
    return "Online Judge Running 🚀"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    user_code = data.get("code")

    try:
        output = run_code(user_code, TEST_INPUT)
        result = check_output(output, EXPECTED_OUTPUT)

        return jsonify({
            "output": output,
            "status": "Accepted" if result else "Wrong Answer",
            "input": TEST_INPUT
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
