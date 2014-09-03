#encoding:utf-8

from django.db import models

# Create your models here.

class RegEnt(models.Model):
    usuario = models.TextField(blank=True) # This field type is a guess.
    fecha_registro = models.TextField(blank=True) # This field type is a guess.
    hora_registro = models.TextField(blank=True) # This field type is a guess.
    tipo_registro = models.TextField(blank=True) # This field type is a guess.
    ip = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'registro'

class Entrevistado(models.Model):
	"""Datos del Entrevistado"""
	folio = models.CharField(max_length=150)
	monitor_clinico = models.CharField(max_length=150)
	supervisor = models.CharField(max_length=150)
	fecha_llenado = models.CharField(max_length=150)
	nombre_medico = models.CharField(max_length=150)
	especialidad = models.CharField(max_length=150)
	pais = models.CharField(max_length=150)
	institucion_publica = models.CharField(max_length=150)
	institucion_privada = models.CharField(max_length=150)
	telefono = models.CharField(max_length=150)
	email = models.CharField(max_length=150)
	class Meta:
		db_table = 'entrevistado'
		
class Seleccion(models.Model):
	"""Datos del Seleccion"""
	folio = models.CharField(max_length=150)
	espe_medica = models.CharField(max_length=150)
	tiempo_endo = models.CharField(max_length=150)
	cushing_actual_tx = models.CharField(max_length=150)
	cushing_cm_12m = models.CharField(max_length=150)
	examen_orina_2 = models.CharField(max_length=150)
	examen_orina_1 = models.CharField(max_length=150)
	examen_orina_0 = models.CharField(max_length=150)
	class Meta:
		db_table = 'seleccion'

class Control(models.Model):
	"""Datos del Control"""
	folio = models.CharField(max_length=150)
	control_alto = models.CharField(max_length=150)
	control_bajo = models.CharField(max_length=150)
	control_medio = models.CharField(max_length=150)
	corti_libre_orina = models.CharField(max_length=150)
	hormona_adreno = models.CharField(max_length=150)
	sintomas_paciente = models.CharField(max_length=150)
	class Meta:
		db_table = 'control'

class Generales(models.Model):
	"""Datos del Generales"""
	folio = models.CharField(max_length=150)
	edad = models.CharField(max_length=150)
	sexo = models.CharField(max_length=150)
	peso = models.CharField(max_length=150)
	talla = models.CharField(max_length=150)
	imc = models.CharField(max_length=150)
	fecha_diag = models.DateField(auto_now=False)
	class Meta:
		db_table = 'generales'

# Por generar en el excel


class Sintomas(models.Model):
	"""Datos del Sintomas"""
	folio = models.CharField(max_length=150)
	cara_luna_6 = models.CharField(max_length=150)
	cara_luna_12 = models.CharField(max_length=150)
	ojos_jinchados_6 = models.CharField(max_length=150)
	ojos_jinchados_12 = models.CharField(max_length=150)
	tez_purpuras_6 = models.CharField(max_length=150)
	tez_purpuras_12 = models.CharField(max_length=150)
	acne_6 = models.CharField(max_length=150)
	acne_12 = models.CharField(max_length=150)
	estrias_6 = models.CharField(max_length=150)
	estrias_12 = models.CharField(max_length=150)
	moretones_6 = models.CharField(max_length=150)
	moretones_12 = models.CharField(max_length=150)
	aumento_abdomen_6 = models.CharField(max_length=150)
	aumento_abdomen_12 = models.CharField(max_length=150)
	joroba_6 = models.CharField(max_length=150)
	joroba_12 = models.CharField(max_length=150)
	temperatura_baja_6 = models.CharField(max_length=150)
	temperatura_baja_12 = models.CharField(max_length=150)
	sensibilidad_frio_6 = models.CharField(max_length=150)
	sensibilidad_frio_12 = models.CharField(max_length=150)
	fatiga_6 = models.CharField(max_length=150)
	fatiga_12 = models.CharField(max_length=150)
	osteopenia_6 = models.CharField(max_length=150)
	osteopenia_12 = models.CharField(max_length=150)
	osteoporosis_6 = models.CharField(max_length=150)
	osteoporosis_12 = models.CharField(max_length=150)
	ablan_col_vertebral_6 = models.CharField(max_length=150)
	ablan_col_vertebral_12 = models.CharField(max_length=150)
	dolores_espalda_6 = models.CharField(max_length=150)
	dolores_espalda_12 = models.CharField(max_length=150)
	fracturas_6 = models.CharField(max_length=150)
	fracturas_12 = models.CharField(max_length=150)
	debilidad_muscular_6 = models.CharField(max_length=150)
	debilidad_muscular_12 = models.CharField(max_length=150)
	debilidad_extrem_6 = models.CharField(max_length=150)
	debilidad_extrem_12 = models.CharField(max_length=150)
	hirsutismo_6 = models.CharField(max_length=150)
	hirsutismo_12 = models.CharField(max_length=150)
	ciclo_mesn_6 = models.CharField(max_length=150)
	ciclo_mesn_12 = models.CharField(max_length=150)
	infertilidad_6 = models.CharField(max_length=150)
	infertilidad_12 = models.CharField(max_length=150)
	disminucion_sexual_6 = models.CharField(max_length=150)
	disminucion_sexual_12 = models.CharField(max_length=150)
	impotencia_6 = models.CharField(max_length=150)
	impotencia_12 = models.CharField(max_length=150)
	deficit_cognitivos_6 = models.CharField(max_length=150)
	deficit_cognitivos_12 = models.CharField(max_length=150)
	otro1_cual = models.CharField(max_length=150)
	otro1_6 = models.CharField(max_length=150)
	otro1_12 = models.CharField(max_length=150)
	otro2_cual = models.CharField(max_length=150)
	otro2_6 = models.CharField(max_length=150)
	otro2_12 = models.CharField(max_length=150)

	class Meta:
		db_table = 'sintomas'

class Comorbilidades(models.Model):
	"""Datos del Generales"""
	folio = models.CharField(max_length=150)
	dm1_6 = models.CharField(max_length=150)
	dm1_12 = models.CharField(max_length=150)
	dm2_6 = models.CharField(max_length=150)
	dm2_12 = models.CharField(max_length=150)
	sind_met_6 = models.CharField(max_length=150)
	sind_met_12 = models.CharField(max_length=150)
	int_glucosa_6 = models.CharField(max_length=150)
	int_glucosa_12 = models.CharField(max_length=150)
	obeisdad_6 = models.CharField(max_length=150)
	obeisdad_12 = models.CharField(max_length=150)
	hipertension_6 = models.CharField(max_length=150)
	hipertension_12 = models.CharField(max_length=150)
	colesterol_6 = models.CharField(max_length=150)
	colesterol_12 = models.CharField(max_length=150)
	trombosis_6 = models.CharField(max_length=150)
	trombosis_12 = models.CharField(max_length=150)
	infarto_miocardio_6 = models.CharField(max_length=150)
	infarto_miocardio_12 = models.CharField(max_length=150)
	angina_pecho_6 = models.CharField(max_length=150)
	angina_pecho_12 = models.CharField(max_length=150)
	cardiopatia_6 = models.CharField(max_length=150)
	cardiopatia_12 = models.CharField(max_length=150)
	cerebrovascular_6 = models.CharField(max_length=150)
	cerebrovascular_12 = models.CharField(max_length=150)
	isquemia_6 = models.CharField(max_length=150)
	isquemia_12 = models.CharField(max_length=150)
	sepsis_6 = models.CharField(max_length=150)
	sepsis_12 = models.CharField(max_length=150)
	neumonia_6 = models.CharField(max_length=150)
	neumonia_12 = models.CharField(max_length=150)
	vias_urinarias_6 = models.CharField(max_length=150)
	vias_urinarias_12 = models.CharField(max_length=150)
	pytb_6 = models.CharField(max_length=150)
	pytb_12 = models.CharField(max_length=150)
	fungicas_6 = models.CharField(max_length=150)
	fungicas_12 = models.CharField(max_length=150)
	depresion_6 = models.CharField(max_length=150)
	depresion_12 = models.CharField(max_length=150)
	ansiedad_6 = models.CharField(max_length=150)
	ansiedad_12 = models.CharField(max_length=150)
	psicosis_6 = models.CharField(max_length=150)
	psicosis_12 = models.CharField(max_length=150)
	cr_6 = models.CharField(max_length=150)
	cr_12 = models.CharField(max_length=150)
	otro1_cual = models.CharField(max_length=150)
	otro1_6 = models.CharField(max_length=150)
	otro1_12 = models.CharField(max_length=150)
	otro2_cual = models.CharField(max_length=150)
	otro2_6 = models.CharField(max_length=150)
	otro2_12 = models.CharField(max_length=150)

	class Meta:
		db_table = 'comorbilidades'

class Especialista(models.Model):
	"""Datos del Especialista"""
	folio = models.CharField(max_length=150)
	endo_1_mes = models.CharField(max_length=150)
	endo_2_mes = models.CharField(max_length=150)
	endo_3_mes = models.CharField(max_length=150)
	endo_4_mes = models.CharField(max_length=150)
	endo_5_mes = models.CharField(max_length=150)
	endo_6_mes = models.CharField(max_length=150)
	endo_7_mes = models.CharField(max_length=150)
	endo_8_mes = models.CharField(max_length=150)
	endo_9_mes = models.CharField(max_length=150)
	endo_10_mes = models.CharField(max_length=150)
	endo_11_mes = models.CharField(max_length=150)
	endo_12_mes = models.CharField(max_length=150)
	inter_1_mes = models.CharField(max_length=150)
	inter_2_mes = models.CharField(max_length=150)
	inter_3_mes = models.CharField(max_length=150)
	inter_4_mes = models.CharField(max_length=150)
	inter_5_mes = models.CharField(max_length=150)
	inter_6_mes = models.CharField(max_length=150)
	inter_7_mes = models.CharField(max_length=150)
	inter_8_mes = models.CharField(max_length=150)
	inter_9_mes = models.CharField(max_length=150)
	inter_10_mes = models.CharField(max_length=150)
	inter_11_mes = models.CharField(max_length=150)
	inter_12_mes = models.CharField(max_length=150)
	cx_1_mes = models.CharField(max_length=150)
	cx_2_mes = models.CharField(max_length=150)
	cx_3_mes = models.CharField(max_length=150)
	cx_4_mes = models.CharField(max_length=150)
	cx_5_mes = models.CharField(max_length=150)
	cx_6_mes = models.CharField(max_length=150)
	cx_7_mes = models.CharField(max_length=150)
	cx_8_mes = models.CharField(max_length=150)
	cx_9_mes = models.CharField(max_length=150)
	cx_10_mes = models.CharField(max_length=150)
	cx_11_mes = models.CharField(max_length=150)
	cx_12_mes = models.CharField(max_length=150)
	urg_1_mes = models.CharField(max_length=150)
	urg_2_mes = models.CharField(max_length=150)
	urg_3_mes = models.CharField(max_length=150)
	urg_4_mes = models.CharField(max_length=150)
	urg_5_mes = models.CharField(max_length=150)
	urg_6_mes = models.CharField(max_length=150)
	urg_7_mes = models.CharField(max_length=150)
	urg_8_mes = models.CharField(max_length=150)
	urg_9_mes = models.CharField(max_length=150)
	urg_10_mes = models.CharField(max_length=150)
	urg_11_mes = models.CharField(max_length=150)
	urg_12_mes = models.CharField(max_length=150)
	otro1_cual = models.CharField(max_length=150)
	otro1_1_mes = models.CharField(max_length=150)
	otro1_2_mes = models.CharField(max_length=150)
	otro1_3_mes = models.CharField(max_length=150)
	otro1_4_mes = models.CharField(max_length=150)
	otro1_5_mes = models.CharField(max_length=150)
	otro1_6_mes = models.CharField(max_length=150)
	otro1_7_mes = models.CharField(max_length=150)
	otro1_8_mes = models.CharField(max_length=150)
	otro1_9_mes = models.CharField(max_length=150)
	otro1_10_mes = models.CharField(max_length=150)
	otro1_11_mes = models.CharField(max_length=150)
	otro1_12_mes = models.CharField(max_length=150)
	otro2_cual = models.CharField(max_length=150)
	otro2_1_mes = models.CharField(max_length=150)
	otro2_2_mes = models.CharField(max_length=150)
	otro2_3_mes = models.CharField(max_length=150)
	otro2_4_mes = models.CharField(max_length=150)
	otro2_5_mes = models.CharField(max_length=150)
	otro2_6_mes = models.CharField(max_length=150)
	otro2_7_mes = models.CharField(max_length=150)
	otro2_8_mes = models.CharField(max_length=150)
	otro2_9_mes = models.CharField(max_length=150)
	otro2_10_mes = models.CharField(max_length=150)
	otro2_11_mes = models.CharField(max_length=150)
	otro2_12_mes = models.CharField(max_length=150)
	class Meta:
		db_table = 'especialista'

class Hospitalizacion(models.Model):
	"""Datos del Hospitalizacion"""
	folio = models.CharField(max_length=150)
	hosp_1_mes = models.CharField(max_length=150)
	hosp_2_mes = models.CharField(max_length=150)
	hosp_3_mes = models.CharField(max_length=150)
	hosp_4_mes = models.CharField(max_length=150)
	hosp_5_mes = models.CharField(max_length=150)
	hosp_6_mes = models.CharField(max_length=150)
	hosp_7_mes = models.CharField(max_length=150)
	hosp_8_mes = models.CharField(max_length=150)
	hosp_9_mes = models.CharField(max_length=150)
	hosp_10_mes = models.CharField(max_length=150)
	hosp_11_mes = models.CharField(max_length=150)
	hosp_12_mes = models.CharField(max_length=150)
	ci_1_mes = models.CharField(max_length=150)
	ci_2_mes = models.CharField(max_length=150)
	ci_3_mes = models.CharField(max_length=150)
	ci_4_mes = models.CharField(max_length=150)
	ci_5_mes = models.CharField(max_length=150)
	ci_6_mes = models.CharField(max_length=150)
	ci_7_mes = models.CharField(max_length=150)
	ci_8_mes = models.CharField(max_length=150)
	ci_9_mes = models.CharField(max_length=150)
	ci_10_mes = models.CharField(max_length=150)
	ci_11_mes = models.CharField(max_length=150)
	ci_12_mes = models.CharField(max_length=150)

	class Meta:
		db_table = 'hospitalizacion'

class Laboratorio(models.Model):
	"""Datos del Laboratorio"""
	folio = models.CharField(max_length=150)
	clo_no_1_mes = models.CharField(max_length=150)
	clo_valor_1_mes = models.CharField(max_length=150)
	clo_no_2_mes = models.CharField(max_length=150)
	clo_valor_2_mes = models.CharField(max_length=150)
	clo_no_3_mes = models.CharField(max_length=150)
	clo_valor_3_mes = models.CharField(max_length=150)
	clo_no_4_mes = models.CharField(max_length=150)
	clo_valor_4_mes = models.CharField(max_length=150)
	clo_no_5_mes = models.CharField(max_length=150)
	clo_valor_5_mes = models.CharField(max_length=150)
	clo_no_6_mes = models.CharField(max_length=150)
	clo_valor_6_mes = models.CharField(max_length=150)
	clo_no_7_mes = models.CharField(max_length=150)
	clo_valor_7_mes = models.CharField(max_length=150)
	clo_no_8_mes = models.CharField(max_length=150)
	clo_valor_8_mes = models.CharField(max_length=150)
	clo_no_9_mes = models.CharField(max_length=150)
	clo_valor_9_mes = models.CharField(max_length=150)
	clo_no_10_mes = models.CharField(max_length=150)
	clo_valor_10_mes = models.CharField(max_length=150)
	clo_no_11_mes = models.CharField(max_length=150)
	clo_valor_11_mes = models.CharField(max_length=150)
	clo_no_12_mes = models.CharField(max_length=150)
	clo_valor_12_mes = models.CharField(max_length=150)
	ha_no_1_mes = models.CharField(max_length=150)
	ha_valor_1_mes = models.CharField(max_length=150)
	ha_no_2_mes = models.CharField(max_length=150)
	ha_valor_2_mes = models.CharField(max_length=150)
	ha_no_3_mes = models.CharField(max_length=150)
	ha_valor_3_mes = models.CharField(max_length=150)
	ha_no_4_mes = models.CharField(max_length=150)
	ha_valor_4_mes = models.CharField(max_length=150)
	ha_no_5_mes = models.CharField(max_length=150)
	ha_valor_5_mes = models.CharField(max_length=150)
	ha_no_6_mes = models.CharField(max_length=150)
	ha_valor_6_mes = models.CharField(max_length=150)
	ha_no_7_mes = models.CharField(max_length=150)
	ha_valor_7_mes = models.CharField(max_length=150)
	ha_no_8_mes = models.CharField(max_length=150)
	ha_valor_8_mes = models.CharField(max_length=150)
	ha_no_9_mes = models.CharField(max_length=150)
	ha_valor_9_mes = models.CharField(max_length=150)
	ha_no_10_mes = models.CharField(max_length=150)
	ha_valor_10_mes = models.CharField(max_length=150)
	ha_no_11_mes = models.CharField(max_length=150)
	ha_valor_11_mes = models.CharField(max_length=150)
	ha_no_12_mes = models.CharField(max_length=150)
	ha_valor_12_mes = models.CharField(max_length=150)
	# Columnas no contabilizadas en el excel
	control_1_mes = models.CharField(max_length=150)
	control_2_mes = models.CharField(max_length=150)
	control_3_mes = models.CharField(max_length=150)
	control_4_mes = models.CharField(max_length=150)
	control_5_mes = models.CharField(max_length=150)
	control_6_mes = models.CharField(max_length=150)
	control_7_mes = models.CharField(max_length=150)
	control_8_mes = models.CharField(max_length=150)
	control_9_mes = models.CharField(max_length=150)
	control_10_mes = models.CharField(max_length=150)
	control_11_mes = models.CharField(max_length=150)
	control_12_mes = models.CharField(max_length=150)
	# Terminan las columnas no coontabilizadas en excel
	psd_si_6 = models.CharField(max_length=150)
	psd_pruebas_6 = models.CharField(max_length=150)
	psd_si_12 = models.CharField(max_length=150)
	psd_pruebas_12 = models.CharField(max_length=150)
	acth_si_6 = models.CharField(max_length=150)
	acth_pruebas_6 = models.CharField(max_length=150)
	acth_si_12 = models.CharField(max_length=150)
	acth_pruebas_12 = models.CharField(max_length=150)
	metirapona_si_6 = models.CharField(max_length=150)
	metirapona_pruebas_6 = models.CharField(max_length=150)
	metirapona_si_12 = models.CharField(max_length=150)
	metirapona_pruebas_12 = models.CharField(max_length=150)
	crh_si_6 = models.CharField(max_length=150)
	crh_pruebas_6 = models.CharField(max_length=150)
	crh_si_12 = models.CharField(max_length=150)
	crh_pruebas_12 = models.CharField(max_length=150)
	seno_petroso_si_6 = models.CharField(max_length=150)
	seno_petroso_pruebas_6 = models.CharField(max_length=150)
	seno_petroso_si_12 = models.CharField(max_length=150)
	seno_petroso_pruebas_12 = models.CharField(max_length=150)
	tomografia_si_6 = models.CharField(max_length=150)
	tomografia_pruebas_6 = models.CharField(max_length=150)
	tomografia_si_12 = models.CharField(max_length=150)
	tomografia_pruebas_12 = models.CharField(max_length=150)
	res_magnetica_si_6 = models.CharField(max_length=150)
	res_magnetica_pruebas_6 = models.CharField(max_length=150)
	res_magnetica_si_12 = models.CharField(max_length=150)
	res_magnetica_pruebas_12 = models.CharField(max_length=150)
	otro1_cual = models.CharField(max_length=150)
	otro1_si_6 = models.CharField(max_length=150)
	otro1_pruebas_6 = models.CharField(max_length=150)
	otro1_si_12 = models.CharField(max_length=150)
	otro1_pruebas_12 = models.CharField(max_length=150)
	otro2_cual = models.CharField(max_length=150)
	otro2_si_6 = models.CharField(max_length=150)
	otro2_pruebas_6 = models.CharField(max_length=150)
	otro2_si_12 = models.CharField(max_length=150)
	otro2_pruebas_12 = models.CharField(max_length=150)

	class Meta:
		db_table = 'laboratorio'

class Intervenciones(models.Model):
	"""Datos del Intervenciones"""
	folio = models.CharField(max_length=150)
	rx_si_6 = models.CharField(max_length=150)
	rx_hipo_comp_6 = models.CharField(max_length=150)
	rx_hipo_veces_6 = models.CharField(max_length=150)
	rx_cerebro_comp_6 = models.CharField(max_length=150)
	rx_cerebro_veces_6 = models.CharField(max_length=150)
	rx_otras_comp_6 = models.CharField(max_length=150)
	rx_otras_veces_6 = models.CharField(max_length=150)
	radiocirugia_si_6 = models.CharField(max_length=150)
	radiocirugia_hipo_comp_6 = models.CharField(max_length=150)
	radiocirugia_hipo_veces_6 = models.CharField(max_length=150)
	radiocirugia_visual_comp_6 = models.CharField(max_length=150)
	radiocirugia_visual_veces_6 = models.CharField(max_length=150)
	radiocirugia_craneal_comp_6 = models.CharField(max_length=150)
	radiocirugia_craneal_veces_6 = models.CharField(max_length=150)
	radiocirugia_otras_comp_6 = models.CharField(max_length=150)
	radiocirugia_otras_veces_6 = models.CharField(max_length=150)
	cirugia_si_6 = models.CharField(max_length=150)
	cirugia_hormo_comp_6 = models.CharField(max_length=150)
	cirugia_hormo_veces_6 = models.CharField(max_length=150)
	cirugia_diabetes_comp_6 = models.CharField(max_length=150)
	cirugia_diabetes_veces_6 = models.CharField(max_length=150)
	cirugia_cerebro_comp_6 = models.CharField(max_length=150)
	cirugia_cerebro_veces_6 = models.CharField(max_length=150)
	cirugia_visual_comp_6 = models.CharField(max_length=150)
	cirugia_visual_veces_6 = models.CharField(max_length=150)
	cirugia_menin_comp_6 = models.CharField(max_length=150)
	cirugia_menin_veces_6 = models.CharField(max_length=150)
	cirugia_cefalo_comp_6 = models.CharField(max_length=150)
	cirugia_cefalo_veces_6 = models.CharField(max_length=150)
	cirugia_otras_comp_6 = models.CharField(max_length=150)
	cirugia_otras_veces_6 = models.CharField(max_length=150)
	adrena_si_6 = models.CharField(max_length=150)
	adrena_nelson_comp_6 = models.CharField(max_length=150)
	adrena_nelson_veces_6 = models.CharField(max_length=150)
	adrena_otras_comp_6 = models.CharField(max_length=150)
	adrena_otras_veces_6 = models.CharField(max_length=150)
	rx_si_12 = models.CharField(max_length=150)
	rx_hipo_comp_12 = models.CharField(max_length=150)
	rx_hipo_veces_12 = models.CharField(max_length=150)
	rx_cerebro_comp_12 = models.CharField(max_length=150)
	rx_cerebro_veces_12 = models.CharField(max_length=150)
	rx_otras_comp_12 = models.CharField(max_length=150)
	rx_otras_veces_12 = models.CharField(max_length=150)
	radiocirugia_si_12 = models.CharField(max_length=150)
	radiocirugia_hipo_comp_12 = models.CharField(max_length=150)
	radiocirugia_hipo_veces_12 = models.CharField(max_length=150)
	radiocirugia_visual_comp_12 = models.CharField(max_length=150)
	radiocirugia_visual_veces_12 = models.CharField(max_length=150)
	radiocirugia_craneal_comp_12 = models.CharField(max_length=150)
	radiocirugia_craneal_veces_12 = models.CharField(max_length=150)
	radiocirugia_otras_comp_12 = models.CharField(max_length=150)
	radiocirugia_otras_veces_12 = models.CharField(max_length=150)
	cirugia_si_12 = models.CharField(max_length=150)
	cirugia_hormo_comp_12 = models.CharField(max_length=150)
	cirugia_hormo_veces_12 = models.CharField(max_length=150)
	cirugia_diabetes_comp_12 = models.CharField(max_length=150)
	cirugia_diabetes_veces_12 = models.CharField(max_length=150)
	cirugia_cerebro_comp_12 = models.CharField(max_length=150)
	cirugia_cerebro_veces_12 = models.CharField(max_length=150)
	cirugia_visual_comp_12 = models.CharField(max_length=150)
	cirugia_visual_veces_12 = models.CharField(max_length=150)
	cirugia_menin_comp_12 = models.CharField(max_length=150)
	cirugia_menin_veces_12 = models.CharField(max_length=150)
	cirugia_cefalo_comp_12 = models.CharField(max_length=150)
	cirugia_cefalo_veces_12 = models.CharField(max_length=150)
	cirugia_otras_comp_12 = models.CharField(max_length=150)
	cirugia_otras_veces_12 = models.CharField(max_length=150)
	adrena_si_12 = models.CharField(max_length=150)
	adrena_nelson_comp_12 = models.CharField(max_length=150)
	adrena_nelson_veces_12 = models.CharField(max_length=150)
	adrena_otras_comp_12 = models.CharField(max_length=150)
	adrena_otras_veces_12 = models.CharField(max_length=150)

	class Meta:
		db_table = 'inteervenciones'

class Tratamiento(models.Model):
	"""Datos del Tratamiento"""
	folio = models.CharField(max_length=150)
	keto_6 = models.CharField(max_length=150)
	keto_12 = models.CharField(max_length=150)
	caber_6 = models.CharField(max_length=150)
	caber_12 = models.CharField(max_length=150)
	mife_6 = models.CharField(max_length=150)
	mife_12 = models.CharField(max_length=150)
	otro1_cual = models.CharField(max_length=150)
	otro1_6 = models.CharField(max_length=150)
	otro1_12 = models.CharField(max_length=150)
	otro2_cual = models.CharField(max_length=150)
	otro2_6 = models.CharField(max_length=150)
	otro2_12 = models.CharField(max_length=150)
	otro3_cual = models.CharField(max_length=150)
	otro3_6 = models.CharField(max_length=150)
	otro3_12 = models.CharField(max_length=150)
	metfo_6 = models.CharField(max_length=150)
	metfo_12 = models.CharField(max_length=150)
	sulfo_6 = models.CharField(max_length=150)
	sulfo_12 = models.CharField(max_length=150)
	tiazo_6 = models.CharField(max_length=150)
	tiazo_12 = models.CharField(max_length=150)
	dpp4_6 = models.CharField(max_length=150)
	dpp4_12 = models.CharField(max_length=150)
	glp1_6 = models.CharField(max_length=150)
	glp1_12 = models.CharField(max_length=150)
	insu_rapida_6 = models.CharField(max_length=150)
	insu_rapida_12 = models.CharField(max_length=150)
	insu_lenta_6 = models.CharField(max_length=150)
	insu_lenta_12 = models.CharField(max_length=150)
	ieca_6 = models.CharField(max_length=150)
	ieca_12 = models.CharField(max_length=150)
	bra_6 = models.CharField(max_length=150)
	bra_12 = models.CharField(max_length=150)
	beta_bloq_6 = models.CharField(max_length=150)
	beta_bloq_12 = models.CharField(max_length=150)
	fibratos_6 = models.CharField(max_length=150)
	fibratos_12 = models.CharField(max_length=150)
	bcc_6 = models.CharField(max_length=150)
	bcc_12 = models.CharField(max_length=150)
	diuretico_6 = models.CharField(max_length=150)
	diuretico_12 = models.CharField(max_length=150)
	iac_6 = models.CharField(max_length=150)
	iac_12 = models.CharField(max_length=150)
	vit_b3_6 = models.CharField(max_length=150)
	vit_b3_12 = models.CharField(max_length=150)
	nitrato_6 = models.CharField(max_length=150)
	nitrato_12 = models.CharField(max_length=150)
	antiplaq_6 = models.CharField(max_length=150)
	antiplaq_12 = models.CharField(max_length=150)
	acido_acetil_6 = models.CharField(max_length=150)
	acido_acetil_12 = models.CharField(max_length=150)
	estatina_6 = models.CharField(max_length=150)
	estatina_12 = models.CharField(max_length=150)
	sab_6 = models.CharField(max_length=150)
	sab_12 = models.CharField(max_length=150)
	sepsis_cual = models.CharField(max_length=150)
	sepsis_6 = models.CharField(max_length=150)
	sepsis_12 = models.CharField(max_length=150)
	neumonia_cual = models.CharField(max_length=150)
	neumonia_6 = models.CharField(max_length=150)
	neumonia_12 = models.CharField(max_length=150)
	vias_cual = models.CharField(max_length=150)
	vias_6 = models.CharField(max_length=150)
	vias_12 = models.CharField(max_length=150)
	ptb_cual = models.CharField(max_length=150)
	ptb_6 = models.CharField(max_length=150)
	ptv_12 = models.CharField(max_length=150)
	fungi_cual = models.CharField(max_length=150)
	fungi_6 = models.CharField(max_length=150)
	fungi_12 = models.CharField(max_length=150)

	class Meta:
		db_table = 'tratamiento'

class ComorbilidadesTx(models.Model):
	"""Datos del Comorbilidades"""
	folio = models.CharField(max_length=150)
	depre_cual = models.CharField(max_length=150)
	depre_6 = models.CharField(max_length=150)
	depre_12 = models.CharField(max_length=150)
	ansi_cual = models.CharField(max_length=150)
	ansi_6 = models.CharField(max_length=150)
	ansi_12 = models.CharField(max_length=150)
	psico_cual = models.CharField(max_length=150)
	psico_6 = models.CharField(max_length=150)
	psico_12 = models.CharField(max_length=150)
	cr_cual = models.CharField(max_length=150)
	cr_6 = models.CharField(max_length=150)
	cr_12 = models.CharField(max_length=150)
	otra1_cual = models.CharField(max_length=150)
	otra1_6 = models.CharField(max_length=150)
	otra1_12 = models.CharField(max_length=150)
	otra2_cual = models.CharField(max_length=150)
	otra2_6 = models.CharField(max_length=150)
	otra2_12 = models.CharField(max_length=150)

	class Meta:
		db_table = 'comorbilidades_tx'

class Complicaciones(models.Model):
	"""Datos del Complicaciones"""
	folio = models.CharField(max_length=150)
	cual_1 = models.CharField(max_length=150)
	hosp_si_1 = models.CharField(max_length=150)
	hosp_eventos_1 = models.CharField(max_length=150)
	hosp_duracion_1 = models.CharField(max_length=150)
	espe_si_1 = models.CharField(max_length=150)
	espe_eventos_1 = models.CharField(max_length=150)
	espe_duracion_1 = models.CharField(max_length=150)
	otras_visitas_cual_1 = models.CharField(max_length=150)
	otras_visitas_si_1 = models.CharField(max_length=150)
	otras_visitas_eventos_1 = models.CharField(max_length=150)
	otras_visitas_duracion_1 = models.CharField(max_length=150)
	proc_1 = models.CharField(max_length=150)
	proc_si_1 = models.CharField(max_length=150)
	proc_eventos_1 = models.CharField(max_length=150)
	proc_duracion_1 = models.CharField(max_length=150)
	tx_1 = models.CharField(max_length=150)
	tx_posologia_1 = models.CharField(max_length=150)
	tx_si_1 = models.CharField(max_length=150)
	tx_eventos_1 = models.CharField(max_length=150)
	tx_duracion_1 = models.CharField(max_length=150)
	cual_2 = models.CharField(max_length=150)
	hosp_si_2 = models.CharField(max_length=150)
	hosp_eventos_2 = models.CharField(max_length=150)
	hosp_duracion_2 = models.CharField(max_length=150)
	espe_si_2 = models.CharField(max_length=150)
	espe_eventos_2 = models.CharField(max_length=150)
	espe_duracion_2 = models.CharField(max_length=150)
	otras_visitas_cual_2 = models.CharField(max_length=150)
	otras_visitas_si_2 = models.CharField(max_length=150)
	otras_visitas_eventos_2 = models.CharField(max_length=150)
	otras_visitas_duracion_2 = models.CharField(max_length=150)
	proc_2 = models.CharField(max_length=150)
	proc_si_2 = models.CharField(max_length=150)
	proc_eventos_2 = models.CharField(max_length=150)
	proc_duracion_2 = models.CharField(max_length=150)
	tx_2 = models.CharField(max_length=150)
	tx_posologia_2 = models.CharField(max_length=150)
	tx_si_2 = models.CharField(max_length=150)
	tx_eventos_2 = models.CharField(max_length=150)
	tx_duracion_2 = models.CharField(max_length=150)

	class Meta:
		db_table = 'complicaciones'

class TxCompleto(models.Model):
	"""docstring for Tx"""
	folio = models.CharField(max_length=150)
	tratamiento = models.CharField(max_length=150)
	meses = models.CharField(max_length=150)
	dosis = models.CharField(max_length=150)
	ciclo = models.CharField(max_length=150)
	intervalos = models.CharField(max_length=150)
	ciclos = models.CharField(max_length=150)
	cateterismo = models.BooleanField()
	class Meta:
		db_table = 'tx_completo'
		