from odoo.odoo import http

class CenterPaysystemController(http.Controller):
    @http.route('/center_paysystem/students/', auth='public')
    def list_students(self, **kwargs):
        students = http.request.env['center_paysystem.student'].search([])
        return http.request.render('center_paysystem.student_listing', {'students': students})
