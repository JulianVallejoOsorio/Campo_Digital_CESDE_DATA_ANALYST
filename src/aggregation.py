import pandas as pd

def total_sales_per_user(df_sales, df_users):
    df_total = (
        df_sales.groupby("id_cliente")["total"]
        .sum()
        .reset_index()
        .merge(df_users[["id_cliente", "nombre_completo"]], on="id_cliente", how="left")
        .sort_values(by="total", ascending=False)
    )

    print("Total de ventas por usuario:")
    print(df_total.head(10))
    return df_total

def total_products_by_address(df_sales, df_salesdetails, df_address):
    df_merged = (
        df_sales.merge(df_salesdetails, left_on="id", right_on="id_venta", how="left")
        .merge(df_address, left_on="direccion_id", right_on="id_direccion", how="left")
    )

    df_total = (
        df_merged.groupby(["direccion_id", "descripcion"])["cantidad"]
        .sum()
        .reset_index()
        .sort_values(by="cantidad", ascending=False)
    )

    print("Total de productos vendidos por dirección: ")
    print(df_total.head(10))
    return df_total
