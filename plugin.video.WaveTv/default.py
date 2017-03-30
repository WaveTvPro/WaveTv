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
i1iII1IiiIiI1 = "0.0.6"
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
 IIiiiiiiIi1I1 ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40 , i1111 + 'standard.png' , oooOOOOO , '' )
 if 21 - 21: OoooooooOO - OoooooooOO
def iIii11I ( ) :
 OOO0OOO00oo = Iii111II ( o0OoOoOO00 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 iiii11I = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OOO0OOO00oo )
 for Ooo0OO0oOO , ii11i1 in iiii11I :
  IIiiiiiiIi1I1 ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , 'http://www.listenlive.eu/' + Ooo0OO0oOO , 51 , i1111 + '3.png' , '' , '' )
def IIIii1II1II ( url ) :
 OOO0OOO00oo = Iii111II ( url )
 iiii11I = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OOO0OOO00oo )
 for ii11i1 , url in iiii11I :
  i1I1iI ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , url , 15 , i1111 + '3.png' , '' , '' )
  if 93 - 93: iIii1I11I1II1 % O0O00o0OOO0 * i1IIi
  if 16 - 16: O0 - Ii * iIii1I11I1II1 + I11II1i
def Ii11iII1 ( title , message , times = 2000 , icon = oOOoo00O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
def Oo0O0O0ooO0O ( ) :
 IIIIii = O0o0 ( )
 OO00Oo = IIIIii . replace ( O0O , "" )
 if os . path . exists ( IIIIii ) or not IIIIii == False :
  O0OOO0OOoO0O = open ( IIIIii , mode = 'r' ) ; O00Oo000ooO0 = O0OOO0OOoO0O . read ( ) ; O0OOO0OOoO0O . close ( )
  OoO0O00 ( "%s - %s" % ( Iii1ii1II11i , OO00Oo ) , O00Oo000ooO0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def O0o0 ( ) :
 IIiII = False
 if os . path . exists ( os . path . join ( O0O , 'xbmc.log' ) ) :
  IIiII = os . path . join ( O0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( O0O , 'kodi.log' ) ) :
  IIiII = os . path . join ( O0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( O0O , 'spmc.log' ) ) :
  IIiII = os . path . join ( O0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( O0O , 'tvmc.log' ) ) :
  IIiII = os . path . join ( O0O , 'tvmc.log' )
 return IIiII
 if 80 - 80: OOoo0O0 . O0O00o0OOO0
 if 25 - 25: OO0o . iIiIiIiIIi / I11II1i . O0o * i1I . ooOoo0O
 if 59 - 59: iIiIiIiIIi + OoooooooOO * OO0o + i1IIi
 if 58 - 58: iIiIiIiIIi * O0o * Oo00OOOOO / O0o
 if 75 - 75: O0O00o0OOO0
def OoO0O00 ( heading , announce ) :
 class I1III ( ) :
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
   try : O0OOO0OOoO0O = open ( announce ) ; OO0O0OoOO0 = O0OOO0OOoO0O . read ( )
   except : OO0O0OoOO0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OO0O0OoOO0 ) )
   return
 I1III ( )
 I1III ( )
 if 10 - 10: OoooooooOO % iIii1I11I1II1
 if 54 - 54: Ii - iIiIiIiIIi % OO0o % o0 % iIii1I11I1II1 + I1I
def I1111I1iII11 ( data ) :
 Oooo0O0oo00oO = len ( data ) % 4
 if 14 - 14: OO0o / OOoo0O0 . OO0o . o0 % i1I * o0
 if 16 - 16: OO0o . I1I + i11iIiiIii
 if 38 - 38: OOoo0O0 * O0o . ooO0o0Oo
 if 98 - 98: OoooooooOO + I11II1i . OO0o
 if 67 - 67: i11iIiiIii - i1IIi % Oo00OOOOO . O0
 if 77 - 77: OOoo0O0 / ooOoo0O
 if Oooo0O0oo00oO != 0 :
  data += b'=' * ( 4 - Oooo0O0oo00oO )
 return base64 . decodestring ( data )
I1 = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s' % ( o0oO0 , Oo0oO0ooo )
iiIii = Oo0o0000o0o0 + 'movie/%s/%s/' % ( o0oO0 , Oo0oO0ooo )
ooo0O = Oo0o0000o0o0 + 'live/%s/%s/' % ( o0oO0 , Oo0oO0ooo )
oOoO0o00OO0 = '&action=get_live_categories'
i1I1ii = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( o0oO0 , Oo0oO0ooo )
oOOo0 = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s&action=get_vod_categories' % ( o0oO0 , Oo0oO0ooo )
oo00O00oO = Oo0o0000o0o0 + 'enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( o0oO0 , Oo0oO0ooo )
iIiIIIi = Oo0o0000o0o0 + 'player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( o0oO0 , Oo0oO0ooo )
ooo00OOOooO = Oo0o0000o0o0 + 'enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=' % ( o0oO0 , Oo0oO0ooo )
if 67 - 67: o0 * O0O00o0OOO0 * Oo00OOOOO + O0o / i1IIi
def I1I111 ( ) :
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , '0' , 14 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]PPV Wrestling[/COLOR]' ) . replace ( '\/' , ' - ' ) , '23' , 14 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]PPV Boxing[/COLOR]' ) . replace ( '\/' , ' - ' ) , '13' , 14 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]IND/PAK[/COLOR]' ) . replace ( '\/' , ' - ' ) , '21' , 14 , i1111 + '1.png' , oooOOOOO , '' )
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]International[/COLOR]' ) . replace ( '\/' , ' - ' ) , '12' , 14 , i1111 + '1.png' , oooOOOOO , '' )
 Oo00oo0oO = Iii111II ( I1 + oOoO0o00OO0 )
 iiii11I = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( Oo00oo0oO )
 for Ooo0OO0oOO , ii11i1 in iiii11I :
  IIiiiiiiIi1I1 ( ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Ooo0OO0oOO , 14 , i1111 + '1.png' , oooOOOOO , '' )
def IIiIi1iI ( url ) :
 url = url
 Oo00oo0oO = Iii111II ( ooo00OOOooO + url )
 i1IiiiI1iI = re . compile ( '<channel>(.+?)</channel>' ) . findall ( Oo00oo0oO )
 iiii11I = re . compile ( '<title>(.+?)</title><description>(.+?)/description><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( i1IiiiI1iI ) )
 i1iIi = re . compile ( '<title>(.+?)</title>.+?<description/><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( i1IiiiI1iI ) )
 for ii11i1 , ooOOoooooo , II1I , O0i1II1Iiii1I11 in iiii11I :
  if 'PPV' in ii11i1 :
   pass
  else :
   try :
    IIII = ( o0OoOoOO00 ( ii11i1 ) )
    iiIiI = ( ( o0OoOoOO00 ( ooOOoooooo ) ) )
    o00oooO0Oo = '('
    o0O0OOO0Ooo = ')'
    i1I1iI ( ( '[COLORsteelblue]' + IIII + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + O0i1II1Iiii1I11 + '.m3u8' , 15 , 'http' + II1I , oooOOOOO , ( '[COLORsteelblue]' + iiIiI + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( o0O0OOO0Ooo , '[COLORsteelblue]' ) . replace ( o00oooO0Oo , '[COLORorangered]' ) )
   except :
    pass
    o00oooO0Oo = '('
    o0O0OOO0Ooo = ')'
    i1I1iI ( ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + O0i1II1Iiii1I11 + '.m3u8' , 15 , 'http' + II1I , oooOOOOO , ( '[COLORsteelblue]' + ooOOoooooo + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( o0O0OOO0Ooo , '[COLORsteelblue]' ) . replace ( o00oooO0Oo , '[COLORorangered]' ) )
   iiIiII1 ( 'tvshows' , 'Media Info 3' )
 for ii11i1 , II1I , O0i1II1Iiii1I11 in i1iIi :
  if 'PPV' in ii11i1 :
   pass
  IIII = ( I1111I1iII11 ( ii11i1 ) )
  i1I1iI ( ( '[COLORsteelblue]' + IIII + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + O0i1II1Iiii1I11 + '.m3u8' , 15 , 'http' + II1I , oooOOOOO , '' )
  iiIiII1 ( 'tvshows' , 'Media Info 3' )
def OOO00O0O ( url ) :
 url = url
 Oo00oo0oO = Iii111II ( i1I1ii + url )
 iiii11I = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( Oo00oo0oO )
 for ii11i1 , type , O0i1II1Iiii1I11 , iii in iiii11I :
  oOooOOOoOo = ( ooo0O + O0i1II1Iiii1I11 + '.m3u8' ) . strip ( )
  i1I1iI ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , oOooOOOoOo , 15 , ( iii ) . replace ( '\/' , '/' ) + 'jpg' , oooOOOOO , type )
  iiIiII1 ( 'tvshows' , 'Media Info 3' )
  if 41 - 41: I11ii1 - O0 - O0
  if 68 - 68: O0o % Ii
def ooO00OO0 ( ) :
 IIiiiiiiIi1I1 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , I1 + '&action=get_vod_streams' , 41 , i1111 + '9.png' , oooOOOOO , '' )
 Oo00oo0oO = Iii111II ( oOOo0 )
 iiii11I = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( Oo00oo0oO )
 for Ooo0OO0oOO , ii11i1 in iiii11I :
  IIiiiiiiIi1I1 ( ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Ooo0OO0oOO , 41 , i1111 + '9.png' , oooOOOOO , '' )
def i11111IIIII ( url ) :
 url = url
 Oo00oo0oO = Iii111II ( oo00O00oO + url )
 iiii11I = re . compile ( '<title>(.+?)</title>.+?<desc_image>.+?http:(.+?).jpg.+?</desc_image>.+?<description>(.+?)</description>.+?<category_id>(.+?)</category_id>.+?<stream_url>.+?http:(.+?).mp4.+?</stream_url>' , re . DOTALL ) . findall ( Oo00oo0oO )
 for ii11i1 , iii , ooOOoooooo , iIiii1i111iI1 , url in iiii11I :
  IIII = ( o0OoOoOO00 ( ii11i1 ) )
  iiIiI = ( ( o0OoOoOO00 ( ooOOoooooo ) ) )
  i1I1iI ( '[COLORsteelblue]' + IIII + '[/COLOR]' , 'http:' + url + '.mp4' , 15 , 'http:' + ( iii ) . replace ( '\/' , '/' ) + '.jpg' , oooOOOOO , '[COLORsteelblue]' + iiIiI + '[/COLOR]' )
  if 14 - 14: I11II1i . I11II1i % OoooooooOO
def iiIi1IIi1I ( ) :
 o0OoOO000ooO0 = Iii111II ( I1 )
 iiii11I = re . compile ( '"username":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 o0o0o0oO0oOO = re . compile ( '"password":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 ii1Ii11I = re . compile ( '"status":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 i1iIi = re . compile ( '"exp_date":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 o00o0 = re . compile ( '"active_cons":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 ii = re . compile ( '"created_at":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 OOooooO0Oo = re . compile ( '"max_connections":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 OO = re . compile ( '"is_trial":"1"' ) . findall ( o0OoOO000ooO0 )
 iIiIIi1 = re . compile ( '"is_trial":"0"' ) . findall ( o0OoOO000ooO0 )
 I1IIII1i = re . compile ( '"timezone":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 I1I11i = re . compile ( '"time_now":"([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 for Ooo0OO0oOO in iiii11I :
  i1I1iI ( '[COLORsteelblue]My Account Information[/COLOR]' , '' , '' , i1111 + '7.png' , '' , '' )
  i1I1iI ( '[COLORsteelblue]Username:[/COLOR]  %s' % ( Ooo0OO0oOO ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in o0o0o0oO0oOO :
  i1I1iI ( '[COLORsteelblue]Password:[/COLOR]  %s' % ( Ooo0OO0oOO ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in ii1Ii11I :
  i1I1iI ( '[COLORsteelblue]Status:[/COLOR]  %s' % ( Ooo0OO0oOO ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in ii :
  Ii1I1I1i1Ii = datetime . fromtimestamp ( float ( ii [ 0 ] ) )
  Ii1I1I1i1Ii . strftime ( '%Y-%m-%d %H:%M:%S' )
  i1I1iI ( '[COLORsteelblue]Created:[/COLOR]  %s' % ( Ii1I1I1i1Ii ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in i1iIi :
  Ii1I1I1i1Ii = datetime . fromtimestamp ( float ( i1iIi [ 0 ] ) )
  Ii1I1I1i1Ii . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= Ii1I1I1i1Ii <= I11i + timedelta ( hours = 24 ) :
   i1I1iI ( '[COLORred]Expires Today[/COLOR]' , '' , '' , i1111 + '7.png' , '' , '' )
  i1I1iI ( '[COLORsteelblue]Expires:[/COLOR]  %s' % ( Ii1I1I1i1Ii ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in o00o0 :
  i1I1iI ( '[COLORsteelblue]Active Connection:[/COLOR]  %s' % ( Ooo0OO0oOO ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in OOooooO0Oo :
  i1I1iI ( '[COLORsteelblue]Max Connection:[/COLOR]  %s' % ( Ooo0OO0oOO ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in OO :
  i1I1iI ( '[COLORsteelblue]Trial:[/COLOR] Yes' , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in iIiIIi1 :
  i1I1iI ( '[COLORsteelblue]Trial:[/COLOR] No' , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in I1IIII1i :
  i1I1iI ( '[COLORsteelblue]Timezone:[/COLOR] %s' % ( Ooo0OO0oOO ) . replace ( '\/' , '/' ) , '' , '' , i1111 + '7.png' , '' , '' )
 for Ooo0OO0oOO in I1I11i :
  i1I1iI ( '[COLORsteelblue]Time Now:[/COLOR] %s' % ( Ooo0OO0oOO ) , '' , '' , i1111 + '7.png' , '' , '' )
 i1I1iI ( '[COLORsteelblue]Sign up[/COLOR]' , '' , 50006 , '' , '' , '' )
def i1Oo0oO00o ( ) :
 o0OoOO000ooO0 = Iii111II ( Oo0o0000o0o0 + 'panel_api.php?username=' + o0oO0 + '&password=' + Oo0oO0ooo )
 iiii11I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( o0OoOO000ooO0 )
 for Ooo0OO0oOO in iiii11I :
  Ii1I1I1i1Ii = datetime . fromtimestamp ( float ( iiii11I [ 0 ] ) )
  Ii1I1I1i1Ii . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I11i <= Ii1I1I1i1Ii <= I11i + timedelta ( hours = 24 ) :
   O0OoO000O0OO . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLORsteelblue]If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLORsteelblue]Please Visit [COLORred]' + oOo0oooo00o + '[COLORsteelblue] To Purchase A licence[/COLOR]' )
   if 13 - 13: o0 * i1II1I11 * I1I
def iI11iI1IiiIiI ( ) :
 Oo00oo0oO = Iii111II ( I1 + '&action=get_simple_data_table&stream_id=1309' )
 iiii11I = re . compile ( '"id":"([^"]*)","epg_id":"([^"]*)","title":"([^"]*)","lang":"([^"]*)","start":"([^"]*)","end":"([^"]*)","description":"([^"]*)","channel_id":"([^"]*)"' , re . DOTALL ) . findall ( Oo00oo0oO )
 for id , Ii1I1i , IIII , OOI1iI1ii1II , O0O0OOOOoo , oOooO0 , ooOOoooooo , Ii1I1Ii in iiii11I :
  i1I1iI ( '[COLORsteelblue]' + Ii1I1Ii + ' - ' + o0OoOoOO00 ( IIII ) + ' - ' + OOI1iI1ii1II + '[/COLOR]' , id , 31 , i1111 + '0.png' , oooOOOOO , O0O0OOOOoo + '[CR]' + oOooO0 + '[CR]' + o0OoOoOO00 ( ooOOoooooo ) )
def OOoO0 ( url ) :
 url = iiIii + id + '.mp4'
 OO0Oooo0oOO0O ( url )
def o00O0 ( url ) :
 IIiiiiiiIi1I1 ( '*[COLORsteelblue]Search[/COLOR]*' , url , 4 , i1111 + '2.png' , i1111 + '2.png' , 'Search Movies' )
 Oo00oo0oO = Iii111II ( url )
 iiii11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( Oo00oo0oO )
 for url , II1I , ooOOoooooo , oOO0O00Oo0O0o , ii11i1 in iiii11I :
  if 'php' in url :
   IIiiiiiiIi1I1 ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , url , 21 , i1111 + '2.png' , i1111 + '2.png' , ooOOoooooo )
  else :
   i1I1iI ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , url , 15 , II1I , oOO0O00Oo0O0o , ooOOoooooo )
   xbmcplugin . addSortMethod ( iI111I11I1I1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1 ( url ) :
 Oo00oo0oO = Iii111II ( url )
 iiii11I = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oo00oo0oO )
 for II1I , ii11i1 , url in iiii11I :
  url = ( ( o0OoOoOO00 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + o0oO0 + '/' + Oo0oO0ooo + url ) . strip ( )
  i1I1iI ( ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(ULTIMATE ONLY)' , ' ' ) , url , 15 , II1I , I1iIIiiIIi1i , '' )
  if 66 - 66: I11II1i - I11II1i - i11iIiiIii . Oo00OOOOO - O0o
  if 77 - 77: OO0o - iIiIiIiIIi - I1I
def IiiiIIiIi1 ( ) :
 i1I1iI ( '[COLORsteelblue]Delete Packages[/COLOR]' , '' , 6 , i1111 + 'standard.png' , oooOOOOO , '' )
 i1I1iI ( '[COLORsteelblue]Delete Cache[/COLOR]' , '' , 7 , i1111 + 'standard.png' , oooOOOOO , '' )
 i1I1iI ( '[COLORsteelblue]View Log File[/COLOR]' , '' , 50000 , i1111 + 'standard.png' , oooOOOOO , '' )
 i1I1iI ( '[COLORsteelblue]Force Refresh[/COLOR]' , '' , 50001 , i1111 + 'standard.png' , oooOOOOO , '' )
 i1I1iI ( '[COLORsteelblue]Force Close[/COLOR]' , '' , 8 , i1111 + 'standard.png' , oooOOOOO , '' )
 if 74 - 74: iIii1I11I1II1 * Oo00OOOOO + OO0o / i1IIi / iIiIiIiIIi . i1II1I11
 if 62 - 62: OoooooooOO * ooOoo0O
 if 58 - 58: OO0o % ooO0o0Oo
def i1OOoO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def OO0O000 ( url ) :
 if url == 'http://' : return False
 try :
  iiIiI1i1 = urllib2 . Request ( url )
  iiIiI1i1 . add_header ( 'User-Agent' , I1IiI )
  oO0O00oOOoooO = urllib2 . urlopen ( iiIiI1i1 )
  oO0O00oOOoooO . close ( )
 except Exception , IiIi11iI :
  return IiIi11iI
 return True
def Oo0O00O000 ( ) :
 o0OoOO000ooO0 = Iii111II ( I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiii11I = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( o0OoOO000ooO0 )
 for ii11i1 , Ooo0OO0oOO , iii , I1iIIiiIIi1i , i11I1IiII1i1i in iiii11I :
  i1I1iI ( ii11i1 , Ooo0OO0oOO , 60002 , iii , i1111 + 'a.png' , i11I1IiII1i1i )
  if 95 - 95: i11iIiiIii
def iI1111iiii ( name , url ) :
 if i1OOoO ( ) == 'android' :
  Oo0OO = O0OoO000O0OO . yesno ( Iii1ii1II11i , "Would you like to download and install:" , "%s" % name )
  if not Oo0OO : Ii11iII1 ( Iii1ii1II11i , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  O0OooOo0o = name
  if Oo0OO :
   if not os . path . exists ( iiIIIII1i1iI ) : os . makedirs ( iiIIIII1i1iI )
   if not OO0O000 ( url ) == True : Ii11iII1 ( Iii1ii1II11i , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iIiiiI . create ( Iii1ii1II11i , 'Downloading %s' % O0OooOo0o , '' , 'Please Wait' )
   iiI11ii1I1 = os . path . join ( iiIIIII1i1iI , "%s.apk" % name )
   try : os . remove ( iiI11ii1I1 )
   except : pass
   downloader . download ( url , iiI11ii1I1 , iIiiiI )
   xbmc . sleep ( 500 )
   iIiiiI . close ( )
   O0OoO000O0OO . ok ( Iii1ii1II11i , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + iiI11ii1I1 + '")' )
  else : Ii11iII1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Ii11iII1 ( Iii1ii1II11i , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 82 - 82: iIiIiIiIIi % o0 / i1I + OO0o / ooO0o0Oo / Ii
 if 70 - 70: O0O00o0OOO0
 if 59 - 59: ooO0o0Oo % O0O00o0OOO0
def ii1iI1I11I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 II1iI = xbmcgui . Dialog ( )
 II1iI . ok ( "Wave Tv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Wave Tv[/COLOR]" )
 return
 if 54 - 54: Ii * OOoo0O0 / Ii / i1II1I11 * OO0o
def O0oOo0o0OO00O ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING Addons20.db ###'
 iIi = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , '' ) )
 II1i111Ii1i = os . path . join ( iIi , 'Addons20.db' )
 try :
  os . remove ( II1i111Ii1i )
  II1iI = xbmcgui . Dialog ( )
  print '=== ' + Iii1ii1II11i + ' - DELETING    ' + str ( II1i111Ii1i ) + '    ==='
  II1iI . ok ( Iii1ii1II11i , "       Remove Addons20.db Sucessfull Please Reboot To Take Affect" )
 except :
  II1iI = xbmcgui . Dialog ( )
  II1iI . ok ( Iii1ii1II11i , "       No File To Remove" )
 return
 if 15 - 15: iIiIiIiIIi / i1IIi
 if 76 - 76: o0 / O0o . O0 % ooOoo0O . ooO0o0Oo + OOoo0O0
 if 71 - 71: Ii . iIiIiIiIIi
 if 62 - 62: OoooooooOO . o0
def ooooooO0oo ( ) :
 if Oo0oO0ooo == 'insert_password' :
  O0OoO000O0OO . ok ( '[COLORsteelblue]Wave Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase ' , ' @ [COLORsteelblue]Wave Tv Media[/COLOR]' )
  I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
 else :
  i1Oo0oO00o ( )
  if 61 - 61: OO0o - O0o - i1IIi
def Iii111II ( url ) :
 iiIiI1i1 = urllib2 . Request ( url )
 iiIiI1i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 oO0O00oOOoooO = urllib2 . urlopen ( iiIiI1i1 )
 o0OoOO000ooO0 = oO0O00oOOoooO . read ( )
 oO0O00oOOoooO . close ( )
 return o0OoOO000ooO0
def IiI1iIiIIIii ( ) :
 Ooo0OO0oOO = oO0o0o0ooO0oO
 oOoO = O0OoO000O0OO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoO00O0 = oOoO . lower ( )
 Oo00oo0oO = Iii111II ( Ooo0OO0oOO )
 OOIi1iI111II1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( Oo00oo0oO )
 for Ooo0OO0oOO , II1I , ooOOoooooo , oOO0O00Oo0O0o , ii11i1 in OOIi1iI111II1I1 :
  if oOoO00O0 in ii11i1 . lower ( ) :
   i1I1iI ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , Ooo0OO0oOO , 15 , II1I , oOO0O00Oo0O0o , ooOOoooooo )
   iIiiiI . create ( '[COLORsteelblue]' + Iii1ii1II11i + '[/COLOR]' , "Checking Library" , '' , 'Please Wait' )
   iIiiiI . update ( 53 , "" , "Getting Movie Links" )
   if 91 - 91: O0o % O0o - ooOoo0O
  iiIiII1 ( 'tvshows' , 'Media Info 3' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
def OoO0O00 ( heading , announce ) :
 class I1III ( ) :
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
   try : O0OOO0OOoO0O = open ( announce ) ; OO0O0OoOO0 = O0OOO0OOoO0O . read ( )
   except : OO0O0OoOO0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OO0O0OoOO0 ) )
   return
 I1III ( )
 I1III ( )
 if 18 - 18: o0 - i11iIiiIii / iIiIiIiIIi . O0o
def OoOo00o0O00 ( ) :
 o0OoOO000ooO0 = Iii111II ( i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( o0OoOO000ooO0 )
 for ii11i1 , Ooo0OO0oOO , iiI , I1iIIiiIIi1i , iiIiI in iiii11I :
  i1I1iI ( '[COLORsteelblue]' + ii11i1 + '[/COLOR]' , Ooo0OO0oOO , 20 , iiI , I1iIIiiIIi1i , iiIiI )
 iiIiII1 ( 'movies' , 'MAIN' )
def oOoo0oOo00 ( url ) :
 iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iIiiiI = xbmcgui . DialogProgress ( )
 iIiiiI . create ( "Wave Tv" , "Downloading Files" , '' , 'Please Wait' )
 iiI11ii1I1 = os . path . join ( iIi , 'plugin.video.WaveTv' + '.zip' )
 try :
  os . remove ( iiI11ii1I1 )
 except :
  pass
 downloader . download ( url , iiI11ii1I1 , iIiiiI )
 IiiiIiii11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iIiiiI . update ( 0 , "" , "Wave Tv Is Now Installing Files Please Wait" )
 print '======================================='
 print IiiiIiii11
 print '======================================='
 extract . all ( iiI11ii1I1 , IiiiIiii11 , iIiiiI )
 OO0000o ( url )
 II1iI = xbmcgui . Dialog ( )
 II1iI . ok ( "Wave Tv" , "Press ok to force close Wave Tv, If unsuccessful Please press home button got to settings/apps and force close Wave Tv and clear cache. " , "[COLOR yellow]Brought To You By Wave Tv[/COLOR]" )
 i1I1i1 ( )
def OO0000o ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 O0OoooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( O0OoooO0 ) :
   IiIIi1 = 0
   IiIIi1 += len ( IiIi1I1 )
   if 47 - 47: i1II1I11 * Oo00OOOOO + iIii1I11I1II1 / Ii / i1I - OoooooooOO
   if 33 - 33: OO0o * O0o - iIiIiIiIIi
   if IiIIi1 > 0 :
    if 83 - 83: OO0o - I11ii1 / o0 / Ii + O0O00o0OOO0 - O0
    II1iI = xbmcgui . Dialog ( )
    if II1iI . yesno ( "Delete Package Cache Files" , str ( IiIIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: O0o * i1I % i1IIi * i11iIiiIii % i1II1I11 - O0O00o0OOO0
     for O0OOO0OOoO0O in IiIi1I1 :
      os . unlink ( os . path . join ( ooo0O0o00O , O0OOO0OOoO0O ) )
     for OOoOoOo in I1i11 :
      shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
     II1iI = xbmcgui . Dialog ( )
     II1iI . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    II1iI = xbmcgui . Dialog ( )
    II1iI . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  II1iI = xbmcgui . Dialog ( )
  II1iI . ok ( Iii1ii1II11i , "Error Deleting Packages please visit The Support Group, Wave Tv on facebook" )
 o000ooooO0o ( url )
 return
def o000ooooO0o ( url ) :
 iI1i11 = os . path . join ( iI1Ii11111iIi , 'addon_data' )
 OoOOoooOO0O = [
 ( iI1i11 ) ,
 ( I1i1iiI1 ) ,
 ( os . path . join ( IiII , 'cache' ) ) ,
 ( os . path . join ( IiII , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1i1iiI1 , 'plugin.video.WaveTv' , 'Images' ) ) ,
 ( os . path . join ( iI1i11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iI1i11 , 'plugin.video.WaveTv' , 'Images' ) ) ]
 if 86 - 86: ooO0o0Oo
 i1Iii11Ii1i1 = 0
 if 59 - 59: i1II1I11 % OoooooooOO . I11II1i / OOoo0O0 + ooOoo0O
 for o0O0oO0O00O0o in OoOOoooOO0O :
  if os . path . exists ( o0O0oO0O00O0o ) and not o0O0oO0O00O0o in [ I1i1iiI1 , iI1i11 ] :
   for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( o0O0oO0O00O0o ) :
    IiIIi1 = 0
    IiIIi1 += len ( IiIi1I1 )
    if IiIIi1 > 0 :
     for O0OOO0OOoO0O in IiIi1I1 :
      if not O0OOO0OOoO0O in i1i1II :
       try :
        os . unlink ( os . path . join ( ooo0O0o00O , O0OOO0OOoO0O ) )
       except :
        pass
      else : IIIIii ( 'Ignore Log File: %s' % O0OOO0OOoO0O )
     for OOoOoOo in I1i11 :
      try :
       shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
       i1Iii11Ii1i1 += 1
       IIIIii ( "[Success] cleared %s files from %s" % ( str ( IiIIi1 ) , os . path . join ( o0O0oO0O00O0o , OOoOoOo ) ) )
      except :
       IIIIii ( "[Failed] to wipe cache in: %s" % os . path . join ( o0O0oO0O00O0o , OOoOoOo ) )
  else :
   for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( o0O0oO0O00O0o ) :
    for OOoOoOo in I1i11 :
     if 'cache' in OOoOoOo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
       i1Iii11Ii1i1 += 1
       IIIIii ( "[Success] wiped %s " % os . path . join ( o0O0oO0O00O0o , OOoOoOo ) )
      except :
       IIIIii ( "[Failed] to wipe cache in: %s" % os . path . join ( o0O0oO0O00O0o , OOoOoOo ) )
       if 28 - 28: i1II1I11 + i1I * O0o % O0O00o0OOO0 . o0 % O0
 Ii11iII1 ( Iii1ii1II11i , 'Clear Cache: Removed %s Files' % i1Iii11Ii1i1 )
def I1iiiiIii ( url ) :
 print '###' + Iii1ii1II11i + ' - DELETING PACKAGES###'
 O0OoooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooo0O0o00O , I1i11 , IiIi1I1 in os . walk ( O0OoooO0 ) :
   IiIIi1 = 0
   IiIIi1 += len ( IiIi1I1 )
   if 19 - 19: i1I - i1II1I11 . O0
   if 60 - 60: iIiIiIiIIi + i1II1I11
   if IiIIi1 > 0 :
    if 9 - 9: I1I * OoooooooOO - iIii1I11I1II1 + OO0o / i1I . i1I
    II1iI = xbmcgui . Dialog ( )
    if II1iI . yesno ( "Delete Package Cache Files" , str ( IiIIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 49 - 49: iIiIiIiIIi
     for O0OOO0OOoO0O in IiIi1I1 :
      os . unlink ( os . path . join ( ooo0O0o00O , O0OOO0OOoO0O ) )
     for OOoOoOo in I1i11 :
      shutil . rmtree ( os . path . join ( ooo0O0o00O , OOoOoOo ) )
     II1iI = xbmcgui . Dialog ( )
     II1iI . ok ( Iii1ii1II11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    II1iI = xbmcgui . Dialog ( )
    II1iI . ok ( Iii1ii1II11i , "       No Packages to DELETE" )
 except :
  II1iI = xbmcgui . Dialog ( )
  II1iI . ok ( Iii1ii1II11i , "Error Deleting Packages" )
 return
 if 25 - 25: OoooooooOO - ooOoo0O . ooOoo0O * O0O00o0OOO0
def i1I1i1 ( ) :
 II1iI = xbmcgui . Dialog ( )
 o000oo = II1iI . yesno ( 'Force Close Wave Tv' , 'You are about to close Wave Tv' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o000oo == 0 : return
 elif o000oo == 1 : pass
 o00o0II1I = i1OOoO ( )
 IIIIii ( "Platform: " + str ( o00o0II1I ) )
 os . _exit ( 1 )
 IIIIii ( "Force close failed!  Trying alternate methods." )
 if o00o0II1I == 'osx' :
  IIIIii ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o00o0II1I == 'linux' :
  IIIIii ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o00o0II1I == 'android' :
  IIIIii ( "############ try android force close #################" )
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
  II1iI . ok ( Iii1ii1II11i , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif o00o0II1I == 'windows' :
  IIIIii ( "############ try windows force close #################" )
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
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  IIIIii ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  IIIIii ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  II1iI . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 12 - 12: ooO0o0Oo - Oo00OOOOO % OO0o * o0
def OO0Oooo0oOO0O ( url ) :
 i11IIIiI11 = xbmc . Player ( III11I1 ( ) )
 import urlresolver
 try : i11IIIiI11 . play ( url ) . strip ( )
 except : pass
def i1OOoO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
 if 36 - 36: O0O00o0OOO0 - I11ii1 . i1II1I11 - i11iIiiIii - O0o * i1II1I11
def IIIIii ( log ) :
 xbmc . log ( "[%s]: %s" % ( Iii1ii1II11i , log ) )
 if not os . path . exists ( I1i1iiI1 ) : os . makedirs ( I1i1iiI1 )
 if not os . path . exists ( o00 ) : O0OOO0OOoO0O = open ( o00 , 'w' ) ; O0OOO0OOoO0O . close ( )
 with open ( o00 , 'a' ) as O0OOO0OOoO0O :
  OooOOOO = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  O0OOO0OOoO0O . write ( OooOOOO . rstrip ( '\r\n' ) + '\n' )
  if 45 - 45: Oo00OOOOO % ooOoo0O - i11iIiiIii
def III11I1 ( ) :
 try :
  ii1iiIiIII1ii = getSet ( "core-player" )
  if ( ii1iiIiIII1ii == 'DVDPLAYER' ) : oO0o0oooO0oO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ii1iiIiIII1ii == 'MPLAYER' ) : oO0o0oooO0oO = xbmc . PLAYER_CORE_MPLAYER
  elif ( ii1iiIiIII1ii == 'PAPLAYER' ) : oO0o0oooO0oO = xbmc . PLAYER_CORE_PAPLAYER
  else : oO0o0oooO0oO = xbmc . PLAYER_CORE_AUTO
 except : oO0o0oooO0oO = xbmc . PLAYER_CORE_AUTO
 return oO0o0oooO0oO
 return True
 if 19 - 19: i11iIiiIii + OoooooooOO - i1II1I11 - o0
 if 21 - 21: O0 % OOoo0O0 . ooOoo0O / iIiIiIiIIi + OOoo0O0
def IIiiiiiiIi1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 53 - 53: O0O00o0OOO0 - ooOoo0O - O0O00o0OOO0 * I11II1i
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1I = True
 OooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOoOo . setProperty ( "Fanart_Image" , fanart )
 iI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = OooOoOo , isFolder = True )
 return iI1I
 if 14 - 14: ooO0o0Oo * O0o + I11II1i + O0 + i11iIiiIii
def i1I1iI ( name , url , mode , iconimage , fanart , description ) :
 if 77 - 77: ooO0o0Oo / OoooooooOO
 oooooo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1I = True
 OooOoOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOoOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOoOo . setProperty ( "Fanart_Image" , fanart )
 iI1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oooooo0OO , listitem = OooOoOo , isFolder = False )
 return iI1I
 if 46 - 46: ooO0o0Oo % iIii1I11I1II1 . I11II1i % I11II1i + i11iIiiIii
def Oo00o0OO0O00o ( ) :
 O0Oooo = [ ]
 iiIi1i = sys . argv [ 2 ]
 if len ( iiIi1i ) >= 2 :
  I1i11111i1i11 = sys . argv [ 2 ]
  OOoOOO0 = I1i11111i1i11 . replace ( '?' , '' )
  if ( I1i11111i1i11 [ len ( I1i11111i1i11 ) - 1 ] == '/' ) :
   I1i11111i1i11 = I1i11111i1i11 [ 0 : len ( I1i11111i1i11 ) - 2 ]
  I1I1i = OOoOOO0 . split ( '&' )
  O0Oooo = { }
  for I1IIIiIiIi in range ( len ( I1I1i ) ) :
   IIIII1 = { }
   IIIII1 = I1I1i [ I1IIIiIiIi ] . split ( '=' )
   if ( len ( IIIII1 ) ) == 2 :
    O0Oooo [ IIIII1 [ 0 ] ] = IIIII1 [ 1 ]
    if 5 - 5: I11ii1
 return O0Oooo
 if 46 - 46: OOoo0O0
 if 45 - 45: I1I
I1i11111i1i11 = Oo00o0OO0O00o ( )
Ooo0OO0oOO = None
ii11i1 = None
IIi = None
iiI = None
I1iIIiiIIi1i = None
iiIiI = None
ooO0oOo0o = None
if 66 - 66: OO0o . i1IIi . i11iIiiIii % I11II1i % I1I
if 43 - 43: O0
try :
 ooO0oOo0o = int ( I1i11111i1i11 [ "fav_mode" ] )
except :
 pass
 if 39 - 39: ooOoo0O . iIii1I11I1II1 * I11ii1 % I1I . iIii1I11I1II1
try :
 Ooo0OO0oOO = urllib . unquote_plus ( I1i11111i1i11 [ "url" ] )
except :
 pass
try :
 ii11i1 = urllib . unquote_plus ( I1i11111i1i11 [ "name" ] )
except :
 pass
try :
 iiI = urllib . unquote_plus ( I1i11111i1i11 [ "iconimage" ] )
except :
 pass
try :
 IIi = int ( I1i11111i1i11 [ "mode" ] )
except :
 pass
try :
 I1iIIiiIIi1i = urllib . unquote_plus ( I1i11111i1i11 [ "fanart" ] )
except :
 pass
try :
 iiIiI = urllib . unquote_plus ( I1i11111i1i11 [ "description" ] )
except :
 pass
 if 54 - 54: O0o
 if 45 - 45: OoooooooOO - O0o + O0 * I11ii1 . Oo00OOOOO
print str ( i1iiIIiiI111 ) + ': ' + str ( i1iII1IiiIiI1 )
print "Mode: " + str ( IIi )
print "URL: " + str ( Ooo0OO0oOO )
print "Name: " + str ( ii11i1 )
print "IconImage: " + str ( iiI )
if 39 - 39: iIii1I11I1II1 / O0 / O0O00o0OOO0 - I11ii1 - I11II1i % O0o
if 31 - 31: o0 - O0 / I1I * OO0o
def iiIiII1 ( content , viewType ) :
 if 12 - 12: ooO0o0Oo - I1I * Ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if I1ii11iIi11i . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % I1ii11iIi11i . getSetting ( viewType ) )
  if 14 - 14: i1II1I11 - I11ii1 % I11ii1 * O0 . i11iIiiIii / O0
  if 79 - 79: ooO0o0Oo - o0 + ooO0o0Oo . O0O00o0OOO0
if IIi == None : IIIII ( )
elif IIi == 1 : Genres ( )
elif IIi == 2 : Lists ( Ooo0OO0oOO , iiI )
elif IIi == 3 : all_mov ( )
elif IIi == 4 : IiI1iIiIIIii ( )
elif IIi == 5 : IiiiIIiIi1 ( )
elif IIi == 6 : I1iiiiIii ( Ooo0OO0oOO )
elif IIi == 7 : o000ooooO0o ( Ooo0OO0oOO )
elif IIi == 8 : i1I1i1 ( )
elif IIi == 9 : OOO00 ( )
elif IIi == 10 : iiIi1IIi1I ( )
elif IIi == 11 : TvGuide ( )
elif IIi == 12 : ooooooO0oo ( )
elif IIi == 13 : ReCreate_Addon_ini ( )
elif IIi == 14 : IIiIi1iI ( Ooo0OO0oOO )
elif IIi == 144 : OOO00O0O ( Ooo0OO0oOO )
elif IIi == 15 : OO0Oooo0oOO0O ( Ooo0OO0oOO )
elif IIi == 16 : I1I111 ( )
elif IIi == 17 : Live_Events ( ii11i1 )
elif IIi == 18 : I1ii11iIi11i . openSettings ( sys . argv [ 0 ] )
elif IIi == 19 : OoOo00o0O00 ( )
elif IIi == 20 : oOoo0oOo00 ( Ooo0OO0oOO )
elif IIi == 30 : iI11iI1IiiIiI ( )
elif IIi == 31 : OOoO0 ( Ooo0OO0oOO )
elif IIi == 40 : ooO00OO0 ( )
elif IIi == 41 : i11111IIIII ( Ooo0OO0oOO )
elif IIi == 21 : o00O0 ( Ooo0OO0oOO )
elif IIi == 22 : ii1 ( Ooo0OO0oOO )
elif IIi == 50 : iIii11I ( )
elif IIi == 51 : IIIii1II1II ( Ooo0OO0oOO )
elif IIi == 50000 : Oo0O0O0ooO0O ( )
elif IIi == 50001 : ii1iI1I11I ( )
elif IIi == 50002 : O0oOo0o0OO00O ( Ooo0OO0oOO )
elif IIi == 60001 : Oo0O00O000 ( )
elif IIi == 60002 : iI1111iiii ( ii11i1 , Ooo0OO0oOO )
if 28 - 28: i1IIi - I11II1i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
