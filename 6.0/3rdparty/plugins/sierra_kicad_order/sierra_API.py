#  sierra_API.py
#
#  Copyright (C) 2019 Sierra Circuits, Inc
#
#  Designed by KiCad Services, Inc.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import sys
import datetime
import urllib.request, urllib.error, urllib.parse
from urllib.parse import quote
from . import  globalVars
# from urllib import addinfourl
import json
import uuid

import logging

class sierra_api:

    NO_ERROR      =  0
    UNKOWN_ERROR  = -1
    NETWORK_ERROR = -2
    AUTH_ERROR    = -3
    pswd = ""

    def __init__(self, logger, uuid_input = ""):
        self.username = ""
        self.password = ""
        self.user_id = ""
        self.refresh_token = ""
        self.access_token = ""
        self.session_id = ""
        self.logged_in = False
        self.token_time = datetime.datetime.now()
        self.last_error = 0
        self.last_error_message = ""
        self.registration_msg ="Not"
        self.new_registration = False
        self.resetpass = False
        self.force_password_reset = 0

        if uuid_input == "":
            self.uuid = uuid.uuid1()
        else:
            self.uuid = uuid_input
        self.registered = False
        self.log = logger

        handler=urllib.request.HTTPSHandler(debuglevel=1)
        opener = urllib.request.build_opener(handler)
        urllib.request.install_opener(opener)

    def SetUsername(self, username):
        self.username = username

    def SetPassword(self, password):
        self.pswd = password
        self.password = password

    def RegisterPlugin(self):
        #Register a new client of the device
        msg = urllib.request.Request( globalVars.lambdaURL + "/client",
            data=bytes('{"client_id":"' + str( self.uuid ) + '"}','utf-8'),
            headers={'Content-Type' : 'application/json',
                     'Authorization' : 'Basic '+ str( self.uuid ) }
            )
        self.registered = False

        try:
            resp = urllib.request.urlopen(msg )
        except ValueError as err:
            self.log.error( "Invalid Value Error: " + str(err) )
            return False
        except Exception as err:
            self.log.error("Exception: " + str(err))
            self.last_error = self.NETWORK_ERROR
            return False

        try:
            retdata = resp.read().decode("utf-8") 
            # self.log.debug("Received " + retdata)

            jsondata = json.loads( retdata )

            if( jsondata['status'] == 200 ):
                self.registered = True
        except:
            self.last_error = self.UNKOWN_ERROR
        return self.registered

    def RefreshPlugin(self, refresh = ""):
        # return False
        if self.registered is False:
            if not self.RegisterPlugin():
                return False

        if refresh == "":
            if self.refresh_token == "":
                return False
            else:
                refresh = self.refresh_token

        msg = urllib.request.Request( globalVars.lambdaURL +"/token",
            data=bytes('{"client_id":"' + str(self.uuid) +
                '","refresh_token":"' + str(refresh) + '"}','utf-8'),
            headers={'Content-Type' : 'application/json',
                     'Authorization' : 'Basic '+ str( self.uuid ) }
            )
        msg.get_method = lambda: 'PUT'

        self.logged_in = False

        try:
            datareturn = urllib.request.urlopen( msg ).read().decode("utf-8")
        except urllib.error.HTTPError as h:
            self.last_error = self.NETWORK_ERROR
            try:
                self.last_error_message = h.read()
            except:
                self.last_error_message = h.msg

            self.log.error(self.last_error_message)
        except:
            self.last_error = self.NETWORK_ERROR
            self.last_error_message = "Could not request refresh authorization"
            self.log.error(self.last_error_message)
            return False

        try:
            jsondata = json.loads(datareturn)
            self.refresh_token = jsondata['refresh_token']
            self.user_id = jsondata['user_id']
            self.access_token = jsondata['access_token']

        except:
            self.last_error = self.AUTH_ERROR
            self.last_error_message = "Invalid refresh token"
            self.log.error(self.last_error_message)
            return False

        self.logged_in = True
        self.last_error = self.NO_ERROR
        return True

    def Login(self, username = None, password = None):
        if( username is not None ):
            self.username = username

        if( password is not None ):
            self.pswd = password
            self.password = password

        if self.registered is False:
            if not self.RegisterPlugin():
                return False

        if( self.username is None or self.password is None ):
            self.last_error = self.AUTH_ERROR
            self.last_error_message = "Missing username or password"
            return False

        msg = urllib.request.Request( globalVars.lambdaURL +"/token",
            data=bytes('{"client_id":"' + str( self.uuid ) +
                '","username":"' + self.username +
                '","password":"' + self.password + '"}','utf-8'),
            headers={'Content-Type' : 'application/json',
                     'Authorization' : 'Basic '+ str( self.uuid ) }
            )

        self.logged_in = False

        try:
            datareturn = urllib.request.urlopen( msg ).read()
        except urllib.error.HTTPError as h:
            self.last_error = self.NETWORK_ERROR
            try:
                self.last_error_message = h.read()
            except:
                self.last_error_message = h.msg

            self.log.error(self.last_error_message)
            return False

        except:
            self.last_error = self.NETWORK_ERROR
            self.last_error_message = "Could not request authorization"
            self.log.error(self.last_error_message)
            return False

        try:
            jsondata = json.loads(datareturn)
            self.refresh_token = jsondata['refresh_token']
            self.user_id = jsondata['user_id']
            self.access_token = jsondata['access_token']
            self.force_password_reset = jsondata['force_password_reset']
            self.session_id = jsondata['session_id']

        except:
            self.last_error = self.AUTH_ERROR
            self.last_error_message = "Invalid login"
            self.log.error(self.last_error_message)
            return False

        self.logged_in = True
        self.last_error = self.NO_ERROR
        return True

    def GetMatrix(self, data):

        user = 'user_id=' + self.user_id
        
        msg = urllib.request.Request( globalVars.lambdaURL +'/quote/standardpcb?' + user,
            data = bytes(data,'utf-8'),
            headers = { 'Content-Type' : 'application/json',
                        'Authorization' : 'Bearer '+ str(self.access_token) }
            )

        try:
            remote = urllib.request.urlopen(msg)
            datareturn = remote.read()
        except urllib.error.HTTPError as h:
            self.last_error = self.NETWORK_ERROR
            try:
                self.last_error_message = h.read()
            except:
                self.last_error_message = h.msg

            self.log.error(self.last_error_message)
            return None
        except Exception as e:
            self.last_error = self.UNKOWN_ERROR
            self.last_error_message = "Could not establish connection.  Error: " + str(e)
            self.log.error(self.last_error_message)
            return None

        try:
            jsondata = json.loads( datareturn )

        except:
            self.last_error = self.AUTH_ERROR
            self.last_error_message = "Invalid login"
            return None

        self.last_error = self.NO_ERROR
        return jsondata

    def GetRedirect(self, data):
        class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
            def http_error_302(self, req, fp, code, msg, headers):
                # infourl = addinfourl(fp, headers, req.get_full_url())
                # infourl.status = code
                # infourl.code = code
                return 'infourl'
            http_error_300 = http_error_302
            http_error_301 = http_error_302
            http_error_303 = http_error_302
            http_error_307 = http_error_302

        opener = urllib.request.build_opener(NoRedirectHandler())
        urllib.request.install_opener(opener)

        user = 'user_id=' + self.user_id
        #Modified by Renjith for Order Redirect
        msg = urllib.request.Request(globalVars.kicadBackendURL +'/orderRedirect?' + user + '&' + data,
            headers = { 'Authorization' : str(self.access_token) }
            )

        try:
            remote = urllib.request.urlopen(msg)
            datareturn = remote.read()
            return datareturn
        except urllib.error.HTTPError as h:
            self.last_error = self.NETWORK_ERROR
            try:
                self.last_error_message = h.read()
            except:
                self.last_error_message = h.msg

            self.log.error(self.last_error_message)
            return None
        except Exception as e:
            self.last_error = self.UNKOWN_ERROR
            self.last_error_message = "Could not establish connection.  Error: " + str(e)
            self.log.error(self.last_error_message)
            return None

        try:
            jsondata = json.loads( datareturn )
            self.last_error = self.NO_ERROR
            return jsondata['location']

        except:
            self.last_error = self.AUTH_ERROR
            self.last_error_message = "Invalid server return"
            return None

    def GetCredentials(self):
        return({"user_id": self.user_id,"access_token":self.access_token,"refresh_token":self.refresh_token,"session_id":self.session_id})

    def SetRegistration(self, regdata):

        if self.registered is False:
            if not self.RegisterPlugin():
                return False

        data = str('{"client_id":"' + str( self.uuid ) +
            '","username":"' + regdata["email"] +
            '","password":"' + regdata["password"] +
            '","email":"' + regdata["email"] +
            '","first_name":"' + regdata["firstName"] +
            '","last_name":"' + regdata["lastName"] +
            '","company":"' + regdata["company"] +
            '","phone":"' + regdata["phoneNo"] + '"}')


        msg = urllib.request.Request( globalVars.lambdaURL +"/register",
            data = bytes(data, 'utf-8') ,
            headers={'Content-Type' : 'application/json',
                     'Authorization' : 'Basic '+ str( self.uuid ) }
            )

        self.new_registration = False

        try:
            datareturn = urllib.request.urlopen( msg ).read()
        except urllib.error.HTTPError as h:
            self.last_error = self.NETWORK_ERROR
            try:
                self.last_error_message = h.read()
                errMsg = self.last_error_message.decode('utf-8').split('New user registration failed: ')[-1]
                errMsg = errMsg.replace('\'','"')
                errMsg = json.loads(errMsg)
                self.registration_msg = str(errMsg["errorMessage"])
            except Exception as e:
                self.last_error_message = h.msg
                self.registration_msg = str(e)

            self.log.error(self.last_error_message)
            return False

        except Exception as e:
            self.last_error = self.NETWORK_ERROR
            self.last_error_message = "Could not request authorization"
            self.registration_msg = self.last_error_message
            self.log.error(self.last_error_message)
            return False

        try:
            jsondata = json.loads(datareturn)

        except Exception as e:
            self.last_error = self.AUTH_ERROR
            self.last_error_message = "Invalid Registration"
            self.registration_msg = self.last_error_message
            self.log.error(self.last_error_message)
            return False

        self.new_registration = True
        self.last_error = self.NO_ERROR
        self.last_error_message = "Success: " + datareturn.decode("utf-8") 
        self.log.error(self.last_error_message)
        self.registration_msg = "User registration successful.\n\nPlease check your registered email account to verify your registration with Sierra Kicad Plugin"
        return True

    def ResetPassword(self, rusername):
        if self.registered is False:
            if not self.RegisterPlugin():
                return False

        data = str('{"username":"' + str( rusername ) +
            '","last_name":"' + "Herrington" + '"}')

        msg = urllib.request.Request( globalVars.lambdaURL +"/recover/password",
            data = bytes(data,'utf-8') ,
            headers={'Content-Type' : 'application/json',
                     'Authorization' : 'Basic '+ str( self.uuid ) }
            )

        self.resetpass = False

        try:
            resp = urllib.request.urlopen(msg )
        except ValueError as err:
            self.log.error( "Invalid Value Error: " + str(err) )
            return False
        except Exception as err:
            self.log.error("Exception: " + str(err))
            self.last_error = self.NETWORK_ERROR
            return False

        try:
            retdata = resp.read().decode("utf-8")
            self.log.debug("Received " + retdata)

            jsondata = json.loads( retdata )

            if( jsondata['status'] == 200 ):
                self.resetpass = True
        except:
            self.last_error = self.UNKOWN_ERROR

        return self.resetpass


    def UpdatePassword(self, updata):

        data = str('{"user_id":"' + str( self.user_id  ) +
            '","old":"' + str( updata['old'] ) +
            '","new":"' + str( updata['new'] ) +  '"}')

        msg = urllib.request.Request( globalVars.lambdaURL +"/account/password",
            data =bytes( data,'utf-8') ,
            headers={'Content-Type' : 'application/json',
                     'Authorization' : 'Bearer '+ self.access_token }
            )

        msg.get_method = lambda: 'PUT'

        try:
            resp = urllib.request.urlopen(msg )
        except ValueError as err:
            self.log.error( "Invalid Value Error: " + str(err) )
            return False
        except Exception as err:
            self.log.error("Exception: " + str(err))
            self.last_error = self.NETWORK_ERROR
            return False

        try:
            retdata = resp.read()
            self.log.debug("Received " + retdata)

            jsondata = json.loads( retdata )

            if( jsondata['status'] == 200 ):
                return True
        except:
            self.last_error = self.UNKOWN_ERROR

        return True

