# Restaurante - Página Web 🍽️

¡Bienvenidos a la página web oficial de [Nombre del Restaurante]! Esta es una **versión beta** del sitio, desarrollada principalmente con **Django**, **CSS** personalizado desde cero y funcionalidades interactivas utilizando **JavaScript**. El diseño incluye animaciones en CSS que mejoran la experiencia del usuario.

## 🚀 Características

- **Desarrollo con Django**: Backend desarrollado usando el framework de Django para ofrecer una experiencia rápida y segura.
- **CSS personalizado**: Todo el estilo está hecho desde cero, sin utilizar frameworks de CSS como Bootstrap o Foundation.
- **JavaScript dinámico**: Funcionalidades interactivas, como formularios y elementos dinámicos, implementadas usando JavaScript.
- **Animaciones con CSS**: Efectos y transiciones que mejoran la interfaz y la navegación del sitio.
- **Implementación de Cookies**: Próximamente se implementarán las cookies para gestionar preferencias y datos del usuario mediante **Google Analytics** y otras herramientas de seguimiento.

## ⚠️ Estado del Proyecto

Actualmente el proyecto se encuentra en **fase beta**. Aunque gran parte de las funcionalidades principales están implementadas, aún faltan algunos ajustes y mejoras:

- **Refactorización**: El código necesita ser refactorizado para mejorar la legibilidad y rendimiento. Algunas partes del proyecto tienen código que podría simplificarse.
- **Limpieza de código**: Hay fragmentos de código redundante que deben eliminarse o reorganizarse.
- **Implementación de tests**: Los tests unitarios no están completos. Buscamos colaboradores interesados en ayudar con la parte de **testing** para asegurar la calidad del código y la funcionalidad del sitio.

## 🛠️ Instalación y Ejecución

### Requisitos

- Python 3.x
- Django 4.x
- Las bibliotecas de requirements.txt

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/nombre-del-repositorio.git
   cd nombre-del-repositorio

    Instala las dependencias de Python:

    bash

pip install -r requirements.txt

Ejecuta las migraciones de la base de datos:

bash

python manage.py migrate

Inicia el servidor de desarrollo de Django:

bash

    python manage.py runserver

    Abre el navegador y accede a http://localhost:8000 para ver el sitio web en funcionamiento.

### Consideraciones y colaboración

📋 Tests

Los tests no están completos y se aceptan colaboraciones en esta área. Si te interesa contribuir, por favor revisa los archivos bajo la carpeta tests/ y ayuda a mejorar la cobertura de código.

Puedes ejecutar los tests actuales con el siguiente comando:

bash

python manage.py test

🏗️ Refactorización Pendiente

Además de los tests, se necesita trabajar en la refactorización del código. Algunas áreas que requieren atención incluyen:

    Modularización del CSS: El código CSS podría beneficiarse de una mejor organización mediante la separación en diferentes archivos o bloques de estilo.
    Mejora del código JavaScript: Algunas funciones en JavaScript pueden optimizarse o reescribirse para mejorar la eficiencia.
    Simplificación de vistas de Django: Refactorización de algunas vistas para hacerlas más reutilizables y menos redundantes.

🎨 Mejoras Futuras

    Integración de Cookies: Próximamente se implementarán cookies con el soporte de Google Analytics para gestionar las preferencias del usuario y proporcionar información valiosa sobre el tráfico del sitio.
    SEO y accesibilidad: Mejorar la optimización para motores de búsqueda y asegurar que el sitio sea accesible para todos los usuarios.
    Responsive Design: Aunque el sitio es funcional en dispositivos móviles, se pueden mejorar algunos aspectos del diseño responsivo.

🤝 Contribuir

Si deseas contribuir a este proyecto, ¡eres más que bienvenido! Aquí algunos pasos para comenzar:

    Haz un fork de este repositorio.
    Crea una nueva rama (git checkout -b feature/mi-nueva-funcionalidad).
    Haz tus cambios y commitea (git commit -m 'Agrega mi nueva funcionalidad').
    Sube tu rama (git push origin feature/mi-nueva-funcionalidad).
    Abre un Pull Request y explica tus cambios detalladamente.

Por favor, asegúrate de seguir las guías de estilo y que tu código esté bien comentado antes de enviarlo.
📝 Licencia

Este proyecto está licenciado bajo la licencia GPLV3. Si deseas utilizar el código para tu propio proyecto, siéntete libre de hacerlo.

¡Gracias por visitar y contribuir al desarrollo de la página web de nuestro restaurante! 🍕🍲🍷