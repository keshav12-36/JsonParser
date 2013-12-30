# encoding: utf-8
__author__ = 'lgl'

import JsonParser
import unittest

class PyTest(unittest.TestCase):
    pyjson = JsonParser.JsonParser()
    load = pyjson.load
    dump = pyjson.dump
    loadJson = pyjson.loadJson
    dumpJson = pyjson.dumpJson
    loadDict = pyjson.loadDict
    dumpDict = pyjson.dumpDict
    # def __init__(self):
    #     self.pyjson = JsonParser()
    #     self.load = self.pyjson.load
    #     self.dump = self.pyjson.dump
    #     self.loadJson = self.pyjson.loadJson
    #     self.dumpJson = self.pyjson.dumpJson
    #     self.loadDict = self.pyjson.loadDict