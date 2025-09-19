from locust import HttpUser, task, between
import random

class EvaluacionesUser(HttpUser):
    wait_time = between(1,3) #Cada usuario del test de carga esperará entre 1 y 3 segundos.

    @task
    def crear_sede(self):
        num_random = random.randint(0,20)
        self.client.post("/sedes/", json={
            "nombre": "Sede Central N"+str(num_random), "direccion": "Av. Principal 222"
        })

    # @task
    # def listar_sedes(self):
    #     self.client.get("/sedes")