from func import isvalidcheck

def check_key():
    result = isvalidcheck()

    if result:
        print("CHECK KEY - OK")
    else:
        print("CHECK KEY - ERROR")


check_key()