from coldtype import *
from coldtype.time.nle.ascii import AsciiTimeline

nudge = Font.MutatorSans()

at = AsciiTimeline(1, """
                                                                <
        [L                                   ]
                        [Lr             ]
                     [F                                     ]
               [H                 ]             
""")

@animation(timeline=at)
def officehours(f):
    stx = Style.StretchX(0,
        L=(730*at.ki("L").io(10, "eeio"), 310),
        F=(1220*at.ki("F").io(10, "eleio"), 260),
        H=(1900*at.ki("H").io(10, "ceio"), 250))
    
    txt = (StSt("Coldtype\nOffice\nHours".upper()
        , Font.MutatorSans()
        , fontSize=125
        , ss02=1
        , mods=stx
        , leading=20)
        .f(1)
        .xalign(f.a.r)
        .align(f.a.r))

    bg = (P(txt.copy().ambit().inset(-50))
            .f(hsl(0.35, 0.8, 0.3)))

    # after bg, so it doesn't effect bounds 
    txt.index([0, 2], lambda p: p
        .rotate(at.ki("Lr").e("eeio", 0, r=(0, 360))
            , th=1))

    return PS([
        bg.copy().translate(5, -5).f(0),
        bg,
        txt])