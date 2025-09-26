import pandas as pd
import os

def load_csv():
    files = { 
    'df_address': "data/address/address.csv",
    'df_products': "data/products/products.csv",
    'df_sales': "data/sales/sales.csv",
    'df_salesdetails': "data/sales_details/sales_details.csv",
    'df_users': "data/users/users.csv"
    }

    data_frames = {}
    
    for key, file_path in files.items():
        if os.path.exists(file_path):
            try:
                data_frames[key] = pd.read_csv(file_path, sep=";")
                print(f"Archivo {key} cargado correctamente.")
            except Exception as e:
                print(f"Error al cargar el archivo {key}: {e}")
        else:
            print(f"El archivo {key} no existe en la ruta: {file_path}")
            
        if len(data_frames) == len(files):
            return (data_frames["df_address"], data_frames["df_products"], data_frames["df_sales"],
                    data_frames["df_salesdetails"], data_frames["df_users"])
    else:
        raise ValueError("No se cargaron todos los archivos. Verifica los mensajes de error.")
    
def load_json():
    files ={     
    'df_products': "data/products/products.json",
    'df_address': "data/address/address.json",
    'df_sales': "data/sales/sales.json",
    'df_salesdetails': "data/sales_details/sales_details.json",
    'df_users': "data/users/users.json"
    }
    
    data_frames={}
    
    for key, file_path in files.items():
        if os.path.exists(file_path):
            try:
                data_frames[key]= pd.read_json(file_path)
                print(f"Archivo {key} cargado correctamente.")
            except Exception as e:
                print(f"Error al cargar el archivo {key}: {e}")
        else:
            print(f"El archivo {key} no existe en la ruta: {file_path}")
        if len(data_frames) == len(files):
            return (data_frames["df_address"], data_frames["df_products"], data_frames["df_sales"],
                    data_frames["df_salesdetails"], data_frames["df_users"])
    else:
        raise ValueError("No se cargaron todos los archivos. Verifica los mensajes de error.")
    
        match option:
        case 1:
            try:
                df_address, df_products, df_sales, df_salesdetails, df_users = load_csv()
                main_analysis(df_address, df_products, df_sales, df_salesdetails, df_users)
            except ValueError as e:
                print(e)
        case 2:
            try:
                df_address, df_products, df_sales, df_salesdetails, df_users = load_json()
                main_analysis(df_address, df_products, df_sales, df_salesdetails, df_users)
            except ValueError as e:
                print(e)
        case _:
            print("Opción incorrecta, por favor seleccione una de las opciónes disponibles")