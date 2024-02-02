import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    search = re.search(r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$", ip);
    return bool(search);

if __name__ == "__main__":
    main()