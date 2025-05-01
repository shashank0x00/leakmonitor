
1. Unzip and Navigate
unzip leakmonitor.zip
cd leakmonitor

2. Install the package
pip install .

3.Run the tool
python -m leakmonitor.main yourcompany.com


4. Result
It will:

Search for public paste URLs using DuckDuckGo
Fetch raw content
Extract email:password leaks tied to your domain
Save files inside the leaks/ folder

