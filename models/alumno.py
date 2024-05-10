from odoo import models, fields, api

class Alumno(models.Model):
    _name = "aden.alumno"
    _description = "aden.alumno"
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    legajo = fields.Integer(string='Legajo', required=True)
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Telefono')
    direccion = fields.Char(string='Direccion', required=True)
    pais = fields.Char(string='Pais', required=True)
    
    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('nombre', 'apellido')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.nombre} {record.apellido}"