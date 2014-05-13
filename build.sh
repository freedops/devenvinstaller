#!bin/bash
if [ ! $1 ];then
    echo Error, no properties file specified, format: build.sh properties_file
    exit
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

export PYTHONPATH=~/workspace/Freedops/Python/Instance/:~/workspace/Freedops/Python/Props_man
python3 Python/create_build.py $1
sh build_docker.sh
 