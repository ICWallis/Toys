# Author: Irene Wallis
# Email: irene@cubicearth.nz
# License: Apache2

def dip2strike(dipaz):
    """Convert dip-dipazimuth data to strike using the right-hand rule

    Args:
        dipaz (float): Azimuth of dip in degrees from north

    Returns:
        float: Strike azimuth (0-360 degrees) based on the right hand rule
    """
    if dipaz < 90:
        strike = (dipaz - 90) + 360
    else:
        strike = dipaz - 90
    return strike

def ft2m(ft):
    return ft / 3.281

def m2ft(m):
    return m * 3.281