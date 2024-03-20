from odoo import models, fields, api


class Kittens(models.Model):
    _name = 'cat_breeder.kittens'
    _description = 'Available Kittens'

    name = fields.Char("Name")
    breed = fields.Char("Breed", required=True)
    gender = fields.Selection("Gender", [('male', 'Male'), ('female', 'Female')], required=True)
    birth_date = fields.Date("Birth Date", required=True)
    color = fields.Char("Color")
    
    # --------------------------------------- Computed Fields ----------------------------------
    age = fields.Integer("Days Old", compute="_compute_age")
    
    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                record.age = (fields.Date.today() - record.birth_date).days
        


