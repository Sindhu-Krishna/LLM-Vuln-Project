#!/usr/bin/env bash
# run_all.sh
# Usage: ./run_all.sh ~/LLM-Vuln-Project
set -euo pipefail
BASE_DIR="${1:-$HOME/LLM-Vuln-Project}"
SCRIPTS_DIR="$BASE_DIR/scripts"
RESULTS_DIR="$BASE_DIR/detection"
mkdir -p "$RESULTS_DIR/bandit" "$RESULTS_DIR/semgrep"

# iterate CWE folders
for cwe_path in "$BASE_DIR"/*/; do
  # skip scripts/ and other non-CWE directories
  foldername=$(basename "$cwe_path")
  if [[ "$foldername" == "scripts" ]] || [[ "$foldername" == "detection" ]]; then
    continue
  fi
  echo "=== Processing $foldername ==="
  # run extraction for this folder
  python3 "$SCRIPTS_DIR/extract_code_blocks.py" "$cwe_path"

  # run bandit on all .py files in folder (if any)
  pyfiles=($(find "$cwe_path" -maxdepth 1 -type f -name "*.py"))
  if [ ${#pyfiles[@]} -gt 0 ]; then
    bandit_out="$RESULTS_DIR/bandit/${foldername}_bandit.json"
    echo "[*] Running Bandit on ${foldername} (py files count: ${#pyfiles[@]})"
    bandit -r "$cwe_path" -f json -o "$bandit_out" || true
  else
    echo "[i] No Python files detected in $foldername, skipping Bandit"
  fi

  # run semgrep on entire folder (multi-lang)
  semgrep_out="$RESULTS_DIR/semgrep/${foldername}_semgrep.json"
  echo "[*] Running Semgrep on ${foldername}"
  semgrep --config=auto --json --output "$semgrep_out" "$cwe_path" || true

  echo "=== Done $foldername ==="
done

echo "All done. Results in $RESULTS_DIR"
