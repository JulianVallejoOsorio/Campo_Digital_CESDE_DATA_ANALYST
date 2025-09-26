import pandas as pd
from src.clean_text_rows import clean_text_rows_na

def bestselligproduct(df_salesdetails, df_products):
    try:

        df_merged_details_products = pd.merge(
            df_products, df_salesdetails, on="id_producto", how="left"
        )

        df_merged_details_products = clean_bestselling_na(df_merged_details_products)

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


def clean_bestselling_na(df_merged_details_products):
    try:
        df_merged_details_products = df_merged_details_products.dropna(
            subset=['subtotal', 'precio'], how="all"
        )

        mask_subtotal_na = df_merged_details_products['subtotal'].isna() & df_merged_details_products['cantidad'].notna()
        df_merged_details_products.loc[mask_subtotal_na, 'subtotal'] = (
            df_merged_details_products.loc[mask_subtotal_na, 'precio'] * 
            df_merged_details_products.loc[mask_subtotal_na, 'cantidad']
        )
        
        mask_precio_na = df_merged_details_products['precio'].isna() & (df_merged_details_products['cantidad'] > 0)
        df_merged_details_products.loc[mask_precio_na, 'precio'] = (
            df_merged_details_products.loc[mask_precio_na, 'subtotal'] / 
            df_merged_details_products.loc[mask_precio_na, 'cantidad']
        )

    except Exception as e:
        print(f"Ocurrió un error en clean_bestselling_na: {e}")

    return df_merged_details_products


def bestbuyer(df_users, df_sales):
    try:

        df_merged_users_sales = pd.merge(df_users, df_sales, on='id_cliente', how='left')

        df_merged_users_sales = clean_bestbuyer_na(df_merged_users_sales)
        clean_text_rows_na(df_merged_users_sales, replace_value='Desconocido')

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

def clean_bestbuyer_na(df_merged_users_sales):
    try:
        default_date = pd.to_datetime('1900-01-01')

        df_merged_users_sales = df_merged_users_sales.dropna(subset=['id', 'total']).copy()

        if pd.api.types.is_numeric_dtype(df_merged_users_sales['fecha']):
            
            df_merged_users_sales.loc[:, 'fecha'] = (
                df_merged_users_sales['fecha'].astype('Int64')
            )
            df_merged_users_sales.loc[:, 'fecha'] = pd.to_datetime(
                df_merged_users_sales['fecha'],
                unit='D', origin='1899-12-30', errors='coerce'
            )
        else:
            df_merged_users_sales.loc[:, 'fecha'] = pd.to_datetime(
                df_merged_users_sales['fecha'].astype(str),
                errors='coerce', dayfirst=True
            )

        df_merged_users_sales.loc[:, 'fecha_nacimiento'] = (
            pd.to_datetime(df_merged_users_sales['fecha_nacimiento'], errors='coerce')
            .fillna(default_date)
            .astype("datetime64[ns]")
        )
        
        df_merged_users_sales.loc[:, 'direccion_id'] = (
            df_merged_users_sales['direccion_id'].fillna(0).astype(int)
        )

        return df_merged_users_sales

    except Exception as e:
        print(f"Ocurrió un error en clean_bestbuyer_na: {e}")
        return df_merged_users_sales
