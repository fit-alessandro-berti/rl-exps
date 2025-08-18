import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
permit_filing = Transition(label='Permit Filing')
design_layout = Transition(label='Design Layout')
install_hvac = Transition(label='Install HVAC')
set_lighting = Transition(label='Set Lighting')
build_racks = Transition(label='Build Racks')
install_hydroponics = Transition(label='Install Hydroponics')
configure_sensors = Transition(label='Configure Sensors')
select_crops = Transition(label='Select Crops')
seed_planting = Transition(label='Seed Planting')
monitor_growth = Transition(label='Monitor Growth')
nutrient_mixing = Transition(label='Nutrient Mixing')
staff_training = Transition(label='Staff Training')
market_launch = Transition(label='Market Launch')
waste_recycling = Transition(label='Waste Recycling')
customer_onboarding = Transition(label='Customer Onboarding')

# Define the process structure
site_survey_to_structural_audit = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit])
structural_audit_to_permit_filing = OperatorPOWL(operator=Operator.XOR, children=[structural_audit, permit_filing])
permit_filing_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, design_layout])
design_layout_to_install_hvac = OperatorPOWL(operator=Operator.XOR, children=[design_layout, install_hvac])
install_hvac_to_set_lighting = OperatorPOWL(operator=Operator.XOR, children=[install_hvac, set_lighting])
set_lighting_to_build_racks = OperatorPOWL(operator=Operator.XOR, children=[set_lighting, build_racks])
build_racks_to_install_hydroponics = OperatorPOWL(operator=Operator.XOR, children=[build_racks, install_hydroponics])
install_hydroponics_to_configure_sensors = OperatorPOWL(operator=Operator.XOR, children=[install_hydroponics, configure_sensors])
configure_sensors_to_select_crops = OperatorPOWL(operator=Operator.XOR, children=[configure_sensors, select_crops])
select_crops_to_seed_planting = OperatorPOWL(operator=Operator.XOR, children=[select_crops, seed_planting])
seed_planting_to_monitor_growth = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, monitor_growth])
monitor_growth_to_nutrient_mixing = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, nutrient_mixing])
nutrient_mixing_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mixing, staff_training])
staff_training_to_market_launch = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_launch])
market_launch_to_waste_recycling = OperatorPOWL(operator=Operator.XOR, children=[market_launch, waste_recycling])
waste_recycling_to_customer_onboarding = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, customer_onboarding])

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey_to_structural_audit,
    structural_audit_to_permit_filing,
    permit_filing_to_design_layout,
    design_layout_to_install_hvac,
    install_hvac_to_set_lighting,
    set_lighting_to_build_racks,
    build_racks_to_install_hydroponics,
    install_hydroponics_to_configure_sensors,
    configure_sensors_to_select_crops,
    select_crops_to_seed_planting,
    seed_planting_to_monitor_growth,
    monitor_growth_to_nutrient_mixing,
    nutrient_mixing_to_staff_training,
    staff_training_to_market_launch,
    market_launch_to_waste_recycling,
    waste_recycling_to_customer_onboarding
])
root.order.add_edge(site_survey_to_structural_audit, structural_audit_to_permit_filing)
root.order.add_edge(structural_audit_to_permit_filing, permit_filing_to_design_layout)
root.order.add_edge(permit_filing_to_design_layout, design_layout_to_install_hvac)
root.order.add_edge(design_layout_to_install_hvac, install_hvac_to_set_lighting)
root.order.add_edge(install_hvac_to_set_lighting, set_lighting_to_build_racks)
root.order.add_edge(set_lighting_to_build_racks, build_racks_to_install_hydroponics)
root.order.add_edge(build_racks_to_install_hydroponics, install_hydroponics_to_configure_sensors)
root.order.add_edge(install_hydroponics_to_configure_sensors, configure_sensors_to_select_crops)
root.order.add_edge(configure_sensors_to_select_crops, select_crops_to_seed_planting)
root.order.add_edge(select_crops_to_seed_planting, seed_planting_to_monitor_growth)
root.order.add_edge(seed_planting_to_monitor_growth, monitor_growth_to_nutrient_mixing)
root.order.add_edge(monitor_growth_to_nutrient_mixing, nutrient_mixing_to_staff_training)
root.order.add_edge(nutrient_mixing_to_staff_training, staff_training_to_market_launch)
root.order.add_edge(staff_training_to_market_launch, market_launch_to_waste_recycling)
root.order.add_edge(market_launch_to_waste_recycling, waste_recycling_to_customer_onboarding)

print(root)