from odoo import api, models


class AdopterReport(models.AbstractModel):
    _name = "report.cattery.adopter_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [("adopter_id", "in", docids)]
        kittens = self.env["cattery.kitten"].search(domain)
        adopters = kittens.mapped("adopter_id")
        adopter_kittens = [
            (adopter, kittens.filtered(lambda kitten: kitten.adopter_id == adopter))
            for adopter in adopters
        ]
        docargs = {
            "adopter_kittens": adopter_kittens,
        }
        return docargs
