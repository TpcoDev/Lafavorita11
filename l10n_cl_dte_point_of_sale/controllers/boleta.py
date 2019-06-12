# -*- coding: utf-8 -*-

from odoo.http import request
from odoo.addons.web.controllers.main import serialize_exception
from odoo.tools.misc import formatLang
from odoo.addons.l10n_cl_fe.controllers.boleta import Boleta
from odoo import http
import json
import logging
_logger = logging.getLogger(__name__)

class PosOrderController(http.Controller):
    @http.route('/get_order_by_pos_reference/<pos_reference>', type='json', auth="user")
    def get_order_by_pos_reference(self, pos_reference, **kwargs):
       pos_fields = ['sii_document_number','sequence_id']
       result = http.request.env["pos.order"].search_read([('pos_reference', '=', pos_reference)], pos_fields, limit=1, order="id desc")
       if len(result) == 0:
           return json.dumps({})
       result = result[0]
       if len(result["sequence_id"]) == 0:
           result["sequence_id"] = {}
       elif len(result["sequence_id"]) == 2:
           r_sequence = http.request.env["ir.sequence"].search_read([('id', '=', int(result["sequence_id"][0]))], ['sii_document_class_id'], limit=1)
           if len(r_sequence) == 0:
               result["sequence_id"] = {}
           else:
               r_sequence = r_sequence[0]
               r_sii_document_class = http.request.env["sii.document_class"].search_read([('id', '=', int(r_sequence['sii_document_class_id'][0]))], ['name'], limit=1)
               if len(r_sii_document_class) == 0:
                   result["sequence_id"] = {'sii_document_class_id': {}}
               else:
                   r_sii_document_class = r_sii_document_class[0]
                   result["sequence_id"] = {'sii_document_class_id': {'name': r_sii_document_class['name']}}

       return json.dumps(result)

class POSBoleta(Boleta):

    def _get_domain_pos_order(self, folio, post_values):
        domain = [('sii_document_number', '=', int(folio))]
        #if post.get('date_invoice', ''):
        #    domain.append(('date_order','=',post.get('date_invoice', '')))
        #if post.get('amount_total', ''):
        #    domain.append(('amount_total','=',float(post.get('amount_total', ''))))
        if post_values.get('sii_codigo', ''):
            domain.append(('document_class_id.sii_code', '=', int(post_values.get('sii_codigo', ''))))
        else:
            domain.append(('document_class_id.sii_code', 'in', [39, 41] ))
        return domain

    def get_orders(self, folio, post):
        orders = super(POSBoleta, self).get_orders(folio, post)
        if not orders:
            Model = request.env['pos.order'].sudo()
            domain = self._get_domain_pos_order(folio, post)
            orders = Model.search(domain, limit=1)
        return orders

    def _get_report(self, document):
        if document._name == 'pos.order':
            return request.env.ref('l10n_cl_dte_point_of_sale.action_report_pos_boleta_ticket').sudo().render_qweb_pdf([document.id])[0]
        return super(POSBoleta, self)._get_report(document)
