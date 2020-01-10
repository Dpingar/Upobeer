# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Pedido(models.Model):
    _name = "upobeer.pedido"
    
    name = fields.Char("ID Pedido", size=10, required=True)
    cantidad = fields.Integer("Cantidad", required=True, default=1)
    state = fields.Selection([('sin_iniciar', 'Sin iniciar'),
                                     ('en_proceso', 'En proceso'),
                                     ('terminado', 'Terminado'),
                                     ('enviado', 'Enviado'), ],
                                     'Estado del pedido',
                                     default='sin_iniciar')
    inicio = fields.Date('Fecha pedido', autodate=True, required=True)
    fin = fields.Date('Terminado', autodate=True)
    precioT = fields.Float('Precio Total',compute='_compute_total_price')
    direccionCliente = fields.Char('Direccion',compute='_getDireccion')
    cpCliente = fields.Char('Codigo postal',compute='_getCP')
    descripcion = fields.Text('Descripcion')
    cant = fields.Integer(compute='_cantidadOperarios', string='Cantidad de operarios', store=True) 
    cerveza_id = fields.Many2one('upobeer.cerveza', string='Cerveza',required=True)
    cliente_id =  fields.Many2one('upobeer.cliente','Cliente',required=True)
    empresa_id = fields.Many2one('upobeer.empresa', string='Empresa',required=True)
    operario_ids =  fields.Many2many('upobeer.operario', string='Operarios')
    envio_ids = fields.One2many('upobeer.envio','pedido_id', 'NºEnvios')
    
    @api.one
    def btn_submit_to_proceso(self):
        self.write({'state':'en_proceso'})
    
    @api.one
    def btn_submit_to_terminado(self):
        self.write({'state':'terminado'})
        update_dia = datetime.today()
        self.fin = update_dia
        
    @api.one
    @api.depends('operario_ids')
    def _cantidadOperarios(self):                             
        self.cant = len(self.operario_ids)
    
    @api.onchange('cant','alcohol')
    def onchange_pedido(self):
        resultado = {}
        if self.cant > 2:
            resultado = {'value': {'cant' : 2 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Un pedido puede tener un maximo de 2 operarios'}}
        return resultado
    
        
    def _compute_total_price(self):
        for line in self:
            line.precioT = line.cantidad * (line.cerveza_id.precio)
    
    def _getDireccion(self):
        for line in self:
            line.direccionCliente = line.cliente_id.direccion
            
    def _getCP(self):
        for line in self:
            line.cpCliente = line.cliente_id.cp