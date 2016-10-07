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
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 'plugin.video.WaveTv'
IiII = 'plugin.video.WaveTv'
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = xbmcaddon . Addon ( id = IiII )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
IiII = 'plugin.video.WaveTv'
iiIIIII1i1iI = 'plugin.video.WaveTv'
o0oO0 = xbmcgui . DialogProgress ( )
oo00 = "Wave Tv"
o00 = Net ( )
Oo0oO0ooo = base64 . decodestring
o0oOoO00o = O0oo0OO0 . getSetting ( 'User' )
i1 = O0oo0OO0 . getSetting ( 'Pass' )
oOOoo00O0O = O0oo0OO0 . getSetting ( 'AdultPass' )
i1111 = xbmc . translatePath ( 'special://home/' )
i11 = ( Oo0oO0ooo ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
I11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII , 'icon.png' ) )
Oo0o0000o0o0 = i11 + ( Oo0oO0ooo ( 'R2VuaWVBcnQvd2F2ZS8=' ) )
oOo0oooo00o = "0.0.2"
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.WaveTv' )
oo0o0O00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.WaveTv/imports/tvGuide/ResetDatabase.py' ) )
oO = xbmc . translatePath ( 'special://thumbnails' ) ;
i1iiIIiiI111 = "Xhoans"
oooOOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII , 'fanart.jpg' ) )
i1iiIII111ii = base64 . decodestring ( 'LnBocA==' )
i1iIIi1 = O0oo0OO0 . getLocalizedString
ii11iIi1I = CookieJar ( )
iI111I11I1I1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( ii11iIi1I ) )
iI111I11I1I1 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
OOooO0OOoo = int ( sys . argv [ 1 ] )
iIii1 = xbmc . translatePath ( O0oo0OO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
oOOoO0 = xbmc . translatePath ( 'special://home/userdata/' )
O0OoO000O0OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
iiI1IiI = oO0o0o0ooO0oO + '/addons.ini'
II = xbmcgui . Dialog ( )
if 57 - 57: ooOoo0O
def OooO0 ( ) :
 II11iiii1Ii ( )
 OO0o ( '[COLORsteelblue]LOGIN[/COLOR]' , '' , 60000 , I11 , oooOOOOO , '' )
 if 82 - 82: i1I1i1Ii11 . IIIIII11i1I - o0o0OOO0o0 % O0 % i1IIi * OoOoOO00
 if 62 - 62: i1I1i1Ii11 . i1IIi / Ii1I
 Iii1i1I11I ( '[COLORsteelblue]Stream Lists[/COLOR]' , '' , 16 , Oo0o0000o0o0 + 'lists.png' , oooOOOOO , '' )
 if 50 - 50: i1IIi . I1IiiI % OoOoOO00 - OoO0O00 - I11i
 if 34 - 34: II111iiii / OoooooooOO . o0oOOo0O0Ooo . OoooooooOO % i1IIi
def II11iiii1Ii ( ) :
 if i1 == 'insert_password' :
  II . ok ( '[COLORsteelblue]Wave Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]http://wavemediapro.com[/COLOR]' )
  O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
 else :
  IIiiiiiiIi1I1 = open ( iiI1IiI , "r" )
  I1IIIii = re . compile ( 'plugin.video.WaveTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( IIiiiiiiIi1I1 ) )
  for oOoOooOo0o0 , OOOO in I1IIIii :
   if oOoOooOo0o0 == 'replace_user' or OOOO == 'replace_pass' :
    II . ok ( '[COLOR=yellow]Need to set login details' , 'You need to input your login details to activate streams' , '' )
    O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
    if 87 - 87: oO0o / I11i - i1IIi * OOooOOo / OoooooooOO . O0
    if 1 - 1: II111iiii - I11i / I11i
def I1II1III11iii ( ) :
 II11iiii1Ii ( )
 Iii1i1I11I ( 'Full List' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'PPV' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'Entertainment' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'Factual' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'Movie Channels' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'US Movie Channels TEST' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'Kids' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'Music' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'UK Sports' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'International Sports' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'News UK & International' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'German' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'Arabic' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'TV Series Latest' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'VOD Latest' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 Iii1i1I11I ( 'VOD Bollywood' , '' , 14 , Oo0o0000o0o0 + 'UltimateList.png' , oooOOOOO , '' )
 if 75 - 75: iIii1I11I1II1 / OOooOOo % o0oOOo0O0Ooo * OoOoOO00
 if 9 - 9: OoO0O00
def i11O0oo0OO0oOOOo ( name ) :
 i1i1i11IIi = name
 II1III = iI1iI1I1i1I ( Oo0oO0ooo ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 I1IIIii = re . compile ( '#EXTINF:-1 tvg-name="(.+?)" tvg-logo="(.+?)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II1III )
 for name , iIi11Ii1 , Ii11iII1 in I1IIIii :
  Ii11iII1 = ( Ii11iII1 ) . replace ( 'replace_user' , o0oOoO00o ) . replace ( 'replace_pass' , i1 )
  OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Ii11iII1 ) . strip ( ) , 15 , iIi11Ii1 , iIi11Ii1 , '' )
 else :
  OO0o ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 15 , '' , '' , '' )
  if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / o0o0OOO0o0
def iIIIIii1 ( ) :
 II . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + oo0o0O00 + ")" )
 oo000OO00Oo ( )
 II . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your Wave Tv streams' )
 if 51 - 51: i1I1i1Ii11 * o0oOOo0O0Ooo + I11i + OoO0O00
 if 66 - 66: OoOoOO00
def oO000Oo000 ( name ) :
 i1i1i11IIi = name
 II1III = iI1iI1I1i1I ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 I1IIIii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( II1III )
 for name , iIi11Ii1 , i111IiI1I , Ii11iII1 in I1IIIii :
  if i1i1i11IIi == 'Full List' :
   Ii11iII1 = ( Ii11iII1 ) . replace ( '.ts' , '.m3u8' )
   OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Ii11iII1 ) . strip ( ) , 15 , iIi11Ii1 , iIi11Ii1 , '' )
  else :
   i1i1i11IIi = ( i1i1i11IIi ) . replace ( 'World' , 'القنوات العربية' )
   if i1i1i11IIi in i111IiI1I :
    Ii11iII1 = ( Ii11iII1 ) . replace ( '.ts' , '.m3u8' )
    print Ii11iII1 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    OO0o ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Ii11iII1 ) . strip ( ) , 15 , iIi11Ii1 , iIi11Ii1 , '' )
   else :
    pass
def O0iII ( ) :
 oo000OO00Oo ( )
 try :
  o0 = gui . TVGuide ( )
  o0 . doModal ( )
  del o0
  if 62 - 62: iIii1I11I1II1 * OoOoOO00
 except :
  import sys
  import traceback as tb
  ( i1OOO , Oo0oOOo , traceback ) = sys . exc_info ( )
  tb . print_exception ( i1OOO , Oo0oOOo , traceback )
  if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
def iI1iI1I1i1I ( url ) :
 oO0o0OOOO = urllib2 . Request ( url )
 oO0o0OOOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0O0OoOO0 = urllib2 . urlopen ( oO0o0OOOO )
 iiiI1I11i1 = O0O0OoOO0 . read ( )
 O0O0OoOO0 . close ( )
 return iiiI1I11i1
 if 49 - 49: I1IiiI % o0o0OOO0o0 . o0o0OOO0o0 . I11i * o0o0OOO0o0
 if 97 - 97: Ii1I + o0oOOo0O0Ooo . OOooOOo + I1ii11iIi11i % ooOoo0O
 if 95 - 95: i1IIi
def oo000OO00Oo ( ) :
 I1ii11iI = os . path . join ( oO0o0o0ooO0oO , 'addons.ini' )
 IIi1i = open ( I1ii11iI , "w+" )
 II1III = iI1iI1I1i1I ( 'http://piesustv.net:8000/get.php?username=' + o0oOoO00o + '&password=' + i1 + '&type=m3u_plus&output=mpegts' )
 I1IIIii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II1III )
 IIi1i . write ( r'[' + IiiIII111iI + ']' + '\n' )
 for I1I1iIiII1 , iIi11Ii1 , i111IiI1I , Ii11iII1 in I1IIIii :
  Ii11iII1 = ( Ii11iII1 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  i11i1I1 = ( I1I1iIiII1 + '=plugin://' + IiiIII111iI + '/?url=' + Ii11iII1 + '&mode=15&name=' + ( I1I1iIiII1 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iIi11Ii1 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iIi11Ii1 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IIi1i . write ( i11i1I1 + '\n' )
  if 36 - 36: iIii1I11I1II1 / OoOoOO00 * OOooOOo
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
def iii1i1iiiiIi ( url ) :
 Iiii = xbmc . Player ( OO0OoO0o00 ( ) )
 import urlresolver
 try : Iiii . play ( url ) . strip ( )
 except : pass
 if 53 - 53: O0 * OoO0O00 + OOooOOo
 if 50 - 50: O0 . O0 - oO0o / I1IiiI - o0oOOo0O0Ooo * OoOoOO00
def OO0OoO0o00 ( ) :
 try :
  o0O00oOoOO = getSet ( "core-player" )
  if ( o0O00oOoOO == 'DVDPLAYER' ) : iIIi1i1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0O00oOoOO == 'MPLAYER' ) : iIIi1i1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0O00oOoOO == 'PAPLAYER' ) : iIIi1i1 = xbmc . PLAYER_CORE_PAPLAYER
  else : iIIi1i1 = xbmc . PLAYER_CORE_AUTO
 except : iIIi1i1 = xbmc . PLAYER_CORE_AUTO
 return iIIi1i1
 return True
 if 10 - 10: I11i
 if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
def Iii1i1I11I ( name , url , mode , iconimage , fanart , description ) :
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / ooOoo0O
 I1111IIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0oO = True
 IIiIi1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiIi1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiIi1iI . setProperty ( "Fanart_Image" , fanart )
 Oo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1111IIi , listitem = IIiIi1iI , isFolder = True )
 return Oo0oO
 if 35 - 35: Ii1I % O0 - O0
def OO0o ( name , url , mode , iconimage , fanart , description ) :
 if 16 - 16: II111iiii % OoOoOO00 - II111iiii + Ii1I
 I1111IIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo0oO = True
 IIiIi1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiIi1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiIi1iI . setProperty ( "Fanart_Image" , fanart )
 Oo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1111IIi , listitem = IIiIi1iI , isFolder = False )
 return Oo0oO
 if 12 - 12: OOooOOo / OOooOOo + i11iIiiIii
def Ii ( ) :
 iii1i = [ ]
 I11i1ii1 = sys . argv [ 2 ]
 if len ( I11i1ii1 ) >= 2 :
  O0Oooo0O = sys . argv [ 2 ]
  O0o = O0Oooo0O . replace ( '?' , '' )
  if ( O0Oooo0O [ len ( O0Oooo0O ) - 1 ] == '/' ) :
   O0Oooo0O = O0Oooo0O [ 0 : len ( O0Oooo0O ) - 2 ]
  OoOooO = O0o . split ( '&' )
  iii1i = { }
  for II111iiiI1Ii in range ( len ( OoOooO ) ) :
   o0O0OOO0Ooo = { }
   o0O0OOO0Ooo = OoOooO [ II111iiiI1Ii ] . split ( '=' )
   if ( len ( o0O0OOO0Ooo ) ) == 2 :
    iii1i [ o0O0OOO0Ooo [ 0 ] ] = o0O0OOO0Ooo [ 1 ]
    if 45 - 45: O0 / o0oOOo0O0Ooo
 return iii1i
 if 32 - 32: ooOoo0O . i1I1i1Ii11 . i1I1i1Ii11
 if 62 - 62: I1ii11iIi11i + i1I1i1Ii11 % ooOoo0O + OOooOOo
O0Oooo0O = Ii ( )
Ii11iII1 = None
I1I1iIiII1 = None
iii = None
oOooOOOoOo = None
i1Iii1i1I = None
OOoO00 = None
IiI111111IIII = None
if 37 - 37: IIIIII11i1I / OoOoOO00
if 23 - 23: O0
try :
 IiI111111IIII = int ( O0Oooo0O [ "fav_mode" ] )
except :
 pass
 if 85 - 85: Ii1I
try :
 Ii11iII1 = urllib . unquote_plus ( O0Oooo0O [ "url" ] )
except :
 pass
try :
 I1I1iIiII1 = urllib . unquote_plus ( O0Oooo0O [ "name" ] )
except :
 pass
try :
 oOooOOOoOo = urllib . unquote_plus ( O0Oooo0O [ "iconimage" ] )
except :
 pass
try :
 iii = int ( O0Oooo0O [ "mode" ] )
except :
 pass
try :
 i1Iii1i1I = urllib . unquote_plus ( O0Oooo0O [ "fanart" ] )
except :
 pass
try :
 OOoO00 = urllib . unquote_plus ( O0Oooo0O [ "description" ] )
except :
 pass
 if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
 if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + ooOoo0O / OoOoOO00
print str ( i1iiIIiiI111 ) + ': ' + str ( oOo0oooo00o )
print "Mode: " + str ( iii )
print "URL: " + str ( Ii11iII1 )
print "Name: " + str ( I1I1iIiII1 )
print "IconImage: " + str ( oOooOOOoOo )
if 84 - 84: o0o0OOO0o0 * II111iiii + Oo0Ooo
if 53 - 53: ooOoo0O % II111iiii . i1I1i1Ii11 - iIii1I11I1II1 - i1I1i1Ii11 * II111iiii
def ooO0oOOooOo0 ( content , viewType ) :
 if 38 - 38: IIIIII11i1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if O0oo0OO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % O0oo0OO0 . getSetting ( viewType ) )
  if 84 - 84: iIii1I11I1II1 % ooOoo0O / iIii1I11I1II1 % I11i
  if 45 - 45: O0
if iii == None : OooO0 ( )
elif iii == 11 : O0iII ( )
elif iii == 12 : II11iiii1Ii ( )
elif iii == 13 : iIIIIii1 ( )
elif iii == 14 : oO000Oo000 ( I1I1iIiII1 )
elif iii == 15 : iii1i1iiiiIi ( Ii11iII1 )
elif iii == 16 : I1II1III11iii ( )
elif iii == 17 : i11O0oo0OO0oOOOo ( I1I1iIiII1 )
elif iii == 60000 : O0oo0OO0 . openSettings ( sys . argv [ 0 ] )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
