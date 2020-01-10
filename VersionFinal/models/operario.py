# -*- coding: utf-8 -*-

from odoo import models, fields, api


class operario(models.Model):
    _name = 'upobeer.operario'
    
    name = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=60, required=True)
    dni = fields.Char('DNI', size=9, required=True)
    fecha_nac = fields.Date('Fecha de nacimiento', autodate=True, required=True)
    foto = fields.Binary('Foto')
    direccion = fields.Char('Direccion', size=60, required=True)
    cp = fields.Char('Codigo postal', size=5, required=True)
    tlf = fields.Char('Telefono', size=9)
    email = fields.Char('Email', size=60)
    id = fields.Char('ID Operario', size=4, required=True)
    tlf2 = fields.Char('Telefono de empresa', size=9, required=True)
    fecha_con = fields.Date('Contratado desde', autodate=True, required=True)
    empresa_id = fields.Many2one('upobeer.empresa', string='Empresa',required=True)
    pedido_ids = fields.Many2many('upobeer.pedido', string='Pedidos asignados')
    
    _sql_constraints = [('operario_dni_unique','UNIQUE (dni)','El dni debe ser único')]

    