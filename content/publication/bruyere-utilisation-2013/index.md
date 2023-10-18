---
title: Utilisation d'OpenFlow et des modules Splite Data Plane de DELL pour traiter
  le DUID-MAC-spoofing des requêtes DHCPv6

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Marc Bruyère
- David Delavennat

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2013-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2023-10-18T09:04:26.251443Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: ''
publication_short: ''

doi: ''

abstract: IPv6 a longtemps été associé à un mécanisme d’auto-configuration sans-état
  (Router Advertisements). La mise à disposition tardive d’une implémentation de protocole
  d’attribution d’adresses IPv6, avec-état, par l’ISC, a été un frein à son déploiement
  sur un parc de postes clients « administrés ». Cependant, l’arrivée du protocole
  DHCPv6 ne se fait pas sans soulever de nouvelles difficultés opérationnelles. Dans
  les environnements à double pile IP, le fait que DHCPv4 et DHCPv6 n’utilisent pas
  les mêmes attributs pour identifier les objets IP ( MAC dans le premier cas, DUID
  dans le second ), complique la tâches des ASR (plusieurs variantes de DUID coexistent)
  et rend problématique la corrélation des adressages au sein des journaux d’activités
  réseaux. Une implantation de serveur DHCPv6 est disponible, autorisant le référencement
  d’objets IP par leurs adresses MAC, i.e. ne tenant pas compte de l’attribut DUID.
  Nous souhaitons toutefois pouvoir utiliser notre infrastructure DHCPv6 ISC préexistante,
  qui, elle, ne supporte que les attributs DUID, tout en référençant nos postes clients
  par leurs adresses MAC, peu importe la version du protocole DHCP. Cette contrainte
  peut être résolue en utilisant un mécanisme embarqué au sein des modules Split Data
  Plane des commutateurs DELL SDN de nouvelle génération. Ces modules embarquent des
  applicatifs métiers au sein des commutateurs afin de réaliser des opérations au
  plus près du réseau.

# Summary. An optional shortened abstract.
summary: ''

tags: []

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
