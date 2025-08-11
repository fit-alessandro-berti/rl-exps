import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_audit = Transition(label='Site Audit')
impact_study = Transition(label='Impact Study')
design_modules = Transition(label='Design Modules')
sensor_setup = Transition(label='Sensor Setup')
hydroponics_install = Transition(label='Hydroponics Install')
nutrient_test = Transition(label='Nutrient Test')
lighting_config = Transition(label='Lighting Config')
staff_training = Transition(label='Staff Training')
data_collection = Transition(label='Data Collection')
yield_analysis = Transition(label='Yield Analysis')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
feedback_loop = Transition(label='Feedback Loop')

# Define silent transitions
skip = SilentTransition()

# Define loop for pest control
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, feedback_loop])

# Define XOR for data collection
xor_data_collection = OperatorPOWL(operator=Operator.XOR, children=[data_collection, feedback_loop])

# Define loop for staff training
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for staff training and feedback loop
xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_staff_training_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for data collection and feedback loop
xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_data_collection_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop, feedback_loop])

# Define XOR for pest control and feedback loop
xor_pest_control_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_pest_control_loop_loop