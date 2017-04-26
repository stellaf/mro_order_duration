# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2013-2017 CodUP (<http://codup.com>).
#
##############################################################################

import time
from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp


class mro_order(models.Model):
    """
    add duration on Maintenance Orders, so that we can drag calendar
    """
    _inherit = 'mro.order'
    order_duration = fields.Float(string='Duration', store=True, default=1.0)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
