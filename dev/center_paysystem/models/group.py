from odoo import models, fields

class Group(models.Model):
    _name = 'center_paysystem.group'
    _description = 'Group'

    name = fields.Char(string='Name', required=True)
    course_id = fields.Many2one('center_paysystem.course', string='Course')
    student_ids = fields.Many2many('center_paysystem.student', string='Students')
    payment_ids = fields.One2many('center_paysystem.payment', 'group_id', string='Payments')
