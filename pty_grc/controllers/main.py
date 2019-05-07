import odoo.http as http
from odoo.http import request


class WebServices(http.Controller):
    @http.route('/web-services', type="http", auth="public", website=True)
    def support_help(self, **kw):

        return http.request.render('pty_grc.web_services')

    @http.route('/web-services/my', type="http", auth="user", website=True)
    def my_web_services(self, **kw):
        my_tickets = request.env['website.support.ticket'].search(['|', ('create_user_id', '=', request.env.user.id),
                                                                   ('partner_id', '=', request.env.user.partner_id.id)])
        return http.request.render('pty_grc.my_web_services', {'my_tickets': my_tickets})

    @http.route('/web-services/create', type="http", auth="public", website=True)
    def web_services_create(self, *args, **post):
        dico = {}
        if request.httprequest.method == 'GET':
            type = post.get('type')
            rtype = request.env['website.support.ticket.subcategory'].search([('name', '=', type)])
            dico['type'] = rtype
        if request.httprequest.method == 'POST':
            if request.env.user.name != 'Public user':
                request.env['website.support.ticket'].create({'subject': post.get('subject', False),
                                                              'create_user_id': request.env.user.id})
                return http.request.redirect('/web-services/my')
            else:
                request.env['website.support.ticket'].sudo().create({'subject': post.get('subject', False),
                                                                     'create_user_id': 4})
                return http.request.redirect('/')

        return http.request.render('pty_grc.web_services_create', dico)