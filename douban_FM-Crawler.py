#import urllib
import urllib2
import re


class douban_FM:
    "This is a python crawler to crawl the popular music on Douban FM."

    def __init__(self):
        self.url = "http://music.douban.com/musician/"
        self.currentPage = 100001
        self.thresholdValue = 100
        self.txtFile = open('douban_Data.txt', 'w')

    def getData(self):
        try:
            pageInfo = urllib2.urlopen(self.url + str(self.currentPage)).read()
            pageInfo = pageInfo.decode("utf-8")
            numberMatch = self.currentPage
            titleMatch = re.search('<title>(.*?)\\|.*?</title>', pageInfo, re.S)
            contentMatch = re.findall(r'<div class="col song-name-short" data-title="(.*?)">.*?<span class="n_doulists unfoldable">(\d+).*?</span>', pageInfo, re.S)
            data = {}
            for i in contentMatch:
                if int(i[1]) >= self.thresholdValue:
                    data.update({i[0]: i[1]})
            if len(data) > 0:
                print titleMatch.group(1) + "\t" + str(numberMatch)
                #print a
                #self.txtFile.write(a + "\n")
                for i in data:
                    print i, "\t", data[i]
                    #print b
                    #self.txtFile.write(b + "\n")
        except urllib2.URLError as e:
            pass

    def multiPage(self):
        num = 2396
        while num <= 10000:
            self.currentPage = 100000 + num
            self.getData()
            num = num + 1
        #self.txtFile.close()

douban = douban_FM()
douban.multiPage()
