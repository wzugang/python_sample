```

一、python自带库----urllib2
python自带库urllib2使用的比较多，简单使用如下：
import urllib2
response = urllib2.urlopen('http://localhost:8080/jenkins/api/json?pretty=true')
print response.read() 
简单的get请求
import urllib2
import urllib
post_data = urllib.urlencode({})
response = urllib2.urlopen('http://localhost:8080/, post_data)
print response.read()
print response.getheaders() 
这就是最简单的urllib2发送post例子。代码比较多
二、python自带库--httplib
httplib是一个相对底层的http请求模块，urlib就是基于httplib封装的。简单使用如下：
import httplib
conn = httplib.HTTPConnection("www.python.org")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
data2 = r2.read()
conn.close()
简单的get请求
我们再来看post请求
import httplib, urllib
params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = httplib.HTTPConnection("bugs.python.org")
conn.request("POST", "", params, headers)
response = conn.getresponse()
data = response.read()
print data
conn.close()
是不是觉得太复杂了。每次写还得再翻文档，看看第三种吧
三、第三方库--requests
发请get请求超级简单：
print requests.get('http://localhost:8080).text
就一句话，再来看看post请求

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text
也很简单。
再看看如果要认证：

url = 'http://localhost:8080'
r = requests.post(url, data={}, auth=HTTPBasicAuth('admin', 'admin'))
print r.status_code
print r.headers
print r.reason
是不是比urllib2更简单多了吧，且requests自带json解析。这点非常棒
python中的http请求 
import urllib
params = urllib.urlencode({key:value,key:value})
resultHtml = urllib.urlopen('[API or 网址]',params)
result = resultHtml.read()
print result

```
