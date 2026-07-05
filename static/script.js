const passwordInput = document.getElementById("passwordInput");
const toggleVisibility = document.getElementById("toggleVisibility");
const meterFill = document.getElementById("meterFill");
const strengthLabel = document.getElementById("strengthLabel");
const checkList = document.getElementById("checkList");

const strengthColors = {
  "None": "#8a6216",
  "Weak": "#ff4d4d",
  "Medium": "#ffb000",
  "Strong": "#7fdc7f",
  "Very Strong": "#39ff87"
};

const strengthWidths = {
  "None": "0%",
  "Weak": "25%",
  "Medium": "55%",
  "Strong": "80%",
  "Very Strong": "100%"
};

let debounceTimer = null;

passwordInput.addEventListener("input", () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(runCheck, 150);
});

async function runCheck() {
  const password = passwordInput.value;

  const response = await fetch("/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password })
  });

  const result = await response.json();
  updateUI(result);
}

function updateUI(result) {
    const { checks, strength, percentage } = result;
  
    meterFill.style.width = percentage + "%";
    meterFill.style.background = strengthColors[strength];
  
    document.getElementById("strengthPercentage").textContent = percentage + "%";
    document.getElementById("strengthText").textContent =
      strength === "None" ? "Awaiting input" : strength;
  
    strengthLabel.style.color = strengthColors[strength];
  
    Object.keys(checks).forEach((key) => {
      const li = checkList.querySelector(`li[data-check="${key}"]`);
      const icon = li.querySelector(".check-icon");
      const passed = checks[key];
  
      li.classList.toggle("passed", passed);
      li.classList.toggle("failed", !passed);
      icon.textContent = passed ? "✓" : "✗";
    });
  }

toggleVisibility.addEventListener("click", () => {
  const isPassword = passwordInput.type === "password";
  passwordInput.type = isPassword ? "text" : "password";
  toggleVisibility.textContent = isPassword ? "HIDE" : "SHOW";
});

// Initialize input type
passwordInput.type = "text";