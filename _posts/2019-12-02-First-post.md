---
layout: post
title: "Learning Something New: Jekyll"
date: 2019-12-02
categories: tech
mathjax: true
---
This post is about how I set up this Github hosted site using Jekyll on Windows 10.  I'm writing it because I could not find one single place that explained how to start from ground level.

## The Plan
1. Use Windows Subsystem for Linux (WSL) for development.
1. Use the [Tale][tale-url] theme developed by Chester How.
1. Support local preview with Jekyll.

### WSL
If you haven't already, enable WSL from a Powershell with administrator privileges.
{% highlight bash %}
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
{% endhighlight %}

## Theme
Fork the [Tale][tale-url] theme to a repo named `your_username.github.io`.

Then clone it locally.

## Install Ruby v2.6.5
I needed a newer version of Ruby, v2.6.5, than I could readily get from Ubuntu Apt. 
{% highlight shell %}
sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt update
sudo apt-get install ruby2.6 ruby2.6-dev
{% endhighlight %}

Install bundler gem for the user
{% highlight shell %}
gem install --user-install bundler 
{% endhighlight %}

Add local gem executables to PATH
{% highlight shell %}
echo 'export PATH="$HOME/.gem/ruby/2.6.0/bin:$PATH"' >> ~/.bashrc
{% endhighlight %}

## MathJax
Follow the instructions in this blog entry: 
[Adding MathJax to a GitHub Pages Jekyll Blog](http://sgeos.github.io/github/jekyll/2016/08/21/adding_mathjax_to_a_jekyll_github_pages_blog.html)

[tale-url]: https://github.com/chesterhow/tale/