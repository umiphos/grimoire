from . import openacademy_course

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
