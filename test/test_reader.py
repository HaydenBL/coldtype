from coldtype.test import *


@test()
def test_fit(r):
    inset = 150
    return [
        DATPen().rect(r.inset(inset, 0)).f("hr", 0.5, 0.9),
        Slug("COLD", Style(co, 500, wdth=1, wght=1, slnt=1, tu=-150, r=1)).fit(r.w-inset*2).pens().f("random").align(r).understroke()
    ]


@test()
def test_emoji(r):
    return StyledString("🍕💽🖥", Style("ç/TwemojiMozilla.ttf", 300, t=20, ch=500, bs=11)).pens().align(r)


@test()
def test_color_font(r):
    out = DATPenSet()
    for x in reversed(range(0, 6)):
        out += StyledString("COLDTYPE", Style("≈/PappardelleParty-VF.ttf", 550, palette=x)).pens().translate(x*10, x*10)
    return out.align(r)


@test()
def test_interp(r):
    count = 30
    out = DATPenSet()
    for x in range(count):
        style = Style(co, 200, wdth=x/count, ro=1)
        out += StyledString("COLDTYPE", style).pens().f("random", 0.1).s(0, 0.1).sw(2).align(r).translate(0, x).rotate(x*0.5)
    return out


@test()
def test_family_narrowing(r):
    style = Style("≈/NikolaiV0.4-Bold.otf", 200, narrower=Style("≈/NikolaiV0.4Narrow-Bold.otf", 200, narrower=Style("≈/NikolaiV0.4Condensed-Bold.otf", 200)))
    out = DATPenSet()
    rs = r.inset(0, 40).subdivide(3, "mxy")
    out += StyledString("Narrowing", style).pens().align(rs[0])
    out += StyledString("Narrowing", style).fit(r.w-100).pens().align(rs[1])
    out += StyledString("Narrowing", style).fit(r.w-200).pens().align(rs[2])
    return out


@test()
async def test_stroke_ufo(r):
    hershey_gothic = Font("≈/Hershey-TriplexGothicGerman.ufo")
    await hershey_gothic.load()
    return StyledString("Grieß".upper(), Style(hershey_gothic, 200, tu=-100)).pens().f(None).s("hr", 0.5, 0.5).sw(3).align(r)


@test()
def test_kern_pairs(r):
    return StyledString("CLD", Style(co, 300, rotate=-10, kp={"C/L":20, "L/D":45})).pens().align(r).f("hr", 0.65, 0.65)