from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
onboard = Transition(label='Artist Onboard')
verify = Transition(label='Asset Verify')
check = Transition(label='Identity Check')
deploy = Transition(label='Smart Deploy')
bid_monitor = Transition(label='Bid Monitor')
price_adjust = Transition(label='Price Adjust')
link = Transition(label='Wallet Link')
submit = Transition(label='Bid Submit')
close = Transition(label='Auction Close')
transfer = Transition(label='Ownership Transfer')
release = Transition(label='Fund Release')
review = Transition(label='Dispute Review')
update = Transition(label='Reputation Update')
fractional = Transition(label='Fractional Offer')
secondary = Transition(label='Secondary Sale')

# Define silent transitions (empty labels)
skip_onboard = SilentTransition()
skip_verify = SilentTransition()
skip_check = SilentTransition()
skip_deploy = SilentTransition()
skip_bid_monitor = SilentTransition()
skip_price_adjust = SilentTransition()
skip_link = SilentTransition()
skip_submit = SilentTransition()
skip_close = SilentTransition()
skip_transfer = SilentTransition()
skip_release = SilentTransition()
skip_review = SilentTransition()
skip_update = SilentTransition()
skip_fractional = SilentTransition()
skip_secondary = SilentTransition()

# Create POWL model
root = StrictPartialOrder(
    nodes=[
        onboard,
        verify,
        check,
        deploy,
        bid_monitor,
        price_adjust,
        link,
        submit,
        close,
        transfer,
        release,
        review,
        update,
        fractional,
        secondary,
    ],
    order=[
        (onboard, verify),
        (verify, check),
        (check, deploy),
        (deploy, bid_monitor),
        (bid_monitor, price_adjust),
        (price_adjust, link),
        (link, submit),
        (submit, close),
        (close, transfer),
        (transfer, release),
        (release, review),
        (review, update),
        (update, fractional),
        (fractional, secondary),
    ]
)