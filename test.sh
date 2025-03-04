echo "[!] - Running src/ tests..."
python3 -m unittest discover -s src
echo "[!] - Running src/parsing/ tests..."
python3 -m unittest discover -s src/parsing
