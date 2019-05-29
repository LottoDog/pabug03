import requests, time
import urllib.parse
from lxml import etree

"""
*url  http://tieba.baidu.com/f?kw= &pn=
*xpath  
    页面帖子//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a/@href
    
    帖子图片
            说明贴吧图片不同二级页面图片元素节点不能用id用统一一致的class
            //*[@class="d_post_content j_d_post_content  clearfix"]/img/@src
          

"""

"""
key = input('请输入搜索的内容')
dic = {
    'wd': key,
    'pn': '10',
}
params = urllib.parse.urlencode(dic)
url += params
"""


class BaiduPicSpider(object):
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?"
        self.url2 = 'http://tieba.baidu.com'
        self.hearder = {
            'User-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"
        }

    def get_pic(self, url):
        req = requests.get(url, headers=self.hearder)
        req.encoding = 'utf-8'
        pic = req.content

        return pic
    def get_page(self, url):
        req = requests.get(url, headers=self.hearder)
        req.encoding = 'utf-8'
        html = req.text

        return html

    def html_parse(self, html):
        # 一级解析，获得所有本贴吧的所有帖子路径列表
        parse_html = etree.HTML(html)


        url_div_list = parse_html.xpath(
            '//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a/@href')
        print(url_div_list)
        self.html_pic(url_div_list)

    def html_pic(self, url_div_list):
        #重构二级url,调用get_page()
        for u2 in url_div_list:
            url = self.url2+u2
            time.sleep(0.5)
            html = self.get_page(url)
            #开始获取图片地址
            pu = etree.HTML(html)
            pics_url = pu.xpath('//*[@class="d_post_content j_d_post_content  clearfix"]/img/@src')
            #去除空列表
            if len(pics_url) == 0:
                del pics_url
                continue
            #获得图片地址第三次使用get_page()请求图片数据
            for url in pics_url:
                pic = self.get_pic(url)

                # filename = url[-1:-10:-1][::-1]
                filename = url[-10:]
                print(filename)
                with open(filename, 'wb') as f:
                    f.write(pic)


    def main(self):
        name = input("请输入爬去的贴吧：")
        start = int(input("起始页："))
        end = int(input("终止页："))

        for p in range(start, end + 1):
            params = urllib.parse.urlencode({
                "kw": name,
                "pn": 50 * (p - 1)
            })
            url = self.url + params
            print(url)
            html = self.get_page(url)
            self.html_parse(html)
            print("第%d页爬取成功" % p)


if __name__ == "__main__":
    p = BaiduPicSpider()
    p.main()
