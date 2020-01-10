# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = 'upobeer.cliente'

    name = fields.Char('Nombre', size=60, required=True)
    id = fields.Char('ID Cliente', size=4, required=True)
    apellidos = fields.Char('Apellidos', size=60, required=True)
    dni = fields.Char('DNI', size=9, required=True)
    fecha_nac = fields.Date('Fecha de nacimiento', autodate=True, required=True)
    foto = fields.Binary('Foto')
    direccion = fields.Char('Direccion', size=60, required=True)
    cp = fields.Char('Codigo postal', size=5, required=True)
    tlf = fields.Char('Telefono', size=9, required=True)
    email = fields.Char('Email', size=60)
    desde = fields.Date('Miembro desde', autodate=True, required=True)
    pedido_ids = fields.One2many('upobeer.pedido','cliente_id', 'Pedidos') 
    
    _sql_constraints = [('cliente_dni_unique','UNIQUE (dni)','El dni debe ser único')]
