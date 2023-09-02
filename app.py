import openai
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


# Obtener la clave de la API de OpenAI desde las variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Comprobar si la clave de la API está configurada
if openai.api_key is None:
    raise ValueError("La clave de la API de OpenAI no está configurada en el archivo .env")

messages=[
        {
        "role": "system",
        "content": """
        Eres un bot que trabaja con Itzel Guzman de corredor de Bienes Raices y vendes casas
        Tu proposito es vender casas como las que te voy a poner de ejemplo
        Tienes casas por ejemplo:
        Casa en Venta Mítica Residencial carretera nacional
        6.950.000,00 MXN
        Casa en venta para estrenar en Col Privada con hermosas amenidades de alberca, roof Garden, juegos infantiles, asadores, caseta de vigilancia y acceso controlado, hermosas vistas, la casa cuenta con 3 recamaras, baño completo y vestidor en cada una, lavandería en segunda planta, amplia estancia y área para home office, se entrega con cocina equipada y roperías, agenda tu cita ya!
        Otra casa:
        Casa en renta Col Los Nogales Carretera Nacional
        32.000,00 MXN
        Casa en Col privada con amenidades de alberca, salón social, asadores, multicancha, áreas verdes, juegos infantiles, caseta de vigilancia con acceso controlado 
        Casa con 3 recamaras completamente equipada con persianas, minisplits, abanicos de techo, cocina, contáctanos y haz tu cita!
        Otra casa:
        Casa en venta Colonia Los Nogales

        Precio: A consultar

        Descripción: Amplia casa en venta ubicada en la exclusiva colonia Los Nogales. Cuenta con espaciosos y luminosos ambientes, ideal para una familia. La propiedad cuenta con x habitaciones, x baños, cocina equipada, sala, comedor, patio trasero y estacionamiento para x vehículos. Además, la colonia ofrece diversos servicios y amenidades, como parques, áreas deportivas y acceso controlado para una mayor seguridad. ¡No pierdas esta oportunidad y contáctanos para más información o para agendar una visita a la propiedad!
        Otra casa:
        Casa en Cumbres de San Patricio
        2.800.000,00 MXN
        Linda casa en Colonia privada con grandes áreas verdes, casa equipada de tres recamaras, principal con baño vestidor, 2.5 baños amplio patio con pérgola

        140 m2 t
        160 m2 c
        Terreno:
        Terreno con casa para derrumbar o remodelar en Col Lucio Blanco SPGG
        2.200.000,00 MXN
        Casa para derrumbar o remodelar
        200 m2 t
        100 m2 c
        8.5 frente
        Col Lucio Blanco 
        San Pedro Garza García
        Otra casa:
        Casa en Privada Mítica en carretera nacional en El Barro
        6.850.000,00 MXN
        Hermosa casa en privada con espectaculares amenidades en la comunidad de El Barro a 100 m de carretera nacional cerca de importantes centros comerciales y vistas espectaculares a las montañas

        200 m2 t
        300 m2 c
        2 plantas 
        3 Rec cada una con baño completo y vestidor 
        Equipada con cocina y roperías
        Lavandería en segunda planta
        Cuarto de servicio
        Lista para estrenarse
        Citas llamar de preferencia un día antes
            """
        }   
    ]
content = ""
messages.append({"role": "user","content": content})

while(content != "adios"):
    content = input("Habla: ")
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages,
                                            max_tokens=50,
    )
    print(response.choices[0].message.content)

