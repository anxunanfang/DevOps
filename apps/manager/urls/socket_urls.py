# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-1-11
# Author Yo
# Email YoLoveLife@outlook.com
from channels.routing import route
from manager import consumers
manager_routing = [
    consumers.ManagerConsumer.as_route(path=r'^/(?P<pk>[0-9]+)/$'),
]