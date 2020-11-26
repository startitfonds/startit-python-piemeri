# startit-python-piemeri

Piemēri dažādu Python bibliotēku lietošanai

## Autentifikācija ar GitHub

1. Jāizveido jauna OAuth aplikācija GitHub <https://github.com/settings/applications/new> . Tur kā "Homepage URL" jānorāda <http://localhost:5000> un "Authorization callback URL" - <http://localhost:5000/gh-callback>
1. Jāuzģenerē jauns *Client secret*
1. Jānodefinē CLIENT_ID un CLIENT_SECRET:

```sh
export CLIENT_ID=myid
export CLIENT_SECRET=mysecret
```

Pārbauda vai strādā aizejot uz <http://localhost:5000>
