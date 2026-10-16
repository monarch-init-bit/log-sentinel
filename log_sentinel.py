# Author : monarch
import re
import argparse

parser = argparse.ArgumentParser(description="Log-sentinel: Track auth failures")
parser.add_argument("-f", "--file", required=True, help="Path to log file")
parser.add_argument("-t", "--threshold", type=int, default=3, help="Failure threshold")

args = parser.parse_args()

failed_logs = {}

def main():
    try:
        with open(args.file, "r") as log_data:
            for line in log_data:
                match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)

                if match:
                    failed_match = re.search(r"\bFAILED\b", line)
                    if failed_match:
                        ip = match.group()
                        # print(ip)
                        if ip in failed_logs:
                            failed_logs[ip] += 1
                        else:
                            failed_logs[ip] = 1


        for ip, count in failed_logs.items():
            if count >= args.threshold:
                print(f"IP : {ip} | Fail count : {count}")

    except KeyboardInterrupt:
        print("program stopped by user")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()