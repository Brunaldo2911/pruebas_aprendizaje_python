apatece_helado = input(" Te apetece un helado? (SI / NO )")
tienes_dinero = input("tienes dinero para el helado? (SI / NO )" )
tio_helados = input("Esta el tio de los helados (SI / NO )" )
esta_la_tia = input("Estas con tu tia? (SI / NO )" )

if apatece_helado == "SI" and (tienes_dinero == "NO" or esta_la_tia == "SI") and tio_helados == "SI":
    print("Comprate un helado")
else:
    print("No compres ni shit")