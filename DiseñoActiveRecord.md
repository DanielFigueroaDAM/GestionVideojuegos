1. ¿Por qué el objeto (la clase Juego) tiene las llamadas a la base de datos?

Esto sigue el patrón de diseño Active Record. Cada objeto Juego es responsable de su propia persistencia: sabe cómo guardarse a sí mismo, actualizarse o eliminarse en la base de datos. Además, los métodos de clase (get_all, get_by_id) actúan como consultas que devuelven colecciones de objetos.

Ventajas en un proyecto pequeño como este:

    Simplicidad: No necesitas una capa separada de acceso a datos (repositorio, DAO). Todo está en un mismo lugar.

    Intuitivo: Si tienes un juego, puedes hacer juego.save() para guardarlo. Si quieres todos los juegos, usas Juego.get_all().

    Cumple con el requisito de usar conexionBD.py: Las llamadas a BD se hacen a través de ese módulo, pero la lógica de negocio (qué consultas hacer) reside en el modelo.

Para un trabajo de clase con una sola tabla y pocas operaciones, es más que suficiente.
2. ¿Por qué algunos métodos son @classmethod?

@classmethod define un método de clase, que se llama sobre la clase directamente, no sobre una instancia. El primer parámetro es cls (la clase), no self (la instancia).

Se usan aquí para:

    Obtener todos los juegos: Juego.get_all() – no necesitas un juego existente para pedir la lista completa.

    Buscar por ID: Juego.get_by_id(5) – igualmente, es una operación de consulta que devuelve una instancia concreta.

    Dentro de estos métodos, se usa cls(...) para crear nuevas instancias de la clase (los objetos Juego que devuelven).

En resumen: los métodos de clase agrupan funcionalidades que pertenecen a la "colección" de juegos, no a un juego individual. Es una forma clara y común en Python de implementar este tipo de operaciones.