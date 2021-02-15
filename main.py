import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://www.whexy.com/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w+') as f:
    f.write(r'''
```
                 GGLD:                          
                DGLLKKG                         
              :DGGLGEEGGLD                      
           LGKGEDGGGGGGGGDDf                    
        DEEDEKEDDDGGGGGDEKKED                   
     ;DEGGGGGKKEEEGGDDDEDEKKKD LG               
    DEDEEKKGGGEKWEEDDDEDEKKKWKDGK               
   EEDGDDKKKDGDDKEEDDEEKWWWKW##W                
   EDDDDDEKKEDDDEKEEEEKWGGGLGGG;                
   KKWEEDEEKKDDDEKEEEKEGGGGGGGGGK               
  KKKEWKEEEWKEDEEKEEKKDDDDDDDDDDEt              
  KKWKEWEEEKKEEEEEEKWEEEEEEEEEEEEE              
  WKKWKKWKEEKEEKKEEWKEEEKKKKKKKKKKf             
  WWKWWKKKKEWKKKEEKKWKKKKKKWWWWWWWW             
  #WWKWWWWWKWWWKEKWKWWWWWWWWWWWWWWK             
  KKWWKWWE#WWWWKKWKKWWWWWWWWWWWWWWWD            
  EEKWW;,,:::,iK##WWWWW#WW##WWWWWWWD            
 fEEED;,,,:::::.....:::,;jL#WWWWWWWE            
 LEDE;;,,:::::.......::::,,;G#WWWWWK            
  EEt;;,,:::..........::::,,;jWWWWK,            
  WEi;;,,::::..........:::,,;;KKWKW             
  KEi;;,,:::::........::::,,;;tEEKG             
  EDi;iGGGD::::.....::::::,,;;iEEK              
  KtiDDLtijLG,::..:::,fLf,,,;iiEEK              
  Ktit;,,,,,,,,::::,,iLDGGG,;iiEEKL             
  Kti;,,,,,,,;,,,,,,,,,,,,;D;iiEKWj             
  Kt;;,,,,,,;;,,,,,,,,,,,,,,GitEKW              
  Lt;;,,;;;;;;,,:,;;;,,,,,,,;itKKK              
:,jt;,####;;;;,::,;;;;;,,,,,;itKWW              
j:ji;D K,#Et;i,::,;;;;W#G;,,;itDW               
iijif.,W###,;i,::,i;EEEEKKE,;tjGW               
;:ji,..E##E:Ki,.:;it E ##K ;;tjfE,              
  ji,:.DWWf..i,.:;i: E###G.W;tjf:;              
 :ji,:::it.:,;:.:;i..E##DE.:;tjj,j              
 iti;::...::,,:.:,,:: DjD..,itjjj;              
 iti;,::::::,;,,,,,:::....:,itjj.,              
ftti;,,:::::,;::;,:::....:,;itjj,:              
  ji;;,,::::t,..,t::::.:::,;itjt                
  ji;;,,:::,j,::,j,::::::,;;ijji                
  jti;;,,::,;Lttfi,::::,,,;itjff                
  fti;;,,,::::;;,:::::,,,;;itf t                
  tti;;,,,:,::...::::,,,;;itjL                  
   jti;;,,,,,i;;,,,:,,,;;iitj                   
   jtii;,,;tEW##Dj;,,,,;;itjL                   
   jjti;;,;LWWWWWWj;,,;;iitj                    
    ftii;;,tDGGDEWi,,;;iitjL                    
     jtii;;iiitfLt;,;;iitjf                     
      ftii;;jitttt;;;iitjf                      
       jtiiiitjjt;;iittjf                       
        ftiiiiiiiiiitjf                         
         fjtttiiiittjL                          
           ;Lfjjjjf;                            
```

Hi. My name is [Wenxuan SHI](https://www.whexy.com), a junior student in SUSTech CSE.

TAG: *System Security* (be in a lab), *Rustaceans* (fall in love with Rust), *Apple Guy* (write Swift), *music lover* ...

## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:updated', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://www.whexy.com/writings)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=whexy&theme=vue)
''')
