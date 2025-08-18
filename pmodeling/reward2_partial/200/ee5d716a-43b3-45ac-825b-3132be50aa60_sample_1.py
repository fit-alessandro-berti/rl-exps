import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
Verify_Artwork = Transition(label='Verify Artwork')
Analyze_Provenance = Transition(label='Analyze Provenance')
Set_Reserve = Transition(label='Set Reserve')
Activate_Auction = Transition(label='Activate Auction')
Monitor_Bids = Transition(label='Monitor Bids')
Adjust_Pricing = Transition(label='Adjust Pricing')
Enable_Fractional = Transition(label='Enable Fractional')
Validate_Bidders = Transition(label='Validate Bidders')
Resolve_Disputes = Transition(label='Resolve Disputes')
Distribute_Royalties = Transition(label='Distribute Royalties')
Promote_Auction = Transition(label='Promote Auction')
Process_Payments = Transition(label='Process Payments')
Confirm_Ownership = Transition(label='Confirm Ownership')
Arrange_Shipping = Transition(label='Arrange Shipping')
Track_Delivery = Transition(label='Track Delivery')
Report_Analytics = Transition(label='Report Analytics')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Verify_Artwork,
    Analyze_Provenance,
    Set_Reserve,
    Activate_Auction,
    Monitor_Bids,
    Adjust_Pricing,
    Enable_Fractional,
    Validate_Bidders,
    Resolve_Disputes,
    Distribute_Royalties,
    Promote_Auction,
    Process_Payments,
    Confirm_Ownership,
    Arrange_Shipping,
    Track_Delivery,
    Report_Analytics
])

# Define the dependencies between activities
root.order.add_edge(Verify_Artwork, Analyze_Provenance)
root.order.add_edge(Analyze_Provenance, Set_Reserve)
root.order.add_edge(Set_Reserve, Activate_Auction)
root.order.add_edge(Activate_Auction, Monitor_Bids)
root.order.add_edge(Monitor_Bids, Adjust_Pricing)
root.order.add_edge(Adjust_Pricing, Enable_Fractional)
root.order.add_edge(Enable_Fractional, Validate_Bidders)
root.order.add_edge(Validate_Bidders, Resolve_Disputes)
root.order.add_edge(Resolve_Disputes, Distribute_Royalties)
root.order.add_edge(Distribute_Royalties, Promote_Auction)
root.order.add_edge(Promote_Auction, Process_Payments)
root.order.add_edge(Process_Payments, Confirm_Ownership)
root.order.add_edge(Confirm_Ownership, Arrange_Shipping)
root.order.add_edge(Arrange_Shipping, Track_Delivery)
root.order.add_edge(Track_Delivery, Report_Analytics)