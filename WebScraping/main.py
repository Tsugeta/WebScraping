import requests
from bs4 import BeautifulSoup
import json
headers = {
        "User-agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

def number_of_pages():
    url = "https://www.koton.com/tr/kadin/giyim/elbise/c/M01-C02-N01-AK103?q=%3Arelevance&psize=192&page=0"
    headers = {
        "User-agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    r = requests.get(url,headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")

    page = soup.find("div", {"class": "paging"}).find_all("li")[-2].text
    return page


'''
url2=[]
def all_prod_url():
   for page2 in range(0,int(number_of_pages())):
       url = "https://www.koton.com/tr/kadin/giyim/elbise/c/M01-C02-N01-AK103?q=%3Arelevance&psize=192&page=" + str(
           page2) + ""
       headers = {
           "User-agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
       r = requests.get(url, headers=headers)
       soup = BeautifulSoup(r.content, "html.parser")
       all_prods_in_page = soup.find_all("div", {"class": "product-item plp-small-images"})
       for prod in all_prods_in_page:
           prod_code=prod.get("data-product")
           url2.append("https://www.koton.com/tr/kadin-kolsuz-midi-pencere-detayli-elbise/p/" + prod_code + "?productPosition=0&listName=Kad%C4%B1n%20Abiye%20ve%20Kad%C4%B1n%20Elbise%20Modelleri%20ve%20Fiyatlar%C4%B1#tab-1")
       big_size_code=soup.find("div",{"class":"product-item plp-small-images big-size"}).get("data-product")
       url2.append("https://www.koton.com/tr/kadin-kolsuz-midi-pencere-detayli-elbise/p/" + big_size_code + "?productPosition=0&listName=Kad%C4%B1n%20Abiye%20ve%20Kad%C4%B1n%20Elbise%20Modelleri%20ve%20Fiyatlar%C4%B1#tab-1")

   return url2

prods = []
def prod_info():

   for url in all_prod_url():

       session=requests.session()
       session.max_redirects=3
       r=session.get(url,headers=headers)
       soup=BeautifulSoup(r.content,"html.parser")
       prod_name=soup.find("h1").text
       prod_price=soup.find("span", {"class": ["normalPrice", "newPrice"]}).text.strip()
       prod_image=soup.find("div",{"class":"left-content"}).find_all("p",{"class":"alt-text"})[0].text.strip()
       prod_color=soup.find_all("span", {"class": "title"})[1].text.strip()[6:]
       prod_detail=soup.find("div",{"class":"left-content"}).find_all("p",{"class":"alt-text"})[0].text.strip()
       prod_materiel=soup.find("div",{"class":"left-content"}).find_all("p",{"class":"alt-text"})[1].text.strip()
       try:
           prod_model=soup.find("div",{"class":"left-content"}).find_all("p",{"class":"alt-text"})[2].text.strip().replace("\xa0"," ")
       except:
           prod_model=" "
       size_feature=soup.find_all("a", {"stocklevelstatus": ["lowStock", "inStock"]})
       prod_size=[]
       prod_stock=[]
       for size in size_feature:
           prod_size.append(size.text)
           prod_stock.append(size.get("stocklevel"))
       prod_dic={"UrunAd":prod_name,"UrunFiyat":prod_price,"Renk":prod_color,"Beden":prod_size,"Stok":prod_stock,"UrunDetay":prod_detail,"UrunMateryal":prod_materiel,"UrunModel":prod_model}
       prods.append(prod_dic)
       session.close()

   return prods


with open("Urunler.json", "w") as f:
    json.dump(prod_info(), f)
    
    '''
with open("Urunler.json") as f:
    veriler=json.load(f)
    


for i in range(0,2356):
   print((veriler)[i])


