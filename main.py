from bs4 import BeautifulSoup
import requests
import datetime
import time
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


today_date = datetime.date.today().strftime("%m/%d/%Y").replace('-','/')

my_str = ''
answer = ''
new_list = []

cookies = {
    '_ga': 'GA1.2.1749201438.1633440146',
    'ASPSESSIONIDQURTSQRQ': 'BJHCLDBCHAPKBPMGFNNMGOBD',
    'ASPSESSIONIDAUQTRRRS': 'LMBMFCBCOKHINPLLPOAPGEPK',
    'ASPSESSIONIDQWRQRSQS': 'JHHMLFBCCOHHPJEJIBIFFKID',
    'ASPSESSIONIDCUSTTSSR': 'BBFEGDBCNAOBPKAALMJKPCMH',
    'ASPSESSIONIDAGACDCBB': 'PJJGMFBCEHMCPFPIHNCOOPKE',
    'ASPSESSIONIDAUCDSAQD': 'AILCIOLCGJKMEBFEBLJIMIMO',
    'ASPSESSIONIDQEDCTCSA': 'NBHNDMLCIPMKNOJEOOAMNOBA',
    'ASPSESSIONIDQGQSCTDT': 'PAIBDKHDGFIMDBKFHHKCNFEI',
    'loginid': '27786',
    'loginuser': '8090',
    'ASPSESSIONIDAGADCATT': 'OGEIMKODOMDBABOCGFLOEJAO',
    'ASPSESSIONIDAECDCBTS': 'HDCFGKODKKPGNAFBECBKFEJH',
    'ASPSESSIONIDSGBCCDST': 'LOGJENODGINBEMHACFBFFKBP',
    'ASPSESSIONIDCUADDARS': 'CMJOONODBFEHNPAGCFNGANNH',
    'ASPSESSIONIDQGACCDTR': 'MMEHGLODJHDKDDCKGNEDDJAK',
    'ASPSESSIONIDCESDQCCD': 'NLKFDGJADEKODAAILBJGIIBM',
    'ASPSESSIONIDSUBAQBCA': 'NHDBLCJAOCNIMJKJILILFGFO',
    'ASPSESSIONIDSUAAQACB': 'LJMOKDJAEOILDCIMJKFHNFHJ',
    'ASPSESSIONIDQWQRAQDQ': 'KBLLIONDNDPLPCLBBEFPENAH',
    'ASPSESSIONIDCEAARSCR': 'JOAAACODFLJCJOABCFEBCOMK',
    '_gid': 'GA1.2.1034576230.1635922045',
    '_gat_gtag_UA_9515119_2': '1',
    'GPSID': '1689729422250118145103389_27786_20211103024840',
    'ASPSESSIONIDSEABADAD': 'KGLMMHIADNPBAADDMJHAHEOP',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://www8.sylectus.com',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://www8.sylectus.com/I16_vehicleaddressbook.asp',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
}

data = {
  'secondsleft': '291',
  'vabcode': '',
  'city': '',
  'state': ' ',
  'trucksize': '0',
  'currentstatus': 'A',
  'availstatus': 'B',
  'qualcommmct': '',
  'licenseplate': '',
  'txtvinnumber': '',
  'driverid': '0',
  'ownerid': '0',
  'selliftgate': '',
  'status': 'Y',
  'airride': '',
  'commandbutton': 'SEARCH',
  'refreshrate': '300',
  'sel_reccount': '0',
  'sel_icontype': 'box',
  'sel_maptype': 'auto',
  'sortby': 'UNITNO',
  'sortorder': 'ASC'
}

response = requests.post('https://www8.sylectus.com/I16_vehicleaddressbook.asp', headers=headers, cookies=cookies, data=data)
soup = BeautifulSoup(response.text, 'lxml')


# def send_test_mail():
#     sender_email = "keern1922@gmail.com"
#     receiver_email = "zhenia.k@auraegaming.com"
#
#     msg = MIMEMultipart()
#     msg['Subject'] = '[Sylectus]'
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#
#     csv = MIMEApplication(open("cms.csv", 'rb').read())
#     csv.add_header('Content-Disposition', 'attachment', filename="cms.csv")
#     msg.attach(csv)
#
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
#             smtpObj.ehlo()
#             smtpObj.starttls()
#             smtpObj.login("keern1922@gmail.com", "Kernleon1")
#             smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
#     except Exception as e:
#         print(e)





def get_html(url):
    response = requests.get(url, headers=headers, cookies=cookies)
    return response.text



def write_csv(data):
    with open('cms.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(('Time: ', data['Time'],
                         ' Out of Service: ', data['Out of Service'],
                         ' On a Load: ', data['On a Load'],
                         ' Avaible: ', data['Avaible'],
                         ' Total: ', data['Total']))



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('body').find_all('table')
    #Преобразую инфу в строки и чищу строку оставляя только цифры
    trs3 = trs[3].find_all('tr')
    Inserv_OOS = trs3[0].text
    Onload_Unconf = trs3[1].text
    mystr = ''.join(Inserv_OOS)
    Inserv_oos_digits = list(mystr.replace('- In. Serv.', ' ').replace('- OOS', '').split())
    mystr2 = ''.join(Onload_Unconf)
    Onload_Unconf_digits = list(mystr2.replace('- On Load', ' ').replace('- Unconf.', '').split())
    #Преобразую инфу в строки и чищу строку оставляя только цифры
    trs4 = trs[4].find_all('tr')
    avail = trs4[0].text
    mystr3 = ''.join(avail)
    avail_digits = list(mystr3.replace('- Avail.', ' ').replace('- Unavail.', '').split())
    what_time_is_now = time.ctime()




def avaible():
    outserv = 0
    oos = 0
    onaload = 0
    counter = 1
    avaible = 0

    for i in range(10):
        try:
            tr = soup.find('body').find('tr', id='tr_'f'{counter}')
            td = tr.find_all('td')
            trs = soup.find('body').find_all('table')
            trs3 = trs[3].find_all('tr')
            Inserv_OOS = trs3[0].text
            mystr = ''.join(Inserv_OOS)
            outserv = list(mystr.replace('- In. Serv.', ' ').replace('- OOS', '').split())
        except:
            pass
            continue

        answer = str(td[5].text).replace('Free space = 0.00 linear ft.', '').split()
        status = str(td[4].text).replace('StatusPlanner', '')
        status2 = str(td[3].text).replace('StatusPlanner', '')


        time_sec = answer[-1]
        my_str = answer[-2]
        counter += 1

        try:
            time_of_driver_MDYYYY = my_str.replace(f'{my_str[0]}', '').replace(f'{my_str[1]}', '')
            if "SERVICE" in status and time_of_driver_MDYYYY == today_date and time_sec != "00:00":
                avaible += 1
            elif "ON A LOAD" in status2:
                onaload += 1
        except:
            pass
        continue

    data = {'Time': today_date,
            'Out of Service': counter - 1 - onaload - avaible,
            'On a Load': onaload,
            'Avaible': avaible,
            'Total': counter - 1
            }

    write_csv(data)

    print(avaible)
    print(oos)
    print(onaload)





def main():
    startTime = datetime.datetime.now()
    url = 'https://www8.sylectus.com/I16_vehicleaddressbook.asp'
    get_page_data(get_html(url))
    avaible()
    # send_test_mail()
    print(datetime.datetime.now() - startTime)



main()





