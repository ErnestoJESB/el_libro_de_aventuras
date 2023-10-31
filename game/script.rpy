init:
    $ vida_bruja = 3  # La bruja comienza con 3 vidas
    $ vida_dragon = 3 # El dragón comienza con 3 vidas
    $ vida_nino = 3   # El niño comienza con 3 vidas
    $ puntaje = 0     # Inicializa el puntaje del jugador
    
# Declare characters used by this game.
define l = Character(_("Mr. lapiz"), color="#c8ffda")
define m = Character(_("Me"), color="#c8c8ff")
define d = Character(_("Draco"), color="#f0b3a0")
define n = Character(_("Narrador"), color="#bca0f0")
define b = Character(_("Bruja"), color="#a0f0a7")
# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene inicio
    with dissolve
    n "Eres un niño que le gustan los libros y la lectura."
    
    scene inicio1
    with dissolve
    n "Encuentras uno bien curioso y al abrilo ves que el libro está encantado."

    scene inicio2
    with dissolve
    n "En ese instante eres absorbido por él."

    scene libreta
    with dissolve
    n "Ahora estás atrapado dentro."

    scene lapiz2
    with dissolve
    l "Hola, soy el señor Lapiz, el dueño de este libro."
    l "Te ayudaré a escapar de aquí."

    scene lapiz1
    with dissolve 
    l "Para escapar, debes derrotar a los 3 enemigos que hay dentro del libro."
    l "Respondiendo correctamente a las preguntas que te hagan."

    scene lapiz3
    with dissolve
    l "Si respondes mal, perderás una vida."
    l "Si pierdes las 3 vidas, perderás el juego."
    l "Si eliminas a los 3 villanos, ganarás el juego y podrás volver a la vida real."


    scene presentaciondragon
    with dissolve
    play music "dragon.mp3"
    d "Mi nombre es Dracán Gramático, y soy un poderoso dragón que vuela por los cielos corrigiendo errores gramaticales con mi aliento de fuego y mis afiladas garras."
    d "No soy un dragón cualquiera, soy el más poderoso de todos ni creas que podrás escapar de mí."
    
    scene dragonvsnino
    with dissolve
    d "Para poder vencerme, debes responder correctamente a las preguntas que te haga."
    jump juegoDragon


label juegoDragon:
    play music "illurock.opus"
    if vida_dragon <= 0:
        scene festejodrag        
        with dissolve
        play music "dragonmuerto.mp3"
        n "¡Has vencido a Dracán Gramático y pasas al siguiente nivel"
        scene ganastevsdrag        
        with dissolve
        n "Y lo has convertido en un Ajolote."
        jump presentacionbruja
    elif vida_nino <= 0:
        scene perdistedrag        
        with dissolve
        play music "fuego.mp3"
        n "Fallaste en responder correctamente y te has convertido en polvo. ¡Juego terminado!"
        $ vida_nino = 3
        $ vida_dragon = 3
        $ vida_bruja = 3
        jump start
    else:
        scene dragonvsnino
        with dissolve
        n "Te enfrentas a Dracán Gramático."
        n "Él tiene [vida_dragon] vidas restantes."
        n "Te quedan [vida_nino] vidas."
        
        scene escdrag1
        with dissolve
        d "¿Cuál es la palabra correcta? 'Zanahoria' o 'Zanaoria'?"
        scene ataqueadrag     
        with dissolve
        menu:
            "Zanahoria":
                scene ataqueadrag     
                with dissolve
                play music "success.mp3"
                n "¡Respuesta correcta! Le restas una vida al dragón."
                $ vida_dragon -= 1
                $ puntaje += 10
                jump juegoDragon1
            "Zanaoria":
                scene ataquedragon        
                with dissolve
                play music "disparodefuego.mp3"
                n "Respuesta incorrecta. El dragón te lanza fuego."
                $ vida_nino -= 1
                jump juegoDragon


label juegoDragon1:
    play music "illurock.opus"
    if vida_dragon <= 0:
        scene festejodrag        
        with dissolve
        play music "dragonmuerto.mp3"
        n "¡Has vencido a Dracán Gramático y pasas al siguiente nivel"
        scene ganastevsdrag        
        with dissolve
        n "Y lo has convertido en un ajolote."
        jump presentacionbruja
    elif vida_nino <= 0:
        scene perdistedrag        
        with dissolve
        play music "fuego.mp3"
        n "Fallaste en responder correctamente y te has convertido en polvo. ¡Juego terminado!"
        $ vida_nino = 3
        $ vida_dragon = 3
        $ vida_bruja
        jump start
    else:
        scene dragonvsnino
        with dissolve
        n "Te enfrentas a Dracán Gramático."
        n "Él tiene [vida_dragon] vidas restantes."
        n "Te quedan [vida_nino] vidas."
        
        scene escdrag1
        with dissolve
        d "¿Cuál es la forma correcta de la siguiente oración: 'Ellos __________ a la tienda ayer.'?"
        scene ataqueadrag     
        with dissolve
        menu:
            "Fueron":
                scene ataqueadrag     
                with dissolve
                play music "success.mp3"
                n "¡Respuesta correcta! Le restas una vida al dragón."
                $ vida_dragon -= 1
                $ puntaje += 10
                jump juegoDragon2 
            "Fuimos":
                scene ataquedragon        
                with dissolve
                play music "disparodefuego.mp3"
                n "Respuesta incorrecta. El dragón te lanza fuego."
                $ vida_nino -= 1
                jump juegoDragon1          
            "Fui":
                scene ataquedragon        
                with dissolve
                play music "disparodefuego.mp3"
                n "Respuesta incorrecta. El dragón te lanza fuego."
                $ vida_nino -= 1
                jump juegoDragon1             

label juegoDragon2:
    play music "illurock.opus"
    if vida_dragon <= 0:
        scene festejodrag        
        with dissolve
        play music "dragonmuerto.mp3"
        n "¡Has vencido a Dracán Gramático y pasas al siguiente nivel"
        scene ganastevsdrag        
        with dissolve
        n "Y lo has convertido en un ajolote."
        jump presentacionbruja
    elif vida_nino <= 0:
        scene perdistedrag        
        with dissolve
        play music "fuego.mp3"
        n "Fallaste en responder correctamente y te has convertido en polvo. ¡Juego terminado!"
        $ vida_nino = 3
        $ vida_dragon = 3
        $ vida_bruja
        jump start
    else:
        scene dragonvsnino
        with dissolve
        n "Te enfrentas a Dracán Gramático."
        n "Él tiene [vida_dragon] vidas restantes."
        n "Te quedan [vida_nino] vidas."
        
        scene escdrag1
        with dissolve
        d "¿Cuál de las siguientes oraciones contiene un error en el uso de los tiempos verbales?"
        scene ataqueadrag     
        with dissolve
        menu:
            
            "Ayer, Juan comió pizza para la cena.":
                scene ataquedragon        
                with dissolve
                play music "disparodefuego.mp3"
                n "Respuesta incorrecta. El dragón te lanza fuego."
                $ vida_nino -= 1
                jump juegoDragon2 
            "Ellos estaba jugando al fútbol en el parque.":
                scene ataqueadrag     
                with dissolve
                play music "success.mp3"
                play music "success.mp3"
                n "¡Respuesta correcta! Le restas una vida al dragón."
                $ puntaje += 10
                $ vida_dragon -= 1
                jump juegoDragon2          
            "Esta mañana, nosotros iremos al mercado.":
                scene ataquedragon        
                with dissolve
                play music "disparodefuego.mp3"
                n "Respuesta incorrecta. El dragón te lanza fuego."
                $ vida_nino -= 1
                jump juegoDragon2             
            "María estudiará para su examen mañana.":
                scene ataquedragon        
                with dissolve
                play music "disparodefuego.mp3"
                n "Respuesta incorrecta. El dragón te lanza fuego."
                $ vida_nino -= 1
                jump juegoDragon2             


label presentacionbruja:
    play music "bruja.mp3"
    scene presentacionbruja
    with dissolve
    b "Soy la bruja de la ortografía, y soy la más poderosa de todas."
    b "No podrás escapar de mí, niño."

    scene brujavsnino
    with dissolve
    b "Para poder vencerme, debes responder correctamente a las preguntas que te haga."
    jump juegoBruja
    

label juegoBruja:
    play music "illurock.opus"
    if vida_bruja <= 0:
        scene festejobruj        
        with dissolve
        n "¡Has vencido a la bruja de la ortografía."
        scene ganastevsbruj       
        with dissolve
        play music "cat.mp3"
        n "Y la has convertido en una gata fea."
        jump juegoBruja
    elif vida_nino <= 0:
        $ vida_nino = 3
        $ vida_bruja = 3
        $ vida_dragon = 3
        scene perdistebruj        
        with dissolve
        play music "chihuahua.mp3"
        n "Fallaste en responder correctamente y te has convertido en un chihuahua. ¡Juego terminado!"
        jump start
    else:
        scene bruja1vsnino
        with dissolve
        n "Te enfrentas a la bruja de la ortografía."
        n "Ella tiene [vida_bruja] vidas restantes."
        n "Te quedan [vida_nino] vidas."
        
        scene escbruj
        with dissolve
        "Señala la palabra que está escrita incorrectamente:"
        scene ataqueabruj     
        with dissolve
        menu:
            "Hábito":
                scene ataquebruja       
                with dissolve
                play music "disparobruja.mp3"
                n "Respuesta incorrecta. La bruja te lanza un hechizo."
                $ vida_nino -= 1
                jump juegoBruja
            "Bién":                
                scene ataqueabruja

                with dissolve
                play music "success.mp3"
                n "¡Respuesta correcta! Le restas una vida a la bruja."
                $ vida_bruja -= 1
                $ puntaje += 10
                jump juegoBruja1
            "Después":
                scene ataquebruja        
                with dissolve
                play music "disparobruja.mp3"
                n "Respuesta incorrecta. La bruja te lanza un hechizo."
                $ vida_nino -= 1
                jump juegoBruja

label juegoBruja1:
    play music "illurock.opus"
    if vida_bruja <= 0:
        scene festejobruj        
        with dissolve
        n "¡Has vencido a la bruja de la ortografía."
        scene ganastevsbruj       
        with dissolve
        play music "cat.mp3"
        n "Y la has convertido en una gata fea."
        jump juegoBruja
    elif vida_nino <= 0:
        scene perdistebruj        
        with dissolve
        play music "chihuahua.mp3"
        n "Fallaste en responder correctamente y te has convertido en un chihuahua. ¡Juego terminado!"
        $ vida_nino = 3
        $ vida_bruja = 3
        $ vida_dragon
        jump start
    else:
        scene bruja1vsnino
        with dissolve
        n "Te enfrentas a la bruja de la ortografía."
        n "Ella tiene [vida_bruja] vidas restantes."
        n "Te quedan [vida_nino] vidas."
        
        scene escbruj
        with dissolve
        b "¿Cuál es la ortografía correcta de la palabra que significa 'un animal pequeño que se parece a un ratón y vuela de noche'?"
        scene ataqueabruj     
        with dissolve
        menu:            
            "Murciégalo":
                scene ataquebruja        
                with dissolve
                play music "disparobruja.mp3"
                n "Respuesta incorrecta. La bruja te lanza un hechizo."
                $ vida_nino -= 1
                jump juegoBruja1          
            "Murcielgalo":
                scene ataquebruja        
                with dissolve
                play music "disparobruja.mp3"
                n "Respuesta incorrecta. La bruja te lanza un hechizo."
                $ vida_nino -= 1
                jump juegoBruja1
            "Murciélago":
                scene ataqueabruja

                with dissolve
                play music "success.mp3"
                n "¡Respuesta correcta! Le restas una vida a la bruja."
                $ vida_bruja -= 1
                $ puntaje += 10
                jump juegoBruja2              

label juegoBruja2:
    play music "illurock.opus"
    if vida_bruja <= 0:
        scene festejobruj        
        with dissolve
        n "¡Has vencido a la bruja de la ortografía."
        scene ganastevsbruj       
        with dissolve
        play music "cat.mp3"
        n "Y la has convertido en una gata fea."
        jump hasGanado
    elif vida_nino <= 0:
        scene perdistebruj        
        with dissolve
        play music "chihuahua.mp3"
        n "Fallaste en responder correctamente y te has convertido en un chihuahua. ¡Juego terminado!"
        $ vida_nino = 3
        $ vida_bruja = 3
        $ vida_dragon
        jump start
    else:
        scene bruja1vsnino
        with dissolve
        n "Te enfrentas a la bruja de la ortografía."
        n "Ella tiene [vida_bruja] vidas restantes."
        n "Te quedan [vida_nino] vidas."
        
        scene escbruj
        with dissolve
        b "¿Cómo se llama el gentilicio de una persona que nació en la ciudad de Roma, Italia?"
        scene ataqueabruj     
        with dissolve
        menu:
            
            "Románico":
                scene ataquebruja        
                with dissolve
                play music "disparobruja.mp3"
                n "Respuesta incorrecta. La bruja te lanza un hechizo."
                $ vida_nino -= 1
                jump juegoBruja2 
            "Romano":
                scene ataqueabruja
                with dissolve
                play music "success.mp3"
                n "¡Respuesta correcta! Le restas una vida a la bruja."
                $ puntaje += 10
                $ vida_bruja -= 1
                jump juegoBruja2          
            "Romés":
                scene ataquebruja        
                with dissolve
                play music "disparobruja.mp3"
                n "Respuesta incorrecta. La bruja te lanza un hechizo."
                $ vida_nino -= 1
                jump juegoBruja2


label hasGanado:
    scene hasganado
    with dissolve
    n "¡Has ganado el juego!"
    n "Tu puntaje es de [puntaje] puntos."
    "¡Felicidades!"
    return
