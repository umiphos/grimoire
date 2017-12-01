from elaphe import barcode

bc = barcode('pdf417', "Bienvenidos a poncesoft.blogspot.com", options=dict(eclevel=2, compact=True, columns=2, rows=10), margin=1, scale=2)
bc.save('test.png')
