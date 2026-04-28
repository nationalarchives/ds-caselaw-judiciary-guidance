# The National Archives: Find Case Law

## Introduction

This repository is part of the [Find Case Law](https://caselaw.nationalarchives.gov.uk/) project at [The National Archives](https://www.nationalarchives.gov.uk/). For more information on the project, check [the documentation](https://github.com/nationalarchives/ds-find-caselaw-docs).

# Judiciary Guidance

This repository contains advice and notes to help the judiciary deliver judgments to the Find Case Law service.

## Updating this guidance

### Content

All content for this guidance minisite is kept in the `content` folder as HTML files. These contain a very minimalistic `<head>` element with a `<title>`, and the content itself lives in the `<body>` element. You do not need to include any additional markup for the site layout such as header, menu or footers.

### Menus

The site's menus are defined in the `NAV_STRUCTURE` constant in `pelicanconf.py`

### Templates

Templates for this minisite (including overall page layout, header, menus and footer) are kept in the `theme/templates` folder.

The bulk of the layout is defined in `base.html`. `page.html` provides additional behaviour around page titles.

## Deployment

<!-- last_review: 2026-04-13 -->

This documentation is automatically deployed to [GitHub Pages](https://nationalarchives.github.io/ds-caselaw-judiciary-guidance/) from `main`.
