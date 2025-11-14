import random
import time
from .BaseLogin import BaseLogin  
from utils.file_manager import load_data
from .decorators import rate_limit, captcha



class OTPLogin(BaseLogin):

    otp_status = {}

    # Overriding Parent class method
    @captcha(required_after = 2)      
    @rate_limit(block_seconds = 60)
    def login(self):
        users = load_data("Week09/HW/data/users.json")
        for attempt in range(1, 4):
            number = input(f"\nPlease enter your number ({attempt} / 3 attempt) : ")
            for user in users:
                if user["number"] == number:
                    otp_code = random.randint(100000, 999999)
                    expires_at = time.time() + 10 
                    OTPLogin.otp_status[number] = {
                        "otp_code" : otp_code,
                        "expires_at" : expires_at,
                        "attempts" : 0
                    }
                    print(f"\nOTP sent to {user['number']}: {otp_code}")
                    break
            else:
                print(
                    "\nNumber not found in the system! --> Try Again."
                    if attempt < 3
                    else "\nNumber not found in the system! --> No more attempt left to try."
                    )
                continue
            
            is_founded = False
            while True:
                entered_code = input("\nPlease enter the 6-digit code you've received : ")

                record = OTPLogin.otp_status.get(number)
                if not record:
                    print(
                        "\nNo Active OTP found! --> Request a new code."
                        if attempt < 3
                        else "\nNo Active OTP found! --> No more attempt left to try."
                        )
                    break
                
                # Checking expiry
                if time.time() > record["expires_at"]:
                    print(
                        "\nOTP-code expired! --> Please request a new code."
                        if attempt < 3
                        else "\nOTP-code expired! --> No more attempt left to try."
                        )
                    del OTPLogin.otp_status[number]
                    break

                # Checking code
                if entered_code == str(record["otp_code"]):
                    print("\nOTP verified successfully and Login completed!")
                    del OTPLogin.otp_status[number]
                    is_founded = True
                    return self.authentication_result(True, user["user_id"])
                else:
                    record["attempts"] += 1
                    if record["attempts"] >= 3:
                        print(
                            "\nToo many wrong attempts! --> Please request a new code."
                            if attempt < 3
                            else "\nToo many wrong attempts! --> No more attempt left to try."
                            )
                        del OTPLogin.otp_status[number]
                        break
                    else:
                        print(f"\nIncorrect code! Attempts left: {3 - record['attempts']}")
                        continue
            if is_founded:
                break
        else:
            return self.authentication_result(False)