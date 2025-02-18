import frappe
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
import json
import random
from datetime import date
from frappe.utils import get_site_name, cstr, encode

@frappe.whitelist(allow_guest=True)
def get_vehiculos(placa):
	values = {'placa': placa}
	data = frappe.db.sql(""" SELECT tv.placa,tv.marca,tv.modelo,tv.numero_vehiculo from tabVehiculo tv where tv.placa=%(placa)s""",values=values, as_dict=1)
	return {"status": "success", "data": data}

@frappe.whitelist(allow_guest=True)
def get_conductores():
	data = frappe.db.sql(""" SELECT tc.nombres,tc.apellidos,tc.tipo_licencia,tc.numero_cedula 	
FROM tabConductor tc """, as_dict=1)
	return {"status": "success", "data": data}

@frappe.whitelist(allow_guest=True)
def obtener_registro_salida(placa_vehiculo):
    # Buscar registros en tabRegistroKM donde la placa coincide
    # y hay una fecha de salida pero no hay fecha de ingreso
	values = {'placa': placa_vehiculo}
	registros = frappe.db.sql(""" SELECT tr.name,tr.fecha_salida,tr.kilometraje_salida 
	from tabRegistroKM tr 
	where tr.vehiculo=%(placa)s and
	tr.fecha_salida IS NOT NULL and
	tr.fecha_ingreso IS NULL """,values=values, as_dict=1)
	
    # Si hay registros que cumplen con la condición, devolver el último
	if registros:
		return registros[-1]  # Devuelve el último registro encontrado
	else:
		return None  # No se encontraron registros

@frappe.whitelist(allow_guest=True)
def insert_regvehiculo(placa_vehiculo,conductor,fecha_salida,hora_salida,km_salida):
    # Buscar registros en tabRegistroKM donde la placa coincide
    # y hay una fecha de salida pero no hay fecha de ingreso
	nuevo_registro = frappe.get_doc({
        "doctype": "RegistroKM",
        "vehiculo": placa_vehiculo,
        "conductor": conductor,
        "fecha_salida": fecha_salida,
        "hora_salida": hora_salida,
        "kilometraje_salida": km_salida
    })
	nuevo_registro.insert()
	return nuevo_registro.name


@frappe.whitelist(allow_guest=True)
def update_regvehiculo(name,fecha_ingreso,hora_ingreso,km_ingreso):
    # Buscar registros en tabRegistroKM donde la placa coincide
    # y hay una fecha de salida pero no hay fecha de ingreso
	values = {'name': name,"fecha_ingreso":fecha_ingreso, "hora_ingreso":hora_ingreso, "km_ingreso":km_ingreso}
	registros = frappe.db.sql(""" UPDATE tabRegistroKM tr
	set tr.fecha_ingreso=%(fecha_ingreso)s,
	tr.hora_ingreso=%(hora_ingreso)s,
	tr.kilometraje_ingreso=%(km_ingreso)s
	where  tr.name=%(name)s """,values=values, as_dict=1)
	
	return registros