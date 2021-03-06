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
#print(dir(h))
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
print(r.readline()) # at the end of the file, readline() returns empty string 

r.seek(0)
# if want to read all lines at once and know for sure there is enough memory; this is particularly useful if parsing the file invovles hopping backwards and forwards between lines so putting them into a list is useful!
all_lines = r.readlines(); # put each line into a list 
print(all_lines)
r.close() # close the file to release the resource


# Appending to text files
a = open('wasteland.txt', mode='at', encoding='utf-8')
# writelines exist but no writeline
# this takes a series of string and must specify explicit line-ending to provide symmetry with readlines()
a.writelines(['Son of man,\n', 
                'You cannot say, or guests, ', 'for you know only, \n', 
            'A heap of broken images, ', 'where the sun beats\n']) # this should write 3 new lines. The file doesn't end with a new line. 
a.close()


# The notion that files are like objects in python is not supported strongly by any protocol but it works well due to duck typing and polymorphism. Namely, depending on the file path, open will return different specific objects which all behave like a file! 
def word_per_line(fileobject): # any object bahaves like a file will be fine for this function to work due to duck typing!
    return [len(line.split()) for line in fileobject.readlines()]

def main():
    with open('wasteland.txt', mode="tr", encoding="utf-8") as file:
        word_counter = word_per_line(file) # pass in a text file which is io.textWrapper 
        print(word_counter)

    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as webfile:
        print(word_per_line(webfile)) # webfile is a http.client.HTTPResponse

if __name__ == '__main__':
    main()
