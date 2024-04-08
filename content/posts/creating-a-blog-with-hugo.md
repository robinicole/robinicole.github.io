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
lastmod: 2024-04-06
---
When it comes to creating a blog, popular platforms like WordPress and Wix offer user-friendly interfaces and a wide range of features. However, as a developper I prioritize simplicity, performance, and flexibility.  The combination of Hugo and GitHub presents ticked all those boxes. Hugo, is a static site generator which allows to create blogs by generating static HTML files from your content, eliminating the need for server-side processing and database queries.

In this first, we'll walk through the process of creating this blog using the Hugo static site generator and the Tranquilpeak theme. We'll cover the basic setup, theme installation, and some customization tips to help you get started.

# Setting Up a Blog with Hugo and Tranquilpeak Theme

## Step 1: Install Hugo and Create a New Site

This first step is to have a functioning blog with a basix theme. To do so I followed the [official Hugo quick start instructions](https://gohugo.io/getting-started/quick-start/) to install Hugo and create a new site. Once you have completed the initial setup, serve your site locally using the following command:

```bash
hugo server --disableFastRender
```
This command will build your site and make it available at [http://localhost:1313/](http://localhost:1313/).

## Step 2: Installing and customizing Tranquilpeak

### Install the theme
Then if you want to mimic this blog you can install the [TranquikPeak](https://github.com/kakawait/hugo-tranquilpeak-theme) which is my favourite one so fare. To do so just add it to the themes folder using git submodule command which will make sure that your theme will stay in sync with the version that is maintained in kakawait repo.
```bash
git submodule add https://github.com/kakawait/hugo-tranquilpeak-theme.git themes/hugo-tranquilpeak-theme 
```
Once this is done you should also update the toml following [this template](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/exampleSite/config.toml) to activate all the customizations in the tranquilpeak theme. Once this is done I added some small customization:

### Darker sidebar image 

I am not a fan of the cover image of tranquilpaeak which does not render well on the white characters as you can see on the [demo of theme here](https://tranquilpeak.kakawait.com/) so I made it darker with Imagemagic.
```bash
convert themes/hugo-tranquilpeak-theme/static/images/cover.jpg -modulate 50,100,100 assets/images/cover.jpg
```
At some point I will certainly use another but it does the job for now

### Modiify the configuration file (`.toml`)
I also made few modifications to the `.toml.` file which you can find [here](https://github.com/robinicole/robinicole.github.io/blob/main/hugo.toml). Below I list the main ones
- In the original version of the theme you will store your blog posts into `content/en-us/posts/` I do not plan to write article in a language different from english so I changed the default directory to `content/posts/` by setting `contentDir = "content"` in `hugo.toml`.
- I added my personnal info

I also made further modifications which I won't detail here and if you want to make some modifications as well [this page](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/docs/user.md) should get you sorted. 

## Step 3: Write my first blog post 

The final step was to write my first blog post: [following this template](https://raw.githubusercontent.com/kakawait/hugo-tranquilpeak-theme/master/exampleSite/content/posts/Welcome-to-the-new-Tranquilpeak.md) as a starting point.


