Author : monarch

Log-Sentinel

A lightweight, command line static[can't analyze in real time] log analyzer written in Python, tracks failed login attempts, and flags suspicious IP addresses based on a customizable threshold

---Features---
Regex-powered: Extracts IP regardless of log layout
Dynamic CLI[command line interface]: Uses "argparse" to accept dynamic Log file paths and thresholds directly from terminal
Error handling: Gracefully handles invalid paths and user interruptions["Ctrl + C"]


---Installation---
Clone the repository and enter the directory: 
git clone https://github.com/monarch-init-bit/log-sentinel
cd log-sentinel


---Usage---
python log_sentinel.py -f sample_auth.log -t 5

"-f" or "--file" tell the path to the log file and it is mandatory
"-t" or "--threshold" tells the threshold(by default it is 3) for the failed attempts