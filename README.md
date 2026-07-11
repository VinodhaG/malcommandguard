# MalCommandGuard

A lightweight, offline endpoint security tool that monitors PowerShell commands and URLs in 
real-time, classifying them as Malicious, Suspicious, or Legitimate using a layered detection approach.

## Problem

Attackers increasingly abuse legitimate command-line tools (PowerShell, CMD, Bash) to evade 
traditional antivirus — a technique known as "Living off the Land" (LOTL). MalCommandGuard 
addresses this gap by combining multiple detection methods to catch both known and previously 
unseen threats in real time.

## Key Features

- Real-time monitoring of PowerShell command history
- **Rule-Based Detection** — regex matching against known malicious command patterns
- **Signature-Based Detection** — blacklist matching for known malicious URLs/domains
- **Machine Learning Detection** — TF-IDF + Logistic Regression classifies unknown/obfuscated inputs
- Console alerts, desktop notifications, and sanitized activity logging
- CSV log export and pie chart detection summaries
- Manual detection mode to test individual methods against a single input

## Secure Coding Practices

Centralized input validation, secure file handling with exception handling, fail-safe error 
handling, and log input sanitization to prevent log injection.

## Model Evaluation

Trained on a self-built dataset (600 samples, 300 malicious / 300 legitimate) using TF-IDF + 
Logistic Regression. Achieved 100% accuracy, precision, recall, and F1-score on the held-out test set.

## Tech Stack

Python 3.10+ · scikit-learn · joblib · plyer · Matplotlib · regex

## Setup

Requires Python 3.10+ and Windows (reads PowerShell's `ConsoleHost_history.txt`). Live setup 
instructions are not included here — see screenshots below for a demonstration of functionality.

## Screenshots
<img width="691" height="331" alt="image" src="https://github.com/user-attachments/assets/f00bed1c-d7d0-4a45-b70a-020488b5c367" />

<img width="664" height="234" alt="image" src="https://github.com/user-attachments/assets/0230240a-e82e-424e-a932-bc5fc38eed78" />

<img width="899" height="431" alt="image" src="https://github.com/user-attachments/assets/30075d51-661e-47c2-bb80-5a80f5487df2" />



