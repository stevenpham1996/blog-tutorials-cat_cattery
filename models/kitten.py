from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from dateutil.relativedelta import relativedelta


class Kitten(models.Model):
    _name = 'cat_breeder.kitten'
    _description = 'Adoptable Kittens'
    
    # --------------------------------------- Default Methods ----------------------------------
    def _default_birth_date(self):
        return (fields.Date.today() - relativedelta(weeks=8))
    
    name = fields.Char("Name")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender",  required=True)
    birth_date = fields.Date(
        "Birth Date", 
        default=lambda self: self._default_birth_date(), # Kitten must be at least 8 weeks old 
        required=True)
    color = fields.Char("Color")
    temperament = fields.Char("Temperament")
    active = fields.Boolean("Active", default=True) 
    state = fields.Selection(
        selection=[
            ('not_available', "Not Available"),
            ("available", "Available"),
            ("adopted", "Adopted"), 
        ],           
        string="Status",
        required=True,
        copy=False,
        default="available"
    )
    image = fields.Binary("Kitten's Image")
    
    # --------------------------------------- Relational Fields ----------------------------------
    breed_id = fields.Many2one("cat_breeder.breed", string="Breed")

    # --------------------------------------- Computed Fields ----------------------------------
    age = fields.Integer(string="Weeks Old", compute="_compute_age")
    
    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            record.age = round((fields.Date.today() - record.birth_date).days / 7)


    # --------------------------------------- Action Methods ----------------------------------
    def action_adopt(self):
        for record in self:
            if record.state == "adopted":
                raise UserError("Sorry, the kitten has gotten a new home.")
            elif record.state == "not_available":
                raise UserError("The kitten has not yet arrived at the cattery, please wait.")
            return record.write({"state": "adopted"})
                