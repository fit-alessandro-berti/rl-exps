import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transition for exit
exit_transition = SilentTransition()

# Define the loop for remote audit and auction setup
remote_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[remote_audit, auction_setup])

# Define the choice for legal review and remote audit loop
legal_review_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_review, remote_audit_loop])

# Define the choice for bid monitoring and dispute handling
bid_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[bid_monitoring, dispute_handling])

# Define the choice for fraud detection and fund allocation
fraud_detection_choice = OperatorPOWL(operator=Operator.XOR, children=[fraud_detection, fund_allocation])

# Define the choice for tax calculation and report generation
tax_calculation_choice = OperatorPOWL(operator=Operator.XOR, children=[tax_calculation, report_generation])

# Define the choice for payment clearing and stakeholder update
payment_clearing_choice = OperatorPOWL(operator=Operator.XOR, children=[payment_clearing, stakeholder_update])

# Define the final choice for exit and stakeholder update
exit_choice = OperatorPOWL(operator=Operator.XOR, children=[exit_transition, stakeholder_update])

# Define the partial order with all the transitions and choices
root = StrictPartialOrder(nodes=[asset_listing, valuation_check, compliance_scan, legal_review_choice, remote_audit_loop, bid_monitoring_choice, fraud_detection_choice, payment_clearing_choice, tax_calculation_choice, exit_choice])

# Add the edges to the partial order
root.order.add_edge(asset_listing, valuation_check)
root.order.add_edge(valuation_check, compliance_scan)
root.order.add_edge(compliance_scan, legal_review_choice)
root.order.add_edge(legal_review_choice, remote_audit_loop)
root.order.add_edge(remote_audit_loop, bid_monitoring_choice)
root.order.add_edge(bid_monitoring_choice, fraud_detection_choice)
root.order.add_edge(fraud_detection_choice, payment_clearing_choice)
root.order.add_edge(payment_clearing_choice, tax_calculation_choice)
root.order.add_edge(tax_calculation_choice, exit_choice)
root.order.add_edge(exit_choice, stakeholder_update)

print(root)