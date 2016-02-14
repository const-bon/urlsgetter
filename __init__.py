from urls_getter import UrlsGetter
import requests
import threading
import time
import asyncio
import aiohttp

# import gevent.monkey

@asyncio.coroutine
def thread_builder(link):
    threading.Thread(target=check_async_url, args=(link,)).start()


@asyncio.coroutine
def check_async_url(link):
    #with aiohttp.Timeout(timeout):
    try:
        response = yield from aiohttp.request('GET', link)
        assert response.status == 200
        print(response.status, link)
        # content = yield from response.read()
        # print('URL: {0}:  Content: {1}'.format(url, content))
    except Exception as e:
        pass
    print("Elapsed time: {:.3f} sec".format(time.time() - startTime))

@asyncio.coroutine
def check_url(link):
    try:
        r = requests.get(link, timeout=timeout)
        print(r.status_code, link)
        print("Elapsed time: {:.3f} sec".format(time.time() - startTime))
    # except requests.exceptions.ConnectionError as e:
    #     return 1
    #     print("ERROR", link, e)
    # except requests.exceptions.ReadTimeout as e:
    #     return 1
    #     print("ERROR", link, e)
    # except requests.exceptions.InvalidSchema as e:
    #     return 1
    #     print("ERROR", link, e)
    except Exception as e:
        return 1
        print("ERROR", link, e)

# gevent.monkey.patch_socket()

startTime = time.time()

site = "https://tools.ietf.org/html/rfc1738.html"
# site = "http://bash.im"
# site = "https://ru.wikipedia.org/wiki/HTTPS"
# site = "http://formvalidation.io/validators/uri/"
urls = UrlsGetter()
urls_list = urls.get_urls(site)
# urls.print_urls_tuples()
# urls.print_urls_tuples("1234")
print(urls.get_urls_tuples())
print(len(urls.get_urls_tuples()))
possible_schemas = ("http", "https")
timeout = 10
threads = []    #For async program
for url in urls.get_urls_tuples():
    if len(url[0]) == 0:
        schemas = [schema.__add__(":") for schema in possible_schemas]
        if len(url[1]) == 0:
            schemas = [schema.__add__("//") for schema in schemas]
        url = [schema.__add__(''.join(url)) for schema in schemas]
    else:
        url = [''.join(url)]
    # print(url)

#     """Async threaded program"""
#     for link in url:
#         threads.append(gevent.spawn(thread_builder, link))
#
# gevent.joinall(threads)

#     """Async program"""
#     for link in url:
#         threads.append(gevent.spawn(check_url, link))
#
# gevent.joinall(threads)

    """Asyncio"""
    for link in url:
        threads.append(check_async_url(link))

print(threads)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(threads))
loop.close()


    # """Threaded program"""
    # for link in url:
    #     threading.Thread(target=check_url, args=(link,)).start()

    # """Line program"""
    # for link in url:
    #     if not check_url(link):
    #         continue

    # schemas = ''
    # if len(url[0]) == 0:
    #     schemas = (schema.__add__(":") for schema in possible_schemas)
    # for schema in schemas:
    #     if len(url[1]) == 0:
    #         schema += "//"
    #     url_str = ''.join(url)
    #     link = schema.__add__(url_str)
    #     try:
    #         r = requests.get(link)
    #         print(r.status_code, link, url)
    #     except requests.exceptions.ConnectionError as e:
    #         print("ERROR", link, url, e)

print("Elapsed time: {:.3f} sec".format(time.time() - startTime))
