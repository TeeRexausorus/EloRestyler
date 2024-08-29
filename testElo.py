import http.client
import json
from html2image import Html2Image
from Levenshtein import distance
from templates import templatePole, templateLine, templateClock, headerHtml, messages, prompt, promptBasicMessage, templateAi
import google.generativeai as genai

gemini_api = "AIzaSyDojmcOLgdF1xbqTyspJMjYCQhO-u-ExFY"
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel('gemini-1.5-pro-latest')
hti = Html2Image(size=(1630, 650))


class Plat:
    def __init__(self, name, price, info1, info2):
        self.name = name
        self.price = price
        self.info1 = info1
        self.info2 = info2

    def __hash__(self):
        return hash(('name', self.name, 'price', self.price, 'info1', self.info1, 'info2', self.info2))

    def __eq__(self, other):
        return distance(self.name, other.name) <= 2


def getData():
    conn = http.client.HTTPSConnection("toast-js.ew.r.appspot.com")
    payload = ''
    headers = {}
    conn.request("GET", "/coteresto?key=1fhVfd7RFwj3901K83g9wQXbsAHdsOILibUh2PWTfzQ8", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data


def generate_stuff_yolo():
    global line, dateMenu, sumDate, dateForFilename
    for line in loadedData[0]:
        dateMenu = str(line['dateUs'])
        sumDate = int(dateMenu[:4]) + int(dateMenu[4:6]) + int(dateMenu[6:])
        dateForFilename = dateMenu[6:] + '_' + dateMenu[4:6] + '_' + dateMenu[:4]
        dateMenu = dateMenu[6:] + '/' + dateMenu[4:6] + '/' + dateMenu[:4]
        if line['accompagnement'] == 'TRUE':
            poles['accompagnement'] = []
            poles['accompagnement'].append(Plat(line['nom'].strip(), '', line['info1'].strip(), line['info2'].strip()))
        if line['pole'] not in poles:
            poles[line['pole']] = []
        if line['nom'] != '' and line['accompagnement'] == 'FALSE':
            poles[line['pole']].append(
                Plat(line['nom'].split(':')[0].strip().lower(), line['prix'].lower(), line['info1'].lower(),
                     line['info2'].lower()))
    if 'Cuisine du marché' in poles:
        poles['Cuisine du marché'] = [plat for plat in poles['Cuisine du marché'] if plat not in poles['Asado']]


def generate_html():
    global polesHtml
    polesHtml = headerHtml
    prompts = []
    for key in poles:
        lineHtml = ''
        for plat in poles[key]:
            lineHtml = lineHtml + templateLine.format(title=plat.name, subtitle=plat.info1, price=plat.price)
            if plat.name != '':
                prompts.append(prompt.format(plat=plat.name, subtitle=plat.info1))
        polesHtml += templatePole.format(pole=key, line=lineHtml)
    polesHtml += '</div>'
    print(prompts)
    #polesHtml += templateAi.format(text=ask_gemini(prompts).replace('\r', '<br/>').replace('\n', '<br/>'))
    polesHtml += templateClock.format(day=dateMenu, message=messages[sumDate % (len(messages))])
    polesHtml += '</body>'


def ask_gemini(prompts):
    query_prompt = promptBasicMessage + '\r\n' + '\r\n'.join(prompts)
    return model.generate_content(query_prompt).text



if __name__ == '__main__':
    data = getData()
    poles = {"Asado": [], "Impasto": []}
    loadingData = ""
    dateMenu = ""
    dateForFilename = ""

    for line in data.decode("utf-8").splitlines():
        if "var loadingData" in line:
            loadingData = line
            break
    loadedData = json.loads(loadingData.split("=")[1])
    sumDate = 0

    generate_stuff_yolo()
    generate_html()
    with open('test.html', 'w') as f:
        f.write(polesHtml)
    hti.screenshot(html_file="test.html", css_file='testElo.css',
                   save_as='menu_' + dateForFilename + '.png')
    ''' hti.screenshot(html_str=polesHtml, css_file='testElo.css',
                   save_as='latest.png')'''
