from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
artist_onboard = Transition(label='Artist Onboard')
verify_asset = Transition(label='Asset Verify')
identity_check = Transition(label='Identity Check')
smart_deploy = Transition(label='Smart Deploy')
bid_monitor = Transition(label='Bid Monitor')
price_adjust = Transition(label='Price Adjust')
wallet_link = Transition(label='Wallet Link')
bid_submit = Transition(label='Bid Submit')
auction_close = Transition(label='Auction Close')
ownership_transfer = Transition(label='Ownership Transfer')
fund_release = Transition(label='Fund Release')
dispute_review = Transition(label='Dispute Review')
reputation_update = Transition(label='Reputation Update')
fractional_offer = Transition(label='Fractional Offer')
secondary_sale = Transition(label='Secondary Sale')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        artist_onboard, verify_asset, identity_check, smart_deploy,
        bid_monitor, price_adjust, wallet_link, bid_submit, auction_close,
        ownership_transfer, fund_release, dispute_review, reputation_update,
        fractional_offer, secondary_sale
    ],
    order=[
        (artist_onboard, verify_asset),
        (verify_asset, identity_check),
        (identity_check, smart_deploy),
        (smart_deploy, bid_monitor),
        (bid_monitor, price_adjust),
        (price_adjust, wallet_link),
        (wallet_link, bid_submit),
        (bid_submit, auction_close),
        (auction_close, ownership_transfer),
        (ownership_transfer, fund_release),
        (fund_release, dispute_review),
        (dispute_review, reputation_update),
        (reputation_update, fractional_offer),
        (fractional_offer, secondary_sale)
    ]
)