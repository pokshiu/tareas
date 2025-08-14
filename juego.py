#----------------------------------------------------------------------------------------------------------------------------------
#                                             ¡Bienvenido al Juego de Aventura de Mago!
#                                         Tu historia empieza en una antigua torre.
#----------------------------------------------------------------------------------------------------------------------------------

print("Eres un joven aprendiz de mago en una antigua torre. El viejo mago ha salido, y estás a cargo de la torre.")
print("De repente, escuchas un estruendo proveniente del sótano. Algo ha caído.")
print("Tienes dos objetos a tu alcance para investigar: un libro de hechizos o una antorcha.")

# Nivel 1: Primera decisión (2 opciones)
# Se usa .upper() para que la entrada del usuario sea insensible a mayúsculas y minúsculas.
opcion1 = input("¿Qué decides? ¿LIBRO DE HECHIZOS o ANTORCHA? ").upper()

if opcion1 == "LIBRO DE HECHIZOS":
    #----------------------------------------------------------------------------------------------------------------------------------
    #                                              CAMINO DEL LIBRO DE HECHIZOS
    #----------------------------------------------------------------------------------------------------------------------------------
    print("\n--- ¡Has elegido el libro de hechizos! ---")
    print("Tomas el libro de hechizos y desciendes las escaleras de piedra. El sótano está oscuro y hay un polvo mágico flotando en el aire.")
    print("Tu libro se abre solo y una página se ilumina. Muestra un hechizo para crear luz y otro para crear una ilusión.")
    
    # Nivel 2: Decisión (2 opciones)
    opcion2 = input("¿Qué hechizo usarás? ¿LUZ o ILUSIÓN? ").upper()

    if opcion2 == "LUZ":
        #----------------------------------------------------------------------------------------------------------------------------------
        #                                           CAMINO DEL LIBRO - LUZ
        #----------------------------------------------------------------------------------------------------------------------------------
        print("\n--- Creas una esfera de luz. ---")
        print("La esfera flota y revela una gran criatura de piedra que se ha desprendido del techo. Parece inofensiva.")
        print("La criatura tiene una llave en una de sus manos de piedra.")
        
        # Nivel 3: Decisión (2 opciones)
        opcion3 = input("¿Qué haces? ¿TOMAR la llave o IGNORARLA? ").upper()
        
        if opcion3 == "TOMAR":
            #----------------------------------------------------------------------------------------------------------------------------------
            #                                           CAMINO DEL LIBRO - LUZ - TOMAR
            #----------------------------------------------------------------------------------------------------------------------------------
            print("\n--- Coges la llave. ---")
            print("Al tomar la llave, se ilumina un portal en la pared del fondo. Parece un camino de escape.")
            
            # Nivel 4: Decisión (3 opciones)
            opcion4 = input("¿Qué haces? ¿ENTRAR al portal, BUSCAR más objetos o SALIR del sótano? ").upper()

            if opcion4 == "ENTRAR":
                #----------------------------------------------------------------------------------------------------------------------------------
                #                                          CAMINO DEL LIBRO - LUZ - TOMAR - ENTRAR
                #                                          ¡Este es el sexto nivel de decisión!
                #----------------------------------------------------------------------------------------------------------------------------------
                print("\nEntras al portal. La luz te envuelve y al disiparse, te encuentras en un bosque mágico lleno de criaturas luminosas.")
                print("Te das cuenta de que has viajado a otro reino.")
                
                # Nivel 5: Decisión (2 opciones)
                opcion5 = input("¿Qué haces? ¿EXPLORAR el nuevo reino o BUSCAR la forma de REGRESAR a la torre? ").upper()
                
                if opcion5 == "EXPLORAR":
                    #----------------------------------------------------------------------------------------------------------------------------------
                    #                                        CAMINO DEL LIBRO - LUZ - TOMAR - ENTRAR - EXPLORAR
                    #                                        ¡Este es el sexto nivel de decisión!
                    #----------------------------------------------------------------------------------------------------------------------------------
                    print("\n--- Decides explorar. ---")
                    print("Caminas un poco y encuentras un hermoso lago, en el cual hay una espada mágica en el fondo. Te preguntas si hay algo más allá del lago.")
                    
                    # Nivel 6: Decisión (3 opciones)
                    opcion6 = input("¿Qué haces? ¿NADAR para conseguir la espada, IR alrededor del lago o SALIR del lugar? ").upper()

                    if opcion6 == "NADAR":
                        print("\nNadas hacia el fondo del lago y logras conseguir la espada. ¡Te has convertido en un poderoso guerrero! FIN del juego.")
                    elif opcion6 == "IR":
                        print("\nCaminas alrededor del lago y sigues explorando el bosque, hasta que encuentras la salida. FIN del juego.")
                    elif opcion6 == "SALIR":
                        print("\nDecides que el lago es muy peligroso y te das la vuelta para salir. FIN del juego.")
                    else:
                        print("Opción no válida. Debes elegir NADAR, IR o SALIR.")
                
                elif opcion5 == "REGRESAR":
                    print("\nBuscas la forma de regresar y el portal se abre de nuevo para ti. Vuelves a la torre sano y salvo. FIN del juego.")
                
                else:
                    print("Opción no válida. Debes elegir EXPLORAR o REGRESAR.")

            elif opcion4 == "BUSCAR":
                print("\nBuscas más objetos y encuentras una gema mágica. Decides tomarla y salir del sótano. FIN del juego.")
            
            elif opcion4 == "SALIR":
                print("\nTe asustas y sales corriendo del sótano, cerrando la puerta detrás de ti. FIN del juego.")

            else:
                print("Opción no válida. Debes elegir ENTRAR, BUSCAR o SALIR.")

        elif opcion3 == "IGNORARLA":
            print("\n--- Ignoras la llave. ---")
            print("Regresas a la torre, dejando el sótano intacto. No sabes lo que podría haber pasado.")
            print("FIN del juego. Has evitado un peligro desconocido, pero te quedas con la duda de qué era la llave.")
        
        else:
            print("Opción no válida. Debes elegir TOMAR o IGNORARLA.")

    elif opcion2 == "ILUSIÓN":
        print("\n--- Creas una ilusión. ---")
        print("La ilusión de un gran dragón aparece y la criatura de piedra reacciona. Ves que es un golem protector.")
        print("El golem te ve como una amenaza. Tienes que pensar rápido.")
        
        # Nivel 3: Decisión (3 opciones)
        opcion3_b = input("¿Qué haces? ¿HUIR, LUCHAR o OFRECER un objeto para calmarlo? ").upper()
        
        if opcion3_b == "HUIR":
            print("\nSales corriendo del sótano. La torre tiembla, pero logras escapar. FIN del juego.")
        elif opcion3_b == "LUCHAR":
            print("\nIntentas atacar al golem con otro hechizo, pero es demasiado fuerte. El golem te deja inconsciente. FIN del juego.")
        elif opcion3_b == "OFRECER":
            print("\nOfreces tu libro de hechizos al golem. El golem lo toma y te deja salir del sótano, a salvo. FIN del juego.")
        else:
            print("Opción no válida. Debes elegir HUIR, LUCHAR o OFRECER.")

    else:
        print("Opción no válida. Debes elegir LUZ o ILUSIÓN.")

elif opcion1 == "ANTORCHA":
    #----------------------------------------------------------------------------------------------------------------------------------
    #                                              CAMINO DE LA ANTORCHA
    #----------------------------------------------------------------------------------------------------------------------------------
    print("\n--- ¡Has elegido la antorcha! ---")
    print("Bajas las escaleras, la antorcha ilumina un camino polvoriento en la pared. Encuentras un cofre antiguo.")
    print("Parece estar cerrado con un hechizo.")
    
    # Nivel 2: Decisión (2 opciones)
    opcion2_b = input("¿Qué haces? ¿INTENTAR abrirlo con fuerza o BUSCAR la forma de desactivar el hechizo? ").upper()

    if opcion2_b == "INTENTAR":
        #----------------------------------------------------------------------------------------------------------------------------------
        #                                           CAMINO DE LA ANTORCHA - INTENTAR
        #----------------------------------------------------------------------------------------------------------------------------------
        print("\n--- Intentas abrirlo a la fuerza. ---")
        print("El cofre tiene una cerradura mágica que se activa y te lanza una maldición. Te conviertes en un sapo.")
        print("FIN del juego. ¡No debiste haberlo forzado!")
        
    elif opcion2_b == "BUSCAR":
        #----------------------------------------------------------------------------------------------------------------------------------
        #                                           CAMINO DE LA ANTORCHA - BUSCAR
        #----------------------------------------------------------------------------------------------------------------------------------
        print("\n--- Buscas la forma de desactivar el hechizo. ---")
        print("Encuentras un pequeño pergamino que describe el hechizo y te da tres opciones para abrir el cofre.")
        
        # Nivel 3: Decisión (3 opciones)
        opcion3_b = input("¿Qué haces? ¿DECIR la palabra mágica, OFRECER un objeto de valor o USAR un conjuro para abrirlo? ").upper()
        
        if opcion3_b == "DECIR":
            #----------------------------------------------------------------------------------------------------------------------------------
            #                                           CAMINO DE LA ANTORCHA - BUSCAR - DECIR
            #                                           ¡Aquí se cumplen las 3 opciones!
            #----------------------------------------------------------------------------------------------------------------------------------
            print("\n--- Dices la palabra mágica. ---")
            print("El cofre se abre con un clic. Dentro encuentras una poción y una moneda de oro.")
            
            # Nivel 4: Decisión (2 opciones)
            opcion4_b = input("¿Qué haces? ¿TOMAR la poción o LA MONEDA? ").upper()
            
            if opcion4_b == "TOMAR":
                #----------------------------------------------------------------------------------------------------------------------------------
                #                                          CAMINO DE LA ANTORCHA - BUSCAR - DECIR - TOMAR
                #                                          ¡Este es el sexto nivel de decisión!
                #----------------------------------------------------------------------------------------------------------------------------------
                print("\n--- Te bebes la poción. ---")
                print("Te sientes invencible. El cofre tiene un mapa del tesoro. Ahora tienes que elegir tu camino.")
                
                # Nivel 5: Decisión (3 opciones)
                opcion5 = input("¿Qué haces? ¿BUSCAR el tesoro, QUEDARSE en la torre o TIRAR el mapa? ").upper()

                if opcion5 == "BUSCAR":
                    #----------------------------------------------------------------------------------------------------------------------------------
                    #                                        CAMINO DE LA ANTORCHA - BUSCAR - DECIR - TOMAR - BUSCAR
                    #                                        ¡Este es el sexto nivel de decisión!
                    #----------------------------------------------------------------------------------------------------------------------------------
                    print("\n--- Decides buscar el tesoro. ---")
                    print("El mapa te lleva a una caverna con tres entradas.")
                    
                    # Nivel 6: Decisión (3 opciones)
                    opcion6 = input("¿Qué haces? ¿ENTRAR por la entrada de la DERECHA, IZQUIERDA o la del CENTRO? ").upper()

                    if opcion6 == "DERECHA":
                        print("\nEntras por la derecha, la caverna te lleva a un dragón. ¡FIN del juego!")
                    elif opcion6 == "IZQUIERDA":
                        print("\nEntras por la izquierda, la caverna se derrumba y te quedas atrapado. ¡FIN del juego!")
                    elif opcion6 == "CENTRO":
                        print("\nEntras por el centro, la caverna te lleva a un tesoro lleno de oro. ¡FIN del juego!")
                    else:
                        print("Opción no válida. Debes elegir DERECHA, IZQUIERDA o CENTRO.")
                
                elif opcion5 == "QUEDARSE":
                    print("\nDecides que el tesoro no vale la pena. Te quedas en la torre hasta que regresa el mago. FIN del juego.")
                
                elif opcion5 == "TIRAR":
                    print("\nTiras el mapa. El mapa cobra vida y te ataca, derrotándote. FIN del juego.")
                
                else:
                    print("Opción no válida. Debes elegir BUSCAR, QUEDARSE o TIRAR.")

            elif opcion4_b == "LA MONEDA":
                print("\nTomas la moneda de oro. Sales del sótano y decides usar el oro para irte de la torre. FIN del juego.")
            
            else:
                print("Opción no válida. Debes elegir TOMAR o LA MONEDA.")

        elif opcion3_b == "OFRECER":
            print("\nOfreces tu antorcha como sacrificio. El cofre te recompensa con un mapa, pero te quedas sin luz en el sótano. FIN del juego.")
        
        elif opcion3_b == "USAR":
            print("\nIntentas usar un conjuro, pero el pergamino no es para ti. El hechizo rebota y te conviertes en una estatua de hielo. FIN del juego.")
        
        else:
            print("Opción no válida. Debes elegir DECIR, OFRECER o USAR.")

    else:
        print("Opción no válida. Debes elegir INTENTAR o BUSCAR.")

else:
    print("Opción no válida. Debes elegir LIBRO DE HECHIZOS o ANTORCHA.")