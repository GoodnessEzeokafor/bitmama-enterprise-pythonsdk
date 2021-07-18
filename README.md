## Bitmama Enterprse 

Python API wrapper for [Bitmama Enterprise](https://bitmama.io/).
This SDK can be used to create a crypto wallet and receive crypto transactions
https://developers.bitmama.io/

### Installation

```
pip install sdk
```

```python
// Require the library
import bitmama from sdk
```


#### Making calls to the resources
```python
bitmama = Bitmama(token, env)
print(bitmama.wallet.create_ripple_wallet("ripple label"))
```

### Examples
## create crypto wallet

```python
bitmama = Bitmama(token, env)
bitmama.wallet.create_wallet("coin label", "celo")

```


## create bitcoin wallet
```python
bitmama = Bitmama(token, env)
bitmama.wallet.create_btc_wallet("bitcoin label")

```
## create ethereum wallet
```python
bitmama = Bitmama(token, env)
bitmama.wallet.create_eth_wallet("ethereum label")

```
## create ripple wallet
```python

bitmama = Bitmama(token, env)
print(bitmama.wallet.create_ripple_wallet("ripple label"))

```
## create stellar wallet
```python
bitmama = Bitmama(token, env)
print(bitmama.wallet.create_stellar_wallet("stellar label"))
```
## create celo wallet
```python
bitmama = Bitmama(token, env)
print(bitmama.wallet.create_celo_wallet("celo label"))

```

## get crypto wallet
```python
bitmama = Bitmama(token, env)
pagination = {"page":1,"size":40}
print(bitmama.wallet.list_crypto_wallets('xrp', pagination))

```
## get bitmama wallet
```python
bitmama = Bitmama(token, env)
print(bitmama.wallet.enterprise_wallet())
```
## list banks
```python
bitmama = Bitmama(token, env)
print(bitmama.banks.list_banks("ng"))
```

## get webhook
```python
bitmama = Bitmama(token, env)
print(bitmama.banks.get_webhook())
```

## create webhook
```python
bitmama = Bitmama(token, env)
print(bitmama.banks.create_webhook(endpoint))

```
## get tickers
```python
bitmama = Bitmama(token, env)
print(bitmama.tickers())
```
## get exchange rate
```python
bitmama = Bitmama(token, env)
print(bitmama.get_rate('btcngn'))
```


## COMING SOON
* btc_eth_rate
* btc_usdt_rate
* btc_usdc_rate
* btc_xrp_rate
* btc_xlm_rate
* btc_celo_rate
* btc_cusd_rate
* btc_ceur_rate
* btc_NGN_rate
* btc_GHS_rate
* btc_usd_rate
* eth_NGN_rate
* eth_GHS_rate
* eth_btc_rate
* eth_celo_rate
* eth_xrp_rate
* eth_xlm_rate
* eth_cusd_rate
* eth_usdt_rate
* eth_usdc_rate
* eth_ceur_rate
* eth_usd_rate
* celo_NGN_rate
* celo_GHS_rate
* celo_USD_rate
* celo_eth_rate 
* celo_btc_rate
* celo_xrp_rate
* celo_xlm_rate
* celo_cusd_rate
* celo_ceur_rate
* celo_usdt_rate
* celo_usdc_rate
* xrp_NGN_rate
* xrp_GHS_rate
* xrp_USD_rate
* xrp_btc_rate
* xrp_eth_rate
* xrp_xlm_rate
* xrp_usdt_rate
* xrp_usdc_rate
* xrp_cusd_rate
* xrp_ceur_rate
* xlm_NGN_rate
* xlm_GHS_rate
* xlm_USD_rate
* xlm_btc_rate
* xlm_eth_rate
* xlm_xrp_rate
* xlm_usdt_rate
* xlm_usdc_rate
* xlm_cusd_rate
* xlm_ceur_rate
* usdt_NGN_rate
* usdt_GHS_rate
* usdt_USD_rate
* usdt_btc_rate
* usdt_eth_rate
* usdt_xrp_rate
* usdt_xlm_rate
* usdt_usdc_rate
* usdt_cusd_rate
* usdt_ceur_rate
* usdc_NGN_rate
* usdc_GHS_rate
* usdc_USD_rate
* usdc_btc_rate
* usdc_eth_rate
* usdc_xrp_rate
* usdc_xlm_rate
* usdc_cusd_rate
* usdc_ceur_rate
* cusd_NGN_rate
* cusd_GHS_rate
* cusd_USD_rate
* cusd_btc_rate
* cusd_eth_rate
* cusd_xrp_rate
* cusd_xlm_rate
* cusd_usdc_rate
* cusd_ceur_rate
* ceur_NGN_rate
* ceur_GHS_rate
* ceur_USD_rate
* ceur_btc_rate
* ceur_eth_rate
* ceur_xrp_rate
* ceur_xlm_rate
* ceur_cusd_rate




## Contribution Guidelines
* create a new branch
* make sure new branch and main branch are in sync
* after updating codebase write tests and make sure the all pass
