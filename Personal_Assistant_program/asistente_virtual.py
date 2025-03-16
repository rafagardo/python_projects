import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar nuestro microfono y devolver el audio como texto
def transformar_voz_texto():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Escuchando...")
        audio = r.listen(source)
    try:
        print("Reconociendo...")
        query = r.recognize_google(audio, language='es-ES')
        print(f"Tu dijiste: {query}")
        return query
    except sr.UnknownValueError:
        print("Repita por favor...")
        return "None"
    except sr.RequestError:
        print("No se puede obtener la información solicitada, intente de nuevo...")
        return "None"
    except:
        return "None"

# Funcion pare que el asistente hable
def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def pedir_dia():
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    print(dia_semana)

    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miercoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }

    dia_semana = calendario[dia_semana]
    hablar(f"Hoy es {dia_semana}")

def pedir_hora():
    hora = datetime.datetime.now()
    hablar(f"Son las {hora.hour} horas y {hora.minute} minutos")

def saludo_inicial():
    hora = datetime.datetime.now()
    if 6 <= hora.hour < 12:
        momento = 'Buenos dias'
    elif 12 <= hora.hour < 18:
        momento = 'Buenas tardes'
    elif 18 <= hora.hour < 23:
        momento = 'Buenas noches'
    else:
        hablar('Es muy tarde, deberias ir a dormir')
    hablar(f'{momento}, soy tu asistente virtual, en que puedo ayudarte?')

def centro_de_pedidos():
    saludo_inicial()
    comenzar = True
    while comenzar:
        transcripcion = transformar_voz_texto().lower()
        if 'abrir youtube' in transcripcion:
            hablar('Claro que si')
            webbrowser.open('https://www.youtube.com/')
            hablar('Abriendo youtube...')
            continue
        elif 'abrir navegador' in transcripcion:
            hablar('Claro que si')
            webbrowser.open('https://www.google.com/')
            hablar('Abriendo navegador...')
            continue
        elif 'qué día es hoy' in transcripcion:
            pedir_dia()
            continue
        elif 'qué hora es' in transcripcion:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in transcripcion:
            hablar('Buscando eso en wikipedia')
            transcripcion = transcripcion.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(transcripcion, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in transcripcion:
            hablar('Ya mismo estoy en eso')
            transcripcion = transcripcion.replace('busca en internet', '')
            pywhatkit.search(transcripcion)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in transcripcion:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(transcripcion)
            continue
        elif 'chiste' in transcripcion:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in transcripcion:
            accion = transcripcion.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in transcripcion:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break

centro_de_pedidos()


