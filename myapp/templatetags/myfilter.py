from django.template import Library
import re

register = Library()


@register.filter(name="split")
def split(value):
    """
    Returns the value turned into a list.
    """
    # print(value)
    try:
        number = re.search('pagenumber=(?P<number>\d+)',value).group('number')
        return number
    except:
        pass
