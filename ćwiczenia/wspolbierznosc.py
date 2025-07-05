# import threading
# import time
# # Function to simulate a time-consuming task
# def print_numbers():
#     for i in range(1, 6):
#         print(f"Printing number {i}")
#         time.sleep(1)  # Simulate a delay of 1 second
# # Function to simulate another task
# def print_letters():
#     for letter in 'Geeks':
#         print(f"Printing letter {letter}")
#         time.sleep(1)  # Simulate a delay of 1 second
# # Create two thread objects, one for each function
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# # Start the threads
# thread1.start()
# thread2.start()
#
# # The main thread waits for both threads to finish
# thread1.join()
# thread2.join()
#
# print("Both threads have finished.")

# import multiprocessing
# def square(x):
#     return x*x
#
# if __name__ == "__main__":
#     numbers = [1,2,3,4,5]
#
#     with multiprocessing.Pool(processes=4) as pool:
#         result = pool.map(square, numbers)
#     print(result)

import asyncio
import aiohttp
import time

async def pobierz_strone(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    strony = [
        "https://www.geeksforgeeks.org/",
        "https://www.amazon.pl/",
        "https://zoo.wroclaw.pl/",
        "https://www.youtube.com/",
    ]

    async with aiohttp.ClientSession() as session:
        zadania = [pobierz_strone(session, url) for url in strony]

        wyniki = await asyncio.gather(*zadania)
        for i, wynik in enumerate(wyniki, 1):
            print(f"Strona {i}: Pobrano {len(wynik)} znaków")

def synchroniczne_pobieranie():
    import requests
    strony = [
        "https://www.geeksforgeeks.org/",
        "https://www.amazon.pl/",
        "https://zoo.wroclaw.pl/",
        "https://www.youtube.com/",
    ]

    for i, url in enumerate(strony, 1):
        response = requests.get(url)
        print(f"Strona {i}: Pobrano {len(response.text)} znaków")

if __name__ == "__main__":
    print("Asynchroniczne pobranie stron:")
    start = time.time()
    asyncio.run(main())
    print(f"Czas acynchroniczny: {time.time() - start:.2f} sekund")

    print("\nSynchroniczne pobranie stron:")
    start = time.time()
    synchroniczne_pobieranie()
    print(f"Czas synchroniczny: {time.time() - start:.2f} sekund")


