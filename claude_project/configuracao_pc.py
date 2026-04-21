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

class ConfiguracaoGamer(Configuracao_pc):
    def __init__(self, configuracao, placa_mae, processador, placa_video, ram, ssd, cooler, fonte, monitor, headset):
        super().__init__(configuracao, placa_mae, processador, placa_video, ram, ssd, cooler, fonte)
        self.monitor = monitor
        self.headset = headset

    def __repr__(self):
        return (
            f"Configuracao:   {self.configuracao}💻☠️\n"
            f"Placa Mae:      {self.placa_mae}\n"
            f"Processador:    {self.processador}\n"
            f"Placa de video: {self.placa_video}\n"
            f"Memoria RAM:    {self.ram[0]}x {self.ram[1]}\n"
            f"Memoria SSD:    {self.ssd[0]}x {self.ssd[1]}\n"
            f"Cooler:         {self.cooler}\n"
            f"Fonte:          {self.fonte}\n"
            f"Monitor:        {self.monitor}\n"
            F"Headset:        {self.headset}\n"
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

lista_pcs = [pc_entrada, pc_intermediario, pc_greg, pc_entusiasta]

for computador in lista_pcs:
    print(f"{computador}\n")


pc_gamer_elite = ConfiguracaoGamer(
    "PC Gamer Elite",
    "ASUS ROG Strix X670E-E Gaming WiFi",
    "AMD Ryzen 7 7800X3D",
    "NVIDIA GeForce RTX 4080 Super 16GB",
    [2, "16GB G.Skill Trident Z5 DDR5 6000MHz"],
    [2, "SSD NVMe 2TB Samsung 990 Pro"],
    "NZXT Kraken Elite 360",
    "Corsair RM1000x 1000W",
    "ASUS ROG Swift PG27AQDM 27\" OLED 240Hz",
    "SteelSeries Arctis Nova Pro"
)

pc_gamer_gladiator = ConfiguracaoGamer(
    "PC Gamer Gladiator",
    "MSI MPG B650 Carbon WiFi",
    "AMD Ryzen 7 7700X",
    "NVIDIA GeForce RTX 4070 Ti Super 16GB",
    [2, "16GB Corsair Vengeance DDR5 6000MHz"],
    [1, "SSD NVMe 2TB WD Black SN850X"],
    "Corsair iCUE H150i Elite Capellix",
    "Corsair RM850x 850W",
    "LG UltraGear 27GP850-B 27\" 165Hz",
    "HyperX Cloud III"
)

pc_gamer_spartan = ConfiguracaoGamer(
    "PC Gamer Spartan",
    "ASUS TUF Gaming B650-PLUS",
    "AMD Ryzen 5 7600X",
    "NVIDIA GeForce RTX 4070 12GB",
    [2, "16GB Kingston Fury Beast DDR5 5600MHz"],
    [1, "SSD NVMe 1TB Kingston KC3000"],
    "Cooler Master MasterLiquid ML240L",
    "Corsair RM750e 750W",
    "AOC 24G2SP 24\" 165Hz",
    "Razer BlackShark V2"
)

pc_gamer_valkyrie = ConfiguracaoGamer(
    "PC Gamer Valkyrie",
    "Gigabyte B550 AORUS Elite V2",
    "AMD Ryzen 7 5800X3D",
    "NVIDIA GeForce RTX 4060 Ti 16GB",
    [2, "16GB Corsair Vengeance LPX DDR4 3600MHz"],
    [1, "SSD NVMe 1TB Samsung 970 EVO Plus"],
    "DeepCool AK620",
    "XPG Core Reactor 750W",
    "Samsung Odyssey G5 27\" 144Hz",
    "Logitech G Pro X"
)

pc_gamer_legacy = ConfiguracaoGamer(
    "PC Gamer Legacy",
    "ASUS TUF Gaming B550M-PLUS",
    "AMD Ryzen 5 5600",
    "NVIDIA GeForce RTX 4060 8GB",
    [2, "8GB Kingston Fury Beast DDR4 3200MHz"],
    [1, "SSD NVMe 1TB WD Blue SN570"],
    "Cooler Master Hyper 212 Black Edition",
    "Corsair CV650 650W",
    "Acer Nitro VG240Y 24\" 165Hz",
    "HyperX Cloud Stinger 2"
)

lista_pc_gamers = [pc_gamer_elite, pc_gamer_gladiator, pc_gamer_spartan, pc_gamer_valkyrie, pc_gamer_legacy]

for computador in lista_pc_gamers:
    print(f"{computador}\n")