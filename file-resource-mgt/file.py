import sys

def main(filename):
    f = open(filename, mode="tr", encoding="utf-8")
    for line in f:
        #this gets double line space because each line is terminated by a newline and gets printed on its own
        #print(line)
        sys.stdout.write(line) # stream is a file-like object; file and stream are closed related.
    # closing the file is important because it informs the underlying OS you're done with the file. Without closing it, it's possible to data; also there may be pending write buffered up which might get written completely. Furthermore if opening lots of files without closing the system may run out of resources. 
    # To aid this Python provides a syntax suger with block which will auto close the file! With block can be used with any objects that support context-manager protocol (including the file objects returned by the open(), essentially open() returns a context-manager implementation!)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
