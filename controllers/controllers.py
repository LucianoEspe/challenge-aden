# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Controlador(http.Controller):
    @http.route('/obtener_inscriptos/<int:programa_id>', auth='public', methods=['GET'])
    def obtener_inscriptos(self, programa_id):
        programa = request.env['aden.programa'].browse(programa_id)
        if not programa.exists():
            return request.make_json_response({'error': 'El programa no existe'})
        # SELECT alumno_id FROM aden_inscripcion WHERE programa_id = programa.id
        alumnos = request.env['aden.inscripcion'].search([('programa_id', '=', programa.id)]).mapped('alumno_id')
        lista_inscriptos = []
        for alumno in alumnos:
            info_alumno = {
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'legajo': alumno.legajo,
                'fecha_nacimiento': str(alumno.nacimiento),
                'email': alumno.email,
                'telefono': alumno.telefono,
                'pais': alumno.pais,
            }
            lista_inscriptos.append(info_alumno)
        if len(lista_inscriptos) == 0:
            return request.make_json_response({'error': 'No hay inscriptos en este programa'})
        return request.make_json_response(lista_inscriptos)