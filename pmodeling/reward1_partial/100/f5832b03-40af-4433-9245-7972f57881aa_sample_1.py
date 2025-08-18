import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
legal_review = Transition(label='Legal Review')
tech_sourcing = Transition(label='Tech Sourcing')
structural_build = Transition(label='Structural Build')
climate_setup = Transition(label='Climate Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
crop_select = Transition(label='Crop Select')
nutrient_prep = Transition(label='Nutrient Prep')
waste_system = Transition(label='Waste System')
automation_config = Transition(label='Automation Config')
trial_growth = Transition(label='Trial Growth')
data_analysis = Transition(label='Data Analysis')
quality_audit = Transition(label='Quality Audit')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')

# Define exclusive choices for activities that can occur in parallel
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[structural_build, legal_review])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[tech_sourcing, climate_setup])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_install, sensor_deploy])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_prep])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[waste_system, automation_config])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[trial_growth, data_analysis])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, compliance_check])

# Define loops for activities that need to be repeated until conditions are met
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_1, exclusive_choice_2])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_3, exclusive_choice_4])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_5, exclusive_choice_6])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_7])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, loop_1, loop_2, loop_3, loop_4, stakeholder_meet, compliance_check])
root.order.add_edge(site_survey, exclusive_choice_1)
root.order.add_edge(exclusive_choice_1, loop_1)
root.order.add_edge(exclusive_choice_2, loop_2)
root.order.add_edge(loop_1, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, loop_3)
root.order.add_edge(loop_2, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, loop_4)
root.order.add_edge(loop_3, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, stakeholder_meet)
root.order.add_edge(loop_4, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, compliance_check)