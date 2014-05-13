'''
Created on 5 May 2014

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
import plain_pickle
import string


class BuildFromTemplate(object):
    '''
    base class for building files from a template and a set of properties.
    '''

    def __init__(self, template, inputdata, out_file, master_file):
        '''
        Constructor
        inputs:
          template
          inputdata
          out_file
        outputs:
          text file named out_file stored in ?
        '''
        self.data = plain_pickle.PlainPickle()
        if self.data.read(inputdata):
            raise FileNotFoundError('Could not find input file')
        if self.data.read(master_file):
            raise FileNotFoundError('Could not find master properties file')
        self.run_rules()
        with open(template, 'r+') as plate:
            filein = string.Template(plate.read())

        text_out = filein.safe_substitute(self.data.pjd)
        with open(out_file, 'w+') as docker_out:
            docker_out.write(text_out)

    def run_rules(self):
        '''
        Apply a set of rules to generate missing properties in template.
        '''
        pass
        