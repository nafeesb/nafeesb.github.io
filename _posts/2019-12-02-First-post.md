---
layout: post
title: "Learning Something New: Jekyll"
date: 2019-12-02
categories: tech
mathjax: true
description: How to setup Jekyll for github pages on Windows 10 WSL.
---
This post is about how I set up this Github hosted site using Jekyll on Windows 10.  Jekyll is not officially supported on Windows, but it's totally possible to get it to work.  I'm writing this up because I could not find one single place that explained how to start from ground level.

## The Plan
1. Use Windows Subsystem for Linux (WSL) for development.
2. Use the [Tale][tale-url] theme developed by Chester How.
3. Support local preview with Jekyll.

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

Install bundler gem for the user. I am deliberately installing to the user, because I don't like the idea of installing a bunch of gems to the system.  However this means that we have to use some additional commandline arguments in subsequent steps.
{% highlight shell %}
gem install --user-install bundler 
{% endhighlight %}

Add local gem executables to PATH
{% highlight shell %}
echo 'export PATH="$HOME/.gem/ruby/2.6.0/bin:$PATH"' >> ~/.bashrc
exec $SHELL
{% endhighlight %}

## Jekyll
Jekyll does the work of creating the site. How it works with GitHub is explained in more detail in [Setting up a GitHub Pages site with Jekyll](https://help.github.com/en/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll).

Go to the directory where you cloned the website repo.

Modify `Gemfile` file to look like this:
{% highlight ruby %}
source "https://rubygems.org"
gem 'github-pages', group: :jekyll_plugins
{% endhighlight %}

Install required packages, including Jekyll.
```shell
bundle install --path ~/.gem
```

## Ready to rock
Run the local Jekyll preview.
```shell
bundle exec jekyll serve
```
You should be able to connect to http://127.0.0.1:4000 and see your website.

## Publish
Stage and commit your changes. Push to GitHub, and your website will be available in a few minutes.

## MathJax
If you want to render equations, you need MathJax. Follow the instructions in this blog entry: 
[Adding MathJax to a GitHub Pages Jekyll Blog](http://sgeos.github.io/github/jekyll/2016/08/21/adding_mathjax_to_a_jekyll_github_pages_blog.html)

[tale-url]: https://github.com/chesterhow/tale/