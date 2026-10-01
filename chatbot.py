# CHATBOT DE ACTIVIDADES EN CDMX 
print('  𐙚‧₊˚📒✩ ₊˚☁️⊹♡   CDMX  𐙚‧₊˚📒✩ ₊˚☁️⊹♡')
print('                 actividades          ')

# Menú inicial
menu = 0

while menu != 4:
    menu = int(input('\n1. Comida \n2. Museos \n3. Música \n4. Salir\nElige una opción: '))

    # OPCIÓN 1 COMIDA
    if menu == 1:
        print('˚🥟⋅₊🍱 ࣪˖ ִֶ‧₊˚🍜 ࿔*:')
        # MENÚ PARA COMIDA
        comida = int(input('1. Pizza \n2. Comida mexicana \n3. Comida asiática \n0. Regresar al menú principal\nElige una opción: '))
        # PIZZA
        if comida == 1:
            print('Elige una opción: 🍕')
            pizza = input('a) Pizza estilo Nueva York \nb) Pizza estilo Chicago \nc) Pizza Napolitana\n: ')
            if pizza == 'a':
                print("Boogie's Pizza")
            elif pizza == 'b':
                print("Homeslice Pizza")
            elif pizza == 'c':
                print('Ardente Pizza')
            else:
                print('Opción no válida')
            
            ubicacion = input('¿Necesitas la ubicación? Si/No: ').lower()
            if ubicacion == 'si':
                if pizza == 'a':
                    print('Condesa, CDMX')
                elif pizza == 'b':
                    print('Colonia del Valle Sur, CDMX')
                elif pizza == 'c':
                    print('Cuauhtémoc, CDMX')
            elif ubicacion != 'no':
                print('Opción no válida')

        # MEXICANA
        elif comida == 2:
            print('Elige un restaurant: 🌮')
            mexican = input('a) El Bajío \nb) Corazón de Maguey\n: ')
            if mexican == 'a':
                print("Dirección: Av. Insurgentes Sur 800, Col. Del Valle")
            elif mexican == 'b':
                print("Dirección: Jardín Centenario 9-A, Villa Coyoacán, Coyoacán, 04000 Ciudad de México, CDMX")
            else:
                print('Opción no válida')

        # ASIÁTICA
        elif comida == 3:
            sugerencia = input('¿Recomendación? Si/No: ').lower()
            if sugerencia == 'si':
                print('Ling Ling by Hakkasan')
            elif sugerencia != 'no': 
                print('Opción no válida')

    # OPCIÓN 2 MUSEOS
    elif menu == 2:
        museos = int(input("1. Museos para niños \n2. Museos contemporáneos \n0. Regresar al menú principal\nElige una opción: "))
        if museos == 1:
            ninos = input('a) Papalote museo del niño \nb) Museo de historia natural y cultura ambiental \nc) Regresar al menú\n: ').lower()
            if ninos == 'a':
                boletos = input('Comprar boletos: Si/No: ').lower()
                if boletos == 'si':
                    print('Boleto número 1')
            elif ninos == 'b':
                sugerencia = input('Ingresa la letra A para conocer una sala sorpresa!: ').lower()
                if sugerencia == 'a':
                    print('Dinosaurios | Sala Nueva!\nIngresa a la página web de nuestro museo para conocerla!')
            elif ninos != 'c': 
                print('Opción no válida')
            
        elif museos == 2:
            contemporaneo = input('| Museo Franz Mayer |\na) Lista de inventario \nb) Comprar una visita guiada\n: ').lower()
            if contemporaneo == 'a':
                print('♡ Orfebrería y Plata. \n♡ Cerámica y Vidrio. \n♡ Mobiliario y Biombos. \n♡ Pintura y Escultura. \n♡ Relojes y Textiles.')
            elif contemporaneo == 'b':
                descuento = input('¿Cuentas con credencial de estudiante? Si/No: ').lower()
                precio = 150
                if descuento == 'no':
                    print('El precio del boleto es de $150')
                elif descuento == 'si':
                    print('El precio del boleto con descuento es de $' + str(precio*0.6))
                else: 
                    print('Opción no válida')
        elif museos != 0:
            print('Opción no válida')

    # OPCIÓN 3 MÚSICA
    elif menu == 3: 
        print('♫₊˚.🎧 ✧')
        musica = int(input('1. Próximas conciertos \n2. Participa en la rifa de boletos \n3. Recomendaciones musicales \n0. Regresar al menú principal\nElige una opción: '))
        
        if musica == 1:
            genero = input('Género: \na) Pop \nb) Clásico\n: ').lower()

            if genero == 'a':
                artistapop = input('Ingresa el artista que prefieras (Adele, Coldplay o Miley Cyrus): ').lower()
                if artistapop == 'miley cyrus':
                    print('Próximo concierto: Corona Capital | Noviembre 20')
                elif artistapop == 'adele':
                    print('¡Lo sentimos!, por el momento no hay conciertos.')
                elif artistapop == 'coldplay':
                    print('Las fechas se anunciarán pronto!')
                else:
                    print('Artista no encontrado')
            
            elif genero == 'b':
                clasica = input('Ingresa una opción (Palacio de Bellas Artes / Auditorio Nacional): ').lower()
                if clasica == 'auditorio nacional':
                    print('El Cascanueces | 18 - 23 de Diciembre')
                    boletos = input('¿Deseas comprar boletos? Si/No: ').lower()
                    if boletos == 'si':
                        eleccion = int(input("Ingresa un precio entre $470 y $2000: "))
                        
                        if eleccion == 470:
                            print("Zona C | Boleto: $470")
                            compra = input('¿Comprar? Si/No: ').lower()
                            if compra == 'si':
                                print('Boleto #1')
                            elif compra == 'no':
                                print('Compra cancelada')
                            else:
                                print('Opción no válida')
                            
                        elif 470 < eleccion < 1000:
                            print('Zona B | Boleto: $700')
                            compra = input('¿Comprar? Si/No: ').lower()
                            if compra == 'si':
                                print('Boleto #1')
                            elif compra == 'no':
                                print('Compra cancelada')
                            else:
                                print('Opción no válida')
                            
                        elif 1000 <= eleccion <= 2000:
                            print('Zona A | Boleto: $1500')
                            compra = input('¿Comprar? Si/No: ').lower()
                            if compra == 'si':
                                print('Boleto #1')
                            elif compra == 'no':
                                print('Compra cancelada')
                            else:
                                print('Opción no válida')
                        else:
                            print('Precio fuera del rango')
                    elif boletos != 'no':
                        print('Opción no válida')

print('¡Gracias por usar el chatbot de la CDMX! ¡Hasta luego!')
