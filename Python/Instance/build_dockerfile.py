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
from build_from_template import BuildFromTemplate


class BuildDockerfile(object):
    '''
    create a runfile to build then test the project based on the input
    properties.
    '''

    def __init__(self, template, input_file, master_file,
                 out_file='Docker/Dockerfile'):
        '''
        Constructor
        '''
        BuildFromTemplate.__init__(self, template, input_file, out_file,
                                   master_file)

    def run_rules(self):
        # check for additional command fields, and add blanks if needed
        additionals = ['additional_cmd', 'additional_os_cmd']
        for extras in additionals:
            numb = 1
            additional_str = '{}_{}'.format(extras, numb)
            extras_str = ''
            while self.data.exists(additional_str):
                print(numb)
                extras_str = extras_str + '\n' + self.data.get_value(
                                                            additional_str)
                numb = numb + 1
                additional_str = '{}_{}'.format(extras, numb)
            
            self.data.add(extras, extras_str,
                           'Data for {}'.format(extras))
            print(extras)
       
        # version control
        os = self.data.get_value('root_dist')
        
        # operating system
        update_cmd = self.data.get_value('{}_update'.format(os))
        self.data.add('update_os', update_cmd, 'update os')

        extra_cmd = self.data.get_value('{}_install'.format(os))
        self.data.add('install_os_sw', extra_cmd, 'install extra software')
        os_extras = ''
        self.data.add('os_extras', os_extras, 'os system extras')