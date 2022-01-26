# unhackable_calculator

Pythonistas [Remote Code Execution Meetup](https://www.meetup.com/pythonistas/events/283364790/) on January 22, 2022

## Setup
* Install [docker-compose](https://docs.docker.com/compose/install/)
* Install [poetry](https://python-poetry.org/docs/)

## Usage
### Poetry
`TODO`

### Docker
```bash
# clean build (remove `--no-cache` for speed)
docker-compose build --no-cache --parallel

# start container
docker-compose up --remove-orphans -d

# exec into container
docker attach unhackable

# destroy container
docker-compose down
```

#### Troubleshooting
* Watch logs in real-time: `docker-compose logs -tf --tail="50" unhackable`
* Check exit code
    ```bash
    $ docker-compose ps
    Name                          Command               State    Ports
    ------------------------------------------------------------------------------
    docker_python_dockerpython_1   python manage.py runserver ...   Exit 0
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
