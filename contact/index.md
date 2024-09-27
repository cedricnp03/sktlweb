---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

Our lab is part of the Department of Chemistry and Biochemistry at Waseda University. We're based in the Nishiwaseda campus, in room 60-211. If you're interested in collaborating, joining our lab, or you're just interested in knowing more about our research, please feel free to reach out!

{%
  include button.html
  type="email"
  text="aditya@aoni.waseda.jp"
  link="aditya@aoni.waseda.jp"
%}

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/7AQAK3twM2V9h1ah8"
%}

{%
  include figure.html
  image="images/nishiwaseda.png"
  width ="600px"
%}

{% capture col1 %}

{% include figure.html image="images/gallery/87850.jpg" %}

{% endcapture %}

{% capture col2 %}

{% include figure.html image="images/gallery/87847.jpg" %}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% capture col3 %}

{% include figure.html image="images/gallery/87845.jpg" %}

{% endcapture %}

{% capture col4 %}

{% include figure.html image="images/gallery/87855.jpg" %}

{% endcapture %}

{% include cols.html col1=col3 col2=col4 %}