from odoo import models, fields

class Course(models.Model):
    _name = 'center_paysystem.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Many2one('center_paysystem.teacher', string='Teacher')
    group_ids = fields.One2many('center_paysystem.group', 'course_id', string='Groups')
