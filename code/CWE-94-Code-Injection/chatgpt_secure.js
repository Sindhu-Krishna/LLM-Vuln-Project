// INSECURE: evaluates arbitrary code
const userInput = prompt("Enter math expression:"); // e.g. "2 + 3"
const result = eval(userInput);                     // DANGEROUS
console.log("Result:", result);
