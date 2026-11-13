# Catalogue content model

Front-matter keys used by every entry:

- `title` - display name of the component
- `slug` - stable identifier, also used for the companion resource folder name
- `status` - `published` or `draft`
- `summary` - one-line description shown in listings
- `link` - optional URL of the entry's public companion resource
- `benchmark` - optional mapping (`platform`, `entity`, `project`) for an online
  benchmark dashboard

Companion resources for catalogue entries live in this repository under
`companions/<slug>/`. A companion folder is only a released resource when its
README and contents show a shipped implementation; folders that only carry design
notes or a future-work announcement are not released.
