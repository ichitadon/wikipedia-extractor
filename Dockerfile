FROM python:3.11.4-slim-buster

# install dependent packages
RUN apt-get -y update && apt-get install -y --no-install-recommends \
  # for install
  curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*# install poetry

WORKDIR /home
ENV HOME /home
RUN curl -sSL https://install.python-poetry.org | python
ENV PATH $PATH:/home/.local/bin
RUN poetry config virtualenvs.create false

WORKDIR /app
COPY . /app

# install full dependencies (includes dev-dependencies)
RUN poetry install