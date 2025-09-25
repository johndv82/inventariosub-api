import uuid
from locust import HttpUser, task, between
import random

class InventarioUser(HttpUser):
    # Tiempo de espera entre cada request por usuario locust
    wait_time = between(1, 3)

    def on_start(self):
        # Precarga de producto y sede
        proveedor = {
            "ruc": str(uuid.uuid4().int)[:11] ,
            "razon_social": "Proveedor Locust",
            "contacto": "Carga",
            "telefono_contacto": "999999999",
            "estado": "ACTIVO",
            "usuario_creacion": "locust"
        }
        self.client.post("/proveedores/", json=proveedor)

        producto = {
            "codigo": f"LOCUST-PROD-{uuid.uuid4().hex[:18]}",
            "descripcion": "Producto Locust",
            "unidad_medida": "LT",
            "peso_en_kilos": 1,
            "proveedor_ruc": proveedor["ruc"],
            "estado": "ACTIVO",
            "usuario_creacion": "locust"
        }
        prod_resp = self.client.post("/productos/", json=producto)
        self.producto_id = prod_resp.json().get("id")

        sede = {
            "nombre": f"Sede Locust {uuid.uuid4().hex[:6]}",
            "direccion": "Av. Carga 123"
        }
        sede_resp = self.client.post("/sedes/", json=sede)
        self.sede_id = sede_resp.json().get("id")

    @task(3)
    def crear_movimiento_ingreso(self):
        data = {
            "producto_id": self.producto_id,
            "sede_id": self.sede_id,
            "tipo_movimiento": "INGRESO",
            "cantidad": 10,
            "estado_producto": "DISPONIBLE",
            "usuario_creacion": "locust",
            "observaciones": "Carga masiva test"
        }
        self.client.post("/inventario/", json=data)

    @task(2)
    def obtener_movimiento(self):
        inventario_id = random.randint(1, 500)

        with self.client.get(f"/inventario/{inventario_id}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 404:
                response.success()  # Error controlado: inventario inexistente
            else:
                response.failure(f"Respuesta inesperada: {response.status_code} - {response.text}")