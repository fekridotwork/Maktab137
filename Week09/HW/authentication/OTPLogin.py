import random
import time
import BaseLogin
from utils.file_manager import load_data, save_data

class OTPLogin(BaseLogin):

    otp_status = {}

    # Overriding Parent class method
    def login(self):
        users = load_data("data/users.json")

        email = input("Please enter your email : ").strip().lower()
        for user in users:
            if user["email"] == email:
                otp_code = random.randint(100000, 999999)
                expires_at = time.time() + 120 # 2minutes
                OTPLogin.otp_status[email] = {
                    "otp_code" : otp_code,
                    "expires_at" : expires_at,
                    "attempts" : 0
                }
                print(f"OTP sent to {email}: {otp_code}")
                break
        else:
            print("Email not found in the system! --> Try Again.")

        while True:
            entered_code = input("Please enter the 6-digit code you've received : ")

            record = OTPLogin.otp_status.get(email)
            if not record:
                print("No Active OTP found! --> Request a new code.")
                break
            
            # Checking expiry
            if time.time() > record["expires_at"]:
                print("OTP-code expired! --> Please request a new code.")
                del OTPLogin.otp_status[email]
                break

            # Checking code
            if entered_code == str(record["otp_code"]):
                print("OTP verified successfully and Login completed!")
                del OTPLogin.otp_status[email]
                break
            else:
                record["attempts"] += 1
                if record["attempts"] >= 3:
                    print("Too many wrong attempts! --> Please request a new code. ")
                    del OTPLogin.otp_status[email]
                    break
                else:
                    print(f"Incorrect code! Attempts left: {3 - record['attempts']}")
