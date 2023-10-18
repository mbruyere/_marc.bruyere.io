---
title: Learning-based Incast Performance Inference in Software-Defined Data Centers

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Kokouvi Benoit Nougnanke
- Yann Labit
- Marc Bruyere
- Simone Ferlin
- Ulrich Aivodji

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2021-03-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2023-10-18T09:04:26.289594Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*2021 24th Conference on Innovation in Clouds, Internet and Networks
  and Workshops (ICIN)*'
publication_short: ''

doi: 10.1109/ICIN51074.2021.9385546

abstract: Incast trafﬁc is a many-to-one communication pattern used in many applications,
  including distributed storage, web-search with partition/aggregation design pattern,
  and MapReduce, commonly in data centers. It is generally composed of short-lived
  ﬂows that may be queued behind large ﬂows’ packets in congested switches where performance
  degradation is observed. Smart buffering at the switch level is sensed to mitigate
  this issue by automatically and dynamically adapting to trafﬁc conditions changes
  in the highly dynamic data center environment. But for this dynamic and smart buffer
  management to become effectively beneﬁcial for all the trafﬁc, and especially for
  incast the most critical one, incast performance models that provide insights on
  how various factors affect it are needed. The literature lacks these types of models.
  The existing ones are analytical models, which are either tightly coupled with a
  particular protocol version or speciﬁc to certain empirical data. Motivated by this
  observation, we propose a machine-learning-based incast performance inference. With
  this prediction capability, smart buffering scheme or other QoS optimization algorithms
  could anticipate and efﬁciently optimize system parameters adjustment to achieve
  optimal performance. Since applying machine learning to networks managed in a distributed
  fashion is hard, the prediction mechanism will be deployed on an SDN control plane.
  We could then take advantage of SDN’s centralized global view, its telemetry capabilities,
  and its management ﬂexibility.

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
links:
- name: URL
  url: https://ieeexplore.ieee.org/document/9385546/
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
