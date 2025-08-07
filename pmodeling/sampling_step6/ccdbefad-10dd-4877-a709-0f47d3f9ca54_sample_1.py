import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    material_scout, supplier_vetting, skill_audit, order_forecast,
    custom_scheduling, impact_review, product_inspect, eco_packaging,
    multi_transport, route_optimize, feedback_loop, craft_refine,
    inventory_balance, story_marketing, heritage_share, demand_adjust,
    community_sync
])

# Add dependencies if any (in this case, no explicit dependencies are given)
# The model is fully defined as a partial order with no additional edges

# Save the final result in the variable 'root'
print(root)