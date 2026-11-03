# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

# FTI properties that register the custom default view of the Organization
# type.  These are imported by the default profile, but we enforce them
# explicitly in the install and upgrade steps so that sites where the FTI
# was already installed with the wrong values get repaired.
DEFAULT_VIEW = 'organization-view'
VIEW_METHODS = ('view', DEFAULT_VIEW)


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'sinar.organization:uninstall',
        ]


def fix_organization_fti(portal):
    """Make sure the Organization FTI registers organization-view
    as its default view and as an available view method.

    Without organization-view in the FTI's view_methods, the custom
    default view is not offered in the view selector, so content can
    be switched to the generic DX view but never switched back.
    """
    types = getattr(portal, 'portal_types', None)
    if types is None:
        return
    fti = types.get('Organization')
    if fti is None:
        return

    if fti.default_view != DEFAULT_VIEW:
        fti.default_view = DEFAULT_VIEW
    if fti.default_view_fallback:
        fti.default_view_fallback = False
    if fti.immediate_view != 'view':
        fti.immediate_view = 'view'

    view_methods = list(fti.view_methods or ())
    for view in VIEW_METHODS:
        if view not in view_methods:
            view_methods.append(view)
    fti.view_methods = tuple(view_methods)


def _get_site(context):
    """The context of a profile handler or upgrade step is the
    portal_setup tool of the site being installed/upgraded."""
    return getToolByName(context, 'portal_url').getPortalObject()


def post_install(context):
    """Post install script"""
    # Register the Organization default view on the FTI, in case the
    # type information was imported with stale values.
    fix_organization_fti(_get_site(context))


def upgrade_to_1001(context):
    """Upgrade step to 1001: register organization-view as an
    available view method of the Organization type on sites that
    were installed with the broken FTI configuration."""
    fix_organization_fti(_get_site(context))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
