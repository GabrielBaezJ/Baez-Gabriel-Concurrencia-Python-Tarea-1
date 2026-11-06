import asyncio
import time

async def tarea(nombre, duracion):
    print(f"Iniciando: {nombre}")
    await asyncio.sleep(duracion)
    print(f"Terminado: {nombre} ({duracion} segundos)")

async def main():
    inicio = time.perf_counter()

    await asyncio.gather(
        tarea("Hervir agua para café", 3),
        tarea("Tostar pan", 2),
        tarea("Freír huevos", 3),
    )

    fin = time.perf_counter()
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
asyncio.run(main())