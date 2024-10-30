from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread
from time import sleep
from os import path
from enum import Enum

class DFServer():
    class DFServerType(Enum):
        type1 = 'type1'
        type2 = 'type2'
        type3 = 'type3'
        type4 = 'type4'

    def __init__(self, clientType : DFServerType, gameName : str, gameUnit = None, host = '127.0.0.1', port = 5000):
        if not isinstance(clientType, DFServer.DFServerType):
            raise ValueError("clientType must be of type 'DFServerType'")

        self.__app = Flask(__name__)
        self.socketio = SocketIO(self.__app)
        self.__host = host
        self.__port = port
        self.__gameName = gameName
        self.__gameUnit = gameUnit

        self.__serverRunning = False

        dir = path.join(path.dirname(path.abspath(__file__)),'screens_generic')
        with open(path.join(dir,'screens_generic.html'),'r') as f:
            self.__screens_content = f.read()
        with open(path.join(dir,f'screens_{clientType.value}.html'), 'r') as f:
            self.__screens_content += f.read()

        @self.__app.route('/')
        def __renderTotem():
            return render_template('totem.html', screensContent = self.__screens_content, gameName = self.__gameName, gameUnit = gameUnit)

    def __server(self):
        print('socketio run')
        self.socketio.run(self.__app, self.__host, self.__port, use_reloader = False)

    def start(self):
        if self.__serverRunning == False:
            self.__serverRunning = True
            self.__serverThread = Thread(target = self.__server)
            self.__serverThread.daemon = True
            self.__serverThread.start()