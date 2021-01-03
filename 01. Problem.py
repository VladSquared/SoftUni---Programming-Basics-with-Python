email = input()

while True:
    cmd = input()
    if cmd == "Complete":
        break
    elif "Make Upper" in cmd:
        email = email.upper()
        print(email)
    elif "Make Lower" in cmd:
        email = email.lower()
        print(email)
    elif "GetDomain" in cmd:
        count = int(cmd.split()[1])
        print(email[-count:])
    elif "GetUsername" in cmd:
        if not "@" in email:
            print(f"The email {email} doesn't contain the @ symbol.")
            continue
        at_char = int(email.index("@"))
        print(email[:at_char])
    elif "Replace" in cmd:
        char = cmd.split()[1]
        email = email.replace(char, "-")
        print(email)
    elif "Encrypt" in cmd:
        for char in email:
            print(ord(char), end=" ")
