from configparser import ConfigParser


class ConfigParserWrapper(ConfigParser):
    """
    Used to wrap config parser.

    Helpful when unit testing as you can send a string in ini format
    or a file name and then use '.read()' for both instead of having
    to use '.read_string()' for
    """

    def __init__(self, *args, **kwargs):
        """

        """
        super().__init__(*args, **kwargs)

    def read(self, config_item, encoding=None):
        """
        This function transforms .read() into whichever ConfigParser
        read function is appropriate. This is designed to allow you
        to pass a ConfigParserWrapper object to your tests and you
        do not have to change any '.read()' functions to test a
        string or dict.

        """

        if self._read_normal(config_item, encoding=encoding):
            return
        elif self._read_from_string(config_item):
            return
        elif self._read_from_dict(config_item):
            return

    def _read_normal(self, config_item_, encoding=None):

        super().read(config_item_, encoding=encoding)

        if len(self['DEFAULT']) or self.sections():
            return True
        else:
            return False

    def _read_from_string(self, config_item_):

        try:
            super().read_string(config_item_, source="STRING")
        except TypeError:
            return False

        if len(self['DEFAULT']) or self.sections():
            return True
        else:
            return False

    def _read_from_dict(self, config_item_):
        try:
            super().read_dict(config_item_, source="DICT")
        except AttributeError:
            return False

        if len(self['DEFAULT']) or self.sections():
            return True
        else:
            return False
