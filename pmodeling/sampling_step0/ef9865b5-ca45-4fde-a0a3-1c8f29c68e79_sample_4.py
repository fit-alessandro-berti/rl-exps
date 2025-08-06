import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
structural_test = Transition(label='Structural Test')
recruit_farmers = Transition(label='Recruit Farmers')
trial_planting = Transition(label='Trial Planting')
pest_control = Transition(label='Pest Control')
soilless_prep = Transition(label='Soilless Prep')
system_calibrate = Transition(label='System Calibrate')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
community_outreach = Transition(label='Community Outreach')

loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_test, permit_review, design_layout, material_sourcing, irrigation_setup, sensor_install, recruit_farmers, trial_planting, pest_control, soilless_prep, system_calibrate, data_monitor, harvest_plan, community_outreach])
xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, loop])
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(site_survey, loop)
root.order.add_edge(loop, xor)