from pdf417gen import encode, render_image, render_svg

# Some data to encode
text = """20600467124|01|F001|00000078|41.92|274.80|2016-10-21|6|20553703540|ONqVxrcnGq9BUsI1pYOWzMFxroI=|JLA+BsT+y5fgsKGruIRXcL8FWbIsNnR9eTQGBjS2VvZ2vciEJoDKr0JRBoXqxVWyZR6OK/e5AtPQXOZE7TEdlQ8zV8plaqCNjwgabCOpA7JEToEX84fZ4sxwQe+048Wgc+5mtk8MxfmrhOvxEfeTsGSz5N7JhFK80vD2uh4FaIwTI93Xiucfzvn7OqsD+LVA7kHAMqHC+6p7qgkhASXtYSQrxEReg0zMPVumaNhH+4hY86U5D77vEPtsWzWx4lklW0/qNLLPzYOGhjlTL4dzqdSuSw73r5ocZb/eXOtKW+OFGBcZYJkNFsgseHH81cFAL2qk5CrZr4N/3OYYWWxQNg==|"""

# Convert to code words
codes = encode(text, columns=13)

# Generate barcode as image
image = render_image(codes, scale=5)  # Pillow Image object
image.save('barcode.jpg')
