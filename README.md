# Auditoría de calidad de un equipo ágil

Cristian David Cotrino Vasquez

Juan Gabriel Gutierrez 

Juan Carlos Suarez Merchan 

Johan Garcia

Proyecto académico para aplicar prácticas de calidad de software a un equipo ágil que desarrolla una aplicación de citas médicas.

## Objetivo

Definir y demostrar un plan de calidad basado en ISO/IEC 25010, Scrum/Kanban, XP, DevOps y métricas DORA.

## Caso de estudio

La startup entrega una nueva versión de la aplicación cada dos semanas. Se han presentado defectos que llegan a producción, las pruebas son principalmente manuales y los despliegues se realizan los viernes.

## Estructura

- `src/citas.py`: función de validación de citas.
- `tests/test_citas.py`: pruebas unitarias con pytest.
- `.github/workflows/quality.yml`: integración continua y puerta de calidad.
- `docs/iso-25010.md`: diagnóstico de atributos de calidad.
- `docs/definition-of-done.md`: Definition of Done y políticas Kanban.
- `docs/dora.md`: métricas DORA y fórmulas.

## Ejecución local

```bash
pip install -r requirements.txt
pytest
```

## XP — Estándares de código

1. Usar nombres descriptivos para funciones, variables y pruebas.
2. Mantener una indentación de 4 espacios y seguir convenciones de estilo consistentes.
3. Aplicar responsabilidad única: cada función debe realizar una tarea concreta.
4. Evitar duplicación de código y reutilizar lógica cuando corresponda.
5. Escribir comentarios solamente cuando aporten contexto útil que no sea evidente en el código.

## Puerta de calidad

Cada push a `main` y cada Pull Request hacia `main` ejecuta las pruebas automáticamente mediante GitHub Actions. Si una prueba falla, el workflow falla.

## Definition of Done

1. Cumplimiento de estándares de código.
2. Pruebas unitarias automatizadas.
3. Todas las pruebas pasan.
4. Revisión de código por otro integrante.
5. Criterios de aceptación verificados.
6. Documentación actualizada y entregable listo.

Link de Trello: https://trello.com/b/1rh9kNbx/auditoria-de-calidad-app-de-citas-medicas


## Flujo Kanban

BACKLOG → TODO → IN PROGRESS → CODE REVIEW → TESTING → DONE

Límites WIP:
- IN PROGRESS: máximo 2 tarjetas.
- CODE REVIEW: máximo 2 tarjetas.
- TESTING: máximo 2 tarjetas.

## Equipo

Proyecto académico — Universidad Manuela Beltrán (UMB).
