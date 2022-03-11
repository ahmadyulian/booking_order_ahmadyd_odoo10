import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, exceptions, _
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class CancelOrder(models.TransientModel):
    _name = "cancel.workorder"

    #oftxt
    note = fields.Text('Note')

    def cancelled(self):
        cancel = self.env['work.order'].browse(self.env.context['active_id'])
        cancel_create = cancel.update({'note': self.note, 'state': 'cancelled'})
