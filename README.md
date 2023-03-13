# Organisation et publication de code

1.	Créer un module Python exposant :
		- une fonction d'addition `add` (return a + b) ;
		- une fonction `hello` qui écrit dans la console la version de `numpy` actuellement installée (votre package a donc besoin de numpy pour fonctionner).
	Les fonctions doivent pouvoir être importées via `from nom_du_package import add, hello`.

2.	Packager le module pour en faire un package Python prêt à être distribué.
	Utiliser `setuptools`.

3.	Publier le package sur le PyPI de test (https://test.pypi.org/).

4.	Installer le package depuis le PyPI sur un autre projet Python (via pip).
	La commande `hello` dans le terminal doit executer la fonction `hello()` du module.
	La commande `python3 -m mytestpackage` doit executer la fonction `hello()` du module.