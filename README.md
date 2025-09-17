# InventarioSub

InventarioSub es un sistema backend para **gestión de inventario** de productos y materias primas.  
Está diseñado para controlar stocks, movimientos entre sedes, control de almacenes y gestión de proveedores,.  

El proyecto está desarrollado con **FastAPI** y **PostgreSQL**, utilizando **SQLAlchemy** para ORM y **Pydantic** para validación de datos.

---

## Características principales

- Gestión de **sedes**.
- Gestión de **usuarios** (administradores por sede y globales).
- Gestión de **proveedores** y **productos**.
- Tests automatizados con **pytest**.
- Preparado para **entornos de desarrollo y CI/CD**.

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/InventarioSub.git
cd InventarioSub
```

2. Crea un entorno virtual e instálalo:

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Configura variables de entorno en .env:

```env
DB_URL=postgresql+psycopg2://usuario:password@localhost:5432/inventariosub
```

## Ejecución

```bash
uvicorn main:app --reload
```

# Test

```bash
pytest -v
```