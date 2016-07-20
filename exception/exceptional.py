''' A module for demonstrating exceptions and control flow in Python '''
def convert(x):
    '''Convert to an integer.'''
    try:
        s = int(x)
    except (ValueError, TypeError): # except can take a tuple
        s = -1
    #except TypeError:
     #   s = -1
    return s 


def convert2(x):
    '''Convert to an integer.'''
    try:
        s = int(x)
    except (ValueError, TypeError): # except can take a tuple
        pass # do nothing when exception happens
    return s


def convert2(x):
    '''Convert to an integer.'''
    try:
        return int(x)
    except (ValueError, TypeError): # except can take a tuple
        return -1


import sys
def convert3(x):
    '''Convert to an integer.'''
    try:
        return int(x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr) # print out the error and indicate where the error happened!
        return -1


def convert4(x):
    '''Convert to an integer.'''
    try:
        return int(x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr) # print out the error and indicate where the error happened!
        raise # re-throw the caught exception         


# commone python exception types: IndexError, KeyError, ValueError, TypeError (should be avoided if possible as it defects the dynamic type in python!)
# two philosophies to deal errors in python: 
# 1) Look Before You Leap (LBYL): pre-check all possible failures that might happen before the actual operation.
# 2) it's Easier to Ask Forgiveness than Permission (EAFP): hope for the best and prepare for the consequence if it doesn't work out
# Python is strongly in favor of EAFP because it puts primary logic for the happy path in the most readable form with deviations from the normal flow
# handled separately rather than interspersed with the main flow. 


#An example: processing a file
import os

# LBYL version: problems are there could be a race condition here e.g. accessing a file while it's being deleted; no good way to handle this.
# also it only checks the successful case, what if the file exists but it contains garbage? what if it's not a file but a directory? All these 
# potential errors need to be handled 
p = '/path/to/datafile.dat'
if os.path.exists(p):
    process_file(p)
else:
    print('no such file as {}'.format(p))

# EAFP version
try:
    process_file(p)
# catch any possible OS error; EAFP is standard in Python and this philosophy is enabled by exceptions which allow centralized, non-local handling.
# Unlike error codes which require interspersed, local handling. Additionally, Exceptions + EAFP makes the error very hard to ignore wheras error code 
# by default are silent. 
except OSError as e:
    print('Could not process file because {}'.format(str(e)))

# finally is 'always' run so it's a good place to clean up resources.
# Moment of Zen: Errors should never pass silently unless explicitly silenced.
                # Errors are like bells and if we make them silent they are of no use!


# Platform specific code: detecting a key press:
# On windows: msvcrt module
# On OSX : sys, tty, termios modules.                
