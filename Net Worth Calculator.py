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
print()
print('Open MetaMask Ethereum Main Network.')
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

# Metamask Avalanche Network
print()
print('Open Metamask Avalanche Network.')
metamask_avalanche_balance = float(input('What is the balance in your MetaMask Avalanche Network? '))

# traderjoexyz.com
print()
print('Open traderjoexyz.com')
print()
print('Click the Lend tab.')
traderjoexyz_lending_supply = float(input('How much is your Supply Balance? '))
joe_balance = float(input('What is the value of your JOE Rewards? '))
joe_price = float(input('What is the current price of JOE according to CoinMarketCap? '))
joe_rewards = joe_balance * joe_price
print(f'You have ${joe_rewards} worth of JOE rewards.')
print()
avax_balance = float(input('What is the value of your AVAX Rewards? '))
avax_price = float(input('What is the current price of AVAX according to CoinMarketCap? '))
avax_rewards = avax_balance * avax_price
print(f'You have ${avax_rewards} worth of avax rewards.')
print()
print('CLick the Farm tab.')
melt_avax_balance = float(input('How much MELT/AVAX do you have staked? '))
melt_avax_pending_rewards = float(input('How much Pending Rewards do you have? '))
melt_avax_bonus_rewards = float(input('How much Bonus Rewards do you have? '))

# Wonderland
print()
print('Open Wonderland.')
memo_balance = float(input('How much MEMO do you have? '))
time_value = float(input('What is the USD value of TIME according to CoinMarketCap? '))
memo_value = memo_balance * time_value
print(f'You have ${memo_value} worth of MEMO.')

# Crypto.com App
print()
crypto_dot_com_balance = float(input("What's the balance of your Crypto.com account? "))

# Mint
print()
mint_net_worth = float(input('How much does Mint say your annual net worth changed? '))

# KuCoin
print()
KuCoin_balance = float(input('What is the balance of your KuCoin account? '))

# Algorand App
print()
algorand_app_balance = float(input('What is the balance of your Algorand account? '))

# Helium App
print()
helium_balance = float(input('What is the balance of your Helium account? '))

# Coinbase Wallet App, NOT Coinbase App
print()
coinbase_wallet_balance = float(input('What is the balance of your Coinbase Wallet? '))

# Trust Wallet
print()
trust_wallet_balance = float(input('What is the balance of your Trust Wallet? '))

# Pancake Swap
print()
print('Go to PancakeSwap.')
# Farm
print('Click the Farms tab under Earn.')
cake_earned = float(input('How much CAKE have you earned? '))
kart_bnb_staked = float(input('How much KART-BNB is staked? '))
# Pool
print()
print('Switch to the Pools tab.')
PancakeSwap_kart_balance = float(input('How much KART have you earned? '))
PancakeSwap_KART_pooled_amount = float(input('How much USD do you have staked in the KART pool? '))
# Liquidity
print()
print('Click the Liquidity tab under Trade.')
mcrt_bnb_lp = float(input('How much BNB is in your MCRT-BNB LP paid? '))
mcrt_bnb_value = 2 * mcrt_bnb_lp
mcrt_bnb_usd = float(input(f'Plug {mcrt_bnb_value} BNB into Coingecko. How much USD is that? '))
print(f'You have ${mcrt_bnb_usd} in your MCRT-BNB LP.')

print()
annual_change = round(float(
    XYO_CoinGecko_plug + matic_staked_balance + matic_rewards_balance + crypto_dot_com_balance + mint_net_worth +
    metamask_ethereum_balance + metamask_smartchain_balance + KuCoin_balance + algorand_app_balance + helium_balance +
    mtv_staked + coinbase_wallet_balance + trust_wallet_balance + PancakeSwap_kart_balance +
    PancakeSwap_KART_pooled_amount + cake_earned + kart_bnb_staked + metamask_avalanche_balance +
    traderjoexyz_lending_supply + joe_rewards + avax_rewards + melt_avax_bonus_rewards + melt_avax_pending_rewards +
    melt_avax_balance + memo_value + mcrt_bnb_usd),
    2)
daily_change = round(float(annual_change / 365), 2)
print(f'Your net worth changed by ${annual_change} this year.')
print(f'Your net worth changed by about ${daily_change} daily.')
