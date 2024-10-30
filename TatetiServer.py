from DFServer import *

class TatetiServer(DFServer):

    class TatetiPlayer(Enum):
        p1 = 'jugador 1'
        p2 = 'jugador 2'
        tie = 'empate'

    def __init__(self, host = '127.0.0.1', port = 5000):
        super().__init__(DFServer.DFServerType.type1, gameName = 'tateti', host = host, port = port)

    def showPlaying(self, player : TatetiPlayer):
        if not isinstance(player, TatetiServer.TatetiPlayer):
            raise ValueError("player must be of type 'TatetiServer.TatetiPlayer")

        if player == TatetiServer.TatetiPlayer.p1:
            currScreen = DFServer.DFType1Screens.playingP1
        else:
            currScreen = DFServer.DFType1Screens.playingP2
        
        if currScreen != self._lastScreen:
            self._socketio.emit('change-screen',{'screenId': currScreen.value})
            self.__lastScreen = currScreen

    def showWinner(self, player : TatetiPlayer):
        if not isinstance(player, TatetiServer.TatetiPlayer):
            raise ValueError("player must be of type 'TatetiServer.TatetiPlayer")
        
        if player == TatetiServer.TatetiPlayer.p1:
            currScreen = DFServer.DFType1Screens.finishedP1
        elif player == TatetiServer.TatetiPlayer.p2:
            currScreen = DFServer.DFType1Screens.finishedP2
        else:
            currScreen = DFServer.DFType1Screens.finishedTie

        if currScreen != self.__lastScreen:
            self._socketio.emit('change-screen',{'screenId': currScreen.value})
            self.__lastScreen = currScreen

if __name__ == "__main__":

    server = TatetiServer()
    server.start()

    sleep(2)

    for t in range(5):
        server.showCountdown(t)
        sleep(1)

    players = [player for player in TatetiServer.TatetiPlayer][:-1]

    players *= 3

    for player in players:
        server.showPlaying(player)
        sleep(1)

    players = [player for player in TatetiServer.TatetiPlayer]

    for player in players:
        server.showWinner(player)
        sleep(1)

    sleep(1000)