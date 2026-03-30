import csv

def save_csv(inventary, ruta, incluir_header=True):
    

    if not inventary:
        print("\n-----There are no Student-----\n")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

    
            if incluir_header:
                writer.writerow(["ID", "name", "age", "program", "stade"])

   
            for producto in inventary:
                writer.writerow([
                    producto["ID"],
                    producto["name"],
                    producto["age"],
                    producto["program"],
                    producto["stade"]
                ])

        print(f"\n Inventario guardado en: {ruta}\n")

    except Exception as e:
        print(f"\n Error al guardar archivo: {e}\n")


def load_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            
   
            encabezado = next(reader)

            if encabezado != ["ID", "name", "age", "program", "stade"]:
                print("\n Encabezado inválido\n")
                return []

            for fila in reader:
                if len(fila) != 5:
                    errores += 1
                    continue

                try:
                    ID = int(fila[0])
                    name = fila[1]
                    age = int(fila[2])
                    program = fila[3]
                    stade = fila[4]

                    if ID < 0 or age < 0:
                        errores += 1
                        continue

                    producto = {
                        "ID": ID,
                        "name": name,
                        "age": age,
                        "program": program,
                        "stade": stade
                    }

                    inventario.append(producto)

                except ValueError:
                    errores += 1

        print(f"\n Productos cargados: {len(inventario)}")
        print(f" Filas inválidas omitidas: {errores}\n")

        return inventario

    except FileNotFoundError:
        print("\n Archivo no encontrado\n")
        return []

    except Exception as e:
        print(f"\n Error al leer archivo: {e}\n")
        return []