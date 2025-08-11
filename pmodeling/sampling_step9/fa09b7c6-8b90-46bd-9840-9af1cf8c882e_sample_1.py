import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

# Site Survey
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])

# Design Layout
design_layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])

# Install Lighting
install_lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_lighting])

# Setup Hydroponics
setup_hydroponics_loop = OperatorPOWL(operator=Operator.LOOP, children=[setup_hydroponics])

# Calibrate Sensors
calibrate_sensors_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_sensors])

# Select Crops
select_crops_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_crops])

# Mix Nutrients
mix_nutrients_loop = OperatorPOWL(operator=Operator.LOOP, children=[mix_nutrients])

# Deploy IoT
deploy_iot_loop = OperatorPOWL(operator=Operator.LOOP, children=[deploy_iot])

# Energy Audit
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])

# Train Staff
train_staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[train_staff])

# Pest Control
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])

# Legal Review
legal_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review])

# Market Analysis
market_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis])

# Plan Logistics
plan_logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[plan_logistics])

# Yield Review
yield_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_review])

# XOR (Choice) between the above loops and the skip activity
xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey_loop, design_layout_loop, install_lighting_loop, setup_hydroponics_loop, calibrate_sensors_loop, select_crops_loop, mix_nutrients_loop, deploy_iot_loop, energy_audit_loop, train_staff_loop, pest_control_loop, legal_review_loop, market_analysis_loop, plan_logistics_loop, yield_review_loop, skip])

# Root of the POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(site_survey_loop, xor)
root.order.add_edge(design_layout_loop, xor)
root.order.add_edge(install_lighting_loop, xor)
root.order.add_edge(setup_hydroponics_loop, xor)
root.order.add_edge(calibrate_sensors_loop, xor)
root.order.add_edge(select_crops_loop, xor)
root.order.add_edge(mix_nutrients_loop, xor)
root.order.add_edge(deploy_iot_loop, xor)
root.order.add_edge(energy_audit_loop, xor)
root.order.add_edge(train_staff_loop, xor)
root.order.add_edge(pest_control_loop, xor)
root.order.add_edge(legal_review_loop, xor)
root.order.add_edge(market_analysis_loop, xor)
root.order.add_edge(plan_logistics_loop, xor)
root.order.add_edge(yield_review_loop, xor)