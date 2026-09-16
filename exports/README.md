# Paquete portable para otra cuenta

- [Descargar `hoplite-kit-portable.zip`](hoplite-kit-portable.zip).
- [Checksum SHA-256](hoplite-kit-portable.zip.sha256).
- [Guía completa](../LEEME-PRIMERO.md) y [prompt para el hilo de destino](../PROMPT-PARA-HOPLITE.txt).
- [Verificación de esta entrega y límites observados](VERIFICACION.md).

El ZIP es un entregable pequeño generado desde una lista explícita de fuentes revisadas, no una copia del sandbox. Incluye las 27 skills, los 4 MCP y todo lo necesario para reconstruir las dependencias y repetir las pruebas. No contiene autenticación, historial, los adjuntos originales ni dependencias instaladas.

```sh
python3 scripts/exportar_kit.py build
python3 scripts/exportar_kit.py check
```

La lista de fuentes y la configuración MCP se validan antes de exportar. La construcción fija el orden, las fechas y los permisos del ZIP; su manifiesto registra SHA-256 y tamaño por archivo. Los cambios legítimos de contenido requieren reconstruir y revisar el ZIP y su checksum juntos. Una verificación de integridad no sustituye las pruebas funcionales ni la autorización de la cuenta de destino.

El README dentro del ZIP es la guía de transferencia, no el README histórico del repositorio. El ZIP no incluye otra copia de sí mismo. Conserva las carpetas ocultas al extraerlo.
