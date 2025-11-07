import time
from datetime import datetime

class Log:
    def __enter__(self):
        self.start_time = datetime.now()
        print(f"Entered at: {self.start_time}")
        return self  

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = datetime.now()
        print(f"Exited at: {self.end_time}")
        return False

with Log():
    print("Working ..")
    time.sleep(5)

