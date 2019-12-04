
from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    cod_id = fields.Char(
        string="Codigo",
        required=True
    )
    cod_version = fields.Integer(
        string="Version",
        required=True
    )
    cod_date = fields.Date(
        string="Fecha",
        required=True
    )
    