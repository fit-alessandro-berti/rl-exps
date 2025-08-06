import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Asset ID', 'Value Assess', 'Risk Scan', 'Market Review', 'Initial Offer', 'Counter Offer', 'Negotiation', 'Contract Draft', 'Legal Review', 'Digital Sign', 'Royalty Setup', 'Transfer Record', 'Compliance Check', 'Audit Schedule', 'Market Feedback', 'Strategy Update']

# Create the POWL model
root = StrictPartialOrder()

# Add activities to the model
for activity in activities:
    root.nodes.append(Transition(label=activity))

# Define the transitions
Asset_ID = Transition(label='Asset ID')
Value_Assess = Transition(label='Value Assess')
Risk_Scan = Transition(label='Risk Scan')
Market_Review = Transition(label='Market Review')
Initial_Offer = Transition(label='Initial Offer')
Counter_Offer = Transition(label='Counter Offer')
Negotiation = Transition(label='Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Legal_Review = Transition(label='Legal Review')
Digital_Sign = Transition(label='Digital Sign')
Royalty_Setup = Transition(label='Royalty Setup')
Transfer_Record = Transition(label='Transfer Record')
Compliance_Check = Transition(label='Compliance Check')
Audit_Schedule = Transition(label='Audit Schedule')
Market_Feedback = Transition(label='Market Feedback')
Strategy_Update = Transition(label='Strategy Update')

# Define the exclusive choice nodes
market_review_choice = OperatorPOWL(operator=Operator.XOR, children=[Market_Review, Counter_Offer])
initial_offer_choice = OperatorPOWL(operator=Operator.XOR, children=[Initial_Offer, Counter_Offer])

# Define the loops
negotiation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Negotiation, Market_Review])
legal_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[Legal_Review, Digital_Sign])
royalty_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[Royalty_Setup, Contract_Draft])
compliance_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Check, Audit_Schedule])

# Define the partial order
root.nodes.extend([Asset_ID, Value_Assess, Risk_Scan, market_review_choice, initial_offer_choice, negotiation_loop, legal_review_loop, royalty_setup_loop, compliance_check_loop, Transfer_Record, Market_Feedback, Strategy_Update])

# Define the order dependencies
root.order.add_edge(Asset_ID, Value_Assess)
root.order.add_edge(Value_Assess, Risk_Scan)
root.order.add_edge(Risk_Scan, market_review_choice)
root.order.add_edge(market_review_choice, initial_offer_choice)
root.order.add_edge(initial_offer_choice, negotiation_loop)
root.order.add_edge(negotiation_loop, legal_review_loop)
root.order.add_edge(legal_review_loop, royalty_setup_loop)
root.order.add_edge(royalty_setup_loop, compliance_check_loop)
root.order.add_edge(compliance_check_loop, Transfer_Record)
root.order.add_edge(Transfer_Record, Market_Feedback)
root.order.add_edge(Market_Feedback, Strategy_Update)

# Print the POWL model
print(root)