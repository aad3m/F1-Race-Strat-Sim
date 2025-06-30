from typing import List, Tuple, Dict

from tireCompounds import TireCompound, compounds


# Scenario definitions
def apply_race_conditions(lap_index: int, drs: bool, ers: bool, safety_car_laps: List[int], red_flag_laps: List[int], track_grip: float):
    if lap_index in red_flag_laps:
        return 0  # simulate session pause
    base_modifier = 0
    if lap_index in safety_car_laps:
        base_modifier += 8  # slower laps
    if drs:
        base_modifier -= 0.3
    if ers:
        base_modifier -= 0.2
    grip_bonus = (1.0 - track_grip)
    return base_modifier + grip_bonus

def simulate_strategy(strategy: List[Tuple[str, int]], compounds: Dict[str, TireCompound],
                      pit_loss=22.0, fuel_effect=0.03, drs=True, ers=True,
                      safety_car_laps=[], red_flag_laps=[], track_evo=0.02) -> Tuple[float, List[float], List[str]]:
    total_time = 0.0
    lap_times = []
    warnings = []
    lap_index = 0
    evo = 0.0

    for stint_index, (compound_name, stint_length) in enumerate(strategy):
        if compound_name not in compounds:
            warnings.append(f"Unknown compound: {compound_name}")
            continue

        compound = compounds[compound_name]

        if stint_length > compound.max_life:
            warnings.append(f"WARNING: {compound_name} used for {stint_length} laps (max {compound.max_life})")

        for lap in range(1, stint_length + 1):
            evo += track_evo
            grip = min(evo, 1.0)
            base_time = compound.lap_time(lap)
            modifiers = apply_race_conditions(lap_index, drs, ers, safety_car_laps, red_flag_laps, 1.0 - grip)
            fuel_penalty = (fuel_effect * (50 - lap_index))  # less fuel = faster
            time = base_time + modifiers - fuel_penalty
            lap_times.append(time)
            total_time += time
            lap_index += 1

        if stint_index < len(strategy) - 1:
            total_time += pit_loss  # add pit stop time

    return total_time, lap_times, warnings

# Optimal strategy search (basic brute force)
def generate_strategies(max_laps=70) -> List[List[Tuple[str, int]]]:
    strategies = []
    for s1 in ["Soft", "Medium", "Hard"]:
        for s2 in ["Soft", "Medium", "Hard"]:
            for len1 in range(10, 35, 5):
                len2 = max_laps - len1
                if 10 <= len2 <= 40:
                    strategies.append([(s1, len1), (s2, len2)])
    return strategies

def find_best_strategy():
    candidates = generate_strategies()
    best_time = float("inf")
    best_strat = None
    for strat in candidates:
        t, _, _ = simulate_strategy(strat, compounds)
        if t < best_time:
            best_time = t
            best_strat = strat
    return best_strat, best_time
