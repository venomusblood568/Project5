# pip instll qrcode
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
message = input("enter your message here: ")
qr.add_data(message)
img = qr.make_image(image_factory=StyledPilImage,module_drawer=VerticalBarsDrawer(),color_mask = RadialGradiantColorMask())
type(img)  # qrcode.image.pil.PilImage
file_name = input("enter the file name: ")
img.save(file_name+".png")
