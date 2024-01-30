import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("TESTE", image_factory=factory)
svg_img.save("moreqr.svg")