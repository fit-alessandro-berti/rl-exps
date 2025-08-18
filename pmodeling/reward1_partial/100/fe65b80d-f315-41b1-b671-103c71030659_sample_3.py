import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Ingredient_Sourcing = Transition(label='Ingredient Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Scent_Blending = Transition(label='Scent Blending')
Micro_Batch = Transition(label='Micro Batch')
Sensory_Panel = Transition(label='Sensory Panel')
Formula_Adjust = Transition(label='Formula Adjust')
Safety_Review = Transition(label='Safety Review')
Sustainability_Check = Transition(label='Sustainability Check')
Packaging_Design = Transition(label='Packaging Design')
Prototype_Creation = Transition(label='Prototype Creation')
Client_Feedback = Transition(label='Client Feedback')
Label_Approval = Transition(label='Label Approval')
Final_Production = Transition(label='Final Production')
Marketing_Plan = Transition(label='Marketing Plan')
Distribution_Prep = Transition(label='Distribution Prep')
Sales_Launch = Transition(label='Sales Launch')

# Define silent transitions for transitions with no label
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define nodes and their relationships
ingredient_sourcing = OperatorPOWL(operator=Operator.PARALLEL, children=[Ingredient_Sourcing, Quality_Testing, Scent_Blending])
quality_testing = OperatorPOWL(operator=Operator.PARALLEL, children=[Micro_Batch, Sensory_Panel])
scent_blending = OperatorPOWL(operator=Operator.PARALLEL, children=[Formula_Adjust, Safety_Review])
formula_adjust = OperatorPOWL(operator=Operator.PARALLEL, children=[Sustainability_Check, Packaging_Design])
sustainability_check = OperatorPOWL(operator=Operator.PARALLEL, children=[Prototype_Creation, Client_Feedback])
prototype_creation = OperatorPOWL(operator=Operator.PARALLEL, children=[Label_Approval, Final_Production])
client_feedback = OperatorPOWL(operator=Operator.PARALLEL, children=[Marketing_Plan, Distribution_Prep])
marketing_plan = OperatorPOWL(operator=Operator.PARALLEL, children=[Sales_Launch])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[ingredient_sourcing, quality_testing, scent_blending, formula_adjust, sustainability_check, prototype_creation, client_feedback, marketing_plan, sales_launch])
root.order.add_edge(ingredient_sourcing, quality_testing)
root.order.add_edge(ingredient_sourcing, scent_blending)
root.order.add_edge(quality_testing, formula_adjust)
root.order.add_edge(quality_testing, sustainability_check)
root.order.add_edge(scent_blending, prototype_creation)
root.order.add_edge(scent_blending, client_feedback)
root.order.add_edge(formula_adjust, marketing_plan)
root.order.add_edge(formula_adjust, distribution_prep)
root.order.add_edge(sustainability_check, label_approval)
root.order.add_edge(sustainability_check, final_production)
root.order.add_edge(prototype_creation, marketing_plan)
root.order.add_edge(prototype_creation, distribution_prep)
root.order.add_edge(client_feedback, marketing_plan)
root.order.add_edge(client_feedback, distribution_prep)
root.order.add_edge(marketing_plan, sales_launch)