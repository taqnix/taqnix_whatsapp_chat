from odoo import http
from odoo.http import request


class WhatsAppController(http.Controller):

    @http.route('/taqnix_whatsapp/config', type='json', auth='public')
    def get_whatsapp_config(self):
        ICP = request.env['ir.config_parameter'].sudo()
        return {
            'active': ICP.get_param('taqnix_whatsapp_chat.active', 'False').lower() == 'true',
            'phone_number': ICP.get_param('taqnix_whatsapp_chat.phone_number', ''),
            'default_message': ICP.get_param('taqnix_whatsapp_chat.default_message', ''),
            'button_position': ICP.get_param('taqnix_whatsapp_chat.button_position', 'right'),
            'button_color': ICP.get_param('taqnix_whatsapp_chat.button_color', '#25D366'),
            'text_color': ICP.get_param('taqnix_whatsapp_chat.text_color', '#FFFFFF'),
            'button_text': ICP.get_param('taqnix_whatsapp_chat.button_text', 'Chat with Us'),
            'show_on_mobile': ICP.get_param('taqnix_whatsapp_chat.show_on_mobile', 'True').lower() == 'true',
            'show_on_desktop': ICP.get_param('taqnix_whatsapp_chat.show_on_desktop', 'True').lower() == 'true',
        }