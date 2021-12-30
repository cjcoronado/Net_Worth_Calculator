#  This script was crated to calculate my net worth across all my accounts, including crypto wallets. I track my fiat
#  currency using Mint. The majority of my crypto wallets are not able to sync with Mint. With this script, I answer a
#  few questions regarding wallet balances, then my change in net worth (annual and daily) are printed. All mentioned
#  wallets are ones I personally use.
coin_balance = float(input('How much COIN do you have in USD? '))  # Check conversion rate, price using Coingecko.
matic_staked_balance = float(input('How much Matic do you have staked? '))
matic_rewards_balance = float(input('How much Matic have you earned? '))
crypto_dot_com_balance = float(input("What's the balance of your Crypto.com account? "))
mint_net_worth = float(input('How much does Mint say your annual net worth changed? '))
metamask_balance = float(input('What is the balance on your MetaMask account? '))
kucoin_balance = float(input('What is the balance of your KuCoin account? '))
algorand_app_balance = float(input('What is the balance of your Algorand account? '))
helium_balance = float(input('What is the balance of your Helium account? '))
mtv_staked = float(input('How much MTV (in USD) do you have staked? '))  # Price using Coingecko.
coinbase_wallet_balance = float(input('What is the balance of your Coinbase Wallet? '))
annual_change = round(float(
    coin_balance + matic_staked_balance + matic_rewards_balance + crypto_dot_com_balance + mint_net_worth +
    metamask_balance + kucoin_balance + algorand_app_balance + helium_balance + mtv_staked +
    coinbase_wallet_balance), 2)
daily_change = round(float(annual_change / 365), 2)
print(f'Your net worth changed by ${annual_change} this year.')
print(f'Your net worth changed by about ${daily_change} daily.')
