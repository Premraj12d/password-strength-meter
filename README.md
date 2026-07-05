# Password Strength Meter

A simple web app that checks how strong your password is — in real time, as you type. Built with Flask on the backend and plain HTML/CSS/JS on the frontend.

I built this to understand how password validation actually works under the hood, instead of just using a library for it. No external strength-checking packages — the whole scoring logic is written from scratch in Python.

## What it does

Type a password into the input box and it instantly checks:

- Is it at least 8 characters long?
- Does it have an uppercase letter?
- Does it have a lowercase letter?
- Does it have a number?
- Does it have a special character?
- Is it one of the commonly used weak passwords (like "123456" or "password")?

Based on these checks, it gives you a percentage score and a strength label — Weak, Medium, Strong, or Very Strong. Longer passwords get bonus points, and common passwords get capped low no matter how many other boxes they tick.

## Why percentage instead of just Weak/Medium/Strong

A label alone doesn't tell you much. A password could be barely "Medium" or almost "Strong" — the percentage gives a clearer, more precise picture of where it actually stands.

## Tech used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (vanilla, no frameworks)

## Running it locally
