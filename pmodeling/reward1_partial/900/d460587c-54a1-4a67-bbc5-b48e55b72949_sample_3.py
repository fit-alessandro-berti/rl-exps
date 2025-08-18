import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
load_testing = Transition(label='Load Testing')
soil_sampling = Transition(label='Soil Sampling')
water_testing = Transition(label='Water Testing')
system_design = Transition(label='System Design')
solar_setup = Transition(label='Solar Setup')
crop_planning = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
material_order = Transition(label='Material Order')
system_install = Transition(label='System Install')
environmental_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
market_launch = Transition(label='Market Launch')

# Define the loop for the system design and solar setup
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design, solar_setup])

# Define the XOR for the environmental audit and growth monitoring
xor = OperatorPOWL(operator=Operator.XOR, children=[environmental_audit, growth_monitoring])

# Define the XOR for the pest control and market launch
market_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, market_launch])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, permit_filing, load_testing, soil_sampling, water_testing, loop, xor, market_xor])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, load_testing)
root.order.add_edge(load_testing, soil_sampling)
root.order.add_edge(soil_sampling, water_testing)
root.order.add_edge(water_testing, loop)
root.order.add_edge(loop, system_design)
root.order.add_edge(system_design, solar_setup)
root.order.add_edge(solar_setup, xor)
root.order.add_edge(xor, market_xor)
root.order.add_edge(market_xor, pest_control)
root.order.add_edge(market_xor, market_launch)

print(root)