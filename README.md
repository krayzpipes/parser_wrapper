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

