# Ejecución Concurrente en Python

Script en Python que simula la preparación de un desayuno. Las tareas se ejecutan **de forma concurrente** con `asyncio`: las tres se inician casi al mismo tiempo y mientras una espera, las otras avanzan.

## Tareas del ejemplo

| Tarea                    | Duración |
|--------------------------|----------|
| Hervir agua para el café | 3 s      |
| Tostar el pan            | 2 s      |
| Freír los huevos         | 3 s      |

Tiempo total esperado: **~3 segundos** (la duración de la tarea más larga), frente a los ~8 s de la versión secuencial.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado y en ejecución
- Docker Compose (incluido en Docker Desktop)

Para verificar la instalación:

docker --version
docker compose version

## Cómo ejecutar el script

### 1. Clonar el repositorio

git clone https://github.com/GabrielBaezJ/Baez-Gabriel-Concurrencia-Python-Tarea-1.git

### 2. Ejecutar con Docker Compose

docker compose run --rm python-app python 01_concurrente.py

## Salida esperada

Iniciando: Hervir agua para el café...
Iniciando: Tostar el pan...
Iniciando: Freír los huevos...
Terminado: Tostar el pan (2 s).
Terminado: Hervir agua para el café (3 s).
Terminado: Freír los huevos (3 s).
Tiempo total del desayuno: 3.00 segundos.