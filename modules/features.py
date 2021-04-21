
'''
Module for adding features
'''

from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import re

def show_latest_cves():

    url = 'https://cve.circl.lu/'

    cve_req = requests.get(url)
    content = str(cve_req.content)
    soup = BeautifulSoup(content ,'html.parser')
    content = soup.findAll('tr')

    number_of_cves = 0
    cve_names = []
    for l in content:
        if number_of_cves >= 10 :
            break
        if l.get('id') :
            number_of_cves += 1
            cve_names.append(l.get('id'))

    cvss_pattern = '''<td data-type="CVSS" data-value="(.*?)">'''
    summary_pattern = '''<div rel=".*" title="(.*?)">'''
    published_at_pattern = '''<td data-type="PUBLISHED" data-value="(.*?)">'''

    cves_info = []

    for cve in cve_names:
        specific_cve = soup.find(id=cve)
        specific_cve = str(specific_cve)
        # data
        cve_name = cve
        cve_link = url + 'cve/' + cve
        cvss = re.findall(cvss_pattern ,specific_cve)
        if len(cvss) != 1:
            cvss = 'None'
        else:
            cvss = cvss[0]

        summary = re.findall(summary_pattern ,specific_cve)
        if len(summary) != 1:
            summary = 'Empty'
        else:
            summary = summary[0]

        published_at = re.findall(published_at_pattern ,specific_cve)
        if len(published_at) != 1:
            published_at = 'None'
        else:
            published_at = published_at[0]

        if summary:
            summary = summary[0:10] + '...'

        cves_info.append([cve_name ,cvss ,summary ,published_at ,cve_link])

    temp_text = tabulate(cves_info ,headers=['CVE_Name','CVSS','Summary','Published At','CVE_Link'])
    return temp_text
