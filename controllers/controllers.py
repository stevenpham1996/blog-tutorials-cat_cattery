from odoo import http


class CatBreeder(http.Controller):

    @http.route('/cat_breeder/kitten', auth='public')
    def list(self, **kw):
        Kitten = http.request.env["cat_breeder.kitten"]
        kittens = Kitten.search([])
        return http.request.render(
            'cat_breeder.breeder_kitten_list_template', 
            {'kittens': kittens}
        )


    # @http.route('/cat_breeder/cat_breeder', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
#     @http.route('/cat_breeder/cat_breeder/objects/<model("cat_breeder.cat_breeder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cat_breeder.object', {
#             'object': obj
#         })

