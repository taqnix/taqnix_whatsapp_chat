from odoo import models, fields, api

class Website(models.Model):
    _inherit = 'website'

    # WhatsApp Configuration Fields
    taqnix_whatsapp_active = fields.Boolean(
        string="Enable Floating Chat Button",
        default=True
    )
    taqnix_whatsapp_link = fields.Char(
        string="Contact Link"
    )
    taqnix_whatsapp_default_message = fields.Char(
        string="Default Message"
    )
    taqnix_whatsapp_button_position = fields.Selection([
        ('left', 'Left'),
        ('right', 'Right')
    ], string="Button Position",
        default='right'
    )
    taqnix_whatsapp_button_color = fields.Char(
        string="Button Color",
        default='#25D366'
    )
    taqnix_whatsapp_text_color = fields.Char(
        string="Text Color",
        default='#FFFFFF'
    )
    taqnix_whatsapp_icon_color = fields.Char(
        string="Icon Color",
        default='#FFFFFF'
    )
    taqnix_whatsapp_button_text = fields.Char(
        string="Button Text",
        default='Chat with Us',
        translate=True
    )
    taqnix_whatsapp_show_on_mobile = fields.Boolean(
        string="Show on Mobile",
        default=True
    )
    taqnix_whatsapp_show_on_desktop = fields.Boolean(
        string="Show on Desktop",
        default=True
    )
    taqnix_whatsapp_button_icon = fields.Char(
        string="Button Icon",
        default='fa-whatsapp',
        help="Font Awesome icon class (e.g., 'fa-whatsapp', 'fa-comment')"
    )

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_id = fields.Many2one('website', string='Website', ondelete='cascade')

    # Related fields for website-specific configurations
    taqnix_whatsapp_active = fields.Boolean(
        related='website_id.taqnix_whatsapp_active',
        string="Enable Floating Chat Button",
        readonly=False,
        default=True
    )
    taqnix_whatsapp_link = fields.Char(
        related='website_id.taqnix_whatsapp_link',
        string="Link",
        readonly=False
    )
    taqnix_whatsapp_default_message = fields.Char(
        related='website_id.taqnix_whatsapp_default_message',
        string="Default Message",
        readonly=False
    )
    taqnix_whatsapp_button_position = fields.Selection(
        related='website_id.taqnix_whatsapp_button_position',
        string="Button Position",
        readonly=False
    )
    taqnix_whatsapp_button_color = fields.Char(
        related='website_id.taqnix_whatsapp_button_color',
        string="Button Color",
        readonly=False
    )
    taqnix_whatsapp_text_color = fields.Char(
        related='website_id.taqnix_whatsapp_text_color',
        string="Text Color",
        readonly=False
    )
    taqnix_whatsapp_icon_color = fields.Char(
        related='website_id.taqnix_whatsapp_icon_color',
        string="Icon Color",
        readonly=False
    )
    taqnix_whatsapp_button_text = fields.Char(
        related='website_id.taqnix_whatsapp_button_text',
        string="Button Text",
        readonly=False,
        translate=True
    )
    taqnix_whatsapp_show_on_mobile = fields.Boolean(
        related='website_id.taqnix_whatsapp_show_on_mobile',
        string="Show on Mobile",
        readonly=False
    )
    taqnix_whatsapp_show_on_desktop = fields.Boolean(
        related='website_id.taqnix_whatsapp_show_on_desktop',
        string="Show on Desktop",
        readonly=False
    )
    taqnix_whatsapp_button_icon = fields.Char(
        related='website_id.taqnix_whatsapp_button_icon',
        string="Button Icon",
        readonly=False
    )