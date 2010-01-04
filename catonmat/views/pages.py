#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# The new catonmat.net website. See this post for more info:
# http://www.catonmat.net/blog/50-ideas-for-the-new-catonmat-website/
#
# Code is licensed under GNU GPL license.
#

from catonmat.views.utils import render_template_with_quote
from catonmat.quotes      import get_random_quote
from catonmat.parser      import parse

def main(request, map):
    template_data = {
        'page':      map.page,
        'page_path': map.request_path
    }
    map.page.content = parse(map.page.content)
    return render_template_with_quote("page", template_data)
