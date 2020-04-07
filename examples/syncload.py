from coldtype import *

page = Rect(1080, 1080)

@renderable(rect=Rect(1080, 1080))
def render(r):
    style = Style("ç/MutatorSans.ttf", 250, wdth=0, wght=1, tu=-350, r=1, ro=1)
    return StyledString("COLDTYPE", style).pens().align(r).f(150j, 0.8, 0.7).understroke()