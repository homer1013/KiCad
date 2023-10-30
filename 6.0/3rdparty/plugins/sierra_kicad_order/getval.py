import os
import urllib.request, urllib.error, urllib.parse
import json
import logging
from . import  globalVars



def getValidate(boardName,vuserid,vtoken,sessionid):

    try:
        infile2 = open(boardName, 'rb')
        ledata2 = {'file': infile2}
        file_name =  boardName.replace('\\','/')
        file_name = file_name.rpartition('/')[2]
        headers = {
                'Authorization': vtoken ,
                'user_id' : vuserid,
                'file_name': file_name,
                'Content-Type':'application/zip',
                'Content-Length':os.stat(boardName).st_size,
                'bomAutoMap' : 'false',
                'sessionId' : sessionid,
                'source' : globalVars.pluginVersion
                    }
        request = urllib.request.Request(globalVars.kicadBackendURL + "/validate?service=validateFile",  data=open(boardName, 'rb'),headers=headers)

        response = urllib.request.urlopen(request)
        return(json.loads(response.read()))
    except Exception as e:
        return False

def getorder(userID):

    res = urllib.request.Request(globalVars.SCABackendURL + "/orderapi/order/getListOfOrderDetails/userID={}".format(userID))
    response = urllib.request.urlopen(res)
    return(json.loads(response.read()))

def redirectCustPortal():
    redirectCustPortalrl = globalVars.FEMSBackendURL + "/customer-portal/"
    return(redirectCustPortalrl)