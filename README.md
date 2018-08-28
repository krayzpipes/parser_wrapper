# parser_wrapper
Wrapper for ConfigParser to enable easier unit testing: Instead of using ConfigParser.read_string(), ConfigParser.read_dict(), or ConfigParser.read_file(), you can just use ConfigParserWrapper.read().

### Without ConfigParserWrapper

If your program normally reads a config file from the file system, then it is difficult to perform unit tests without said tests actually becoming integration tests.  For example, if you wanted to test the following function, you would have to use a fake file system that actually resides in memory:

```python

def get_config(config_file):
   parser = ConfigParser()
   parser.read(config_file)
   return parser
```

### With ConfigParserWrapper

If you use ConfigParserWrapper in addition to a slight change to your function implementation, you can use a string or dictionary instead of having to use a fake file system while unit testing.

```python
from parser_wrapper import ConfigParserWrapper

def get_config(config_info):
    parser = ConfigParserWrapper()
    parser.read(config_info)
    return parser
    
import unittest

class TestConfigParser(unittest.TestCase):
    
    def test_get_config(self):
        read_me = ("[DEFAULT]\n"
                   "option1=Hello\n"
                   "option2=World\n")
        test_parser = get_config(read_me)
        self.assertEqual('Hello', test_parser.get('DEFAULT', 'option1')

```

