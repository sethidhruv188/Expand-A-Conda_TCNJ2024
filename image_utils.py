from PIL import Image, ImageOps, ImageEnhance
from io import BytesIO
import base64

def decode_base64_image(base64_str):
    return Image.open(BytesIO(base64.b64decode(base64_str)))
