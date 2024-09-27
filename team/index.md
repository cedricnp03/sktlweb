---
title: Team
nav:
  order: 2
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team


{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi, group:" %}
{% include list.html data="members" component="portrait" filters="role: resfel, group:" %}
{% include list.html data="members" component="portrait" filters="role: postdoc, group:" %}
{% include list.html data="members" component="portrait" filters="role: phd, group:" %}
{% include list.html data="members" component="portrait" filters="role: masters, group:" %}
{% include list.html data="members" component="portrait" filters="role: undergrad, group:" %}


{% include section.html %}

{% include button.html icon="fa-solid fa-handshake-angle" text="Join the Team" link="join" style="button" %}

{% include section.html %}

## Affiliates

{% include list.html data="members" component="portrait" filters="role: pi, group: affiliates" style="small" %}
{% include list.html data="members" component="portrait" filters="role: prof, group: affiliates" style="small" %}
{% include list.html data="members" component="portrait" filters="role: postdoc, group: affiliates" style="small" %}


{% include section.html %}

## Alumni

{% include list.html data="members" component="portrait" filters="role: pi, group: alumni" %}
{% include list.html data="members" component="portrait" filters="role: fellow, group: alumni" %}
{% include list.html data="members" component="portrait" filters="role: postdoc, group: alumni" %}
{% include list.html data="members" component="portrait" filters="role: phd, group: alumni" %}