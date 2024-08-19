from odoo import models, fields

# Student modeli
class Student(models.Model):
    _name = 'center_paysystem.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    group_ids = fields.Many2many('center_paysystem.group', string='Groups')
    payment_ids = fields.One2many('center_paysystem.payment', 'student_id', string='Payments')


# Teacher modeli
class Teacher(models.Model):
    _name = 'center_paysystem.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    course_ids = fields.One2many('center_paysystem.course', 'teacher_id', string='Courses')


# Course modeli
class Course(models.Model):
    _name = 'center_paysystem.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Many2one('center_paysystem.teacher', string='Teacher')
    group_ids = fields.One2many('center_paysystem.group', 'course_id', string='Groups')


# Group modeli
class Group(models.Model):
    _name = 'center_paysystem.group'
    _description = 'Group'

    name = fields.Char(string='Name', required=True)
    course_id = fields.Many2one('center_paysystem.course', string='Course')
    student_ids = fields.Many2many('center_paysystem.student', string='Students')
    payment_ids = fields.One2many('center_paysystem.payment', 'group_id', string='Payments')


# Payment modeli
class Payment(models.Model):
    _name = 'center_paysystem.payment'
    _description = 'Payment'

    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Date', required=True)
    description = fields.Text(string='Description')
    student_id = fields.Many2one('center_paysystem.student', string='Student', required=True)
    group_id = fields.Many2one('center_paysystem.group', string='Group', required=True)
