import yfinance as yf
import matplotlib.pyplot as plt

accion = input("Ingrea codigo de Accion: ")
inicio = input("Fecha de inicio, AAAA-MM-DD: ")
final = input("Fecha de Final, AAAA-MM-DD: ")

try:
    data = yf.download(accion, start=inicio, end=final)
    print(data.head())

    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"])
    plt.title(f"{accion} stock Chart")
    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.show()

except ValueError:
    print("No se encuentra la accion")  
