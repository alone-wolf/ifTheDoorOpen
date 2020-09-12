# mySync server

### environment requirement

    >= python3.5

    - flask
    - os
    - json
    - time
    - argparse
    - flask-sqlalchemy
    - flask-script

    tip for development:

    use windows subsystem linux with python-venv

    For my personality, I don't like to code upon pure Windows environment, wsl could be one good choice.

### directory tree

    +--mySync/
    |   +--apps/ (locate apps)
    |   +--common/ (common libs)
    |   |   +--__init__.py
    |   |   +--ext.py
    |   +--config/ (server config)
    |   |   +--__init__.py
    |   |   +--errorpage.py
    |   +--templates/ (view page templates)
    |   |   +--template.html
    |   |   +--temp.html
    |   |   +--index.html
    |   +--static/ (static files for templates)
    |   |   +--...
    +--data/ (store data, auto create)
    |   +--markdown/
    +--manage.py

### server usage

    python3 manage.py runserver
    usage: 
        [-?] [-h HOST] [-p PORT] [--threaded]
        [--processes PROCESSES] [--passthrough-errors] [-d]
        [-D] [-r] [-R] [--ssl-crt SSL_CRT]
        [--ssl-key SSL_KEY]
    default:
        host http://127.0.0.1
        port 5000
        debug mode off
    
