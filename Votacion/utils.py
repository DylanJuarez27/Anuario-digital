from .models import Votacion
from Nominacion.models import Nominacion
from Voto.models import Voto
from PremiosGanados.models import PremiosGanados
from django.utils import timezone


def limpiar_elecciones(elecciones):
    ahora = timezone.now()
    elecciones_eliminar = [e for e in elecciones if e.fecha_fin < ahora]
    elecciones_restantes = [e for e in elecciones if e.fecha_fin >= ahora]

    for ele in elecciones_eliminar:
        l = []
        for nominacion in ele.nominacion:
            for perfil in nominacion.perfiles_nominados_list:
                l.append((perfil, perfil.votos.count()))
        
        l = sorted(l, key=lambda par: par[1], reverse=True)
        max_votos = l[0][1] if l else 0
        ganadores = [par for par in l if par[1] == max_votos]
        suma_votos = sum(par[1] for par in ganadores)

        # Eliminar entradas anteriores de ese premio
        PremiosGanados.objects.filter(premio=ele.premio).delete()

        for perfil, votos in ganadores:
            PremiosGanados.objects.create(
                perfil=perfil,
                premio=ele.premio,
                medalla='bi bi-trophy-fill',
                puntaje=votos,
                porcentaje_ganado=(votos / suma_votos) * 100 if suma_votos != 0 else 0
            )

    # Limpieza en la base de datos
    premios_eliminar = [e.premio.id for e in elecciones_eliminar]
    Nominacion.objects.filter(premio_id__in=premios_eliminar).delete()
    Voto.objects.filter(votacion__in=[e.id for e in elecciones_eliminar]).delete()
    for ele in elecciones_eliminar:
        ele.delete()

    return elecciones_restantes