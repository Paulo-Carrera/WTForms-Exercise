from flask import Flask , render_template, redirect
from models import db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'loki444'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()


@app.route('/')
def homepage():
    """Show list of all pets"""

    pets = Pet.query.all()
    return render_template('pets.html', pets = pets)


@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """Add a pet"""

    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            available = form.available.data
        )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet_form.html', form = form)
    

@app.route('/pets/<int:pet_id>/edit', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    """Edit an existing pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj = pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else :
        return render_template('edit_pet_form.html', form = form)




if __name__ == '__main__':
    app.run(debug=True)