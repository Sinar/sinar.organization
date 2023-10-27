# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from sinar.organization import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider
from plone.schema import Email


class IContactDetailsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IContactDetails(model.Schema):
    """
    """

    contact_website = schema.URI(
        title=_(u'Website'),
        required=False,
    )

    contact_email = Email(
        title=_(u'Email address'),
        required=False,
    )

    contact_address = schema.Text(
        title=_(u'Address'),
        required=False,
    )

    contact_number = schema.TextLine(
        title=_(u'Phone number'),
        required=False,
    )

    contact_mobile = schema.TextLine(
        title=_(u'Mobile phone number'),
        required=False,
    )

    contact_social_facebook = schema.URI(
        title=_(u'Facebook page/profile'),
        required=False,
    )

    contact_social_x = schema.URI(
        title=_(u'X (formerly known as Twitter) profile'),
        required=False,
    )

    contact_social_youtube = schema.URI(
    title=_(u'Youtube channel'),
    required=False,
    )

    contact_social_instagram = schema.URI(
    title=_(u'Instagram profile'),
    required=False,
    )

@implementer(IContactDetails)
@adapter(IContactDetailsMarker)
class ContactDetails(object):
    def __init__(self, context):
        self.context = context

    @property
    def contact_website(self):
        if safe_hasattr(self.context, 'contact_website'):
            return self.context.contact_website
        return None

    @contact_website.setter
    def contact_website(self, value):
        self.context.contact_website = value

    @property
    def contact_email(self):
        if safe_hasattr(self.context, 'contact_email'):
            return self.context.contact_email
        return None

    @contact_email.setter
    def contact_email(self, value):
        self.context.contact_email = value

    @property
    def contact_address(self):
        if safe_hasattr(self.context, 'contact_address'):
            return self.context.contact_address
        return None

    @contact_address.setter
    def contact_address(self, value):
        self.context.contact_address = value

    @property
    def contact_number(self):
        if safe_hasattr(self.context, 'contact_number'):
            return self.context.contact_number
        return None

    @contact_number.setter
    def contact_number(self, value):
        self.context.contact_number = value

    @property
    def contact_mobile(self):
        if safe_hasattr(self.context, 'contact_mobile'):
            return self.context.contact_mobile
        return None

    @contact_mobile.setter
    def contact_mobile(self, value):
        self.context.contact_mobile = value

    @property
    def contact_social_facebook(self):
        if safe_hasattr(self.context, 'contact_social_facebook'):
            return self.context.contact_social_facebook
        return None

    @contact_social_facebook.setter
    def contact_social_facebook(self, value):
        self.context.contact_social_facebook = value

    @property
    def contact_social_x(self):
        if safe_hasattr(self.context, 'contact_social_x'):
            return self.context.contact_social_x
        return None

    @contact_social_x.setter
    def contact_social_x(self, value):
        self.context.contact_social_x = value

    @property
    def contact_social_youtube(self):
        if safe_hasattr(self.context, 'contact_social_youtube'):
            return self.context.contact_social_youtube
        return None

    @contact_social_youtube.setter
    def contact_social_youtube(self, value):
        self.context.contact_social_youtube = value

    @property
    def contact_social_instagram(self):
        if safe_hasattr(self.context, 'contact_social_instagram'):
            return self.context.contact_social_instagram
        return None

    @contact_social_instagram.setter
    def contact_social_instagram(self, value):
        self.context.contact_social_instagram = value