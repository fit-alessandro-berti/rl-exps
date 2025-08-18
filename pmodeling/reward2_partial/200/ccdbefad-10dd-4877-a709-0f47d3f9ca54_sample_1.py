from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

root = StrictPartialOrder(nodes=[
    material_scout, supplier_vetting, skill_audit, order_forecast, custom_scheduling,
    impact_review, product_inspect, eco_packaging, multi_transport, route_optimize,
    feedback_loop, craft_refine, inventory_balance, story_marketing, heritage_share,
    demand_adjust, community_sync
])

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