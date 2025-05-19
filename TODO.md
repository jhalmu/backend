# IBKR Portfolio - Kehityssuunnitelma

## Tärkein seuraava askel
- [ ] **Siirrä mock-data (MOCIT) ja osaketiedot tietokantaan (esim. DuckDB).**
    - Osakkeita ei poisteta tietokannasta, vaan niille lisätään "ei omistuksessa" -merkintä, jos ne eivät ole enää salkussa.
    - Myös määrän muutokset ja historia säilytetään.
    - Datan määrä voi kasvaa suureksi, joten tietomallin normalisointi ja tehokas haku pitää huomioida.

## Prioriteetit
1. Perustoiminnallisuus
2. Datanhallinta
3. Visualisointi
4. Optimointi
5. Monetiisointi

## 1. Perusrakenne ja Templatet
- [x] Mock API IBKR:n datalle
- [x] Perus UI Tailwind CSS:llä
- [x] Siirrä layout.html käyttöön
- [x] Lisää CUSIP ja ISIN -tiedot mock-dataan
- [ ] Lisää mikro-animaatiot ja modernisoi UI
- [ ] Lisää responsiivisuus ja mobiilioptimointi
- [ ] Lisää latausanimaatiot
- [ ] Lisää virheilmoitusten tyylittely
- [ ] Lisää vahvistusviestit toiminnoille
- [ ] Tarkista Flet vs HTML-pohjainen mobiilioptimointi

## 2. Osakkeen Yksityiskohtasivu
- [ ] Luo uusi sivu /stock/{ticker}
- [ ] Integroi yfinance API osaketietojen hakemiseen
- [ ] Lisää graafit ApexCharts:lla:
  - [ ] Pitkän aikavälin kehitys (1v, 5v, 10v)
  - [ ] Omistusajan kehitys
  - [ ] Vuosittainen osinkokehitys
  - [ ] Volatiliteetti
  - [ ] Sektori- ja markkinasuoritus
- [ ] Näytä perustiedot:
  - [ ] Yrityksen tiedot
  - [ ] Taloudelliset tunnusluvut
  - [ ] Osinkohistoria
  - [x] CUSIP/ISIN tiedot
  - [ ] Analyyttikoiden suositukset
  - [ ] Uutiset ja tapahtumat
  - [ ] Osinkotappioiden analyysi

## 3. Osinkosivu
- [x] Siirrä osinkosivu erilliseksi /dividends
- [x] Lisää CUSIP ja ISIN -tiedot osinkotaulukkoon
- [ ] Lisää osinkotulojen yhteenveto:
  - [ ] Kuukausittain (perusvaluutta ja EUR)
  - [ ] Vuosittain
  - [ ] 5 vuoden ennuste
  - [ ] Sektoreittain
  - [ ] Maittain
  - [ ] Osinkotappioiden vertailu
- [ ] Lisää osinkohistoria:
  - [ ] IBKR:n API:sta
  - [ ] CSV-tuonti
  - [ ] Automaattinen päivitys (3min välein)
  - [ ] Manuaalinen päivitys
- [ ] Lisää osinkotulojen visualisointi:
  - [ ] Kuukausittainen jakautuminen
  - [ ] Sektorikohtainen jakautuminen
  - [ ] Trendianalyysi
  - [ ] Osinkokasvun ennuste
  - [ ] Osinkotuoton vertailu markkinoihin
  - [ ] Osinkotappioiden analyysi

## 4. Tietokanta ja Datanhallinta (DuckDB)
- [ ] Tietokantakaavio:
  - [ ] Osakkeet (sis. CUSIP/ISIN)
  - [ ] Positionit
  - [ ] Osingot
  - [ ] Transaktiot
  - [ ] Valuuttakurssit
  - [ ] Välimuisti (DuckDB:n sisäinen)
- [ ] Migraatiot:
  - [ ] Alustava skeema
  - [ ] Versiointi
  - [ ] Päivitysskriptit
- [ ] CSV-tuonti:
  - [ ] Kuukausittaiset talletukset/nostot
  - [ ] Historialliset osingot
  - [ ] Osakkeiden perustiedot
  - [ ] Valuuttakurssit
- [ ] Datan varmuuskopiointi:
  - [ ] Automaattinen varmuuskopiointi
  - [ ] Palautusproseduuri
  - [ ] Versiointi
- [ ] Manuaalinen datan hallinta:
  - [ ] Eri välittäjien CSV-muotojen tuonti
  - [ ] Excel-tiedostojen tuonti
  - [ ] Manuaalinen datan syöttö
  - [ ] Datan validointi ja korjaus
  - [ ] Harjoittelutilan datan hallinta
  - [ ] Datan vienti ja varmuuskopiointi

## 5. API ja Integraatiot
- [x] REST API perusrakenne
- [ ] REST API:
  - [x] OpenAPI/Swagger dokumentaatio perusrakenne
  - [ ] OpenAPI/Swagger dokumentaatio:
    - [ ] Suojaa /docs ja /redoc endpointit
    - [ ] Konfiguroi dokumentaatio ympäristökohtaisesti:
      - [ ] Kehitys: Avoin dokumentaatio
      - [ ] Testaus: Basic auth
      - [ ] Tuotanto: API key tai OAuth2
    - [ ] Mukauta dokumentaation ulkoasua
    - [ ] Lisää esimerkkejä ja kuvauksia
    - [ ] Versionhallinta dokumentaatiossa
  - [ ] API versiointi (v1, v2)
  - [ ] Rate limiting ja throttling
  - [ ] CORS konfiguraatio
  - [ ] API avaimet ja autentikaatio:
    - [ ] API key autentikaatio
    - [ ] OAuth2 tuki
    - [ ] JWT tokenit
    - [ ] Role-based access control (RBAC)
  - [ ] Error handling ja standardoidut virheviestit
  - [ ] API health check endpoint
  - [ ] API metrics ja monitoring

- [ ] Endpointit:
  - [ ] Osakkeet:
    - [ ] GET /api/v1/stocks - Listaa kaikki osakkeet
    - [ ] GET /api/v1/stocks/{symbol} - Osakkeen tiedot
    - [ ] GET /api/v1/stocks/{symbol}/dividends - Osakkeen osingot
    - [ ] GET /api/v1/stocks/{symbol}/history - Osakkeen historia
    - [ ] GET /api/v1/stocks/{symbol}/analysis - Osakkeen analyysi
  - [ ] Positionit:
    - [ ] GET /api/v1/positions - Listaa positionit
    - [ ] POST /api/v1/positions - Lisää positio
    - [ ] PUT /api/v1/positions/{id} - Päivitä positio
    - [ ] DELETE /api/v1/positions/{id} - Poista positio
  - [ ] Osingot:
    - [ ] GET /api/v1/dividends - Listaa osingot
    - [ ] GET /api/v1/dividends/summary - Osinkoyhteenveto
    - [ ] GET /api/v1/dividends/forecast - Osinkoennusteet
    - [ ] POST /api/v1/dividends/import - Tuo osinkotiedot
  - [ ] Datan hallinta:
    - [ ] POST /api/v1/data/import - Tuo data
    - [ ] GET /api/v1/data/export - Vie data
    - [ ] GET /api/v1/data/validate - Validoi data
    - [ ] POST /api/v1/data/backup - Luo varmuuskopio
    - [ ] POST /api/v1/data/restore - Palauta varmuuskopio

- [ ] IBKR API:
  - [ ] Osinkotiedot
  - [ ] Transaktiohistoria
  - [ ] Position tiedot
  - [ ] Reaaliaikaiset hinnat

- [ ] yfinance API:
  - [ ] Reaaliaikaiset hinnat
  - [ ] Historialliset hinnat
  - [ ] Osinkotiedot
  - [ ] Taloustiedot

- [ ] Valuuttakurssit:
  - [ ] Reaaliaikaiset kurssit
  - [ ] Historialliset kurssit
  - [ ] Automaattinen päivitys

- [ ] Uutisvirta:
  - [ ] Yritysuutiset
  - [ ] Markkinauutiset
  - [ ] Osinkouutiset
  - [ ] Tärkeimmät markkinatapahtumat

- [ ] Frontend-integraatiot:
  - [ ] WebSocket tuki reaaliaikaisille päivityksille
  - [ ] Server-Sent Events (SSE) tuki
  - [ ] GraphQL API (vaihtoehto REST:ille)
  - [ ] API client kirjastot:
    - [ ] Python
    - [ ] JavaScript/TypeScript
    - [ ] Elixir
    - [ ] .NET
  - [ ] Frontend-esimerkit:
    - [ ] Elixir Phoenix LivevView
    - [ ] React
    - [ ] Vue
    - [ ] Svelte
    - [ ] Flet (Python)

## 6. UI/UX Parannukset
- [ ] Korjaa osakelinkit: Tällä hetkellä kaikki osakelinkit vievät samaan näkymään. Ehdotus:
  - Osinkosivulla linkit vievät osinkotietoihin painottuvaan näkymään (osinkohistoria, tuotto, ennusteet)
  - Etusivulla ja muissa näkymissä linkit vievät yleiseen osaketietonäkymään (hinta, volyymi, tekniset indikaattorit)
  - Lisää selkeä navigaatio näkymien välillä
  - Harkitse erillistä "Osinkoanalyysi" -näkymää, joka näyttää:
    - Osinkohistorian
    - Osinkotuoton kehityksen
    - Osinkokasvun ennusteet
    - Vertailun sektorin keskiarvoihin
    - Osinkomaksujen aikataulun
- [ ] Erottele UI:n toiminnot:
  - [ ] Pääsivu: Selkeä ja moderni yleiskatsaus
  - [ ] Datan hallinta: Eri välittäjien tuonti ja hallinta
  - [ ] Osinkoanalyysi: Syvällinen osinkotietojen analyysi
  - [ ] Osaketiedot: Tekniset indikaattorit ja perustiedot
  - [ ] Asetukset: Sovelluksen konfiguraatio ja datan hallinta
- [ ] ApexCharts integraatio:
  - [ ] Interaktiiviset graafit
  - [ ] Zoomaus ja filtteröinti
  - [ ] Reaaliaikaiset päivitykset
  - [ ] Animaatiot
- [ ] Lisää animaatiot:
  - [ ] Sivujen siirtymät
  - [ ] Datan päivitykset
  - [ ] Graafien interaktiot
  - [ ] Latausanimaatiot
- [ ] Lisää teemat:
  - [ ] Vaalea/tumma teema
  - [ ] Värimaailma
  - [ ] Typografia
  - [ ] Responsiivisuus

## 7. Testaus ja Dokumentaatio
- [x] Perus dokumentaatio (README.md, CONTRIBUTING.md)
- [x] GitHub Actions workflowt
- [ ] Yksikkötestit:
  - [ ] API-tasot
  - [ ] Tietokantaoperaatiot
  - [ ] Laskentafunktiot
- [ ] Integraatiotestit:
  - [ ] API-integraatiot
  - [ ] Tietokanta-integraatiot
  - [ ] UI-komponentit
- [ ] Käyttöohjeet:
  - [ ] Asennus
  - [ ] Konfiguraatio
  - [ ] Käyttö
- [ ] API-dokumentaatio:
  - [ ] Endpointit
  - [ ] Parametrit
  - [ ] Vastaukset
- [ ] Tietokantadokumentaatio:
  - [ ] Skeema
  - [ ] Migraatiot
  - [ ] Kyselyt

## 8. Suorituskyky ja Optimointi
- [ ] Datan välimuisti:
  - [ ] DuckDB:n sisäinen välimuisti
  - [ ] TTL-strategiat
  - [ ] Invalidointi
- [ ] API-kutsujen optimointi:
  - [ ] Batch-kutsut
  - [ ] Rinnakkaisuus
  - [ ] Retry-strategiat
- [ ] Tietokannan optimointi:
  - [ ] Indeksit
  - [ ] Partitionointi
  - [ ] Materialisoidut näkymät
- [ ] Sivujen optimointi:
  - [ ] Lazy loading
  - [ ] Code splitting
  - [ ] Asset optimointi

## 9. Tietoturva
- [x] GitHub repository privaattina
- [ ] Autentikaatio:
  - [ ] JWT
  - [ ] Session hallinta
  - [ ] 2FA
  - [ ] API key hallinta
  - [ ] OAuth2 integraatio
- [ ] Datan suojaus:
  - [ ] Salaus
  - [ ] Backup
  - [ ] Audit log
- [ ] API-suojaus:
  - [ ] Rate limiting
  - [ ] CORS
  - [ ] Input validointi
  - [ ] API dokumentaation suojaus
  - [ ] API endpointien suojaus
- [ ] Ympäristömuuttujat:
  - [ ] .env tiedostot
  - [ ] Salaisuuksien hallinta
  - [ ] Tuotantoympäristön konfiguraatio
  - [ ] API avainten hallinta

## 10. DevOps
- [x] GitHub Actions workflowt:
  - [x] CI
  - [x] Docker
  - [x] Security
  - [x] Documentation
- [ ] CI/CD:
  - [ ] GitHub Actions:
    - [x] Automaattinen testaus
    - [x] Automaattinen deploy
    - [x] Koodin laadun tarkistus
    - [x] Tietoturvatarkistukset
    - [x] Dokumentaation generointi
  - [ ] GitHub Integraatio:
    - [ ] Issue tracking
    - [ ] Project boards
    - [ ] Milestone hallinta
    - [ ] Release management
    - [ ] Code review prosessi
  - [ ] Automaattinen versiointi:
    - [ ] Semantic versioning
    - [ ] Changelog generointi
    - [ ] Release notes
  - [ ] Kehitysympäristön optimointi:
    - [ ] Docker Compose kehitysympäristö:
      - [ ] Optimoi Dockerfile (multi-stage build)
      - [ ] Lisää hot-reload kehitysympäristöön
      - [ ] Konfiguroi DuckDB välimuisti
      - [ ] Lisää health checks
    - [ ] Caddy Server proxy:
      - [ ] Automaattinen SSL/TLS
      - [ ] Reverse proxy
      - [ ] Basic auth kehitysympäristöön
    - [ ] Debug konfiguraatio
    - [ ] VS Code settings
- [ ] Monitorointi:
  - [ ] Loggaus
  - [ ] Metriikat
  - [ ] Hälytykset
- [ ] Skalautuvuus:
  - [ ] Load balancing
  - [ ] Auto scaling
  - [ ] Failover

## 11. Monetiisointi
- [ ] Premium-taso:
  - [ ] Lisäominaisuudet
  - [ ] Hinnastrategia
  - [ ] Maksutavat
- [ ] API-taso:
  - [ ] API-avaimet
  - [ ] Käyttörajoitukset
  - [ ] Hinnastrategia
- [ ] Lisäpalvelut:
  - [ ] Henkilökohtainen neuvonta
  - [ ] Automaattinen sijoitus
  - [ ] Riskianalyysi
- [ ] Markkinointi:
  - [ ] Verkkosivut
  - [ ] Sosiaalinen media
  - [ ] Sisällönmarkkinointi

## 12. GitHub ja Versionhallinta
- [x] Repository asetukset:
  - [x] Private repository
  - [ ] Branch protection rules
  - [ ] Required reviews
  - [ ] Status checks
  - [ ] Branch naming conventions
- [x] Workflow automatisointi:
  - [x] Automaattinen testaus PR:ille
  - [x] Automaattinen deploy stagingiin
  - [x] Automaattinen deploy tuotantoon
  - [x] Automaattinen dokumentaation päivitys
- [x] Issue ja PR template:
  - [x] Bug report template
  - [x] Feature request template
  - [x] PR template
  - [x] Release template
- [x] Dokumentaatio:
  - [x] README.md päivitys
  - [x] CONTRIBUTING.md
  - [ ] CHANGELOG.md
  - [ ] API dokumentaatio
- [x] Security:
  - [x] Dependabot
  - [x] Code scanning
  - [x] Secret scanning
  - [ ] Security policy

## Kysymykset tarkennettavaksi:
1. Minkä tietokannan haluat käyttää (SQLite3 vai DuckDB)? -> DuckDB suositeltu
2. Haluatko käyttää Chart.js vai Plotly graafeihin? -> ApexCharts suositeltu
3. Tarvitsetko reaaliaikaisia päivityksiä vai riittääkö päivitys käynnistyksessä? -> 3min automaattinen + manuaalinen
4. Haluatko käyttää jotain tiettyä CSS-frameworkia tai komponenttikirjastoa? -> Tailwind CSS käytössä
5. Tarvitsetko autentikaatiota sovellukseen? -> Kyllä, myöhemmin
6. Haluatko käyttää Docker Composea kehitysympäristössä? -> Pohdittava
7. Tarvitsetko CI/CD pipelinea? -> Kyllä, myöhemmin
8. Haluatko käyttää Redis/Memcached välimuistina? -> DuckDB:n sisäinen välimuisti
9. Tarvitsetko reaaliaikaista uutisvirtaa? -> Kyllä, markkinauutiset
10. Haluatko käyttää WebSocket-yhteyttä reaaliaikaisten päivitysten välittämiseen? -> Pohdittava
11. Flet vs HTML-pohjainen mobiilioptimointi? -> HTML-pohjainen ensin
12. Monetiisointistrategia? -> Premium-taso, API-taso, lisäpalvelut

## Development Plan

## Development Environment Optimization
- [x] Simplify Docker setup by removing Caddy
- [x] Configure DuckDB for development
- [x] Add hot-reload support
- [ ] Add development-specific logging
- [ ] Configure development-specific environment variables
- [ ] Add development tools (debugger, profiler)

## Database Management
- [x] Set up DuckDB with proper configuration
- [x] Configure cache size and memory mapping
- [ ] Implement database migrations
- [ ] Add database backup functionality
- [ ] Optimize query performance

## Testing and Quality Assurance
- [ ] Add unit tests for database operations
- [ ] Add integration tests for API endpoints
- [ ] Set up continuous integration
- [ ] Add code coverage reporting
- [ ] Implement automated testing

## Documentation
- [x] Update Docker documentation
- [ ] Add API documentation
- [ ] Add development setup guide
- [ ] Document database schema
- [ ] Add troubleshooting guide 