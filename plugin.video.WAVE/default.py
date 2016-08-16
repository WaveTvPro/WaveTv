import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs
import shutil
import urllib2 , urllib
import re
import extract
import downloader
import time
from addon . common . addon import Addon
from addon . common . net import Net
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
###THANK YOU TO THE PEOPLE THAT ORIGINALY WROTE SOME OF THIS CODE WITHOUT YOU I STILL PROBABLY WOULDNT HAVE A CLUE WHERE TO START###
if 73 - 73: II111iiii
IiII1IiiIiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
iIiiiI1IiI1I1 = 'plugin.video.WAVE'
o0OoOoOO00 = xbmcaddon . Addon ( id = iIiiiI1IiI1I1 )
I11i = "Wave Media"
O0O = Net ( )
Oo = o0OoOoOO00 . getSetting ( 'User' )
I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'fanart.jpg' ) )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 , 'icon.png' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iIiiiI1IiI1I1 + '/resources/art/' ) )
iIiiiI = "1.0.8"
Iii1ii1II11i = xbmc . translatePath ( 'special://database' )
iI111iI = xbmc . translatePath ( 'special://thumbnails' ) ;
IiII = "Wave Media Centre"
iI1Ii11111iIi = "http://wavemedia.x10.mx"
i1i1II = 'http://'
O0oo0OO0 = xbmcgui . Dialog ( )
if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
def iiI1iIiI ( ) :
 OOo ( 'THE BUILDS' , iI1Ii11111iIi , 1 , o0OOO + 'PREMIUM.png' , I1ii11iIi11i , '' )
 OOo ( 'URL FIXES' , iI1Ii11111iIi , 2 , o0OOO + 'URL.png' , I1ii11iIi11i , '' )
 OOo ( 'MAINTENANCE' , iI1Ii11111iIi , 3 , o0OOO + 'MAINTENANCE.png' , I1ii11iIi11i , '' )
 if 1 - 1: IIii11I1 - i1111 - i1IIi11111i / I11i1i11i1I % Iiii
 if 87 - 87: oO0o0o0ooO0oO / I1i1I - OoOoo0 % iIiiI1 % OOooO % i1111
 ooO00oo ( 'movies' , 'MAIN' )
 if 52 - 52: I1i1I + I11i1i11i1I % OoooooooOO / i11iIiiIii
def iiIIi1IiIi11 ( ) :
 OOo ( 'DELETE CACHE' , 'url' , 14 , o0OOO + 'MAINTENANCE.png' , I1ii11iIi11i , '' )
 OOo ( 'DELETE PACKAGES' , 'url' , 6 , o0OOO + 'MAINTENANCE.png' , I1ii11iIi11i , '' )
 OOo ( 'FORCE REFRESH' , 'url' , 10 , o0OOO + 'MAINTENANCE.png' , I1ii11iIi11i , 'Force Refresh All Repos' )
 if 11 - 11: OOooO / O0 - i1IIi
 OOo ( 'CHECK MY IP' , 'url' , 12 , o0OOO + 'MAINTENANCE.png' , I1ii11iIi11i , '' )
 OOo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , o0OOO + 'MAINTENANCE.png' , I1ii11iIi11i , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ooO00oo ( 'movies' , 'MAIN' )
 if 85 - 85: I11i1i11i1I % i1111 * OOooO
 if 90 - 90: IIii11I1 % IIii11I1 % Iiii * II1Ii1iI1i
def i1IIiiiii ( ) :
 OOo ( 'CHECK ADVANCED XML' , iI1Ii11111iIi , 8 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( 'MUCKYS XML' , iI1Ii11111iIi + '/wizard/muckys.xml' , 7 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( '0CACHE XML' , iI1Ii11111iIi + '/wizard/0cache.xml' , 7 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( 'MIKEY1234 XML' , iI1Ii11111iIi + '/wizard/mikey.xml' , 7 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( 'TUXENS XML' , iI1Ii11111iIi + '/wizard/tuxens.xml' , 7 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( 'P2P RECOMMENDED XML1' , iI1Ii11111iIi + '/wizard/p2p1.xml' , 7 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( 'P2P RECOMMENDED XML2' , iI1Ii11111iIi + '/wizard/p2p2.xml' , 7 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 OOo ( 'DELETE XML' , iI1Ii11111iIi , 11 , o0OOO + 'XML.png' , I1ii11iIi11i , '' )
 ooO00oo ( 'movies' , 'MAIN' )
 if 55 - 55: i1IIi
def OO ( ) :
 OOo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , iI1Ii11111iIi + '/wizard/customftv/ftvguide-addons.zip' , 5 , o0OOO + 'ftv.png' , I1ii11iIi11i , '' )
 OOo ( 'FTV GUIDE FIRST RUN SETTINGS' , iI1Ii11111iIi + '/wizard/customftv/settings.xml' , 17 , o0OOO + 'ftv.png' , I1ii11iIi11i , '' )
 OOo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , o0OOO + 'ftv.png' , I1ii11iIi11i , '' )
 OOo ( 'RESET FTV DATABASE' , 'url' , 18 , o0OOO + 'ftv.png' , I1ii11iIi11i , '' )
 if 55 - 55: i111I / i1111 * I11i1i11i1I
 if 86 - 86: i11iIiiIii + oO0o0o0ooO0oO + OOooO * Iiii + IIii11I1
 if 61 - 61: i111I / i11iIiiIii
def IiIiIi ( url ) :
 II = iI ( iI11iiiI1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0oooo0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( II )
 for Ii11iii11I , url , oOo00Oo00O , iI11i1I1 , o0o0OOO0o0 in O0oooo0Oo00 :
  OOo ( Ii11iii11I , url , 5 , oOo00Oo00O , iI11i1I1 , o0o0OOO0o0 )
 ooO00oo ( 'movies' , 'MAIN' )
 if 84 - 84: OoOoo0
def iIi1ii1I1 ( ) :
 if Oo == 'Here' :
  O0oo0OO0 . ok ( 'Please Login' , 'You need to set your username to access this' , 'These are unique and provided on sign up' )
  o0OoOoOO00 . openSettings ( sys . argv [ 0 ] )
 else :
  pass
def o0 ( ) :
 iIi1ii1I1 ( )
 II = iI ( iI1Ii11111iIi + '/' + Oo + I11II1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0oooo0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( II )
 for Ii11iii11I , IIIII , oOo00Oo00O , iI11i1I1 , o0o0OOO0o0 in O0oooo0Oo00 :
  OOo ( Ii11iii11I , IIIII , 5 , oOo00Oo00O , iI11i1I1 , o0o0OOO0o0 )
 try :
  II = iI ( ooooooO0oo + Oo + IIiiiiiiIi1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  O0oooo0Oo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( II )
  for Ii11iii11I , IIIII , oOo00Oo00O , iI11i1I1 , o0o0OOO0o0 in O0oooo0Oo00 :
   OOo ( Ii11iii11I , IIIII , 5 , oOo00Oo00O , iI11i1I1 , o0o0OOO0o0 )
 except : pass
 ooO00oo ( 'movies' , 'INFO' )
 if 13 - 13: OoOoo0 + II1Ii1iI1i - OoooooooOO + iIiiI1 . I1i1I + i111I
 if 8 - 8: iIii1I11I1II1 . oooO0oo0oOOOO - iIii1I11I1II1 * oO0o0o0ooO0oO
def OOOO ( name , url , description ) :
 OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iiiiiIIii = xbmcgui . DialogProgress ( )
 iiiiiIIii . create ( "Wave Media Centre" , "Downloading " , '' , 'Please Wait' )
 O000OO0 = os . path . join ( OOO00 , name + '.zip' )
 try :
  os . remove ( O000OO0 )
 except :
  pass
 downloader . download ( url , O000OO0 , iiiiiIIii )
 I11iii1Ii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iiiiiIIii . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I11iii1Ii
 print '======================================='
 extract . all ( O000OO0 , I11iii1Ii , iiiiiIIii )
 O0oo0OO0 = xbmcgui . Dialog ( )
 O0oo0OO0 . ok ( "Wave Media Centre" , "Please Disconnect The Power To Take Effect" , "[COLOR yellow]Brought To You By Wave Media[/COLOR]" )
 if 13 - 13: iIiiI1 % II1Ii1iI1i - i11iIiiIii . oooO0oo0oOOOO + II111iiii
 if 10 - 10: i1111 * OOooO * II111iiii % oO0o0o0ooO0oO . I11i1i11i1I + iIiiI1
 if 19 - 19: II1Ii1iI1i - oooO0oo0oOOOO . I11i1i11i1I / OoOoo0
 if 33 - 33: iIiiI1 / i1111 % oooO0oo0oOOOO + OOooO / i111I
 if 52 - 52: IIii11I1 - OoooooooOO + oO0o0o0ooO0oO + oO0o0o0ooO0oO - IIii11I1 / iIiiI1
def I1I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 O0oo0OO0 = xbmcgui . Dialog ( )
 O0oo0OO0 . ok ( "Wave Media Centre" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Wave Media[/COLOR]" )
 return
 if 24 - 24: i1111
 if 56 - 56: OOooO
 if 92 - 92: I1i1I . Iiii + IIii11I1
 if 28 - 28: i1IIi * ooO0oo0oO0 - IIii11I1 * OoOoo0 * oO0o0o0ooO0oO / i111I
 if 94 - 94: II111iiii % i1111 / II1Ii1iI1i * iIii1I11I1II1
 if 54 - 54: IIii11I1 - oooO0oo0oOOOO + OoooooooOO
 if 70 - 70: oO0o0o0ooO0oO / Iiii . I1i1I % ooO0oo0oO0
 if 67 - 67: II1Ii1iI1i * IIii11I1 . OoOoo0 - i111I * IIii11I1
 if 46 - 46: I11i1i11i1I + II1Ii1iI1i . oooO0oo0oOOOO * i1IIi11111i % OoOoo0
 if 86 - 86: oooO0oo0oOOOO + oO0o0o0ooO0oO % i11iIiiIii * i1IIi11111i . OOooO * Iiii
 if 44 - 44: i1IIi11111i
 if 88 - 88: iIiiI1 % oO0o0o0ooO0oO . II111iiii
 if 38 - 38: IIii11I1
 if 57 - 57: O0 / i1IIi11111i * iIiiI1 / II1Ii1iI1i . II111iiii
 if 26 - 26: I1i1I
 if 91 - 91: i111I . i1111 + i111I - I1i1I / OoooooooOO
 if 39 - 39: i1111 / OOooO - II111iiii
 if 98 - 98: i1111 / Iiii % i1IIi11111i . II1Ii1iI1i
 if 91 - 91: i1IIi11111i % ooO0oo0oO0
 if 64 - 64: Iiii % I1i1I - iIiiI1 - i1IIi11111i
 if 31 - 31: Iiii - II111iiii . Iiii
 if 18 - 18: IIii11I1
 if 98 - 98: I1i1I * I1i1I / I1i1I + Iiii
def ii111111I1iII ( ) :
 try :
  if os . path . exists ( iI111iI ) == True :
   O0oo0OO0 = xbmcgui . Dialog ( )
   if O0oo0OO0 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( iI111iI ) :
     i11i1I1 = 0
     i11i1I1 += len ( I1I1iIiII1 )
     if i11i1I1 > 0 :
      for ii1I in I1I1iIiII1 :
       os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
  Oo0ooOo0o = os . path . join ( Iii1ii1II11i , "Textures13.db" )
  os . unlink ( Oo0ooOo0o )
  O0oo0OO0 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "Error Deleting Thumbnails please visit Wave Media on facebook" )
 return
 if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * II111iiii . I11i1i11i1I / i11iIiiIii
 if 2 - 2: oooO0oo0oOOOO / O0 / IIii11I1 % II1Ii1iI1i % oO0o0o0ooO0oO
 if 52 - 52: IIii11I1
 if 95 - 95: oO0o0o0ooO0oO
 if 87 - 87: OOooO + II1Ii1iI1i . I11i1i11i1I + II1Ii1iI1i
 if 91 - 91: O0
 if 61 - 61: II111iiii
 if 64 - 64: OOooO / II1Ii1iI1i - O0 - Iiii
 if 86 - 86: Iiii % II1Ii1iI1i / oooO0oo0oOOOO / II1Ii1iI1i
def iIIi1i1 ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 i1IIIiiII1 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( i1IIIiiII1 ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( i1IIIiiII1 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 87 - 87: i1IIi11111i * i1111 + I11i1i11i1I / iIii1I11I1II1 / I1i1I
   if 37 - 37: I1i1I - OOooO * i1IIi11111i % i11iIiiIii - iIiiI1
   if i11i1I1 > 0 :
    if 83 - 83: Iiii / oooO0oo0oOOOO
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete KODI Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 34 - 34: OoOoo0
     for ii1I in I1I1iIiII1 :
      try :
       os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
      except :
       pass
     for oOo in i1iIi1iIi1i :
      try :
       shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      except :
       pass
       if 75 - 75: oooO0oo0oOOOO + ooO0oo0oO0
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  OoooO0oO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 49 - 49: oO0o0o0ooO0oO / i111I . II111iiii
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( OoooO0oO ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 68 - 68: i11iIiiIii % i1111 + i11iIiiIii
   if i11i1I1 > 0 :
    if 31 - 31: II111iiii . oooO0oo0oOOOO
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete ATV2 Cache Files" , str ( i11i1I1 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 1 - 1: ooO0oo0oO0 / IIii11I1 % I1i1I * OoOoo0 . i11iIiiIii
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 2 - 2: i1111 * Iiii - iIii1I11I1II1 + oooO0oo0oOOOO . i1IIi11111i % I1i1I
   else :
    pass
  ooOOOoOooOoO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 91 - 91: I1i1I % i1IIi % iIii1I11I1II1
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( ooOOOoOooOoO ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 20 - 20: I11i1i11i1I % oO0o0o0ooO0oO / oO0o0o0ooO0oO + oO0o0o0ooO0oO
   if i11i1I1 > 0 :
    if 45 - 45: i1IIi11111i - OoOoo0 - OoooooooOO - i111I . II111iiii / O0
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete ATV2 Cache Files" , str ( i11i1I1 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 51 - 51: O0 + I1i1I
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 8 - 8: i1IIi11111i * II1Ii1iI1i - oO0o0o0ooO0oO - i111I * I11i1i11i1I % oooO0oo0oOOOO
   else :
    pass
    if 48 - 48: O0
    if 11 - 11: Iiii + OoooooooOO - i111I / IIii11I1 + ooO0oo0oO0 . II111iiii
    if 41 - 41: oO0o0o0ooO0oO - O0 - O0
    if 68 - 68: I11i1i11i1I % iIiiI1
 ooO00OO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( ooO00OO0 ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( ooO00OO0 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 31 - 31: I1i1I % I1i1I % Iiii
   if 69 - 69: i111I - ooO0oo0oO0 + i1IIi / iIiiI1
   if i11i1I1 > 0 :
    if 49 - 49: O0 . I1i1I
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete WTF Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: OoOoo0 * oooO0oo0oOOOO . iIii1I11I1II1 % OoooooooOO + I1i1I
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 78 - 78: i111I . I11i1i11i1I + i111I / Iiii / i111I
   else :
    pass
    if 54 - 54: II1Ii1iI1i % I1i1I
    if 37 - 37: II1Ii1iI1i * ooO0oo0oO0 / OOooO - I1i1I % II111iiii . i1IIi11111i
 O00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( O00 ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( O00 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 29 - 29: iIiiI1 / i111I . i1IIi * oooO0oo0oOOOO + i11iIiiIii
   if 6 - 6: OOooO / i11iIiiIii + I1i1I * i1IIi11111i
   if i11i1I1 > 0 :
    if 80 - 80: II111iiii
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete 4oD Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 83 - 83: Iiii . i11iIiiIii + II111iiii . IIii11I1 * Iiii
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 53 - 53: II111iiii
   else :
    pass
    if 31 - 31: i111I
    if 80 - 80: iIiiI1 . i11iIiiIii - IIii11I1
 iIiIIi1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iIiIIi1 ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( iIiIIi1 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 7 - 7: OOooO - ooO0oo0oO0 - i1IIi11111i + OOooO
   if 26 - 26: oO0o0o0ooO0oO
   if i11i1I1 > 0 :
    if 35 - 35: oO0o0o0ooO0oO - oooO0oo0oOOOO % IIii11I1 . OoooooooOO % oO0o0o0ooO0oO
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete BBC iPlayer Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: I1i1I - oO0o0o0ooO0oO . II111iiii + OoooooooOO . i11iIiiIii
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 94 - 94: IIii11I1 * oO0o0o0ooO0oO / ooO0oo0oO0 / oO0o0o0ooO0oO
   else :
    pass
    if 87 - 87: ooO0oo0oO0 . OoOoo0
    if 75 - 75: OOooO + II1Ii1iI1i + IIii11I1 * Iiii % i1IIi11111i . I1i1I
    if 55 - 55: I11i1i11i1I . oooO0oo0oOOOO
 oOo0O0o00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( oOo0O0o00o ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( oOo0O0o00o ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 64 - 64: I11i1i11i1I % iIii1I11I1II1 * i1IIi11111i
   if 79 - 79: O0
   if i11i1I1 > 0 :
    if 78 - 78: i1111 + I11i1i11i1I - iIiiI1
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete Simple Downloader Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: IIii11I1 - i1IIi11111i + iIii1I11I1II1 / II1Ii1iI1i % ooO0oo0oO0
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 57 - 57: i111I / OOooO
   else :
    pass
    if 29 - 29: iIii1I11I1II1 + II1Ii1iI1i * i111I * I11i1i11i1I . oooO0oo0oOOOO * oooO0oo0oOOOO
    if 7 - 7: OoOoo0 * iIiiI1 % oO0o0o0ooO0oO - IIii11I1
 i1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( i1i ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 56 - 56: i1111 % O0 - oooO0oo0oOOOO
   if 100 - 100: oO0o0o0ooO0oO - O0 % i1IIi11111i * I11i1i11i1I + oooO0oo0oOOOO
   if i11i1I1 > 0 :
    if 88 - 88: OoooooooOO - i111I * O0 * OoooooooOO . OoooooooOO
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete ITV Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: iIiiI1 + I1i1I * i1IIi11111i / iIii1I11I1II1 - oooO0oo0oOOOO
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 54 - 54: iIiiI1 / I11i1i11i1I . i1IIi11111i % I1i1I
   else :
    pass
    if 57 - 57: i11iIiiIii . i1111 - oO0o0o0ooO0oO - i1IIi11111i + II1Ii1iI1i
    if 63 - 63: II1Ii1iI1i * I1i1I
 oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( oo ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 44 - 44: i1IIi11111i / Iiii / Iiii
   if 87 - 87: ooO0oo0oO0 . oooO0oo0oOOOO - II111iiii + O0 / ooO0oo0oO0 / i1IIi11111i
   if i11i1I1 > 0 :
    if 25 - 25: oooO0oo0oOOOO . oooO0oo0oOOOO - II1Ii1iI1i % II1Ii1iI1i - i11iIiiIii / iIiiI1
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete Movies4me Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 51 - 51: ooO0oo0oO0 / II1Ii1iI1i . I11i1i11i1I * IIii11I1 + i111I * OoOoo0
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 73 - 73: i111I + OoooooooOO - O0 - oO0o0o0ooO0oO - II111iiii
   else :
    pass
    if 99 - 99: OOooO . oO0o0o0ooO0oO + iIiiI1 + OoooooooOO % IIii11I1
    if 51 - 51: iIii1I11I1II1
 iIIiIi1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( iIIiIi1 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 74 - 74: I1i1I + IIii11I1
   if 71 - 71: ooO0oo0oO0 % I11i1i11i1I
   if i11i1I1 > 0 :
    if 98 - 98: Iiii % i11iIiiIii % OOooO + oO0o0o0ooO0oO
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete Phoenix Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 78 - 78: i1111 % i1IIi11111i / I1i1I - iIii1I11I1II1
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 69 - 69: iIiiI1
   else :
    pass
    if 11 - 11: oooO0oo0oOOOO
    if 16 - 16: oO0o0o0ooO0oO + OoOoo0 * O0 % i1IIi . oooO0oo0oOOOO
 Oo0OO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( Oo0OO ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 78 - 78: I11i1i11i1I - OoooooooOO - i1111 / OOooO / II111iiii
   if 29 - 29: oooO0oo0oOOOO % oooO0oo0oOOOO
   if i11i1I1 > 0 :
    if 94 - 94: iIii1I11I1II1 / ooO0oo0oO0 % I1i1I * I1i1I * II111iiii
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete YouTube Music Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: i111I + II1Ii1iI1i / IIii11I1 / I11i1i11i1I * iIii1I11I1II1
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 62 - 62: I11i1i11i1I / i1IIi11111i - i111I . Iiii
   else :
    pass
    if 11 - 11: i1111 . i111I * OoOoo0 * OoooooooOO + OOooO
    if 33 - 33: O0 * IIii11I1 - iIiiI1 % iIiiI1
 I11I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( I11I ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 50 - 50: iIiiI1 * i11iIiiIii * iIii1I11I1II1 - II111iiii * IIii11I1 * II1Ii1iI1i
   if 94 - 94: OoooooooOO + OoooooooOO . II111iiii + Iiii / i1111 % oO0o0o0ooO0oO
   if i11i1I1 > 0 :
    if 18 - 18: I1i1I * O0 - OoooooooOO % oooO0oo0oOOOO . II111iiii / i1IIi
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete SuperCartoons Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: Iiii / I11i1i11i1I . O0 % oooO0oo0oOOOO . IIii11I1 + OoOoo0
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 71 - 71: iIiiI1 . II111iiii
   else :
    pass
    if 62 - 62: OoooooooOO . Iiii
    if 61 - 61: II1Ii1iI1i - I11i1i11i1I - i1IIi
 IiI1iIiIIIii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( IiI1iIiIIIii ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 53 - 53: i1IIi
   if 59 - 59: IIii11I1
   if i11i1I1 > 0 :
    if 81 - 81: II1Ii1iI1i - II1Ii1iI1i . I1i1I
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete TVonline Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: Iiii % i11iIiiIii - oooO0oo0oOOOO
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 7 - 7: O0 * i11iIiiIii * oO0o0o0ooO0oO + OOooO % i111I - OOooO
   else :
    pass
    if 39 - 39: ooO0oo0oO0 * I11i1i11i1I % I11i1i11i1I - OoooooooOO + IIii11I1 - Iiii
    if 23 - 23: i11iIiiIii
 II1iIi11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( i1i ) == True :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( II1iIi11 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 12 - 12: oO0o0o0ooO0oO + i11iIiiIii * iIii1I11I1II1 / i1111 . Iiii
   if 5 - 5: i1IIi + OoOoo0 / IIii11I1 . I1i1I / Iiii
   if i11i1I1 > 0 :
    if 32 - 32: oooO0oo0oOOOO % iIii1I11I1II1 / i1IIi - oooO0oo0oOOOO
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete YouTube Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: iIiiI1 * i111I - OOooO + I11i1i11i1I * oooO0oo0oOOOO % i111I
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
      if 15 - 15: II1Ii1iI1i % oooO0oo0oOOOO * Iiii
   else :
    pass
    if 81 - 81: OOooO - iIii1I11I1II1 - i1IIi / iIiiI1 - O0 * Iiii
    if 20 - 20: i1IIi11111i % OoOoo0
    if 19 - 19: i1111 % OoOoo0 + OOooO / iIiiI1 . OOooO
 IiIi1I1 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 O0oo0OO0 = xbmcgui . Dialog ( )
 try :
  if O0oo0OO0 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   IiIIi1 = os . path . join ( IiIi1I1 , "cache.db" )
   os . unlink ( IiIIi1 )
   if 47 - 47: ooO0oo0oO0 * i1111 + iIii1I11I1II1 / iIiiI1 / i111I - OoooooooOO
 except :
  pass
  if 33 - 33: II1Ii1iI1i * I11i1i11i1I - II111iiii
 O0oo0OO0 = xbmcgui . Dialog ( )
 O0oo0OO0 . ok ( "Wave Media" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By Wave Media[/COLOR]" )
 if 83 - 83: II1Ii1iI1i - oO0o0o0ooO0oO / Iiii / iIiiI1 + i1IIi11111i - O0
 if 4 - 4: I11i1i11i1I * i111I % i1IIi * i11iIiiIii % ooO0oo0oO0 - i1IIi11111i
 if 67 - 67: II1Ii1iI1i + i1111 . IIii11I1 . II111iiii
 if 98 - 98: I1i1I
 if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . IIii11I1 / II111iiii % ooO0oo0oO0
 if 38 - 38: OOooO - I11i1i11i1I / I1i1I
 if 66 - 66: O0 % i1111 + i11iIiiIii . II1Ii1iI1i / oO0o0o0ooO0oO + i1111
 if 86 - 86: IIii11I1
 if 5 - 5: OoOoo0 * II1Ii1iI1i
def i1Ii1i1I11Iii ( url ) :
 print '###' + I11i + ' - DELETING PACKAGES###'
 I1i1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for O00ooo0O0 , i1iIi1iIi1i , I1I1iIiII1 in os . walk ( I1i1i1 ) :
   i11i1I1 = 0
   i11i1I1 += len ( I1I1iIiII1 )
   if 73 - 73: O0 * I1i1I + oO0o0o0ooO0oO + OOooO
   if 40 - 40: II111iiii . II1Ii1iI1i * iIiiI1 + I11i1i11i1I + I11i1i11i1I
   if i11i1I1 > 0 :
    if 9 - 9: Iiii % OoooooooOO . i1IIi11111i % Iiii
    O0oo0OO0 = xbmcgui . Dialog ( )
    if O0oo0OO0 . yesno ( "Delete Package Cache Files" , str ( i11i1I1 ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: i11iIiiIii
     for ii1I in I1I1iIiII1 :
      os . unlink ( os . path . join ( O00ooo0O0 , ii1I ) )
     for oOo in i1iIi1iIi1i :
      shutil . rmtree ( os . path . join ( O00ooo0O0 , oOo ) )
     O0oo0OO0 = xbmcgui . Dialog ( )
     O0oo0OO0 . ok ( I11i , "       Deleting Packages all done" )
    else :
     pass
   else :
    O0oo0OO0 = xbmcgui . Dialog ( )
    O0oo0OO0 . ok ( I11i , "       No Packages to DELETE" )
 except :
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "Error Deleting Packages please visit Android Bros on facebook" )
 return
 if 31 - 31: iIii1I11I1II1 / i111I / i1111
 if 41 - 41: ooO0oo0oO0
 if 10 - 10: ooO0oo0oO0 / ooO0oo0oO0 / iIiiI1 . iIiiI1
 if 98 - 98: ooO0oo0oO0 / oooO0oo0oOOOO . O0 + i111I
 if 43 - 43: II111iiii . i1IIi11111i / i1111
 if 20 - 20: oooO0oo0oOOOO
 if 95 - 95: I1i1I - oooO0oo0oOOOO
 if 34 - 34: OOooO * oooO0oo0oOOOO . i1IIi * OOooO / OOooO
 if 30 - 30: i1111 + ooO0oo0oO0 / ooO0oo0oO0 % i1111 . i1111
def O0O0Oo00 ( url , name ) :
 OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOoO00o = os . path . join ( OOO00 , 'advancedsettings.xml' )
 O0oo0OO0 = xbmcgui . Dialog ( )
 oO00O0 = os . path . join ( OOO00 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oO00O0 ) == False :
  if O0oo0OO0 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + I11i + ' - ADVANCED XML###'
   OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oOoO00o = os . path . join ( OOO00 , 'advancedsettings.xml' )
   try :
    os . remove ( oOoO00o )
    print '=== Wave Media - REMOVING    ' + str ( oOoO00o ) + '    ==='
   except :
    pass
   II = O0O . http_GET ( url ) . content
   IIi1IIIi = open ( oOoO00o , "w" )
   IIi1IIIi . write ( II )
   IIi1IIIi . close ( )
   print '=== Wave Media - WRITING NEW    ' + str ( oOoO00o ) + '    ==='
   O0oo0OO0 = xbmcgui . Dialog ( )
   O0oo0OO0 . ok ( I11i , "       Done Adding new Advanced XML" )
 else :
  print '###' + I11i + ' - ADVANCED XML###'
  OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oOoO00o = os . path . join ( OOO00 , 'advancedsettings.xml' )
  try :
   os . remove ( oOoO00o )
   print '=== Wave Media - REMOVING    ' + str ( oOoO00o ) + '    ==='
  except :
   pass
  II = O0O . http_GET ( url ) . content
  IIi1IIIi = open ( oOoO00o , "w" )
  IIi1IIIi . write ( II )
  IIi1IIIi . close ( )
  print '=== Wave Media - WRITING NEW    ' + str ( oOoO00o ) + '    ==='
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "       Done Adding new Advanced XML" )
 return
 if 99 - 99: oO0o0o0ooO0oO + i111I * II111iiii . IIii11I1 - i1111
def o0OOOo ( url , name ) :
 print '###' + I11i + ' - CHECK ADVANCE XML###'
 OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOoO00o = os . path . join ( OOO00 , 'advancedsettings.xml' )
 try :
  IIi1IIIi = open ( oOoO00o ) . read ( )
  if 'zero' in IIi1IIIi :
   name = '0CACHE'
  elif 'tuxen' in IIi1IIIi :
   name = 'TUXENS'
  elif 'muckys' in IIi1IIIi :
   name = 'MUCKYS'
  elif 'p2p1' in IIi1IIIi :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IIi1IIIi :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IIi1IIIi :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 O0oo0OO0 = xbmcgui . Dialog ( )
 O0oo0OO0 . ok ( I11i , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * oooO0oo0oOOOO
def iII1ii1 ( url ) :
 print '###' + I11i + ' - DELETING ADVANCE XML###'
 OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOoO00o = os . path . join ( OOO00 , 'advancedsettings.xml' )
 try :
  os . remove ( oOoO00o )
  O0oo0OO0 = xbmcgui . Dialog ( )
  print '=== Wave Media - DELETING    ' + str ( oOoO00o ) + '    ==='
  O0oo0OO0 . ok ( I11i , "       Remove Advanced Settings Sucessfull" )
 except :
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "       No Advanced Settings To Remove" )
 return
 if 12 - 12: I11i1i11i1I - OOooO . OoooooooOO / i1111 . i1IIi * i111I
 if 19 - 19: i11iIiiIii + OoooooooOO - ooO0oo0oO0 - Iiii
 if 21 - 21: O0 % OoOoo0 . oooO0oo0oOOOO / II111iiii + OoOoo0
 if 53 - 53: i1IIi11111i - oooO0oo0oOOOO - i1IIi11111i * I1i1I
 if 71 - 71: O0 - iIii1I11I1II1
 if 12 - 12: I11i1i11i1I / IIii11I1
 if 42 - 42: ooO0oo0oO0
 if 19 - 19: i1IIi11111i % i1111 * iIii1I11I1II1 + oooO0oo0oOOOO
 if 46 - 46: ooO0oo0oO0
 if 1 - 1: I1i1I
def O0O0Ooo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 O0oooo0Oo00 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( O0O . http_GET ( url ) . content )
 for oOoO0 , Oo0 , oo0O0o00o0O , I11i1II in O0oooo0Oo00 :
  if inc < 2 : O0oo0OO0 = xbmcgui . Dialog ( ) ; O0oo0OO0 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % oOoO0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oo0O0o00o0O , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I11i1II )
  inc = inc + 1
  if 72 - 72: iIii1I11I1II1 . i1IIi / ooO0oo0oO0 . II111iiii
  if 54 - 54: II111iiii % II111iiii
  if 86 - 86: O0 % oO0o0o0ooO0oO * OOooO * iIii1I11I1II1 * i1IIi * Iiii
  if 83 - 83: II1Ii1iI1i % II111iiii - II1Ii1iI1i + OoOoo0 - O0
  if 52 - 52: ooO0oo0oO0 * OOooO
  if 33 - 33: oO0o0o0ooO0oO
  if 74 - 74: I11i1i11i1I + O0 + i1IIi - i1IIi + II111iiii
  if 83 - 83: i1111 - oooO0oo0oOOOO + I11i1i11i1I
  if 5 - 5: oO0o0o0ooO0oO
def iIi1i1iIi1iI ( url , name ) :
 O0oo0OO0 = xbmcgui . Dialog ( )
 if O0oo0OO0 . yesno ( "Wave Media" , '                                    Install Latest .ini File' ) :
  print '###' + I11i + ' - CUSTOM FTV INI###'
  OOO00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  oOoO00o = os . path . join ( OOO00 , 'addons2.ini' )
  II = O0O . http_GET ( url ) . content
  IIi1IIIi = open ( oOoO00o , "w" )
  IIi1IIIi . write ( II )
  IIi1IIIi . close ( )
  print '=== Wave Media - WRITING NEW    ' + str ( oOoO00o ) + '    ==='
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "                               Done Adding New .ini File" )
 return
 if 26 - 26: OoooooooOO * oooO0oo0oOOOO + I11i1i11i1I
def IiIii1i111 ( url , name ) :
 O0oo0OO0 = xbmcgui . Dialog ( )
 if O0oo0OO0 . yesno ( "Wave Media" , '                               Install Custom Settings' ) :
  print '###' + I11i + ' - CUSTOM FTV SETTINGS###'
  OOO00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  oOoO00o = os . path . join ( OOO00 , 'settings.xml' )
  II = O0O . http_GET ( url ) . content
  IIi1IIIi = open ( oOoO00o , "w" )
  IIi1IIIi . write ( II )
  IIi1IIIi . close ( )
  print '=== Wave Media - WRITING NEW    ' + str ( oOoO00o ) + '    ==='
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "                               Done Adding New Settings" )
 return
 if 43 - 43: O0
 if 39 - 39: oooO0oo0oOOOO . iIii1I11I1II1 * oO0o0o0ooO0oO % OOooO . iIii1I11I1II1
def oO0OoO00o ( ) :
 try :
  II1iiiiII = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/script.ftvguide' , '' ) )
  if os . path . exists ( II1iiiiII ) == True :
   O0oo0OO0 = xbmcgui . Dialog ( )
   if O0oo0OO0 . yesno ( "Wave Media" , "                               Delete FTV Guide Database" ) :
    O0OoOO0oo0 = os . path . join ( II1iiiiII , "source.db" )
    os . unlink ( O0OoOO0oo0 )
  O0oo0OO0 . ok ( "Wave Media" , "                                     FTV Database Reset" )
 except :
  O0oo0OO0 = xbmcgui . Dialog ( )
  O0oo0OO0 . ok ( I11i , "               Error Deleting Database No Database To Delete" )
 return
 if 96 - 96: II1Ii1iI1i . IIii11I1 - OOooO
 if 99 - 99: OoOoo0 . ooO0oo0oO0 - oO0o0o0ooO0oO % oO0o0o0ooO0oO * O0 . II111iiii
 if 4 - 4: oO0o0o0ooO0oO
 if 51 - 51: i111I - O0 % i1IIi11111i - II111iiii
 if 31 - 31: I1i1I / ooO0oo0oO0 - I1i1I - I11i1i11i1I
def iI ( url ) :
 I1iiIIIi11 = urllib2 . Request ( url )
 I1iiIIIi11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1I11ii1i = urllib2 . urlopen ( I1iiIIIi11 )
 II = Ii1I11ii1i . read ( )
 Ii1I11ii1i . close ( )
 return II
 if 89 - 89: I1i1I . O0 / i1111 % II1Ii1iI1i . ooO0oo0oO0
 if 50 - 50: II111iiii + i1111 . i1IIi % IIii11I1
def IIIi ( ) :
 O00OoO0o = [ ]
 i1i111iI = sys . argv [ 2 ]
 if len ( i1i111iI ) >= 2 :
  IIiiI = sys . argv [ 2 ]
  III1i11 = IIiiI . replace ( '?' , '' )
  if ( IIiiI [ len ( IIiiI ) - 1 ] == '/' ) :
   IIiiI = IIiiI [ 0 : len ( IIiiI ) - 2 ]
  iiI111 = III1i11 . split ( '&' )
  O00OoO0o = { }
  for I1iIiIi11i11 in range ( len ( iiI111 ) ) :
   O0ooo0 = { }
   O0ooo0 = iiI111 [ I1iIiIi11i11 ] . split ( '=' )
   if ( len ( O0ooo0 ) ) == 2 :
    O00OoO0o [ O0ooo0 [ 0 ] ] = O0ooo0 [ 1 ]
    if 8 - 8: OOooO + II111iiii / I1i1I / Iiii
 return O00OoO0o
 if 74 - 74: O0 / i1IIi
ooooooO0oo = base64 . decodestring ( 'aHR0cDovL25ld2l6LmJ5ZXRob3N0MTIuY29tLw==' )
IIiiiiiiIi1I1 = base64 . decodestring ( 'L3dpemFyZC50eHQ=' )
I11II1i = base64 . decodestring ( 'L3dhdmUudHh0' )
iI11iiiI1II = base64 . decodestring ( 'aHR0cDovL3dpemguaXMtZ3JlYXQub3JnL3doZi50eHQ=' )
def OOo ( name , url , mode , iconimage , fanart , description ) :
 OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iiiiii111i1ii = True
 i1i1iII1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1iII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1iII1 . setProperty ( "Fanart_Image" , fanart )
 if mode == 5 :
  Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = False )
 else :
  Iiiiii111i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OoO , listitem = i1i1iII1 , isFolder = True )
 return Iiiiii111i1ii
 if 25 - 25: iIii1I11I1II1 % I1i1I . OOooO
 if 14 - 14: i1IIi11111i + i1111 - I1i1I / O0 . iIiiI1
IIiiI = IIIi ( )
IIIII = None
Ii11iii11I = None
i1iiIiI1Ii1i = None
oOo00Oo00O = None
iI11i1I1 = None
o0o0OOO0o0 = None
if 22 - 22: OoOoo0 / i11iIiiIii
if 62 - 62: i111I / i1111
try :
 IIIII = urllib . unquote_plus ( IIiiI [ "url" ] )
except :
 pass
try :
 Ii11iii11I = urllib . unquote_plus ( IIiiI [ "name" ] )
except :
 pass
try :
 oOo00Oo00O = urllib . unquote_plus ( IIiiI [ "iconimage" ] )
except :
 pass
try :
 i1iiIiI1Ii1i = int ( IIiiI [ "mode" ] )
except :
 pass
try :
 iI11i1I1 = urllib . unquote_plus ( IIiiI [ "fanart" ] )
except :
 pass
try :
 o0o0OOO0o0 = urllib . unquote_plus ( IIiiI [ "description" ] )
except :
 pass
 if 7 - 7: OoooooooOO . OoOoo0
 if 53 - 53: oO0o0o0ooO0oO % oO0o0o0ooO0oO * IIii11I1 + II1Ii1iI1i
print str ( IiII ) + ': ' + str ( iIiiiI )
print "Mode: " + str ( i1iiIiI1Ii1i )
print "URL: " + str ( IIIII )
print "Name: " + str ( Ii11iii11I )
print "IconImage: " + str ( oOo00Oo00O )
if 92 - 92: OoooooooOO + i1IIi / oO0o0o0ooO0oO * O0
if 100 - 100: OOooO % iIii1I11I1II1 * II111iiii - I1i1I
def ooO00oo ( content , viewType ) :
 if 92 - 92: OOooO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OoOoOO00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OoOoOO00 . getSetting ( viewType ) )
  if 22 - 22: ooO0oo0oO0 % I1i1I * i1111 / I11i1i11i1I % i11iIiiIii * Iiii
  if 95 - 95: OoooooooOO - OoOoo0 * oooO0oo0oOOOO + II1Ii1iI1i
if i1iiIiI1Ii1i == None or IIIII == None or len ( IIIII ) < 1 :
 o0 ( )
 if 10 - 10: IIii11I1 / i11iIiiIii
elif i1iiIiI1Ii1i == 1 :
 PREMIUM ( IIIII )
 if 92 - 92: Iiii . iIiiI1
elif i1iiIiI1Ii1i == 2 :
 IiIiIi ( IIIII )
 if 85 - 85: i1111 . iIiiI1
elif i1iiIiI1Ii1i == 3 :
 iiIIi1IiIi11 ( )
 if 78 - 78: OOooO * iIiiI1 + iIii1I11I1II1 + iIii1I11I1II1 / iIiiI1 . oO0o0o0ooO0oO
elif i1iiIiI1Ii1i == 4 :
 i1IIiiiii ( )
 if 97 - 97: OOooO / iIiiI1 % i1IIi % i1111
elif i1iiIiI1Ii1i == 5 :
 OOOO ( Ii11iii11I , IIIII , o0o0OOO0o0 )
 if 18 - 18: iIii1I11I1II1 % Iiii
elif i1iiIiI1Ii1i == 6 :
 i1Ii1i1I11Iii ( IIIII )
 if 95 - 95: OOooO + i11iIiiIii * iIiiI1 - i1IIi * iIiiI1 - iIii1I11I1II1
elif i1iiIiI1Ii1i == 7 :
 O0O0Oo00 ( IIIII , Ii11iii11I )
 if 75 - 75: OoooooooOO * OoOoo0
elif i1iiIiI1Ii1i == 8 :
 o0OOOo ( IIIII , Ii11iii11I )
 if 9 - 9: OoOoo0 - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
elif i1iiIiI1Ii1i == 9 :
 FIXREPOSADDONS ( IIIII )
 if 39 - 39: OoOoo0 * ooO0oo0oO0 + iIii1I11I1II1 - OoOoo0 + I11i1i11i1I
elif i1iiIiI1Ii1i == 10 :
 I1I ( )
 if 69 - 69: O0
elif i1iiIiI1Ii1i == 11 :
 iII1ii1 ( IIIII )
 if 85 - 85: OOooO / O0
elif i1iiIiI1Ii1i == 12 :
 O0O0Ooo ( )
 if 18 - 18: IIii11I1 % O0 * i1111
elif i1iiIiI1Ii1i == 13 :
 ii111111I1iII ( )
 if 62 - 62: iIiiI1 . OoOoo0 . OoooooooOO
elif i1iiIiI1Ii1i == 14 :
 iIIi1i1 ( IIIII )
 if 11 - 11: I11i1i11i1I / Iiii
elif i1iiIiI1Ii1i == 15 :
 OO ( )
 if 73 - 73: i1IIi / i11iIiiIii
elif i1iiIiI1Ii1i == 16 :
 iIi1i1iIi1iI ( IIIII , Ii11iii11I )
 if 58 - 58: ooO0oo0oO0 . II111iiii + i1IIi11111i - i11iIiiIii / II111iiii / O0
elif i1iiIiI1Ii1i == 17 :
 IiIii1i111 ( IIIII , Ii11iii11I )
 if 85 - 85: II1Ii1iI1i + I11i1i11i1I
elif i1iiIiI1Ii1i == 18 :
 oO0OoO00o ( )
 if 10 - 10: OoOoo0 / i111I + II1Ii1iI1i / i1IIi
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
