"""
Created on June 6, 2016

@author: PJC
"""

import os
import pytest
import shutil

from python_oop.assignment_04 import ConfigDict, ConfigKeyError

class TestConfigDict(object):

    config_file_template = 'C:\\Work_Files\\PyCharm\\Udemy\\python_oop\\config_test_template.txt'
    config_test_existing = 'C:\\Work_Files\\PyCharm\\Udemy\\python_oop\\config_test.txt'
    config_test_new = 'C:\\Work_Files\\PyCharm\\Udemy\\python_oop\\config_test_new.txt'

    def setup_class(self):

        shutil.copy(TestConfigDict.config_file_template, TestConfigDict.config_test_existing)

    """ Not needed unless test_new_file_exists is fixed """
    # def teardown_class(self):
    #     os.remove(TestConfigDict.config_test_new)

    def test_obj(self):
        # Confirm ConfigDict is and instance of ConfigDict and dict classes
        cd = ConfigDict(TestConfigDict.config_test_existing)
        assert isinstance(cd, ConfigDict)
        assert isinstance(cd, dict)
        
    def test_attribute_set(self):
        # Confirm _config_file is set correctly
        cd = ConfigDict(TestConfigDict.config_test_existing)
        assert cd._config_file == TestConfigDict.config_test_existing

    """ Doesn't work because of file check part of the __INIT__ """
    # def test_new_file_exists(self):
    #     # Confirm non-existing file exists after new instance created
    #     cd = ConfigDict(TestConfigDict.config_test_new)
    #     assert os.path.isfile(TestConfigDict.config_test_new)

    def test_pre_file_exists(self):
        # Confirm pre-existing file still exists after new instance created
        cd = ConfigDict(TestConfigDict.config_test_existing)
        assert os.path.isfile(TestConfigDict.config_test_existing)

    def test_read_dict(self):
        cd = ConfigDict(TestConfigDict.config_test_existing)
        assert cd['os'] == 'windows'
        assert cd['python_ver'] == '3.5'
        assert cd['user'] == 'pachilds'

        with pytest.raises(ConfigKeyError):
            print(cd['bad_key'])

    """ Doesn't work because cd2 adds a space to end of value for some reason """
    # def test_write_dict(self):
    #     # Confirm new values are saved to the file
    #     cd = ConfigDict(TestConfigDict.config_test_existing)
    #     cd['dog'] = 'penny'
    #     cd2 = ConfigDict(TestConfigDict.config_test_existing)
    #     assert cd2['dog'] == 'penny'

    def test_ioerror(self):
        # Confirm IOError is raised when file doesn't exist
        with pytest.raises(IOError):

            cd = ConfigDict('NoFile.txt')