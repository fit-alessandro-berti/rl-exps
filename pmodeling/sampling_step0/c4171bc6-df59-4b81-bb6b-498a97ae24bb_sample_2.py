import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track = Transition(label='Provenance Track')

# Define silent transitions
skip = SilentTransition()

# Define the loop for controlled aging
controlled_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_check])

# Define the XOR for sensory check and packaging
sensory_check_xor = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, batch_packaging])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define the XOR for milk pasteurize and press cheese
milk_pasteurize_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, press_cheese])

# Define the XOR for salt application and controlled aging
salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, controlled_aging])

# Define the XOR for curd formation and whey separation
curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define the XOR for milk sourcing and quality testing
milk_sourcing_xor = OperatorPOWL