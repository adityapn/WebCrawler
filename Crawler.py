from bs4 import BeautifulSoup
import urllib2
import re

#This dict holds the links of the visited pages to avoid reputation of links 
global_hash = dict() 

# validate_url(url) function : 
# checks if the given url is in the form of http://www.domain_name.type/optionals
# This validation is based on given format not based on the existence of domain

def validate_url(url):
        match = re.search(r'http://[\'"]?([^\'" >]+)',url)
        domain_name = match.group(1)
        if domain_name.find('www') == -1:
                domain_name = "http://www."+domain_name
        else:
                domain_name = "http://"+domain_name
        return domain_name

def Get_Page_Links(lis):
        other_links = [] # maintins the list of links in the page
        print "\nFetched links \n"
        for links in lis:
                match = match = re.search(r'href=[\'"]?([^\'" >]+)', str(links))                
                print match.group(1)+"\n"                
                other_links.append(validate_url(match.group(1)))
        return other_links
        
def crawl(url):
        if not global_hash.has_key(str(url)):
                global_hash[str(url)] = True
        else:                
                return
        mysite = None
        try:                
                mysite = urllib2.urlopen(url)
        except Exception:
                return
        print "\nFor "+str(url)+"\n"        
        html = mysite.read()
        soup = BeautifulSoup(html)
        links = soup.findAll('a',href=re.compile(r'http://[\'"]?([^\'" >]+)'))
        other_links_in_page = Get_Page_Links(links)
        
        if other_links_in_page is not None:
                for link in other_links_in_page:                        
                                crawl(link)                       
        
def main():      
      url = str(raw_input("Enter the target url : "))
      print "Processing ...\n"
      crawl(validate_url(url))
      

if __name__ == "__main__":main()
