// Copyright (c) 2025, Alvaro and contributors
// For license information, please see license.txt

frappe.ui.form.on("RegistroKM", {
    onload: function(frm) {
        // Establecer fecha y hora de salida al cargar el formulario
        if (!frm.doc.fecha_salida) {
            frm.set_value('fecha_salida', frappe.datetime.get_today());
        }
        if (!frm.doc.hora_salida) {
            frm.set_value('hora_salida', frappe.datetime.now_time());
        }

        // Hacer que los campos de ingreso sean solo lectura al cargar
        console.log("carga kmsalida:",frm.doc.kilometraje_salida);

        if (frm.doc.kilometraje_salida) {
            frm.set_df_property('vehiculo', 'read_only', 1);
            frm.set_df_property('conductor', 'read_only', 1);
            frm.set_df_property('fecha_ingreso', 'read_only', 1);
            frm.set_df_property('hora_ingreso', 'read_only', 1);
            frm.set_df_property('kilometraje_ingreso', 'read_only', 0);
            frm.set_df_property('kilometraje_salida', 'read_only', 1);
        }

        if (frm.doc.kilometraje_ingreso && frm.doc.kilometraje_salida) {
            frm.set_df_property('fecha_ingreso', 'read_only', 1);
            frm.set_df_property('hora_ingreso', 'read_only', 1);
            frm.set_df_property('kilometraje_ingreso', 'read_only', 1);
            frm.set_df_property('kilometraje_salida', 'read_only', 1);
        }

        if (!frm.doc.kilometraje_ingreso && !frm.doc.kilometraje_salida) {
            frm.set_df_property('fecha_ingreso', 'read_only', 1);
            frm.set_df_property('hora_ingreso', 'read_only', 1);
            frm.set_df_property('fecha_ingreso', 'read_only', 1);
            frm.set_df_property('hora_ingreso', 'read_only', 1);
            frm.set_df_property('kilometraje_ingreso', 'read_only', 1);
            frm.set_df_property('kilometraje_salida', 'read_only', 0);
        }
    },
    kilomentraje_salida: function(frm) {
        // Al ingresar el kilometraje de salida, hacer que los campos de ingreso sean solo lectura
        if (frm.doc.kilometraje_salida) {
            console.log("aldfksdlfkj");
            frm.set_df_property('fecha_ingreso', 'read_only', 1);
            frm.set_df_property('hora_ingreso', 'read_only', 1);
            frm.set_df_property('kilometraje_salida', 'read_only', 1);
            frm.set_df_property('vehiculo', 'read_only', 1);
            frm.set_df_property('conductor', 'read_only', 1);
        }
    },
    kilomentraje_ingreso: function(frm) {
        // Al ingresar el kilometraje de ingreso, establecer fecha y hora de ingreso
        if (frm.doc.kilometraje_ingreso) {
            frm.set_value('fecha_ingreso', frappe.datetime.get_today());
            frm.set_value('hora_ingreso', frappe.datetime.now_time());

            // Hacer que los campos de salida sean solo lectura
            //frm.set_df_property('kilometraje_salida', 'read_only', 1);
            frm.set_df_property('fecha_salida', 'read_only', 1);
            frm.set_df_property('hora_salida', 'read_only', 1);
        }
    }


});
