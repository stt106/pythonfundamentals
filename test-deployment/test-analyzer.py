# python standard library includes the unitest module which in fact covers integration test, accpetance test and unit test. The key main of this module is to automate tests and make the testing repeatable!
# The unittest module is built around a range of key concepts and at the center is the concept of TestCase which groups together a set of related individual test functions. It's the basic unit of text organization in the unittest framework. 

# The other key concept is fixtures which run before (set-up fixture) and/or after (tear-down fixture) each test function; they are like test initializer in .NET unit test. Asseration will test the specific conditions and actual behaviors.  


import unittest
import os

def analyze_text(filename):
    """Calculate the number of lines and characters in a file
    
    Args:
        filename: The name of the file to analyze_text
    
    Raises:
        IOError: If ``filename`` does not exist or can't be read
    
    Returns: A tuple with first element being the line count and second element being the character count
    """
    line_count = 0
    char_count = 0
    with open(filename, mode="r") as f: # raise IOError
        #return list((sum(1, len(line)) for line in f))
        for line in f:
            line_count += 1
            char_count += len(line)
        return (line_count, char_count)


# To create test cases with unittest framework create a class derived from unittest.TestCase
class TestAnalyzerTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""
    

    # to create pre-fixture which runs before each testing method
    def setUp(self):
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'text_analysis_test_file.txt'
        # write 4 lines to the file 
        with open(self.filename, mode="wt", encoding = "utf-8") as f:
            f.write('Now we ar engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.') # note that adjacent strings will concatenate together!
    

    # to create post-fixture which runs after testing methods
    def tearDown(self):
        """Fixture that will delete the files used by the test methods"""
        try:
            os.remove(self.filename)
        except IOError:
            pass # ignore any error as tearDown can't be sure the file actually exists



    #To create individual test methods simply name it beginning with test_ then they're automatically discovered by the unittest framework and don't require any sort of registration.
    def test_function_run(self):
        """Basic smoke test: does the function run at all"""
        analyze_text(self.filename)
    

    def test_line_count(self):
        """Check the line count is correct"""
        with open(self.filename, mode="r") as f:
            #print('result:', analyze_text(self.filename))
            self.assertEqual(analyze_text(self.filename)[0], 4)

    
    def test_character_count(self):
        """Check the character count is correct"""
        with open(self.filename, 'r') as f:
            self.assertEqual(analyze_text(self.filename)[1], 130)
    

    def test_raise_error(self):
        """Check raising correct error for missing file."""
        with self.assertRaises(IOError):
            analyze_text('foo.txt')

    
    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))
    

if __name__ == '__main__':
    unittest.main() # this will search all sub-classes of unittest and run all their test methods. 
