import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_analyze    = Transition(label='Site Analyze')
soil_enhance    = Transition(label='Soil Enhance')
seed_select     = Transition(label='Seed Select')
plant_precise   = Transition(label='Plant Precise')
sensor_deploy   = Transition(label='Sensor Deploy')
climate_monitor = Transition(label='Climate Monitor')
irrigate_adjust = Transition(label='Irrigate Adjust')
nutrient_feed   = Transition(label='Nutrient Feed')
pest_control    = Transition(label='Pest Control')
community_engage= Transition(label='Community Engage')
feedback_collect= Transition(label='Feedback Collect')
yield_harvest   = Transition(label='Yield Harvest')
waste_sort      = Transition(label='Waste Sort')
compost_create  = Transition(label='Compost Create')
data_analyze    = Transition(label='Data Analyze')
network_distribute = Transition(label='Network Distribute')

# Build the adaptive loop: after each feedback collection, perform data analysis and then either exit or repeat
adaptive_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_analyze, OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, adaptive_loop]))