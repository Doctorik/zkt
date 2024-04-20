-zo SW hľadiska je potrebné mať nainštalovaný docker s podporov docker-compose 3, všetky ostatné potrebné veci si aplikaca stiahne z internetu.

- jednoducha stranka na styl blogu, ktorá uchováva dáta v postgres databaze

- využíva jednú virtuálnu sieť, ktorá prepája kontajneri, pre databázu je vytvorený z zväzok "data" na uchovavanie dát aj po vypnutý kontajnerov.

-pre aplikaciu si musíme vytvoriť vlastný obraz za pomoci Dockerfile-u, v ktorom najprv použijeme uź existujúci python obraz, nastavíme pracovný adresát, skopírujeme potrebné súbory, spustime aplikáciu a zverejníme ju. Následne vytvoríme postgres kontajner, spustíme a prepojíme oba kontajnery za pomoci docker-compose, nastavíme mapovanie portov, link na databázu, jej heslo, vytvoríme vlasntnú sieť a vytvoríme zväzok pre dáta.

-v postgres kontaineri beží databáza pre aplikáciu a vo web kontajneri beží flask aplikacia zobrazujúca jednoduchú html stránku

-po stiahnutí potrebných súborov, si aplikaciu najprv pripravime "bash prepare-app", následne ju môźeme spustiť "bash start-app.sh", pozastavíme aplikaciu "bash stop-app.sh" a vymažeme všetky súbory vytvorené aplikaciou "remove-app.sh"

-vo webovom prehľadači a) ak aplikácia beží na rovnakom stroji na akom ju chceme prezieť otvoríme link: http://localhost:5000/
b) ak aplikácia beží na inom stroji zadáme ip adresu daného stroja za ktorú následne pridáme port 5000 (napr. 10.0.4.152:5000)
