import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[impact_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[multi_transport, route_optimize])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[story_marketing, heritage_share])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[demand_adjust, community_sync])
loop = OperatorPOWL(operator=Operator.LOOP, children=[skill_audit, product_inspect, eco_packaging])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[custom_scheduling, order_forecast])

root = StrictPartialOrder(nodes=[material_scout, supplier_vetting, xor5, loop, xor1, xor2, xor3, xor4, feedback_loop, craft_refine, inventory_balance])
root.order.add_edge(material_scout, supplier_vetting)
root.order.add_edge(supplier_vetting, xor5)
root.order.add_edge(xor5, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, feedback_loop)
root.order.add_edge(feedback_loop, craft_refine)
root.order.add_edge(craft_refine, inventory_balance)

print(root)