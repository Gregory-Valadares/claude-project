import weather_functions as w7 #Me permite usar minha função de traduzir o Weather-code, printar as informações de clima dos 7 dias.

reset_program = True
while reset_program == True:

    print("Weather App")
    #Validação da entrada de dados da decisão do usuário, se deseja prosseguir com o programa.
    while True:
        run_program = input("Deseja ver as condições climáticas da sua localização? [Tecle 's' para SIM]: ")

        if run_program == "s":
            #Aqui iniciamos o programa com suas funções principais:
            local_json = w7.current_location()

            cidade = str(local_json["city"])
            estado = str(local_json["regionName"])
            pais = str(local_json["country"])
            lat = float(local_json["lat"])
            lon = float(local_json["lon"])
            print(f"Cidade:               {cidade}")
            print(f"Estado:               {estado}")
            print(f"País:                 {pais}")
            print(f"Latitude:             {lat}")
            print(f"Longitude:            {lon}\n")

            weather_json = w7.current_conditions(lat, lon)

            current = weather_json['current']  # Informações atuais
            units = weather_json['current_units']  # Informações atuais
            daily = weather_json["daily"]  # Informações dos próximos dias.
            du = weather_json["daily_units"]  # Informações dos próximos dias.

            w7.show_current_weather(current, units) #Mostra as condições climáticas atuais:
            break

        else:
            print("Programa finalizado com sucesso.")
            reset_program = False
            break

    if not reset_program:  # ✅ se o usuário não quis continuar, para tudo
        break

    # função que utiliza o timedelta de datetime para facilitar o fornecimento de data atual + 6 dias.
    data_final = w7.datafinal(current)

    #Validação de dados da decisão do usuário, se deseja reiniciar o programa.
    while True:
        next_7days = input(f"Deseja saber a previsão do tempo até o dia {data_final}? [s/n]: ").lower()
        try:
            next_7days = str(next_7days)
            if next_7days == 's':
                w7.weather_7days(weather_json, daily, du)
                break

            elif next_7days == 'n':
                reset_program = False
                print("Programa finalizado com sucesso. Obrigado!")
                break

            else:
                print("Digite 's' para SIM e 'n' para NÃO.")

        except:
            print("Caractere inválido. Digite 's' para SIM e 'n' para NÃO.")