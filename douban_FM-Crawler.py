import urllib
import urllib2
import re


class douban_FM:
    "This is a python crawler to crawl the popular music on Douban FM."

    def __init__(self):
        self.url = "http://music.douban.com/subject/"
        self.getData()

    def getData(self):
        pageInfo = urllib2.urlopen(self.url + "3533452").read()
        print(pageInfo)

douban = douban_FM()
