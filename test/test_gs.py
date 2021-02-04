from coldtype.test import *
from coldtype.gs import gs

@renderable((500, 500))
def test(r):
    return (DPS()
        .constants(ri=r.inset(50), cf=65)
        .gss("""
            $ri $ri𝓘50⌶∩$ri𝓘100⊤
            $ri𝓣Y=0.5𝓘X75𝓒20—a—10@1⊥⍺
            $ri𝓘75↖⨝$ri↘〻𝓞X-50 □𝓘50""")
        .f(None).s(0).sw(4))

@renderable((500, 500))
def test2(r):
    return (DPS()
        .constants(r=r.inset(50), cf=65)
        .gs("$r←↓↑ $r↓|45|$r→ ↙|65|$r↑ $r→|85|$r↓OX-130 ɜ")
        .f(hsl(0.9,l=0.8)).s(0).sw(4)
        .register(a="$r↖⨝$r↘", b="$rＨ∩&a")
        .realize())