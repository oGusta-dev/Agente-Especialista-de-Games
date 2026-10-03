from database import JOGOS_DATABASE

def buscar_jogo(genero, plataforma, hardware):
    for jogo in JOGOS_DATABASE:
        if (jogo["genero"].strip().lower() == genero.strip().lower() and
            jogo["plataforma"].strip().lower() == plataforma.strip().lower() and
            jogo["hardware"].strip().lower() == hardware.strip().lower()):
            return jogo
    return None

