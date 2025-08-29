from .database import Session
from . import Plant, Customer, Employee, Sale

def list_plants(session):
    plants = session.query(Plant).all()
    if not plants:
        print("No plants found.")
    else:
        for plant in plants:
            print(f"{plant.id}. {plant.name} - ${plant.price}")

def add_plant(session):
    name = input("Enter plant name: ")
    price = int(input("Enter price: "))
    plant = Plant(name=name, price=price)
    session.add(plant)
    session.commit()
    print("Plant added successfully!")

def record_sale(session):
    list_plants(session)
    plant_id = int(input("Enter plant ID to sell: "))
    customer_name = input("Enter customer name: ")
    employee_name = input("Enter employee name: ")

    customer = session.query(Customer).filter_by(name=customer_name).first()
    if not customer:
        customer = Customer(name=customer_name)
        session.add(customer)

    employee = session.query(Employee).filter_by(name=employee_name).first()
    if not employee:
        employee = Employee(name=employee_name)
        session.add(employee)

    plant = session.query(Plant).get(plant_id)
    if not plant:
        print("Invalid plant ID.")
        return

    sale = Sale(plant=plant, customer=customer, employee=employee)
    session.add(sale)
    session.commit()
    print("Sale recorded!")

def list_sales(session):
    sales = session.query(Sale).all()
    if not sales:
        print("No sales yet.")
    else:
        for sale in sales:
            print(f"Sale #{sale.id}: {sale.customer.name} bought {sale.plant.name} from {sale.employee.name}")

def main():
    session = Session()

    while True:
        print("\n🌱 Plant Nursery Manager 🌱")
        print("1. List plants")
        print("2. Add plant")
        print("3. Record sale")
        print("4. List sales")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_plants(session)
        elif choice == "2":
            add_plant(session)
        elif choice == "3":
            record_sale(session)
        elif choice == "4":
            list_sales(session)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()