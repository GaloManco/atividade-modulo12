# import time
# from django.http import JsonResponse

# def api(request):
#     time.sleep(1)
#     payload = {"message": "Hello from Crowdbotics"}
#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET["task_id"]
#     return JsonResponse(payload)

import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

async def http_call_async():
    l = ['Estou', 'fazendo','execicio', 'ebac']
    for num in l:
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org')
        print(r)


def http_call_sync():
    for num in range(1,6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org")
    print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    texto = "Non-blocking HTTP request"
    exec = "Eu estou fazendo meu execício ebac!"
    return HttpResponse(texto)


def sync_views(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
