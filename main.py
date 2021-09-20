import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://www.whexy.com/feed/feed.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w+') as f:
    f.write(r'''
**Hooray! You found me.**

[![Blog](https://img.shields.io/badge/Blog-F0773A?style=flat-square&logo=firefox-browser&logoColor=white)](https://www.whexy.com)
[![Linkedin](https://img.shields.io/badge/-LinkedIn-1568BF?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/whexy)
[![Email](https://img.shields.io/badge/-Email-E8453C?style=flat-square&logo=Gmail&logoColor=white)](mailto:gwhexy@gmail.com)

The name is SHI Wenxuan, I use he/him/his pronouns. 

- I work on topics related to *system*. I fight with the compiler, linker, OS, firmware, bootloader, etc.
- I work on topics related to *security*. I keep eyes on the CVEs, vulnerabilities, malicious codes, etc.
- I know nothing about artificial intelligence.
- I use Vim. I love Rust. I prefer spaces rather than tab.

TAG: *System Security* (be in a lab), *Rustaceans* (fall in love with Rust), *Apple Guy* (write Swift), *music lover* ...

## My blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:updated', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://www.whexy.com/posts)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=whexy&theme=vue)
''')
