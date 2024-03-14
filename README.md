# httpie-shinkansen

[Shinkansen](http://shinkansen.finance)  plugin for [HTTPie](http://httpie.org).

This plugin sign payload and add header `shinkansen-jws-signature` to each request.

In order to use it you **must** set one pair of environment variables:

Plain text certificates

- SHINKANSEN_CERTIFICATE
- SHINKANSEN_KEY

Path to certificates

- SHINKANSEN_CERTIFICATE_PATH
- SHINKANSEN_KEY_PATH

Certificates must be PEM encoded and no password. Plain text has prevalence.

## Usage

    $ http post --auth-type=shinkansen dev.shinkansen.finance/api/payout <body>

## Installation

    $ pip install httpie-shinkansen

or

    $ httpie cli plugins install httpie-shinkansen

## Development
Install this plugin directly into httpie

    $ httpie cli plugins install -e <path_to_repo>

Run it

    $ http post --auth-type=shinkansen example.org

Uninstall a re install to bring new changes

    $ httpie plugins uninstall httpie-shinkansen