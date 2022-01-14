import asyncio
from PySide6.QtCore import QThread, Signal
import aiohttp
import configs


async def fetch(session, endpoint, params, headers, data, json, method):
    try:
        if method == 'GET':
            async with session.get(endpoint, headers=headers, params=params, data=data, json=json) as response:
                data = await response.json()

                return {'status_code': response.status,
                        **data}
                
        elif method == 'POST':
            async with session.post(endpoint, headers=headers, params=params, data=data, json=json) as response:
                data = await response.json()

                return {'status_code': response.status,
                        **data}
    except:
       return {'status_code': 500,
               'detail': 'Unable to connect. Try again'}


async def make_request(*args):
    timeout = aiohttp.ClientTimeout(total=10)
    url = configs.API_URL

    async with aiohttp.ClientSession(base_url=url, timeout=timeout) as session:
        task = [fetch(session=session, **args[i])
                for i in range(len(args))]
        return await asyncio.gather(*task)


class RequestThread(QThread):
    
    data = Signal(list)
    
    def __init__(self, *args):
        print(args)
        super(RequestThread, self).__init__()
        self.request = args
        
    def run(self):
        data =  asyncio.run(make_request(*self.request))
        self.data.emit(data)
        
def get_token(obj):
    parent = obj

    for i in range(0, 101):
        parent = parent.parent()
        
        if hasattr(parent, 'objectName'):

            name = parent.objectName()

            if name == 'app':
                return parent.token
        else:
            return None
