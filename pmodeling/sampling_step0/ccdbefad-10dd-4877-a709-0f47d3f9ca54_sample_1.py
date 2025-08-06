import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
material_scout = Transition(label='Material Scout')
supplier_vetting = Transition(label='Supplier Vetting')
skill_audit = Transition(label='Skill Audit')
order_forecast = Transition(label='Order Forecast')
custom_scheduling = Transition(label='Custom Scheduling')
impact_review = Transition(label='Impact Review')
product_inspect = Transition(label='Product Inspect')
eco_packaging = Transition(label='Eco Packaging')
multi_transport = Transition(label='Multi Transport')
route_optimize = Transition(label='Route Optimize')
feedback_loop = Transition(label='Feedback Loop')
craft_refine = Transition(label='Craft Refine')
inventory_balance = Transition(label='Inventory Balance')
story_marketing = Transition(label='Story Marketing')
heritage_share = Transition(label='Heritage Share')
demand_adjust = Transition(label='Demand Adjust')
community_sync = Transition(label='Community Sync')

# Define silent transitions
skip = SilentTransition()

# Define partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_scout, supplier_vetting, skill_audit, order_forecast, custom_scheduling, impact_review])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[product_inspect, eco_packaging])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[multi_transport, route_optimize])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, craft_refine])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_balance, story_marketing, heritage_share, demand_adjust])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[community_sync, skip])

# Connect nodes
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)

# Print the final result
print(root)