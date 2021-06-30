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