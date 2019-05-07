# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Service(models.Model):

    _name = 'website.support.ticket.service'

    name = fields.Char()
    sub_category_id = fields.One2many(string='Sub category',
                                      comodel_name='website.support.ticket.subcategory',
                                      inverse_name='service_id')
    email = fields.Char(string='Email')
    ticket_count = fields.Integer(string="Ticket count", compute='compute_ticket_count')
    ticket_urgent_count = fields.Integer(string="Ticket urgent count", compute='compute_ticket_urgent_count')
    my_ticket_count = fields.Integer(string="My tickets count", compute='compute_my_ticket_count')

    def compute_ticket_count(self):
        for rec in self:
            count = self.env['website.support.ticket'].search_count([('service_id', '=', rec.id)])
            rec.ticket_count = count

    def compute_ticket_urgent_count(self):
        for rec in self:
            count = self.env['website.support.ticket'].search_count([('priority_id', '=', 5),('service_id', '=', rec.id)])
            rec.ticket_urgent_count = count

    def compute_my_ticket_count(self):
        for rec in self:
            count = self.env['website.support.ticket'].search_count([('user_id', '=', self.env.user.id), ('service_id', '=', rec.id)])
            rec.my_ticket_count = count


class InheritedWebsiteSupportTickets(models.Model):

    _inherit = 'website.support.ticket'
    _order = 'priority_id desc'

    service_id = fields.Many2one(related='sub_category_id.service_id', readonly=True)
    additionnal_service_ids = fields.Many2many(string='Additionnal services',
                                               comodel_name='website.support.ticket.service')
    parent_ticket_id = fields.Many2one(string='Related ticket', comodel_name='website.support.ticket')
    related_ticket_ids = fields.One2many(string='Related tickets',
                                         comodel_name='website.support.ticket',
                                         inverse_name='parent_ticket_id')
    delay = fields.Integer(string='Delay')
    other_field_ids = fields.Many2many(comodel_name='website.support.ticket.field', string="Other Details")

    @api.onchange('category')
    def onchange_category(self):
        self.sub_category_id = False

    @api.onchange('sub_category_id')
    def onchange_sub_category(self):
        if self.sub_category_id and self.sub_category_id.additional_field_ids:
            for subc in self.sub_category_id.additional_field_ids:
                self.other_field_ids = [(0, 0,  {'name': subc.name})]

    @api.onchange('priority_id')
    def onchange_priority_id(self):
        self.delay = self.priority_id.delay

    @api.multi
    def write(self, vals):
        if vals.get('state'):
            if self.state.id != 1 and vals['state'] == 1:
                raise exceptions.ValidationError("T'es nul !")
        return super(InheritedWebsiteSupportTickets, self).write(vals)

    @api.model
    def create(self, vals):
        new_id = super(InheritedWebsiteSupportTickets, self).create(vals)

        new_id.ticket_number = new_id.company_id.next_support_ticket_number + 42
        return new_id


class InheritedWebsiteSupportCategory(models.Model):

    _inherit = 'website.support.ticket.subcategory'

    service_id = fields.Many2one(string='Service',
                                 comodel_name='website.support.ticket.service')


class InheritedWebsiteSupportPriority(models.Model):

    _inherit = 'website.support.ticket.priority'

    delay = fields.Integer(string='Delay')


class WebsiteSupportTicketSubCategoryField(models.Model):
    _inherit = "website.support.ticket.subcategory.field"

    type = fields.Selection(selection_add=[('binary', 'Binary'), ('polar', 'Yes / No')])
