from flask import jsonify, request, abort
from .app import db
from .models import Hero, Power, HeroPower

def register_routes(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Superheroes API!"})
    
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes])

    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if hero is None:
            abort(404, description="Hero not found")
        return jsonify(hero.to_dict())

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers])

    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if power is None:
            abort(404, description="Power not found")
        return jsonify(power.to_dict())

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
            return jsonify(power.to_dict())
        except:
            db.session.rollback()
            abort(400, description="Invalid data")

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
            return jsonify(hero.to_dict()), 201
        except:
            db.session.rollback()
            abort(400, description="Invalid data")
