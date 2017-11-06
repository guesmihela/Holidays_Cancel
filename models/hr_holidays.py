# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from odoo import models, fields, api
import odoo.addons.decimal_precision as dp
from odoo import netsvc

class hr_holidays(models.Model):
    _inherit = "hr.holidays"
    can_reset = fields.Boolean('Can reset', compute='_compute_can_reset')
    cancel = fields.Boolean('Can Cancel', compute='_compute_can_cancel')
    can_cancel = fields.Boolean('employe can cancel request',related='holiday_status_id.can_cancel')
    @api.multi
    def _compute_can_reset(self):
        """ User can reset a leave request if it is its own leave request
            or if he is an Hr Manager.
        """
        user = self.env.user
        group_hr_manager = self.env.ref('hr_holidays.group_hr_holidays_manager')
        for holiday in self:
            if group_hr_manager in user.groups_id:
                holiday.can_reset = True
    @api.multi
    def _compute_can_cancel(self):
        """ User can reset a leave request if it is its own leave request
            or if he is an Hr Manager.
        """
        user = self.env.user
        for holiday in self:
            if holiday.can_cancel:
                holiday.cancel = True
        return True
    def set_to_draft(self):
        for holiday in self:
            holiday.write({
                'state': 'draft',
                'manager_id': False,
                'manager_id2': False,
            })
            linked_requests = holiday.mapped('linked_request_ids')
            for linked_request in linked_requests:
                linked_request.set_to_draft()
            linked_requests.unlink()
        return True
    
hr_holidays()