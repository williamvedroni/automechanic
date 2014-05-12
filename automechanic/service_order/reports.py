# coding:utf-8
from geraldo import Report
from reportlab.lib.units import cm
from geraldo.base import ReportBand
from geraldo.widgets import ObjectValue, SystemField, Label
from geraldo.utils import BAND_WIDTH
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from django.utils.formats import number_format


class ReportServiceOrder(Report):
    title = u'Ordens de Serviço'
    author = u'Automechanic'
    margin_left = 2 * cm
    margin_top = 0.5 * cm
    margin_right = 0.5 * cm
    margin_bottom = 0.5 * cm

    class band_detail(ReportBand):
        height = 0.5 * cm
        elements = (
                    ObjectValue(attribute_name='id', left=0.5 * cm),
                    ObjectValue(attribute_name='vehicle', left=3.5 * cm),
                    ObjectValue(attribute_name='service_rating', left=8.5 * cm,
                                get_value=lambda instance: number_format(instance.service_rating)),
                    ObjectValue(attribute_name='created', left=11.5 * cm,
                    get_value=lambda instance: instance.created.strftime('%m/%d/%Y')),
        )

    class band_page_header(ReportBand):
        height = 1.3 * cm
        elements = [
                SystemField(expression='%(report_title)s', top=0.1 * cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                Label(text="ID", top=0.8 * cm, left=0.5 * cm),
                Label(text=u"Carro", top=0.8 * cm, left=3.5 * cm),
                Label(text=u"Valor", top=0.8 * cm, left=8.5 * cm),
                Label(text=u"Data de Criação", top=0.8 * cm, left=11.5 * cm),
                SystemField(expression=u'Página %(page_number)d de %(page_count)d', top=0.1 * cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'bottom': True}

    class band_page_footer(ReportBand):
        height = 0.5 * cm
        elements = [
                Label(text='Automechanic Reports', top=0.1 * cm),
                SystemField(expression=u'Gerado em %(now:%d/%m/%Y)s as %(now:%H:%M)s', top=0.1 * cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
        borders = {'top': True}
