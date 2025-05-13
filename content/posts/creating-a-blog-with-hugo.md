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
draft: true
summary: "A step-by-step guide on setting up a blog using Hugo and the TranquilPeak theme, with tips on customization and theme management."
title: "How to create a Blog (like this website) with Hugo and TranquilPeak Theme ?"
lastmod: 2024-04-06

---
When it comes to creating a blog, popular platforms like WordPress and Wix offer user-friendly interfaces and a wide range of features. However, as a developer I prioritize simplicity, performance, and flexibility.  The combination of Hugo and GitHub presents ticked all those boxes. Hugo, is a static site generator which allows to create blogs by generating static HTML files from your content, eliminating the need for server-side processing and database queries.

In this first, we'll walk through the process of creating this blog using the Hugo static site generator and the TranquilPeak theme. We'll cover the basic setup, theme installation, and some customization tips to help you get started.

# Setting Up a Blog with Hugo and TranquilPeak Theme

## Step 1: Install Hugo and Create a New Site

This first step is to follow the official Hugo quick start guide, which will walk you through installing the Hugo framework and creating your first site with a custom theme. After completing the initial setup, you can serve your site locally by running the following command in your terminal:
```bash
hugo server --disableFastRender
```
This command will generate a local version of your site, allowing you to preview it in your web browser and make changes in real time: see [http://localhost:1313/](http://localhost:1313/).

## Step 2: Deployment on Github pages
At this stage you can already deploy your website on github page as explained on [this page](https://gohugo.io/hosting-and-deployment/hosting-on-github/). Once the workflow is set up your website should be accessible online at `http://<your-username>.github.io`

## Step 3: Installing and customizing Tranquilpeak

### Install the theme
Next, you can explore and try out different themes. For this blog, I've chosen the TranquilPeak theme, which is my favorite so far. To install it, add the theme to your themes folder using the git submodule command, which ensures that your theme stays in sync with the version maintained in the repo below:
```bash
git submodule add https://github.com/kakawait/hugo-tranquilpeak-theme.git themes/hugo-tranquilpeak-theme 
```
Once this is done you should also update the `.toml` following [this template](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/exampleSite/config.toml) to activate all the customizations in the TranquilPeak theme.

### Customizations
After completing the theme setup, I made few customizations:
#### Darker sidebar image 
I am not a fan of the cover image of TranquilPeak which does not render well on the white characters as you can see on the [demo of theme here](https://tranquilpeak.kakawait.com/) so I made it darker with Imagemagic.
```bash
convert themes/hugo-tranquilpeak-theme/static/images/cover.jpg -modulate 50,100,100 assets/images/cover.jpg
```
At some point I will certainly use another but it does the job for now

#### Modiify the configuration file (`.toml`)
I also made a few modifications to the config.toml file, which you can find here. Below, I list the main changes:
- In the original version of the theme, blog posts are stored in the content/en-us/posts/ directory. Since I don't plan to write articles in languages other than English, I changed the default directory to `content/posts/` by setting `contentDir = "content"` in hugo.toml.
- I added my personal information to the config.toml file, such as my name, bio, and social media links because that's my blog after all.

I also made further modifications which I won't detail here and if you want to make some modifications as well [this page](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/docs/user.md) should get you sorted. 

## Step 3: Write my first blog post 

The final step was to write my first blog post. There are few options to add to the font-matter to get a good-looking post and that's why I recommend to use [this template](https://raw.githubusercontent.com/kakawait/hugo-tranquilpeak-theme/master/exampleSite/content/posts/Welcome-to-the-new-Tranquilpeak.md) as a starting point as change the options in the font-matter (the two `---`) to suit your needs.


