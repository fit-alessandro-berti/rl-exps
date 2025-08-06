import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the silent transitions
skip_material_scout = SilentTransition(label='Skip Material Scout')
skip_supplier_vetting = SilentTransition(label='Skip Supplier Vetting')
skip_skill_audit = SilentTransition(label='Skip Skill Audit')
skip_order_forecast = SilentTransition(label='Skip Order Forecast')
skip_custom_scheduling = SilentTransition(label='Skip Custom Scheduling')
skip_impact_review = SilentTransition(label='Skip Impact Review')
skip_product_inspect = SilentTransition(label='Skip Product Inspect')
skip_eco_packaging = SilentTransition(label='Skip Eco Packaging')
skip_multi_transport = SilentTransition(label='Skip Multi Transport')
skip_route_optimize = SilentTransition(label='Skip Route Optimize')
skip_feedback_loop = SilentTransition(label='Skip Feedback Loop')
skip_craft_refine = SilentTransition(label='Skip Craft Refine')
skip_inventory_balance = SilentTransition(label='Skip Inventory Balance')
skip_story_marketing = SilentTransition(label='Skip Story Marketing')
skip_heritage_share = SilentTransition(label='Skip Heritage Share')
skip_demand_adjust = SilentTransition(label='Skip Demand Adjust')
skip_community_sync = SilentTransition(label='Skip Community Sync')

# Define the partial order
root = StrictPartialOrder(nodes=[
    material_scout, supplier_vetting, skill_audit, order_forecast,
    custom_scheduling, impact_review, product_inspect, eco_packaging,
    multi_transport, route_optimize, feedback_loop, craft_refine,
    inventory_balance, story_marketing, heritage_share, demand_adjust,
    community_sync, skip_material_scout, skip_supplier_vetting,
    skip_skill_audit, skip_order_forecast, skip_custom_scheduling,
    skip_impact_review, skip_product_inspect, skip_eco_packaging,
    skip_multi_transport, skip_route_optimize, skip_feedback_loop,
    skip_craft_refine, skip_inventory_balance, skip_story_marketing,
    skip_heritage_share, skip_demand_adjust, skip_community_sync])

# Define the dependencies
root.order.add_edge(material_scout, supplier_vetting)
root.order.add_edge(supplier_vetting, skill_audit)
root.order.add_edge(skill_audit, order_forecast)
root.order.add_edge(order_forecast, custom_scheduling)
root.order.add_edge(custom_scheduling, impact_review)
root.order.add_edge(impact_review, product_inspect)
root.order.add_edge(product_inspect, eco_packaging)
root.order.add_edge(eco_packaging, multi_transport)
root.order.add_edge(multi_transport, route_optimize)
root.order.add_edge(route_optimize, feedback_loop)
root.order.add_edge(feedback_loop, craft_refine)
root.order.add_edge(craft_refine, inventory_balance)
root.order.add_edge(inventory_balance, story_marketing)
root.order.add_edge(story_marketing, heritage_share)
root.order.add_edge(heritage_share, demand_adjust)
root.order.add_edge(demand_adjust, community_sync)
root.order.add_edge(skip_material_scout, supplier_vetting)
root.order.add_edge(skip_supplier_vetting, skill_audit)
root.order.add_edge(skip_skill_audit, order_forecast)
root.order.add_edge(skip_order_forecast, custom_scheduling)
root.order.add_edge(skip_custom_scheduling, impact_review)
root.order.add_edge(skip_impact_review, product_inspect)
root.order.add_edge(skip_product_inspect, eco_packaging)
root.order.add_edge(skip_eco_packaging, multi_transport)
root.order.add_edge(skip_multi_transport, route_optimize)
root.order.add_edge(skip_route_optimize, feedback_loop)
root.order.add_edge(skip_feedback_loop, craft_refine)
root.order.add_edge(skip_craft_refine, inventory_balance)
root.order.add_edge(skip_inventory_balance, story_marketing)
root.order.add_edge(skip_story_marketing, heritage_share)
root.order.add_edge(skip_heritage_share, demand_adjust)
root.order.add_edge(skip_demand_adjust, community_sync)
root.order.add_edge(skip_community_sync, community_sync)

# Print the result
print(root)