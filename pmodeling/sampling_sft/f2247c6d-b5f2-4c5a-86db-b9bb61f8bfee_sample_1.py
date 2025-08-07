import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
receive = Transition(label='Receive Returns')
inspect = Transition(label='Inspect Items')
segregate = Transition(label='Segregate Stock')
wipe = Transition(label='Wipe Data')
harvest = Transition(label='Harvest Parts')
refurbish = Transition(label='Refurbish Units')
test = Transition(label='Test Quality')
recycle = Transition(label='Recycle Waste')
dispose = Transition(label='Dispose Defects')
update_inventory = Transition(label='Update Inventory')
coordinate_resale = Transition(label='Coordinate Resale')
process_refunds = Transition(label='Process Refunds')
analyze = Transition(label='Analyze Patterns')
improve_design = Transition(label='Improve Design')
report = Transition(label='Report Metrics')

# Define the main workflow as a strict partial order
main_workflow = StrictPartialOrder(nodes=[
    receive, inspect, segregate, wipe, harvest, refurbish, test,
    recycle, dispose, update_inventory, coordinate_resale, process_refunds,
    analyze, improve_design, report
])

# Define the sequence of activities
main_workflow.order.add_edge(receive, inspect)
main_workflow.order.add_edge(inspect, segregate)
main_workflow.order.add_edge(segregate, wipe)
main_workflow.order.add_edge(wipe, harvest)
main_workflow.order.add_edge(harvest, refurbish)
main_workflow.order.add_edge(refurbish, test)
main_workflow.order.add_edge(test, recycle)
main_workflow.order.add_edge(test, dispose)
main_workflow.order.add_edge(recycle, update_inventory)
main_workflow.order.add_edge(dispose, update_inventory)
main_workflow.order.add_edge(update_inventory, coordinate_resale)
main_workflow.order.add_edge(coordinate_resale, process_refunds)
main_workflow.order.add_edge(process_refunds, analyze)
main_workflow.order.add_edge(analyze, improve_design)
main_workflow.order.add_edge(improve_design, report)

# Define the loop for continuous analysis
# A = analyze, B = improve_design
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[analyze, improve_design])

# Add the analysis loop to the root
root = StrictPartialOrder(nodes=[
    receive, inspect, segregate, wipe, harvest, refurbish, test,
    recycle, dispose, update_inventory, coordinate_resale, process_refunds,
    loop_analysis, report
])

# Add the sequence of the main workflow before the analysis loop
for node in main_workflow.nodes:
    root.order.add_edge(receive, node)

# Add the analysis loop
root.order.add_edge(main_workflow.nodes[-1], loop_analysis)

# Add the report after the analysis loop
root.order.add_edge(loop_analysis, report)

print(root)