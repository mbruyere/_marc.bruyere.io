---
title: An outright open source approach for simple and pragmatic Internet eXchange

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Marc Bruyère

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2016-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2023-10-18T09:04:26.209973Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: ''
publication_short: ''

doi: ''

abstract: The Internet is indispensable for our life today and for our globalized
  financial economy. The effectiveness of the Internet as a public resource depends
  upon interoperability and trust. Free and open source software promotes the development
  of the Internet as a public resource. Physical location Internet eXchange Points
  (IXP) are highly valuable for the Internet as neutral exchange places where all
  type and size of networks can exchange traffic. The fundamental service offered
  by IXP is a shared layer2 switching fabric. IXPs are fastened by using close source
  technology for their switching fabric. Although this should be a basic functionality,
  today solutions never address their basic requirements properly. Today’s network
  solutions are inflexible as proprietary closed implementation of a distributed control
  plane tight together with the data plane. Software Defined Networking (SDN) is an
  emerging paradigm decoupling the control and data planes, on opening high performance
  forwarding plane with OpenFlow. The goal of this thesis is to propose an IXP pragmatic
  Openflow switching fabric, addressing the critical requirements and affording greater
  simplicity and flexibility. Few SDN solutions have been presented already but all
  of them propose fuzzy layer 2 and 3 separation. For a enhanced stability not all
  control planes functions can be decoupled from the data plane. As an other goal
  statement, networking testing tools are essential for qualifying networking equipment.
  Network hardware monitoring and testing being critical for computer networks, current
  solutions are both very expensive, inflexible and not open source. The experience
  in deploying Openflow in production networks has highlight significant limitations
  in the support of the protocol by hardware switches. Open source hardware solutions
  give total flexibility and reproducibility for testing and selecting suitable hardware
  equipment to go to production. We present Umbrella, a new SDN-enabled IXP fabric
  architecture, that aims to promote strengthening the separation of control and data
  plane to increase robustness, flexibility and reliability of the IXP. Umbrella abolishes
  broadcasting with a pseudo wire and segment routing approach. We demonstrated for
  an IXP fabric that not all the control plane can be decoupled from the date plane.
  We show that Umbrella can scale and recycle legacy non OpenFlow core switch to reduce
  migration cost. Into the testing tools lacuna we launch the Open Source Network
  Tester (OSNT), a fully open-source traffic generator and capture system. Additionally,
  our approach has proved less costly than comparable commercial systems while achieving
  comparable levels of precision and accuracy; all within an open-source framework
  extensible with new features to support new applications, while permitting validation
  and review of the implementation. Furthermore we present the integration of OpenFLow
  Operations Per Second (OFLOPS), an OpenFlow switch evaluation platform, with the
  OSNT platform, a hardware-accelerated traffic generation and capturing platform.
  We demonstrate the real flexibility and benefit of the Umbrella architecture persuading
  ten Internet operators to migrate the entire Toulouse IXP. The hardware testing
  tools we have developed have been used to qualify the hardware which has been deployed
  in production. The TouIX has been running stable for a year. It is fully managed
  and monitored through a single web application removing all the complex legacy management
  systems.

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
