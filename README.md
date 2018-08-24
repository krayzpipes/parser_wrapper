# parser_wrapper
Wrapper for ConfigParser to enable easier unit testing: Allows same functions to be used reading a file or string as a configuration.

### Without parser wrapper

```python
from configparser import ConfigParser

#  Reading a file
parser = ConfigParser()
parser.read('config_file.cfg')

# Reading a string
read_me = ("[DEFAULT]\n"
           "option1=Hello\n"
           "option2=World\n")
parser = ConfigParser()
parser.read_string(read_me)
```

### Using parser wrapper:

```python
from parser-wrapper import ParserWrapper

# Reading a file
parser = ParserWrapper()
parser.read('config_file.cfg')

# Reading a string
read_me = ("[DEFAULT]\n"
           "option1=Hello\n"
           "option2=World\n")
parser = ParserWrapper(string=True)
parser.read(read_me)
```

How does that help?

This helps during unit testing.  Let's suppose you have a function that requires reading an .ini-formatted config file. Within this function, you would change the assignment of the config parser:

#### Instead of:
```python
from configparser import ConfigParser
import unittest

def get_config(config_name):
    config = ConfigParser()
    config.read(config_name)
    config.get('DEFAULT', 'option1')
    
class ConfigTest(unittest.TestCase):
    def test_get_config(self):
        read_me = ("[DEFAULT]\n"
                   "option1=Hello\n"
                   "option2=World\n")
        try:
            get_config(read_me)
        except Exception:
            self.fail("Couldn't parse config")
        
# ^^^^ this test will throw an error
```

#### Change your function to accept a ParserWrapper object:

This won't require you to change your code. You can still use '.read()', but you are passing a wrapper which knows how to read a string even when you use '.read()'.

```python
from parser-wrapper import ParserWrapper
import unittest

def get_config(config_item, parser=None):
    config = parser or ParserWrapper()
    config.read(config_item)

class ConfigTest(unittest.TestCase):
    def test_get_config(self):
        read_me = ("[DEFAULT]\n"
                   "option1=Hello\n"
                   "option2=World\n")
        parser = ParserWrapper(string=True)
        try:
            get_config(read_me, parser=parser)
        except Exception:
            self.fail("Couldn't parse config")
