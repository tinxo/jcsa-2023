import pandas as pd

# Lectura de los datos
df_creditos = pd.read_parquet("../data/datos_creditos.parquet")
df_tarjetas = pd.read_parquet("../data/datos_tarjetas.parquet")

# Integración de los datos
df_integrado = pd.merge(df_creditos, df_tarjetas, on='id_cliente', how='inner')

# Transformaciones sobre los datos
cambios_estado_civil = {
    'CASADO' : 'C',
    'SOLTERO' : 'S',
    'DESCONOCIDO' : 'N',
    'DIVORCIADO' : 'D',
}
estado_civil_N = df_integrado.loc[:, ('estado_civil')].map(cambios_estado_civil).rename('estado_civil')

etiquetas_a_e = ['menor_5', '5_a_10', 'mayor_10']
rangos_a_e = [0, 4, 10, 50]
valor_para_nan = 'NA'
antiguedad_empleados_N = pd.cut(df_integrado['antiguedad_empleado'], 
                                bins=rangos_a_e, 
                                labels=etiquetas_a_e,
                                right=False).cat.add_categories(valor_para_nan).fillna(valor_para_nan)

etiquetas_i = ['hasta_20k', '20k_a_50k', '50k_a_100k', 'mayor_100k']
rangos_i = [0, 19999, 49999, 99999, 999999]
ingresos_N = pd.cut(df_integrado['ingresos'], 
                                bins=rangos_i, 
                                labels=etiquetas_i)

etiquetas_l_tc = ['menor_3k', '3k_a_5k', '5k_a_10k', 'mayor_10k']
rangos_l_tc = [0, 2999, 4999, 9999, 100000]
limite_credito_tc_N = pd.cut(df_integrado['limite_credito_tc'], 
                                bins=rangos_l_tc, 
                                labels=etiquetas_l_tc)

etiquetas_g_u12 = ['menor_1k', '2k_a_4k', '4k_a_6k', '6k_a_8k', '8k_a_10k', 'mayor_10k']
rangos_g_u12 = [0, 999, 3999, 5999, 7999, 9999, 100000]
gastos_ult_12m_N = pd.cut(df_integrado['gastos_ult_12m'], 
                                bins=rangos_g_u12, 
                                labels=etiquetas_g_u12)

# Eliminación de columnas modificadas
col_eliminar_final = [
              'antiguedad_empleado',
              'ingresos',
              'gastos_ult_12m', 
              'limite_credito_tc', 
              'estado_civil',
              'id_cliente']

df_integrado.drop(col_eliminar_final, inplace=True, axis=1)

# Integración de los datos modificados 
df_final = pd.concat([gastos_ult_12m_N, 
                        limite_credito_tc_N, 
                        ingresos_N, 
                        antiguedad_empleados_N, 
                        estado_civil_N,
                        df_integrado], axis=1)

# Filtro de datos
df_final = df_final[df_final['gastos_ult_12m'] != 'mayor_10k']

# Exportación de resultados
df_final.to_parquet("../data/datos_integrados.parquet")