'name': "CGR Parthenay-Gatine",
'version': "10.0.0.1"
'summary': "",
'description':
'actor':
'website':
'licence':
'catégorie':
'esternal_dependance':
'dépendance':
'data': (bien mettre le chemin).
'demo':
'application':true,
'auto_install':false,                                               ''
                                                        

        
        
        
        
        
        
        
# -*- coding; utf-8 -*-
from odoo import model, field, api, expession

class service(models.Model):
    
    _name = 'website.support.ticket.service'
    
    name = fields.char()
    
    sub_catégory_id = fields.One2many(string='sub_category', comedel_name='website.support.ticket.subcategory',
    inverse_name='service_id')

    email = fields.char(string="Email")
    
class inheritedWebsiteSuppourtTickets(models.Model):
    
    _inherit = 'website.support.ticket'
    _order = 'priority_id.sequence'
    service_id = fields.Many2one(related='sub_category_id.service_id', readonly=true)
    
    additionnal_service_ids = field.Many2Many(string ='additonnal service_id', comodel_name='website.support.ticket.service')
   
    parent_ticket_id =field.many2many(string='related ticket', comodel='website.support.ticket')
    related_ticket_ids = field.Many2Many(string='related ticket', comodel='website.support.ticket', inverse_name='parent_ticket_id',groups='')

    @api.onchange('category')
    def onchange_category(self):
        self.sub_category_id = False

        
    @api.constraints('category')
    def check_category(self):
    if self.category.id == 1 and self.priority_id.sequence <2:
         raise exception.ValidatorError("vous avais une error.")
        
    @api.multi
    def write(self, val):
        if vals.get('state'):
            if self.state.id != 1 and vals['state'] == 1
                raise exception.ValidatorError("vous ne pouvez pas revenir en arrière.")
        return super(inheritedWebsiteSuppourtTickets,self).write(vals)   
        
    delay = field.interger(string='delay')
    
class InheritedWebsiteSupportCategory(models.Model)

    _inherit = 'website.support.ticket.subcategory'
    
    service_id = fields.Many2one(string='service', comedel='website.support.service')
    
    
    

                                                        
                                                    
