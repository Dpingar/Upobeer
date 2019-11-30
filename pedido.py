# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pedido(models.Model):
    _name = "upobeer.pedido"
    
    name = fields.Char("ID Pedido", size=4, required=True)
    cantidad = fields.Integer("Cantidad", required=True, default=1)
    estado = fields.Selection([('sin_iniciar', 'Sin iniciar'),
                                     ('en_proceso', 'En proceso'),
                                     ('pausado', 'Pausado'),
                                     ('terminado', 'Terminado'),
                                     ('enviado', 'Enviado'), ],
                                     'Estado del pedido')
    inicio = fields.Date('Fecha pedido', autodate=True, required=True)
    fin = fields.Date('Terminado', autodate=True)
    precioT = fields.Float('Precio Total',compute='_compute_total_price')
    direccionCliente = fields.Char('Direccion',compute='_getDireccion')
    cpCliente = fields.Char('Codigo postal',compute='_getCP')
    descripcion = fields.Text('Descripcion')
    cerveza_id = fields.Many2one('upobeer.cerveza', string='Cerveza',required=True)
    cliente_id =  fields.Many2one('upobeer.cliente','Cliente',required=True)
    
    def _compute_total_price(self):
        for line in self:
            line.precioT = line.cantidad * (line.cerveza_id.precio)
    
    def _getDireccion(self):
        for line in self:
            line.direccionCliente = line.cliente_id.direccion
            
    def _getCP(self):
        for line in self:
            line.cpCliente = line.cliente_id.cp