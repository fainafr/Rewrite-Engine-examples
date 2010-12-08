#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# דוגמה ברמה נמוכה יותר של קוד, המאפשרת הדגמה מלאה של שינוי ייעוד נתיב הכתובת

import SocketServer
from twisted.web.google import checkGoogle
from twisted.internet import reactor

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
        if self.data.startswith('GET'):
            self.sdata = self.data.split()[1]
            getattr(self,self.sdata.split('/')[1])(self.request,self.sdata.split('/')[2])
    
    def echo(self,requestobj,data):
        requestobj.send(data)
    
    def google(self,requestobj,data):
        checker = checkGoogle(data)
        checker.addCallback(
                            lambda l: (requestobj.send(l), reactor.stop())
                            )
        

if __name__ == "__main__":
    HOST, PORT = "", 8880

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()