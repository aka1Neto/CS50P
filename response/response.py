import validators

email = input("What's your email address?");

email = validators.email(email);

if email:
    print("Valid");

else:
    print("Invalid");
