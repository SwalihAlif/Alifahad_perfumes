# utils.py
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings

def generate_invoice(order):
    template_path = 'user/invoice_template.html'
    context = {'order': order}
    
    template = get_template(template_path)
    html = template.render(context)
    
    result = open(os.path.join(settings.MEDIA_ROOT, f'invoices/invoice_{order.serial_number}.pdf'), 'wb')
    pdf = pisa.pisaDocument(html.encode('UTF-8'), dest=result)
    result.close()
    
    if pdf.err:
        return None
    return result.name
