from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
data_capture = Transition(label='Data Capture')
trend_scan = Transition(label='Trend Scan')
idea_workshop = Transition(label='Idea Workshop')
concept_draft = Transition(label='Concept Draft')
expert_review = Transition(label='Expert Review')
prototype_build = Transition(label='Prototype Build')
regulation_check = Transition(label='Regulation Check')
ip_alignment = Transition(label='IP Alignment')
supply_sync = Transition(label='Supply Sync')
market_mapping = Transition(label='Market Mapping')
pilot_launch = Transition(label='Pilot Launch')
feedback_loop = Transition(label='Feedback Loop')
design_iterate = Transition(label='Design Iterate')
impact_measure = Transition(label='Impact Measure')
strategy_adapt = Transition(label='Strategy Adapt')

# Define the loop nodes
idea_and_validation = OperatorPOWL(operator=Operator.LOOP, children=[idea_workshop, expert_review, prototype_build, pilot_launch, feedback_loop, design_iterate])
ip_and_supply = OperatorPOWL(operator=Operator.LOOP, children=[ip_alignment, supply_sync])
regulatory_and_market = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, market_mapping])
impact_and_adapt = OperatorPOWL(operator=Operator.LOOP, children=[impact_measure, strategy_adapt])

# Define the root node
root = StrictPartialOrder(nodes=[data_capture, trend_scan, idea_and_validation, ip_and_supply, regulatory_and_market, impact_and_adapt])
root.order.add_edge(data_capture, trend_scan)
root.order.add_edge(trend_scan, idea_and_validation)
root.order.add_edge(idea_and_validation, ip_and_supply)
root.order.add_edge(ip_and_supply, regulatory_and_market)
root.order.add_edge(regulatory_and_market, impact_and_adapt)

print(root)