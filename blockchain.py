MINING_REWARD= 10

genesis_block= {
    'previous_hash':'',
    'index': 0,
    'transaction':[]
}
blockchain = [genesis_block]

open_transaction= []
owner= 'Gracie'
participants= {'Gracie'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_value():
    if len(blockchain) < 1:
       return None
    return blockchain[-1]

def get_balance(participant):
    tx_sender= [[tx['amount'] for tx in block['transaction'] if tx['sender']==participant] for block in blockchain]
    amount_sent= 0
    for tx in tx_sender:
        if len(tx)> 0:
            amount_sent +=tx[0]

    tx_recipient= [[tx['amount'] for tx in block['transaction'] if tx['recipient']==participant] for block in blockchain]
    amount_received= 0
    for tx in tx_recipient:
        if len(tx)> 0:
            amount_received +=tx[0]
    return amount_received- amount_sent


def add_transaction(recipient, sender= owner, amount= 1.0):
    # if last_transaction == None :
    #     last_transaction = [15]
       
    # blockchain.append([last_transaction, transaction_amount])
    transaction= {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    open_transaction.append(transaction)
    participants.add(sender)
    participants.add(recipient)

def open_mine():
    last_block= blockchain[-1]
    hashed_block=hash_block(last_block)


    print(hashed_block)
    reward_transaction= {
        'sender':'Mining',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    open_transaction.append(reward_transaction)
    block= {
        'previous_hash':hashed_block,
        'index': len(blockchain),
        'transaction':open_transaction
    }
    blockchain.append(block)
    return True

def get_user_input():
    tx_receiver= input("Please enter the recipient name:")
    tx_amount= float(input("Please enter your Transaction Amount:"))
    return tx_receiver, tx_amount

def get_user_choice():
    user_input= input("Enter your Choice:")
    return user_input

def print_blockchain_elements():

    for block in blockchain:
            print("outputting block")
            print(block)
    else: 
        print('-' * 20)


def verify_chain():
    for (index, block )in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index -1]):
            return False
    return True



waiting_for_input= True
while True:
    print("Please Choose:")
    print("1: Add a new Transaction")
    print("A: Mine a block")
    print("2: Output the current Transaction")
    print("3: quit")
    print("4: output participants")
    print("5: manipulate")
   
    user_choice= get_user_choice()
    if user_choice== "1" :
        tx_data= get_user_input()
        recipient, amount= tx_data   
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice== "A":
        if open_mine():
            open_transaction = []
    elif user_choice == "2" :
        print_blockchain_elements()
    elif user_choice =="3" :
        break
    elif user_choice =="4":
        print(participants)
    elif user_choice == "5":
        if len(blockchain)>=1:
            blockchain[0]=  {
               'previous_hash':'',
               'index': 0,
               'transaction':[]
            }

    else:
        print("The input was invalid, please select those from the list!")
    if not verify_chain():
        print("invalid blockchain")
        break
    print(get_balance('Gracie'))
else:
    print("User left!")
print("You're done")
        
    
