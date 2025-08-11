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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[custom_scheduling, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scout, supplier_vetting, skill_audit, order_forecast, product_inspect, eco_packaging, multi_transport, route_optimize, feedback_loop, craft_refine, inventory_balance, story_marketing, heritage_share, demand_adjust, community_sync])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)