import requests
import csv
import xml.etree.ElementTree as ET

def get_standings():
    # https://scottrasmussen.com/2020-democratic-candidate-social-media-analysis/
    link = 'https://www.predictit.org/api/marketdata/all'

    resp = requests.get(link)

    # with open('pd_mkts.xml', 'wb') as f:
    #     f.write(resp.content)



def parse_xml(xmlfile):

    tree = ET.parse(xmlfile)

    root = tree.getroot()

    # for item in root.findall('markets'):
    #     # value = item.get('id')
    #     print(item)


    # while True:
    #     page = urllib.request.urlopen(link)
    #     soup = bs(page, 'html.parser')
    #     refresh_date = soup.body.findAll(text='last updated at 04:30EST on 07-17-2019')
    #     if len(refresh_date) > 0:
    #         break
    #     else:
    #         print("Refresh date incorrect")
    #         pause.seconds(15)
    #
    # print("Refresh date good continuing")
    #
    # table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="demtable")
    # rows = table.findAll(lambda tag: tag.name=='tr')
    # for i in range(0, len(rows)):
    #     if rows[i].find('td').text == "Bernie Sanders":
    #         return i

# get_standings()
parse_xml('pd_mkts.xml')