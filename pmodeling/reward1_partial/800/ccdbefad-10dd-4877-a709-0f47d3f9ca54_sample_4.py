import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
root = StrictPartialOrder(
    nodes=[
        material_scout,
        supplier_vetting,
        skill_audit,
        order_forecast,
        custom_scheduling,
        impact_review,
        product_inspect,
        eco_packaging,
        multi_transport,
        route_optimize,
        feedback_loop,
        craft_refine,
        inventory_balance,
        story_marketing,
        heritage_share,
        demand_adjust,
        community_sync
    ],
    order=[
        (material_scout, supplier_vetting),
        (supplier_vetting, skill_audit),
        (skill_audit, order_forecast),
        (order_forecast, custom_scheduling),
        (custom_scheduling, impact_review),
        (impact_review, product_inspect),
        (product_inspect, eco_packaging),
        (eco_packaging, multi_transport),
        (multi_transport, route_optimize),
        (route_optimize, feedback_loop),
        (feedback_loop, craft_refine),
        (craft_refine, inventory_balance),
        (inventory_balance, story_marketing),
        (story_marketing, heritage_share),
        (heritage_share, demand_adjust),
        (demand_adjust, community_sync)
    ]
)