from .database import Session
from . import Plant

def seed_plants():
    session = Session()
    
    plants_data = [
        ("Monstera Deliciosa", 2500.00),
        ("Snake Plant (Sansevieria)", 800.00),
        ("Peace Lily", 1200.00),
        ("Rubber Plant (Ficus)", 1800.00),
        ("Aloe Vera", 600.00),
        ("Spider Plant", 500.00),
        ("Pothos Golden", 700.00),
        ("ZZ Plant (Zamioculcas)", 1500.00),
        ("Fiddle Leaf Fig", 3500.00),
        ("Philodendron Heartleaf", 900.00),
        ("Boston Fern", 1100.00),
        ("Dracaena Marginata", 2200.00),
        ("Calathea Ornata", 1600.00),
        ("Bird of Paradise", 4000.00),
        ("Jade Plant", 750.00),
        ("English Ivy", 650.00),
        ("Parlor Palm", 1300.00),
        ("Croton Petra", 1400.00),
        ("Anthurium Red", 2800.00),
        ("Succulent Mix", 400.00)
    ]
    
    # Get current exchange rate (fallback to 130 if API fails)
    try:
        import requests
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD', timeout=5)
        ksh_rate = response.json()['rates']['KES']
    except:
        ksh_rate = 130.0
    
    for name, price_ksh in plants_data:
        price_usd = price_ksh / ksh_rate  # Convert to USD for storage
        plant = Plant(name=name, price=price_usd)
        session.add(plant)
    
    session.commit()
    session.close()
    print(f"Added {len(plants_data)} plants to the database")

if __name__ == "__main__":
    seed_plants()