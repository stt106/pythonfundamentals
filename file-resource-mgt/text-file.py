# To open a file use open(); the mandatory arg is a file path. 
# Optional args are (recommend to specify!): 
    # mode: read/write/append, binary/text; this is specified using single string as follow; always specify explicitly to aid readability:
            # 'r'  : open for reading (default)
            # 'w'  : open for writing, truncating the file first
            # 'x'  : open for exclusive creation, failing if the file already exists
            # 'a'  : open for writing, appending to the end of file if it exists
            # 'b'  : binary mode
            # 't'  : text mode (default)
            # '+'  : open a disk file for updating (reading and writing)
            # 'U'  : universal newlines mode (for backwards compatibility; should NOT be used in new code)
    # encoding: text encoding; default encoding may not be ideal so better to specify explicitly. to get the default encoding, call sys.getdefaultencoding() function. 

# At the file system level, file contains a series of bytes; Python distiguishes between files opened in binary and text modes even when the underlying operating system doesn't!

# Files open in binary mode return and manipulate their contents as bytes objects without any decoding hence reflecting raw data in the file! 

# Files open text mode treat their contents as if it contains text strings of the str type, the raw bytes having first been decoded using a platform dependent encoding or using the specified encoding if given. By default, text mode also engages support for Python's univeral newline, i.e. translating \n into a platform dependent carriage return newline /r/n on Windows.   


h = open('wasteland.txt', mode = 'wt', encoding = 'utf-8')
print(type(h))
#print(help(h))

h.write('What are the roots that clutch, ') # this returns the number of codepoints or characters in the string passed; NOT the number of bytes to the file after encoding a universal newline translation. Hence it's bad practice to rely on the numbers returned by write to get the total number of bytes!

h.write('what branches grow\n') # have to provide new line operator manually as there is no writelien method
h.write('Out of this stony rubbish? ')
# on Windows it has 79 bytes whereas on Linux it's 78 bytes because of the universal newline behavior translation on different operating system. 

h.close() # flush the content to file on the disk!


# to read the file for reading
r = open('wasteland.txt', mode='rt', encoding='utf-8')

# in the text mode, read accepts the number of characters to read not the number of bytes. read return the text and advances the file pointer to the end of what was read. The return type is str because it's in text mode.
print(r.read(32)) 
print(r.read()) # this reads everything else until the end!
print(r.read() == '') # once at the end, any further read returns empty string 

# normally at the end of reading the file should be closed. But if not closed, we can seek to the beginning of the file using seek()
r.seek(0) # seeking to beginning of the file. returns the new position of the file. 

# to read a while line
print(r.readline())
print(r.readline())
