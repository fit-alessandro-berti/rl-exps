import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_assess = Transition(label='Site Assess')
load_testing = Transition(label='Load Testing')
climate_study = Transition(label='Climate Study')
medium_prep = Transition(label='Medium Prep')
bed_install = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
monitor_deploy = Transition(label='Monitor Deploy')
waste_cycle = Transition(label='Waste Cycle')
yield_forecast = Transition(label='Yield Forecast')
market_link = Transition(label='Market Link')
workshop_plan = Transition(label='Workshop Plan')
tech_integrate = Transition(label='Tech Integrate')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_site_assess = OperatorPOWL(operator=Operator.LOOP, children=[site_assess])
loop_load_testing = OperatorPOWL(operator=Operator.LOOP, children=[load_testing])

# Define exclusive choice nodes
xor_climate_study = OperatorPOWL(operator=Operator.XOR, children=[climate_study, skip])
xor_medium_prep = OperatorPOWL(operator=Operator.XOR, children=[medium_prep, skip])
xor_bed_install = OperatorPOWL(operator=Operator.XOR, children=[bed_install, skip])
xor_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, skip])
xor_crop_select = OperatorPOWL(operator=Operator.XOR, children=[crop_select, skip])
xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
xor_community_meet = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
xor_monitor_deploy = OperatorPOWL(operator=Operator.XOR, children=[monitor_deploy, skip])
xor_waste_cycle = OperatorPOWL(operator=Operator.XOR, children=[waste_cycle, skip])
xor_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
xor_market_link = OperatorPOWL(operator=Operator.XOR, children=[market_link, skip])
xor_workshop_plan = OperatorPOWL(operator=Operator.XOR, children=[workshop_plan, skip])
xor_tech_integrate = OperatorPOWL(operator=Operator.XOR, children=[tech_integrate, skip])

# Define partial order
root = StrictPartialOrder(nodes=[loop_site_assess, loop_load_testing, xor_climate_study, xor_medium_prep, xor_bed_install, xor_irrigation_setup, xor_crop_select, xor_pest_control, xor_community_meet, xor_monitor_deploy, xor_waste_cycle, xor_yield_forecast, xor_market_link, xor_workshop_plan, xor_tech_integrate])
root.order.add_edge(loop_site_assess, xor_climate_study)
root.order.add_edge(loop_site_assess, xor_medium_prep)
root.order.add_edge(loop_site_assess, xor_bed_install)
root.order.add_edge(loop_site_assess, xor_irrigation_setup)
root.order.add_edge(loop_site_assess, xor_crop_select)
root.order.add_edge(loop_site_assess, xor_pest_control)
root.order.add_edge(loop_site_assess, xor_community_meet)
root.order.add_edge(loop_site_assess, xor_monitor_deploy)
root.order.add_edge(loop_site_assess, xor_waste_cycle)
root.order.add_edge(loop_site_assess, xor_yield_forecast)
root.order.add_edge(loop_site_assess, xor_market_link)
root.order.add_edge(loop_site_assess, xor_workshop_plan)
root.order.add_edge(loop_site_assess, xor_tech_integrate)
root.order.add_edge(loop_load_testing, xor_medium_prep)
root.order.add_edge(loop_load_testing, xor_bed_install)
root.order.add_edge(loop_load_testing, xor_irrigation_setup)
root.order.add_edge(loop_load_testing, xor_crop_select)
root.order.add_edge(loop_load_testing, xor_pest_control)
root.order.add_edge(loop_load_testing, xor_community_meet)
root.order.add_edge(loop_load_testing, xor_monitor_deploy)
root.order.add_edge(loop_load_testing, xor_waste_cycle)
root.order.add_edge(loop_load_testing, xor_yield_forecast)
root.order.add_edge(loop_load_testing, xor_market_link)
root.order.add_edge(loop_load_testing, xor_workshop_plan)
root.order.add_edge(loop_load_testing, xor_tech_integrate)

# Save the final result in the variable 'root'