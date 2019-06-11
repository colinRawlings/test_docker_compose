FROM stefanscherer/chocolatey

ENV PYTHONIOENCODING=UTF-8

RUN choco install -y python3
RUN pip install junit-xml

RUN choco install -y nodejs.install
RUN npm i -g xunit-viewer
