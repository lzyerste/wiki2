from PIL import Image, ImageDraw, ImageFont
import os
import sys
import datetime as dt


def get_size(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)


def gen_text(date=None):
    # date
    if not date:
        date = dt.datetime.now().strftime("%m-%d")
    fpath = os.path.join("text", date + ".txt")
    if not os.path.exists(fpath):
        return None
    with open(fpath, encoding='utf8') as f:
        lines = [_.strip() for _ in f.readlines() if _.strip() != ""]

    # title = lines[0] + '（'

    # dynasty = lines.pop(1)
    # index = dynasty.find('：')
    # if index >= 0:
    #     dynasty = dynasty[index + 1:]
    #     if dynasty.endswith('代'):
    #         dynasty = dynasty[:-1]

    # title += dynasty + '·'

    # author = lines.pop(1)
    # index = author.find('：')
    # if index >= 0:
    #     author = author[index + 1:]

    # title += author + '）'

    # lines[0] = title

    return '\n\n'.join(lines)


if __name__ == '__main__':
    # gen text
    text = gen_text()
    tmrrw = dt.datetime.now() + dt.timedelta(1)
    tomorrow = gen_text(tmrrw.strftime("%m-%d"))

    if not text:
        print("Error: no text!")
        sys.exit(1)

    im = Image.open('base.jpg')
    p_w, p_h = im.size
    fontname = os.path.join("fonts", "simkai.ttf")
    # fontsize = 64
    fontsize = 54
    # text_color = (120, 146, 98)  # 竹青
    text_color = (73, 65, 102)  # 黛, good
    # text_color = (212, 242, 232)  # 水绿，太淡
    # text_color = "#DD3B44"  # 银朱，效果可以
    # text_color = "#1b54f2"  # 靛蓝，效果可以
    # text_color = "#008e59"  # 鹦鹉绿，效果可以
    # text_color = "#e7693f"  # 桔红
    # text_color = "#eb652d"  # 章丹
    # text_color = "#e8853b"  # 橘黄
    # text_color = "#FF0000"
    font = ImageFont.truetype(fontname, fontsize)
    d = ImageDraw.Draw(im)
    d.text((p_w * 0.2, p_h * 0.03), text, fill=text_color, font=font)
    # if tomorrow:
    #     d.text((p_w * 0.6, p_h * 0.06), tomorrow, fill=text_color, font=font)

    im = im.resize((1920, 1080), Image.ANTIALIAS)
    # im.show()
    im.save("today.jpg", "JPEG", quality=95)

    print("DONE!")




# text_color = "black"
# text_color = (115, 151, 156)
# text_color = (120, 146, 98)
# text_color = "#228B22"
# colorOutline = "red"
# colorBackground = "white"

# font = ImageFont.truetype(fontname, fontsize)
# width, height = get_size(text, font)


# d = ImageDraw.Draw(im)
# d.text((p_w * 0.2, p_h * 0.06), text, fill=text_color, font=font)

# im.show()

# # im = im.resize((1920, 1080))

# im.save("today.jpg", "JPEG", quality=100)
