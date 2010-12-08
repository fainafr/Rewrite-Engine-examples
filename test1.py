#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web import google

class Echo(Resource):
    """ מחזירה בדיוק את הפלט שלאחר הכתובת. """
    
    def render_GET(self, request):
        """החזרת הפלט."""
        echo = request.args
        return 'The output: {0}'.format(echo['q'][0])

class Code(Resource):
    """החזרת צופן. """
    
    def render_GET(self, request):
        key = {
               'a': 'b',
               'b': 'c',
               'c': 'd',
               'd': 'e',
               'e': 'f',
               'f': 'g',
               'g': 'h',
               'h': 'i',
               'i': 'j',
               'j': 'k',
               'k': 'l',
               'l': 'm',
               'm': 'n',
               'n': 'o',
               'o': 'p',
               'p': 'q',
               'q': 'r',
               'r': 's',
               's': 't',
               't': 'u',
               'u': 'v',
               'v': 'w',
               'w': 'x',
               'x': 'y',
               'y': 'z'
               }
        newstring = ''
        for letter in request.args['q'][0]:
            if key.has_key(letter):
                newstring = newstring + key[letter]
            else:
                newstring = newstring + letter
        return newstring

class Describe(Resource):
    
    def render_GET(self,request):
        return '{0} is {1}.'.format(request.args['name'][0],request.args['t'][0])

root = Resource()
root.putChild('echo',Echo())
root.putChild('code',Code())
root.putChild('describe',Describe())

factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()