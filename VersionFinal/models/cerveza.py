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
    precio = fields.Float('Precio(por unidad)',compute='_compute_total_price')
    cant = fields.Integer(compute='_cantidadIngredientes', string='Cantidad de ingredientes', store=True) 
    cant2 = fields.Integer(compute='_cantidadPedidos', string='Cantidad de pedidos', store=True)     
    ingrediente_ids = fields.Many2many('upobeer.ingrediente', string='Ingredientes')
    pedido_ids = fields.One2many('upobeer.pedido','cerveza_id', 'NºPedidos')
    
    def _compute_total_price(self):
        for line in self:
            for ing in line.ingrediente_ids:
                line.precio = line.precio + ing.coste
            line.precio = line.precio * (1.22)
            
    @api.one
    @api.constrains('cant')
    def _check_capacity(self):
        if (self.cant) > 6:
            raise models.ValidationError('No puede haber más de 6 ingredientes por cerveza')
    
    @api.one
    @api.depends('ingrediente_ids')
    def _cantidadIngredientes(self):                             
        self.cant = len(self.ingrediente_ids)
    
    @api.one
    @api.depends('ingrediente_ids')
    def _cantidadPedidos(self):                             
        self.cant2 = len(self.pedido_ids)
    
    @api.onchange('cant','alcohol')
    def onchange_cerveza(self):
        resultado = {}
        if self.cant > 4 and self.alcohol == False:
            resultado = {'value': {'cant' : 4 },
                         'warning': {'title': 'Valores incorrectos',
                                     'message': 'Las cervezas sin alcohol solo pueden tener 4 ingredientes'}}
        return resultado
    
    def quitarIngrediente(self):         
        self.write({'ingrediente_ids':[ (5,  ) ]})    
        