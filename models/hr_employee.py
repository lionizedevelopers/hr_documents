from odoo import models, fields,api,_
from odoo.exceptions import ValidationError
from datetime import date

class EmployeeWishes(models.Model):
    _inherit = "hr.employee"
    
    aadharcard = fields.Binary(string="Aadhar card")
    pancard = fields.Binary(string="Pan card")
    document_ids = fields.Many2many('ir.attachment',string='Documents')

    def bulk_upload(self):

            return {
            'name': 'Bulk Upload',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            "view_type": "form",
            'res_model': 'bulk.upload.wizard',
            'target': 'new',
            'view_id': self.env.ref('hr_documents.wizard_view_multi_image_upload').id,
            'context': {'default_employee_ids': self.ids},
        }