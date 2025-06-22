from django import template

register = template.Library()

@register.filter
def color_darken(hex_color, percent):
    try:
        # Remove # if present
        hex_color = hex_color.lstrip('#')

        # Convert to RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        # Calculate darken amount
        amount = 1 - float(int(percent)) / 100

        # Darken each channel
        r = int(r * amount)
        g = int(g * amount)
        b = int(b * amount)

        # Ensure values stay within 0-255 range
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        # Convert back to hex
        return "#%02x%02x%02x" % (r, g, b)
    except:
        # Return original color if any error occurs
        return hex_color
