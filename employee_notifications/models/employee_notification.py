from odoo import models, api, fields
from datetime import datetime

class EmployeeNotification(models.Model):
    _inherit = 'hr.employee'

    employee_date_of_joining = fields.Date(string='Date of Joining')

    @api.model
    def send_anniversary_birthday_notifications(self):
        today = datetime.today()
        employees = self.search([])
        for emp in employees:
            # Birthday check
            if emp.birthday and emp.birthday.month == today.month and emp.birthday.day == today.day:
                emp._send_notification_email('birthday')

            # Anniversary check
            if emp.employee_date_of_joining and emp.employee_date_of_joining.month == today.month and emp.employee_date_of_joining.day == today.day:
                emp._send_notification_email('anniversary')

    def _send_notification_email(self, notification_type):
        template_xml_id = 'employee_notifications.mail_template_employee_' + notification_type
        template = self.env.ref(template_xml_id, raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=True)