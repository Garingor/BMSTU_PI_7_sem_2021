from func import writekey


def write_key():
    result = writekey()

    if result:
        print("WRITE - OK")
    else:
        print("WRITE - ERROR")


write_key()