from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Inscripcion(models.Model):
    _name = "aden.inscripcion"
    _description = "aden.inscripcion"
    
    alumno_id = fields.Many2one('aden.alumno', string='Alumno', required=True)
    programa_id = fields.Many2one('aden.programa', string='Programa', required=True)
    
    @api.model
    def create(self, vals):
        if self.inscripto(vals):
            raise ValidationError('Este alumno ya está inscrito en este programa.')
        return super(Inscripcion, self).create(vals)
    
    def inscripto(self, vals):
        if self.env['aden.inscripcion'].search([
            ('alumno_id', '=', vals.get('alumno_id')),
            ('programa_id', '=', vals.get('programa_id'))]):
                return True
        return False