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
summary: "Un guide pas-a-pas pour creer un blog avec Hugo et le theme TranquilPeak, avec des conseils de personnalisation et de gestion du theme."
title: "Comment creer un blog (comme ce site) avec Hugo et le theme TranquilPeak ?"
lastmod: 2024-04-06

---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}
Quand il s'agit de creer un blog, des plateformes populaires comme WordPress et Wix offrent des interfaces intuitives et un large eventail de fonctionnalites. Cependant, en tant que developpeur, je privilegie la simplicite, la performance et la flexibilite. La combinaison de Hugo et GitHub cochait toutes ces cases. Hugo est un generateur de sites statiques qui permet de creer des blogs en generant des fichiers HTML statiques a partir de votre contenu, eliminant ainsi le besoin de traitement cote serveur et de requetes en base de donnees.

Dans ce premier article, nous allons parcourir le processus de creation de ce blog en utilisant le generateur de sites statiques Hugo et le theme TranquilPeak. Nous couvrirons la configuration de base, l'installation du theme et quelques astuces de personnalisation pour vous aider a demarrer.

# Mettre en place un blog avec Hugo et le theme TranquilPeak

## Etape 1 : Installer Hugo et creer un nouveau site

La premiere etape consiste a suivre le guide de demarrage rapide officiel de Hugo, qui vous accompagnera dans l'installation du framework Hugo et la creation de votre premier site avec un theme personnalise. Une fois la configuration initiale terminee, vous pouvez servir votre site localement en executant la commande suivante dans votre terminal :
```bash
hugo server --disableFastRender
```
Cette commande generera une version locale de votre site, vous permettant de le previsualiser dans votre navigateur web et d'effectuer des modifications en temps reel : voir [http://localhost:1313/](http://localhost:1313/).

## Etape 2 : Deploiement sur Github Pages
A ce stade, vous pouvez deja deployer votre site sur Github Pages comme explique sur [cette page](https://gohugo.io/hosting-and-deployment/hosting-on-github/). Une fois le workflow configure, votre site devrait etre accessible en ligne a l'adresse `http://<votre-nom-utilisateur>.github.io`

## Etape 3 : Installation et personnalisation de Tranquilpeak

### Installer le theme
Ensuite, vous pouvez explorer et essayer differents themes. Pour ce blog, j'ai choisi le theme TranquilPeak, qui est mon prefere jusqu'a present. Pour l'installer, ajoutez le theme a votre dossier themes en utilisant la commande git submodule, ce qui garantit que votre theme reste synchronise avec la version maintenue dans le depot ci-dessous :
```bash
git submodule add https://github.com/kakawait/hugo-tranquilpeak-theme.git themes/hugo-tranquilpeak-theme 
```
Une fois cela fait, vous devriez egalement mettre a jour le fichier `.toml` en suivant [ce modele](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/exampleSite/config.toml) pour activer toutes les personnalisations du theme TranquilPeak.

### Personnalisations
Apres avoir termine la configuration du theme, j'ai effectue quelques personnalisations :
#### Image de la barre laterale plus sombre
Je ne suis pas fan de l'image de couverture de TranquilPeak qui ne rend pas bien sur les caracteres blancs, comme vous pouvez le voir sur la [demo du theme ici](https://tranquilpeak.kakawait.com/), alors je l'ai assombrie avec ImageMagick.
```bash
convert themes/hugo-tranquilpeak-theme/static/images/cover.jpg -modulate 50,100,100 assets/images/cover.jpg
```
A un moment donne, j'utiliserai certainement une autre image, mais celle-ci fait l'affaire pour l'instant.

#### Modifier le fichier de configuration (`.toml`)
J'ai egalement apporte quelques modifications au fichier config.toml, que vous pouvez trouver ici. Voici les principaux changements :
- Dans la version originale du theme, les articles de blog sont stockes dans le repertoire content/en-us/posts/. Comme je ne prevois pas d'ecrire des articles dans d'autres langues que l'anglais, j'ai change le repertoire par defaut pour `content/posts/` en definissant `contentDir = "content"` dans hugo.toml.
- J'ai ajoute mes informations personnelles dans le fichier config.toml, comme mon nom, ma biographie et mes liens vers les reseaux sociaux, parce que c'est mon blog apres tout.

J'ai egalement effectue d'autres modifications que je ne detaillerai pas ici. Si vous souhaitez faire des modifications, [cette page](https://github.com/kakawait/hugo-tranquilpeak-theme/blob/master/docs/user.md) devrait vous aider.

## Etape 3 : Ecrire mon premier article de blog

La derniere etape a ete d'ecrire mon premier article de blog. Il y a quelques options a ajouter dans le front-matter pour obtenir un article bien presente, c'est pourquoi je recommande d'utiliser [ce modele](https://raw.githubusercontent.com/kakawait/hugo-tranquilpeak-theme/master/exampleSite/content/posts/Welcome-to-the-new-Tranquilpeak.md) comme point de depart et de modifier les options dans le front-matter (les deux `---`) selon vos besoins.
