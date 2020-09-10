import requests

class Fetcher:
    def params(self,ploads):
        self.params = ploads
        return self
    def data(self,ploads):
        self.data = ploads
        return self
    def headers(self,headers):
        self.headers = headers
        return self
    def Post(self,url):
        try:
            r = requests.post(url,data=self.data,headers=self.headers)
            # print(json.dumps(r.json(),indent=4))
            return r
        except:
            print("check your data,url and headers post")
    def Get(self,url):
        try:
            r = requests.get(url,params=self.params)
            # print(r.text)
            return r
        except:
            print("check your params and url get")
    def Delete(self,url):
        try:
            r = requests.delete(url, data = self.data)
            # print(r.json())
            return r
        except:
            print("check your data and url")
        

            

Fetcher = Fetcher()

# GET
payload = {'name': 'subhan dinda putra'}
r = Fetcher.params(payload).Get('https://httpbin.org/get')
print(r.text)

# POST
headers = {'content-type': 'application/json'}
r = Fetcher.data(payload).headers(headers).Post('https://httpbin.org/post')
# print(json.dumps(r.json(),indent=4))

# DELETE
r = Fetcher.Delete("https://httpbin.org/delete")
# print(json.dumps(r.json(),indent=4))