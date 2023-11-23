from odoo import api, fields, models, _, api
import base64
import io
from zipfile import ZipFile


class BulkUpload(models.TransientModel):
    _name = "bulk.upload.wizard"
    _description = "Upload Bulk Documents or Images"

    file = fields.Binary('Upload File')
    file_name = fields.Char('File Name')
    select_update = fields.Many2one('ir.model.fields',string='Document Type')
    employee_ids = fields.Many2many("hr.employee", string="Employee")


    def upload_images(self):
        
        employees_name = [employee.name for employee in self.employee_ids]

        b64_data = base64.decodebytes(self.file)        # decodes the binary data 
        buffer= io.BytesIO(b64_data)                    # This buffer can then be used to open the ZIP file 
        zip_data = ZipFile(buffer)                      # This allows you to work with the contents of the ZIP file. 
        file_list = zip_data.namelist()                 # List all files in the ZIP archive

       
        try:
            for file in file_list:
                file_name = file.split('.')[0]

                employee_id = self.env['hr.employee'].search([('name','=',file_name)])
            
                if employee_id:
                    file_data = zip_data.read(file)
                    employee_id.write({self.select_update.name : base64.b64encode(file_data)})
            
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                        'type': 'success',
                        'message': _("Zip File Uploded Successfully"),
                        'sticky':False,
                        'next': {'type': 'ir.actions.act_window_close'},
                        }
                    }
                    
        except Exception as error:
            
            return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'type': 'war',
                        'message': error,
                        'sticky':True,
                        'next': {'type': 'ir.actions.act_window_close'},
                            }
                    }