import requests
from lxml import etree

'''
    1分析页面
    
    一级
    //*[@id="leftContent"]
    //*[@id="leftContent"]/ul/li[1]
    //*[@id="leftContent"]/ul/li[1]/div/div[1]
    //*[@id="leftContent"]/ul/li[1]
    //*[@id="leftContent"]/ul/li[1]/div/div[4]/div[2]/div[2]/span
    二级
    name://*[@id="leftContent"]/ul/li[1]/div/div[1]/a
    总价：//*[@id="leftContent"]/ul/li[1]/div/div[4]/div[2]/div[1]/span
    单价：//*[@id="leftContent"]/ul/li[1]/div/div[4]/div[2]/div[2]/span
    
    
'''


class LianJiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}'
        self.headers = {
            'User-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"

        }

    def get_page(self, url):
        req = requests.get(url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        li_list = parse_html.xpath('//*[@id="leftContent"]/u;/li/[@class="clear LOGCLICKDATA"]')
        print(li_list)
        for li in li_list:

            name = li.xpath('./div/div[1]/a/text()')[0].strip()
            tprice = li.xpath('./div/div[0]/a/text()')[0].strip()
            sprice = li.xpath('./div/div[4]/div[2]/div[1]/span/text()')[0].strip()

            house_dic = {
                "house_name": name,
                "total_price": tprice,
                "single_price": sprice
            }
            print(house_dic)

    def main(self):
        start = int(input("起始页："))
        end = int(input("终止页"))
        for p in range(start, end+1):
            url = self.url.format(str(p))
            self.get_page(url)
            print("第%d页爬取成功" % p)


if __name__ == "__main__":
    s = LianJiaSpider()
    s.main()
