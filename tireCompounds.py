# TireCompound class
class TireCompound:
    def __init__(self, name, base_time, degradation, max_life, warmup=3, cliff=1.5):
        self.name = name
        self.base_time = base_time
        self.degradation = degradation
        self.max_life = max_life
        self.warmup = warmup
        self.cliff = cliff

    def lap_time(self, lap_num):
        if lap_num <= self.warmup:
            return self.base_time + (self.warmup - lap_num) * 1.2  # slower in early laps
        elif lap_num > self.max_life:
            excess = lap_num - self.max_life
            return self.base_time + self.degradation * lap_num + self.cliff * excess
        else:
            return self.base_time + self.degradation * lap_num

# Enhanced compound definitions
compounds = {
    "C0": TireCompound("C0", 91.5, 0.10, 45, 1),
    "C1": TireCompound("C1", 91.0, 0.12, 40, 1),
    "C2": TireCompound("C2", 90.5, 0.15, 35, 2),
    "C3": TireCompound("C3", 89.5, 0.20, 30, 2),
    "C4": TireCompound("C4", 88.5, 0.30, 20, 3),
    "C5": TireCompound("C5", 87.5, 0.40, 15, 3),
    "Soft": TireCompound("Soft", 89.5, 0.30, 20, 3),
    "Medium": TireCompound("Medium", 90.5, 0.20, 30, 2),
    "Hard": TireCompound("Hard", 91.5, 0.10, 45, 1),
    "Super Soft": TireCompound("Super Soft", 87.0, 0.45, 12, 2),
    "Ultra Soft": TireCompound("Ultra Soft", 86.5, 0.50, 10, 2),
    "Hyper Soft": TireCompound("Hyper Soft", 86.0, 0.60, 8, 2),
    "Intermediate": TireCompound("Intermediate", 95.0, 0.15, 30, 2),
    "Wet": TireCompound("Wet", 100.0, 0.25, 25, 2),
    "Test": TireCompound("Test", 92.0, 0.20, 25, 1)
}