# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())
allExtLinks=set()
allIntLinks=set()
def getInternalLinks(bsObj, includeUrl):
    internalLinks=[]
    for link in bsObj.findAll("a",href=re.compile(r'^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excluderUrl):
    externalLinks=[]
    for link in bsObj.findAll('a', href=re.compile(r'^(http|www)((?!'+excluderUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html,'lxml')
    externalLinks=getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks)==0:
        internalLinks=getInternalLinks(bsObj,startingPage)
        return getExternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])#getNexExternalLink
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink(startingSite)
    print "随机外链是："+externalLink
    followExternalOnly(externalLink)

def getAllExternalLinks(siteUrl):
    html=urlopen(siteUrl)
    bsObj=BeautifulSoup(html,'lxml')
    internalLinks=getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks=getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print link
    for link in internalLinks:
        if link not in allIntLinks:
            print link
            allIntLinks.add(link)
            getAllExternalLinks(link)
getAllExternalLinks("https://en.wikipedia.org")
#followExternalOnly("http://www.baidu.com/")

