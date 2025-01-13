import sys

from PIL import Image
from pyfiglet import Figlet

f = Figlet(font="slant")

print(f.renderText("Lahhapalagiini"))
if len(sys.argv) != 3:
    print("Error: missing argument")
    print("Usage: python conv.py image_file_path desired_bnw_image_file_path")
    print(
        "Example: python conv.py /home/lahh/relativity.jpg /home/lahh/relativity_bnw.jpg"
    )
    sys.exit(1)

img_path = sys.argv[1]
bnw_img_path = sys.argv[2]

print("[+] Converting image to black and white.")
try:
    img = Image.open(img_path)
    bw_img = img.convert("L")
    bw_img.save(bnw_img_path)
    print("[$] Image converted succesfully.")
except:
    print("[!] Failed to convert image.")
