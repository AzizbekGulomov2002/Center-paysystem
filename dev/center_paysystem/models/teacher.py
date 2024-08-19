from odoo import models, fields

class Teacher(models.Model):
    _name = 'center_paysystem.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    course_ids = fields.One2many('center_paysystem.course', 'teacher_id', string='Courses')
