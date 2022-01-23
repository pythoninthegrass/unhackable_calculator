# unhackable_calculator

Pythonistas [Remote Code Execution Meetup](https://www.meetup.com/pythonistas/events/283364790/) on January 22, 2022

## Setup
* Install [docker-compose](https://docs.docker.com/compose/install/)
* Install [poetry](https://python-poetry.org/docs/)

## Usage
### Poetry
`TODO`

### Docker
* Start container
    ```bash
    docker-compose up --build --remove-orphans -d
    ```
* **Note**
    * Running `docker-compose up` will clean up after itself when run without the `-d` switch
    * Analogous to `docker run -it --rm docker_python bash`

#### Troubleshooting
* Watch logs in real-time: `docker logs -tf --tail="50" python-docker`
* Check exit code
    ```bash
    $ docker-compose ps
    Name                          Command               State    Ports
    ------------------------------------------------------------------------------
    docker_python_dockerpython_1   python manage.py runserver ...   Exit 0
    ```

#### Build
* Remove `docker` volume
    ```bash
    $ docker ps -a
    CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS                       PORTS     NAMES
    66696bb035bc   docker_python                 "python manage.py ru…"   8 minutes ago   Exited (0) 36 seconds ago              docker_python_dockerpython_1
    $ docker rm -v 66696bb035bc
    ```
* Remove `docker` image
    ```bash
    docker images
    docker rmi docker_python:latest
    ```
* Rebuild outside of `docker-compose`
    ```bash
    # build
    docker build --tag docker_python .

    # tag as version other than latest
    docker tag <457e6d6c2d25> docker_python:v1.5
    ```

## TODO
* Poetry
* ~~Dockerfile~~
* Playwright
```bash
# generate boilerplate code
playwright codegen https://app.cloud-logon.com/dev/calculator
```
* Hack [sw33tr0ll](https://github.com/sw33tr0ll)'s [Lambda box](https://app.cloud-logon.com/dev/calculator) (no DDoS plz)
