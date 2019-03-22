import requests
import json
from lxml import etree
import time
import re
import csv
import datetime
def fangjian(room_id):
    url="http://hotels.ctrip.com/Domestic/tool/AjaxHote1RoomListForDetai1.aspx?hotel=%s" % (room_id)
    headers={
        "Connection":"keep-alive",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
        "If-Modified-Since": "Thu, 01 Jan 1970 00:00:00 GMT",
        "Referer": "http://hotels.ctrip.com/hotel/%s.html" % (room_id),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
    }
    a=0
    html=requests.get(url,headers=headers)
    json_html=json.loads(html.text)
    L=[]
    string=json_html["html"]
    html1 = etree.HTML(string)
    room_name = html1.xpath('//*[@class="room_unfold J_show_room_detail"]/text()')
    room_price = html1.xpath('//*[@class="base_price"]/text()')
    for i in room_name:
        i=(i.replace("\n",'')).replace(" ","")
        if i != "" and a<2:
            L.append(i)
            L.append(room_price[a])
            a+=1
        elif a==2:
            break
    return L

def jiudian_name(startpage,endpage):
    L_name=[] #存放每个酒店名称
    L_room=[] #存放每个
    # with open('D://携程/500酒店数据.csv', 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file,dialect='excel')
    for i in range(startpage,endpage):
        headers={
            "Connection":"keep-alive",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
            "If-Modified-Since": "Thu, 01 Jan 1970 00:00:00 GMT",
            "Referer": "https://hotels.ctrip.com/hotel/shanghai2",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
        }
        date={
                "__VIEWSTATEGENERATOR": "DB1FBB6D",
                "cityName": "%E4%B8%8A%E6%B5%B7",
                "StartTime": "2019-03-21",
                "DepTime": "2019-03-22",
                "RoomGuestCount": "1,1,0",
                "txtkeyword": "",
                "Resource": "",
                "Room": "",
                "Paymentterm": "",
                "BRev": "",
                "Minstate": "",
                "PromoteType": "",
                "PromoteDate": "",
                "operationtype": "NEWHOTELORDER",
                "PromoteStartDate": "",
                "PromoteEndDate": "",
                "OrderID": "",
                "RoomNum": "",
                "IsOnlyAirHotel": "F",
                "cityId": "2",
                "cityPY": "shanghai",
                "cityCode": "021",
                "cityLat": "31.2363508011",
                "cityLng": "121.4802384079",
                "positionArea": "",
                "positionId": "",
                "hotelposition": "",
                "keyword": "",
                "hotelId": "",
                "htlPageView": "0",
                "hotelType": "F",
                "hasPKGHotel": "F",
                "requestTravelMoney": "F",
                "isusergiftcard": "F",
                "useFG": "F",
                "HotelEquipment": "",
                "priceRange": "-2",
                "hotelBrandId": "",
                "promotion": "F",
                "prepay": "F",
                "IsCanReserve": "F",
                "OrderBy": "99",
                "OrderType": "",
                "k1": "",
                "k2": "",
                "CorpPayType": "",
                "viewType": "",
                "checkIn": "2019-03-21",
                "checkOut": "2019-03-22",
                "DealSale": "",
                "ulogin": "",
                "hidTestLat": "0%7C0",
                "AllHotelIds": "4399431%2C393916%2C479628%2C473770%2C427622%2C419539%2C1763033%2C21349561%2C12782071%2C6338488%2C8178829%2C441585%2C22273655%2C453317%2C2895314%2C17538562%2C1496646%2C12603011%2C16313232%2C25508399%2C1102954%2C23852115%2C436526%2C15018492%2C16946069",
                "psid": "",
                "isfromlist": "T",
                "ubt_price_key": "htl_search_result_promotion",
                "showwindow": "",
                "defaultcoupon": "",
                "isHuaZhu": "False",
                "hotelPriceLow": "",
                "unBookHotelTraceCode": "",
                "showTipFlg": "",
                "traceAdContextId":"v2_H4sIAAAAAAAAAC3NvU0DQRCGYTujBkLkCLHS%2FM83Dmnk5F1zMTVQA5GboCMKoAqb28tGj1598%2FT98%2Fd1a8%2B%2Fx4I7L%2BNzLMblWguf5a1KYRuCE5BdPc035XSFh2zMRMExnUnKbWfRzMmaIOM5EpW6qaYZcv%2FnmKmyJ3PyPqEeMzYN9T0O9omiRACmGolM5ZRw0D%2B%2FHF5POjg%2FVrEWNbzZGr1VXrmxjYteFL2r0vF8QsdV0KsVkTUjXh%2BXU1vDMJAmWfF%2BuAPjyee2OgEAAA%3D%3D",
                "allianceid":"0",
                "sid": "0",
                "pyramidHotels": "419539_6%7C8178829_11%7C17538562_16%7C1102954_21",
                "hotelIds": "4399431_1_1,393916_2_1,479628_3_1,473770_4_1,427622_5_1,419539_6_1,1763033_7_1,21349561_8_1,12782071_9_1,6338488_10_1,8178829_11_1,441585_12_1,22273655_13_1,453317_14_1,2895314_15_1,17538562_16_1,1496646_17_1,12603011_18_1,16313232_19_1,25508399_20_1,1102954_21_1,23852115_22_1,436526_23_1,15018492_24_1,16946069_25_1",
                "markType": "0",
                "zone": "",
                "location": "",
                "type": "",
                "brand": "",
                "group": "",
                "feature": "",
                "equip": "",
                "bed": "",
                "breakfast": "",
                "other": "",
                "star": "",
                "sl": "",
                "s": "",
                "l": "",
                "price": "",
                "a": "0",
                "keywordLat": "",
                "keywordLon": "",
                "contrast": "0",
                "PaymentType":"", 
                "CtripService":"", 
                "promotionf":"", 
                "allpoint":"", 
                "contyped": "0",
                "productcode":"",
                "page": "%s" % startpage    
            }

        html = requests.post('https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx',headers=headers,data=date)
        json_html=json.loads(html.text)
        string=json_html["hotelList"]
        etree1 = etree.HTML(string)
        jd_name = etree1.xpath('//*[@class="hotel_name"]/a/@title')
        jd_id = etree1.xpath('//*[@class="hotel_name"]/a/@href')
        for x in range(25):
            L_name.append(jd_name[x])
        pattern = re.compile(r'/hotel/(.+?).html')
        c=0
        for y in jd_id:
            id = pattern.findall(y)
            L2 = fangjian(id[0])
            L_room.append([L_name[c]]+L2)
            c+=1
            time.sleep(0.2)
    print(L_room)
    print(len(L_room))
starttime = datetime.datetime.now()
jiudian_name(0,20)
endtime = datetime.datetime.now()
print(endtime - starttime)