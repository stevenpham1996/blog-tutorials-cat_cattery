from odoo import http


class Catcattery(http.Controller):

    @http.route("/cattery/kitten", auth="public")
    def list(self, **kw):
        Kitten = http.request.env["cattery.kitten"]
        kittens = Kitten.search([])
        return http.request.render(
            "cattery.cattery_kitten_list_template", {"kittens": kittens}
        )
