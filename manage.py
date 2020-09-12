from isDoorOpen import create_server
from flask_script import Manager
from os.path import exists
from os.path import isdir
from os import mkdir

server = create_server()
manager = Manager(server)

if __name__ == '__main__':

    if not (exists("data") and isdir("data")):
        print("data folder not exists, creating...")
        mkdir("data")

    manager.run()
