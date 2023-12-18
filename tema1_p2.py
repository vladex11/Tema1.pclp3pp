import pandas as pd
import matplotlib.pyplot as plt

class Grafic:
  #clasa generala pt grafic
    def __init__(self, data, x_col, y_col, label, marker, color):
        self.data = data
        self.x_col = x_col
        self.y_col = y_col
        self.label = label
        self.marker = marker
        self.color = color
  #metoda de afisare
    def afisare(self):
        plt.plot(self.data[self.x_col], self.data[self.y_col], label=self.label, marker=self.marker, color=self.color)

def main():
    data = pd.read_csv("data.csv")

    grafic1 = Grafic(data, "Durata", "Puls", "Puls", "*", "green")
    grafic2 = Grafic(data, "Durata", "Calorii", "Calorii", "*", "yellow")
    grafic3 = Grafic(data, "Durata", "MaxPuls", "Puls maxim", "*", "blue")

    grafic1.afisare()
    grafic2.afisare()
    grafic3.afisare()

    plt.title("Grafice pentru datele de activitate fizică")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
