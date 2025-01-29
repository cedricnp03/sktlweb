---
---



{% include section.html %}

Welcome to the home page of Sakti Lab. We're a molecular simulation laboratory  at the [Department of Chem. and Biochem](http://www.chem.waseda.ac.jp/ja/index-e.html) at [Waseda University](https://www.waseda.jp/top/en/) in Tokyo, Japan. We use theoretical and computational methods such as our in-house `CMMDE.py` program alongside with other computational techniques to uncover the underlying mechanisms and workings of how chemistry influences our world. Currently, our research focus lies in ion batteries, catalysts (homogeneous and heterogeneous), drug design, cosmetics, and condensed-phase materials.


{% capture text %}

We are interested in how to design batteries, catalysts, drugs and other materials that can propel us into a more sustainable and safer world.

{%
  include button.html
  link="publication"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/projects/homogeneous_cat.png"
  link="publication"
  title="Our Research"
  text=text
%}

{% capture text %}

Another way to get to know what we do is to take a quick glance into what kind of topics we are currently focusing on!

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
  image="images/projects/zeolite.png"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

Our team is made up of undergraduate students, master students, and PhD students, and we come from backgrounds ranging from experimental organic chemistry to computer science. Meet the team!

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
  image="images/group_picture.png"
  link="team"
  title="Our team"
  text=text
%}
