# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Envio (models.Model):
    _name = "upobeer.envio"
    
    name = fields.Char('ID Envio', size=6, required=True)
    fecha_sal = fields.Date('Fecha de salida', compute='_getFechaSalida')
    fecha_ent = fields.Date('Fecha de entrega', autodate=True,)
    state = fields.Selection([('sin_iniciar', 'Sin iniciar'),
                                     ('en_reparto', 'En reparto'),
                                     ('entregado', 'Entregado'),],
                                     'Estado del envio', default='sin_iniciar')
    direccion = fields.Char('Direccion',compute='_getDireccion')
    cP = fields.Char('Codigo postal',compute='_getCP')
    gastoEnvio = fields.Float('Gastos de envio',compute='_compute_total_price')
    total = fields.Float('Total envio',compute='_compute_total_price2')
    descripcion = fields.Text('Descripcion')
    pedido_id = fields.Many2one('upobeer.pedido', string='Pedido',required=True)
    emprep_id = fields.Many2one('upobeer.emprep', string='Empresa de reparto',required=True)
    
    @api.one
    def btn_submit_to_reparto(self):
        self.write({'state':'en_reparto'})
        self.pedido_id.state  = 'enviado'
    
    @api.one
    def btn_submit_to_entregado(self):
        self.write({'state':'entregado'})
        update_dia = datetime.today()
        self.fecha_ent = update_dia
    
    @api.one
    @api.constrains('pedido_id')
    def _check_pedidoEstado(self):
        if self.pedido_id.state !='terminado':
            raise models.ValidationError('Un pedido debe estar terminado para poder realizar el envio')
        
    def _compute_total_price(self):
        for line in self:
            line.gastoEnvio = (line.pedido_id.precioT * (1+(line.emprep_id.benef)/100)) - (line.pedido_id.precioT)
    
    def _compute_total_price2(self):
        for line in self:
            line.total = (line.gastoEnvio + line.pedido_id.precioT)

    def _getDireccion(self):
        for line in self:
            line.direccion = line.pedido_id.direccionCliente

    def _getCP(self):
        for line in self:
            line.cP = line.pedido_id.cpCliente
            
    def _getFechaSalida(self):
        for line in self:
            line.fecha_sal = line.pedido_id.fin
            
            