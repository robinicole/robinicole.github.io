---
title: "Générez vos devis voyage en 5 minutes grâce à l'IA"
date: 2026-04-01
draft: false
summary: "Les devis personnalisés sont un cas d'usage idéal pour les LLMs : documents structurés, données propriétaires, besoin de ton cohérent. Voici comment ça fonctionne concrètement pour une agence de voyage."
tags:
  - ai
  - llm
  - french
toc: true
---

Je me suis récemment posé une question simple : quel est le cas d'usage le plus immédiatement utile des LLMs pour une petite entreprise qui n'a ni développeur, ni budget tech ? Pas un cas d'usage spectaculaire -- un cas d'usage ennuyeux, concret, qui fait gagner du temps dès le premier jour.

La génération de devis m'a semblé être un candidat idéal. Un devis, c'est un document semi-structuré, rédigé dans un ton précis, qui combine des données propriétaires (catalogue, tarifs, marges) avec un besoin client spécifique. C'est exactement le type de tâche où les LLMs excellent : transformer une entrée courte ("couple, 3 000 €, Grèce, septembre") en une sortie longue et structurée, en s'appuyant sur un contexte fourni.

J'ai exploré l'idée en prenant comme exemple les agences de voyage, où un conseiller passe en moyenne 1 à 2 heures par devis. Le résultat : avec un simple abonnement Team à ChatGPT, Claude ou Mistral -- sans aucun développement -- on peut ramener ce temps à 5-10 minutes. Voici comment.

## Le principe : un LLM ancré sur des données métier

L'idée centrale est d'utiliser la fonctionnalité "Projets" des plateformes IA (incluse dans les abonnements Team) pour ancrer le LLM sur les données de l'agence. L'assistant ne va pas chercher d'informations sur internet et n'invente rien. Il s'appuie sur trois bases fournies par l'agence :

**Le catalogue d'établissements et de prestataires** -- hôtels, riads, villas, activités, compagnies aériennes et transferts, avec leurs tarifs par saison. C'est le carnet d'adresses professionnel de l'agence, traduit dans un format que le LLM peut exploiter.

**Les meilleurs devis passés** -- une sélection de devis acceptés par des clients, anonymisés. L'assistant s'en inspire pour calibrer ses propositions : niveau de prix, structure, type de prestations qui fonctionnent pour tel profil.

**Les règles commerciales** -- marges, remises, frais de dossier, conditions d'annulation, format et ton des documents. L'assistant les applique systématiquement.

Ce qui rend cette approche intéressante, c'est qu'elle exploite une force souvent sous-estimée des LLMs : leur capacité à appliquer des contraintes multiples simultanément. Un devis doit respecter le bon tarif saisonnier, la bonne marge, le bon format, le bon ton, tout en étant adapté au profil du client. Un humain fait ça en jonglant entre plusieurs documents. Le LLM le fait en une passe.

## Ce que l'assistant produit

Pour chaque demande, l'assistant génère un devis structuré :

- Une **accroche personnalisée** adaptée au profil du client
- **Deux options de voyage** : une dans le budget annoncé, une légèrement au-dessus pour montrer une alternative premium
- Pour chaque option : destination recommandée avec justification, hébergement sélectionné dans le catalogue, résumé d'itinéraire, activités suggérées, budget détaillé ventilé (transport, hébergement, activités, transferts, frais de dossier)
- Le **prix total et le prix par personne**, avec les marges appliquées automatiquement
- Les **conditions commerciales** (validité, acompte, solde, annulation)
- Les **mentions obligatoires**

## Ce que l'assistant ne fait pas

Il ne remplace pas les conseillers. Il ne contacte pas les fournisseurs. Il ne vérifie pas les disponibilités en temps réel. Il ne gère ni la facturation, ni les réservations, ni le suivi client.

L'assistant est un **rédacteur de brouillons intelligent** qui fait gagner du temps sur la partie la plus chronophage du processus. Le conseiller reste maître de la relation client et de la décision finale.

Si une information manque dans la base (un hôtel pas encore référencé, un tarif non renseigné), l'assistant le signale clairement au lieu d'inventer.

## Pourquoi il faut toujours vérifier le devis avant envoi

{{< alert "circle-info" >}}
**L'IA génère un brouillon. Pas un document final.**

**Chaque devis doit être relu et validé par un conseiller avant d'être envoyé au client.**
{{< /alert >}}

C'est le point le plus important, et c'est aussi celui qui révèle les limites réelles des LLMs dans un contexte métier.

### Les erreurs possibles

**L'IA peut se tromper sur un calcul.** Une multiplication de nuits par un tarif, un total mal additionné, une marge mal appliquée. Les LLMs sont des outils de langage, pas des calculatrices. C'est un point fondamental qu'on a tendance à oublier quand le résultat "a l'air correct" : les chiffres doivent toujours être revérifiés.

**L'IA peut appliquer la mauvaise saison tarifaire.** Si le client part fin juin, l'assistant peut hésiter entre moyenne et haute saison. C'est au conseiller de vérifier que le bon tarif s'applique.

**L'IA peut proposer une combinaison incohérente.** Un vol qui arrive tard le soir avec une excursion prévue le lendemain matin à l'autre bout de l'île, ou un hôtel adapté aux couples pour une famille avec enfants en bas âge. Le conseiller connaît le terrain, pas l'IA.

**L'IA peut halluciner.** Même avec des instructions strictes et un contexte fourni, il arrive qu'un LLM invente un détail qui n'est pas dans la base -- un service d'hôtel qui n'existe pas, une activité disponible à une saison où elle ne l'est pas. C'est rare quand la base est bien construite, mais ça peut arriver. C'est d'ailleurs un bon test de la qualité du prompt : moins l'assistant hallucine, mieux les instructions sont rédigées.

**Le prix affiché sur un devis engage l'agence.** Si un client accepte un devis avec un prix erroné, l'agence est dans une situation commerciale délicate. Cinq minutes de relecture évitent ce risque.

### En pratique, la vérification prend 3 à 5 minutes

1. **Les prix** -- le total correspond-il à la somme des lignes ? La marge est-elle correcte ? La bonne saison est-elle appliquée ?
2. **Les établissements** -- sont-ils bien dans le catalogue ? Sont-ils adaptés au profil du client ?
3. **La cohérence** -- l'itinéraire est-il réaliste ? Les dates correspondent-elles ? Les activités sont-elles disponibles à cette période ?
4. **Les conditions** -- la validité, l'acompte, les conditions d'annulation sont-ils corrects ?
5. **Le ton** -- le texte est-il adapté à ce client spécifique ?

Le gain de temps reste considérable : 5 minutes de relecture + 1 minute de génération, au lieu de 1 à 2 heures de rédaction complète. Mais ces 5 minutes ne sont pas optionnelles.

*La fréquence de ces erreurs peut être significativement réduite en rédigeant des instructions précises et bien structurées. Plus les consignes sont claires -- sur les marges, les saisons, le format attendu -- moins l'assistant a de marge d'interprétation, et moins il se trompe. C'est un point important : la qualité du prompt est le vrai levier de fiabilité, bien plus que le choix du modèle.*

## Organisation des rôles

Le système fonctionne mieux avec une séparation claire entre deux rôles.

**Les conseillers voyage** utilisent l'assistant au quotidien pour générer des devis. Ils n'ont aucune configuration à faire. Ils ouvrent l'outil, décrivent le besoin du client, et récupèrent le devis. En parallèle, ils remontent les informations du terrain : nouveau partenariat avec un hôtel, changement de tarif, devis particulièrement réussi accepté par un client.

**La direction** (ou le responsable produit) est garante de la base de données. Elle reçoit les remontées des conseillers, vérifie les informations, anonymise les devis de référence, et met à jour la base. Elle décide aussi des règles commerciales : marges, remises, conditions, format des documents. C'est un travail léger -- environ 30 minutes par mois pour les mises à jour courantes, plus une révision saisonnière des tarifs.

Cette séparation garantit que les conseillers ne peuvent pas modifier la base par erreur, et que les données restent cohérentes et validées.

| Les conseillers | | La direction | | L'assistant IA |
|---|---|---|---|---|
| Négocient avec les fournisseurs | &rarr; | Vérifie et valide les nouveaux tarifs | &rarr; | Connaît les établissements et tarifs à jour |
| Ferment des devis acceptés | &rarr; | Anonymise et ajoute les bons devis à la base | &rarr; | S'inspire des meilleurs devis pour calibrer |
| | | Fixe les marges, remises, conditions | &rarr; | Applique les règles à chaque devis généré |
| Décrivent le profil du nouveau client | | | &rarr; | Génère le devis en 30 secondes |
| Relisent, ajustent et envoient | &larr; | | | |

Le système s'améliore naturellement avec le temps : plus on ajoute de bons devis en référence, plus l'assistant comprend ce qui fonctionne pour chaque type de client. C'est une forme d'apprentissage par l'exemple, sans fine-tuning -- juste du few-shot learning via le contexte.

## Protection des données

Trois points importants.

**Les données ne servent pas à entraîner l'IA.** Les abonnements Team de ChatGPT, Claude et Mistral offrent des garanties contractuelles explicites : les données ne sont jamais utilisées pour améliorer leurs modèles. C'est la différence essentielle avec les versions gratuites.

**Aucune donnée client identifiable ne transite dans le système.** Les devis de référence sont anonymisés avant d'être intégrés : pas de nom, pas d'email, pas de numéro de téléphone. On conserve uniquement le profil type (couple, famille, budget) et les données commerciales. Quand le conseiller décrit un nouveau client, il utilise des termes génériques, pas des informations personnelles.

**L'agence garde le contrôle total.** Les données vivent dans l'espace projet, accessible uniquement à l'équipe. Elles peuvent être modifiées, supprimées ou exportées à tout moment.

## Quelle plateforme choisir

Le système ne nécessite aucun logiciel spécialisé. Tout fonctionne sur les plateformes d'IA grand public, via un abonnement "Team" (~25 EUR/utilisateur/mois). Trois options :

**ChatGPT Team (OpenAI)** -- le plus connu. Si l'équipe utilise déjà ChatGPT, la prise en main est immédiate. Hébergé aux États-Unis, avec garanties contractuelles de non-utilisation des données.

**Claude Team (Anthropic)** -- le plus généreux en volume de données. Permet d'intégrer un catalogue d'établissements très large sans perte de qualité. Excellente qualité de rédaction en français. Hébergé aux États-Unis.

**Mistral Le Chat (Mistral AI)** -- le choix européen. Entreprise française, données hébergées en France et en Union européenne. L'option la plus rassurante si la souveraineté des données est un sujet.

Les trois offrent la même fonctionnalité clé : un **espace Projet** dans lequel on stocke les données une fois, et chaque conversation dans ce projet y a accès automatiquement. C'est cette fonctionnalité qui rend le système possible -- et elle est incluse dans l'abonnement Team, sans surcoût.

## Au-delà des devis

Ce qui m'intéresse dans cet exemple, c'est qu'il illustre un pattern plus général. Les LLMs sont particulièrement efficaces quand la tâche combine :

- **Des données propriétaires** qu'on peut fournir en contexte (catalogue, historique, règles)
- **Un format de sortie structuré** et répétitif (le devis suit toujours le même squelette)
- **Un besoin de personnalisation** qui rend la tâche pénible pour un humain (adapter le ton, les recommandations, les calculs à chaque client)
- **Une vérification humaine possible** en quelques minutes (le conseiller sait repérer une erreur)

Dès qu'une tâche coche ces quatre cases, l'approche "Projet + fichiers de référence + prompt bien rédigé" fonctionne, sans écrire une seule ligne de code.

Le système peut aussi évoluer : si le volume augmente ou que le catalogue s'élargit significativement, on peut passer à une architecture plus avancée (base de données connectée, intégration avec un logiciel de gestion), sans repartir de zéro. Mais dans la grande majorité des cas, l'approche décrite ici couvre les besoins d'une agence de 3 à 15 conseillers.

---

## Guide pratique : mise en place sur ChatGPT Team

Ce guide pas à pas couvre la mise en place de bout en bout. Comptez 2 à 3 heures la première fois.

### 1. Créer le compte ChatGPT Team

1. Rendez-vous sur `chat.openai.com`
2. Connectez-vous ou créez un compte avec un email professionnel
3. Cliquez sur votre nom/photo en bas à gauche &rarr; "My plan" ou "Upgrade"
4. Sélectionnez "Team" (et non "Plus" qui est individuel et sans garanties de confidentialité suffisantes)
5. Renseignez le nom du workspace, le nombre d'utilisateurs, et les informations de facturation

{{< alert "circle-info" >}}
**Important :** ChatGPT Team garantit que les données ne sont pas utilisées pour entraîner les modèles d'OpenAI. Ce n'est pas le cas des plans gratuit et Plus.
{{< /alert >}}

### 2. Inviter l'équipe

1. Nom &rarr; "Settings" &rarr; "Members" &rarr; "Invite people"
2. Entrer les adresses email de chaque conseiller
3. Rôles recommandés :
   - **Admin :** direction + responsable produit
   - **Member :** conseillers voyage

### 3. Créer le Projet

1. Barre latérale &rarr; "Projects" &rarr; "New project"
2. Nom : `Génération de devis`
3. Description : `Assistant pour créer des devis voyage personnalisés`

### 4. Rédiger les instructions

C'est la partie la plus importante. Tout ce qui est écrit dans les instructions du projet sera appliqué automatiquement à chaque conversation.

#### Partie 1 -- Le comportement de l'assistant

```
Tu es l'assistant devis de [NOM DE L'AGENCE], spécialisée dans [SPÉCIALITÉ].

Quand un conseiller te donne un profil client, tu génères un devis professionnel
en t'appuyant UNIQUEMENT sur :
- Les établissements et tarifs fournis dans les fichiers du projet
- Les devis de référence fournis dans les fichiers du projet
- Les règles commerciales ci-dessous

RÈGLES ABSOLUES :
- N'invente JAMAIS un établissement, un prix ou une activité qui n'est pas dans les fichiers
- Si une information manque, écris "[À CONFIRMER]"
- Applique TOUJOURS les marges définies ci-dessous
- Propose TOUJOURS 2 options : une dans le budget, une légèrement au-dessus
```

#### Partie 2 -- Les règles commerciales

À adapter selon l'agence :

```
=== RÈGLES COMMERCIALES ===

MARGES :
- Standard : 12 %
- Haute saison (juillet-août) : 15 %
- Groupes > 6 personnes : 10 %
- Client fidèle (2e voyage+) : 10 %

FRAIS DE DOSSIER : 45 EUR par dossier

REMISES :
- Early booking (> 4 mois avant départ) : -5 % sur hébergement
- Parrainage : -50 EUR sur le total
- Les remises ne se cumulent pas

CONDITIONS :
- Acompte : 30 % à la réservation
- Solde : 45 jours avant le départ
- Validité du devis : 10 jours
- Annulation gratuite : jusqu'à 60 jours avant
- Annulation 30-60 jours : 50 % de frais
- Annulation < 30 jours : 100 %

MENTIONS OBLIGATOIRES :
- "Prix sous réserve de disponibilité"
- "Assurance voyage non incluse — nous consulter"

TON : Chaleureux et passionné, professionnel. Vouvoiement.
```

#### Partie 3 -- Le format du devis

```
=== FORMAT DU DEVIS ===

1. ACCROCHE : 2-3 phrases personnalisées
2. OPTION A -- [Nom accrocheur] (dans le budget)
   - Destination + justification
   - Hébergement : nom, catégorie, nb nuits x prix/nuit
   - Transport : vol + transferts
   - Activités : liste avec prix unitaire
   - Récapitulatif ventilé
   - TOTAL : montant EUR | montant EUR/personne
3. OPTION B -- [Nom accrocheur] (premium)
   Même structure
4. CE QUI REND CE VOYAGE SPÉCIAL
5. PROCHAINES ÉTAPES
6. MENTIONS OBLIGATOIRES
```

*Conseil : relire les instructions à voix haute. Si quelque chose semble ambigu, l'IA le trouvera ambigu aussi.*

### 5. Préparer et uploader les fichiers

ChatGPT Projects permet d'attacher des fichiers que l'assistant consulte automatiquement.

#### Fichier "Établissements"

Créer un fichier `etablissements.txt` structuré comme ceci :

```
========== DESTINATION : Crète, Grèce ==========
Saisons : Basse (nov-avr) | Moyenne (mai-juin, sept-oct) | Haute (juil-août)
Vol depuis Paris : 3h30 | Visa : Non (UE)

HÉBERGEMENTS :

- Blue Marine Resort -- 4* all-inclusive -- Héraklion
  Double : 180 EUR/nuit (basse), 220 EUR/nuit (moy), 310 EUR/nuit (haute)
  Familiale : 240 EUR/nuit (basse), 290 EUR/nuit (moy), 400 EUR/nuit (haute)
  Idéal : familles, couples détente

- Villa Ariadne -- Villa 3 chambres -- Réthymnon
  Entière : 250 EUR/nuit (basse), 350 EUR/nuit (haute)
  Idéal : familles, groupes amis

ACTIVITÉS :
- Palais de Knossos -- visite guidée -- 35 EUR/adulte, 20 EUR/enfant
- Journée bateau Spinalonga -- 45 EUR/adulte, 30 EUR/enfant

TRANSPORTS :
- Vol Paris-Héraklion : Transavia 250-400 EUR/pers A/R
- Transfert aéroport : 35 EUR taxi
- Location voiture : 35-55 EUR/jour
```

#### Fichier "Devis de référence"

Créer un fichier `devis-references.txt` :

```
=== DEVIS #1 -- Couple Crète -- ACCEPTÉ ===
Profil : Couple 30-40 ans, 1re visite
Destination : Crète | 7 nuits | Septembre
Budget annoncé : 2 500-3 000 EUR

Détail :
- Vol Transavia Paris-Héraklion : 520 EUR (2 pers)
- Blue Marine Resort, double, 7n x 220 EUR : 1 540 EUR
- Transfert A/R : 70 EUR
- Knossos : 70 EUR | Spinalonga : 90 EUR
- Location voiture 3j : 135 EUR
Total net : 2 425 EUR | Marge 12 % | Prix client : 2 716 EUR + 45 EUR frais
TOTAL : 2 761 EUR (1 380 EUR/pers)

Retour : Mix organisé + liberté très apprécié.
```

{{< alert "circle-info" >}}
**Rappel RGPD :** aucun nom, email, téléphone ou numéro de passeport dans ce fichier. Uniquement le profil type et les données commerciales.
{{< /alert >}}

#### Upload

1. Dans le projet &rarr; "Files" &rarr; "Upload" ou glisser-déposer les fichiers
2. Pour mettre à jour : supprimer l'ancien, uploader la nouvelle version

### 6. Configurer les droits d'accès

| Personne | Rôle | Peut faire |
|---|---|---|
| Direction | Editor | Tout : instructions, fichiers, devis |
| Responsable produit | Editor | Tout |
| Conseillers voyage | Viewer | Générer des devis uniquement |

Les conseillers ne peuvent pas modifier les instructions ni les fichiers par erreur.

### 7. Tester

Dans le projet, ouvrir un "New chat" et taper un profil client :

```
Nouveau devis :

2 adultes, la trentaine, en couple
Budget : 2 500-3 000 EUR
7 à 10 jours en septembre
Envie de Grèce, plutôt les îles
Plage + snorkeling + bonne cuisine locale
Vol direct depuis Paris
Premier grand voyage ensemble
Pas de remise applicable
```

Vérifier :

| Point de contrôle | OK ? |
|---|---|
| Les établissements proposés sont dans le fichier | |
| Les prix correspondent aux tarifs renseignés | |
| La bonne saison tarifaire est appliquée | |
| La marge est correcte | |
| Les frais de dossier sont inclus | |
| Le format est respecté (accroche, 2 options, récap, conditions) | |
| Le ton est correct | |
| Les mentions obligatoires sont présentes | |
| Rien n'est inventé | |

Faire **5 tests** sur des profils différents avant de déployer à l'équipe.

### 8. Entretien

**Chaque mois** (30 minutes) :

1. Collecter les retours des conseillers (nouveaux tarifs, bons devis acceptés)
2. Mettre à jour `etablissements.txt` et `devis-references.txt`
3. Projet &rarr; Files &rarr; supprimer l'ancien &rarr; uploader le nouveau
4. Tester un devis rapide pour vérifier

**Chaque saison** (1 heure) :

1. Vérifier tous les tarifs basse/moyenne/haute saison
2. Ajouter les nouveaux partenaires, retirer ceux qui ne sont plus actifs

### Problèmes courants

| Symptôme | Cause | Solution |
|---|---|---|
| L'assistant invente un hôtel | Fichier mal uploadé | Vérifier Files, réuploader |
| Prix faux | Tarifs obsolètes | Mettre à jour `etablissements.txt` |
| Devis trop long/court | Format imprécis | Ajouter consigne de longueur |
| Marge mal appliquée | Règle ambiguë | Reformuler clairement |
| Mauvais ton | Instructions vagues | Ajouter un exemple de devis |
| Oubli d'établissements | Fichier trop volumineux | Scinder par destination |
| Instructions modifiées | Mauvais rôle | Passer en Viewer |
