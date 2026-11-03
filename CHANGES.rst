Changelog
=========


1.0a1 (unreleased)
------------------

- Register organization-view as an available view method of the
  Organization type, so the custom default view is offered in the
  view selector and can be re-selected after switching away.
  [kaerumy]

- Add post install and upgrade steps that repair the Organization
  FTI on sites installed with the previous (broken) configuration.
  [kaerumy]

- Remove the duplicate organization-view browser page registration
  that leaked the view to all folderish content without the browser
  layer.
  [kaerumy]

- Initial release.
  [kaerumy]
