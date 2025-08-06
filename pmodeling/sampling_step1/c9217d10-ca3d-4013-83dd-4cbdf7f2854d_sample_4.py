import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
design_layout = Transition(label='Design Layout')
system_install = Transition(label='System Install')
crop_select = Transition(label='Crop Select')
nutrient_plan = Transition(label='Nutrient Plan')
sensor_setup = Transition(label='Sensor Setup')
automation_test = Transition(label='Automation Test')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
supply_chain = Transition(label='Supply Chain')
customer_engage = Transition(label='Customer Engage')

# Define the control-flow operators (choices and loops)
site_climate_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, climate_study])
climate_layout_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_study, design_layout])
layout_install_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, system_install])
install_crop_choice = OperatorPOWL(operator=Operator.XOR, children=[system_install, crop_select])
crop_nutrient_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_plan])
nutrient_sensor_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_plan, sensor_setup])
sensor_test_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, automation_test])
test_train_choice = OperatorPOWL(operator=Operator.XOR, children=[automation_test, staff_train])
train_compliance_choice = OperatorPOWL(operator=Operator.XOR, children=[staff_train, compliance_check])
compliance_marketing_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, marketing_sync])
marketing_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, data_monitor])
monitor_yield_choice = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, yield_analyze])
yield_supply_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, supply_chain])
supply_customer_choice = OperatorPOWL(operator=Operator.XOR, children=[supply_chain, customer_engage])

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_climate_choice,
    climate_layout_choice,
    layout_install_choice,
    install_crop_choice,
    crop_nutrient_choice,
    nutrient_sensor_choice,
    sensor_test_choice,
    test_train_choice,
    train_compliance_choice,
    compliance_marketing_choice,
    marketing_monitor_choice,
    monitor_yield_choice,
    yield_supply_choice,
    supply_customer_choice
])

# Add dependencies between nodes
root.order.add_edge(site_climate_choice, climate_layout_choice)
root.order.add_edge(climate_layout_choice, layout_install_choice)
root.order.add_edge(layout_install_choice, install_crop_choice)
root.order.add_edge(install_crop_choice, crop_nutrient_choice)
root.order.add_edge(crop_nutrient_choice, nutrient_sensor_choice)
root.order.add_edge(nutrient_sensor_choice, sensor_test_choice)
root.order.add_edge(sensor_test_choice, test_train_choice)
root.order.add_edge(test_train_choice, train_compliance_choice)
root.order.add_edge(train_compliance_choice, compliance_marketing_choice)
root.order.add_edge(compliance_marketing_choice, marketing_monitor_choice)
root.order.add_edge(marketing_monitor_choice, monitor_yield_choice)
root.order.add_edge(monitor_yield_choice, yield_supply_choice)
root.order.add_edge(yield_supply_choice, supply_customer_choice)

print(root)