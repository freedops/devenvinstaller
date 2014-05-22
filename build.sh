#!bin/bash
# This script builds all the other scripts needed to create_build
# a project development installer

# Copyright 2014 freedops.org
#
# This file is part of the freedops.org tools collection.
#
# The freedops.org tools collection is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# The freedops.org tools collection is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the freedops.org tools collection.
#
# If not, see <http://www.gnu.org/licenses/>.

if [ ! $1 ];then
    echo Error, no properties file specified, format: build.sh properties_file
    exit
fi

# this is to allow the installer for devenvinstall to be built outside a
# docker container
if [ ! $2 ];then
    wrapdocker &
fi

# clean project files
rm -rf Docker
rm -f build_docker.sh
rm -f setup.sh
rm -rf installer
rm -f *.tar

# set up folders
mkdir Docker
mkdir Docker/Container
mkdir installer
mkdir Docker/Wrap
cp ../dockdock/dind/wrapdocker Docker/Wrap/wrapdocker
cp /usr/local/bin/wrapdocker Docker/Wrap/wrapdocker

export PYTHONPATH=~/workspace/Freedops/Python/Instance/:~/workspace/Freedops/Python/Props_man:/var/local/project/freedops/Python/Props_man:/var/local/project/freedops/Python/Instance
python3 Python/create_build.py $1
sh build_docker.sh
 