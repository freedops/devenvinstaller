#!bin/bash
if [ ! $1 ];then
    echo Error, no properties file specified, format: build.sh properties_file
    exit
fi
export PYTHONPATH=~/workspace/Freedops/Python/Instance/:~/workspace/Freedops/Python/Props_man
python3 Python/create_build.py $1
sh build_docker.sh
# tar up the files into a single archive
 