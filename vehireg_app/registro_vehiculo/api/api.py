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
def news_preview():
	data = frappe.db.sql(""" SELECT tn.name, tn.titulo, tn.resumen, tn.categoria, tn.referencia, tn.autor, tn.imagen, tn.modified 	
FROM tabNews tn
WHERE tn.publicado =1 """, as_dict=1)
	return {"status": "success", "data": data}

@frappe.whitelist(allow_guest=True)
def publicidad():
	data = frappe.db.sql(""" SELECT tp.empresa, tp.publicidad_full ,tp.publicidad_horizontal,tp.publicidad_vertical ,tp.publicidad_opcional ,tp.url, tp.whatsapp
FROM tabPublicidad tp """, as_dict=1)
	return {"status": "success", "data": data}

@frappe.whitelist(allow_guest=True)
def publicidadLigas(liga):
	values = {'name': liga}
	data = frappe.db.sql(""" SELECT tl.name, tl.nombre, tl.empresa, tl.url, tl.whatsapp, tl.publicidad_horizontal,tl.publicidad_horizontal1 
FROM tabLiga tl 
WHERE tl.name= %(name)s """, values=values,as_dict=1)
	return {"status": "success", "data": data}
