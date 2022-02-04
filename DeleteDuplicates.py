from sys import *
import hashlib
import os
import time

def DeleteDuplicateFiles(dups):
    results=list(filter(lambda x:len(x)>1,dups.values()))
    icnt=0
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0
    else:
        print("No duplicate files found")

def hashfile(path,block_size=1024):
    afile = open(path,'rb')
    hasher=hashlib.md5()
    buff=afile.read(block_size)
    while len(buff)>0:
        hasher.update(buff)
        buff=afile.read(block_size)
    afile.close()

    return hasher.hexdigest()

def FindDuplicates(path):
    flag = os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    
    exists=os.path.isdir(path)

    dups={}

    if exists:
        for dirname,subdirs,filelist in os.walk(path):
            print("Current directory: " + dirname)
            for filename in filelist:
                path = os.path.join(dirname,filename)
                filehash=hashfile(path)

                if filehash in dups:
                    dups[filehash].append(path)
                else:
                    dups[filehash]=[path]
        
        return dups
    else:
        print("Invalid path")

def printresults(dups):
    results=list(filter(lambda x:len(x)>1, dups.values()))
    
    if len(results)>0:
        print("Following are the duplicate files found")
        for result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
    else:
        print("No duplicate files found")
def main():
    print("---------Delete Duplicate Files by Shreyas Kulkarni---------")
    print("Application Name:"+argv[0])

    if len(argv)!=2:
        print("Error: Invalid number of Arguments")
        exit()
    
    if argv[1]=="-h" or argv[1]=="-H":
        print("This Script is used to open predefined urls present in a file")
        exit()
    
    if argv[1]=="-u" or argv[1]=="-U":
        print("Usage: Application_Name Name_of_file")
        exit()
    
    try:
        arr={}
        starttime=time.time()
        arr=FindDuplicates(argv[1])
        printresults(arr)
        DeleteDuplicateFiles(arr)
        endtime=time.time()
        print("Time Consumed: %s"%(endtime-starttime))
    
    except ValueError:
        print("Error: Invalid datatype of input")
    except Exception as E:
        print("Error: ",E)



if __name__ == '__main__':
    main()