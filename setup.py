import base64

# Decrypt numbers
def getNumberList():
    with open("data-encrypted.txt", "rb") as f:
        encoded = f.read()

    decoded = base64.b64decode(encoded).decode("utf-8")
    return list(map(int, decoded.strip().split("\n")))