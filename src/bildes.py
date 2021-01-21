import sys
import os
from PIL import Image

def cartoon(pix):
    return pix if pix > 100 else 250                    

def bilzu_info(mape, atvert=False):
    datnes = os.listdir(mape)
    for infile in datnes:
        try:
            with Image.open(os.path.join(mape,infile)) as im:
                print(infile, im.format, f"{im.size}x{im.mode}")
                if atvert:
                    im2 = Image.eval(im, cartoon)
                    im2.show()
        except OSError:
            pass


def sikteli(mape):
    datnes = os.listdir(mape)
    size = (128, 128)
    for infile in datnes:
        if not infile.find(".thumbnail") > 0:
            try:
                with Image.open(os.path.join(mape,infile)) as im:
                    outfile = infile + ".thumbnail."+im.format
                    im.thumbnail(size)
                    im.save(os.path.join(mape,outfile), im.format)
            except OSError:
                print("cannot create thumbnail for", infile)


def bilde():
    from PIL import Image
    datne = "bilde.jpg"
    izmers = (100, 100)
    with Image.open(datne) as im:
        print(datne, im.format, f"{im.size}x{im.mode}")
        im.show()
        im.thumbnail(izmers)
        im.save("bilde-maza.jpg", im.format)
        im.show()
