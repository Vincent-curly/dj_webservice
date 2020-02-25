"""
  Time : 2020-02-23 07:52:30
  Author : Vincent
  FileName: handle.py
  Software: PyCharm
  Last Modified by: Vincent
  Last Modified time: 2020-02-23 07:52:30
"""
import logging
import base64
import re


def request_base64_decode(request_data):
    """对 requests 解密"""
    logging.info('处理请求体requests=%s' % request_data)
    data_encode = request_data.encode('utf-8')
    request_data_decode = base64.b64decode(data_encode).decode()
    # return re.sub('\s+', '', request_data_decode).strip()       # 去除'\n',返回连续的xml字符串
    return request_data_decode


if __name__=='__main__':
    res = """PG9yZGVySW5mbz48aGVhZD48Y29tcGFueV9udW0+MTAzMDc8L2NvbXBhbnlfbnVtPjxrZXk+MTU3OTA2MjU5NjEzNDwva2V5PjxzaWduPjU5MzcxNzc5OEIyMUZDN0Q3Q0YyRkU2REREODlGRTM0PC9zaWduPjwvaGVhZD48ZGF0YT48b3JkZXJfdGltZT4yMDIwLTAxLTE1IDE0OjAwOjAwPC9vcmRlcl90aW1lPjx0cmVhdF9jYXJkPjUzMDExMTE5NjcxMjA0NDQyWDwvdHJlYXRfY2FyZD48cmVnX251bT5VMDEyMTU1MjwvcmVnX251bT48YWRkcl9zdHI+5LqR5Y2X55yBLOaYhuaYjuW4gizlrpjmuKHljLos5piG5piO5biC5a6Y5rih5Yy65Lq65rCR5Yy76Zmi5YaF5LiJ56eR77yI5piG5piO5YWz5LiK5a+F5bOw6LevNjPlj7fkuozlj7fkvY/pmaLmpbw15bGC77yJPC9hZGRyX3N0cj48Y29uc2lnbmVlPumZiOaWh+WFrjwvY29uc2lnbmVlPjxjb25fdGVsPjY3MTg4MTA1LTgwMzM8L2Nvbl90ZWw+PHNlbmRfZ29vZHNfdGltZT48L3NlbmRfZ29vZHNfdGltZT48aXNfaG9zX2FkZHI+MTwvaXNfaG9zX2FkZHI+PHByZXNjcmlwdD48cGRldGFpbD48dXNlcl9uYW1lPuavleS4veS6mjwvdXNlcl9uYW1lPjxhZ2U+NTI8L2FnZT48Z2VuZGVyPjA8L2dlbmRlcj48dGVsPjY3MTg4MTA1LTgwMzM8L3RlbD48aXNfc3VmZmVyaW5nPjE8L2lzX3N1ZmZlcmluZz48YW1vdW50PjE4PC9hbW91bnQ+PHN1ZmZlcmluZ19udW0+MTg8L3N1ZmZlcmluZ19udW0+PGppX2ZyaWVkPjE8L2ppX2ZyaWVkPjx0eXBlPjA8L3R5cGU+PGlzX3dpdGhpbj4wPC9pc193aXRoaW4+PG90aGVyX3ByZXNfbnVtPlUwMTIxNTUyPC9vdGhlcl9wcmVzX251bT48c3BlY2lhbF9pbnN0cnU+KEoxOC45MDAp6IK654KOPC9zcGVjaWFsX2luc3RydT48YmVkX251bT43MzwvYmVkX251bT48aG9zX2RlcGFydD7lhoXkuInnp5E8L2hvc19kZXBhcnQ+PGhvc3BpdGFsX251bT4yMjI4NDc8L2hvc3BpdGFsX251bT48ZGlzZWFzZV9jb2RlPjAyMDA8L2Rpc2Vhc2VfY29kZT48ZG9jdG9yPuadqOmYszwvZG9jdG9yPjxwYXN0ZV9kZXNjX2ZpbGU+PC9wYXN0ZV9kZXNjX2ZpbGU+PHByZXNjcmlwdF9yZW1hcms+PC9wcmVzY3JpcHRfcmVtYXJrPjxwYWNrYWdlX2Rvc2U+PC9wYWNrYWdlX2Rvc2U+PG1lZGljYXRpb25fbWV0aG9kcz7nhY7mnI08L21lZGljYXRpb25fbWV0aG9kcz48aXNfaG9zPjI8L2lzX2hvcz48cGVyX3BhY2tfbnVtPjE8L3Blcl9wYWNrX251bT48cGVyX3BhY2tfZG9zZT4yMDA8L3Blcl9wYWNrX2Rvc2U+PG1lZGljYXRpb25faW5zdHJ1Y3Rpb24+5q+P5aSpM+asoTwvbWVkaWNhdGlvbl9pbnN0cnVjdGlvbj48cHJlc2NyaXB0X3JlbWFyaz7nhY456KKLPC9wcmVzY3JpcHRfcmVtYXJrPjxtZWRpY2lfeHE+PHhxPjxtZWRpY2luZXM+Kum7hOiKqjwvbWVkaWNpbmVzPjxkb3NlPjMwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA4PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDA0MTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KueZveacrzwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA3PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAxMTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KumZiOearjwvbWVkaWNpbmVzPjxkb3NlPjEwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA0PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDI3MzwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+Kua7h+aftOiDoTwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjAyPC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDE5MDwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuiRm+aguTwvbWVkaWNpbmVzPjxkb3NlPjIwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA3PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAyOTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KumYsumjjjwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA4PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAyNTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KumYsumjjjwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA4PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAyNTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+Kum7hOi/njwvbWVkaWNpbmVzPjxkb3NlPjEwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjI4PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAzODwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuiMr+iLkzwvbWVkaWNpbmVzPjxkb3NlPjMwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA3PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDMyMjwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuazleWNiuWkjzwvbWVkaWNpbmVzPjxkb3NlPjEwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjQzPC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAyNDwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuahlOailzwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjExPC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDA0NTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuW5v+iXv+mmmTwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA2PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDE5OTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+Kua1mei0neavjTwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjI0PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDA5MjwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KueUmOiNiTwvbWVkaWNpbmVzPjxkb3NlPjEwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA3PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAyODwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuiWj+iLoeS7gTwvbWVkaWNpbmVzPjxkb3NlPjIwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA0PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDE3ODwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuiWj+iLoeS7gTwvbWVkaWNpbmVzPjxkb3NlPjIwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA0PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDE3ODwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+Kum6u+m7hDwvbWVkaWNpbmVzPjxkb3NlPjEwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA5PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDIwNjwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuiLpuadj+S7gTwvbWVkaWNpbmVzPjxkb3NlPjEwLjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA2PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDE3NTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KuicnOeTnOiSjOearjwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjA2PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDI4NzwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KueZveWPijwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4xLjcwPC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAwNDwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+Kua7h+eZvumDqDwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjEzPC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAwMTwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PHhxPjxtZWRpY2luZXM+KueZveWJjTwvbWVkaWNpbmVzPjxkb3NlPjE1LjAwPC9kb3NlPjx1bml0PuWFizwvdW5pdD48dW5pdF9wcmljZT4wLjE1PC91bml0X3ByaWNlPjxnb29kc19udW0+MDAwMDAwNzwvZ29vZHNfbnVtPjxkb3NlX3RoYXQ+PC9kb3NlX3RoYXQ+PHJlbWFyaz48L3JlbWFyaz48bV91c2FnZT48L21fdXNhZ2U+PGdvb2RzX25vcm1zPuWFizwvZ29vZHNfbm9ybXM+PGdvb2RzX29yZ2luPjwvZ29vZHNfb3JnaW4+PE1lZFBlckRvcz48L01lZFBlckRvcz48TWVkUGVyRGF5PjwvTWVkUGVyRGF5PjwveHE+PC9tZWRpY2lfeHE+PC9wZGV0YWlsPjwvcHJlc2NyaXB0PjwvZGF0YT48L29yZGVySW5mbz4K"""
    print(request_base64_decode(res))