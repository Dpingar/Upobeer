# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cerveza (models.Model):
    _name = 'upobeer.cerveza'

    name = fields.Char('Nombre', size=60, required=True)
    idcerveza = fields.Char('ID Cerveza', size=3, required=True)
    foto = fields.Binary('Foto')
    alcohol = fields.Boolean("Alcohol", default=True, required=True)
    maduracion = fields.Integer("Años de maduracion", required=True)
    envasado = fields.Date('Fecha envasado', autodate=True, required=True)
    precio = fields.Float('Precio(por unidad)', required=True)
    pedido_ids = fields.One2many('upobeer.pedido','cerveza_id', 'Cervezas') 
