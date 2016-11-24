import sys
import os

sys.path.insert(0, os.path.abspath('..\\'))

import pyximport
pyximport.install()

from eudplib import *

LoadMap('outputmap/basemap/basemap_inlinecode.scx')


@EUDFunc
def main():
    if EUDWhile()(Always()):
        RunTrigTrigger()
        EUDDoEvents()
    EUDEndWhile()


SaveMap('outputmap/testinlinecode.scx', main)
