from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[skill_audit, order_forecast])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[multi_transport, route_optimize])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, craft_refine])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[demand_adjust, community_sync])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[inventory_balance, story_marketing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[heritage_share, community_sync])

# Define the root
root = StrictPartialOrder(nodes=[material_scout, supplier_vetting, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(material_scout, supplier_vetting)
root.order.add_edge(supplier_vetting, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)