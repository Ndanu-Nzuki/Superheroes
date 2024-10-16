from flask import jsonify, request, abort
from .app import db
from .models import Hero, Power, HeroPower

def register_routes(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    # Get all heroes
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]), 200

    # Get a hero by ID
    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if hero is None:
            abort(404, description="Hero not found")
        
        hero_powers = [
            {
                "hero_id": hp.hero_id,
                "id": hp.id,
                "strength": hp.strength,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            } for hp in hero.hero_powers
        ]

        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": hero_powers
        }), 200

    # Get all powers
    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([{"id": power.id, "name": power.name, "description": power.description} for power in powers]), 200

    # Get a power by ID
    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if power is None:
            abort(404, description="Power not found")
        
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    # Update a power by ID
    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if power is None:
            abort(404, description="Power not found")

        data = request.json
        if 'description' in data:
            power.description = data['description']
        
        try:
            db.session.commit()
            return jsonify(power.to_dict()), 200
        except:
            db.session.rollback()
            abort(400, description="Invalid data")

    # Create a hero power association
    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.json
        if not all(k in data for k in ('strength', 'power_id', 'hero_id')):
            abort(400, description="Missing required data")
        
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])
        
        if hero is None or power is None:
            abort(404, description="Hero or Power not found")

        hero_power = HeroPower(
            strength=data['strength'],
            hero=hero,
            power=power
        )
        
        try:
            db.session.add(hero_power)
            db.session.commit()
            return jsonify({
                "id": hero_power.id,
                "hero_id": hero_power.hero_id,
                "power_id": hero_power.power_id,
                "strength": hero_power.strength,
                "hero": {
                    "id": hero.id,
                    "name": hero.name,
                    "super_name": hero.super_name
                },
                "power": {
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
                }
            }), 201
        except:
            db.session.rollback()
            abort(400, description="Invalid data")
