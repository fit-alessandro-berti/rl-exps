import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
site_survey = Transition(label='Site Survey')
climate_check = Transition(label='Climate Check')
soil_testing = Transition(label='Soil Testing')
media_select = Transition(label='Media Select')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train = Transition(label='Community Train')
plant_seed = Transition(label='Plant Seed')
monitor_growth = Transition(label='Monitor Growth')
adjust_controls = Transition(label='Adjust Controls')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
feedback_loop = Transition(label='Feedback Loop')

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, climate_check, soil_testing])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[media_select, design_layout])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[hydro_setup, nutrient_mix])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, regulation_review])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, stakeholder_meet])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[community_train, plant_seed])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, adjust_controls])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, waste_recycle])
exclusive_choice_9 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop])

# Define the partial order
root = StrictPartialOrder(nodes=[exclusive_choice, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8, exclusive_choice_9])
root.order.add_edge(exclusive_choice, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, exclusive_choice_9)
root.order.add_edge(exclusive_choice_9, exclusive_choice)

print(root)