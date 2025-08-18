root = StrictPartialOrder(nodes=[
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
])

root.order.add_edge(Transition(label='Artist Onboard'), Transition(label='Asset Verify'))
root.order.add_edge(Transition(label='Asset Verify'), Transition(label='Identity Check'))
root.order.add_edge(Transition(label='Identity Check'), Transition(label='Smart Deploy'))
root.order.add_edge(Transition(label='Smart Deploy'), Transition(label='Bid Monitor'))
root.order.add_edge(Transition(label='Bid Monitor'), Transition(label='Price Adjust'))
root.order.add_edge(Transition(label='Price Adjust'), Transition(label='Wallet Link'))
root.order.add_edge(Transition(label='Wallet Link'), Transition(label='Bid Submit'))
root.order.add_edge(Transition(label='Bid Submit'), Transition(label='Auction Close'))
root.order.add_edge(Transition(label='Auction Close'), Transition(label='Ownership Transfer'))
root.order.add_edge(Transition(label='Auction Close'), Transition(label='Fund Release'))
root.order.add_edge(Transition(label='Ownership Transfer'), Transition(label='Fund Release'))
root.order.add_edge(Transition(label='Fund Release'), Transition(label='Dispute Review'))
root.order.add_edge(Transition(label='Dispute Review'), Transition(label='Reputation Update'))
root.order.add_edge(Transition(label='Reputation Update'), Transition(label='Fractional Offer'))
root.order.add_edge(Transition(label='Fractional Offer'), Transition(label='Secondary Sale'))