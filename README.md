# Official Onion Index

A daily, source-backed index of **official `.onion` addresses**. Every address comes with a link to where the owner of the service publishes it, and the date it was last confirmed.

Maintained by the **[h4ckd4d project](https://github.com/H4ckD4d)**. &nbsp;|&nbsp; [Leia em português](README.pt-BR.md)

[![Daily update](https://github.com/H4ckD4d/official-onion-index/actions/workflows/daily.yml/badge.svg)](https://github.com/H4ckD4d/official-onion-index/actions/workflows/daily.yml)

## Why

Fake copies of onion sites are common, and link lists are the usual way people land on them. This index answers one question: *is this onion address really the one the service publishes?*

- Only addresses published by the owner of the service are listed.
- Every row links to the evidence, so you can check it yourself.
- A robot re-checks the sources every day and records the date.
- Marketplaces, link dumps and addresses without an official source are out of scope.

## How an address gets in

| Evidence | What it means |
|---|---|
| **Onion-Location** | The owner's HTTPS website announces the address itself, in an `Onion-Location` header or `<meta>` tag. Strongest evidence. |
| **Official list** | The organisation publishes a list of its own onion services (Tor Project, Debian). |
| **SecureDrop directory** | Listed in the directory run by Freedom of the Press Foundation. The link goes to the organisation's own landing page. |
| **Checked by hand** | Copied by a person from a page published by the owner or, where the owner has none, from Tor Project documentation. The date is the day of that check. |

Every address must also pass the checksum built into the v3 onion format, which rejects mistyped addresses.

## Index

<!-- BEGIN:INDEX (generated, do not edit by hand) -->

**22 addresses** &middot; last run **2026-11-11** (UTC) &middot; 16 confirmed against a live source on this date


### Search engines

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Ahmia | `juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion` | [Checked by hand](https://ahmia.fi/about/) | 2026-11-11 |
| Brave Search | `search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion` | [Checked by hand](https://community.brave.app/t/update-new-onion-addresses-for-brave-website-and-brave-search/271955) | 2026-11-11 |
| DuckDuckGo | `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` | [Checked by hand](https://tb-manual.torproject.org/onion-services/) | 2026-11-11 |
| Kagi | `kagi2pv5bdcxxqla5itjzje2cgdccuwept5ub6patvmvn3qgmgjd6vid.onion` | [Checked by hand](https://help.kagi.com/kagi/privacy/tor.html) | 2026-11-11 |
| MetaGer | `metagerv65pwclop2rsfzg4jwowpavpwd6grhhlvdgsswvo6ii4akgyd.onion` | [Checked by hand](https://metager.org/hilfe/datensicherheit) | 2026-11-11 |
| Startpage | `startpagel6srwcjlue4zgq3zevrujfaow726kjytqbbjyrswwmjzcqd.onion` | [Checked by hand](https://support.startpage.com/hc/en-us/articles/24786602537364-Startpage-s-Tor-onion-service) | 2026-11-11 |

### Tor Project

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| archive.torproject.org | `uy3qxvwzwoeztnellvvhxh7ju7kfvlsauka7avilcjg7domzxptbq7qd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| blog.torproject.org | `pzhdfe7jraknpj2qgu5cz2u3i4deuyfwmonvzu5i3nyw4t4bmg7o5pad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| bridges.torproject.org | `yq5jjvr7drkjrelzhut7kgclfuro65jjlivyzfmxiq2kyv5lickrl4qd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| community.torproject.org | `xmrhfasfg5suueegrnc4gsgyi2tyclcy5oz7f5drnrodmdtob6t2ioyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| deb.torproject.org | `apow7mjfryruh65chtdydfmqfpj5btws7nbocgtaovhvezgccyjazpqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| dist.torproject.org | `scpalcwstkydpa3y7dbpkjs2dtr7zvtvdbyj3dqwkucfrwyixcl5ptqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| download.torproject.org | `vczcbkhpkhcywcyuyd7rfhu4bebsyscp2qoeyyvjva3km5py5rpisdid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| forum.torproject.org | `v236xhqtyullodhf26szyjepvkbv6iitrhjgrqj4avaoukebkk6n6syd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| gitlab.torproject.org | `eweiibe6tdjsdprb4px6rqrzzcsi22m4koia44kc5pcjr7nec2rlxyad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| metrics.torproject.org | `hctxrvjzfpvmzh2jllqhgvvkoepxb4kfzdjm6h7egcwlumggtktiftid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| onion.torproject.org | `xao2lxsmia2edq2n5zxg6uahx6xox2t7bfjw6b5vdzsxi7ezmqob6qid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| snowflake.torproject.org | `oljlphash3bpqtrvqpr5gwzrhroziw4mddidi5d2qa4qjejcbrmoypqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| support.torproject.org | `rzuwtpc4wb3xdzrj3yeajsvm3fkq4vbeubm2tdxaqruzzzgs5dwemlad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| tails.net | `tzoz3bensgxyzs7da7lpgsn3a74h7hlbm4wa6ytq2tg6ktd57w22vqqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| tb-manual.torproject.org | `dsbqrprgkqqifztta6h3w7i2htjhnq7d3qkh3c7gvc35e66rrcv66did.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |
| www.torproject.org | `2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-11 |

<!-- END:INDEX -->

## Data files

| File | Content |
|---|---|
| [`data/onions.json`](data/onions.json) | Full index with all sources per entry |
| [`data/onions.csv`](data/onions.csv) | One row per address, for spreadsheets and tools |
| [`data/status.json`](data/status.json) | Which sources answered in the last run |
| [`data/pending.json`](data/pending.json) | Mismatches waiting for human review |
| [`CHANGELOG.md`](CHANGELOG.md) | Addresses added or changed |

## How the daily update works

1. A GitHub Actions job runs every day at 05:23 UTC.
2. It reads each source in [`config/sources.yml`](config/sources.yml) over HTTPS.
3. It validates every address and merges the results into the index.
4. It commits the new data and regenerates the tables above.

**An address is never replaced automatically.** If a source starts publishing a different address for a known service, the job opens an issue and waits. A changed address can mean a planned rotation, but it can also mean the source was compromised. The maintainer checks the owner's page by hand and approves the change in [`config/overrides.yml`](config/overrides.yml).

Nothing is removed automatically either. An entry that stops being confirmed keeps its old date and is marked `(stale)` after 14 days.

## Verify it yourself

Do not trust this list more than the owner's own website.

1. Open the service's normal website in Tor Browser.
2. If Tor Browser shows the **.onion available** button, use it. That is the same signal this index reads.
3. Otherwise open the evidence link in the table and compare all 56 characters.
4. Bookmark the address once you have checked it.

## Run it locally

```bash
pip install -r requirements.txt pytest
python -m pytest -q
python -m onionindex.update
```

## Contributing

Open an issue with the service name, its normal website, and the page where the owner publishes the onion address. Requests without an official source cannot be added.

## Sources and credits

The addresses belong to their respective owners. This project only compiles what they publish. See [SOURCES.md](SOURCES.md) for the full list of sources and related projects.

Compiled and maintained by the **h4ckd4d project** &mdash; cyber intelligence, OSINT and digital safety research. <https://github.com/H4ckD4d>

## License

Code: [MIT](LICENSE). Data compilation: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) &mdash; credit "h4ckd4d project, Official Onion Index".

## Disclaimer

This index is provided for security research, journalism and privacy protection. An entry is not an endorsement of the service. Always confirm an address at its source before relying on it.
