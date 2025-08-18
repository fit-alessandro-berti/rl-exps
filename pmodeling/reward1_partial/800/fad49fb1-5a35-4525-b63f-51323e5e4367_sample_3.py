from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
source_materials = Transition(label='Source Materials')
install_framework = Transition(label='Install Framework')
setup_irrigation = Transition(label='Setup Irrigation')
integrate_sensors = Transition(label='Integrate Sensors')
configure_ai = Transition(label='Configure AI')
select_crops = Transition(label='Select Crops')
calibrate_climate = Transition(label='Calibrate Climate')
plant_seeds = Transition(label='Plant Seeds')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
recycle_waste = Transition(label='Recycle Waste')
engage_community = Transition(label='Engage Community')
ensure_compliance = Transition(label='Ensure Compliance')
distribute_produce = Transition(label='Distribute Produce')

# Define the operators (choices and loops)
choice_source_materials = OperatorPOWL(operator=Operator.XOR, children=[source_materials, install_framework])
choice_install_framework = OperatorPOWL(operator=Operator.XOR, children=[install_framework, setup_irrigation])
choice_setup_irrigation = OperatorPOWL(operator=Operator.XOR, children=[setup_irrigation, integrate_sensors])
choice_integrate_sensors = OperatorPOWL(operator=Operator.XOR, children=[integrate_sensors, configure_ai])
choice_configure_ai = OperatorPOWL(operator=Operator.XOR, children=[configure_ai, select_crops])
choice_select_crops = OperatorPOWL(operator=Operator.XOR, children=[select_crops, calibrate_climate])
choice_calibrate_climate = OperatorPOWL(operator=Operator.XOR, children=[calibrate_climate, plant_seeds])
choice_plant_seeds = OperatorPOWL(operator=Operator.XOR, children=[plant_seeds, monitor_growth])
choice_monitor_growth = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_pests])
choice_manage_pests = OperatorPOWL(operator=Operator.XOR, children=[manage_pests, recycle_waste])
choice_recycle_waste = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, engage_community])
choice_engage_community = OperatorPOWL(operator=Operator.XOR, children=[engage_community, ensure_compliance])
choice_ensure_compliance = OperatorPOWL(operator=Operator.XOR, children=[ensure_compliance, distribute_produce])

# Construct the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    choice_source_materials,
    choice_install_framework,
    choice_setup_irrigation,
    choice_integrate_sensors,
    choice_configure_ai,
    choice_select_crops,
    choice_calibrate_climate,
    choice_plant_seeds,
    choice_monitor_growth,
    choice_manage_pests,
    choice_recycle_waste,
    choice_engage_community,
    choice_ensure_compliance
])

# Add dependencies
root.order.add_edge(site_survey, choice_source_materials)
root.order.add_edge(choice_source_materials, choice_install_framework)
root.order.add_edge(choice_install_framework, choice_setup_irrigation)
root.order.add_edge(choice_setup_irrigation, choice_integrate_sensors)
root.order.add_edge(choice_integrate_sensors, choice_configure_ai)
root.order.add_edge(choice_configure_ai, choice_select_crops)
root.order.add_edge(choice_select_crops, choice_calibrate_climate)
root.order.add_edge(choice_calibrate_climate, choice_plant_seeds)
root.order.add_edge(choice_plant_seeds, choice_monitor_growth)
root.order.add_edge(choice_monitor_growth, choice_manage_pests)
root.order.add_edge(choice_manage_pests, choice_recycle_waste)
root.order.add_edge(choice_recycle_waste, choice_engage_community)
root.order.add_edge(choice_engage_community, choice_ensure_compliance)
root.order.add_edge(choice_ensure_compliance, distribute_produce)