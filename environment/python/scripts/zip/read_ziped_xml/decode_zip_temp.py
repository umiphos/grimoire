import zipfile
import base64

# from lxml import etree
import lxml
from lxml.objectify import fromstring
import tempfile
"""Links and comments
https://pymotw.com/2/zipfile/


"""

encoded_file = "UEsDBBQAAgAIAJirhUoAAAAAAgAAAAAAAAAGAAAAZHVtbXkvAwBQSwMEFAACAAgAmKuFSpWhJyPJAwAAoAsAACIAAABSLTIwNTU3OTEyODc5LTAxLUYwMDEtMDAwMDAwMDIueG1stZZbc9o4FMff+yk85qEznXUkm6s9QIdA0rJJ02wC3c6+KbYAdW3JlWQu/fQr+YZNnSl0ZoEH+eic3zn660hm+H4fhcYWc0EYHZn2FTQNTH0WELoemcvFrTUw34/fDBH3JnEcEh9J5fiERcyowIYKpsJDfGQmnHoMCSI8iiIsPBFjn6xyfy95CT3hb3CEvL0ImlCWY+Y0vJcX4qYsihi92UtM9TLUo0JiKsUR6r/4vwW9Vu5+IxD9HnCyXnO8RhI3QQMxMjdSxh4Au93uate+YnwNHAghgC5QPoEg61bhLRiKS/8skbhSU9qeBuoBwHSLQxZjYI6HSlpveX1fKiV+NmWWipZUjeR4+EzWFMmE53t+Vp2qb3QYDuZ0xcZvDGM4RZRRpU9IfqQafcJywwJjEq4ZJ3ITvYK1gQ011sJ73/LtDm39rby1oFo/E6TsssKzobBT1GpFjOMWF8gSG9S1nRz5hFeYq+OAjeXTfGSa2qjMC46oWDEeicxQNf0ybU2iYnMCSxTVZ6kvhJ4jkAKC08qHM7LGQl6omFKkVdWp5HxBYYLHW44//hUJsvnQa7evv80Oix9RuO2zw+rxrrP8/B1+dW5v7g6Dw8f2597ii/9p8o3/+YFsbpKViPfz+1nI29MXOrsL/3Hjvu8wNk3objQagmoWvT+g3CDVaqDea9WOyCLePXKyVSfP+BcfjLfXWKJHdUTV8cZcvjUok0YSv8swlajhHT6kzOHXLnRnSKJspKOys67ID+r4B4Z/NOX8LKEiVPinwSltLkSC+TPmBIVViwZfjq/EpqyM+5BEL5hfTqtFVxMU5YKjMqBU66ijGjffKeDnywc0XFHq7vbms7Hdce1Op9t3XAgHQ5Bbs1ldzkyL6UC7b8GOBXu5RzlzdFwQpQuEXvqruKX21K14KdWR3cy3NllzTwGO7TkDr+PWnXM28r2KLPkStOV5+TBZVBZVOjJ+eERcHjJbOpwHSr3yNVNiVJ1t9XXcbvcIAq9HFRNZm+iAdFSpJJsBJ57gteLU6SQSheUCJ1IifxOlW63n9Z5yisLjoU2zqqt13DrRQNuyRA1B4FfJwKnO+hHTAPP/R0rQmOAJ+5hsL8jZ7fZd2xn03bNzNqSYMT/RKhSNV9RSPqVNmWupUtyqa92C2ccpevY4XevvKQvUwak3dmpLvWZY+JzEaXn3yLhFvlIfGVSVw5lRy/OHsUGGIAEzkI9jiQKUQauIYoXVZRwXV+ug5mWU+jVFZeKRmCj7mRvUs2xo9zrQhd3B4JItqmUBzZsEmv9gj/8DUEsBAgAAFAACAAgAmKuFSgAAAAACAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAGR1bW15L1BLAQIAABQAAgAIAJirhUqVoScjyQMAAKALAAAiAAAAAAAAAAEAAAAAACYAAABSLTIwNTU3OTEyODc5LTAxLUYwMDEtMDAwMDAwMDIueG1sUEsFBgAAAAACAAIAhAAAAC8EAAAAAA=="


with tempfile.temporaryfile(r as zip_file):
    deco = encoded_file.decode('base64')
    zip_file.write(deco)
    zr = zipfile.ZipFile(zip_file,'r')
    # zip_file.close()
    import ipdb;ipdb.set_trace()
    name_cableao = zr.namelist()
    readed = zr.read(name_cableao[1])
    doc = lxml.objectify.XML(readed)
    rawxDdX = raw_input("write the cbc to return")
    print doc.xpath("//cbc:ResponseCode",
              namespaces={
                  'cac':'urn.oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
                  'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
              })
    # print doc.xpath("//cbc:"+rawxDdX,
    #         namespaces={'cac':'urn.oasis:names:specification: ubl:schema:xsd:CommonAggregateComponents-2',
    #                     'cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    #                     })
