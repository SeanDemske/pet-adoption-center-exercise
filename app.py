from flask import Flask, request, redirect, render_template
from models import db, Pet, connect_db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:developer@localhost:5432/pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "SECRET!"

connect_db(app)
db.create_all()

# ////////////////
#     ROUTES
# ////////////////

@app.route("/")
def home_page():
    """Homepage"""

    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """Add pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        if data["photo_url"] == "":
            data["photo_url"] = "https://thehappypuppysite.com/wp-content/uploads/2019/03/Cartoon-Dog-Names-HP-long.jpg"
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet_form(pet_id):
    """Edit pet form"""

    pet = Pet.query.get(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        if pet.photo_url == "":
            pet.photo_url = "https://thehappypuppysite.com/wp-content/uploads/2019/03/Cartoon-Dog-Names-HP-long.jpg"
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet.html", form=form, pet=pet)