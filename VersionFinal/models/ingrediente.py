# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ingrediente (models.Model):
    _name = 'upobeer.ingrediente'
    
    name = fields.Char('Nombre', size=60, required=True)
    idingrediente = fields.Char('ID Ingrediente', size=3, required=True)
    foto = fields.Binary('Foto')
    coste = fields.Float('Coste(por cerveza)', required=True)
    tipo = fields.Selection([('malta', 'Malta'),
                               ('agua', 'Agua'),
                               ('lupulo', 'Lúpulo'),
                               ('especias', 'Especias'),
                               ('levadura', 'Levadura'), ],
                                'Tipologia del ingrediente')
    cerveza_ids = fields.Many2many('upobeer.cerveza', string='Cervezas')
    
    _sql_constraints = [('ingrediente_id_unique','UNIQUE (idingrediente)','El ID debe ser único')]
