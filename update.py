# -*- coding: utf-8 -*
import requests
import xml.etree.ElementTree as ET

with open('README.md', 'w') as f:
    f.write(r'''
<h3 align="center">👋 Hello! I'm Yibo.</h3>

<p align="center">
  <a href="https://haoyizebo.com">Blog</a> •
  <a href="https://github.com/zhaoyibo">GitHub</a>
</p>

### Github Statistics

![Stats](https://github-readme-stats.vercel.app/api?username=zhaoyibo&show_icons=true&layout=compact&count_private=true&hide_title=true&theme=default&)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=zhaoyibo&layout=compact&count_private=true&theme=default&hide=css)

### Latest blog posts

''')
    ret = requests.get('https://haoyizebo.com/atom.xml')
    ret.encoding='utf-8'
    feed = ret.text
    root = ET.fromstring(feed)
    nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://haoyizebo.com/archives/)
''')