'''
PRATICANDO PARA RELEMBRAR E RECUPERAR O TEMPO QUE EU ESTAVA DOENTE. VAMOS PRA CIMA!
'''

class Configuracao_pc:
    def __init__(self, configuracao, placa_mae, processador, placa_video, ram, ssd, cooler, fonte):
        self.configuracao = configuracao
        self.placa_mae = placa_mae
        self.processador = processador
        self.placa_video = placa_video
        self.ram = ram
        self.ssd = ssd
        self.cooler = cooler
        self.fonte = fonte

    def __repr__(self):
        return (
            f"Configuracao:   {self.configuracao}💻\n"
            f"Placa Mae:      {self.placa_mae}\n"
            f"Processador:    {self.processador}\n"
            f"Placa de video: {self.placa_video}\n"
            f"Memoria RAM:    {self.ram[0]}x {self.ram[1]}\n"
            f"Memoria SSD:    {self.ssd[0]}x {self.ssd[1]}\n"
            f"Cooler:         {self.cooler}\n"
            f"Fonte:          {self.fonte}"
        )

pc_greg = Configuracao_pc(
    "PC do Gregory",
    "Aorus Elite B550M",
    "AMD Ryzen 7 5700X",
    "RTX 3060 12GB",
    [2 , "16GB Kingston Fury"],
    [1, "SSD Nvme 1TB Kingston"],
    "Water Cooler Rise Mode Aura Ice Black",
    "Fonte BRX Xtreme Zenith 850W"
)

pc_entrada = Configuracao_pc(
    "PC de Entrada",
    "MSI B450M-A Pro Max",
    "AMD Ryzen 5 5500",
    "RX 6600 8GB",
    [2, "8GB DDR4 3200MHz"],
    [1, "SSD NVMe 500GB Kingston"],
    "Air Cooler DeepCool AG400",
    "Fonte MSI Mag A650BN 650W"
)

pc_intermediario = Configuracao_pc(
    "PC Intermediário",
    "Gigabyte B550M DS3H",
    "AMD Ryzen 5 5600",
    "RTX 4060 8GB",
    [2, "8GB Corsair Vengeance"],
    [1, "SSD NVMe 1TB WD Blue"],
    "Air Cooler Cooler Master Hyper 212",
    "Fonte Corsair CV650 650W"
)

pc_entusiasta = Configuracao_pc(
    "PC Entusiasta",
    "ROG Strix X670E-E Gaming",
    "AMD Ryzen 7 7800X3D",
    "RTX 4080 Super 16GB",
    [2, "16GB G.Skill Trident Z5 DDR5"],
    [2, "SSD NVMe 2TB Samsung 990 Pro"],
    "Water Cooler NZXT Kraken Elite 360",
    "Fonte Corsair RM1000x 1000W"
)

lista_computadores = [pc_entrada, pc_intermediario, pc_greg, pc_entusiasta]

for computador in lista_computadores:
    print(f"{computador}\n")
