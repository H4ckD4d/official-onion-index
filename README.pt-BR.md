# Official Onion Index

Índice diário de **endereços `.onion` oficiais**. Cada endereço traz o link para a página onde o dono do serviço o publica e a data da última confirmação.

Mantido pelo **[projeto h4ckd4d](https://github.com/H4ckD4d)**. &nbsp;|&nbsp; [Read in English](README.md)

## Para que serve

Cópias falsas de sites onion são comuns, e listas de links são o caminho mais usado para cair nelas. Este índice responde a uma pergunta: *este endereço onion é mesmo o que o serviço publica?*

- Só entram endereços publicados pelo dono do serviço.
- Cada linha aponta para a prova, para você conferir.
- Um robô confere as fontes todos os dias e registra a data.
- Mercados, listas de links e endereços sem fonte oficial ficam de fora.

## Como um endereço entra

| Prova | O que significa |
|---|---|
| **Onion-Location** | O site HTTPS do dono anuncia o endereço, no cabeçalho `Onion-Location` ou em uma tag `<meta>`. É a prova mais forte. |
| **Official list** | A organização publica a lista dos próprios serviços onion (Tor Project, Debian). |
| **SecureDrop directory** | Consta no diretório da Freedom of the Press Foundation. O link leva à página do próprio veículo. |
| **Checked by hand** | Copiado por uma pessoa de uma página publicada pelo dono ou, quando ele não tem uma, da documentação do Tor Project. A data é a dessa conferência. |

Todo endereço também passa pelo código de conferência do formato onion v3, que rejeita erros de digitação.

## Onde está a lista

As tabelas ficam no [README principal](README.md#index). Os mesmos dados estão em [`data/onions.json`](data/onions.json) e [`data/onions.csv`](data/onions.csv).

## Como funciona a atualização diária

1. Um job do GitHub Actions roda todo dia às 05:23 UTC (02:23 em Brasília).
2. Ele lê cada fonte de [`config/sources.yml`](config/sources.yml) por HTTPS.
3. Valida cada endereço e junta o resultado ao índice.
4. Grava os dados novos e refaz as tabelas.

**Um endereço nunca é trocado sozinho.** Se uma fonte passa a publicar um endereço diferente para um serviço já listado, o job abre uma issue e espera. A troca pode ser legítima, mas também pode indicar que a fonte foi invadida. O mantenedor confere a página do dono e aprova em [`config/overrides.yml`](config/overrides.yml).

Nada é removido sozinho. Uma entrada que deixa de ser confirmada mantém a data antiga e recebe a marca `(stale)` depois de 14 dias.

## Confira você mesmo

Não confie nesta lista mais do que no site do próprio dono.

1. Abra o site normal do serviço no Tor Browser.
2. Se aparecer o botão **.onion available**, use-o. É o mesmo sinal que este índice lê.
3. Se não aparecer, abra o link da prova na tabela e compare os 56 caracteres.
4. Salve o endereço nos favoritos depois de conferir.

## Como contribuir

Abra uma issue com o nome do serviço, o site normal dele e a página onde o dono publica o endereço onion. Pedidos sem fonte oficial não entram.

## Créditos e licença

Os endereços pertencem aos respectivos donos; o projeto apenas reúne o que eles publicam. As fontes estão em [SOURCES.md](SOURCES.md).

Compilado e mantido pelo **projeto h4ckd4d**. Código sob licença [MIT](LICENSE). Compilação dos dados sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br), com crédito a "h4ckd4d project, Official Onion Index".

## Aviso

Índice destinado a pesquisa em segurança, jornalismo e proteção da privacidade. Constar na lista não é recomendação do serviço. Confirme sempre o endereço na fonte antes de usar.
