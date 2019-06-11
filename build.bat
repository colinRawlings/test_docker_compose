@ECHO OFF

set this_script_folder=%~dp0
set this_script_drive=%~d0

pushd this_script_drive

docker build --rm -t python_runner:latest %this_script_folder%\Dockerfiles\python_runner

popd