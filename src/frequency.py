import pandas as pd

def bestselligproduct(df_salesdetails, df_products):
    try:

        df_merged_details_products = pd.merge(
            df_products, df_salesdetails, on="id_producto", how="left"
        )

        df_bestselling = (
            df_merged_details_products[['id_producto', 'producto', 'cantidad']]
            .groupby(['id_producto', 'producto'])['cantidad']
            .sum()
            .reset_index()
            .sort_values(by='cantidad', ascending=False)
        )
        
        print("Producto más vendido:")
        print(df_bestselling.head(1))
    except Exception as e:
        print(f"Ocurrió un error en bestselligproduct: {e}")
        return None


def bestbuyer(df_users, df_sales):
    try:

        df_merged_users_sales = pd.merge(df_users, df_sales, on='id_cliente', how='left')

        df_bestbuyer = (
            df_merged_users_sales[['id_cliente', 'nombre_completo', 'id']]
            .groupby(['id_cliente', 'nombre_completo'])['id']
            .count()
            .reset_index(name='compras')
            .sort_values(by='compras', ascending=False)
        )
        
        print("Mejor comprador:")
        print(df_bestbuyer.head(1))
    except Exception as e:
        print(f"Ocurrió un error en bestbuyer: {e}")
        return None
