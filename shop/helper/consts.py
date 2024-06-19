from django.utils.translation import gettext_lazy as _

TRANSACTION_STATUS = [
    ('submitted', _('Submitted')),
    ('packing', _('Packing')),
    ('cargo_line', _('Cargo Line')),
    ('sent', _('Sent')),
    ('delivered', _('Delivered')),
]
