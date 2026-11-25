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

**198 addresses** &middot; last run **2026-11-25** (UTC) &middot; 194 confirmed against a live source on this date


### Search engines

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Ahmia | `juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion` | [Onion-Location](https://ahmia.fi/), [Checked by hand](https://ahmia.fi/about/) | 2026-11-25 |
| Brave Search | `search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion` | [Checked by hand](https://community.brave.app/t/update-new-onion-addresses-for-brave-website-and-brave-search/271955) | 2026-11-11 |
| DuckDuckGo | `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` | [Checked by hand](https://tb-manual.torproject.org/onion-services/) | 2026-11-11 |
| Kagi | `kagi2pv5bdcxxqla5itjzje2cgdccuwept5ub6patvmvn3qgmgjd6vid.onion` | [Checked by hand](https://help.kagi.com/kagi/privacy/tor.html) | 2026-11-11 |
| MetaGer | `metagerv65pwclop2rsfzg4jwowpavpwd6grhhlvdgsswvo6ii4akgyd.onion` | [Onion-Location](https://metager.org/), [Checked by hand](https://metager.org/hilfe/datensicherheit) | 2026-11-25 |
| Startpage | `startpagel6srwcjlue4zgq3zevrujfaow726kjytqbbjyrswwmjzcqd.onion` | [Checked by hand](https://support.startpage.com/hc/en-us/articles/24786602537364-Startpage-s-Tor-onion-service) | 2026-11-11 |

### News and journalism

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Deutsche Welle | `www.dwnewsgngmhlplxy6o2twtfgjnrnjxbegbwqx6wnotdhkzt562tszfid.onion` | [Onion-Location](https://www.dw.com/) | 2026-11-25 |
| The Guardian | `www.guardian2zotagl6tmjucg3lrhxdk4dw3lhbqnkvvkywawy3oqfoprid.onion` | [Onion-Location](https://www.theguardian.com/) | 2026-11-25 |

### Privacy services

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Mullvad VPN | `o54hon2e2vj6c7m3aqqu6uyece65by3vgoxxhlqlsvkmacw6a7m7kiad.onion` | [Onion-Location](https://mullvad.net/) | 2026-11-25 |
| Proton | `protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion` | [Onion-Location](https://proton.me/) | 2026-11-25 |
| Riseup | `vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion` | [Onion-Location](https://riseup.net/) | 2026-11-25 |

### Operating systems and software

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Brave | `brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion` | [Onion-Location](https://brave.com/) | 2026-11-25 |
| OnionShare | `lldan5gahapx5k7iafb3s4ikijc4ni7gx5iywdflkba5y2ezyg6sjgyd.onion` | [Onion-Location](https://onionshare.org/) | 2026-11-25 |
| Qubes OS | `qubesosfasa4zl44o4tws22di6kepyzfeqv3tg4e3ztknltfxqrymdad.onion` | [Onion-Location](https://www.qubes-os.org/) | 2026-11-25 |
| SecureDrop | `sdolvtfhatvsysc6l34d65ymdwxcujausv7k5jk4cy5ttzhjoi6fzvyd.onion` | [Onion-Location](https://securedrop.org/) | 2026-11-25 |
| Whonix | `www.dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion` | [Onion-Location](https://www.whonix.org/) | 2026-11-25 |

### Organisations and archives

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Amnesty International | `www.amnestyl337aduwuvpf57irfl54ggtnuera45ygcxzuftwxjvvmpuzqd.onion` | [Onion-Location](https://www.amnesty.org/) | 2026-11-25 |
| CIA | `ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion` | [Onion-Location](https://www.cia.gov/) | 2026-11-25 |
| Freedom of the Press Foundation | `fpfjxcrmw437h6z2xl3w4czl55kvkmxpapg37bbopsafdu7q454byxid.onion` | [Onion-Location](https://freedom.press/) | 2026-11-25 |
| Internet Archive | `archivep75mbjunhxc6x4j5mwjmomyxb573v42baldlqu56ruil2oiad.onion` | [Onion-Location](https://archive.org/) | 2026-11-25 |

### Tor Project

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| archive.torproject.org | `uy3qxvwzwoeztnellvvhxh7ju7kfvlsauka7avilcjg7domzxptbq7qd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| arti.torproject.org | `hjirlp6fu47kox4cnede4zlvaeq672bibss3oxgmsnsc5mdxygqshbqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| aus1.torproject.org | `ot3ivcdxmalbsbponeeq5222hftpf3pqil24q3s5ejwo5t52l65qusid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| aus2.torproject.org | `b5t7emfr2rn3ixr4lvizpi3stnni4j4p6goxho7lldf4qg4hz5hvpqid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| blog.torproject.org | `pzhdfe7jraknpj2qgu5cz2u3i4deuyfwmonvzu5i3nyw4t4bmg7o5pad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| bridges.torproject.org | `yq5jjvr7drkjrelzhut7kgclfuro65jjlivyzfmxiq2kyv5lickrl4qd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| cloud.torproject.org | `ui3cpcohcoko6aydhuhlkwqqtvadhaflcc5zb7mwandqmcal7sbwzwqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| collector.torproject.org | `pgmrispjerzzf2tdzbfp624cg5vpbvdw2q5a3hvtsbsx25vnni767yad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| collector2.torproject.org | `urscdffm73o4y6hpp3r43bgmudq42hq2ibdpkld6a7hy3qa44qbvc2yd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| community.torproject.org | `xmrhfasfg5suueegrnc4gsgyi2tyclcy5oz7f5drnrodmdtob6t2ioyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| consensus-health.torproject.org | `tkskz5dkjel4xqyw5d5l3k52kgglotwn6vgb5wrl2oa5yi2szvywiyid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| deb.tails.net | `umjqavufhoix3smyq6az2sx4istmuvsgmz4bq5u5x56rnayejoo6l2qd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| deb.torproject.org | `apow7mjfryruh65chtdydfmqfpj5btws7nbocgtaovhvezgccyjazpqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| dist.torproject.org | `scpalcwstkydpa3y7dbpkjs2dtr7zvtvdbyj3dqwkucfrwyixcl5ptqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| download.torproject.org | `vczcbkhpkhcywcyuyd7rfhu4bebsyscp2qoeyyvjva3km5py5rpisdid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| exonerator.torproject.org | `pm46i5h2lfewyx6l7pnicbxhts2sxzacvsbmqiemqaspredf2gm3dpad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| extra.torproject.org | `kkr72iohlfix5ipjg776eyhplnl2oiv5tz4h2y2bkhjix3quafvjd5ad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| forum.torproject.org | `v236xhqtyullodhf26szyjepvkbv6iitrhjgrqj4avaoukebkk6n6syd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| gitlab.torproject.org | `eweiibe6tdjsdprb4px6rqrzzcsi22m4koia44kc5pcjr7nec2rlxyad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| lists-01.torproject.org | `e6r6heg2ucmlm2po5yrxzf6k23ta5wwbt2adogjcyntlaiopytjz35yd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| metrics.torproject.org | `hctxrvjzfpvmzh2jllqhgvvkoepxb4kfzdjm6h7egcwlumggtktiftid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| moat.torproject.org | `z7m7ogzdhu43nosvjtsuplfmuqa3ge5obahixydhmzdox6owwxfoxzid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| newsletter.torproject.org | `a4ygisnerpgtc5ayerl22pll6cls3oyj54qgpm7qrmb66xrxts6y3lyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| nightlies.tbb.torproject.org | `umj4zbqdfcyevlkgqgpq6foxk3z75zzxsbgt5jqmfxofrbrjh3crbnad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| nyx.torproject.org | `3ewfgrt4gzfccp6bnquhqb266r3zepiqpnsk3falwygkegtluwuyevid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| onion.torproject.org | `xao2lxsmia2edq2n5zxg6uahx6xox2t7bfjw6b5vdzsxi7ezmqob6qid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| onionservices.torproject.org | `ttevhjjsjxz6uqqcjkbig5cycd7n7xv7cmd6f5fcvrqaaa7f3bj36wad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| openpgpkey.torproject.org | `2yldcptk56shc7lwieozoglw3t5ghty7m6mf2faysvfnzccqavbu2mad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| people.torproject.org | `5ecey6oe4rocdsfoigr4idu42cecm2j7zfogc3xc7kfn4uriehwrs6qd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| rbm.torproject.org | `nkuz2tpok7ctwd5ueer5bytj3bm42vp7lgjcsnznal3stotg6vyaakyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| rdsys-moat.torproject.org | `jcbdm4biw3aac57snk34brzc5fghbszrzde47idnlanj6kf6jmocdgqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| research.torproject.org | `xhqthou6scpfnwjyzc3ekdgcbvj76ccgyjyxp6cgypxjlcuhnxiktnqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| review.torproject.net | `zhkhhhnppc5k6xju7n25rjba3wuip73jnodicxl65qdpchrwvvsilcyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| rpm.torproject.org | `4ayyzfoh5qdrokqaejis3rdredhvf22n3migyxfudpkpunngfc7g4lqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| snowflake.torproject.org | `oljlphash3bpqtrvqpr5gwzrhroziw4mddidi5d2qa4qjejcbrmoypqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| spec.torproject.org | `i3xi5qxvbrngh3g6o7czwjfxwjzigook7zxzjmgwg5b7xnjcn5hzciad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| stem.torproject.org | `mf34jlghauz5pxjcmdymdqbe5pva4v24logeys446tdrgd5lpsrocmqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| styleguide.torproject.org | `7khzpw47s35pwo3lvtctwf2szvnq3kgglvzc22elx7of2awdzpovqmqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| submission.torproject.org | `givpjczyrb5jjseful3o5tn3tg7tidbu4gydl4sa5ekpcipivqaqnpad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| support.torproject.org | `rzuwtpc4wb3xdzrj3yeajsvm3fkq4vbeubm2tdxaqruzzzgs5dwemlad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| survey.torproject.org | `eh5esdnd6fkbkapfc6nuyvkjgbtnzq2is72lmpwbdbxepd2z7zbgzsqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| svn-archive.torproject.org | `b63iq6es4biaawfilwftlfkw6a6putogxh4iakei2ioppb7dsfucekyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| tails.net | `tzoz3bensgxyzs7da7lpgsn3a74h7hlbm4wa6ytq2tg6ktd57w22vqqd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| tb-manual.torproject.org | `dsbqrprgkqqifztta6h3w7i2htjhnq7d3qkh3c7gvc35e66rrcv66did.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| tpa.torproject.org | `65sphwmep6ti5oo3usizno67ox5jzsxxzgauzttjnqxhjtaem7wy4pyd.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| www.onion-router.net | `tttyx2vwp7ihml3vkhywwcizv6nbwrikpgeciy3qrow7l7muak2pnhad.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |
| www.torproject.org | `2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion` | [Official list](https://onion.torproject.org/) | 2026-11-25 |

### Debian

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| 10years.debconf.org | `spdobp2dcjfg3c56j37y7hmsi6tjauslqvbcgfgvhyuv37yiodphirad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| appstream.debian.org | `6swc2kxdtxwqku6ieo2bppmehqo3dncdaznvytb37fbsnanlkci3rbid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| backports-staging.debian.org | `fpwbdxpgygpxzilnlezsr64k7cp6lscbycmkq6wfzfdhjgek3pqzlmyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| backports.debian.org | `ii72bjpditizloapohdkpbepu6pkf7rz2jxgsuwebfcn5q5x6qa3xwqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| bcn2014.mini.debconf.org | `mowhzza2pmhj3zambwhaqugwtekfrqftnnrm4xvb4dzaigmp66s3mmad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| berlin2024.mini.debconf.org | `f4acfe5i73w7sdzhw27hzaz4m4nkfh5snnlhaqjk7eejfuvxgqarq2qd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| bh.mini.debconf.org | `w2likml3du2zgssusmh5lougamykso2wita3ein3afyg5x25fk44zoqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| bits.debian.org | `xpsuwzyljwcmk3vmurhw5ryvi66azdexzdabng5bqu56r6xc35puyeyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| blends.debian.org | `zhpfotmfpypyvahcz52iicir4vpqnhnboixg563yojm2itaiukegamyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| bootstrap.debian.net | `ha7gnvks566tk7g4fh7lxm3qtb6eadtcycobibw6uwa6g4icaeazcfad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| br2016.mini.debconf.org | `u65ka5qktmviha6fi4pensw3gp4qjjs5vya5esdmrwtuyenrmxr4njad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| br2017.mini.debconf.org | `q4fkpxl6wfjn24f5yzto6srtakdqmqxk4sd4ng5wdvzsemdk5e34ioad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| br2018.mini.debconf.org | `bbgf3q2u5x643cpfwkzsdih34ua4x3eusob6k2nxqve4rzza5nqn7vqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| bucharest2015.mini.debconf.org | `sw5blsaad2gd67ccvkmnma7qeimi3mepgjlv2zcz2vtcs3nct6kimuyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| busan2025.mini.debconf.org | `vi2hpchlzbgzg5oq3d2ypjeygbcninriaygenyrmswsdbuyqtft2mtad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| cambridge2024.mini.debconf.org | `jcy5dycsu5shg2cxnpojrk6a4evewvcao3uutf2ntpxfu6cxjemyn5qd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| campinas.mini.debconf.org | `2klgkbpvt6pr5yuq7jrysan6emltx6d46qhosttt22svkc3qz75h5kyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| cdbuilder-logs.debian.org | `etv6ce3pbbxvfoevihlqir2xik27rb4j2l5sqpx7d2unhtpiz3ffiqad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| cdimage-search.debian.org | `r6ogx3w3s6rg3gxm3kprurn77z2oim665yr5pcxhr76yit4g65y76zad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| chronicles.debian.org | `mowyaze2i4wfnyl5mgmhv67cditlvs4zicqbjj57lzhxfvfphd34dvqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| d-i.debian.org | `7fezvzv4qm7tly43qikg4juagwx4nyy3iwruq2xds5n64jt4j2yyvwad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| ddtp.debian.org | `iebkxzjscv4jgaucepdbdf4b7bqmcwd5peulm5cbpoavlsnkfhda5gyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debaday.debian.net | `h34nug3iwqjf2376fmmzdhgqivckzemcujmarlptfqeqtq7vya47yyad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf0.debconf.org | `s36sir2fpydvcpon3bb5oz3jghjqci3mn7z26cza5x5b4il2izrybsqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf1.debconf.org | `dywfwwrpxmyaz3cpydemb3k7qw5d5nevat6rpwzqndyj2h2xxf5vibid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf10.debconf.org | `alm6yjl2ry7kjieean3k3f3urqv6vlh2uv6bn4grsgu4vir3eannxrqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf11.debconf.org | `d6lywvnkk7grlhpvlyjrxbgqoqvzpvw2fv6j3fhk6fetmica6ayjcnid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf12.debconf.org | `nkrn33kekot25j2wh52k3xmfewip4tha6s6es4ivdy4n6ruogrhd47qd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf13.debconf.org | `l54wuyoo32aqezzte7tcta2khpzc3kgwyr7vayfx3vnoyoohajoam4qd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf14.debconf.org | `p5sdauvqlthmjuljoig7zgt6ybk7o5emng4l2he6gofvirfpkdz46rad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf15.debconf.org | `m2x4cztyasoyalil5htan3onbknasgwjsxithajk2glydlv4x3ky62yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf16.debconf.org | `tjulrdmbhkwzdvborn6r723mdyuqgolctejxm3hze2ygvmagmwei3iad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf17.debconf.org | `knyybdmc4kakd7gs4y6fvshg27t7jud5oiyrmaihijpepxbehcn7svid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf18.debconf.org | `2b5calm3k7sozky46ac65hx3edlmbssogpbg57h2iycolpmjtjwukyyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf19.debconf.org | `t6unvxtmmjiy6fap4ynahv6ntjdoqice6glvzzdlsohnuhuwa3fojlad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf2.debconf.org | `st44cej736t2jpbzaww6vbws6mhs74n5tycyr6b2vuvvreko4yigruqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf20.debconf.org | `tfrconhwbjuq4kkjds55rrzmdxhg5ousbdmwkqjjhsov3dbfhcsjakqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf21.debconf.org | `arf5sgoqvzde4vp6coqlmdjroqdngbq3rm5yd6eahndgxadmnieiivyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf22.debconf.org | `p6eqtjmvwkiw2pteelfqi4oj4nqwzb64xdvacijuavclxhcpqostipad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf23.debconf.org | `lybn62gyzy5af245ue3s3ykoegywjgexdv7ptrnnfczn2reaqv23sqqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf3.debconf.org | `ctndhon5ms5qw4zvip4lirgofkgs5f6pmxnloszzssftudzo34rbeyad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf4.debconf.org | `zqz43hjr4azeovtgr4osgdsok66d7ezawoysxxuyyw4qzia6hdhaosqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf5.debconf.org | `ibcf6qlyirfnc6vcfuv4y7k6oowwqz4jmcjbrkxov43feyqj6cnyvcqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf6.debconf.org | `cunu7dhfzpelt7cxlidw2zcjfe5b65dvsdquf562w5xiraxaqxn4mtid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf7.debconf.org | `h2zkj5xeycxb2esnyqeabuuo6ui6jlkdb72qjfi2hu3y3h5ilpmjphid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf8.debconf.org | `fb7ehq3gx3nw5rqyjuzqixvd3trpc4ps3jiiialpn2qqw6jgfvjevlad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debconf9.debconf.org | `v6ubdgugeqwitnr4cl3gijxnt5lpmxvubhr3zw5legnqioygmqlqozid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debdeltas.debian.net | `h3zfg7pvbedsteur5ruyvku7p7bvmx3tws7m5uxnes53cu6xaiscubyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| debug.mirrors.debian.org | `3lz3irtzg5i4z2sz3qca3oz3sdk3p5a3xlmz3zqwornapeofvoudajid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| dpl.debian.org | `6lgapegkgqepaeh7s6mpxv4lvf7awabky7ginkaycfmq7eko66kivcyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| dsa.debian.org | `k2htee64gyxc4zm7ssrd57zz4t5rbm2rhu4cdpfhdh7y4bkmmft7idad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| es.debconf.org | `3cgri2x3iidmaearj3aryls7w3e74jo3xxxfh2ym5y4hseit3oqvzxqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| fr.debconf.org | `uvf45xdz72xv7plztdtbc6j32pukihpegtnvdcewczrnv32acmqtamad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| fr2010.mini.debconf.org | `exid5ottpil6hacodg4bfo73ks2wqu522gqsggdslvkjm6ikfbqs46ad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| fr2012.mini.debconf.org | `b5do6pb42g3idrc3hha74bmrsavkn3xuirz3dyq4uhsp3u6ebziml6ad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| ftp.debian.org | `2s4yqjx5ul6okpp3f2gaunr2syex5jgbfpfvhxxbbjwnrsvbk5v3qbid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| ftp.ports.debian.org | `xa2v5hi4gwrvrhj3awz2v4crufymvjhkx3q25wd3n2bpf5574du4afqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| hamburg-2022.mini.debconf.org | `5pyzapaecfrn5vvjzyygp5jhe4ciuugbeba3kqah7ycdddnpt3frpryd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| hamburg-2023.mini.debconf.org | `5fyzyfcfqqww47ydvf2v226dfrxpe4xdoc6wkbacc4v5lcuh6covd3ad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| hamburg2025.mini.debconf.org | `s4nyaleuttjlpfkpz7oaqpb3ijauyttj5rryxfdwkysmym4kfhchn3yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| hamburg2026.mini.debconf.org | `jk5dcx6lz7fz6jstkrjh7hxoybixgdqkxr7fde6fvu3cpb3ym34f2sid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2010.mini.debconf.org | `2dkvaqxp4qfffcv6ifyvcrzb2t4evb2bbzkhyfw7pu3mg3jicl53qyyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2011.mini.debconf.org | `fgwzchg2oxrllptbdc6cj6gzsbemgljajbssut2h4qcevgmi2iqa3zqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2013.mini.debconf.org | `sofdtz7phy6p6u3tpjax6e5gfyhbndkpdbvwnp5ixk5v6veuvrlsdoqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2014.mini.debconf.org | `nqlupyypvmlaas6sadmw7f4kgc53dli7fuvy7q2y46ernvegfe344cyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2015.mini.debconf.org | `dojkmu4smsknvbkdek4mhpl4x3x6yhdbcgsezallhzfiafmi2ntn7oad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2016.mini.debconf.org | `hbrcmwnkjnlqcgsa6vice2azafphljnbe75yn2zr5kgqjwp7a5se6sad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2021.mini.debconf.org | `2x2rtdijbuqqw3664ktxwsv255m2m4itmhxhpcvmalqhbiztqfckmsqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| in2022.mini.debconf.org | `5v2fzjlnjwxdo25xlaj5ciqgzu3v4xtobxsiizbjoqwpq3n4utq3d4qd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| incoming.debian.org | `yhugxzj2ys6livectgptp2ohuqnchtfltetjbkn2jkyersatww2am4yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| incoming.ports.debian.org | `y63o645rjql7rm3pnw4sarqaoxrhjk3o62vhgqbkgzjouue2i7qybyad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| kanpur2026.mini.debconf.org | `hytx72zv5kaopo3g2u6smwk7hbc5piamgpn635lu7t4eoxkaj2icguyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| lintian.debian.org | `4ynqnnkbfkq327lqr4kfj2udaki224h4isbpjwj5tagxqcgzu7rv6oqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| maceio.mini.debconf.org | `do4sbqtt6pgdu2qktvxi26vmrwjfqhpojtfmfokclpfud6i7j4ebhnad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| manpages.debian.org | `cuhebenhpxdqskoodifdh5w7dkufya5xwaa3luci7252fc6hwo2dmjid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| mdco2.mini.debconf.org | `npqpz7jy56yinqeryzfhxvzkqg3qdqt3la3p3nqq6svrcgjuywyszlid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| mdcobr2020.debian.net | `zvne6gv7llbazewtpq2aox6wuiuwz3bpetducirepio5row5csnvjvid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| mdcobr2024.mini.debconf.org | `bs4pehkxbjaiqgiyg7xftd7nhphxlj3vnrh3ynadugldwxiupbgysgyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| media.debconf.org | `4ja5brrs4x4qvgquthmjkjykgxbvnfwau7ucgfb3ebclnkl5cpjyw4yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| metadata.ftp-master.debian.org | `4inahjbeyrmqzhvqbsgtcmoibz47joueo3f44rgidig6xdzmljue7uyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| metadata.security.debian.org | `3uuivcvkhvilnhpad2j5nfdl4q7tbq5b7kx5qmb62agdq2uvwqgipcid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| micronews.debian.org | `boowxjehkfc3ip6pnsrtt32s6j252rdzng5rcjhjt7yzh2ieiz5ka4yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| miniconf10.debconf.org | `2ptpv4mi2xtkcn5vrbga4wpgcm2neksgkawn7bwdfmysek6mqytjcwqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| mirror-master.debian.org | `3dglwm65senudd7vqyn6wkwpj2wnwp2rfiw4lmbfa7j6as4b5ekix2id.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| mon.debian.org | `u27zcsfqdlspd5kkzumjxhmniyqpoa3gtdlp47g3tssivsjsea7gb3yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| news.debian.net | `hg36q46xemkwvqcod2pfcuwh24aqcpgcbwqibyblu3nt7l562zahatid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| ni2013.mini.debconf.org | `cq5qgbcftje3y2xa7o6fbuazcbkcnuoxdczet66awdy4skzh676ewkad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| nz2015.mini.debconf.org | `j2bwwakp5uxzqykhmuiumj5b4sbtcb2syy4kz5ecql6sgcie7z7sctqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| onion.debian.org | `jvgypgbnfyvfopg5msp6nwr2sl2fd6xmnguq35n7rfkw3yungjn2i4yd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| openpgpkey.debian.org | `nxw6ies7yaoxybxtorhdknuwiynck4xe5hwfg6evmqoxwyk7nn7nriid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| packages.debian.org | `2s4yqjx5ul6okpp3f2gaunr2syex5jgbfpfvhxxbbjwnrsvbk5v3qbid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| penta.debconf.org | `ej2mxfuqifpvgnczbfejhegy5z664ojfmr4feyveomtglkccrzn67yad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| people.debian.org | `x6tkjqr46ghqmlqiwyllf5ufg6ciyexsxxfw2copx7cptw4aszq6fdqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| planet.debian.org | `3cbzkrvakrpetjjppdwzbzqrlkmzatjs7jbyazap5gwutj32gcltjpqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| pt2023.mini.debconf.org | `mk5hh2yiniwxnqk6jankr3biuful25ocwlzx6fqmis7uhzyee4nhbwqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| release.debian.org | `44w2g3oly2wy6f5q3x5wgdlxj3xqjmd6juhqfp73btzdpue2ujazboyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| security-debug.backend.mirrors.debian.org | `i3hhdhcoozin2qyb5yhhufszgvhz6m2zfy6n6len2gjmetvbnnxcenyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| security-team.debian.org | `juf6ppcps4bxgkoe7wdx5zgv5mwf3bbujzjjoo7dkwpz3vpkkbix3gid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| security.debian.org | `5ajw6aqf3ep7sijnscdzw77t7xq4xjpsy335yb2wiwgouo7yfxtjlmid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| summit.debconf.org | `ruye4n75ifmwqtbj6d43yczflptvz6sttdqvyb4bukds2z2j5qgivaqd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| timeline.debian.net | `ck2b4sppxizlsdj5cuwan6gdiee3fzrw6jlxep7htgy7euxa4m6uukid.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| tn23.mini.debconf.org | `a6edt446yugmd5m7ym2ffwu63mofe2z66ttnk3v7v6jrdsjcyubg3yyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| toulouse2024.mini.debconf.org | `mzhul75t6vmnka65nu2y4cdqfzybcypm2bcdf43b7j7igqgbrbz6f7ad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| tracker.debian.org | `7fgb4sq435vg7slw3u7m2ayze3imybpe7qm3htdklreoag3l6n2mtkyd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| wnpp-by-tags.debian.net | `prtmu3zoeqh4iefuwda7cbs5mbaelqfrcss5exnyayfcyhybeq3s7ryd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| www.debian.org | `5ekxbftvqg26oir5wle3p27ax3wksbxcecnm6oemju7bjra2pn26s3qd.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |
| www.ports.debian.org | `wzmhgtr235jahyxhrpj7wh675vrgouqhpyaecyn6x4r2menefypwyqad.onion` | [Official list](https://onion.debian.org/) | 2026-11-25 |

### SecureDrop tip lines

| Service | Onion address | Evidence | Last verified |
|---|---|---|---|
| Aftenposten AS | `tiykfvhb562gheutfnedysnhrxpxoztyszkqyroloyepwzxmxien77id.onion` | [SecureDrop directory](https://www.aftenposten.no/securedrop) | 2026-11-25 |
| Aftonbladet | `xm33ge4kupk5o66eqxcd2r4fqcplpqb2sbdduf5z2nw4g2jrxe57luid.onion` | [SecureDrop directory](https://www.aftonbladet.se/securedrop/) | 2026-11-25 |
| Bloomberg Industry Group | `3qqupamfznjrai6p4td7epa6pvidpumas2xjsihat73z23f37l2y52id.onion` | [SecureDrop directory](https://news.bloomberglaw.com/tips) | 2026-11-25 |
| Bloomberg News | `ogdwaroarq4p6rnfn2hl4crvldyruyc2g24435qtxmd3twhevg7dsqid.onion` | [SecureDrop directory](https://www.bloomberg.com/tips/) | 2026-11-25 |
| CBC | `gppg43zz5d2yfuom3yfmxnnokn3zj4mekt55onlng3zs653ty4fio6qd.onion` | [SecureDrop directory](https://www.cbc.ca/securedrop) | 2026-11-25 |
| Dagbladet | `ydbpz5knb6ji3bdtahhm3wo7sed6lsy5vqnwfpnhpez4bquvoexbz7qd.onion` | [SecureDrop directory](https://www.dagbladet.no/securedrop/) | 2026-11-25 |
| Der Spiegel | `q6vdlj2ukulrqk37piqgxucpcwtxzdjhvjzqrfbevuhrzimsgjltmpqd.onion` | [SecureDrop directory](https://www.spiegel.de/extra/so-nehmen-informanten-sicheren-kontakt-zum-spiegel-auf-a-1030502.html) | 2026-11-25 |
| Financial Times | `nqu6crmtnzs2hs5abo2uqni53yqsnnwqnerdxuzyz5yxairxlzjzt6yd.onion` | [SecureDrop directory](https://www.ft.com/news-tips/) | 2026-11-25 |
| Forbes | `6zonlfhh7aqtfwoyvdlad3nxn6ljecx2k6tyyy3spt43nn54q6lvncid.onion` | [SecureDrop directory](https://www.forbes.com/fdc/securedrop.html) | 2026-11-25 |
| Forbidden Stories | `fg25fqpu2dnxp24xs3jlcley4hp2inshpzek44q3czkhq3zffoqk26id.onion` | [SecureDrop directory](https://forbiddenstories.org/safebox-network-tutorial/) | 2026-11-25 |
| Greekleaks | `jatasaqcoe7lqdpcyxo7vl3e5tdvl5jgmtadfat77i25qdj6z6a4ulad.onion` | [SecureDrop directory](https://reportersunited.gr/greekleaks/) | 2026-11-25 |
| Kenneth R. Rosen | `dpsw5tvlh2pccviydqw2cz5tjszd34zcdj322oikydqvgsqwitxup7yd.onion` | [SecureDrop directory](https://kennethrrosen.com/securedrop/) | 2026-11-25 |
| New York Times | `ej3kv4ebuugcmuwxctx5ic7zxh73rnxt42soi3tdneu2c2em55thufqd.onion` | [SecureDrop directory](https://www.nytimes.com/tips) | 2026-11-25 |
| News24 | `uhmj4j5pnwbpmkebfze3qgjmkum465fvok376nxtpku5yvyv5takz6qd.onion` | [SecureDrop directory](https://www.news24.com/tips) | 2026-11-25 |
| NRK | `537ztcntpbmspja4mkpxldpsoc46mqlssnsaklqnfw3gnlpj5glcjgid.onion` | [SecureDrop directory](https://www.nrk.no/varsle/) | 2026-11-25 |
| ProPublica | `33xu4yhum2eiisxm6fntaslayop76fvaqgt3ak5dakdm3t7cub25cead.onion` | [SecureDrop directory](https://propublica.org/tips) | 2026-11-25 |
| Stefania Maurizi | `jxsb4ovmavjy3r64bak4ha63xwggf3nzf3vikvs23r2avm5rhzmaqtqd.onion` | [SecureDrop directory](https://stefaniamaurizi.it/en-contactme.html) | 2026-11-25 |
| Süddeutsche Zeitung | `udhauo3m3fh7v6yfiuornjzxn3fh6vlp4ooo3wogvghcnv5xik6mnayd.onion` | [SecureDrop directory](https://www.sueddeutsche.de/projekte/kontakt/) | 2026-11-25 |
| The Economist | `mxmddqsh4jnr4gjan37ayin3fu5ecnejxge4wjhj4i45qq5djbxdjtad.onion` | [SecureDrop directory](https://www.economist.com/securedrop/) | 2026-11-25 |
| The Globe and Mail | `a4zum5ydurvljrohxqp2rjjal5kro4ge2q2qizuonf2jubkhcr627gad.onion` | [SecureDrop directory](https://sec.theglobeandmail.com/securedrop/) | 2026-11-25 |
| The Guardian | `xp44cagis447k3lpb4wwhcqukix6cgqokbuys24vmxmbzmaq2gjvc2yd.onion` | [SecureDrop directory](https://www.theguardian.com/securedrop) | 2026-11-25 |
| The Washington Post | `vfnmxpa6fo4jdpyq3yneqhglluweax2uclvxkytfpmpkp5rsl75ir5qd.onion` | [SecureDrop directory](https://www.washingtonpost.com/securedrop) | 2026-11-25 |
| Whistleblow.co | `zuybtx2nop5cxfz4gyc7hzxpterf3pvf6zixe5cscajhlgqrexpkcoqd.onion` | [SecureDrop directory](https://www.whistleblow.co/whistleblowco-securedrop/) | 2026-11-25 |
| Whistleblower Aid | `kogbxf4ysay2qzozmg7ar45ijqmj2vxrwqa4upzqq2i7sqj7wv7wcdqd.onion` | [SecureDrop directory](https://whistlebloweraid.org/become-a-whistleblower/securedrop/) | 2026-11-25 |

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
