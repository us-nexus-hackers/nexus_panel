ó
ÿc           @   sv   e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d Z d   Z	 d   Z
 e
   d S(   i    iÿÿÿÿNs¸   [1;94m
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
[93m TYPE    : SUBDOMAIN-API
[1;32m------------------------------------------
c          C   sÁ   t  j d  t GHHt d  }  t j d  Hd |  GHd GHd GHt j d  d GHHd	 |  } yQ t j |  } | j } | GHHd
 GHHt d  } H| d k r­ t  j d  n  Wn d GHn Xd  S(   Nt   clears,   [1;31m>> [1;32mEnter Domain Name : [1;35mg      à?s&        [1;31m>> [1;32mTARGET : [1;33ms$        [1;31m>> [1;32mSCANNING......sR        [1;31m>> [1;32mNOTE : [1;31mIf You Face Any Problem While Scanning Use VPNg      @s   [1;32ms+   https://api.hackertarget.com/hostsearch/?q=s/     [1;31m<<< [1;33mThanks For Using [1;31m>>>s8   [1;31m[+] [1;34mPRESS ENTER TO GO BACK MENU [1;31m[+]t    s   cd .. && python2 n-web.pys    [1;31m[+] Something Is Wrong ! (	   t   ost   systemt   logot	   raw_inputt   timet   sleept   nabilt   gett   text(   t   domaint   urlt   reqt   ret   user(    (    s   subdomain-api.pyt   intro   s4    	
	c          C   se   t  j d  t GHHd GHd GHHt d  }  |  d k r@ t   n! |  d k r\ t  j d  n d GHd  S(	   NR    s@   [1;31m[1] [1;34m>> [1;32mSub-Domain-Lookup [1;31m(Using API)s>   [1;31m[2] [1;34m>> [1;32mSub-Domain-Lookup [1;31m(Default)s,   [1;31m>> [1;33mEnter Your Choice : [1;36mt   1t   2s   python3 sub-domain.pys   [1;31m[+] Input Correctly(   R   R   R   R   R   (   t   user_choice(    (    s   subdomain-api.pyt   main<   s    
(   t   Falset   foot   bart   requestsR   R   t   sysR   R   R   R   (    (    (    s   subdomain-api.pyt   <module>   s   
$	 	