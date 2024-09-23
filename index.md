---
---



{% include section.html %}

Welcome to the home page of Sakti Lab. We're a molecular simulation laboratory  at the [Department of Chem. and Biochem](http://www.chem.waseda.ac.jp/ja/index-e.html) at [Waseda University](https://www.waseda.jp/top/en/) in Tokyo, Japan. We use theoretical and computational methods such as our in-house CMMDE program alongside with other computational techniques to uncover the underlying mechanisms and workings of how chemistry influences our world. Currently, our research focus lies in ion batteries, catalysts (homogeneous and heterogeneous), drug design, cosmetics, and condensed-phase materials.


{% capture text %}

We are interested in how to design batteries, catalysts, drugs and other materials that can propell us into a more sustainable and safer world.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Our team is made up of undergraduate students, master students, PhD students, and programmers, and we come from backgrounds ranging from experimental organic chemistry to computer science. Meet the team!

{%
  include button.html
  link="team"
  text="Learn more about us"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Who we are"
  text=text
%}
