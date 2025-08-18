root = StrictPartialOrder(
    nodes=[
        Transition(label='Artist Onboard'),
        Transition(label='Asset Verify'),
        Transition(label='Identity Check'),
        Transition(label='Smart Deploy'),
        Transition(label='Bid Monitor'),
        Transition(label='Price Adjust'),
        Transition(label='Wallet Link'),
        Transition(label='Bid Submit'),
        Transition(label='Auction Close'),
        Transition(label='Ownership Transfer'),
        Transition(label='Fund Release'),
        Transition(label='Dispute Review'),
        Transition(label='Reputation Update'),
        Transition(label='Fractional Offer'),
        Transition(label='Secondary Sale')
    ],
    order={
        ('Artist Onboard', 'Asset Verify'): 1,
        ('Asset Verify', 'Identity Check'): 1,
        ('Identity Check', 'Smart Deploy'): 1,
        ('Smart Deploy', 'Bid Monitor'): 1,
        ('Bid Monitor', 'Price Adjust'): 1,
        ('Price Adjust', 'Wallet Link'): 1,
        ('Wallet Link', 'Bid Submit'): 1,
        ('Bid Submit', 'Auction Close'): 1,
        ('Auction Close', 'Ownership Transfer'): 1,
        ('Ownership Transfer', 'Fund Release'): 1,
        ('Fund Release', 'Dispute Review'): 1,
        ('Dispute Review', 'Reputation Update'): 1,
        ('Reputation Update', 'Fractional Offer'): 1,
        ('Fractional Offer', 'Secondary Sale'): 1
    }
)