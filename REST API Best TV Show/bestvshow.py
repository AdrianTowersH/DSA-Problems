import requests

def bestInGenre(genre):
    # Dirección base de la API de HackerRank
    url = "https://hackerrank.com"
    
    # Inicializamos el contador de páginas para la paginación de la API
    page = 1
    
    # Variables de seguimiento para registrar los datos del mejor programa encontrado
    best_name = None
    best_rating = -1.0  # Empezamos en -1.0 para que cualquier calificación real (0.0 a 10.0) la supere
    
    # Bucle principal: se repetirá para ir descargando página por página
    while True:
        # Hacemos la petición HTTP GET a la API y convertimos la respuesta de JSON a un diccionario de Python
        response = requests.get(f"{url}?page={page}").json()
        
        # Extraemos la lista de programas de la propiedad 'data'. Si no existe, usamos una lista vacía []
        data = response.get('data', [])
        
        # Bucle secundario: procesamos cada programa/show de la página actual
        for show in data:
            
            # --- 1. LIMPIEZA Y VERIFICACIÓN DEL GÉNERO ---
            # Separamos el string de géneros por comas y limpiamos los espacios en blanco de cada uno (ej: " Drama " -> "Drama")
            genres = [g.strip() for g in show.get('genre', '').split(',')]
            
            # Verificamos si el género que buscamos está en la lista de este programa
            if genre in genres:
                
                # --- 2. EXTRACCIÓN DE VALORES ---
                # Obtenemos la calificación de IMDb (la convertimos a float) y el nombre del programa
                rating = float(show.get('imdb_rating', 0))
                name = show.get('name', '')
                
                # --- 3. COMPARACIÓN DE CALIFICACIONES Y DESEMPATES ---
                # Caso A: Si encontramos una calificación estrictamente mayor, actualizamos al nuevo líder
                if rating > best_rating:
                    best_rating = rating
                    best_name = name
                    
                # Caso B: Si hay un empate en la calificación, desempatamos por orden alfabético
                elif rating == best_rating:
                    # Si es el primer programa que evaluamos o si su nombre va antes en el abecedario, actualizamos
                    if best_name is None or name < best_name:
                        best_name = name
        
        # --- 4. CONTROL DE PAGINACIÓN ---
        # Obtenemos el total de páginas que la API contiene para esta consulta
        total_pages = response.get('total_pages', 0)
        
        # Si ya revisamos la última página (o si vamos más allá), rompemos el bucle infinito
        if page >= total_pages:
            break
            
        # Si aún quedan páginas, incrementamos el contador para pedir la siguiente en la próxima vuelta
        page += 1
        
    # Una vez revisadas todas las páginas de la API, devolvemos el nombre del ganador absoluto
    return best_name