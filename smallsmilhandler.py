#!/usr/bin/python3
# -*- coding: utf-8 -*-


from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class ChistesHandler(ContentHandler):
    def __init__(self):

        self.tags = []
        self.biblio = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "begin", "dur"]
        }

    def startElement(self, name, attrs):
        biblio = {}
        if name in self.biblio:
            biblio['tag'] = name
            for atributo in self.biblio[name]:
                    biblio[atributo] = attrs.get(atributo, "")
            self.tags.append(biblio)

    def get_tags(self):
        return self.tags

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
