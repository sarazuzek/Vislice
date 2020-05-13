import model

def izpis_igre(igra):
    return (
        "Pravilni del gesla: {}\n".format(igra.pravilni_del_gesla()) +
        "Neuspeli poskusi: {}\n".format(igra.nepravilni_ugibi()) +
        "Število preostalih poskusov: {}\n".format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak())
    )

def izpis_zmage(igra):
    return (
        "Čestitam, uganil si geslo {}\n".format(igra.geslo) +
        "Uspelo ti je v {} poskusih\n".format(len(igra.crke))
    )

def izpis_poraza(igra):
    return(
        "Porabil si vse poskuse.\n" +
        "Pravilno geslo je bilo {}\n".format(igra.geslo)
    )

def zahtevaj_vnos():
    return input('Vnesi črko: ')

def pozeni_vmestnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        stanje = igra.ugibaj(poskus)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmestnik()
        
