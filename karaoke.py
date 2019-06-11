#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import SmallSMILHandler
from xml.sax import make_parser
from urllib.request import urlretrieve
from xml.sax.handler import ContentHandler

class KaraokeLocal:

    def __init__(self, file):
        self.get_tags = []
        self.dicc = {}
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        self.get_tags = cHandler.get_tags()

     def __str__(self):
        line_etiqueta = ''
        for biblio in self.lista:
            nom_etiqueta = biblio['tag']
            line_etiqueta += biblio['tag']
            biblio['tag'] = 'tag'
            for atributo, valor in biblio.items():
                if atributo != biblio['tag'] and valor != "":
                    line_etiqueta += '\t'+'{0}="{1}"'.format(atributo, valor)
            line_etiqueta += '\n'
            biblio['tag'] = nom_etiqueta
            return line_etiqueta

    def to_json(self, file):
        smiltojson = file.replace('.smil', '.json')
        with open(smiltojson, 'w') as fichjson:
        json.dump(self.get_tags, fichjson, indent=4)


    def do_local(self):
        for biblio in self.lista:
            for atributo, valor in biblio.items():
                if atributo == 'src':
                    if valor.startswith('http://'):
                        file_local = valor[valor.rfind('/'):]
                        urllib.request.urlretrieve(valor, file_local[1:])
                        biblio['src'] = file_local[1:]

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")
    karaokelocal = KaraokeLocal(file)
    print(karaokelocal)
    karaokelocal.to_json(file)
    karaokelocal.do_local()
    karaokelocal.to_json('local.smil')
    print(karaoke)
