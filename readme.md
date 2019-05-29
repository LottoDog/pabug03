#D03
#链家二手房案例（Xpath）
    1分析页面
    //*[@id="leftContent"]
    
    //*[@id="leftContent"]/ul/li[1]
    
#有密码验证的web爬取-或异步响应

    requests.get(url, params=params)
    
    之前的做法
    url+‘编码处理过的字符串’
    
    查询参数params={}
    
    url = http://www.baidu.com/f?
    headers = {
         'User-agent': "xxxxx"
    }
    params = {
         'kw':'哈哈',
         'pn': '20'
    }
    requests.get(url, params=params, headers=headers)
    会自动转为标准格式,中文也会进行编码
    'http://www.baidu.com/f?kw=xx&pn=xx'
    