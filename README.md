## Simulation d'un glioblastome

Pour cela, nous utilisons le projet nommé PhysiCell, un simulateur de cellules open-source (version 1.13.1)


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
