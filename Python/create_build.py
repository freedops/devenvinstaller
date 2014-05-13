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
if __name__ == "__main__":
    import sys
    from build_from_template import BuildFromTemplate
    from build_runfile import BuildRunfile
    from build_setupfile import BuildSetupfile
    from build_dockerfile import BuildDockerfile 
    
    if len(sys.argv)>1:
        input_file = sys.argv[1]
        master_file = 'Properties/Master_properties'
        build_docker_template = 'Templates/build_docker_template'
        dockerfile_template = 'Templates/Dockerfile_template'
        setup_template = 'Templates/setup_template'
        runfile_template = 'Templates/runfile_template'
        BuildFromTemplate(build_docker_template, input_file, 'build_docker.sh',
                          master_file)
        BuildDockerfile(dockerfile_template, input_file, master_file)
        BuildSetupfile(setup_template, input_file, master_file)
        BuildRunfile(runfile_template, input_file, master_file)
    else:
        print('Error, no imput data file specified')
        
        
