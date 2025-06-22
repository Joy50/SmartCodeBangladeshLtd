from django import template
from colorsys import rgb_to_hls, hls_to_rgb

register = template.Library()

@register.filter
def color_darken(value, amount=0.1):
    """Darken a hex color by a percentage (0-1)"""
    try:
        value = value.lstrip('#')
        r, g, b = int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)
        h, l, s = rgb_to_hls(r/255, g/255, b/255)
        l = max(0, min(1, l - float(amount)))
        r, g, b = hls_to_rgb(h, l, s)
        return '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
    except:
        return value