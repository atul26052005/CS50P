from validator_collection import validators, checkers, errors

email_add = input("What's your email address? ")

print("Valid" if checkers.is_email(email_add) == True else "Invalid")
