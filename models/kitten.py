from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta


class Kitten(models.Model):
    _name = 'cat_breeder.kitten'
    _description = 'Kittens'
    
    # --------------------------------------- Default Methods ----------------------------------
    def _default_birth_date(self):
        return (fields.Date.today() - relativedelta(weeks=8))
    
    active = fields.Boolean("Active", default=True) 
    name = fields.Char("Name")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender",  required=True)
    birth_date = fields.Date(
        "Birth Date", 
        default=lambda self: self._default_birth_date(), # Kitten must be at least 8 weeks old 
        required=True)
    color = fields.Char("Color")
    temperament = fields.Char("Temperament")
    state = fields.Selection(
        selection=[
            ('not_available', "Not Arrived"),
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
    adopter_id = fields.Many2one("res.partner", string="Adopter")
    # --------------------------------------- Computed Fields ----------------------------------
    age = fields.Integer(string="Weeks Old", compute="_compute_age")
    
    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            record.age = round((fields.Date.today() - record.birth_date).days / 7)


    # --------------------------------------- Action Methods ----------------------------------
    def action_adopt(self):
        if self.state == "adopted":
            raise UserError("Sorry, the kitten has gotten a new home.")
        elif self.state == "not_available":
            raise UserError("The kitten's not yet arrived at the cattery,\
                but we've registered your interest, please wait.")
        return self.write({"state": "adopted"})
     
    # --------------------------------------- Constraints ----------------------------------
    @api.constrains("state", "adopter_id")
    def _check_adopter_id(self):
        for record in self:
            if record.state != "adopted" and record.adopter_id:
                raise ValidationError("Only adopted kittens can have an adopter.")
    
                