import weather_functions as wf

reset_program = True
while reset_program == True:

    print("Weather App")

    while True:
        run_program = input("Deseja ver as condições climáticas da sua localização? [Tecle 's' para SIM]: ").lower()

        if run_program == "s":
            local_json = wf.current_location()

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

            weather_json = wf.current_conditions(lat, lon)

            current = weather_json['current']
            units = weather_json['current_units']
            daily = weather_json["daily"]
            du = weather_json["daily_units"]

            wf.show_current_weather(current, units)
            break

        else:
            print("Programa finalizado com sucesso.")
            reset_program = False
            break  # ✅ sai do while interno

    if not reset_program:  # ✅ se o usuário não quis continuar, para tudo
        break

    # Só chega aqui se o usuário digitou 's'
    data_final = wf.datafinal(current)

    while True:
        next_7days = input(f"Deseja saber a previsão do tempo até o dia {data_final}? [s/n]: ").lower()

        if next_7days == 's':
            wf.weather_7days(daily, du)
            break

        elif next_7days == 'n':
            reset_program = False
            print("Programa finalizado com sucesso. Obrigado!")
            break

        else:
            print("Digite 's' para SIM e 'n' para NÃO.")