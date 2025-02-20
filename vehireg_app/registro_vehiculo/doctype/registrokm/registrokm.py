# Copyright (c) 2025, Alvaro and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class RegistroKM(Document):
	def before_insert(self):
        # Establecer fecha y hora de salida al momento de crear el registro
		self.fecha_salida = datetime.now().date()
		self.hora_salida = datetime.now().time()
        


	def on_update(self):
        # Al actualizar, si se está registrando la entrada
		values = {'name': self.name, 'fecha_ingreso':datetime.now().date(),'hora_ingreso':datetime.now().time()}
		#data = frappe.db.sql(""" SELECT count(name) FROM `tabSanciones` s	WHERE s.ci = %(ci)s and docstatus = 0""", values=values, as_dict=0)
		frappe.db.sql(""" UPDATE `tabRegistroKM` tc SET tc.fecha_ingreso =%(fecha_ingreso)s, tc.hora_ingreso =%(hora_ingreso)s WHERE tc.name = %(name)s """, values=values, as_dict=0)
		self.fecha_ingreso = datetime.now().date()
		self.hora_ingreso = datetime.now().time()

	
	