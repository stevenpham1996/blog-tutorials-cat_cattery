from odoo import http


class Catcattery(http.Controller):

    @http.route('/cat_cattery/kitten', auth='public')
    def list(self, **kw):
        Kitten = http.request.env["cat_cattery.kitten"]
        kittens = Kitten.search([])
        return http.request.render(
            'cat_cattery.cattery_kitten_list_template', 
            {'kittens': kittens}
        )




