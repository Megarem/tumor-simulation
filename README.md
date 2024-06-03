## Simulation d'un glioblastome

Pour cela, nous utilisons le projet nommé PhysiCell, un simulateur de cellules open-source (version 1.13.1)

## Installation de PhysiCell
Pour cloner le projet, il suffit de taper la commande suivante dans le terminal :
```bash
mkdir pidr_final
git clone https://gitlab.telecomnancy.univ-lorraine.fr/Victor.Levrel/pidr_final.git
```

## Compilation de PhysiCell
Avant de complier le projet, il faut se placer dans le dossier du projet :
```bash
cd pidr_final 
cd PhysiCell
```

Ensuite, il faut compiler un des projets existants dans le dossier `sample-projects` :
```bash
make name-of-the-project-sample
make
```

## Exécution de PhysiCell
Pour exécuter le projet, il suffit de taper la commande suivante :
```bash
./name-of-the-project-sample
```

## Suppression des fichiers générés
Pour supprimer les fichiers générés lors de la compilation, il suffit de taper la commande suivante :
```bash
make data-cleanup
make clean
make reset
```

## Commande pour afficher l'interface graphique liée au projet 
### Installation des dépendances
```bash
pip install -r studio/requirements.txt

pip uninstall opencv-python
pip install opencv-python-headless

sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```

### Exécution de l'interface graphique
```bash
python3 studio/bin/studio.py -e name-of-the-project-sample
```

## Génération de vidéos à partir des images générées 
Pour générer des images et des vidéos, il suffit de taper la commande suivante :
```bash
make movie 
```

## Comment load un projet

make unpack PROJ=session04_4
make data-cleanup
make reset
make clean
make load PROJ=session04_4
make
python3 studio/bin/studio.py -e name-of-the-project-sample
ensuite sur studio open les config.xml
