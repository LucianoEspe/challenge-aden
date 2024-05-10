from odoo import models, fields, api

class Programa(models.Model):
    _name = "aden.programa"
    _description = "aden.programa"
    _rec_name = 'nombre'
    
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripcion')