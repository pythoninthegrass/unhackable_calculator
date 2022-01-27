# unhackable_calculator

Pythonistas [Remote Code Execution Meetup](https://www.meetup.com/pythonistas/events/283364790/) on January 22, 2022

## Setup
* Install 
    * [editorconfig](https://editorconfig.org/)
    * [poetry](https://python-poetry.org/docs/)
    * [docker-compose](https://docs.docker.com/compose/install/)
    * [playwright](https://playwright.dev/python/docs/intro#installation)

## Usage
### Poetry
```bash
# Install
curl -sSL https://install.python-poetry.org | $(which python3) -

# Change config
poetry config virtualenvs.in-project true          # .venv in `pwd`
poetry config experimental.new-installer false     # fixes JSONDecodeError on Python3.10

# Activate virtual environment (venv)
poetry shell

# Deactivate venv
exit  # ctrl-d

# Install multiple libraries
poetry add google-auth google-api-python-client

# Initialize existing project
poetry init

# Run script and exit environment
poetry run python your_script.py

# Install from requirements.txt
poetry add `cat requirements.txt`

# Update dependencies
poetry update

# Remove library
poetry remove google-auth

# Generate requirements.txt
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### Docker
```bash
# clean build (remove `--no-cache` for speed)
docker-compose build --no-cache --parallel

# start container
docker-compose up --remove-orphans -d

# exec into container
docker attach unhackable

# run command inside container
python unhackable.py

# destroy container
docker-compose down
```

#### Docker Troubleshooting
* Watch logs in real-time: `docker-compose logs -tf --tail="50" unhackable`
* Check exit code
    ```bash
    $ docker-compose ps
    Name                          Command               State    Ports
    ------------------------------------------------------------------------------
    docker_python      python manage.py runserver ...   Exit 0
    ```

### Playwright
```bash
# install
pip install --upgrade pip
pip install playwright
playwright install

# download new browsers (chromedriver, gecko)
npx playwright install

# generate code via macro
playwright codegen wikipedia.org
```

## TODO
* ~~Poetry~~
* ~~Dockerfile~~
* ~~Playwright~~
* Hack [sw33tr0ll](https://github.com/sw33tr0ll)'s [Lambda box](https://app.cloud-logon.com/dev/calculator) (no DDoS plz)
