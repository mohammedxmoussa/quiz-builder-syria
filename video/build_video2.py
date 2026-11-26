#!/usr/bin/env python3
"""Exam Builder intro video v2: text + REAL phone screenshots of the site
(slow vertical pan), a chatbot-logos scene, Syrian-style Arabic narration
(Middle Eastern voice, no brand names in scene 3). Re-runnable."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(HERE, "work2"); os.makedirs(WORK, exist_ok=True)
SHOTS = os.path.join(HERE, "shots"); LOGOS = os.path.join(HERE, "logos")
W, H = 1280, 720
BG = (250, 247, 242); INK = (30, 41, 59); ACCENT = (15, 118, 110)
MUTED = (100, 116, 139); BAR_BG = (226, 232, 240); FRAME = (30, 41, 59)
FONTS = os.path.join(HERE, "fonts")  # bundled Noto fonts, no system install needed
F_BOLD = os.path.join(FONTS, "NotoSansArabic_700Bold.ttf")
F_KUFI = os.path.join(FONTS, "NotoKufiArabic_700Bold.ttf")
F_REG = os.path.join(FONTS, "NotoSansArabic_400Regular.ttf")
F_LAT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_LATB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
VOICE = "avocado_v2:vd2_r8_rep1k_0534_v068_28k_g5k"  # Dazed Petal — LOCKED by the user 2026-11-26: this and ONLY this voice for this video. Do not substitute.
TTS = "/opt/hatch/bin/tts"

# kind: phone / logos / books ; shot + pan start for phone scenes
SCENES = [
    ("phone", "landing", 50, "", "عندك امتحان بدّك تجهّزه؟", "",
     "عندك امتحان وبدّك تجهّزه بسرعة وبشكل مرتّب؟"),
    ("phone", "json", 50, "", "منشئ الاختبارات", "أداة مجانية بسيطة لعمل امتحان جاهز للطباعة",
     "هادا مُنْشِئُ الاختبارات: أداة مجانية بتساعدك تعمل امتحان جاهز للطباعة، بخطوات بسيطة، وبدون ما تْكون خبير بالكمبيوتر."),
    ("logos", None, 0, "الخطوة ١", "اطلب الامتحان من نموذج محادثة", "",
     "أول خطوة: احكي مع أي نموذج محادثة تَستخدمه. انسخلو رابط الدليل من الموقع، واطلب منو يكتبلك الامتحان."),
    ("phone", "editor", 50, "أنت الأساس", "أنت بتخطّط للامتحان", "القرار إلك: الدروس والأسئلة والعلامات",
     "الامتحان امتحانك: أنت بتقرر الدروس والأسئلة والعلامات. فيك تكتب أسئلتك بنفسك وتبعتلو ياها، أو ترفع ملف فيه تفاصيل الامتحان، وهو بس بيكتبها بالصيغة المطلوبة."),
    ("phone", "json", 55, "الخطوة ٢", "الصق النص في الموقع", "",
     "تاني خطوة: انسخ النص يلي عطاك ياه، والصقو بالموقع. إذا في غلط، الموقع بيقلك وين الغلط بالعربي، وبترجعلو ياه ليصلّحو."),
    ("phone", "images", 50, "الخطوة ٣", "أضف الصور واختر القالب", "قوالب وزارية ومؤتمتة وعادية",
     "تالت خطوة: إذا امتحانك فيو صور أو رسوم، ارفعها. وبعدين اختار القالب يلي بناسب مادتك: عنا قوالب وزارية ومُؤَتْمَتَة وقوالب عادية."),
    ("phone", "preview", 0, "الخطوة ٤", "اطبع الامتحان", "ونزّل ملف الامتحان لتحتفظ فيه وترجع تعدّل عليه",
     "وآخر خطوة: اطبع الامتحان مباشرة من الموقع. بيطلع مرتّب وجاهز على ورقة واحدة، على الوجهين. وبس تخلّص، فيك تنزّل ملف الامتحان من الموقع لتحتفظ فيه، وترجع تعدّل عليه أو تطبعو بأي وقت."),
    ("books", None, 0, "ميزة إضافية", "امتحان من الكتاب المدرسي", "كتب الصف التاسع والبكالوريا موجودة بالموقع",
     "وفي ميزة حلوة: كتب الصف التاسع والبكالوريا موجودة بالموقع. فيك تطلب من الذكاء الاصطناعي يعملك الامتحان من صفحات محددة من الكتاب نفسه."),
    ("phone", "landing", 40, "", "مجاني، بدون تسجيل", "معلوماتك ما بتطلع من جهازك أبداً",
     "الأداة مجانية، وبدون تسجيل، ومعلوماتك ما بتطلع من جهازك أبداً. جرّبها بامتحانك الجاية!"),
]
PHONE_X, PHONE_Y, PHONE_W, PHONE_H = 54, 48, 336, 596

def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font, direction="rtl", language="ar") <= max_w: cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

def base(i):
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    bf = ImageFont.truetype(F_KUFI, 27)
    d.text((1230, 30), "منشئ الاختبارات", font=bf, fill=ACCENT, anchor="ra", direction="rtl", language="ar")
    bx0, bx1, by = 90, W - 90, H - 56
    d.rounded_rectangle([bx0, by, bx1, by + 10], radius=5, fill=BAR_BG)
    d.rounded_rectangle([bx0, by, bx0 + (bx1 - bx0) * (i + 1) / len(SCENES), by + 10], radius=5, fill=ACCENT)
    ff = ImageFont.truetype(F_LAT, 22)
    d.text((W // 2, H - 40), "mohammedxmoussa.github.io/quiz-builder-syria", font=ff, fill=MUTED, anchor="ma")
    return img, d


_REF = "إلأبجيقط٣ا"  # tall + deep Arabic glyphs: one consistent centre line per font

def ink_center_baseline(d, font, cy):
    """Baseline y so the ink of a reference string is centred on cy."""
    b = d.textbbox((0, 0), _REF, font=font, anchor="ls", direction="rtl", language="ar")
    return cy - (b[1] + b[3]) / 2

def pill(d, text, font, y, fill, fg, cx=None, right=None, pad_x=34, pad_y=20,
         outline=None, width=2, text_fill=None, gap_min=0):
    """Draw a pill with text properly padded. Centred on cx, or right edge at `right`."""
    b = d.textbbox((0, 0), _REF, font=font, anchor="ls", direction="rtl", language="ar")
    h = int((b[3] - b[1]) + 2 * pad_y)
    bb = d.textbbox((0, 0), text, font=font, anchor="ls", direction="rtl", language="ar")
    tw = bb[2] - bb[0]
    w = tw + 2 * pad_x
    x1 = (cx + w / 2) if cx is not None else right
    x0 = x1 - w
    d.rounded_rectangle([x0, y, x1, y + h], radius=h // 2, fill=fill, outline=outline, width=width)
    base = ink_center_baseline(d, font, y + h / 2)
    # centre the ink horizontally (bbox x offset aware)
    tx = (x0 + x1) / 2 - (bb[0] + bb[2]) / 2
    d.text((tx, base), text, font=font, fill=fg, anchor="ls", direction="rtl", language="ar")
    return h, x0, x1

def chip(d, text, right_x, y):
    f = ImageFont.truetype(F_BOLD, 32)
    h, _, _ = pill(d, text, f, y, ACCENT, (255, 255, 255), right=right_x, pad_x=32, pad_y=18)
    return y + h + 30

def text_block(d, ch, title, sub, right_x=1230, y=170, max_w=720, centered=False):
    if ch:
        if centered:
            f = ImageFont.truetype(F_BOLD, 32)
            h, _, _ = pill(d, ch, f, y, ACCENT, (255, 255, 255), cx=W // 2, pad_x=32, pad_y=18)
            y += h + 30
        else:
            y = chip(d, ch, right_x, y)
    tf = ImageFont.truetype(F_BOLD, 58)
    for ln in wrap(d, title, tf, max_w):
        if centered: d.text((W // 2, y), ln, font=tf, fill=INK, anchor="ma", direction="rtl", language="ar")
        else: d.text((right_x, y), ln, font=tf, fill=INK, anchor="ra", direction="rtl", language="ar")
        y += 80
    y += 26
    if sub:
        sf = ImageFont.truetype(F_REG, 36)
        for ln in wrap(d, sub, sf, max_w):
            if centered: d.text((W // 2, y), ln, font=sf, fill=MUTED, anchor="ma", direction="rtl", language="ar")
            else: d.text((right_x, y), ln, font=sf, fill=MUTED, anchor="ra", direction="rtl", language="ar")
            y += 52

def make_bezel(path):
    """RGBA bezel: dark rounded frame with a rounded transparent window.
    Overlaid ON TOP of the screenshot so the screen corners are curved."""
    pad, ro, ri, S = 8, 36, 28, 4          # S = supersampling for smooth edges
    w, h = (PHONE_W + 2 * pad) * S, (PHONE_H + 2 * pad) * S
    img = Image.new("RGBA", (w, h), FRAME + (255,))
    hole = Image.new("L", (w, h), 255); hd = ImageDraw.Draw(hole)
    hd.rounded_rectangle([pad * S, pad * S, w - pad * S - 1, h - pad * S - 1], radius=ri * S, fill=0)
    outer = Image.new("L", (w, h), 0); od = ImageDraw.Draw(outer)
    od.rounded_rectangle([0, 0, w - 1, h - 1], radius=ro * S, fill=255)
    alpha = Image.composite(hole, Image.new("L", (w, h), 0), outer)   # frame area only
    img.putalpha(alpha)
    img = img.resize((w // S, h // S), Image.LANCZOS); img.save(path)

def slide_phone(i, ch, title, sub):
    img, d = base(i)
    text_block(d, ch, title, sub)
    return img

def slide_logos(i, ch, title, sub):
    img, d = base(i)
    y = 92
    if ch:
        f = ImageFont.truetype(F_BOLD, 32)
        h, _, _ = pill(d, ch, f, y, ACCENT, (255, 255, 255), cx=W // 2, pad_x=32, pad_y=18)
        y += h + 26
    tf = ImageFont.truetype(F_BOLD, 58)
    d.text((W // 2, y), title, font=tf, fill=INK, anchor="ma", direction="rtl", language="ar")
    y += 132
    tiles = [("deepseek", "DeepSeek", True), ("gemini", "Gemini", True),
             ("metaai", "Muse", False), ("claude", "Claude", False), ("chatgpt", "ChatGPT", False)]
    tw_, th_, gap = 216, 222, 18
    x = (W - (tw_ * 5 + gap * 4)) // 2
    cf = ImageFont.truetype(F_LATB, 21); sf = ImageFont.truetype(F_REG, 20)
    for name, cap, vpn in tiles:
        d.rounded_rectangle([x, y, x + tw_, y + th_], radius=18, fill=(255, 255, 255), outline=BAR_BG, width=2)
        logo = Image.open(os.path.join(LOGOS, name + ".png")).convert("RGBA")
        logo.thumbnail((176, 92))
        img.paste(logo, (x + (tw_ - logo.width) // 2, y + 14 + (92 - logo.height) // 2), logo)
        d.text((x + tw_ // 2, y + 118), cap, font=cf, fill=INK, anchor="ma")
        if vpn: pill(d, "متاح بسوريا", sf, y + 156, (226, 244, 241), ACCENT, cx=x + tw_ // 2, pad_x=18, pad_y=11)
        x += tw_ + gap
    nf = ImageFont.truetype(F_REG, 30)
    d.text((W // 2, y + th_ + 30), "أي نموذج محادثة بيكفي، هدول بس أمثلة", font=nf, fill=MUTED, anchor="ma", direction="rtl", language="ar")
    return img

def slide_books(i, ch, title, sub):
    img, d = base(i)
    text_block(d, ch, title, sub, right_x=W // 2 + 360, y=110, max_w=760, centered=True)
    subjects = ["العلوم", "الرياضيات", "الفيزياء", "الكيمياء", "اللغة العربية", "التاريخ", "الجغرافيا", "اللغة الإنكليزية"]
    f = ImageFont.truetype(F_BOLD, 30)
    rows = [subjects[:4], subjects[4:]]
    y = 430
    for row in rows:
        widths = []
        for s_ in row:
            bb = d.textbbox((0, 0), s_, font=f, anchor="ls", direction="rtl", language="ar")
            widths.append((bb[2] - bb[0]) + 2 * 30)
        total = sum(widths) + 24 * (len(row) - 1)
        x = W // 2 + total / 2
        for s_, w_ in zip(row, widths):
            h, _, _ = pill(d, s_, f, y, (255, 255, 255), INK, right=x, pad_x=30, pad_y=17, outline=ACCENT)
            x -= w_ + 24
        y += h + 20
    return img

def tts(text, path):
    if os.path.exists(path): return
    r = subprocess.run([TTS, "speak", "--language", "ar", "--voice", VOICE,
                        "--output", path, "--text-stdin"], input=text, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(path): raise RuntimeError(r.stdout + r.stderr)

def dur(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())

def main():
    global BEZEL
    BEZEL = os.path.join(WORK, "bezel.png"); make_bezel(BEZEL)
    segs = []
    for i, (kind, shot, y0, ch, title, sub, narr) in enumerate(SCENES):
        mp3 = os.path.join(WORK, f"voice-{i}.mp3"); tts(narr, mp3)
        D = dur(mp3) + 0.8
        png = os.path.join(WORK, f"slide-{i}.png")
        if kind == "phone": slide = slide_phone(i, ch, title, sub)
        elif kind == "logos": slide = slide_logos(i, ch, title, sub)
        else: slide = slide_books(i, ch, title, sub)
        slide.save(png)
        seg = os.path.join(WORK, f"seg-{i}.mp4")
        fade_out = max(D - 0.35, 0.1)
        if kind == "phone":
            shotp = os.path.join(SHOTS, shot + ".png")
            fc = (f"[1:v]scale=336:727,crop=336:596:0:'{y0}+(131-{y0})*t/{D:.2f}'[ph];"
                  f"[0:v][ph]overlay={PHONE_X}:{PHONE_Y}[bg];[bg][3:v]overlay={PHONE_X - 8}:{PHONE_Y - 8},format=yuv420p,"
                  f"fade=t=in:st=0:d=0.35,fade=t=out:st={fade_out:.2f}:d=0.35[v]")
            cmd = ["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", png, "-i", shotp, "-i", mp3, "-i", BEZEL,
                   "-filter_complex", fc, "-map", "[v]", "-map", "2:a",
                   "-af", f"apad=pad_dur={D:.2f}", "-c:v", "libx264", "-r", "25",
                   "-c:a", "aac", "-b:a", "128k", "-t", f"{D:.2f}", seg]
        else:
            fc = f"[0:v]format=yuv420p,fade=t=in:st=0:d=0.35,fade=t=out:st={fade_out:.2f}:d=0.35[v]"
            cmd = ["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", png, "-i", mp3,
                   "-filter_complex", fc, "-map", "[v]", "-map", "1:a",
                   "-af", f"apad=pad_dur={D:.2f}", "-c:v", "libx264", "-r", "25",
                   "-c:a", "aac", "-b:a", "128k", "-t", f"{D:.2f}", seg]
        subprocess.run(cmd, check=True)
        segs.append(seg); print(f"scene {i+1}/{len(SCENES)} {kind}: {D:.1f}s")
    lst = os.path.join(WORK, "concat.txt")
    open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
    out = os.path.join(HERE, "exam-builder-intro-v2.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)
    # poster: scene 2 composite
    p = slide_phone(1, "", "منشئ الاختبارات", "أداة مجانية بسيطة لعمل امتحان جاهز للطباعة")
    shot = Image.open(os.path.join(SHOTS, "json.png")).convert("RGB")
    shot = shot.resize((336, 727)).crop((0, 0, 336, PHONE_H))
    p.paste(shot, (PHONE_X, PHONE_Y)); p.alpha_composite if False else None
    bz = Image.open(BEZEL).convert("RGBA"); p = p.convert("RGBA"); p.alpha_composite(bz, (PHONE_X - 8, PHONE_Y - 8)); p = p.convert("RGB"); p.save(os.path.join(HERE, "poster-v2.png"))
    print("DONE", out, f"{os.path.getsize(out)/1e6:.1f} MB", f"total {dur(out):.0f}s")

if __name__ == "__main__":
    main()
