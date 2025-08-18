import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[compliance_scan, silent_transition])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, silent_transition])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[remote_audit, silent_transition])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[auction_setup, silent_transition])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[bid_monitoring, silent_transition])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[fraud_detection, silent_transition])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[ownership_transfer, silent_transition])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[payment_clearing, silent_transition])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[tax_calculation, silent_transition])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[fund_allocation, silent_transition])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[dispute_handling, silent_transition])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[report_generation, silent_transition])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_update, silent_transition])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[asset_listing, valuation_check])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, loop)