apatece_helado_input = input(" Te apetece un helado? (SI / NO) ").upper()

if apatece_helado_input == "SI":
    apetece_helado = True
elif apatece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te dije que me digas que si o no patulopus")
    apetece_helado = False

tienes_dinero_input = input("tienes dinero para el helado? (SI / NO) ").upper()
tio_helados_input = input("Esta el tio de los helados (SI / NO) ").upper()
esta_la_tia_input = input("Estas con tu tia? (SI / NO) ").upper()

puedes_permitirtelo = tienes_dinero_input == "SI"
esta_la_tia = esta_la_tia_input == "SI"
if apetece_helado and puedes_permitirtelo and esta_la_tia:
    print("Comprate un rikolino helado")
else:
    print("Ya fochis papu")