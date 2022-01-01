#  This script was crated to calculate my net worth across all my accounts, including crypto wallets. I track my fiat
#  currency using Mint. The majority of my crypto wallets are not able to sync with Mint. With this script, I answer a
#  few questions regarding wallet balances, then my change in net worth (annual and daily) are printed. All mentioned
#  wallets are ones I personally use.

# COIN App
coin_balance = float(input('How much COIN do you have? '))
denominator = coin_balance / 1000
numerator = float(input('How much XYO do you get from 1000 COIN? '))
COIN_to_xyo = round((numerator * denominator), 3)
XYO_CoinGecko_plug = float(input(f'Enter USD from CoinGecko for {COIN_to_xyo} XYO. '))

# Metamask Ethereum Chain
print('Open MetaMask Ethereum Chain.')
metamask_ethereum_balance = float(input('What is the balance on your MetaMask Ethereum wallet? '))  # MetaMask Ethereum
matic_staked_balance = float(input('How much Matic do you have staked? '))  # MetaMask Ethereum
matic_rewards_balance = float(input('How much Matic have you earned? '))  # MetaMask Ethereum

# Metamask Smart Chain
print()
print('Open MetaMask Binance Smart Chain Mainnet.')
metamask_smartchain_balance = float(input('What is the balance in your MetaMask Binance Smart Chain Mainnet? '))

# Metamask MultiVAC Mainnet
print()
print('Open MetaMask MultiVAC Mainnet.')
print('Stake any accumulated MTV now.')
mtv_staked = float(input('How much MTV (in USD) do you have staked? '))  # Price using CoinGecko.

# Crypto.com App
crypto_dot_com_balance = float(input("What's the balance of your Crypto.com account? "))

# Mint
mint_net_worth = float(input('How much does Mint say your annual net worth changed? '))

# KuCoin
KuCoin_balance = float(input('What is the balance of your KuCoin account? '))

# Algorand App
algorand_app_balance = float(input('What is the balance of your Algorand account? '))

# Helium App
helium_balance = float(input('What is the balance of your Helium account? '))

# Coinbase Wallet App, NOT Coinbase App
coinbase_wallet_balance = float(input('What is the balance of your Coinbase Wallet? '))

# Trust Wallet
trust_wallet_balance = float(input('What is the balance of your Trust Wallet? '))

# Pancake Swap
# Farm
cake_earned = float(input('How much CAKE have you earned? '))
kart_bnb_staked = float(input('How much KART-BNB is staked? '))
# Pool
PancakeSwap_kart_balance = float(input('How much KART have you earned? '))
PancakeSwap_KART_pooled_amount = float(input('How much USD do you have staked in the KART pool? '))
PancakeSwap_autoCake_balance = float(input('How much Cake do you have from PancakeSwap AutoCake? '))

annual_change = round(float(
    XYO_CoinGecko_plug + matic_staked_balance + matic_rewards_balance + crypto_dot_com_balance + mint_net_worth +
    metamask_ethereum_balance + metamask_smartchain_balance + KuCoin_balance + algorand_app_balance + helium_balance +
    mtv_staked + coinbase_wallet_balance + trust_wallet_balance + PancakeSwap_autoCake_balance + PancakeSwap_kart_balance
    + PancakeSwap_KART_pooled_amount + cake_earned + kart_bnb_staked),
    2)
daily_change = round(float(annual_change / 365), 2)
print(f'Your net worth changed by ${annual_change} this year.')
print(f'Your net worth changed by about ${daily_change} daily.')
