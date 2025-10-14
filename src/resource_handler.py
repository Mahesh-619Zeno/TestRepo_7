def copy_file(source, destination):
    src = open(source, 'rb')
    dst = open(destination, 'wb')
    while True:
        chunk = src.read(1024)
        if not chunk:
            break
        dst.write(chunk)
