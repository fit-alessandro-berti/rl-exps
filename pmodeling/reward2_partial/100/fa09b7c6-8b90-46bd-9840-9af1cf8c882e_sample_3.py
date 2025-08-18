import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_lighting = Transition(label='Install Lighting')
setup_hydroponics = Transition(label='Setup Hydroponics')
calibrate_sensors = Transition(label='Calibrate Sensors')
select_crops = Transition(label='Select Crops')
mix_nutrients = Transition(label='Mix Nutrients')
deploy_iot = Transition(label='Deploy IoT')
energy_audit = Transition(label='Energy Audit')
train_staff = Transition(label='Train Staff')
pest_control = Transition(label='Pest Control')
legal_review = Transition(label='Legal Review')
market_analysis = Transition(label='Market Analysis')
plan_logistics = Transition(label='Plan Logistics')
yield_review = Transition(label='Yield Review')

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, install_lighting, setup_hydroponics, calibrate_sensors, select_crops, mix_nutrients, deploy_iot, energy_audit, train_staff, pest_control, legal_review, market_analysis, plan_logistics, yield_review])

# Define the dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_lighting)
root.order.add_edge(install_lighting, setup_hydroponics)
root.order.add_edge(setup_hydroponics, calibrate_sensors)
root.order.add_edge(calibrate_sensors, select_crops)
root.order.add_edge(select_crops, mix_nutrients)
root.order.add_edge(mix_nutrients, deploy_iot)
root.order.add_edge(deploy_iot, energy_audit)
root.order.add_edge(energy_audit, train_staff)
root.order.add_edge(train_staff, pest_control)
root.order.add_edge(pest_control, legal_review)
root.order.add_edge(legal_review, market_analysis)
root.order.add_edge(market_analysis, plan_logistics)
root.order.add_edge(plan_logistics, yield_review)

print(root)