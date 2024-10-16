from server.app import create_app, db
from server.models import Hero, Power

def seed_data():
    db.session.query(Hero).delete()
    db.session.query(Power).delete()
    db.session.commit()  
    
    hero1 = Hero(name="Bob Parr", super_name="Mr. Incredible")
    hero2 = Hero(name="Helen Parr", super_name="Elastigirl")
    hero3 = Hero(name="Violet Parr", super_name="Violet")
    hero4 = Hero(name="Dash Parr", super_name="Dash")
    hero5 = Hero(name="Jack-Jack Parr", super_name="Jack-Jack")
    hero6 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero7 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero8 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    hero9 = Hero(name="Janet Van Dyne", super_name="The Wasp")
    hero10 = Hero(name="Wanda Maximoff", super_name="Scarlet Witch")
    hero11 = Hero(name="Carol Danvers", super_name="Captain Marvel")
    hero12 = Hero(name="Jean Grey", super_name="Dark Phoenix")
    hero13 = Hero(name="Ororo Munroe", super_name="Storm")
    hero14 = Hero(name="Kitty Pryde", super_name="Shadowcat")
    hero15 = Hero(name="Elektra Natchios", super_name="Elektra")

    power1 = Power(name="Super Strength", description="Gives the wielder super-human strength.")
    power2 = Power(name="Elasticity", description="Allows the user to stretch their body into various shapes.")
    power3 = Power(name="Invisibility", description="Grants the ability to become unseen by others.")
    power4 = Power(name="Super Speed", description="Allows the user to move at incredible speeds.")
    power5 = Power(name="Fire Manipulation", description="Enables the user to control and create fire.")
    power6 = Power(name="Shape-shifting", description="Allows the user to alter their appearance and size.")
    power7 = Power(name="Super Strength", description="Gives the wielder super-human strength.")
    power8 = Power(name="Web-Shooting", description="Allows the user to shoot webs for swinging and trapping.")
    power9 = Power(name="Pym Particles", description="Allows the user to change size at will.")
    power10 = Power(name="Chaos Magic", description="Enables the user to manipulate reality through magic.")
    power11 = Power(name="Photon Manipulation", description="Allows the user to manipulate energy and light.")
    power12 = Power(name="Telepathy", description="Allows the user to read minds and communicate mentally.")
    power13 = Power(name="Weather Control", description="Grants the ability to control weather patterns.")
    power14 = Power(name="Phasing", description="Allows the user to pass through solid objects.")
    power15 = Power(name="Martial Arts Mastery", description="Expert in various forms of combat.")

    
    db.session.add_all([hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10, hero11, hero12, hero13, hero14, hero15, 
                        power1, power2, power3, power4, power5, power6, power7, power8, power9, power10, power11, power12, power13, power14, power15])
    db.session.commit()


if __name__ == '__main__':
    app = create_app() 
    with app.app_context():
        db.create_all()  
        seed_data()
        print("Database seeded!")
