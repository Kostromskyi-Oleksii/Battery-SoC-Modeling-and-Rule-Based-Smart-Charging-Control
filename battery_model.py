class Battery:
    def __init__(self, capacity_wh, soc_init):
        self.capacity_wh = capacity_wh
        self.soc = soc_init
        self.soh = 1.0
        self.cycles = 0

    def charge(self, power, dt, efficiency):
        energy = power * dt * efficiency
        self.soc += energy / (self.capacity_wh * self.soh)
        self.soc = min(self.soc, 1.0)

    def discharge(self, power, dt, efficiency):
        energy = power * dt / efficiency
        self.soc -= energy / (self.capacity_wh * self.soh)
        self.soc = max(self.soc, 0.0)

    def update_soh(self, degradation_rate):
        self.cycles += 1
        self.soh = max(0.7, 1 - degradation_rate * self.cycles)
