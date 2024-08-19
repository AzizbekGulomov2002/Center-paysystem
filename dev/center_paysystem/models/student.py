from odoo.odoo import models, fields


class Student(models.Model):
    _name = 'center_paysystem.student'

    name = fields.Char(string="Name")
    date_of_birth = fields.Date(string="Date of Birth")
    group_ids = fields.Many2many('center_paysystem.group', string="Groups")
    payment_ids = fields.One2many('center_paysystem.payment', 'student_id', string="Payments")
