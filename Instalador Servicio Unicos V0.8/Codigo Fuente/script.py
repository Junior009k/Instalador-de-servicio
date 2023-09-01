from os import system

def instalarServicio(name,path):
    system('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start=auto ')
    print('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start=auto ')

def instalarCounter(name,path):
    system('')


