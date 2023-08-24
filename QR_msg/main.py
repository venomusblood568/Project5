# pip instll qrcode
import qrcode
from qrcode.image.styledpil import StyledPilImage
# Square,gapped,circle,rounded,vertical and horizontal are differnt style of QR
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer
from qrcode.image.styles.moduledrawers.pil import GappedSquareModuleDrawer
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer
from qrcode.image.styles.moduledrawers.pil import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
#input message for the QR
message = input("enter your message here: ")
#for embedding the text message in the QR code 
qr.add_data(message)
#properties defined for making the QR code
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=VerticalBarsDrawer(),
    color_mask = RadialGradiantColorMask())
    #note for changing the color pattern you can just change the color_mask 
    #color_mask = SolidFillColorMask()
    #color_mask = squareGradiantMask()
    #color_mask = HorizontalGradiantMask()
    #Color_mask = VerticalGradientMask() 
    
# for making the img using pil
type(img)  # qrcode.image.pil.PilImage
#for taking the input for file name 
file_name = input("enter the file name: ")
# saving file with the extension of .png
img.save(file_name+".png")
