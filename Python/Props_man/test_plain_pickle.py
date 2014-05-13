'''
Created on 9 Apr 2014

@author: Scott Reeve

Copyright 2014 freedops.org

This file is part of the freedops.org tools collection.

The freedops.org tools collection is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

The freedops.org tools collection is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the freedops.org tools collection.

If not, see <http://www.gnu.org/licenses/>.
'''
import unittest
import plain_pickle
import os.path


class Test(unittest.TestCase):

    def setUp(self):
        #self.TestPickle = plain_pickle.PlainPickle()
        pass

    def tearDown(self):
        pass

    def testCreateFile(self):
        TestPickle = plain_pickle.PlainPickle()
        try:
            os.remove('params.txt')
        except:
            pass
        TestPickle.save()
        if not os.path.exists('params.txt'):
            assert False

    def testCreateFileNamed(self):
        TestPickle = plain_pickle.PlainPickle()
        try:
            os.remove('p.txt')
        except:
            pass
        TestPickle.save(name='p.txt')
        if not os.path.exists('p.txt'):
            assert False

    def testReadFile(self):
        TestPickle = plain_pickle.PlainPickle()
        if TestPickle.read('test.txt'):
            assert False
        values = TestPickle.get_set('key1')
        assert values[0] == 'value1'
        assert values[1] == 'comment 1 s d'
        # key and value, but no comment
        values2 = TestPickle.get_set('key2')
        if values2:
            assert values2[0] == 'value2'
            assert values2[1] == None
        else:
            assert False
        values3 = TestPickle.get_set('key3')
        if values3:
            assert values3[0] == None
            assert values3[1] == None
        else:
            assert False
        values4 = TestPickle.get_set('key4')
        if values4:
            assert values4[0] == None
            assert values4[1] == 'comment adgag'
        else:
            assert False

    def testAddfield(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_1', 'value_1', 'comment_1')
        value1 = TestPickle.get_set('key_1')
        if value1:
            assert value1[0] == 'value_1'
            assert value1[1] == 'comment_1'
        else:
            assert False

    def testAddField2(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_2', None, 'comment_2')
        value2 = TestPickle.get_set('key_2')
        if value2:
            assert value2[0] == None
            assert value2[1] == 'comment_2'
        else:
            assert False

    def testAddField3(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_3')
        value3 = TestPickle.get_set('key_3')
        if value3:
            assert value3[0] == None
            assert value3[1] == None
        else:
            assert False

    def testAddField4(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_4', comment='as ge')
        value4 = TestPickle.get_set('key_4')
        if value4:
            assert value4[0] == None
            assert value4[1] == 'as ge'
        else:
            assert False

    def testGet(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_4', comment='as ge')
        value4 = TestPickle.get_set('key_4')
        if value4:
            assert value4[0] == None
            assert value4[1] == 'as ge'
        else:
            assert False

    def testClear(self):
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_4', comment='as ge')
        TestPickle.clear()
        try:
            value4 = TestPickle.get_set('key_4')
            assert False
        except:
            assert True

    def testSave(self):
        try:
            os.remove('params.txt')
        except:
            pass
        TestPickle = plain_pickle.PlainPickle()
        TestPickle.add('key_1', 'value_1', 'comment_1')
        TestPickle.add('key_2', None, 'comment 2')
        TestPickle.add('key_4', 'value 2', None)
        TestPickle.add('key_3')
        TestPickle.save()
        if not os.path.exists('params.txt'):
            assert False
        TestPickle.clear()
        try:
            value = TestPickle.get_set('key_1')
            if value:
                assert False
        except:
            pass
        TestPickle.read()
        value = TestPickle.get_set('key_1')
        if value:
            assert value == ['value_1', 'comment_1']
        else:
            assert False
        value2 = TestPickle.get_set('key_2')
        if value2:
            assert value2 == [None, 'comment 2']
        else:
            assert False
        value3 = TestPickle.get_set('key_3')
        print(value3)
        if value3:
            assert value3 == [None, None]
        else:
            assert False
        value4 = TestPickle.get_set('key_4')
        if value4:
            assert value4 == ['value 2', None]
        else:
            assert False


if __name__ == "__main__":
    import sys
    unittest.main()
