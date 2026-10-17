from PIL import Image
import os
ROOT = "/app/work/game/V6-TURBZ-main/public/sprites/"
SRC = "/app/work/orig_class_warriors.png"
if not os.path.exists(SRC):
    Image.open(ROOT + "class_warriors.png").save(SRC)
src = Image.open(SRC).convert("RGBA")
MAG = (255, 0, 255, 255)
IDS = ['base','warden','spellweaver','spiritbinder','nightblade','pathfinder','ironpalm','bloodrager','ghoulknight','frostblade','pyromancer','tidecaller','stormrider','briarmage','lightbringer','voidwalker','absolver','vigilant','coinmaster','hexbinder','corsair','warlord','nightlord','songweaver','oathkeeper','ronin','seraph','moonhopper','bladedancer','sovereign']
FW, FH = 32, 44
out = Image.new("RGBA", (768, 1056), MAG)
out.paste(src, (0, 0))

PAL = {
    'k': (20, 12, 16), 'S': (236, 240, 246), 's': (178, 188, 202), 'd': (104, 112, 128),
    'w': (112, 70, 38), 'g': (232, 192, 72), 'o': (118, 108, 94), 'O': (164, 152, 132),
}
SWORD = (["..k..", ".kSk.", ".kSk.", ".ksk.", ".ksk.", ".ksk.", ".ksk.", ".ksk.", ".kdk.", "kgggk", ".kwk.", ".kwk.", ".kgk.", "..k.."], 11)
GREAT = (["..k..", ".kSk.", "kSsdk", "kSadk", "kSsdk", "kSadk", "kSsdk", "kSadk", "kSsdk", "kSsdk", "kSsdk", "kkdkk", "kaaak", ".kwk.", ".kwk.", ".kak.", "..k.."], 14)
AXE = ([r[::-1] for r in ["....k..", ".kkkwk.", "kSSkwk.", "kSsswk.", "kSsswk.", "kSsswk.", "kSSkwk.", ".kkkwk.", "...kwk.", "...kwk.", "...kwk.", "...kwk.", "...kak.", "....k.."]], 10)
HAMMER = (["kkkkkkk", "kOOOook", "kOoooOk", "kooooak", "kkkkkkk", "..kwk..", "..kwk..", "..kwk..", "..kwk..", "..kwk..", "..kwk..", "..kgk..", "...k..."], 9)
KATANA = (["..k.", ".kSk", ".kSk", ".kSk", "kSk.", "kSk.", "kSk.", "kSk.", "kdk.", "kggk", "kak.", "kak.", "kak.", ".k.."], 11)
CUTLASS = (["..k..", ".kSk.", ".kSk.", "kSk..", "kSk..", "kSk..", "kSdk.", ".kdk.", "kgggk", ".kwk.", ".kwk.", "kgggk", ".kk.."], 10)
DAGGER = ([".k.", "kSk", "kSk", "ksk", "kdk", "kak", "kwk", ".k."], 6)
MACE = ([".kkk.", "kSsdk", "ksSsk", "kSsdk", ".kkk.", ".kwk.", ".kwk.", ".kwk.", ".kwk.", ".kwk.", ".kgk.", "..k.."], 8)
FIST = (["kkkk", "kSsk", "ksdk", "kkkk"], 1)
HEAVY = (["kkkkk", "kSssk", "kssdk", ".kkk."], 1)
LIGHT = (["kkkk", "kssk", ".kk."], 1)

MELEE = {
    'warden': dict(w=MACE, pad=HEAVY, a=(90, 150, 70), tint=(120, 150, 90)),
    'nightblade': dict(w=DAGGER, dual=True, pad=LIGHT, a=(120, 80, 200), tint=(70, 60, 120)),
    'ironpalm': dict(w=FIST, dual=True, pad=LIGHT, a=(200, 150, 60), tint=(160, 110, 60)),
    'bloodrager': dict(w=AXE, pad=HEAVY, a=(200, 40, 40), tint=(160, 60, 50)),
    'ghoulknight': dict(w=GREAT, pad=HEAVY, a=(90, 210, 120), tint=(70, 100, 80)),
    'frostblade': dict(w=SWORD, pad=HEAVY, a=(150, 220, 255), tint=(150, 200, 230), steel=True),
    'briarmage': dict(w=HAMMER, pad=HEAVY, a=(110, 170, 80), tint=(120, 140, 80)),
    'corsair': dict(w=CUTLASS, pad=LIGHT, a=(40, 90, 160), tint=(150, 110, 70)),
    'warlord': dict(w=SWORD, pad=HEAVY, a=(200, 40, 40), tint=(170, 80, 70)),
    'oathkeeper': dict(w=SWORD, pad=HEAVY, a=(240, 210, 90), tint=(220, 200, 140)),
    'ronin': dict(w=KATANA, pad=LIGHT, a=(170, 30, 40), tint=(150, 40, 50)),
    'bladedancer': dict(w=DAGGER, dual=True, pad=LIGHT, a=(190, 110, 230), tint=(150, 90, 180)),
}


def opaque(c):
    return c[3] > 0 and c[:3] != (255, 0, 255)


def lum(c):
    return (c[0] * 3 + c[1] * 6 + c[2]) / 10


def mix(c, t, k):
    return tuple(int(c[i] * (1 - k) + t[i] * k) for i in range(3)) + (255,)


def stamp(fr, tpl, gx, gy, pal, behind=False, flip=False):
    rows, grip = tpl
    w = len(rows[0])
    ox = gx - w // 2
    oy = gy - grip
    for j, r in enumerate(rows):
        for i, ch in enumerate(r[::-1] if flip else r):
            if ch == '.':
                continue
            x, y = ox + i, oy + j
            if not (0 <= x < FW and 0 <= y < FH):
                continue
            if behind and opaque(fr.getpixel((x, y))):
                continue
            fr.putpixel((x, y), pal[ch] + (255,) if len(pal[ch]) == 3 else pal[ch])


def extents(fr, y):
    xs = [x for x in range(FW) if opaque(fr.getpixel((x, y)))]
    return (min(xs), max(xs)) if xs else (12, 20)


def feet(fr):
    for y in range(FH - 1, -1, -1):
        if any(opaque(fr.getpixel((x, y))) for x in range(FW)):
            return y
    return 42


def polish(fr):
    """Rim light from above, soft shade on the right edge, a contact shadow under the feet."""
    base = fr.copy()
    for y in range(1, FH):
        for x in range(1, FW - 1):
            c = base.getpixel((x, y))
            if not opaque(c) or lum(c) < 48:
                continue
            if not opaque(base.getpixel((x, y - 1))):
                fr.putpixel((x, y), mix(c, (255, 250, 235), 0.18))
            elif not opaque(base.getpixel((x + 1, y))):
                fr.putpixel((x, y), mix(c, (10, 6, 12), 0.16))
    fy = feet(base)
    l, r = extents(base, fy)
    if fy + 1 < FH:
        for x in range(l - 1, r + 2):
            if 0 <= x < FW and not opaque(fr.getpixel((x, fy + 1))):
                fr.putpixel((x, fy + 1), (0, 0, 0, 96))


def melee(fr, cfg, row, f):
    pal = dict(PAL)
    pal['a'] = cfg['a']
    if cfg.get('steel'):
        pal['S'], pal['s'], pal['d'] = (240, 252, 255), (170, 220, 245), (90, 150, 200)
    pp = dict(PAL)
    t = cfg['tint']
    pp['S'] = mix(PAL['S'], t, 0.45)[:3]
    pp['s'] = mix(PAL['s'], t, 0.55)[:3]
    pp['d'] = mix(PAL['d'], t, 0.5)[:3]
    fy = feet(fr)
    sy = fy - 14
    hy = fy - 9
    swing = [0, 1, 0, -1][f]
    l, r = extents(fr, sy)
    hl, hr = extents(fr, hy)
    if row in (0, 2):
        stamp(fr, cfg['pad'], l + 1, sy, pp)
        stamp(fr, cfg['pad'], r - 1, sy, pp)
        behind = row == 0
        main_x = hl if row == 0 else hr
        stamp(fr, cfg['w'], main_x, hy, pal, behind=behind, flip=behind)
        if cfg.get('dual'):
            stamp(fr, cfg['w'], hr if row == 0 else hl, hy, pal, behind=behind, flip=True)
    else:
        right = row == 1
        cx = (l + r) // 2
        stamp(fr, cfg['pad'], cx - (1 if right else -1), sy, pp)
        gx = (hr - 1 + swing) if right else (hl + 1 - swing)
        if cfg.get('dual'):
            stamp(fr, cfg['w'], (hl + 2) if right else (hr - 2), hy + 1, pal, behind=True, flip=not right)
        stamp(fr, cfg['w'], gx, hy, pal, flip=not right)


def crying(fr, row, f):
    """Base girl recoloured: black hair, sailor uniform, red scarf, falling tears."""
    hair = {(144, 106, 75): (62, 58, 78), (106, 68, 40): (34, 30, 44), (85, 46, 29): (22, 18, 30)}
    cloth = {(138, 106, 74): (34, 44, 92), (176, 149, 119): (236, 236, 244), (122, 78, 46): (196, 40, 52), (98, 53, 33): (150, 26, 40),
             (110, 76, 55): (40, 52, 104), (97, 60, 0): (52, 64, 120), (83, 46, 36): (28, 36, 76)}
    fy = feet(fr)
    for y in range(FH):
        for x in range(FW):
            c = fr.getpixel((x, y))
            if not opaque(c):
                continue
            k = c[:3]
            if k in hair:
                fr.putpixel((x, y), hair[k] + (255,))
            elif k in cloth:
                fr.putpixel((x, y), cloth[k] + (255,))
    if row == 0:
        return
    eyes = [(x, y) for y in range(FH) for x in range(FW) if fr.getpixel((x, y))[:3] == (20, 52, 98)]
    seen = set()
    for (x, y) in eyes:
        if x in seen:
            continue
        seen.add(x)
        seen.add(x + 1)
        drip = (f % 3)
        for d in range(1, 3 + drip):
            ty = y + d
            if ty < FH and opaque(fr.getpixel((x, ty))):
                fr.putpixel((x, ty), (140, 210, 255, 255) if d < 3 else (200, 240, 255, 255))


for k, cid in enumerate(IDS):
    bx, by = (k % 6) * 128, (k // 6) * 176
    for row in range(4):
        for f in range(4):
            box = (bx + f * FW, by + row * FH, bx + f * FW + FW, by + row * FH + FH)
            fr = src.crop(box)
            if cid in MELEE:
                melee(fr, MELEE[cid], row, f)
            polish(fr)
            out.paste(fr, box[:2])
# Crying Girl: new block at (0, 880).
for row in range(4):
    for f in range(4):
        fr = src.crop((f * FW, row * FH, f * FW + FW, row * FH + FH))
        crying(fr, row, f)
        polish(fr)
        out.paste(fr, (f * FW, 880 + row * FH))
out.save(ROOT + "class_warriors.png", optimize=True)

# Transformation forms.
def keyed(img, bg):
    img = img.convert("RGBA")
    p = img.load()
    for y in range(img.height):
        for x in range(img.width):
            if p[x, y][:3] == bg[:3]:
                p[x, y] = (0, 0, 0, 0)
    return img


cat = Image.new("RGBA", (40 * 6, 34 * 2), (0, 0, 0, 0))
for r, name in enumerate(["catrunx2.gif", "catwalkx2.gif"]):
    g = Image.open("/app/work/cat/cat sprite/" + name)
    for i in range(g.n_frames):
        g.seek(i)
        fr = g.convert("RGBA")
        fr = keyed(fr, fr.getpixel((0, 0)))
        cat.paste(fr, (i * 40 + (40 - fr.width) // 2, r * 34 + 34 - fr.height), fr)
cat.save(ROOT + "form_cat.png", optimize=True)

bun = Image.open("/app/work/bunny.png").convert("RGBA")
ROWS = {0: (138, 166), 1: (216, 245), 2: (51, 78)}  # up, right, down
rab = Image.new("RGBA", (36 * 4, 36 * 3), (0, 0, 0, 0))
for r, (y0, y1) in ROWS.items():
    strip = bun.crop((0, y0 - 2, bun.width, y1 + 2))
    cols = [x for x in range(strip.width) if any(strip.getpixel((x, y))[3] > 0 for y in range(strip.height))]
    groups = []
    for x in cols:
        if groups and x - groups[-1][-1] <= 2:
            groups[-1].append(x)
        else:
            groups.append([x])
    for i, gcols in enumerate(groups[:4]):
        fr = strip.crop((gcols[0], 0, gcols[-1] + 1, strip.height))
        bb = fr.getbbox()
        fr = fr.crop(bb)
        rab.paste(fr, (i * 36 + (36 - fr.width) // 2, r * 36 + 36 - fr.height), fr)
rab.save(ROOT + "form_rabbit.png", optimize=True)
print("ok")
