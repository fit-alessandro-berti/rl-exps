import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
asset_listing = Transition(label='Asset Listing')
valuation_check = Transition(label='Valuation Check')
compliance_scan = Transition(label='Compliance Scan')
legal_review = Transition(label='Legal Review')
remote_audit = Transition(label='Remote Audit')
auction_setup = Transition(label='Auction Setup')
bid_monitoring = Transition(label='Bid Monitoring')
fraud_detection = Transition(label='Fraud Detection')
ownership_transfer = Transition(label='Ownership Transfer')
payment_clearing = Transition(label='Payment Clearing')
tax_calculation = Transition(label='Tax Calculation')
fund_allocation = Transition(label='Fund Allocation')
dispute_handling = Transition(label='Dispute Handling')
report_generation = Transition(label='Report Generation')
stakeholder_update = Transition(label='Stakeholder Update')

# Create the root partial order
root = StrictPartialOrder(nodes=[
    asset_listing,
    valuation_check,
    compliance_scan,
    legal_review,
    remote_audit,
    auction_setup,
    bid_monitoring,
    fraud_detection,
    ownership_transfer,
    payment_clearing,
    tax_calculation,
    fund_allocation,
    dispute_handling,
    report_generation,
    stakeholder_update
])

# No additional dependencies for this simple workflow
# So we don't need to add edges here

# The final result is stored in 'root'
print(root)