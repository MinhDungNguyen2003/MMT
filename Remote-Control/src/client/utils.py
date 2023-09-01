import ast


def send(socket, data, raw=False):
    if data:
        socket.write(data if raw else data.encode())
        socket.flush()
        socket.waitForBytesWritten()


def _read(socket, length, raw=False):
    if not socket.isReadable() or not socket.bytesAvailable():
        socket.waitForReadyRead()

    return socket.read(length) if raw else socket.read(length).decode()


def readInt(socket):
    if not socket.isReadable() or not socket.bytesAvailable():
        socket.waitForReadyRead()

    return int(bytes(socket.readLine()).decode().strip())


def readStr(socket):
    if not socket.isReadable() or not socket.bytesAvailable():
        socket.waitForReadyRead()

    return str(bytes(socket.readLine()).decode().strip().replace("\r", "\n"))


def readAll(socket, length, raw=False):
    data = _read(socket, length, raw)

    while len(data) < length:
        data += _read(socket, length, raw)

    return data


def parse(x):
    return ast.literal_eval(x)