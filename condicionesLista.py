def analizar_notas():
    estudiantes = []
    
    # Pedir nombre y nota hasta que el usuario escriba 'fin'
    while True:
        nombre = input("Ingresa el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        entrada_nota = input(f"Ingresa la nota para {nombre}: ")
        try:
            nota = float(entrada_nota)
            if 0 <= nota <= 10:
                estudiantes.append({'nombre': nombre, 'nota': nota})
            else:
                print("La nota debe estar entre 0 y 10")
        except ValueError:
            print("Ingresa un número válido para la nota")
    
    if not estudiantes:
        print("No hay estudiantes para analizar")
        return
    
    # Clasificar estudiantes
    aprobados = [est for est in estudiantes if est['nota'] >= 5]
    suspendidos = [est for est in estudiantes if est['nota'] < 5]
    notables = [est for est in estudiantes if 7 <= est['nota'] < 9]
    sobresalientes = [est for est in estudiantes if est['nota'] >= 9]
    
    total = len(estudiantes)
    
    # Calcular porcentajes
    pct_aprobados = (len(aprobados) / total) * 100
    pct_suspendidos = (len(suspendidos) / total) * 100
    pct_notables = (len(notables) / total) * 100
    pct_sobresalientes = (len(sobresalientes) / total) * 100
    
    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"Aprobados ({len(aprobados)} - {pct_aprobados:.2f}%): {', '.join([f"{est['nombre']} ({est['nota']})" for est in aprobados])}")
    print(f"Suspendidos ({len(suspendidos)} - {pct_suspendidos:.2f}%): {', '.join([f"{est['nombre']} ({est['nota']})" for est in suspendidos])}")
    print(f"Notables ({len(notables)} - {pct_notables:.2f}%): {', '.join([f"{est['nombre']} ({est['nota']})" for est in notables])}")
    print(f"Sobresalientes ({len(sobresalientes)} - {pct_sobresalientes:.2f}%): {', '.join([f"{est['nombre']} ({est['nota']})" for est in sobresalientes])}")

analizar_notas()