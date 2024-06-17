from odoo import models, fields


class Breed(models.Model):
    _name = "cattery.breed"
    _description = "Feline Breeds"

    name = fields.Char("Name")
    kitten_ids = fields.One2many(
        "cattery.kitten", "breed_id", string="Kittens", index=True
    )
