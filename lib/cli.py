import click
 
from lib.database import Base, engine, Session
from lib.models.plant import Plant
from lib.models.customer import customer
from lib.models.sale import Sale
from lib.models.employee import Employee

Base.metadata.create_all(engine)

@click.group()
def cli():
    """Plant Nursery Management CLI"""
    pass

#.....................plant.....................

@cli.group()
def plant():
    """Manage plants"""
    pass    

@plant.command('list')
def list_plants():
    plants = Session.query(Plant).all()
    for p in plants:
        click.echo(f"{p.id}: {p.name} - ${p.price}")


@plant.command('add')
@click.argument('name')
@click.argument('price', type=float)
def add_plant(name, price):
    new_plant = Plant(name=name, price=price)
    Session.add(new_plant)
    Session.commit()
    click.echo(f"✅ Plant '{name}' added!")


@plant.command('delete')
@click.argument('plant_id', type=int)
def delete_plant(plant_id):
    plant = Session.query(Plant).get(plant_id)
    if plant:
        Session.delete(plant)
        Session.commit()
        click.echo(f"🗑️ Plant '{plant.name}' deleted!")
    else:
        click.echo("❌ Plant not found.")


#.....................customer.....................
@cli.group()
def customer():
    """Manage customers"""
    pass
@customer.command('list')
def list_customers():
    customers = Session.query(customer).all()
    for c in customers:
        click.echo(f"{c.id}: {c.name} - {c.email}")


@customer.command('add')
@click.argument('name')
@click.argument('email')
def add_customer(name, email):
    new_customer = customer(name=name, email=email)
    Session.add(new_customer)
    Session.commit()
    click.echo(f"✅ Customer '{name}' added!")

#.....................Employees.....................
@cli.group()
def employee():
    """Manage employees"""
    pass    
@employee.command('list')
def list_employees():
    employees = Session.query(Employee).all()
    for e in employees:
        click.echo(f"{e.id}: {e.name} - {e.role}")


@employee.command('add')
@click.argument('name')
@click.argument('role')
def add_employee(name, role):
    new_employee = Employee(name=name, role=role)
    Session.add(new_employee)
    Session.commit()
    click.echo(f"✅ Employee '{name}' added!")

#.....................Sales.....................
@cli.group()
def sale():
    """Manage sales"""
    pass    
@sale.command('list')
def list_sales():
    sales = Session.query(Sale).all()
    for s in sales:
        click.echo(f"{s.id}: {s.quality} x {s.plant.name} to {s.customer.name}")


@sale.command('add')
@click.argument('plant_id', type=int)
@click.argument('customer_id', type=int)
@click.argument('quality', type=int)   
def add_sale(plant_id, customer_id, quality):
    new_sale = Sale(plant_id=plant_id, customer_id=customer_id, quality=quality)
    Session.add(new_sale)
    Session.commit()
    click.echo(f"✅ sale recorded!")

if __name__ == '__main__':
    cli()