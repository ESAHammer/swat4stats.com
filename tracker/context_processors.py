# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, absolute_import)


def current_view(request):
    return {
        'current_url_name': request.resolver_match.url_name,
        'current_view_name': request.resolver_match.view_name,
        'current_view_func': '%s.%s' % 
            (request.resolver_match.func.__module__, request.resolver_match.func.__name__),
    }