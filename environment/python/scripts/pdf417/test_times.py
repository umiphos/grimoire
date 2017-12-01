import sys
from timeit import default_timer as timer
from elaphe import barcode
from pdf417gen import encode, render_image
import treepoem

def elaphe_image(name, text):
    return barcode('pdf417', text, options=dict(eclevel=2, compact=True, columns=13), scale=5)

def treepoem_image(name, text):
    return treepoem.generate_barcode(
        barcode_type="pdf417", data=text,
        options={ 'columns': 13, 'height': 0.64, })

def pdf417gen_image(name, text):
    codes = encode(text, columns=13)
    return render_image(codes, scale=5)

image_name = sys.argv[1]
text = """20600467124|01|F001|00000078|41.92|274.80|2016-10-21|6|20553703540|ONqVxrcnGq9BUsI1pYOWzMFxroI=|JLA+BsT+y5fgsKGruIRXcL8FWbIsNnR9eTQGBjS2VvZ2vciEJoDKr0JRBoXqxVWyZR6OK/e5AtPQXOZE7TEdlQ8zV8plaqCNjwgabCOpA7JEToEX84fZ4sxwQe+048Wgc+5mtk8MxfmrhOvxEfeTsGSz5N7JhFK80vD2uh4FaIwTI93Xiucfzvn7OqsD+LVA7kHAMqHC+6p7qgkhASXtYSQrxEReg0zMPVumaNhH+4hY86U5D77vEPtsWzWx4lklW0/qNLLPzYOGhjlTL4dzqdSuSw73r5ocZb/eXOtKW+OFGBcZYJkNFsgseHH81cFAL2qk5CrZr4N/3OYYWWxQNg==|"""

# Calling elaphe
start = timer()
image = elaphe_image(elaphe_image, text)
image.save("%s_elaphe.jpg" % image_name)
end = timer()
print("The time take elaphe to create an image is:", end-start)

# Calling treepoem
start = timer()
image = treepoem_image(treepoem_image, text)
image.save("%s_treepoem.jpg" % image_name)
end = timer()
print("The time take treepoem to create an image is:", end-start)

# Calling pdf417gen
start = timer()
image = pdf417gen_image(treepoem_image, text)
image.save("%s_pdf417gen.jpg" % image_name)
end = timer()
print("The time take pdf417gen to create an image is:", end-start)
