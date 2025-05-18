# Contributing to IBKR Portfolio Backend

Kiitos kiinnostuksestasi IBKR Portfolio Backend -projektin kehittämiseen! Tämä dokumentti sisältää ohjeet projektin kehittämiseen ja osallistumiseen.

## Kehitysympäristön asettaminen

1. Kloonaa repository:
```bash
git clone https://github.com/yourusername/ibkr-portfolio-backend.git
cd ibkr-portfolio-backend
```

2. Luo uusi branch:
```bash
git checkout -b feature/your-feature-name
```

3. Asenna riippuvuudet:
```bash
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
# tai
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Kehitysprosessi

1. **Branching Strategy**
   - `main`: Tuotantokoodi
   - `develop`: Kehityskoodi
   - `feature/*`: Uudet ominaisuudet
   - `bugfix/*`: Bugikorjaukset
   - `hotfix/*`: Kriittiset korjaukset

2. **Commit Viestit**
   - Käytä selkeitä ja kuvaavia commit-viestejä
   - Käytä imperatiivia ("Add feature" ei "Added feature")
   - Viittaa issueihin #numero-muodossa

3. **Code Review**
   - Kaikki muutokset vaativat vähintään yhden hyväksynnän
   - Testit pitää läpäistä
   - Koodin laadun tarkistukset pitää läpäistä

## Koodin Laatu

1. **Tyyliohjeet**
   - Noudata PEP 8 -tyyliohjeita
   - Käytä type hints
   - Dokumentoi funktiot ja luokat

2. **Testaus**
   - Kirjoita yksikkötestit uusille ominaisuuksille
   - Varmista että testikattavuus on riittävä
   - Testaa myös edge case -tapaukset

3. **Dokumentaatio**
   - Päivitä API dokumentaatio
   - Lisää kommentteja monimutkaisiin kohtiin
   - Päivitä README.md tarvittaessa

## Pull Request Prosessi

1. Varmista että koodi on ajan tasalla:
```bash
git fetch origin
git rebase origin/develop
```

2. Suorita testit:
```bash
pytest
```

3. Tarkista koodin laatu:
```bash
flake8
mypy .
```

4. Luo Pull Request:
   - Kuvaile muutokset selkeästi
   - Viittaa liittyviin issueihin
   - Lisää testitulokset ja kattavuusraportti

## Issue Template

Käytä seuraavaa templatea uusien issueiden luomiseen:

```markdown
## Kuvaus
[Selkeä kuvaus ongelmasta tai ominaisuudesta]

## Toimenpiteet
- [ ] Tarkista olemassa oleva toiminnallisuus
- [ ] Suunnittele ratkaisu
- [ ] Toteuta muutokset
- [ ] Testaa muutokset
- [ ] Päivitä dokumentaatio

## Hyväksymiskriteerit
- [ ] Koodi noudattaa tyyliohjeita
- [ ] Testit läpäisty
- [ ] Dokumentaatio päivitetty
- [ ] Code review hyväksytty
```

## Yhteystiedot

Jos sinulla on kysymyksiä tai ehdotuksia, ota yhteyttä:
- GitHub Issues
- Email: your.email@example.com

## Lisenssi

Tämä projekti on lisensoitu MIT-lisenssillä. Katso [LICENSE](LICENSE) tiedosto lisätietoja varten. 