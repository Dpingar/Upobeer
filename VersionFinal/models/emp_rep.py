# -*- coding: utf-8 -*-

from odoo import models, fields, api


class emp_rep(models.Model):
    _name = 'upobeer.emprep'

    name = fields.Char('Nombre', size=60, required=True)
    id = fields.Char('ID Empresa', size=4, required=True)
    cif = fields.Char('CIF', size=9, required=True)
    foto = fields.Binary('Foto')
    benef = fields.Integer('% Beneficios', required=True)
    fecha_cre = fields.Date('Fecha de creacion', autodate=True, required=True)
    direccion = fields.Char('Direccion', size=60, required=True)
    cp = fields.Char('Codigo postal', size=5, required=True)
    tlf = fields.Char('Telefono', size=9, required=True)
    email = fields.Char('Email', size=60)
    envio_ids = fields.One2many('upobeer.envio','emprep_id', 'Envios')
    
    _sql_constraints = [('empresa_rep_cif_unique','UNIQUE (cif)','El cif debe ser único')]
