import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://www.whexy.com/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w+') as f:
    f.write(r'''
```
+--------------------------------------------------+----------------------------+
|                       GLGLGKKi                   |                            |
|                    EGGGGGLDGGGGGGGE              |                            |
|            ,DEDGEKKEGDDGGGGGGGGDEKKEDt           |                            |
|        GDEGGDDGGGDEKKKEEDGGDDDEEDDEKKKEGtGG;     |              t             |
|      EEGGGDEEKKKGGGDDKWEEDDDDEEKKWWKKWWWWW;      |        t ttttttttt t       |
|     KEEEEEDDDEKKKDDDDEEKKEEEEK#DGGGGLGGGGE       |      ttttttjjjjjjjjjj      |
|    WKKEEWWEEDEEWKEEDEEEKEEKKKDDDDDDDDDDGGDDE     |     jjjjjjjjjjjjjjjjjjj    |
|   .KKKWKKEKKEEEKWKEEEEKEEEWKEEEEEEEEEEEEEEEEK    |    jjjjjjjj#jjjjffffffff   |
|   .WWKKWWKKKKKEEWKKKKEEEEWKKKKKKKWKKWWWWWWWKKK   |    ffffffff##ff##fffffff   |
|    W#WWKKWWWWWWKWWWWKEKKWEEWWWWWWWWWWWWWWWWWWW.  |   ffj fffff#fffffffDf Dff  |
|    EEEKWWW;,,,::,tKWWWWWWKWWWWWWWWW##WWWWWWWWWD  |     f   ff       LL  D     |
|   DKEEEE;;,,,::::::........:::::,itfWWWWWWWWWWE  |           GG   Gi          |
|   jKEEfi;,,,:::::............:::::,,,;;WWWWWWWK  |                            |
|    WKKi;;,,,:::::.............::::,,,;;;KKKWKW   |                            |
|   .KDii;;iGGGf,::::.......::::::::,,,;;ifEEEK.   |          Rustaceans        |
|    WKtiDDt:,,,,,,,,:::::::::GGGGGDi,,;;iiEEEKf   |                            |
|    Ktii;;,,,,,,,,,,,,::,,,,,,,,,,:tDD;;iiEKKKD   |                            |
|    Kji;;,,,,,,,,;;;,,,,,,;;,,,,,,,,,;DiitKKWW    +----------------------------+
|  ,,Kti;,,K###t;;;;;,,:,,;;;;,;,,,,,,,;iitKKWi    |                            |
|  L,fti;j Ki ##E#;;;,:::,;;;;f####f,,,;itjGKW     |                            |
|  ;jjt;:..E####DiKii,:.:;i;# K K#WE #,;itjfW      |               ttt          |
|    jt;,::.EGLtE..i;:..:;ij.tE####G .W;itjf,,t    |              ttti          |
|   tji;,::...::::,,,:..:,,,:.,DLjj..:,;ttjjtt;    |        ,ttt     ttt.       |
|   ijii;,::::::::,,;,,,,,,:::......::;itjjf  ,    |      ttttttttttttttttt     |
|    jti;;,,::::::;;:..:;;::::....::,,;itjjj,      |    :;;;;;;;;;;;;;;;;,      |
|    ftii;;,,,:::,it,::,it,::::::::,,;iitjfi       |    ttttttttttttttttt       |
|    ;tti;;;,,,:::,:;tft,,::::::,,,;;iitjffL:      |    ttttttttttttttttt       |
|     jtii;;,,,,,,,:....::,:::,,,,;;iittf          |    tLLLLLLLLLLLLLLLLL      |
|     jjtii;;,,,;;fGKWEfti,,,,,,;;;iittf           |     LLLLLLLLLLLLLLLLLLL    |
|      Ljtii;;,,;iWWHEXYWWf;,,,;;;iitjj            |      LLLLLLLLLLLLLLLLG     |
|       .jttii;;;iifjjjfLi;,,;;;iittjf             |       .fffffffffffff       |
|         tjttii;;ifttttji;;;iiittjf               |                            |
|           .fttiiiiiiiiiiiiitjjfi                 |                            |
|              ;jjtttttttttjjL.                    |          Apple Fan         |
|                                                  |                            |
+--------------------------------------------------+----------------------------+
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
