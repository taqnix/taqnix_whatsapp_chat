{
    'name': 'Website Floating Icon Button for WhatsApp, Messenger, SMS, Instagram, Telegram & More',
        'version': '18.0.1.1.1',
    'summary': 'Add a configurable floating chat/contact button for WhatsApp, Messenger, Email, SMS, Instagram, and more on your website',
    'description': """
        Add a customizable floating contact/chat button to your Odoo website for platforms like WhatsApp, Messenger, Email, SMS, Instagram, Telegram, and more.
        🔧 Features:
        - Fully customizable floating button
        - Supports multiple platforms:
          • WhatsApp
          • Facebook Messenger
          • Email (mailto)
          • SMS
          • Instagram
          • Telegram
          • Direct phone call (tel)
        - Set the link and default message per platform
        - Choose Font Awesome icon classes:
          • WhatsApp: `fa-whatsapp`
          • Email: `fa-envelope`
          • SMS: `fa-comment`
          • Instagram: `fa-instagram`
          • Facebook Messenger: `fa-facebook-messenger`
          • Telegram: `fa-telegram`
          • Phone Call: `fa-phone`
        - Customize button position (left/right/bottom)
        - Control visibility on desktop and mobile separately
        - Configure background, text, and icon colors
        - Enable or disable the button from Website Settings
        - Mobile-responsive design
        """,
    'author': 'Taqnix',
    'website': 'https://www.taqnix.com',
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'price': 100.00,
    'currency': 'USD',
    'assets': {
        'web.assets_frontend': [
            'taqnix_whatsapp_chat/static/src/js/whatsapp_button.js',
            'taqnix_whatsapp_chat/static/src/scss/whatsapp_button.scss',
        ],
    },
}
