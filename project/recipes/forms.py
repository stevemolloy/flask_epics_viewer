# project/recipes/forms.py


from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from project import images


class AddRecipeForm(Form):
    recipe_title = StringField('Recipe Title', validators=[DataRequired()])
    recipe_description = StringField('Recipe Description', validators=[DataRequired()])
    recipe_public = BooleanField('Public Recipe', default="")
    recipe_type = RadioField('Recipe Type', validators=[DataRequired()],
                             choices=[('Breakfast', 'Breakfast Recipe'),
                                      ('Lunch', 'Lunch Recipe'),
                                      ('Dinner', 'Dinner Recipe'),
                                      ('Dessert', 'Dessert Recipe'),
                                      ('Side', 'Side Dish')],
                             default='Dinner')
    recipe_image = FileField('Recipe Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
