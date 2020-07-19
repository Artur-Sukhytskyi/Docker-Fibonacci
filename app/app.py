import sys
import os
import json
from pymemcache.client import Client
from bottle import route, run


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2

def json_deserializer(key, value, flags):
   if flags == 1:
       return value.decode("utf-8")
   if flags == 2:
       return json.loads(value.decode("utf-8"))
   raise Exception("Неизвестный формат")

def get_fibonacci(number):
    if (number == 0) or (number == 1): 
        return number
    return get_fibonacci(number-1) + get_fibonacci(number-2)

port = int(os.environ.get("PORT", 5000))
client = Client(('memcached', 11211), serializer=json_serializer, deserializer=json_deserializer)

@route('/')
def host():
    return "Модуль Е6.9. Для поиска числа фибоначи введите число после '/'. Пример : http://0.0.0.0:5000/15"

@route("/<n:int>")
def fib_handler(n):
   fib_result = client.get(str(n))
   if(fib_result):
       result = fib_result
       return str(result)
   else:
        result = get_fibonacci(n)
        client.set(str(n), result)
        return str(result)

if __name__ == "__main__":
    run(host="0.0.0.0", port=port, debug=True)
