#Written by Rohith Saradhy
# Description:
#  Looks at all the *json files in the root_folder and creates a json file of processes given in the listOfInterest list
#  saves the final process json into a file named by the variable outputName if saveFile is set to True; default is output.json
#  
#Need the following libraries for the function to work:
import json
import glob

def MergeJSON(d1,d2,campaign=None):
    if campaign != None:
        d1['cmdLine']="campaign="+campaign
    for item in d1['processes'].keys():
        for entries in d2['processes'][item]:
            d1['processes'][item].append(entries)
    return d1;

def saveJSON(outputName,data_out):
    with open(outputName,'w') as fp:
        print "Saving to the following file: " + outputName
        json.dump(data_out,fp,sort_keys=True,indent=4)
        print "Done Saving"
    return None
    

def findDataFromCatalog(root_folder, listOfInterest,outputName="output.json",saveFile=False): 
    list_files = glob.glob(root_folder+"/*json")
    if len(list_files) < 1:
        print "The folder does not contain any files...; Please Check Again"
        return None
    else:
        print "Files found... Processing"
    data = {}
    data_out = {}
    data_process = {}
    data_out["cmdLine"] = "campaign="+list_files[0].split('/')[-2]
    for lookingAt in range(0,len(listOfInterest)):
        data_process[listOfInterest[int(lookingAt)]] = []
        for files in list_files:
            
            nameOfFile = files.split('/')[-1].split(".")[0]  
            data[nameOfFile] = json.load(open(files))
            # pprint(data.keys())
        for key in data:
            # pprint(data[key].keys())
            for names in data[key].keys():
                if ('/'+listOfInterest[int(lookingAt)]) in names: #the / in front helps to isolate channels beginning
#                     print listOfInterest[int(lookingAt)]+'\t'+key + "\n" + names + "\n"
                    data_process[listOfInterest[int(lookingAt)]].append(names)
                    
    data_out['processes'] = data_process
    if saveFile:
        saveJSON(outputName,data_out)
        return None
    else:
        return data_out
    
 

