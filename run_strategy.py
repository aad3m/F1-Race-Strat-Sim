from strategy import simulate_strategy, find_best_strategy, compounds


def format_strategy(strategy):
    return " -> ".join(f"{c} {l}L" for c, l in strategy)


def main():
    print("=== F1 Strategy Simulator ===")
    mode = input("Type 'custom' to enter your own strategy, or 'best' to find optimal: ").strip().lower()

    if mode == 'custom':
        inp = input("Enter stints (e.g., Soft 15, Medium 30): ").strip()
        try:
            stints = [
                (c.strip().title(), int(l.strip()))
                for c, l in (s.split() for s in inp.split(","))
            ]
        except Exception as e:
            print("❌ Invalid input.")
            return
        total_time, laps, warns = simulate_strategy(stints, compounds)
        print("\nStints:", stints)
        print(f"Simulated Total Time: {total_time:.2f} sec")
        if warns:
            print("Warnings:")
            for w in warns:
                print("-", w)

    elif mode == 'best':
        best_strat, best_time = find_best_strategy()
        print("\n✅ Best Strategy Found:")
        print(format_strategy(best_strat))
        print(f"Estimated Race Time: {best_time:.2f} sec")

    else:
        print("❌ Unknown mode. Use 'custom' or 'best'.")


if __name__ == '__main__':
    main()
