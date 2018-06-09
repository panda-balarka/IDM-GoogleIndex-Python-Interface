# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:01:27 2018

@author: a
"""
import urllib.request
import lxml.html
import os

global seriesIndex_v
seriesIndex_v = 1

def get_links(home_url,destination_path,string_seriesName):
        connection = urllib.request.urlopen(home_url)
        dom =  lxml.html.fromstring(connection.read())
        links = []
        # select the url in href for all a tags(links)
        for link in dom.xpath('//a/@href'): 
                links.append(link)
        links.pop(0)
        for idx,link in enumerate(links):
                links[idx] =  home_url + link
        for idx,link in enumerate(links):
                #print (link)
                download_from_idm(link,destination_path,string_seriesName)

def download_from_idm(url,destination_path,string_seriesName):
        idm_path = 'idman'
        if string_seriesName:
            global seriesIndex_v
            file_name = '"'+string_seriesName+'_'+seriesIndex_v+'"'
            seriesIndex_v += 1
        else:        
            file_name = '"'+url.split('/')[-1]+'"'
        #print(file_name)
        path = ' /n /d "'+url+'" /p '+destination_path +' /f '+file_name
        #print(path)
        if not os.path.exists(os.path.join(destination_path,file_name.split('"')[1])):
            os.system(idm_path+path)