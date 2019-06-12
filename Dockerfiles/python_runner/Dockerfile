# Get appropriate base image:
# - get OsVersion: systeminfo | findstr Build
# - get container tag for OsVersion from Full Tag Listing section: https://hub.docker.com/_/microsoft-windows-servercore
FROM mcr.microsoft.com/windows/servercore:ltsc2019

RUN powershell iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'));

ENV PYTHONIOENCODING=UTF-8

RUN choco install -y python3
RUN pip install junit-xml

RUN choco install -y nodejs.install
RUN npm i -g xunit-viewer

RUN choco install -y vcredist-all
