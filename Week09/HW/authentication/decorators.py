import time
import random


def rate_limit(block_seconds = 30):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, "blocked_until"):
                self.blocked_until = 0.0

            now = time.time()

            if now < self.blocked_until:
                wait = int(self.blocked_until - now)
                print(f"\nYou can't login until {wait} more seconds.")
                return False, None

            success, user_id = func(self, *args, **kwargs)

            if not success:
                self.blocked_until = time.time() + block_seconds
                print(f"\nYour login was unsuccessful so you have to wait until {block_seconds} more seconds.")

            return success, user_id

        return wrapper
    return decorator


def captcha(required_after = 2):
    def decorator(func):
        def wrapper(self, *args, **kwargs):

            if not hasattr(self, "captcha_fail_count"):
                self.captcha_fail_count = 0

            if self.captcha_fail_count >= required_after:
                a = random.randint(1, 9)
                b = random.randint(1, 9)
                correct = a + b
                answer = input(f"\nCaptcha: What is {a} + {b}? ")

                if str(answer).strip() != str(correct):
                    print("\nCaptcha failed.")
                    return self.authentication_result(False)

                print("\nCaptcha passed.")
                self.captcha_fail_count = 0 

         
            success, user_id = func(self, *args, **kwargs)

            if not success:
                self.captcha_fail_count += 1
            else:
                self.captcha_fail_count = 0

            return success, user_id

        return wrapper
    return decorator

def mfa():
    def decorator(func):
        def wrapper(self, *args, **kwargs):

            success, user_id = func(self, *args, **kwargs)

            if not success:
                return self.authentication_result(False)

            print("\nFirst step successful. Going for the second (MFA)")

            from .OTPLogin import OTPLogin

            otp = OTPLogin()
            otp_success, _ = otp.login()

            if otp_success:
                print("\nMFA passed.")
                return self.authentication_result(True, user_id)

            print("\nMFA failed.")
            return self.authentication_result(False)

        return wrapper
    return decorator


