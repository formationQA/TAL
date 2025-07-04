# Détecteur de Registre Linguistique
Ce projet  été développé dans le cadre de validation du cours Ingénierie des langues il permet de
de detecter un registre d'un texte (Académique, Famillier ou courant)

##  Fonctionnalités

-   **Interface Web** : Saisie d'une phrase via Streamlit.
-   **Prédiction ** : Analyse du registre d'une phrase.
-   **Trois registres programmé ** : Familier, Courant, et Académique.
-   **Modèle d'apprentissage automatique** : Utilise un classifieur Bayes Naïf Multinomial entraîné sur un corpus diversifié de texte français.


##  Démarrage rapide

Suivez ces étapes pour exécuter l'application sur votre machine locale.

### Prérequis

Assurez-vous d'avoir Python installé sur votre système.
Dans un terminal exécutez ces commandes : 

### 1. Cloner le dépôt (ou télécharger les fichiers)

```bash
git clone https://github.com/formationQA/TAL.git
cd /TAL/src 
python3 -m venv .venv
source .venv/bin/activate
streamlit run application.py
