import re, csv, json

def read_and_parse(file_path):

    counts = {"info": 0, "warning": 0, "error": 0}
    try:
        with open (file_path, 'r', encoding='utf-8', errors='ignore') as file, \
             open("errors.log", "w", encoding="utf-8") as errlog, \
            open("critical_errors.csv", "w", newline="", encoding="utf-8") as ce:

            writer = csv.writer(ce); 
            writer.writerow(["Timestamp", "Message"])

            for line_num, line in enumerate(file, 1):
                
                match = re.match(r'^\[(?P<timestamp>[A-Za-z]{3}\s+[A-Za-z]{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4})\]\s+\[(?P<level>[A-Za-z]+)\]\s+(?P<message>.*)$', line)
                if match:
                    timestamp = match.group(1)
                    level = match.group(2)
                    message = match.group(3)
                    print(f"Timestamp: {timestamp}, Level: {level}, message: {message}")
                    if level == "error": 
                        writer.writerow([timestamp, message])      
                else:
                    errlog.write(f"{line_num}: {line}")  

                    if level in counts: 
                        counts[level] += 1
    except FileNotFoundError:
        print("File not found")
    with open("summary.json", "w", encoding="utf-8") as sum_js:
                json.dump(counts, sum_js, indent=2)
        
read_and_parse(r"C:\Users\almahdi laptop\Desktop\Maktab\HW\HW2\sample.log") 