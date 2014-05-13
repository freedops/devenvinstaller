'''
Created on 8 May 2014

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
from build_from_template import BuildFromTemplate


class BuildSetupfile(object):
    '''
    create a setup file to build then test the project based on the input
    properties.
    '''

    def __init__(self, template, input_file, master_file,
                 out_file='setup.sh'):
        '''
        Constructor
        '''
        print('build setup file')
        BuildFromTemplate.__init__(self, template, input_file, out_file,
                                   master_file)
        print('setup file built')

    def run_rules(self):
        '''
        Work out extra properties for the templates
        '''
        # version control
        ver_ctrl = self.data.get_value('version_control')
        get_cmd = '{}_get'.format(ver_ctrl)
        command = '{} {}'.format(self.data.get_value(get_cmd),
                                    self.data.get_value('project_location'))
        self.data.add('get_project', command, 'clone command')
        
        
        