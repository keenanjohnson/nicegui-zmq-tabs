FROM python:3.12

# Install D2 for documentation.
RUN curl -fsSL https://d2lang.com/install.sh | sh -s --

# Install python requirements for GUI folder.
COPY requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt
