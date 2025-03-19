echo "[!] - Running src/nodes tests..."
python3 -m unittest discover -s src/nodes
echo "[!] - Running src/parsing/ tests..."
python3 -m unittest discover -s src/parsing
echo "[!] - Running src/ tests..."
python3 -m unittest discover -s src/
