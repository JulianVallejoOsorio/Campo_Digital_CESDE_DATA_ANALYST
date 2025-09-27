import pandas as pd

def users_with_more_than_five_purchases(df_sales, df_users):
    df_count = (
        df_sales.groupby("id_cliente")["id"]
        .count()
        .reset_index(name="compras")
        .merge(df_users[["id_cliente", "nombre_completo"]], on="id_cliente", how="left")
    )

    df_filtered = df_count[df_count["compras"] > 5]

    print("Usuarios con más de 5 compras: ")
    print(df_filtered)
    return df_filtered


def sales_to_bogota(df_sales, df_address):
    df_merged = df_sales.merge(df_address, left_on="direccion_id", right_on="id_direccion", how="left")

    df_bogota = df_merged[df_merged["codigo_ciudad"] == 40]

    print("Ventas enviadas a Bogotá: ")
    print(df_bogota[["id", "id_cliente", "total", "codigo_ciudad"]].head(10))
    print(f"Total ventas a Bogotá: {len(df_bogota)}")
    return df_bogota
