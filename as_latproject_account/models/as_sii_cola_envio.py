# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.tools.translate import _
import ast
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTF
import logging
_logger = logging.getLogger(__name__)


class ColaEnvio(models.Model):
    _inherit = "sii.cola_envio"

    @api.model
    def _getIDs(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        # docs = self.env[self.model].sudo(self.user_id.id).browse(ast.literal_eval(self.doc_ids))
        # active_ids = docs.ids if docs else []
        return [(6, 0, active_ids)]

    documentos = fields.Many2many('account.invoice', string="Movimientos", default=_getIDs)