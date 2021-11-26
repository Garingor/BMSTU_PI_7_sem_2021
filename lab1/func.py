import os
from hashlib import sha256


def uuid():
    uuidpl = os.popen('ioreg -rd1 -c IOPlatformExpertDevice | awk /IOPlatformUUID/').readlines()

    uuidpl = uuidpl[0].split("\"")[3]

    return uuidpl

#  ioreg displays the I/O Kit registry. Он показывает иерархическую структуру реестра в виде перевернутого дерева.
# -c Показывать свойства объекта только в том случае, если объект является экземпляром или производным от указанного
# Класс C ++ (например, IOService)
# используется класс IOPlatformExpertDevice для доступа к серийному номеру Mac/оборудованию uuid
# awk для дальнейшего сокращения данных

def sha(uuidpl):
    return sha256(uuidpl.encode('utf-8')).hexdigest()


def write_to_file(uuidpl):
    error = True

    try:
        filename = open("key.txt", "w")
        filename.write(uuidpl)
        filename.close()
    except:
        error = False

    return error


def isvalidcheck():
    uuidpl = uuid()
    uuidpl = sha(uuidpl)

    try:
        filename = open("key.txt")
        uuidplfile = filename.read()
    except:
        return False

    return uuidpl == uuidplfile


def writekey():
    uuidpl = uuid()
    uuidpl = sha(uuidpl)
    error = write_to_file(uuidpl)

    return error

