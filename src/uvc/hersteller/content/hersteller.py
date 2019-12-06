# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from uvc.hersteller import _


class IHersteller(model.Schema):
    """ 
    Hersteller von Produkten oder Maschinen
    """

    anschrift1 = schema.TextLine(title = _(u"Anschrift 1"),
            description = _(u"Bitte geben Sie hier die Anschrift des Herstellers ein."),
            required = True,)

    anschrift2 = schema.TextLine(title = _(u"Anschrift 2"),
            description = _(u"Bitte geben Sie hier einen evtl. Adresszusatz des Herstellers ein."),
            required = False,)

    anschrift3 = schema.TextLine(title = _(u"Anschrift 3"),
            description = _(u"Bitte geben Sie hier einen evtl. weiteren Adresszusatz des Herstellers ein."),
            required = False,)

    land = schema.TextLine(title = _("Land"),
            description = _(u"Bitte geben Sie hier das Land des Herstellers ein."),
            required = True,)

    telefon = schema.TextLine(title = _("Telefonnummer"),
            description = _(u"Bitte geben Sie hier die vollständige Telefonnummer mit Ländercode ein,\
                              Beispiel: +49 (0) 30 12345/678"),
            required = True,)

    telefax = schema.TextLine(title = _("Faxnummer"),
            description = _(u"Bitte geben Sie hier die vollständige Telefaxnummer mit Ländercode ein,\
                              Beispiel: +49 (0) 30 12345/777"),
            required = False,)

    email = schema.TextLine(title = _("E-Mail Adresse"),
            description = _(u"Bitte geben Sie hier die E-Mailadresse des Herstellers ein."),
            required = False,)

    homepage = schema.URI(title = _("Hompage"),
            description = _(u"Bitte geben Sie hier die Internetadresse (http://www.example.de)\
                              des Herstellers ein."),
            required = False)

@implementer(IHersteller)
class Hersteller(Container):
    """
    """
