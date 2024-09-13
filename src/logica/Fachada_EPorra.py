from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.models import Carrera, session,Competidor,Session



class Fachada_EPorra():
    def __init__(self):
        #Este constructor contiene los datos falsos para probar la interfaz
        
        self.carreras = self.obtener_carreras()
        self.actual=0
        
        

    

    def obtener_carreras(self):
        carreras = session.query(Carrera).all()
        
        return carreras

    def dar_carreras(self):
    
        if not self.carreras:
         return []  # Retorna una lista vacía si no hay carreras
        return self.carreras  # Retorna todas las carreras almacenadas
        
        

    def dar_carrera(self, id_carrera):
        ''' Retorna una carrera a partir de su identificador
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
        Retorna:
            (dict): La carrera identificada con el id_carrera recibido como parámetro
        '''
        raise NotImplementedError("Método no implementado")
        
    def actualizar_lista_carreras(self):
        """ Actualiza la lista de carreras """
        self.carreras = self.obtener_carreras()

    def crear_carrera(self, nombre_carrera, competidores):
        with Session() as session:
            # Validar el nombre de la carrera
            if not nombre_carrera or nombre_carrera.strip() == "":
                return False, "El nombre de la carrera no puede estar vacío."

            # Verificar si la carrera ya existe
            carrera_existente = session.query(Carrera).filter_by(nombre=nombre_carrera).first()
            
            if carrera_existente:
                carrera = carrera_existente
            else:
                carrera = Carrera(nombre=nombre_carrera)
                session.add(carrera)
                session.commit()
            
            # Procesar competidores
            for competidor_data in competidores:
                if 'Nombre' not in competidor_data or 'Probabilidad' not in competidor_data:
                    return False, "Cada competidor debe tener un nombre y una probabilidad."

                if competidor_data['Nombre'].strip() == "":
                    return False, "Cada competidor debe tener un nombre."

                if competidor_data['Probabilidad'] <= 0:
                    return False, "La probabilidad debe ser mayor que 0."

                if competidor_data.get('Estado') == 'Nueva':
                    nuevo_competidor = Competidor(
                        nombre=competidor_data['Nombre'],
                        probabilidad=competidor_data['Probabilidad'],
                        carrera=carrera
                    )
                    session.add(nuevo_competidor)
                else:
                    competidor_existente = session.query(Competidor).filter_by(nombre=competidor_data['Nombre'], carrera=carrera).first()
                    if competidor_existente:
                        competidor_existente.probabilidad = competidor_data['Probabilidad']
            
            session.commit()
            self.actualizar_lista_carreras()
        return True, "Carrera y competidores guardados con éxito."
        
        
    def terminar_carrera(self, id, ganador):
        ''' Termina una carrera asignando un ganador y dejando su variable de terminada en verdadero
        Parámetros:
            id (int): La posición de la carrera en la lista de carreras
            ganador (int): El ganador de la carrera
        '''
        raise NotImplementedError("Método no implementado")

    def eliminar_carrera(self, id):
        ''' Elimina una carrera
        Parámetros:
            id (int): La posición de la carrera en la lista de carreras
        '''
        raise NotImplementedError("Método no implementado")

    def dar_apostadores(self):
        ''' Retorna una lista de apostadores
        Parámetros:
            Ninguno
        Retorna:
            (list): La lista de apostadores en EPorra
        '''
        raise NotImplementedError("Método no implementado")

    def aniadir_apostador(self, nombre):
        ''' Adiciona un apostador
        Parámetros:
            nombre (string): El nombre del apostador a adicionar
        '''
        raise NotImplementedError("Método no implementado")
    
    def editar_apostador(self, id, nombre):
        ''' Edita un apostador cambiando su nombre
        Parámetros:
            id (int): La posición del apostador en la lista de apostadores
            nombre (string): El nombre del apostador a actualizar
        '''
        raise NotImplementedError("Método no implementado")
    
    def validar_crear_editar_apostador(self, nombre):
        ''' Valida los datos de un apostador antes de guardarlos
        Parámetros:
            nombre (string): El nombre del apostador a crear o editar
        Retorna:
            (string): Una cadena con los mensajes de error en la validación o vacío si no hay errores
        '''
        raise NotImplementedError("Método no implementado")
    
    def eliminar_apostador(self, id):
        ''' Elimina un apostador de la lista
        Parámetros:
            id (int): La posición del apostador en la lista de apostadores
        '''
        raise NotImplementedError("Método no implementado")

    def dar_competidores_carrera(self, id):
        ''' Retorna la lista de competidores de una carrera
        Parámetros:
            id (int): La posición de la carrera en la lista de carreras
        Retorna:
            (list): La lista de competidores de una carrera
        '''
        raise NotImplementedError("Método no implementado")

    def dar_competidor(self, id_carrera, id_competidor):
        ''' Retorna un competidor en una carrera
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
            id_competidor (int): La posición del competidor en la lista de competidores de la carrera
        Retorna:
            (list): La lista de competidores d euna carrera
        '''
        raise NotImplementedError("Método no implementado")

    def aniadir_competidor(self, id, nombre, probabilidad):
        ''' Adiciona un competidor a una carrera
        Parámetros:
            id (int): La posición de la carrera en la lista de carreras
            nombre (string): El nombre del competidor a adicionar
            probabilidad (float): La probabilidad asignada al competidor
        '''
        raise NotImplementedError("Método no implementado")

    def editar_competidor(self, id_carrera, id_competidor, nombre, probabilidad):
        ''' Edita un competidor en una carrera
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
            id_competidor (int): La posición del competidor dentro de la lista de competidores en una carrera
            nombre (string): El nombre del competidor a editar
            probabilidad (float): La probabilidad asignada al competidor
        '''
        raise NotImplementedError("Método no implementado")
    
    def eliminar_competidor(self, id_carrera, id_competidor):
        ''' Elimina un competidor de una carrera
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
            id_competidor (int): La posición del competidor dentro de la lista de competidores en una carrera
        '''
        raise NotImplementedError("Método no implementado")

    def dar_apuestas_carrera(self, id_carrera):
        ''' Retorna la lista de apuestas de una carrera
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
        Retorna:
            (list): La lista de apuestas para una carrera
        '''
        raise NotImplementedError("Método no implementado")

    def dar_apuesta(self, id_carrera, id_apuesta):
        ''' Retorna una apuesta a partir de la carrera y su posición en la lista de apuestas
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
            id_apuesta (int): La posición de la apuesta en la lista de apuestas en la carrera
        Retorna:
            (dict): La apuesta de la carrera
        '''
        raise NotImplementedError("Método no implementado")

    def crear_apuesta(self, apostador, id_carrera, valor, competidor):
        ''' Crea una apuesta a partir de los datos enviados por parámetro
        Parámetros:
            apostador (string): El nombre del apostador
            id_carrera (int): La posición de la carrera en la lista de carreras
            valor (float): El valor de la apuesta
            competidor (string): El nombre del competidor sobre el que se apuesta
        '''
        raise NotImplementedError("Método no implementado")

    def editar_apuesta(self, id_apuesta, apostador, carrera, valor, competidor):
        ''' Actualiza los datos de una apuesta según los datos enviados por parámetro
        Parámetros:
            id_apuesta (int): La posición de la apuesta en la lista de apuestas de la carrera
            apostador (string): El nombre del apostador
            id_carrera (int): La posición de la carrera en la lista de carreras
            valor (float): El valor de la apuesta
            competidor (string): El nombre del competidor sobre el que se apuesta
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_apuesta(self, apostador, carrera, valor, competidor):
        ''' Valida que los datos de una apuesta sean los correctos
        Parámetros:
            apostador (string): El nombre del apostador
            carrera (int): La posición de la carrera en la lista de carreras
            valor (float): El valor de la apuesta
            competidor (string): El nombre del competidor sobre el que se apuesta
        Retorna:
            (string): Una cadena con los mensajes de error en la validación o vacío si no hay errores
        '''
        raise NotImplementedError("Método no implementado")

    def eliminar_apuesta(self, id_carrera, id_apuesta):
        ''' Elimina una apuesta de una carrera
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
            id_apuesta (int): La posición de la apuesta en la lista de apuestas
        '''
        raise NotImplementedError("Método no implementado")

    def dar_reporte_ganancias(self, id_carrera, id_competidor):
        ''' Genera la información para el reporte de ganancias
        Parámetros:
            id_carrera (int): La posición de la carrera en la lista de carreras
            id_competidor (int): La posición del competidor en la lista de competidores de la carrera
        Retorna:
            (list, float): Una lista con los valores que ganan los apostadores y el valor de las ganancias de la casa
        '''
        raise NotImplementedError("Método no implementado")
