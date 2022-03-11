from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
import logging

_logger = logging.getLogger(__name__)

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'service time'

    #ofchar
    name = fields.Char(string='Nama Tim', required=True)

    #ofm2o
    team_leader = fields.Many2one('res.users', 
    string='Ketua Tim',  
    required=True)
    
    #ofm2m
    team_member = fields.Many2many('res.users', 
    string='Anggota Tim')