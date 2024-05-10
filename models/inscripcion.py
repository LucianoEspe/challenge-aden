from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Inscripcion(models.Model):
    _name = "aden.inscripcion"
    _description = "aden.inscripcion"
    
    alumno_id = fields.Many2one('aden.alumno', string='Alumno', required=True)
    programa_id = fields.Many2many('aden.programa', string='Programa', required=True) 
    
    # Cambio a Many2many para permitir inscribir a un alumno en varios programas a la vez
    
    @api.model
    def create(self, vals):
        if self.alumno_inscripto(vals):
            raise ValidationError('Ya existe un registro para este alumno.')
        return super(Inscripcion, self).create(vals)
    
    # def inscripto(self, vals):
    #     if self.env['aden.inscripcion'].search([
    #         ('alumno_id', '=', vals.get('alumno_id')),
    #         ('programa_id', '=', vals.get('programa_id'))]):
    #             return True
    #     return False
    
    # no necesito mas este metodo porque ahora el campo programa_id es Many2many
    
    def alumno_inscripto(self, vals):
        if self.env['aden.inscripcion'].search([('alumno_id', '=', vals.get('alumno_id'))]):
            return True
        return False