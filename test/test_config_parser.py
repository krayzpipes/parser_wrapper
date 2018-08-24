import unittest

from pyfakefs.fake_filesystem_unittest import Patcher

from parser_wrapper.config_parser import ConfigParserWrapper


class TestConfigParserWrapper(unittest.TestCase):

    def setUp(self):
        self.patcher = Patcher()
        self.patcher.setUp()
        self.wrapper = ConfigParserWrapper()

    def test_read_normal_file_success(self):
        good_config = ("[TestSection]\n"
                       "item1=answer1\n"
                       "item2=answer2\n")
        self.patcher.fs.create_file('/foo/bar', contents=good_config)
        self.wrapper.read('/foo/bar')
        self.assertEqual(['TestSection'], self.wrapper.sections())
        self.assertEqual('answer1', self.wrapper.get('TestSection', 'item1'))
        self.assertEqual('answer2', self.wrapper.get('TestSection', 'item2'))

    def test_read_string_file_success(self):
        good_config = ("[TestSection]\n"
                       "item1=answer1\n"
                       "item2=answer2\n")
        self.wrapper.read(good_config)
        self.assertEqual(['TestSection'], self.wrapper.sections())
        self.assertEqual('answer1', self.wrapper.get('TestSection', 'item1'))
        self.assertEqual('answer2', self.wrapper.get('TestSection', 'item2'))

    def test_read_dictionary_file_success(self):
        good_config = {
            'TestSection': {
                'item1': 'answer1',
                'item2': 'answer2',
            }
        }
        self.wrapper.read(good_config)
        self.assertEqual(['TestSection'], self.wrapper.sections())
        self.assertEqual('answer1', self.wrapper.get('TestSection', 'item1'))
        self.assertEqual('answer2', self.wrapper.get('TestSection', 'item2'))
    '''
    def test_read_file_object_success(self):
        good_config = ("[TestSection]\n"
                       "item1=answer1\n"
                       "item2=answer2\n")
        self.patcher.fs.create_file('/foo/bar', contents=good_config)
        with open('/foo/bar', 'r') as file_:
            self.wrapper.read(file_)
        self.assertEqual(['TestSection'], self.wrapper.sections())
        self.assertEqual('answer1', self.wrapper.get('TestSection', 'item1'))
        self.assertEqual('answer2', self.wrapper.get('TestSection', 'item2'))
    '''
    def tearDown(self):
        self.patcher.tearDown()
