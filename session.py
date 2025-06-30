import fastf1

def load_f1_session():
    year = int(input("Enter session year (e.g., '2023'): "))
    gp = input("Enter session Grand Prix (e.g., 'Monaco'): ").strip()
    stype = input("Enter session type (e.g., 'Q', 'R'): ").strip().upper()
    session = fastf1.get_session(year, gp, stype)
    session.load(laps=True)
    return session, year, gp