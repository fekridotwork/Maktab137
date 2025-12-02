import argparse
import re
import os
import time
from pathlib import Path

IP_REG = re.compile(r'\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b')
URL_REG = re.compile(r'https?://[^\s]+')
ERROR_CODE_REG = re.compile(r'\b(4\d{2}|5\d{2})\b')
ENDPOINT_REG = re.compile(r'\"[A-Z]+\s+(/[^ "\?]*)')
STATUS_SIZE_REG = re.compile(r'"\s*(\d{3})\s+(\d+|-)\b')
EMAIL_REG = re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w+\b')
TIMESTAMP_REG = re.compile(r'\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}')

def file_exist(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p

def mask_email(m):
    email = m.group()
    name, domain = email.split('@')
    if len(name) > 2:
        masked_name = name[0] + '*'*(len(name)-2) + name[-1]
    else:
        masked_name = '*'*len(name)
    return masked_name + '@' + domain

def scan(args):
    p = file_exist(args.file)

    results = []
    with p.open('r', encoding='utf-8') as file:
        for line in file:
            if args.ip:
                results.extend(IP_REG.findall(line))
            if args.url:
                results.extend(URL_REG.findall(line))
            if args.errors:
                results.extend(ERROR_CODE_REG.findall(line))

    if args.count:
        print(f"Count: {len(results)}")
    else:
        for r in results:
            print(r)

    if args.export:
        try:
            with open(args.export, 'w', encoding='utf-8') as out:
                out.write('\n'.join(results))
            print(f"Exported {len(results)} results to {args.export}")
        except Exception as e:
            print(f"Export failed: {e}")

def stats(args):
    p = file_exist(args.file)


    ip_set = set()
    endpoint_count = {}
    error_count = 0
    total_size = 0
    total_requests = 0
    size_count = 0

    with p.open('r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            ip_match = IP_REG.search(line)
            if ip_match:
                ip_set.add(ip_match.group())

            endpoint_match = ENDPOINT_REG.search(line)
            if endpoint_match:
                endpoint = endpoint_match.group(1)
                endpoint_count[endpoint] = endpoint_count.get(endpoint, 0) + 1
                total_requests += 1

            s = STATUS_SIZE_REG.search(line)
            if s:
                status = s.group(1)
                size = s.group(2)
                if status.startswith(('4', '5')):
                    error_count += 1
                if size != '-':
                    try:
                        total_size += int(size)
                        size_count += 1
                    except ValueError:
                        pass

    print(f"Unique IPs: {len(ip_set)}")
    if endpoint_count:
        most_requested = max(endpoint_count, key=endpoint_count.get)
        print(f"Most requested endpoint: {most_requested}")
    print(f"Error rate: {0:.2%}" if total_requests == 0 else f"Error rate: {error_count / total_requests:.2%}")
    print(f"Average response size: {0:.2f}" if size_count == 0 else f"Average response size: {total_size / size_count:.2f}")


def clean(args):
    p = file_exist(args.file)
    out_lines = []

    with p.open('r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            s = line.rstrip('\n')
            if args.remove_ip:
                s = IP_REG.sub('', s)
            if args.mask_email:
                s = EMAIL_REG.sub(mask_email, s)
            if args.remove_timestamp:
                s = TIMESTAMP_REG.sub('', s)

            if args.api_only and '/api/' not in s:
                continue

            out_lines.append(s)

    print("\n".join(out_lines or ["(no output)"]))

def monitor(args):
    p = file_exist(args.file)
    pattern = re.compile(args.contains) if args.contains else None

    with p.open('r', encoding='utf-8', errors='ignore') as file:
        file.seek(0, os.SEEK_END)
        try:
            while True:
                line = file.readline()
                if not line:
                    time.sleep(2)
                    continue
                if pattern:
                    if pattern.search(line):
                        print(line.rstrip('\n'))
                else:
                    print(line.rstrip('\n'))
        except KeyboardInterrupt:
            print("\nStopped.")


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    # scan
    scan_parser = sub.add_parser("scan")
    scan_parser.add_argument("--file", required=True)
    scan_parser.add_argument("--ip", action="store_true")
    scan_parser.add_argument("--url", action="store_true")
    scan_parser.add_argument("--errors", action="store_true")
    scan_parser.add_argument("--count", action="store_true")
    scan_parser.add_argument("--export")


    # stats
    stats_parser = sub.add_parser("stats")
    stats_parser.add_argument("--file", required=True)


    # clean
    clean_parser = sub.add_parser("clean")
    clean_parser.add_argument("--file", required=True)
    clean_parser.add_argument("--remove-ip", action="store_true")
    clean_parser.add_argument("--mask-email", action="store_true")
    clean_parser.add_argument("--remove-timestamp", action="store_true")
    clean_parser.add_argument("--api-only", action="store_true", dest="api_only")



    # monitor
    monitor_parser = sub.add_parser("monitor")
    monitor_parser.add_argument("--file", required=True)
    monitor_parser.add_argument("--contains")


    args = parser.parse_args()
    if args.command == "scan":
        scan(args)
    elif args.command == "stats":
        stats(args)
    elif args.command == "clean":
        clean(args)
    elif args.command == "monitor":
        monitor(args)

if __name__ == "__main__":
    main()
