from odoo import models, fields, api

class Kitten(models.Model):
    _name = 'cat_breeder.breed'
    _description = 'Feline Breeds'

    name = fields.Char("Name")
    kitten_ids = fields.One2many(
        "cat_breeder.kitten", "breed_id", string="Kittens", ondelete="set null", index=True
        )
