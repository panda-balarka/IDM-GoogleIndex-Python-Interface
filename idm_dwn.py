''' 
Download the files from sublinks in the main index link. Usefull to download whole seasons of serialtrons, pdf collections, etc.
Rusn the IDM downloader for all the files in one go. :D

- panda_inline4
'''

# import required libraries
import urllib.request
import lxml.html
import os

# have a counter variable incase the download is done with Series name of user choice
global seriesIndex_v
seriesIndex_v = 1


def get_links(home_url,destination_path,string_seriesName):
        """ 
        Function to extract the file sublinks from the main index link provided. Then call the interface method 
        to initiate the download from IDM manager silently
        """
        
        # establish the connection to main index link
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
        """
        Check if the file to be downloaded already exists, else start the download of the file via IDM manager
        """
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
