# Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. 
#   Se podría ejecutar varias veces al mismo tiempo.

# Using threading module
from time import sleep
from threading import Thread

def async_sum(n1, n2, seconds):
    sleep(seconds)
    print(n1 + n2)

def execute_function(f, args):
    new_thread = Thread(target=f, args=args)
    new_thread.start()

execute_function(async_sum, (3, 3, 5))
execute_function(async_sum, (2, 2, 2))

# Using asyncio module
import asyncio

async def async_sum(n1, n2, seconds):
    await asyncio.sleep(seconds)
    print(n1 + n2)

async def execute_function():
    await asyncio.gather(
        async_sum(3, 3, 5), 
        async_sum(2, 2, 2)
    )

asyncio.run(execute_function())