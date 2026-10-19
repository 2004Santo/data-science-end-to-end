import duckdb

# Recrea, en un warehouse nuevo, las tablas crudas que ya cargaste en la
# Sesion 1 (Semana 5, Sesion 1), para modelarlas hoy en capas.
con = duckdb.connect("almacen.duckdb")
con.execute("CREATE OR REPLACE TABLE raw_pedidos AS SELECT * FROM read_csv_auto('pedidos.csv')")
con.execute("CREATE OR REPLACE TABLE raw_clientes AS SELECT * FROM read_csv_auto('clientes.csv')")
con.close()
print("raw_pedidos y raw_clientes cargadas en almacen.duckdb")
