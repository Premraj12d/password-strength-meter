from flask import Flask, render_template, request, jsonify
import string

app = Flask(__name__)

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password123", "111111", "letmein", "admin", "welcome"
}


def has_upper(password):
    for char in password:
        if char in string.ascii_uppercase:
            return True
    return False


def has_lower(password):
    for char in password:
        if char in string.ascii_lowercase:
            return True
    return False


def has_digit(password):
    for char in password:
        if char in string.digits:
            return True
    return False


def has_special(password):
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    for char in password:
        if char in special_chars:
            return True
    return False


def check_password(password):
    if len(password) == 0:
        return {
            "checks": {
                "length": False, "upper": False, "lower": False,
                "digit": False, "special": False, "not_common": False
            },
            "percentage": 0,
            "strength": "None"
        }

    checks = {
        "length": len(password) >= 8,
        "upper": has_upper(password),
        "lower": has_lower(password),
        "digit": has_digit(password),
        "special": has_special(password),
        "not_common": password.lower() not in COMMON_PASSWORDS
    }

    # Base score out of the 6 checks
    base_score = sum(checks.values())
    percentage = round((base_score / 6) * 100)

    # Bonus points for extra length (rewards longer passwords, capped at 100)
    if len(password) >= 12:
        percentage = min(100, percentage + 10)
    if len(password) >= 16:
        percentage = min(100, percentage + 10)

    # Penalty if it's a common password, regardless of other checks
    if not checks["not_common"]:
        percentage = min(percentage, 20)

    if percentage <= 30:
        strength = "Weak"
    elif percentage <= 60:
        strength = "Medium"
    elif percentage <= 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "checks": checks,
        "percentage": percentage,
        "strength": strength
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result = check_password(password)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)