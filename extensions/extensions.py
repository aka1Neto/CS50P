name = input("File name: ");
n = name.strip().lower();

if n.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg");

elif n.endswith(".gif"):
    print("image/gif");

elif n.endswith(".png"):
    print("image/png");

elif n.endswith(".pdf"):
    print("application/pdf");

elif n.endswith(".txt"):
    print("text/plain");

elif n.endswith(".zip"):
    print("application/zip");

else:
    print("application/octet-stream");