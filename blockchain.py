genesis_block= {
    'previous_hash':'',
    'index': 0,
    'transaction':[]
}
blockchain = [genesis_block]

open_transaction= []
owner= 'Gracie'

def get_last_value():
    if len(blockchain) < 1:
       return None
    return blockchain[-1]

# def add_values(val, last_transcation= [15]):
#     blockchain.append([last_transcation,val])
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

def open_mine():
    last_block= blockchain[-1]
    hashed_block= ''
    for key in last_block:
        value= last_block[key]
        hashed_block=hashed_block + str(value)
        print(hashed_block)
    block= {
        'previous_hash':hashed_block,
        'index': len(blockchain),
        'transaction':open_transaction
    }
    blockchain.append(block)

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
    block_index = 0
    is_valid = True
    for block_index in range (len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid
waiting_for_input= True
while True:
    print("Please Choose:")
    print("1: Add a new Transaction")
    print("A: Mine a block")
    print("2: Output the current Transaction")
    print("3: quit")
    print("4: manipulate")
    user_choice= get_user_choice()
    if user_choice== "1" :
        tx_data= get_user_input()
        recipient, amount= tx_data   
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice== "A":
        open_mine()
    elif user_choice == "2" :
        print_blockchain_elements()
    elif user_choice =="3" :
        break
    elif user_choice == "4":
        if len(blockchain)>=1:
            blockchain[0]= [2]

    else:
        print("The input was invalid, please select those from the list!")
    # if not verify_chain():
    #     print("invalid blockchain")
    #     break
else:
    print("User left!")
print("You're done")
        
    
