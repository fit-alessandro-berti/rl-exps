from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
colony_sourcing = Transition(label='Colony Sourcing')
hive_design = Transition(label='Hive Design')
site_survey = Transition(label='Site Survey')
installation_prep = Transition(label='Installation Prep')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
product_packaging = Transition(label='Product Packaging')
order_dispatch = Transition(label='Order Dispatch')
workshop_setup = Transition(label='Workshop Setup')
community_outreach = Transition(label='Community Outreach')
regulation_check = Transition(label='Regulation Check')
data_analysis = Transition(label='Data Analysis')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[hive_design, site_survey])
inclusive_choice = OperatorPOWL(operator=Operator.OR, children=[installation_prep, hive_setup])
loop = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, pest_control, honey_harvest])
inclusive_choice_2 = OperatorPOWL(operator=Operator.OR, children=[wax_processing, product_packaging])
inclusive_choice_3 = OperatorPOWL(operator=Operator.OR, children=[order_dispatch, workshop_setup])
inclusive_choice_4 = OperatorPOWL(operator=Operator.OR, children=[community_outreach, regulation_check])
inclusive_choice_5 = OperatorPOWL(operator=Operator.OR, children=[data_analysis, maintenance_plan])

# Create the root POWL model
root = StrictPartialOrder(nodes=[colony_sourcing, exclusive_choice, inclusive_choice, loop, inclusive_choice_2, inclusive_choice_3, inclusive_choice_4, inclusive_choice_5])
root.order.add_edge(colony_sourcing, exclusive_choice)
root.order.add_edge(exclusive_choice, inclusive_choice)
root.order.add_edge(inclusive_choice, loop)
root.order.add_edge(loop, inclusive_choice_2)
root.order.add_edge(inclusive_choice_2, inclusive_choice_3)
root.order.add_edge(inclusive_choice_3, inclusive_choice_4)
root.order.add_edge(inclusive_choice_4, inclusive_choice_5)

print(root)