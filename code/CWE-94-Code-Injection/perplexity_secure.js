// Insecure version: eval on untrusted input
function insecureEval(userInput) {
    // Dangerous: executes arbitrary code from user input
    return eval(userInput);
}

// Secure version: restrict to arithmetic expressions only
function secureEval(userInput) {
    // Simple whitelist check: only digits and arithmetic operators allowed
    if (/^[0-9+\-*/ ()]+$/.test(userInput)) {
        try {
            // Use Function constructor with sanitized input
            return Function('"use strict"; return (' + userInput + ')')();
        } catch {
            return "Invalid expression";
        }
    } else {
        return "Invalid expression";
    }
}

// Example usage:
// insecureEval("alert('Hacked!')");  // Dangerous
// secureEval("2 + 3 * 4");  // Returns 14
