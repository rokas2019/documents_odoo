from odoo import models, fields


class Document(models.Model):
    _name = 'my_library.document'
    _description = 'Library Document'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
