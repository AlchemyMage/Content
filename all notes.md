---
layout: base
---

# all notes


<ul>
    {% for page in site.pages %}
        {% if page.layout == 'notes' and page.title %}
            <li><a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a></li>
        {% endif %}
    {% endfor %}
</ul>