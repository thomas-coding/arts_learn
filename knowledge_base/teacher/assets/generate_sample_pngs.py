from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ASSETS = Path(__file__).resolve().parent


def get_font(size: int):
    candidates = [
        "DejaVuSans.ttf",
        "arial.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibri.ttf",
    ]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_header(draw: ImageDraw.ImageDraw, title: str, subtitle: str, width: int) -> None:
    draw.text((70, 40), title, fill=(24, 35, 52), font=get_font(44))
    draw.text((70, 96), subtitle, fill=(88, 97, 115), font=get_font(24))
    draw.line((70, 132, width - 70, 132), fill=(206, 213, 224), width=3)


def draw_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str) -> None:
    x1, y1, _, _ = box
    draw.rounded_rectangle(box, radius=18, outline=(195, 204, 220), width=3, fill=(255, 255, 255))
    draw.text((x1 + 16, y1 + 14), title, fill=(33, 44, 62), font=get_font(24))


def build_l003() -> None:
    width, height = 1800, 1200
    img = Image.new("RGB", (width, height), (245, 247, 252))
    d = ImageDraw.Draw(img)

    draw_header(
        d,
        "L003 One-Point Perspective Sample",
        "Teacher visual sample: correct flow, common errors, quick checks",
        width,
    )
    p1 = (70, 170, 1160, 760)
    p2 = (1200, 170, 1730, 760)
    p3 = (70, 790, 1730, 1130)
    draw_panel(d, p1, "A. Correct Example")
    draw_panel(d, p2, "B. Common Errors")
    draw_panel(d, p3, "C. Checklist")

    horizon_y = 420
    vp = (640, horizon_y)
    d.line((120, horizon_y, 1110, horizon_y), fill=(108, 120, 150), width=3)
    d.ellipse((vp[0] - 8, vp[1] - 8, vp[0] + 8, vp[1] + 8), fill=(50, 73, 120))
    d.text((vp[0] + 14, vp[1] - 12), "VP", fill=(50, 73, 120), font=get_font(20))
    d.text((124, 390), "Horizon", fill=(108, 120, 150), font=get_font(18))

    front = [(260, 470), (440, 470), (440, 640), (260, 640)]
    d.polygon(front, outline=(37, 55, 94), fill=(240, 245, 255), width=4)
    for x, y in front:
        d.line((x, y, vp[0], vp[1]), fill=(130, 148, 184), width=2)

    back = [(510, 450), (620, 450), (620, 560), (510, 560)]
    d.polygon(back, outline=(37, 55, 94), fill=(235, 241, 252), width=4)
    for i in range(4):
        d.line((front[i][0], front[i][1], back[i][0], back[i][1]), fill=(37, 55, 94), width=3)

    d.text((740, 470), "High view: see bottom", fill=(60, 73, 95), font=get_font(20))
    d.rectangle((740, 520, 900, 620), outline=(55, 78, 120), width=3)
    d.line((740, 620, 900, 620), fill=(55, 78, 120), width=5)
    d.text((740, 640), "Low view: see top", fill=(60, 73, 95), font=get_font(20))
    d.rectangle((740, 680, 900, 760), outline=(55, 78, 120), width=3)
    d.line((740, 680, 900, 680), fill=(55, 78, 120), width=5)

    d.text((1220, 240), "Error 1: Diverging depth lines", fill=(120, 45, 45), font=get_font(20))
    d.rectangle((1235, 280, 1340, 380), outline=(90, 90, 90), width=3)
    d.line((1235, 280, 1520, 250), fill=(179, 56, 56), width=3)
    d.line((1340, 280, 1520, 300), fill=(179, 56, 56), width=3)
    d.line((1235, 380, 1510, 450), fill=(179, 56, 56), width=3)
    d.line((1340, 380, 1520, 430), fill=(179, 56, 56), width=3)

    d.text((1220, 480), "Error 2: Moving horizon", fill=(120, 45, 45), font=get_font(20))
    d.line((1230, 530, 1700, 530), fill=(180, 90, 90), width=3)
    d.line((1230, 600, 1700, 640), fill=(180, 90, 90), width=3)
    d.text((1230, 655), "Use ONE horizon in one exercise", fill=(120, 45, 45), font=get_font(18))

    checks = [
        "1) All depth edges must converge to ONE VP.",
        "2) Keep one horizon line for all objects in this page.",
        "3) Build structure first, contour later.",
        "4) Independent test: no sample reference.",
    ]
    y = 860
    for line in checks:
        d.text((110, y), line, fill=(40, 53, 72), font=get_font(28))
        y += 64

    img.save(ASSETS / "L003_sample_sheet.png")


def build_l004() -> None:
    width, height = 1800, 1200
    img = Image.new("RGB", (width, height), (246, 248, 251))
    d = ImageDraw.Draw(img)

    draw_header(
        d,
        "L004 3-Value Shading Sample",
        "Teacher visual sample: value grouping, noisy-gray fix, checks",
        width,
    )
    p1 = (70, 170, 1160, 760)
    p2 = (1200, 170, 1730, 760)
    p3 = (70, 790, 1730, 1130)
    draw_panel(d, p1, "A. Correct Example")
    draw_panel(d, p2, "B. Common Errors")
    draw_panel(d, p3, "C. Checklist")

    d.text((120, 232), "3-Value setup", fill=(45, 55, 70), font=get_font(22))
    swatches = [(236, 236, 236), (150, 150, 150), (66, 66, 66)]
    labels = ["Light", "Mid", "Dark"]
    x = 120
    for color, label in zip(swatches, labels):
        d.rectangle((x, 270, x + 150, 350), fill=color, outline=(90, 90, 90), width=2)
        d.text((x + 40, 360), label, fill=(65, 65, 65), font=get_font(18))
        x += 190

    d.text((120, 430), "Sphere", fill=(45, 55, 70), font=get_font(20))
    d.ellipse((120, 460, 320, 660), fill=(180, 180, 180), outline=(80, 80, 80), width=3)
    d.pieslice((120, 460, 320, 660), 110, 250, fill=(235, 235, 235))
    d.pieslice((120, 460, 320, 660), -30, 90, fill=(80, 80, 80))
    d.ellipse((290, 640, 400, 700), fill=(100, 100, 100))

    d.text((420, 430), "Cube", fill=(45, 55, 70), font=get_font(20))
    d.polygon([(440, 500), (620, 500), (620, 660), (440, 660)], fill=(210, 210, 210), outline=(70, 70, 70), width=3)
    d.polygon([(620, 500), (730, 450), (730, 610), (620, 660)], fill=(150, 150, 150), outline=(70, 70, 70), width=3)
    d.polygon([(440, 500), (550, 450), (730, 450), (620, 500)], fill=(235, 235, 235), outline=(70, 70, 70), width=3)
    d.polygon([(620, 660), (730, 610), (760, 680), (650, 730)], fill=(90, 90, 90))

    d.text((820, 430), "Cylinder", fill=(45, 55, 70), font=get_font(20))
    d.ellipse((850, 465, 1040, 525), fill=(225, 225, 225), outline=(70, 70, 70), width=3)
    d.rectangle((850, 495, 1040, 655), fill=(165, 165, 165), outline=(70, 70, 70), width=3)
    d.ellipse((850, 625, 1040, 685), fill=(95, 95, 95), outline=(70, 70, 70), width=3)
    d.rectangle((1040, 560, 1130, 620), fill=(100, 100, 100))

    d.text((1220, 240), "Error 1: Muddy middle gray", fill=(120, 45, 45), font=get_font(20))
    for i in range(8):
        x1 = 1230 + i * 55
        y1 = 300 + (i % 3) * 35
        shade = 115 + (i % 4) * 12
        d.rectangle((x1, y1, x1 + 80, y1 + 80), fill=(shade, shade, shade), outline=(100, 100, 100))
    d.text((1220, 500), "Fix: reset to 3 clear groups first", fill=(120, 45, 45), font=get_font(18))

    d.text((1220, 560), "Error 2: Shadow direction mismatch", fill=(120, 45, 45), font=get_font(20))
    d.ellipse((1240, 600, 1320, 660), fill=(160, 160, 160))
    d.polygon([(1320, 630), (1400, 610), (1420, 645), (1340, 670)], fill=(90, 90, 90))
    d.ellipse((1450, 600, 1530, 660), fill=(160, 160, 160))
    d.polygon([(1440, 650), (1370, 675), (1390, 700), (1460, 675)], fill=(90, 90, 90))

    checks = [
        "1) Keep one light direction for all objects.",
        "2) Block in Light / Mid / Dark before details.",
        "3) If muddy: increase light-dark separation first.",
        "4) Independent test: no sample reference.",
    ]
    y = 860
    for line in checks:
        d.text((110, y), line, fill=(40, 53, 72), font=get_font(28))
        y += 64

    img.save(ASSETS / "L004_sample_sheet.png")


def build_l005() -> None:
    width, height = 1800, 1200
    img = Image.new("RGB", (width, height), (245, 248, 252))
    d = ImageDraw.Draw(img)

    draw_header(
        d,
        "L005 Two-Point Perspective Sample",
        "Teacher visual sample: corner-first box, prop placement, checks",
        width,
    )
    p1 = (70, 170, 1160, 760)
    p2 = (1200, 170, 1730, 760)
    p3 = (70, 790, 1730, 1130)
    draw_panel(d, p1, "A. Correct Example")
    draw_panel(d, p2, "B. Common Errors")
    draw_panel(d, p3, "C. Checklist")

    horizon_y = 420
    left_vp = (140, horizon_y)
    right_vp = (1110, horizon_y)
    d.line((120, horizon_y, 1110, horizon_y), fill=(108, 120, 150), width=3)
    d.ellipse((left_vp[0] - 7, horizon_y - 7, left_vp[0] + 7, horizon_y + 7), fill=(45, 70, 120))
    d.ellipse((right_vp[0] - 7, horizon_y - 7, right_vp[0] + 7, horizon_y + 7), fill=(45, 70, 120))
    d.text((154, horizon_y - 24), "VP-L", fill=(45, 70, 120), font=get_font(18))
    d.text((1020, horizon_y - 24), "VP-R", fill=(45, 70, 120), font=get_font(18))

    corner_top = (620, 470)
    corner_bottom = (620, 680)
    d.line((corner_top[0], corner_top[1], corner_bottom[0], corner_bottom[1]), fill=(34, 53, 96), width=4)
    for y in (470, 680):
        d.line((620, y, left_vp[0], horizon_y), fill=(126, 143, 177), width=2)
        d.line((620, y, right_vp[0], horizon_y), fill=(126, 143, 177), width=2)

    left_cut_top = (500, 500)
    left_cut_bottom = (500, 700)
    right_cut_top = (760, 510)
    right_cut_bottom = (760, 705)
    d.line((left_cut_top[0], left_cut_top[1], left_cut_bottom[0], left_cut_bottom[1]), fill=(34, 53, 96), width=4)
    d.line((right_cut_top[0], right_cut_top[1], right_cut_bottom[0], right_cut_bottom[1]), fill=(34, 53, 96), width=4)
    d.line((left_cut_top[0], left_cut_top[1], right_vp[0], horizon_y), fill=(126, 143, 177), width=2)
    d.line((left_cut_bottom[0], left_cut_bottom[1], right_vp[0], horizon_y), fill=(126, 143, 177), width=2)
    d.line((right_cut_top[0], right_cut_top[1], left_vp[0], horizon_y), fill=(126, 143, 177), width=2)
    d.line((right_cut_bottom[0], right_cut_bottom[1], left_vp[0], horizon_y), fill=(126, 143, 177), width=2)

    d.text((140, 520), "Corner first", fill=(60, 73, 95), font=get_font(20))
    d.text((140, 610), "Book + Phone inside perspective boxes", fill=(60, 73, 95), font=get_font(20))
    d.rectangle((150, 640, 260, 710), outline=(60, 86, 124), width=3)
    d.rectangle((280, 655, 370, 700), outline=(60, 86, 124), width=3)

    d.text((1220, 240), "Error 1: Both edge groups to one VP", fill=(120, 45, 45), font=get_font(20))
    d.line((1260, 330, 1610, 320), fill=(180, 56, 56), width=3)
    d.line((1260, 430, 1610, 320), fill=(180, 56, 56), width=3)
    d.line((1360, 300, 1610, 320), fill=(180, 56, 56), width=3)
    d.line((1360, 440, 1610, 320), fill=(180, 56, 56), width=3)

    d.text((1220, 520), "Error 2: No stable near corner", fill=(120, 45, 45), font=get_font(20))
    d.polygon([(1270, 610), (1380, 590), (1440, 690), (1290, 720)], outline=(180, 56, 56), fill=(248, 225, 225), width=3)
    d.text((1220, 700), "Fix: draw a vertical near corner first", fill=(120, 45, 45), font=get_font(18))

    checks = [
        "1) Left edges -> VP-L, right edges -> VP-R.",
        "2) Start from a clear near vertical corner.",
        "3) Build prop structure before contour details.",
        "4) Independent test: no sample reference.",
    ]
    y = 860
    for line in checks:
        d.text((110, y), line, fill=(40, 53, 72), font=get_font(28))
        y += 64

    img.save(ASSETS / "L005_sample_sheet.png")


if __name__ == "__main__":
    build_l003()
    build_l004()
    build_l005()
    print("Generated L003/L004/L005 PNG sample sheets.")
