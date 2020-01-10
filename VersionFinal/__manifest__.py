# -*- coding: utf-8 -*-
{
    'name': "UpoBeer",
    'summary': """Administración de UpoBeer""",
    'description': """Administración de pedidos,clientes,cervezas,empresas...""",
    'author': "Grupo 13",
    'category': 'UpoBeer',
    'version': '2.0',
    'depends': ['base'],
    'data': ['views/cliente_view.xml','views/cerveza_view.xml','views/pedido_view.xml','views/ingrediente_view.xml','views/empresa_view.xml','views/operario_view.xml','views/envio_view.xml','views/emp_rep_view.xml'],
    'demo': ['demo/upobeer_expansion_demo.xml'],
    'application': True,
}