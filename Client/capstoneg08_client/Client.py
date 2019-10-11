import socket
import sys
import threading

from capstoneg08_servermessagehandler import ServerMessageHandler

class Client(threading.Thread):
    isConnected = False
    stopThisThread = False
    
    portNumber = 8888;
    host = 'localhost'
    
    def _init_ (self, portNumber, host):
        threading.Thread.__init__(self)
        self.portNumber = portNumber
        self.host = host
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def connectToServer(self):
        myClientThread = Client(self.ip, self.port)
        myClientThread.start()
        return True
    
    def disconnectFromServer(self):
        try:
            isConnected = False
            self.clientSocket.close()
            self.clientSocket is None
        except socket.error as SocketError:
            print("Unable to disconnect from server", repr(SocketError))
    
    def sendMessageToServer(self, msg):
        self.clientSocket.send(msg)
    
    def stopThread():
        stopThisThread = True
    
    def isConnceted():
        return isConnected
    
    def run(self):
        # create client socket
        try:
            isConnected = True
            self.clientSocket.connect(self.host, self.portNumber)
            myServerMessageHandler = ServerMessageHandler(self.clientSocket)
            stopThisThread = False
        except socket.error as SocketError:
            print("Unable to connect to server", repr(SocketError))
        
        # handle server messages 
        while stopThisThread == False:
            try:
                msg = self.clientSocket.recv()
            except BlockingIOError:
                print("Unable to receive message.", repr(BlockingIOError))
            finally:
                myServerMessageHandler.handleServerMessage(msg)
            break