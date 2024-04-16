from Wallet import Wallet

wallet_1 = Wallet()
wallet_2 = Wallet()
wallet_3 = Wallet()
wallet_4 = Wallet()
wallet_5 = Wallet()


tx12 = wallet_1.create_tx(wallet_2.public_key_string(), 20, "TRANSFER")
tx13 = wallet_1.create_tx(wallet_3.public_key_string(), 30, "TRANSFER")

tx23 = wallet_2.create_tx(wallet_3.public_key_string(), 10, "TRANSFER")
tx24 = wallet_2.create_tx(wallet_4.public_key_string(), 10, "TRANSFER")

tx34 = wallet_3.create_tx(wallet_4.public_key_string(), 15, "TRANSFER")
tx35 = wallet_3.create_tx(wallet_5.public_key_string(), 20, "TRANSFER")

tx41 = wallet_4.create_tx(wallet_1.public_key_string(), 20, "TRANSFER")
tx42 = wallet_4.create_tx(wallet_2.public_key_string(), 15, "TRANSFER")

tx53 = wallet_5.create_tx(wallet_3.public_key_string(), 10, "TRANSFER")
tx54 = wallet_5.create_tx(wallet_4.public_key_string(), 5, "TRANSFER")
