import re
import csv
import argparse
from collections import Counter


parser = argparse.ArgumentParser(description='Reading the log file')
parser.add_argument('logfile', help='Please enter the logfile to parse', type=argparse.FileType('r'))
args = parser.parse_args()


def open_log_file(regex):
    with args.logfile as f:
        logs = f.read()
        ip_list = re.findall(regex, logs)
        return ip_list


def write_to_csv(output_file, ip_list):
    with open(output_file, 'w') as f:
        fwriter = csv.writer(f)
        fwriter.writerow(['IP_Address', 'Count'])
        
        for key,value in Counter(ip_list).items():
            fwriter.writerow([key, value])
        