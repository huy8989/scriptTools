# -*- coding: GBK -*-

#@author 89huy89@gmail.com 

#@version 2012-12-29 16:55 
import json
import time
import win32clipboard as c
import win32con as w



def createJson(dict): 
    result = json.dumps(dict)
    return result

def go(go):
	if('N' == go or 'n' == go):
		return False
	else:
		return True

##回写到剪切板
def clipboard(str):
	c.OpenClipboard() #open the clipboard
	c.EmptyClipboard() #clear the clipboard
	c.SetClipboardData(w.CF_TEXT, str)
	c.CloseClipboard() #close the clipboard
	print "copied to clipboard "


if  __name__ == "__main__": 
    print "begin\n" 
    hasNext  = True
    dict = {}
    while(hasNext):
    	key = raw_input("key:")
    	value = raw_input("value:") 
    	dict[key] = value	
    	hasNext = go(raw_input("has next?(Y/N)"))
    
    
    clipboard(createJson(dict))
    print "end\n" 
    time.sleep(2);