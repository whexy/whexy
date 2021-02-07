import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://www.whexy.com/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w+') as f:
    f.write(r'''
```
      ___           ___           ___           ___
     /__/\         /__/\         /  /\         /__/|          ___
    _\_ \:\        \  \:\       /  /:/_       |  |:|         /__/|
   /__/\ \:\        \__\:\     /  /:/ /\      |  |:|        |  |:|
  _\_ \:\ \:\   ___ /  /::\   /  /:/ /:/_   __|__|:|        |  |:|
 /__/\ \:\ \:\ /__/\  /:/\:\ /__/:/ /:/ /\ /__/::::\____  __|__|:|
 \  \:\ \:\/:/ \  \:\/:/__\/ \  \:\/:/ /:/    ~\~~\::::/ /__/::::\
  \  \:\ \::/   \  \::/       \  \::/ /:/      |~~|:|~~     ~\~~\:\
   \  \:\/:/     \  \:\        \  \:\/:/       |  |:|         \  \:\
    \  \::/       \  \:\        \  \::/        |  |:|          \__\/
     \__\/         \__\/         \__\/         |__|/
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
