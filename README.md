Cristian Steven Calle Cuzco  

Este proyecto es un ejemplo práctico del ciclo **CI/CD** utilizando GitHub Actions.  
Incluye:  
- Pruebas unitarias  
- Construcción automática de un paquete  
- Generación de artefactos  
- Automatización completa desde cada push o pull request  

---

 ¿Qué es CI/CD?

 CI – Integración Continua  
Cada vez que se sube código al repositorio:  
1. El sistema descarga el proyecto  
2. Instala dependencias  
3. Ejecuta pruebas  
4. Verifica que todo funcione  

 CD – Entrega Continua  
Después de CI, se genera un paquete listo para distribución, sin intervención manual

---

Estructura del proyecto

proyecto/
├── app/
│ ├── init.py
│ └── calculo.py
├── tests/
│ └── test_calculo.py
├── setup.py
├── README.md
└── .github/workflows/ci.yml



Pruebas (Unit Testing)

Código principal: `app/calculo.py`

```python
def suma(a, b):
    return a + b