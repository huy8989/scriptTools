# -*- coding: GBK -*-

#@author 89huy89@gmail.com 

#@version 2012-12-24 16:11 
import shutil 
import time

Source_File_Path = "C://Windows/System32/drivers/etc/"
Target_File_Path = "C://Windows/System32/drivers/etc/"
File_Name="hosts"
File_Name1 = "hosts_yufa"
File_Name2 = "hosts_normal"

def moveFileto(sourceDir, targetDir): 
    shutil.copy(sourceDir, targetDir)


if  __name__ == "__main__": 
    print "绑定预发环境(B) or 卸载预发环境(X) \n" 
    
    answer = raw_input() 
    if  ('B'== answer or'b' ==answer): 
        moveFileto(Source_File_Path + File_Name1, Target_File_Path + File_Name) 
        print "预发环境绑定成功"
    elif   ('X'== answer or 'x' ==answer):  
        moveFileto(Source_File_Path + File_Name2, Target_File_Path + File_Name) 
        print "预发环境卸载成功" 
    else: 
        print "not the correct command"
    
    time.sleep(2);