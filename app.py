
from src.data_load import (load_csv, load_json)
from src.frequency import (bestselligproduct, bestbuyer)

def main():
    option = int(input("""Seleccione que tipo de archivos se van a cargar
    1. Archivos CSV
    2. Archivos JSON
Opción: """))
    print()
    print("="*40)
    print()
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

def main_analysis(df_address, df_products, df_sales, df_salesdetails, df_users):
    while True:
        print()
        print("="*40)
        print()
        option = int(input("""CAMPO DIGITAL ANALISIS DE DATOS
    Seleccione una opción:
        1. Análisis de Frecuencia.
        2. Análisis de Agregación.
        3. Análisis con Filtrado y Conteo.
        4. Salir.
    Opción: """))

        match option:
            case 1:
                print()
                frequency_option = int(input("""ANALISIS DE FRECUENCIA
    Seleccione una opción:
        1. ¿Qué producto ha sido el más vendido?
        2. ¿Qué usuario ha realizado la mayor cantidad de compras?
    Opción: """))
                match frequency_option:
                    case 1:
                        print()
                        bestselligproduct(df_salesdetails,df_products)
                        print()

                    case 2:
                        print()
                        bestbuyer(df_users, df_sales)
                        print()
                        pass

            case 2:
                print()
                aggregation_option = int(input("""ANÁLISIS DE AGREGACIÓN
    Seleccione una opción:
        1. ¿Cuál es el total de ventas por usuario?
        2. ¿Cuál es la cantidad total de productos vendidos por dirección de envío?
    Opción: """))
                match aggregation_option:
                    case 1:
                        print()
                        # total_sales_per_user(df_sales, df_salesdetails)
                        print("Genaro ha comprado mil pesos")
                        print()
                        pass
                    case 2:
                        print()
                        # total_products_by_address(df_sales, df_salesdetails, df_address)
                        print("La direccion x tiene tantos envios")
                        print()
                        pass

            case 3:
                print()
                filter_option = int(input("""ANÁLISIS CON FILTRADO Y CONTEO
    Seleccione una opción:
        1. ¿Cuántos usuarios han hecho más de 5 compras?
        2. ¿Cuántas ventas se enviaron a la ciudad de "Bogotá"?
    Opción: """))
                match filter_option:
                    case 1:
                        print()
                        # users_with_more_than_five_purchases(df_sales)
                        print("21 genaros")
                        print()
                        pass
                    case 2:
                        print()
                        # sales_to_bogota(df_sales, df_address)
                        print("cualesquier 5")
                        print()
                        pass
            case 4:
                print()
                print("Saliendo")
                print()
                break
            case _:
                print()
                print("Seleccione una opción valida")
                print()

main()



