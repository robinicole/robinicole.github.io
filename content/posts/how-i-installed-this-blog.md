---
keywords:
 - hugo
 - static site generator
 - blog setup
 - tranquilpeak theme
clearReading: true
autoThumbnailImage: yes
metaAlignment: center
comments: false
showTags: true
showPagination: true
showSocial: true
showDate: true
summary: "A step-by-step guide on setting up a blog using Hugo and the Tranquilpeak theme, with tips on customization and theme management."
title: "Creating a Blog with Hugo and Tranquilpeak Theme"
---

# Setting Up a Blog with Hugo and Tranquilpeak Theme

In this guide, we'll walk through the process of creating a blog using the Hugo static site generator and the Tranquilpeak theme. We'll cover the basic setup, theme installation, and some customization tips to help you get started.

## Step 1: Install Hugo and Create a New Site

First, follow the [official Hugo quick start instructions](https://gohugo.io/getting-started/quick-start/) to install Hugo and create a new site. Once you have completed the initial setup, serve your site locally using the following command:

```bash
hugo server --disableFastRender
```
This command will build your site and make it available at [http://localhost:1313/](http://localhost:1313/) 

## Installing Tranquilpeak
This I installed the [TranquikPeak](https://github.com/kakawait/hugo-tranquilpeak-theme) which is my favourite one so fare. By cloning it into the theme
```bash
git submodule add https://github.com/kakawait/hugo-tranquilpeak-theme.git themes/hugo-tranquilpeak-theme 
```
and activated by modifying the `theme` variable in the `hugo.toml` file
I am not a fan of the cover image of tranquilpaeak which does not render well on the white characters as you can see on the [demo of theme here](https://tranquilpeak.kakawait.com/) so I made it darker with Imagemagic 
```bash
convert themes/hugo-tranquilpeak-theme/static/images/cover.jpg -modulate 50,100,100 assets/images/cover.jpg
```


