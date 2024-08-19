from odoo import models, fields

class Payment(models.Model):
    _name = 'center_paysystem.payment'
    _description = 'Payment'

    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Date', required=True)
    description = fields.Text(string='Description')
    student_id = fields.Many2one('center_paysystem.student', string='Student', required=True)
    group_id = fields.Many2one('center_paysystem.group', string='Group', required=True)
