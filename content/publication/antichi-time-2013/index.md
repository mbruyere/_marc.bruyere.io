---
title: Time structure analysis of the LHCb DAQ network

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Gianni Antichi
- Marc Bruyère
- Daniel Campora Perez
- Guoming Liu
- Niko Neufeld
- Philippe Owezarski
- Andrew W Moore
- Stefano Giordano

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2013-10-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2023-10-18T09:04:26.284881Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Computing in High Energy and Nuclear Physics (CHEP)*'
publication_short: ''

doi: ''

abstract: The LHCb DAQ Network is a real time high performance network, in which 350
  data sources send data over a Gigabit Ethernet LAN to more than 1500 receiving nodes.
  The aggregated throughput of the application, called Event Building, is more than
  60 Gbps. The protocol employed by LHCb makes the sending nodes transmit simultaneously
  portions of events to one receiving node at a time, which is selected using a credit-token
  scheme. The resulting traffic is very bursty and sensitive to irregularities in
  the temporal distribution of packet-bursts to the same destination or region of
  the network. In order to study the relevant properties of such a dataflow, a non-disruptive
  monitoring setup based on a networking capable FPGA (Netfpga) has been deployed.
  The Netfpga allows order of hundred nano-second precise time-stamping of packets.
  We study in detail the timing structure of the Event Building communication, and
  we identify potential effects of micro-bursts like buffer packet drops or jitter.

# Summary. An optional shortened abstract.
summary: ''

tags:
- latency
- measurement
- CERN
- LHCb
- NetfPGA

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
  url: https://hal.science/hal-00908383
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
