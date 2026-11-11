# Sources

## Read by the daily run

| Source | Publisher | What is read |
|---|---|---|
| <https://onion.torproject.org/> | Tor Project | List of the onion services the Tor Project runs (legacy v2 section ignored) |
| <https://onion.debian.org/> | Debian | List of the onion services Debian runs |
| <https://securedrop.org/api/v1/directory/> | Freedom of the Press Foundation | SecureDrop directory: organisation, onion address, landing page |
| Websites in `config/sources.yml` and `config/manual.yml` | Each service owner | `Onion-Location` header or `<meta>` tag on the HTTPS site |

## Checked by hand

Entries in [`config/manual.yml`](config/manual.yml) carry their own proof URL and the date of the check.

## Related projects (not copied)

These lists are good references and are credited here. Their content is not ingested, because their licences require derived work to carry the same licence.

- [Real-World Onion Sites](https://github.com/alecmuffett/real-world-onion-sites) by Alec Muffett (CC BY-SA)
- [List of Tor onion services](https://en.wikipedia.org/wiki/List_of_Tor_onion_services) on Wikipedia (CC BY-SA)
- [Privacy Guides](https://www.privacyguides.org/)

## Out of scope

Marketplaces, link directories, "hidden wiki" pages and any address that the owner of the service does not publish.

---

Compiled by the [h4ckd4d project](https://github.com/H4ckD4d).
