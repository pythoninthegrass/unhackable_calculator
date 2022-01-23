# SOURCES:
# https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# https://docs.docker.com/language/python/build-images/
# https://www.docker.com/blog/containerized-python-development-part-1/
# https://www.docker.com/blog/containerized-python-development-part-2/
# https://stackoverflow.com/questions/29245216/write-in-shared-volumes-docker/29251160#29251160
# https://stackoverflow.com/questions/45972608/how-to-give-folder-permissions-inside-a-docker-container-folder
# https://gist.github.com/simonw/ee63bc5e7feb6e8bb3af82f67a7a36fe
# https://stackoverflow.com/questions/30716937/dockerfile-build-possible-to-ignore-error
# https://docs.djangoproject.com/en/3.2/intro/tutorial02/#creating-an-admin-user
# https://stackoverflow.com/questions/49476217/docker-cant-access-django-server
# https://stackoverflow.com/questions/46503947/how-to-get-pipenv-running-in-docker
# https://aka.ms/vscode-docker-python

# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    software-properties-common \
    && apt-get update \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-wheel \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
RUN python3.10 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel && pip3 install --no-cache-dir -r requirements.txt && \
    find /usr/local/lib/python3.10 -name '*.c' -delete || echo "No leftover *.c files" && \
    find /usr/local/lib/python3.10 -name '*.pxd' -delete || echo "No leftover *.pxd files" && \
    find /usr/local/lib/python3.10 -name '*.pyd' -delete || echo "No leftover *pyd files" && \
    find /usr/local/lib/python3.10 -name '__pycache__' | xargs rm -r || echo "__pycache__ is empty"

FROM ubuntu:20.04 AS runner-image

RUN apt-get update && apt-get install --no-install-recommends -y python3 python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home appuser
COPY --from=builder-image --chown=appuser:appuser /opt/venv /opt/venv

RUN mkdir -p /home/appuser/app
COPY --chown=appuser:appuser . /home/appuser/app
WORKDIR /home/appuser/app/helloworld

# In addition to chown above, sets user after files have been copied
USER appuser

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV="/opt/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# EXPOSE 8000
# RUN python manage.py migrate
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/bin/bash"]
