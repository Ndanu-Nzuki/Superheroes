from server.app import create_app, db
from server.models import Hero, Power

def seed_data():
    # Incredibles data
    hero1 = Hero(name="Bob Parr", super_name="Mr. Incredible")
    hero2 = Hero(name="Helen Parr", super_name="Elastigirl")
    hero3 = Hero(name="Violet Parr", super_name="Violet")
    hero4 = Hero(name="Dash Parr", super_name="Dash")
    hero5 = Hero(name="Jack-Jack Parr", super_name="Jack-Jack")

    power1 = Power(name="Super Strength", description="Gives the wielder super-human strength.")
    power2 = Power(name="Elasticity", description="Allows the user to stretch their body into various shapes.")
    power3 = Power(name="Invisibility", description="Grants the ability to become unseen by others.")
    power4 = Power(name="Super Speed", description="Allows the user to move at incredible speeds.")
    power5 = Power(name="Fire Manipulation", description="Enables the user to control and create fire.")

    # Adding the data to the session
    db.session.add_all([hero1, hero2, hero3, hero4, hero5, power1, power2, power3, power4, power5])
    db.session.commit()


if __name__ == '__main__':
    app = create_app() 
    with app.app_context():
        db.create_all()  
        seed_data()
        print("Database seeded!")
