---
layout: default
permalink: /publications/
---
<div class="catalogue">
{% for pub in site.publications reversed %}
    <a href="{{ pub.url | prepend: site.baseurl }}" class="catalogue-item">
        <div>
            <h1 class="catalogue-title">{{ pub.title }}</h1>
            <p class="catalogue-author">{{ pub.authors }}</p>
            <div class="catalogue-line"></div>
            <p>
            {{ pub.content | strip_html | truncatewords: 30 }}
            </p>

        </div>
    </a>
{% endfor %}
</div>