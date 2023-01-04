"""make tiles"""

import math


def point_to_pixels(lon, lat, zoom):
    """convert gps coordinates to web mercator"""
    radius = math.pow(2, zoom)
    lat = math.radians(lat)

    xcoord = (lon + 180.0) / 360.0 * radius
    ycoord = (1.0 - math.log(math.tan(lat) + (1.0 / math.cos(lat))) / math.pi) / 2.0 * radius

    return xcoord, ycoord


def alltiles(top, bot, lef, rgt, frame=0):
    """generator for tiles"""
    if frame > 0:
        top += (top - bot) * frame
        bot -= (top - bot) * frame
        rgt += (rgt - lef) * frame
        lef -= (rgt - lef) * frame

    for zoom in range(20):
        xlt, ylt = point_to_pixels(lef, top, zoom)
        xrb, yrb = point_to_pixels(rgt, bot, zoom)

        yield (int(xlt), math.ceil(xrb)), (int(ylt), math.ceil(yrb))
