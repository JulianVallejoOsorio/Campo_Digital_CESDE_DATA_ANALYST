import pandas as pd

def clean_sales(df_sales):
    try:
        default_date = pd.to_datetime("1900-01-01")

        df_sales = df_sales.dropna(subset=["id"]).copy()

        if pd.api.types.is_numeric_dtype(df_sales["fecha"]):
            df_sales["fecha"] = pd.to_datetime(
                df_sales["fecha"].astype("Int64"),
                unit="D", origin="1899-12-30", errors="coerce"
            )
        else:
            df_sales["fecha"] = pd.to_datetime(
                df_sales["fecha"].astype(str), errors="coerce", dayfirst=True
            )
        df_sales["fecha"] = df_sales["fecha"].fillna(default_date)

        if "direccion_id" in df_sales.columns:
            df_sales["direccion_id"] = df_sales["direccion_id"].fillna(0).astype(int)
            
        df_sales["total"] = (
            df_sales["total"]
            .astype(str)
            .str.replace(r"[^\d.,-]", "", regex=True)
            .str.replace(",", ".", regex=False)
        )

        df_sales["total"] = pd.to_numeric(df_sales["total"], errors="coerce").fillna(0)

        return df_sales.reset_index(drop=True)

    except Exception as e:
        print(f"Error en clean_sales: {e}")
        return df_sales


def clean_salesdetails(df_salesdetails):
    try:
        df_salesdetails["cantidad"] = pd.to_numeric(df_salesdetails["cantidad"], errors="coerce")
        df_salesdetails["subtotal"] = pd.to_numeric(df_salesdetails["subtotal"], errors="coerce")

        mask = (
            df_salesdetails["id_detalle"].notna() &
            df_salesdetails["id_venta"].notna() &
            df_salesdetails["id_producto"].notna() &
            df_salesdetails["cantidad"].notna() &
            (df_salesdetails["cantidad"] > 0)
        )

        df_salesdetails = df_salesdetails[mask].copy()

        df_salesdetails["cantidad"] = df_salesdetails["cantidad"].astype(int)
        if df_salesdetails["subtotal"].notna().any():
            df_salesdetails["subtotal"] = df_salesdetails["subtotal"].astype(float)

        return df_salesdetails.reset_index(drop=True)

    except Exception as e:
        print(f"Error en clean_salesdetails: {e}")
        return df_salesdetails



def clean_products(df_products):
    try:
        if df_products["precio"].dtype == "object":
            df_products["precio"] = (
                df_products["precio"]
                .astype(str)
                .str.replace(r"[^\d.,-]", "", regex=True)
                .str.replace(",", ".", regex=False)
            )

        df_products["precio"] = pd.to_numeric(df_products["precio"], errors="coerce")

        df_products = df_products.dropna(subset=["id_producto"]).copy()

        if "is_active" in df_products.columns:
            df_products["is_active"] = df_products["is_active"].fillna(True).astype(bool)
        else:
            df_products["is_active"] = True

        for col in ["producto", "descripcion", "categoria", "unidad"]:
            if col in df_products.columns:
                df_products[col] = df_products[col].fillna("Desconocido")

        return df_products.reset_index(drop=True)

    except Exception as e:
        print(f"Error en clean_products: {e}")
        return df_products


def clean_address(df_address):
    try:
        df_address = df_address.dropna(subset=["id_direccion"]).copy()

        if "id_cliente" in df_address.columns:
            df_address["id_cliente"] = df_address["id_cliente"].fillna(0).astype(int)

        if "descripcion" in df_address.columns:
            df_address["descripcion"] = df_address["descripcion"].fillna("Desconocido")

        if "codigo_ciudad" in df_address.columns:
            df_address["codigo_ciudad"] = df_address["codigo_ciudad"].fillna(1).astype(int)

        return df_address.reset_index(drop=True)

    except Exception as e:
        print(f"Error en clean_address: {e}")
        return df_address



def clean_users(df_users):
    try:
        default_date = pd.to_datetime("1900-01-01")

        df_users = df_users.dropna(subset=["id_cliente"]).copy()

        for col in ["nombre_completo", "email", "telefono", "username", "numero_documento"]:
            if col in df_users.columns:
                df_users[col] = df_users[col].fillna("Desconocido")

        if "fecha_nacimiento" in df_users.columns:
            df_users["fecha_nacimiento"] = pd.to_datetime(
                df_users["fecha_nacimiento"], errors="coerce"
            ).fillna(default_date)

        return df_users.reset_index(drop=True)

    except Exception as e:
        print(f"Error en clean_users: {e}")
        return df_users


def clean_all(df_address, df_products, df_sales, df_salesdetails, df_users):
    return (
        clean_address(df_address),
        clean_products(df_products),
        clean_sales(df_sales),
        clean_salesdetails(df_salesdetails),
        clean_users(df_users),
    )