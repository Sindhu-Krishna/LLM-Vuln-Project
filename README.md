# LLM-Vuln-Project

This repository contains the full dataset, analysis scripts, and detection results for a project examining how Large Language Models (LLMs) such as ChatGPT, Gemini, Perplexity, and GitHub Copilot generate both insecure and secure code across 10 high-impact CWE categories.  
The project evaluates LLM-generated code using Bandit, Semgrep, and VirusTotal and documents the vulnerabilities discovered.

---

## Project Goals
- Generate insecure & secure Python code samples from multiple LLMs.  
- Detect vulnerabilities using automated static analysis tools.  
- Compare vulnerability types across LLMs.  
- Explore *why* LLMs produce insecure patterns.

## Tools Used

| Tool                  | Purpose                                     |
|-----------------------|---------------------------------------------|
| Bandit                | Python static vulnerability scanner         |
| Semgrep (local rules) | Pattern-based vulnerability scanning        |
| VirusTotal            | Check for malware signatures                |
| LLMs Used             | ChatGPT, Gemini, Perplexity, GitHub Copilot |

## Disclaimer
This repository contains intentionally vulnerable code examples generated using LLMs.  
They are meant strictly for:

- cybersecurity research  
- academic coursework  
- static analysis benchmarking  
- controlled experiment environments  

*WARNING*
Do NOT use this code in production environments.  
Run only inside isolated sandbox VMs.
