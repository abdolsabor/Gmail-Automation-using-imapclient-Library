from imapclient import IMAPClient

# context manager ensures the session is cleaned up
with IMAPClient(host="imap.gmail.com") as client:
    client.login('Email here', 'password here') #Enter EMail and passowrd
    client.select_folder('[Gmail]/Spam')

    # search criteria are passed in a straightforward way
    # (nesting is supported)
    messages = client.search(['NOT', 'DELETED'])
    

    # fetch selectors are passed as a simple list of strings.
    response = client.fetch(messages, ['ENVELOPE'])
    response2 = client.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
    #print(response)
    for data in response:
        print(data , response[data])
        print('\n')

    # `response` is keyed by message id and contains parsed,
    # converted response items.
    for message_id, data in response2.items():
        print('{id}: {size} bytes, flags={flags}'.format(
            id=message_id,
            size=data[b'RFC822.SIZE'],
            flags=data[b'FLAGS']))

    client.move(messages, 'INBOX')
    print("SPAM EMAIL MOVED TO INBOX")

    
