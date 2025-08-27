import click_
 
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

@cli.group()
def plant():
    """Manage plants"""
    pass    

@plant.command('list')
def list_plants();
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
