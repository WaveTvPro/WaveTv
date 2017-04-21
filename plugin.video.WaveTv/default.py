# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
import httplib
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
import plugintools
import zipfile
import time
import ntpath
import cookielib
import buggalo
import extract
import downloader
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from datetime import date , datetime , timedelta
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.WaveTv'
oo = 'plugin.video.WaveTv'
i1iII1IiiIiI1 = "0.0.7"
iIiiiI1IiI1I1 = xbmc . translatePath ( 'special://home/addons/' )
o0OoOoOO00 = base64 . decodestring
I11i = datetime . now ( )
O0O = xbmc . translatePath ( 'special://logpath/' )
Oo = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1ii11iIi11i = xbmcaddon . Addon ( id = oo )
I1IiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
o0OOO = 'plugin.video.WaveTv'
iIiiiI = xbmcgui . DialogProgress ( )
Iii1ii1II11i = "Wave Tv"
iI111iI = Net ( )
IiII = xbmc . translatePath ( 'special://home/' )
o0OoOoOO00 = base64 . decodestring
iI1Ii11111iIi = xbmc . translatePath ( 'special://profile/' )
i1i1II = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
O0oo0OO0 = os . path . join ( IiII , 'userdata' )
I1i1iiI1 = os . path . join ( O0oo0OO0 , 'addon_data' , o0OO00 )
iiIIIII1i1iI = os . path . join ( iIiiiI1IiI1I1 , 'packages' )
o0oO0 = I1ii11iIi11i . getSetting ( 'User' )
oo00 = I1ii11iIi11i . getSetting ( 'WUSE' )
o00 = os . path . join ( I1i1iiI1 , 'wizard.log' )
Oo0oO0ooo = I1ii11iIi11i . getSetting ( 'Pass' )
o0oOoO00o = I1ii11iIi11i . getSetting ( 'AdultPass' )
i1 = ( o0OoOoOO00 ( 'aHR0cDovL3dhdmVtZWRpYS54MTAubXgv' ) )
oOOoo00O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oo , 'icon.png' ) )
i1111 = i1 + ( o0OoOoOO00 ( 'YWRkb24vYXJ0Lw==' ) )
i11 = i1 + oo00 + ( o0OoOoOO00 ( 'L3dhdmUudHh0' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
I11 = i1 + ( o0OoOoOO00 ( 'YWRkb24vYXBrLnR4dA==' ) )
Oo0o0000o0o0 = ( o0OoOoOO00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwLw==' ) )
oOo0oooo00o = 'https://wavemedia.ecwid.com/'
oO0o0o0ooO0oO = ( o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
oo0o0O00 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.WaveTv' )
oO = xbmc . translatePath ( 'special://thumbnails' ) ;
i1iiIIiiI111 = "WaveTv"
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + oo , 'fanart.jpg' ) )
i1iiIII111ii = I1ii11iIi11i . getLocalizedString
i1iIIi1 = CookieJar ( )
ii11iIi1I = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( i1iIIi1 ) )
ii11iIi1I . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iI111I11I1I1 = int ( sys . argv [ 1 ] )
OOooO0OOoo = xbmc . translatePath ( I1ii11iIi11i . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
O0oo0OO0 = xbmc . translatePath ( 'special://home/userdata/' )
iIii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOOoO0 = oo0o0O00 + '/addons.ini'
O0OoO000O0OO = xbmcgui . Dialog ( )
if 23 - 23: iIiIiIiIIi + ooOoo0O
if 76 - 76: i1II1I11 / i1I / OO0o / ooO0o0Oo % Oo00OOOOO
if 85 - 85: O0O00o0OOO0 . O0o / o0 + I11ii1 / I11II1i
def IIIII ( ) :
 ooooooO0oo ( )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Live Lists[/COLOR]' , '' , 9 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Movies[/COLOR]' , o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvTW92aWVzL01vdmllcy5waHA=' ) , 21 , i1111 + '2.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]World Radio[/COLOR]' , '' , 50 , i1111 + '3.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Wizard[/COLOR]' , '' , 19 , i1111 + '4.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Maintenance[/COLOR]' , '' , 5 , i1111 + 'standard.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]APK Installer[/COLOR]' , '' , 60001 , i1111 + 'a.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Login[/COLOR]' , '' , 18 , i1111 + '7.png' , oooOOOOO , '' )
 if 13 - 13: OOoo0O0 + Ii + I1I - i1IIi % OO0o - i1I
def OOO00 ( ) :
 IIiiiiiiIi1I1 ( '[COLORsteelblue]My Account[/COLOR]' , '' , 10 , i1111 + '7.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Channel Lists[/COLOR]' , '' , 16 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Live Sport[/COLOR]' , ( o0OoOoOO00 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 22 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]Guide Menu[/COLOR]' , '' , 211 , i1111 + '13.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40 , i1111 + 'standard.png' , oooOOOOO , '' )
 iiiiiIIii ( '[COLORsteelblue]Get Short Links[/COLOR]' , '' , 214 , i1111 + '14.png' , oooOOOOO , '' )
 if 71 - 71: O0o + I11ii1 * O0o - i1I * ooO0o0Oo
def Oooo0Ooo000 ( ) :
 ooii11I = Ooo0OO0oOO ( o0OoOoOO00 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 ii11i1 = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( ooii11I )
 for IIIii1II1II , i1I1iI in ii11i1 :
  IIiiiiiiIi1I1 ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , 'http://www.listenlive.eu/' + IIIii1II1II , 51 , i1111 + '3.png' , '' , '' )
def oo0OooOOo0 ( url ) :
 ooii11I = Ooo0OO0oOO ( url )
 ii11i1 = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( ooii11I )
 for i1I1iI , url in ii11i1 :
  iiiiiIIii ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 15 , i1111 + '3.png' , '' , '' )
  if 92 - 92: I11II1i . o0 + ooO0o0Oo
  if 28 - 28: i1IIi * i1II1I11 - ooO0o0Oo * OOoo0O0 * I11ii1 / i1I
def OooO0OoOOOO ( title , message , times = 2000 , icon = oOOoo00O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def i1Ii ( ) :
 o00OO00OoO = OOOO0OOoO0O0 ( )
 O0Oo000ooO00 = o00OO00OoO . replace ( O0O , "" )
 if os . path . exists ( o00OO00OoO ) or not o00OO00OoO == False :
  oO0 = open ( o00OO00OoO , mode = 'r' ) ; Ii1iIiII1ii1 = oO0 . read ( ) ; oO0 . close ( )
  ooOooo000oOO ( "%s - %s" % ( Iii1ii1II11i , O0Oo000ooO00 ) , Ii1iIiII1ii1 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OOOO0OOoO0O0 ( ) :
 Oo0oOOo = False
 if os . path . exists ( os . path . join ( O0O , 'xbmc.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( O0O , 'kodi.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( O0O , 'spmc.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( O0O , 'tvmc.log' ) ) :
  Oo0oOOo = os . path . join ( O0O , 'tvmc.log' )
 return Oo0oOOo
 if 58 - 58: iIiIiIiIIi * O0o * Oo00OOOOO / O0o
 if 75 - 75: O0O00o0OOO0
 if 50 - 50: I11ii1 / i1II1I11 - O0O00o0OOO0 - o0 % I11II1i - O0O00o0OOO0
 if 91 - 91: i1I / o0 - iIiIiIiIIi . o0
 if 18 - 18: ooO0o0Oo
def ooOooo000oOO ( heading , announce ) :
 class O0o0O00Oo0o0 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : oO0 = open ( announce ) ; O00O0oOO00O00 = oO0 . read ( )
   except : O00O0oOO00O00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00O0oOO00O00 ) )
   return
 O0o0O00Oo0o0 ( )
 O0o0O00Oo0o0 ( )
 if 11 - 11: OOoo0O0 . Oo00OOOOO
 if 92 - 92: I11II1i . Ii
def i1i ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 iiI111I1iIiI = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + o0oO0 + '%26password%3D' + Oo0oO0ooo + '%26type%3Dm3u_plus%26output%3Dts'
 II = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + o0oO0 + '%26password%3D' + Oo0oO0ooo
 Ii1I1IIii1II = 'http://piesustv.net:8000/enigma2.php?username=' + o0oO0 + '&password=' + Oo0oO0ooo + '&type=get_vod_categories'
 Ii1I1IIii1II = Ooo0OO0oOO ( Ii1I1IIii1II )
 if not Ii1I1IIii1II == "" :
  O0ii1ii1ii = 'https://tinyurl.com/create.php?source=indexpage&url=' + iiI111I1iIiI + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( O0ii1ii1ii ) )
  oooooOoo0ooo = 'https://tinyurl.com/create.php?source=indexpage&url=' + II + '&submit=Make+TinyURL%21&alias='
  iiI111I1iIiI = Ooo0OO0oOO ( O0ii1ii1ii )
  II = Ooo0OO0oOO ( oooooOoo0ooo )
  xbmc . log ( str ( II ) )
  I1I1IiI1 = III1iII1I1ii ( iiI111I1iIiI , '<div class="indent"><b>' , '</b>' )
  oOOo0 = III1iII1I1ii ( II , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLORsteelblue]WaveTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % I1I1IiI1 , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % oOOo0 )
 else :
  return
def oo00O00oO ( ) :
 iiiiiIIii ( '[COLORsteelblue]Setup Tv Guide[/COLOR]' , '' , 212 , i1111 + '12.png' , oooOOOOO , '' )
 iiiiiIIii ( '[COLORsteelblue]Open Guide[/COLOR]' , '' , 213 , i1111 + '13.png' , oooOOOOO , '' )
 if 23 - 23: i1I + i1I . O0o
def ii1ii11IIIiiI ( ) :
 ivuesetup . iVueInt ( )
 if 67 - 67: o0 * O0O00o0OOO0 * Oo00OOOOO + O0o / i1IIi
def I1I111 ( ) :
 Oo00oo0oO ( )
 return
 if 1 - 1: i1I - O0O00o0OOO0 . o0 . i1I / i1II1I11 + o0
def Oo00oo0oO ( ) :
 if 78 - 78: O0 . O0O00o0OOO0 . iIiIiIiIIi % O0o
 i1iIi = xbmcaddon . Addon ( 'plugin.video.WaveTv' )
 ooOOoooooo = i1iIi . getSetting ( id = 'User' )
 II1I = i1iIi . getSetting ( id = 'Pass' )
 O0i1II1Iiii1I11 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 IIII = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 iiIiI = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 o00oooO0Oo = "http://piesustv.net:8000/get.php?username=" + ooOOoooooo + "&password=" + II1I + "&type=m3u_plus&output=ts"
 o0O0OOO0Ooo = "http://piesustv.net:8000/xmltv.php?username=" + ooOOoooooo + "&password=" + II1I + "&type=m3u_plus&output=ts"
 if 45 - 45: O0 / ooO0o0Oo
 xbmc . executeJSONRPC ( O0i1II1Iiii1I11 )
 xbmc . executeJSONRPC ( IIII )
 xbmc . executeJSONRPC ( iiIiI )
 if 32 - 32: I11II1i . OOoo0O0 . OOoo0O0
 OO00O0O = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 OO00O0O . setSetting ( id = 'm3uUrl' , value = o00oooO0Oo )
 OO00O0O . setSetting ( id = 'epgUrl' , value = o0O0OOO0Ooo )
 OO00O0O . setSetting ( id = 'm3uCache' , value = "false" )
 OO00O0O . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def iii ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 if 90 - 90: ooO0o0Oo % i1IIi / i1I
def IIi ( data ) :
 i1Iii1i1I = len ( data ) % 4
 if 91 - 91: Oo00OOOOO + ooOoo0O . O0o * Oo00OOOOO + ooOoo0O * i1II1I11
 if 80 - 80: I11II1i % O0o % O0O00o0OOO0 - i1II1I11 + i1II1I11
 if 19 - 19: OO0o * i1IIi
 if 14 - 14: I11II1i
 if 11 - 11: OOoo0O0 * ooOoo0O . iIii1I11I1II1 % OoooooooOO + I11II1i
 if 78 - 78: i1I . O0o + i1I / o0 / i1I
 if i1Iii1i1I != 0 :
  data += b'=' * ( 4 - i1Iii1i1I )
 return base64 . decodestring ( data )
oO0O00OoOO0 = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s' % ( o0oO0 , Oo0oO0ooo )
OoO = Oo0o0000o0o0 + 'movie/%s/%s/' % ( o0oO0 , Oo0oO0ooo )
O00 = Oo0o0000o0o0 + 'live/%s/%s/' % ( o0oO0 , Oo0oO0ooo )
I1iI1 = '&action=get_live_categories'
iiiIi1 = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( o0oO0 , Oo0oO0ooo )
i1I1ii11i1Iii = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s&action=get_vod_categories' % ( o0oO0 , Oo0oO0ooo )
I1IiiiiI = Oo0o0000o0o0 + 'enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( o0oO0 , Oo0oO0ooo )
o0O = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( o0oO0 , Oo0oO0ooo )
IiIIii1iII1II = Oo0o0000o0o0 + 'enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=' % ( o0oO0 , Oo0oO0ooo )
Iii1I1I11iiI1 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( o0oO0 , Oo0oO0ooo )
if 18 - 18: O0o + I11II1i - I11ii1 . iIiIiIiIIi + i11iIiiIii
def iI1Ii1iI11iiI ( ) :
 o00oooO0Oo = "http://piesustv.net:8000//get.php?username=" + o0oO0 + "&password=" + Oo0oO0ooo + "&type=m3u_plus&output=ts"
 try :
  OO0OO0O00oO0 = urllib2 . urlopen ( o00oooO0Oo )
  print OO0OO0O00oO0 . getcode ( )
  OO0OO0O00oO0 . close ( )
  if 55 - 55: O0o . ooOoo0O
  pass
  if 61 - 61: i1II1I11 % OOoo0O0 . i1II1I11
 except urllib2 . HTTPError , o0oOO000oO0oo :
  print o0oOO000oO0oo . getcode ( )
  Dialog . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + TEXTCOL + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + TEXTCOL + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def oOO00O ( ) :
 iI1Ii1iI11iiI ( )
 open = Ooo0OO0oOO ( Iii1I1I11iiI1 )
 OOOoo0OO = oO0o0 ( open , '<channel>' , '</channel>' )
 for iI1Ii11iIiI1 in OOOoo0OO :
  i1I1iI = III1iII1I1ii ( iI1Ii11iIiI1 , '<title>' , '</title>' )
  i1I1iI = base64 . b64decode ( i1I1iI )
  OO0Oooo0oOO0O = III1iII1I1ii ( iI1Ii11iIiI1 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  IIiiiiiiIi1I1 ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , OO0Oooo0oOO0O , 14 , i1111 + 'GTV.png' , oooOOOOO , '' )
def o00O0 ( url ) :
 open = Ooo0OO0oOO ( IiIIii1iII1II + url )
 OOOoo0OO = oO0o0 ( open , '<channel>' , '</channel>' )
 for iI1Ii11iIiI1 in OOOoo0OO :
  i1I1iI = III1iII1I1ii ( iI1Ii11iIiI1 , '<title>' , '</title>' )
  i1I1iI = base64 . b64decode ( i1I1iI )
  xbmc . log ( str ( i1I1iI ) )
  oOO0O00Oo0O0o = III1iII1I1ii ( iI1Ii11iIiI1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OO0Oooo0oOO0O = III1iII1I1ii ( iI1Ii11iIiI1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  ii1 = III1iII1I1ii ( iI1Ii11iIiI1 , '<description>' , '</description>' )
  ii1 = base64 . b64decode ( ii1 )
  I1iIIiiIIi1i = '('
  O0O0ooOOO = ')'
  iiiiiIIii ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , OO0Oooo0oOO0O , 15 , oOO0O00Oo0O0o , oOOo0O00o , ( '[COLORsteelblue]' + ii1 + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( O0O0ooOOO , '[COLORsteelblue]' ) . replace ( I1iIIiiIIi1i , '[COLORorangered]' ) )
  if 8 - 8: i1I
def ii1111iII ( url ) :
 url = url
 iiiiI = Ooo0OO0oOO ( iiiIi1 + url )
 ii11i1 = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( iiiiI )
 for i1I1iI , type , oooOo0OOOoo0 , OOoO in ii11i1 :
  OO0O000 = ( O00 + oooOo0OOOoo0 + '.m3u8' ) . strip ( )
  iiiiiIIii ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , OO0O000 , 15 , ( OOoO ) . replace ( '\/' , '/' ) + 'jpg' , oooOOOOO , type )
  iiIiI1i1 ( 'tvshows' , 'Media Info 3' )
  if 69 - 69: I1I
  if 40 - 40: Ii + OoooooooOO % ooO0o0Oo - iIii1I11I1II1 . ooOoo0O
def iIiIi11iI ( ) :
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , oO0O00OoOO0 + '&action=get_vod_streams' , 41 , i1111 + '9.png' , oooOOOOO , '' )
 iiiiI = Ooo0OO0oOO ( i1I1ii11i1Iii )
 ii11i1 = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( iiiiI )
 for IIIii1II1II , i1I1iI in ii11i1 :
  IIiiiiiiIi1I1 ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIIii1II1II , 41 , i1111 + '9.png' , oooOOOOO , '' )
def Oo0O00O000 ( url ) :
 open = Ooo0OO0oOO ( I1IiiiiI + url )
 OOOoo0OO = oO0o0 ( open , '<channel>' , '</channel>' )
 for iI1Ii11iIiI1 in OOOoo0OO :
  if '<playlist_url>' in open :
   i1I1iI = III1iII1I1ii ( iI1Ii11iIiI1 , '<title>' , '</title>' )
   OO0Oooo0oOO0O = III1iII1I1ii ( iI1Ii11iIiI1 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   iiiiiIIii ( str ( base64 . b64decode ( i1I1iI ) ) . replace ( '?' , '' ) , OO0Oooo0oOO0O , 3 , icon , oOOo0O00o , '' )
  else :
   i1I1iI = III1iII1I1ii ( iI1Ii11iIiI1 , '<title>' , '</title>' )
   i1I1iI = base64 . b64decode ( i1I1iI )
   oOO0O00Oo0O0o = III1iII1I1ii ( iI1Ii11iIiI1 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = III1iII1I1ii ( iI1Ii11iIiI1 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   ii1 = III1iII1I1ii ( iI1Ii11iIiI1 , '<description>' , '</description>' )
   ii1 = base64 . b64decode ( ii1 )
   i11I1IiII1i1i = III1iII1I1ii ( ii1 , 'PLOT:' , '\n' )
   ooI1111i = III1iII1I1ii ( ii1 , 'CAST:' , '\n' )
   iIIii = III1iII1I1ii ( ii1 , 'RATING:' , '\n' )
   o00O0O = III1iII1I1ii ( ii1 , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   o00O0O = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( o00O0O )
   ii1iii1i = III1iII1I1ii ( ii1 , 'DURATION_SECS:' , '\n' )
   Iii1I1111ii = III1iII1I1ii ( ii1 , 'GENRE:' , '\n' )
   ooOoO00 ( str ( i1I1iI ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 15 , oOO0O00Oo0O0o , oOOo0O00o , i11I1IiII1i1i , str ( o00O0O ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( ooI1111i ) . split ( ) , iIIii , ii1iii1i , Iii1I1111ii )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 14 - 14: i1IIi - ooO0o0Oo % O0 - i1I
def ooO0O00Oo0o ( ) :
 OOO = Ooo0OO0oOO ( oO0O00OoOO0 )
 ii11i1 = re . compile ( '"username":"([^"]*)"' ) . findall ( OOO )
 Oo0o00OO0000 = re . compile ( '"password":"([^"]*)"' ) . findall ( OOO )
 I1i = re . compile ( '"status":"([^"]*)"' ) . findall ( OOO )
 O00Oooo = re . compile ( '"exp_date":"([^"]*)"' ) . findall ( OOO )
 i11I = re . compile ( '"active_cons":"([^"]*)"' ) . findall ( OOO )
 o00Oo0oooooo = re . compile ( '"created_at":"([^"]*)"' ) . findall ( OOO )
 O0oO0 = re . compile ( '"max_connections":"([^"]*)"' ) . findall ( OOO )
 iII11 = re . compile ( '"is_trial":"1"' ) . findall ( OOO )
 iiIiii1IIIII = re . compile ( '"is_trial":"0"' ) . findall ( OOO )
 o00o = re . compile ( '"timezone":"([^"]*)"' ) . findall ( OOO )
 IIIIiiIiiI = re . compile ( '"time_now":"([^"]*)"' ) . findall ( OOO )
 for IIIii1II1II in ii11i1 :
  iiiiiIIii ( '[COLORsteelblue]My Account Information[/COLOR]' , '' , '' , i1111 + '7.png' , '' , '' )
  iiiiiIIii ( '[COLORsteelblue]Username:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in Oo0o00OO0000 :
  iiiiiIIii ( '[COLORsteelblue]Password:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in I1i :
  iiiiiIIii ( '[COLORsteelblue]Status:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in o00Oo0oooooo :
  IIIIiI11I11 = datetime . fromtimestamp ( float ( o00Oo0oooooo [ 0 ] ) )
  IIIIiI11I11 . strftime ( '%Y-%m-%d %H:%M:%S' )
  iiiiiIIii ( '[COLORsteelblue]Created:[/COLOR]  %s' % ( IIIIiI11I11 ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in O00Oooo :
  IIIIiI11I11 = datetime . fromtimestamp ( float ( O00Oooo [ 0 ] ) )
  IIIIiI11I11 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= IIIIiI11I11 <= I11i + timedelta ( hours = 24 ) :
   iiiiiIIii ( '[COLORred]Expires Today[/COLOR]' , '' , '' , i1111 + '7.png' , '' , '' )
  iiiiiIIii ( '[COLORsteelblue]Expires:[/COLOR]  %s' % ( IIIIiI11I11 ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in i11I :
  iiiiiIIii ( '[COLORsteelblue]Active Connection:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in O0oO0 :
  iiiiiIIii ( '[COLORsteelblue]Max Connection:[/COLOR]  %s' % ( IIIii1II1II ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in iII11 :
  iiiiiIIii ( '[COLORsteelblue]Trial:[/COLOR] Yes' , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in iiIiii1IIIII :
  iiiiiIIii ( '[COLORsteelblue]Trial:[/COLOR] No' , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in o00o :
  iiiiiIIii ( '[COLORsteelblue]Timezone:[/COLOR] %s' % ( IIIii1II1II ) . replace ( '\/' , '/' ) , '' , '' , i1111 + '7.png' , '' , '' )
 for IIIii1II1II in IIIIiiIiiI :
  iiiiiIIii ( '[COLORsteelblue]Time Now:[/COLOR] %s' % ( IIIii1II1II ) , '' , '' , i1111 + '7.png' , '' , '' )
 iiiiiIIii ( '[COLORsteelblue]Sign up[/COLOR]' , '' , 50006 , '' , '' , '' )
def oo00o0 ( ) :
 OOO = Ooo0OO0oOO ( Oo0o0000o0o0 + 'panel_api.php?username=' + o0oO0 + '&password=' + Oo0oO0ooo )
 ii11i1 = re . compile ( '"exp_date":"(.+?)"' ) . findall ( OOO )
 for IIIii1II1II in ii11i1 :
  IIIIiI11I11 = datetime . fromtimestamp ( float ( ii11i1 [ 0 ] ) )
  IIIIiI11I11 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= IIIIiI11I11 <= I11i + timedelta ( hours = 24 ) :
   O0OoO000O0OO . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLORsteelblue]If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLORsteelblue]Please Visit [COLORred]' + oOo0oooo00o + '[COLORsteelblue] To Purchase A licence[/COLOR]' )
   if 4 - 4: I11ii1 % O0O00o0OOO0 * i1I
def o0O0OOOOoOO0 ( ) :
 iiiiI = Ooo0OO0oOO ( oO0O00OoOO0 + '&action=get_simple_data_table&stream_id=1309' )
 ii11i1 = re . compile ( '"id":"([^"]*)","epg_id":"([^"]*)","title":"([^"]*)","lang":"([^"]*)","start":"([^"]*)","end":"([^"]*)","description":"([^"]*)","channel_id":"([^"]*)"' , re . DOTALL ) . findall ( iiiiI )
 for id , II , ii , O0oOo00o , o0ooooO0o0O , iiIi11iI1iii , ii1 , oo000 in ii11i1 :
  iiiiiIIii ( '[COLORsteelblue]' + oo000 + ' - ' + o0OoOoOO00 ( ii ) + ' - ' + O0oOo00o + '[/COLOR]' , id , 31 , i1111 + '0.png' , oooOOOOO , o0ooooO0o0O + '[CR]' + iiIi11iI1iii + '[CR]' + o0OoOoOO00 ( ii1 ) )
def o0000oO ( url ) :
 url = OoO + id + '.mp4'
 iI1i111I1Ii ( url )
def i11i1ii1I ( url ) :
 IIiiiiiiIi1I1 ( '*[COLORsteelblue]Search[/COLOR]*' , url , 4 , i1111 + '2.png' , i1111 + '2.png' , 'Search Movies' )
 iiiiI = Ooo0OO0oOO ( url )
 ii11i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iiiiI )
 for url , o0OO0o0o00o , ii1 , oOo0 , i1I1iI in ii11i1 :
  if 'php' in url :
   IIiiiiiiIi1I1 ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 21 , i1111 + '2.png' , i1111 + '2.png' , ii1 )
  else :
   iiiiiIIii ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , url , 15 , o0OO0o0o00o , oOo0 , ii1 )
   xbmcplugin . addSortMethod ( iI111I11I1I1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOoOO ( url ) :
 iiiiI = Ooo0OO0oOO ( url )
 ii11i1 = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iiiiI )
 for o0OO0o0o00o , i1I1iI , url in ii11i1 :
  url = ( ( o0OoOoOO00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o0oO0 + '/' + Oo0oO0ooo + url ) . strip ( )
  iiiiiIIii ( ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(ULTIMATE ONLY)' , ' ' ) , url , 15 , o0OO0o0o00o , oOOo0O00o , '' )
  if 10 - 10: I11II1i + i1II1I11 * Oo00OOOOO + iIii1I11I1II1 / Ii / Oo00OOOOO
  if 42 - 42: ooOoo0O
def II1i11I ( ) :
 iiiiiIIii ( '[COLORsteelblue]Delete Packages[/COLOR]' , '' , 6 , i1111 + 'standard.png' , oooOOOOO , '' )
 iiiiiIIii ( '[COLORsteelblue]Delete Cache[/COLOR]' , '' , 7 , i1111 + 'standard.png' , oooOOOOO , '' )
 iiiiiIIii ( '[COLORsteelblue]View Log File[/COLOR]' , '' , 50000 , i1111 + 'standard.png' , oooOOOOO , '' )
 iiiiiIIii ( '[COLORsteelblue]Force Refresh[/COLOR]' , '' , 50001 , i1111 + 'standard.png' , oooOOOOO , '' )
 iiiiiIIii ( '[COLORsteelblue]Force Close[/COLOR]' , '' , 8 , i1111 + 'standard.png' , oooOOOOO , '' )
 if 50 - 50: OoooooooOO % o0
 if 49 - 49: O0O00o0OOO0 - i11iIiiIii . Ii * I11ii1 % I11II1i + i1IIi
 if 71 - 71: ooO0o0Oo
def IIIIiIiIi1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def I11iiiiI1i ( url ) :
 if url == 'http://' : return False
 try :
  iI1i11 = urllib2 . Request ( url )
  iI1i11 . add_header ( 'User-Agent' , I1IiI )
  OoOOoooOO0O = urllib2 . urlopen ( iI1i11 )
  OoOOoooOO0O . close ( )
 except Exception , o0oOO000oO0oo :
  return o0oOO000oO0oo
 return True
def ooo00Ooo ( ) :
 OOO = Ooo0OO0oOO ( I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 ii11i1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOO )
 for i1I1iI , IIIii1II1II , OOoO , oOOo0O00o , Oo0o0O00 in ii11i1 :
  iiiiiIIii ( i1I1iI , IIIii1II1II , 60002 , OOoO , i1111 + 'a.png' , Oo0o0O00 )
  if 40 - 40: OoooooooOO
def I1i1i1 ( name , url ) :
 if IIIIiIiIi1 ( ) == 'android' :
  OoO0O00O0oo0O = O0OoO000O0OO . yesno ( Iii1ii1II11i , "Would you like to download and install:" , "%s" % name )
  if not OoO0O00O0oo0O : OooO0OoOOOO ( Iii1ii1II11i , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I1IiI11 = name
  if OoO0O00O0oo0O :
   if not os . path . exists ( iiIIIII1i1iI ) : os . makedirs ( iiIIIII1i1iI )
   if not I11iiiiI1i ( url ) == True : OooO0OoOOOO ( Iii1ii1II11i , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iIiiiI . create ( Iii1ii1II11i , 'Downloading %s' % I1IiI11 , '' , 'Please Wait' )
   iI1iiiiIii = os . path . join ( iiIIIII1i1iI , "%s.apk" % name )
   try : os . remove ( iI1iiiiIii )
   except : pass
   downloader . download ( url , iI1iiiiIii , iIiiiI )
   xbmc . sleep ( 500 )
   iIiiiI . close ( )
   O0OoO000O0OO . ok ( Iii1ii1II11i , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + iI1iiiiIii + '")' )
  else : OooO0OoOOOO ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OooO0OoOOOO ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 19 - 19: i1I - i1II1I11 . O0
 if 60 - 60: iIiIiIiIIi + i1II1I11
 if 9 - 9: I1I * OoooooooOO - iIii1I11I1II1 + OO0o / i1I . i1I
def iiIIi ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iiI1iI111ii1i = xbmcgui . Dialog ( )
 iiI1iI111ii1i . ok ( "Wave Tv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Wave Tv[/COLOR]" )
 return
 if 32 - 32: iIiIiIiIIi * OO0o % i1IIi - I11II1i + iIii1I11I1II1 + Oo00OOOOO
def OO0O0Oo000 ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING Addons20.db ###'
 iiI11i1II = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 OO0O0OOo0O = os . path . join ( iiI11i1II , 'Addons20.db' )
 try :
  os . remove ( OO0O0OOo0O )
  iiI1iI111ii1i = xbmcgui . Dialog ( )
  print '=== ' + Iii1ii1II11i + ' - DELETING    ' + str ( OO0O0OOo0O ) + '    ==='
  iiI1iI111ii1i . ok ( Iii1ii1II11i , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  iiI1iI111ii1i = xbmcgui . Dialog ( )
  iiI1iI111ii1i . ok ( Iii1ii1II11i , "       No File To Remove" )
 return
 if 36 - 36: I1I . i1II1I11 % I1I % i1I
 if 2 - 2: ooO0o0Oo - Oo00OOOOO
 if 58 - 58: I11ii1 + ooO0o0Oo - ooOoo0O
 if 3 - 3: i1I
def ooooooO0oo ( ) :
 if Oo0oO0ooo == 'insert_password' :
  O0OoO000O0OO . ok ( '[COLORsteelblue]Wave Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]Wave Tv Media[/COLOR]' )
  I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
 else :
  oo00o0 ( )
  if 97 - 97: Ii
def Ooo0OO0oOO ( url ) :
 iI1i11 = urllib2 . Request ( url )
 iI1i11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OoOOoooOO0O = urllib2 . urlopen ( iI1i11 )
 OOO = OoOOoooOO0O . read ( )
 OoOOoooOO0O . close ( )
 return OOO
def iiIII1i ( ) :
 IIIii1II1II = oO0o0o0ooO0oO
 I1IooooO0oOoOOoO = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11i = I1IooooO0oOoOOoO . lower ( )
 iiiiI = Ooo0OO0oOO ( IIIii1II1II )
 IiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iiiiI )
 for IIIii1II1II , o0OO0o0o00o , ii1 , oOo0 , i1I1iI in IiIi :
  if I1i11i in i1I1iI . lower ( ) :
   iiiiiIIii ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 15 , o0OO0o0o00o , oOo0 , ii1 )
   iIiiiI . create ( '[COLORsteelblue]' + Iii1ii1II11i + '[/COLOR]' , "Checking Library" , '' , 'Please Wait' )
   iIiiiI . update ( 53 , "" , "Getting Movie Links" )
   if 87 - 87: Oo00OOOOO - Oo00OOOOO - I11II1i + O0O00o0OOO0
  iiIiI1i1 ( 'tvshows' , 'Media Info 3' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
def ooOooo000oOO ( heading , announce ) :
 class O0o0O00Oo0o0 ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : oO0 = open ( announce ) ; O00O0oOO00O00 = oO0 . read ( )
   except : O00O0oOO00O00 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00O0oOO00O00 ) )
   return
 O0o0O00Oo0o0 ( )
 O0o0O00Oo0o0 ( )
 if 82 - 82: O0O00o0OOO0 / iIii1I11I1II1 . ooOoo0O . O0o / ooO0o0Oo
def iiI1I1 ( ) :
 OOO = Ooo0OO0oOO ( i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ii11i1 = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO )
 for i1I1iI , IIIii1II1II , ooO , oOOo0O00o , iiOO0O0Ooo in ii11i1 :
  iiiiiIIii ( '[COLORsteelblue]' + i1I1iI + '[/COLOR]' , IIIii1II1II , 20 , ooO , oOOo0O00o , iiOO0O0Ooo )
 iiIiI1i1 ( 'movies' , 'MAIN' )
def oOoO0 ( url ) :
 iiI11i1II = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( "Wave Tv" , "Downloading Files" , '' , 'Please Wait' )
 iI1iiiiIii = os . path . join ( iiI11i1II , 'plugin.video.WaveTv' + '.zip' )
 try :
  os . remove ( iI1iiiiIii )
 except :
  pass
 downloader . download ( url , iI1iiiiIii , iIiiiI )
 Oo0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iIiiiI . update ( 0 , "" , "Wave Tv Is Now Installing Files Please Wait" )
 print '======================================='
 print Oo0
 print '======================================='
 extract . all ( iI1iiiiIii , Oo0 , iIiiiI )
 oo0O0o00o0O ( url )
 iiI1iI111ii1i = xbmcgui . Dialog ( )
 iiI1iI111ii1i . ok ( "Wave Tv" , "Press ok to force close Wave Tv, If unsuccessful Please press home button got to settings/apps and force close Wave Tv and clear cache. " , "[COLOR yellow]Brought To You By Wave Tv[/COLOR]" )
 I11i1II ( )
def oo0O0o00o0O ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiIi1i , I1i11111i1i11 , OOoOOO0 in os . walk ( Ooo ) :
   I1I1i = 0
   I1I1i += len ( OOoOOO0 )
   if 1 - 1: o0 % O0o + O0 + i1IIi - i1I
   if 22 - 22: ooOoo0O % Oo00OOOOO
   if I1I1i > 0 :
    if 57 - 57: O0o + O0 . I11ii1
    iiI1iI111ii1i = xbmcgui . Dialog ( )
    if iiI1iI111ii1i . yesno ( "Delete Package Cache Files" , str ( I1I1i ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: OOoo0O0
     for oO0 in OOoOOO0 :
      os . unlink ( os . path . join ( iiIi1i , oO0 ) )
     for ii1iIi1iIiI1i in I1i11111i1i11 :
      shutil . rmtree ( os . path . join ( iiIi1i , ii1iIi1iIiI1i ) )
     iiI1iI111ii1i = xbmcgui . Dialog ( )
     iiI1iI111ii1i . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    iiI1iI111ii1i = xbmcgui . Dialog ( )
    iiI1iI111ii1i . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  iiI1iI111ii1i = xbmcgui . Dialog ( )
  iiI1iI111ii1i . ok ( Iii1ii1II11i , "Error Deleting Packages please visit The Support Group, Wave Tv on facebook" )
 iiI1iIii1i ( url )
 return
def iiI1iIii1i ( url ) :
 OOooO0oo0o00o = os . path . join ( iI1Ii11111iIi , 'addon_data' )
 ooOO0OoO = [
 ( OOooO0oo0o00o ) ,
 ( I1i1iiI1 ) ,
 ( os . path . join ( IiII , 'cache' ) ) ,
 ( os . path . join ( IiII , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'plugin.video.WaveTv' , 'Images' ) ) ,
 ( os . path . join ( OOooO0oo0o00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OOooO0oo0o00o , 'plugin.video.WaveTv' , 'Images' ) ) ]
 if 69 - 69: iIii1I11I1II1 . Oo00OOOOO % I1I + iIii1I11I1II1 / O0 / Oo00OOOOO
 O00OoOO0oo0 = 0
 if 96 - 96: OO0o . ooO0o0Oo - I1I
 for O0OI11iiiii1II in ooOO0OoO :
  if os . path . exists ( O0OI11iiiii1II ) and not O0OI11iiiii1II in [ I1i1iiI1 , OOooO0oo0o00o ] :
   for iiIi1i , I1i11111i1i11 , OOoOOO0 in os . walk ( O0OI11iiiii1II ) :
    I1I1i = 0
    I1I1i += len ( OOoOOO0 )
    if I1I1i > 0 :
     for oO0 in OOoOOO0 :
      if not oO0 in i1i1II :
       try :
        os . unlink ( os . path . join ( iiIi1i , oO0 ) )
       except :
        pass
      else : o00OO00OoO ( 'Ignore Log File: %s' % oO0 )
     for ii1iIi1iIiI1i in I1i11111i1i11 :
      try :
       shutil . rmtree ( os . path . join ( iiIi1i , ii1iIi1iIiI1i ) )
       O00OoOO0oo0 += 1
       o00OO00OoO ( "[Success] cleared %s files from %s" % ( str ( I1I1i ) , os . path . join ( O0OI11iiiii1II , ii1iIi1iIiI1i ) ) )
      except :
       o00OO00OoO ( "[Failed] to wipe cache in: %s" % os . path . join ( O0OI11iiiii1II , ii1iIi1iIiI1i ) )
  else :
   for iiIi1i , I1i11111i1i11 , OOoOOO0 in os . walk ( O0OI11iiiii1II ) :
    for ii1iIi1iIiI1i in I1i11111i1i11 :
     if 'cache' in ii1iIi1iIiI1i . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iiIi1i , ii1iIi1iIiI1i ) )
       O00OoOO0oo0 += 1
       o00OO00OoO ( "[Success] wiped %s " % os . path . join ( O0OI11iiiii1II , ii1iIi1iIiI1i ) )
      except :
       o00OO00OoO ( "[Failed] to wipe cache in: %s" % os . path . join ( O0OI11iiiii1II , ii1iIi1iIiI1i ) )
       if 51 - 51: O0 % O0O00o0OOO0 - iIiIiIiIIi
 OooO0OoOOOO ( Iii1ii1II11i , 'Clear Cache: Removed %s Files' % O00OoOO0oo0 )
def I1II ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiIi1i , I1i11111i1i11 , OOoOOO0 in os . walk ( Ooo ) :
   I1I1i = 0
   I1I1i += len ( OOoOOO0 )
   if 64 - 64: O0 % o0 % O0 * i1I . O0O00o0OOO0 + ooOoo0O
   if 75 - 75: o0 . OoooooooOO % ooO0o0Oo * o0 % OoooooooOO
   if I1I1i > 0 :
    if 13 - 13: OOoo0O0 / i11iIiiIii % iIiIiIiIIi % o0 . Oo00OOOOO
    iiI1iI111ii1i = xbmcgui . Dialog ( )
    if iiI1iI111ii1i . yesno ( "Delete Package Cache Files" , str ( I1I1i ) + " files found" , "Do you want to delete them?" ) :
     if 8 - 8: OO0o + i1II1I11 - iIiIiIiIIi
     for oO0 in OOoOOO0 :
      os . unlink ( os . path . join ( iiIi1i , oO0 ) )
     for ii1iIi1iIiI1i in I1i11111i1i11 :
      shutil . rmtree ( os . path . join ( iiIi1i , ii1iIi1iIiI1i ) )
     iiI1iI111ii1i = xbmcgui . Dialog ( )
     iiI1iI111ii1i . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    iiI1iI111ii1i = xbmcgui . Dialog ( )
    iiI1iI111ii1i . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  iiI1iI111ii1i = xbmcgui . Dialog ( )
  iiI1iI111ii1i . ok ( Iii1ii1II11i , "Error Deleting Packages" )
 return
 if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OO0o
def I11i1II ( ) :
 iiI1iI111ii1i = xbmcgui . Dialog ( )
 i1I11IiI1iiII = iiI1iI111ii1i . yesno ( 'Force Close Wave Tv' , 'You are about to close Wave Tv' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i1I11IiI1iiII == 0 : return
 elif i1I11IiI1iiII == 1 : pass
 o00oOo0oOoo = IIIIiIiIi1 ( )
 o00OO00OoO ( "Platform: " + str ( o00oOo0oOoo ) )
 os . _exit ( 1 )
 o00OO00OoO ( "Force close failed!  Trying alternate methods." )
 if o00oOo0oOoo == 'osx' :
  o00OO00OoO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iiI1iI111ii1i . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o00oOo0oOoo == 'linux' :
  o00OO00OoO ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iiI1iI111ii1i . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o00oOo0oOoo == 'android' :
  o00OO00OoO ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.Wave Tv' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.Wave Tv' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.Wave Tv());' )
  except : pass
  iiI1iI111ii1i . ok ( Iii1ii1II11i , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif o00oOo0oOoo == 'windows' :
  o00OO00OoO ( "############ try windows force close #################" )
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
  iiI1iI111ii1i . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  o00OO00OoO ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  o00OO00OoO ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iiI1iI111ii1i . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 57 - 57: OO0o - Oo00OOOOO
def iI1i111I1Ii ( url ) :
 import urlresolver
 try :
  I11iiI11 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( I11iiI11 , xbmcgui . ListItem ( i1I1iI ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( i1I1iI ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "WaveTv" , "unplayable stream" )
   sys . exit ( )
def IIIIiIiIi1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 96 - 96: O0o
def o00OO00OoO ( log ) :
 xbmc . log ( "[%s]: %s" % ( Iii1ii1II11i , log ) )
 if not os . path . exists ( I1i1iiI1 ) : os . makedirs ( I1i1iiI1 )
 if not os . path . exists ( o00 ) : oO0 = open ( o00 , 'w' ) ; oO0 . close ( )
 with open ( o00 , 'a' ) as oO0 :
  OOo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oO0 . write ( OOo . rstrip ( '\r\n' ) + '\n' )
  if 50 - 50: I1I
def o0O0O0ooo0oOO ( ) :
 try :
  oo000ii = getSet ( "core-player" )
  if ( oo000ii == 'DVDPLAYER' ) : OoOIiiiii111i1ii = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oo000ii == 'MPLAYER' ) : OoOIiiiii111i1ii = xbmc . PLAYER_CORE_MPLAYER
  elif ( oo000ii == 'PAPLAYER' ) : OoOIiiiii111i1ii = xbmc . PLAYER_CORE_PAPLAYER
  else : OoOIiiiii111i1ii = xbmc . PLAYER_CORE_AUTO
 except : OoOIiiiii111i1ii = xbmc . PLAYER_CORE_AUTO
 return OoOIiiiii111i1ii
 return True
 if 25 - 25: O0o - I1I / i11iIiiIii
def III1iII1I1ii ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : iiI1ii11i1 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : iiI1ii11i1 = ''
 else :
  try : iiI1ii11i1 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : iiI1ii11i1 = ''
 return iiI1ii11i1
 if 38 - 38: Oo00OOOOO - I11II1i / O0 . Ii
 if 45 - 45: Ii
def oO0o0 ( text , start_with , end_with ) :
 iiI1ii11i1 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return iiI1ii11i1
def oOIIi1iiii1iI ( ) :
 iIiiii = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 iIiiii . connect ( ( '8.8.8.8' , 0 ) )
 iIiiii = iIiiii . getsockname ( ) [ 0 ]
 return iIiiii
 if 89 - 89: I11II1i - I1I % i1II1I11 % ooO0o0Oo
def IIiii11i ( ) :
 open = Ooo0OO0oOO ( 'http://canyouseeme.org/' )
 O00oOo00o0o = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( O00oOo00o0o . group ( ) )
def IIiiiiiiIi1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 85 - 85: I11II1i + OoooooooOO * I11II1i - Ii % i11iIiiIii
 OOo00OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi1 = True
 i11iiI1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11iiI1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11iiI1111 . setProperty ( "Fanart_Image" , fanart )
 iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo00OoO , listitem = i11iiI1111 , isFolder = True )
 return iIi1
 if 97 - 97: i1II1I11 * ooOoo0O . iIii1I11I1II1
def iiiiiIIii ( name , url , mode , iconimage , fanart , description ) :
 if 16 - 16: I1I % OoooooooOO - O0o * I11ii1 * Oo00OOOOO / OoooooooOO
 OOo00OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi1 = True
 i11iiI1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11iiI1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i11iiI1111 . setProperty ( "Fanart_Image" , fanart )
 iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo00OoO , listitem = i11iiI1111 , isFolder = False )
 return iIi1
def ooOoO00 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 OOo00OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 iIi1 = True
 i11iiI1111 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 i11iiI1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 i11iiI1111 . setProperty ( 'fanart_image' , fanart )
 i11iiI1111 . setProperty ( "IsPlayable" , "true" )
 I11o0oO00oO0o0o0 = [ ]
 I11o0oO00oO0o0o0 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 I11o0oO00oO0o0o0 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i11iiI1111 . addContextMenuItems ( I11o0oO00oO0o0o0 , replaceItems = True )
 iIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOo00OoO , listitem = i11iiI1111 , isFolder = False )
def I1Iooooo ( ) :
 i11IIIiI1I = [ ]
 o0iiiI1I1iIIIi1 = sys . argv [ 2 ]
 if len ( o0iiiI1I1iIIIi1 ) >= 2 :
  Iii = sys . argv [ 2 ]
  I1iiiiI1iI = Iii . replace ( '?' , '' )
  if ( Iii [ len ( Iii ) - 1 ] == '/' ) :
   Iii = Iii [ 0 : len ( Iii ) - 2 ]
  iIiiiii1i = I1iiiiI1iI . split ( '&' )
  i11IIIiI1I = { }
  for iiIi1IIiI in range ( len ( iIiiiii1i ) ) :
   i1oO0OO0 = { }
   i1oO0OO0 = iIiiiii1i [ iiIi1IIiI ] . split ( '=' )
   if ( len ( i1oO0OO0 ) ) == 2 :
    i11IIIiI1I [ i1oO0OO0 [ 0 ] ] = i1oO0OO0 [ 1 ]
    if 82 - 82: OOoo0O0 - OOoo0O0 + OO0o
 return i11IIIiI1I
 if 8 - 8: ooO0o0Oo % I11II1i * O0O00o0OOO0 % I11ii1 . I1I / I1I
 if 81 - 81: i1I
Iii = I1Iooooo ( )
IIIii1II1II = None
i1I1iI = None
oO0o00oOOooO0 = None
ooO = None
oOOo0O00o = None
iiOO0O0Ooo = None
OOOoO000 = None
if 57 - 57: iIiIiIiIIi
if 54 - 54: i1II1I11 + O0O00o0OOO0 + i11iIiiIii
try :
 OOOoO000 = int ( Iii [ "fav_mode" ] )
except :
 pass
 if 28 - 28: O0O00o0OOO0
try :
 IIIii1II1II = urllib . unquote_plus ( Iii [ "url" ] )
except :
 pass
try :
 i1I1iI = urllib . unquote_plus ( Iii [ "name" ] )
except :
 pass
try :
 ooO = urllib . unquote_plus ( Iii [ "iconimage" ] )
except :
 pass
try :
 oO0o00oOOooO0 = int ( Iii [ "mode" ] )
except :
 pass
try :
 oOOo0O00o = urllib . unquote_plus ( Iii [ "fanart" ] )
except :
 pass
try :
 iiOO0O0Ooo = urllib . unquote_plus ( Iii [ "description" ] )
except :
 pass
 if 70 - 70: OOoo0O0
 if 34 - 34: Ii % OOoo0O0
print str ( i1iiIIiiI111 ) + ': ' + str ( i1iII1IiiIiI1 )
print "Mode: " + str ( oO0o00oOOooO0 )
print "URL: " + str ( IIIii1II1II )
print "Name: " + str ( i1I1iI )
print "IconImage: " + str ( ooO )
if 3 - 3: iIiIiIiIIi / O0o + OOoo0O0 . I1I . i1I
if 83 - 83: O0O00o0OOO0 + OoooooooOO
def iiIiI1i1 ( content , viewType ) :
 if 22 - 22: I11ii1 % I11II1i * OoooooooOO - ooO0o0Oo / iIii1I11I1II1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if I1ii11iIi11i . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % I1ii11iIi11i . getSetting ( viewType ) )
  if 86 - 86: OoooooooOO . I11II1i % OO0o / o0 * I11II1i / ooO0o0Oo
  if 64 - 64: i11iIiiIii
if oO0o00oOOooO0 == None : IIIII ( )
elif oO0o00oOOooO0 == 1 : Genres ( )
elif oO0o00oOOooO0 == 2 : Lists ( IIIii1II1II , ooO )
elif oO0o00oOOooO0 == 3 : all_mov ( )
elif oO0o00oOOooO0 == 4 : iiIII1i ( )
elif oO0o00oOOooO0 == 5 : II1i11I ( )
elif oO0o00oOOooO0 == 6 : I1II ( IIIii1II1II )
elif oO0o00oOOooO0 == 7 : iiI1iIii1i ( IIIii1II1II )
elif oO0o00oOOooO0 == 8 : I11i1II ( )
elif oO0o00oOOooO0 == 9 : OOO00 ( )
elif oO0o00oOOooO0 == 10 : ooO0O00Oo0o ( )
elif oO0o00oOOooO0 == 11 : TvGuide ( )
elif oO0o00oOOooO0 == 12 : ooooooO0oo ( )
elif oO0o00oOOooO0 == 13 : ReCreate_Addon_ini ( )
elif oO0o00oOOooO0 == 14 : o00O0 ( IIIii1II1II )
elif oO0o00oOOooO0 == 144 : ii1111iII ( IIIii1II1II )
elif oO0o00oOOooO0 == 15 : iI1i111I1Ii ( IIIii1II1II )
elif oO0o00oOOooO0 == 16 : oOO00O ( )
elif oO0o00oOOooO0 == 17 : Live_Events ( i1I1iI )
elif oO0o00oOOooO0 == 18 : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
elif oO0o00oOOooO0 == 19 : iiI1I1 ( )
elif oO0o00oOOooO0 == 20 : oOoO0 ( IIIii1II1II )
elif oO0o00oOOooO0 == 30 : o0O0OOOOoOO0 ( )
elif oO0o00oOOooO0 == 31 : o0000oO ( IIIii1II1II )
elif oO0o00oOOooO0 == 40 : iIiIi11iI ( )
elif oO0o00oOOooO0 == 41 : Oo0O00O000 ( IIIii1II1II )
elif oO0o00oOOooO0 == 21 : i11i1ii1I ( IIIii1II1II )
elif oO0o00oOOooO0 == 22 : OOOoOO ( IIIii1II1II )
elif oO0o00oOOooO0 == 50 : Oooo0Ooo000 ( )
elif oO0o00oOOooO0 == 51 : oo0OooOOo0 ( IIIii1II1II )
elif oO0o00oOOooO0 == 50000 : i1Ii ( )
elif oO0o00oOOooO0 == 50001 : iiIIi ( )
elif oO0o00oOOooO0 == 50002 : OO0O0Oo000 ( IIIii1II1II )
elif oO0o00oOOooO0 == 60001 : ooo00Ooo ( )
elif oO0o00oOOooO0 == 60002 : I1i1i1 ( i1I1iI , IIIii1II1II )
elif oO0o00oOOooO0 == 211 : oo00O00oO ( )
elif oO0o00oOOooO0 == 212 : I1I111 ( )
elif oO0o00oOOooO0 == 213 : iii ( )
elif oO0o00oOOooO0 == 214 : i1i ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
