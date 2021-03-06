# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests
from datetime import date

import logging

_logger = logging.getLogger(__name__)


class employeepenalty(models.Model):
    _name = 'employee.penalty'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'x_employee_id'

    x_employee_id = fields.Many2one('hr.employee', string="Employee", store=True,
                                     tracking=True, index=True)

    x_notes = fields.Text(string="Notes", tracking=True, store=True)

    x_penalty_id = fields.Many2one('penalty.type', string="Penalty", store=True,
                                     tracking=True, index=True)

    x_status = fields.Selection(
        [('New', 'New'), ('Submit', 'Submit'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled')],
        string="Status", store=True, 
        index=True, tracking=True, default='New')

    x_penalty_date = fields.Date(string='Penalty Date', index=True, tracking=True)
