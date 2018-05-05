# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# 以县城ID号作为key的字典  -> Local -> LocaStack

# AppContext RrquestContext -> LocalStack

# Flask -> AppContext  Request -> RequestContext

# current_app -> (LocalStack.top = AppContext top.app=Falsk)

# request -> (LocalStack.top = RequestContext top.request = Request)