import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_test = Transition(label='Soil Test')
climate_eval = Transition(label='Climate Eval')
permit_obtain = Transition(label='Permit Obtain')
design_layout = Transition(label='Design Layout')
seed_sourcing = Transition(label='Seed Sourcing')
irrigation_set = Transition(label='Irrigation Set')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train = Transition(label='Staff Train')
crop_planting = Transition(label='Crop Planting')
yield_monitor = Transition(label='Yield Monitor')
market_setup = Transition(label='Market Setup')
maintenance = Transition(label='Maintenance')
waste_manage = Transition(label='Waste Manage')

# Define the control flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, site_assess])
inclusive_choice = OperatorPOWL(operator=Operator.OR, children=[soil_test, climate_eval])
inclusive_choice_2 = OperatorPOWL(operator=Operator.OR, children=[structure_check, permit_obtain])
inclusive_choice_3 = OperatorPOWL(operator=Operator.OR, children=[design_layout, seed_sourcing])
inclusive_choice_4 = OperatorPOWL(operator=Operator.OR, children=[irrigation_set, nutrient_mix])
inclusive_choice_5 = OperatorPOWL(operator=Operator.OR, children=[pest_control, sensor_install])
inclusive_choice_6 = OperatorPOWL(operator=Operator.OR, children=[staff_train, crop_planting])
inclusive_choice_7 = OperatorPOWL(operator=Operator.OR, children=[yield_monitor, market_setup])
inclusive_choice_8 = OperatorPOWL(operator=Operator.OR, children=[maintenance, waste_manage])

# Define the partial order
root = StrictPartialOrder(nodes=[exclusive_choice, inclusive_choice, inclusive_choice_2, inclusive_choice_3, inclusive_choice_4, inclusive_choice_5, inclusive_choice_6, inclusive_choice_7, inclusive_choice_8])
root.order.add_edge(exclusive_choice, inclusive_choice)
root.order.add_edge(inclusive_choice, inclusive_choice_2)
root.order.add_edge(inclusive_choice_2, inclusive_choice_3)
root.order.add_edge(inclusive_choice_3, inclusive_choice_4)
root.order.add_edge(inclusive_choice_4, inclusive_choice_5)
root.order.add_edge(inclusive_choice_5, inclusive_choice_6)
root.order.add_edge(inclusive_choice_6, inclusive_choice_7)
root.order.add_edge(inclusive_choice_7, inclusive_choice_8)
root.order.add_edge(inclusive_choice_8, inclusive_choice)

print(root)