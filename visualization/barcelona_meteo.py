# visualization/barcelona_meteo.py
import matplotlib.pyplot as plt
import os

def plot_temperature(meteo, output_file=None):
    meses = [dato[0] for dato in meteo]
    t_max = [dato[1] for dato in meteo]
    t_min = [dato[2] for dato in meteo]
    t_media = [dato[3] for dato in meteo]

    plt.figure(figsize=(15,8))
    plt.plot(meses, t_max, color='red', label='Temperatura máxima')
    plt.plot(meses, t_min, color='blue', label='Temperatura mínima')
    plt.plot(meses, t_media, color='yellow', label='Temperatura media')
    plt.xlabel('Mes')
    plt.ylabel('Temperatura (ºC)')
    plt.title('Meteo Barcelona Airport - Temperatura')
    plt.legend()
    plt.ylim(0,35)

    if output_file:
        plt.savefig(output_file)
        print(f"Temperature plot saved to {output_file}")
        plt.close()
    else:
        plt.show()

def plot_rain_humidity(meteo, output_file=None):
    meses = [dato[0] for dato in meteo]
    lluvia = [dato[5] for dato in meteo]
    h_rel = [dato[4] for dato in meteo]

    fig, ax1 = plt.subplots(figsize=(15,8))
    ax1.bar(meses, lluvia, color='blue')
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Lluvia (mm)')
    ax1.set_ylim(0,100)
    ax1.set_title('Meteo Barcelona Airport - Lluvia y Humedad')

    ax2 = ax1.twinx()
    ax2.plot(meses, h_rel, color='green', label='Humedad relativa (%)')
    ax2.set_ylabel('Humedad relativa (%)')
    ax2.set_ylim(0,100)

    if output_file:
        plt.savefig(output_file)
        print(f"Rain & humidity plot saved to {output_file}")
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    meteo = [
        ["January", 13.6, 4.7, 9.2, 70, 37],
        ["February",14.3, 5.4, 9.9, 70, 35],
        ["March", 16.1, 7.4, 11.8, 70, 36],
        ["April", 18.0, 9.4, 13.7, 69, 40],
        ["May", 21.1, 12.8, 16.9, 70, 47],
        ["June", 24.9, 16.8, 20.9, 68, 30],
        ["July", 28.0, 19.8, 23.9, 67, 21],
        ["August", 28.5, 20.2, 24.4, 68, 62],
        ["September", 26.0, 17.4, 21.7, 70, 81],
        ["October", 22.1, 13.5, 17.8, 73, 91],
        ["November", 17.3, 8.6, 13.0, 71, 59],
        ["December", 14.3, 5.7, 10.0, 69, 40]
    ]

    plots_dir = os.path.join(os.path.dirname(__file__), "plots")
    os.makedirs(plots_dir, exist_ok=True)

    plot_temperature(meteo, output_file=os.path.join(plots_dir, "temperature.png"))
    plot_rain_humidity(meteo, output_file=os.path.join(plots_dir, "rain_humidity.png"))
