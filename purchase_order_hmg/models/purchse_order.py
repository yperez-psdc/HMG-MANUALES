# -*- coding: utf-8 -*-

from odoo import models, fields, api

class purchase_order_hmg(models.Model):
    _inherit = 'purchase.order'

    ship_via = fields.Many2one(
        "ship.via",
        string="Enviar a:",
        required=True
    )
    expirate = fields.Many2one(
        "exp.date",
        string="Terminos:",
        required=True
    )
    oc1 = fields.Selection(
        string="O/C",
        required=True,
        selection=[('No. Contrato', 'No. Contrato'),('No. Licitación', 'No. Licitación'),
        ('No. Requisición', 'No. Requisición'),('Stock', 'Stock'),('Acto', 'Acto')]
    )
    oc2 = fields.Char(
        string=" ",
        required=True
    )
    payment = fields.Selection(
        string="Metodo de Pago:",
        required=True,
        selection=[('Cheque', 'Cheque'),('Tarjeta de credito', 'Tarjeta de credito'),
        ('Transferencia bancaria', 'Transferencia bancaria'),('Cuenta abierta', 'Cuenta abierta'),
        ('Número de tarjeta', 'Número de tarjeta'),('Titular de la tarjeta', 'Titular de la tarjeta')]
    )
    prepared = fields.Many2one(
        'res.users',
        string='Preparado por:',
        readonly=True,
        default=lambda self: self.env.user.id,
    )
    employee = fields.Many2one(
        'hr.employee',
        string="Vendedor:",
        required=True,
    )

class ShipVia(models.Model):
    _name = 'ship.via'

    name = fields.Char(
        string="Nombre",
        requerid=True
    )

class ExpDate(models.Model):
    _name = 'exp.date'

    name = fields.Char(
        string="Texto",
        requerid=True
    )