import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define loop for controlled aging
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging])

# Define XOR for packaging and labeling
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, label_printing])

# Define XOR for cold storage and logistics plan
xor_cold_storage = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, logistics_plan])

# Define XOR for retail delivery and feedback review
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, feedback_review])

# Define XOR for demand forecast and provenance track
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, provenance_track])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for salt application and milk pasturize
xor_salt_milk = OperatorPOWL(operator=Operator.XOR, children=[salt_application, milk_pasturize])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation
xor_curd_whey = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])

# Define XOR for controlled aging and sensory check
xor_aging_sensory = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])

# Define XOR for sensory check and provenance track
xor_sensory_provenance = OperatorPOWL(operator=Operator.XOR, children=[sensory_check, provenance_track])

# Define XOR for milk sourcing and quality testing
xor_milk_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])

# Define XOR for milk pasturize and salt application
xor_milk_salt = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, salt_application])

# Define XOR for curd formation and whey separation