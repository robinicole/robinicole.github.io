---
title: "Generate Travel Quotes in 5 Minutes with AI"
date: 2026-04-01
draft: false
summary: "Personalized quotes are an ideal use case for LLMs: structured documents, proprietary data, consistent tone. Here's how it works in practice for a travel agency."
tags:
  - ai
  - llm
toc: true
---

I recently asked myself a simple question: what is the most immediately useful LLM use case for a small business with no developer and no tech budget? Not a spectacular use case -- a boring, concrete one that saves time from day one.

Quote generation struck me as an ideal candidate. A quote is a semi-structured document, written in a specific tone, that combines proprietary data (catalog, rates, margins) with a specific client need. This is exactly the kind of task where LLMs excel: turning a short input ("couple, 3,000 EUR, Greece, September") into a long, structured output, drawing on provided context.

I explored the idea using travel agencies as an example, where an advisor typically spends 1 to 2 hours per quote. The result: with a simple Team subscription to ChatGPT, Claude, or Mistral -- with no development whatsoever -- you can bring that time down to 5-10 minutes. Here's how.

## The concept: an LLM grounded in business data

The core idea is to use the "Projects" feature of AI platforms (included in Team subscriptions) to ground the LLM on the agency's data. The assistant doesn't search for information on the internet and doesn't make anything up. It relies on three knowledge bases provided by the agency:

**The property and supplier catalog** -- hotels, riads, villas, activities, airlines, and transfers, with their rates by season. This is the agency's professional address book, translated into a format the LLM can work with.

**The best past quotes** -- a selection of anonymized quotes that clients have accepted. The assistant draws on these to calibrate its proposals: price level, structure, types of services that work for a given profile.

**The business rules** -- margins, discounts, processing fees, cancellation terms, document format and tone. The assistant applies these systematically.

What makes this approach interesting is that it leverages an often underestimated strength of LLMs: their ability to apply multiple constraints simultaneously. A quote must use the right seasonal rate, the right margin, the right format, the right tone, all while being tailored to the client's profile. A human does this by juggling between multiple documents. The LLM does it in a single pass.

## What the assistant produces

For each request, the assistant generates a structured quote:

- A **personalized hook** tailored to the client's profile
- **Two travel options**: one within the stated budget, one slightly above to showcase a premium alternative
- For each option: recommended destination with rationale, accommodation selected from the catalog, itinerary summary, suggested activities, detailed budget breakdown (transport, accommodation, activities, transfers, processing fees)
- The **total price and price per person**, with margins applied automatically
- The **terms and conditions** (validity, deposit, balance, cancellation)
- The **required legal notices**

## What the assistant does not do

It does not replace advisors. It does not contact suppliers. It does not check real-time availability. It does not handle invoicing, bookings, or client follow-up.

The assistant is a **smart draft writer** that saves time on the most time-consuming part of the process. The advisor remains in control of the client relationship and the final decision.

If information is missing from the knowledge base (a hotel not yet listed, a rate not entered), the assistant flags it clearly instead of making something up.

## Why you should always review the quote before sending

{{< alert "circle-info" >}}
**AI generates a draft. Not a final document.**

**Every quote must be reviewed and approved by an advisor before being sent to the client.**
{{< /alert >}}

This is the most important point, and it's also the one that reveals the real limitations of LLMs in a business context.

### Possible errors

**The AI can get a calculation wrong.** A multiplication of nights by a rate, a subtotal that doesn't add up, a margin applied incorrectly. LLMs are language tools, not calculators. This is a fundamental point that's easy to forget when the result "looks right": the numbers should always be double-checked.

**The AI can apply the wrong seasonal rate.** If the client is departing at the end of June, the assistant may hesitate between mid-season and high season. It's up to the advisor to verify the correct rate applies.

**The AI can suggest an inconsistent combination.** A flight arriving late at night with an excursion planned the next morning on the other side of the island, or a couples-oriented hotel for a family with toddlers. The advisor knows the terrain, the AI doesn't.

**The AI can hallucinate.** Even with strict instructions and provided context, an LLM can occasionally invent a detail that isn't in the knowledge base -- a hotel service that doesn't exist, an activity available in a season when it isn't. It's rare when the knowledge base is well-built, but it can happen. This is actually a good test of prompt quality: the less the assistant hallucinates, the better the instructions are written.

**The price shown on a quote commits the agency.** If a client accepts a quote with an incorrect price, the agency is in a difficult commercial position. Five minutes of review prevents this risk.

### In practice, review takes 3 to 5 minutes

1. **Prices** -- does the total match the sum of the line items? Is the margin correct? Is the right season applied?
2. **Properties** -- are they in the catalog? Are they suited to the client's profile?
3. **Consistency** -- is the itinerary realistic? Do the dates match? Are the activities available during this period?
4. **Terms** -- are the validity period, deposit, and cancellation conditions correct?
5. **Tone** -- is the text appropriate for this specific client?

The time savings remain considerable: 5 minutes of review + 1 minute of generation, instead of 1 to 2 hours of writing from scratch. But those 5 minutes are not optional.

*The frequency of these errors can be significantly reduced by writing precise, well-structured instructions. The clearer the guidelines -- on margins, seasons, expected format -- the less room the assistant has for interpretation, and the fewer mistakes it makes. This is an important point: prompt quality is the real lever for reliability, far more than model choice.*

## Role organization

The system works best with a clear separation between two roles.

**Travel advisors** use the assistant daily to generate quotes. They have no configuration to do. They open the tool, describe the client's needs, and retrieve the quote. In parallel, they feed back field intelligence: a new hotel partnership, a rate change, a particularly successful quote accepted by a client.

**Management** (or the product owner) is responsible for the knowledge base. They receive feedback from advisors, verify the information, anonymize reference quotes, and update the knowledge base. They also set the business rules: margins, discounts, terms, document format. It's lightweight work -- about 30 minutes per month for routine updates, plus a seasonal rate review.

This separation ensures that advisors cannot accidentally modify the knowledge base, and that the data remains consistent and validated.

| Advisors | | Management | | AI Assistant |
|---|---|---|---|---|
| Negotiate with suppliers | &rarr; | Verifies and validates new rates | &rarr; | Knows up-to-date properties and rates |
| Close accepted quotes | &rarr; | Anonymizes and adds good quotes to the base | &rarr; | Draws on the best quotes for calibration |
| | | Sets margins, discounts, terms | &rarr; | Applies the rules to every generated quote |
| Describe the new client's profile | | | &rarr; | Generates the quote in 30 seconds |
| Review, adjust, and send | &larr; | | | |

The system naturally improves over time: the more good reference quotes you add, the better the assistant understands what works for each type of client. This is a form of learning by example, without fine-tuning -- just few-shot learning via context.

## Data protection

Three important points.

**Your data is not used to train the AI.** Team subscriptions for ChatGPT, Claude, and Mistral offer explicit contractual guarantees: data is never used to improve their models. This is the essential difference from the free tiers.

**No identifiable client data passes through the system.** Reference quotes are anonymized before being added: no names, no emails, no phone numbers. Only the profile type (couple, family, budget) and commercial data are kept. When an advisor describes a new client, they use generic terms, not personal information.

**The agency retains full control.** The data lives in the project space, accessible only to the team. It can be modified, deleted, or exported at any time.

## Choosing a platform

The system requires no specialized software. Everything runs on consumer AI platforms, via a "Team" subscription (~25 EUR/user/month). Three options:

**ChatGPT Team (OpenAI)** -- the most well-known. If the team already uses ChatGPT, onboarding is immediate. Hosted in the United States, with contractual guarantees that data won't be used for training.

**Claude Team (Anthropic)** -- the most generous in data volume. Allows you to integrate a very large property catalog without quality loss. Excellent writing quality in French. Hosted in the United States.

**Mistral Le Chat (Mistral AI)** -- the European choice. French company, data hosted in France and the European Union. The most reassuring option if data sovereignty is a concern.

All three offer the same key feature: a **Project space** where you store the data once, and every conversation in that project automatically has access to it. This is the feature that makes the system possible -- and it's included in the Team subscription at no extra cost.

## Beyond quotes

What interests me about this example is that it illustrates a more general pattern. LLMs are particularly effective when the task combines:

- **Proprietary data** that can be provided as context (catalog, history, rules)
- **A structured, repetitive output format** (the quote always follows the same skeleton)
- **A personalization need** that makes the task tedious for a human (adapting the tone, recommendations, and calculations to each client)
- **Human verification possible** in a few minutes (the advisor can spot an error)

As soon as a task checks all four boxes, the "Project + reference files + well-crafted prompt" approach works, without writing a single line of code.

The system can also evolve: if volume increases or the catalog grows significantly, you can move to a more advanced architecture (connected database, integration with management software), without starting from scratch. But in the vast majority of cases, the approach described here covers the needs of an agency with 3 to 15 advisors.

---

## Practical guide: setup on ChatGPT Team

This step-by-step guide covers the end-to-end setup. Expect 2 to 3 hours the first time.

### 1. Create the ChatGPT Team account

1. Go to `chat.openai.com`
2. Sign in or create an account with a professional email
3. Click on your name/photo at the bottom left &rarr; "My plan" or "Upgrade"
4. Select "Team" (not "Plus", which is individual and lacks sufficient confidentiality guarantees)
5. Enter the workspace name, number of users, and billing information

{{< alert "circle-info" >}}
**Important:** ChatGPT Team guarantees that data is not used to train OpenAI's models. This is not the case for the free and Plus plans.
{{< /alert >}}

### 2. Invite the team

1. Name &rarr; "Settings" &rarr; "Members" &rarr; "Invite people"
2. Enter the email addresses of each advisor
3. Recommended roles:
   - **Admin:** management + product owner
   - **Member:** travel advisors

### 3. Create the Project

1. Sidebar &rarr; "Projects" &rarr; "New project"
2. Name: `Quote Generation`
3. Description: `Assistant for creating personalized travel quotes`

### 4. Write the instructions

This is the most important part. Everything written in the project instructions will be applied automatically to every conversation.

#### Part 1 -- The assistant's behavior

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

#### Part 2 -- The business rules

Adapt to your agency:

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

#### Part 3 -- The quote format

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

*Tip: read the instructions out loud. If something sounds ambiguous, the AI will find it ambiguous too.*

### 5. Prepare and upload the files

ChatGPT Projects lets you attach files that the assistant consults automatically.

#### "Properties" file

Create a file called `etablissements.txt` structured like this:

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

#### "Reference quotes" file

Create a file called `devis-references.txt`:

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
**GDPR reminder:** no names, emails, phone numbers, or passport numbers in this file. Only the profile type and commercial data.
{{< /alert >}}

#### Upload

1. In the project &rarr; "Files" &rarr; "Upload" or drag and drop the files
2. To update: delete the old version, upload the new one

### 6. Configure access permissions

| Person | Role | Can do |
|---|---|---|
| Management | Editor | Everything: instructions, files, quotes |
| Product owner | Editor | Everything |
| Travel advisors | Viewer | Generate quotes only |

Advisors cannot accidentally modify the instructions or files.

### 7. Test

In the project, open a "New chat" and type a client profile:

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

Verify:

| Checkpoint | OK? |
|---|---|
| Suggested properties are in the file | |
| Prices match the listed rates | |
| The correct seasonal rate is applied | |
| The margin is correct | |
| Processing fees are included | |
| The format is followed (hook, 2 options, summary, terms) | |
| The tone is correct | |
| Required legal notices are present | |
| Nothing is made up | |

Run **5 tests** on different profiles before deploying to the team.

### 8. Maintenance

**Every month** (30 minutes):

1. Collect feedback from advisors (new rates, good accepted quotes)
2. Update `etablissements.txt` and `devis-references.txt`
3. Project &rarr; Files &rarr; delete the old version &rarr; upload the new one
4. Run a quick test quote to verify

**Every season** (1 hour):

1. Review all low/mid/high season rates
2. Add new partners, remove those no longer active

### Common issues

| Symptom | Cause | Solution |
|---|---|---|
| The assistant invents a hotel | File not uploaded correctly | Check Files, re-upload |
| Wrong prices | Outdated rates | Update `etablissements.txt` |
| Quote too long/short | Imprecise format | Add a length guideline |
| Margin applied incorrectly | Ambiguous rule | Reword clearly |
| Wrong tone | Vague instructions | Add a sample quote |
| Missing properties | File too large | Split by destination |
| Instructions modified | Wrong role | Switch to Viewer |
