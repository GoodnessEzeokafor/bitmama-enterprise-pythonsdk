## Bitmama Enterprse 

Python API wrapper for [Bitmama Enterprise](https://bitmama.io/).
This SDK can be used to create a crypto wallet and receive crypto transactions
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
## get exchange rage
```python
bitmama = Bitmama(token, env)
print(bitmama.get_rate('btcngn'))
```
