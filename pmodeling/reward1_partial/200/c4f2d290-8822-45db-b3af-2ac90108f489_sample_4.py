root = StrictPartialOrder(nodes=[
    Transition(label='Data Ingest'),
    Transition(label='Status Check'),
    Transition(label='Forecast Update'),
    Transition(label='Risk Assess'),
    Transition(label='Scenario Sim'),
    Transition(label='Model Run'),
    Transition(label='Option Select'),
    Transition(label='Team Review'),
    Transition(label='Plan Approve'),
    Transition(label='Procure Adjust'),
    Transition(label='Route Replan'),
    Transition(label='Inventory Shift'),
    Transition(label='Execute Updates'),
    Transition(label='Monitor KPIs'),
    Transition(label='Feedback Loop')
])

root.order.add_edge(Transition(label='Data Ingest'), Transition(label='Status Check'))
root.order.add_edge(Transition(label='Data Ingest'), Transition(label='Forecast Update'))
root.order.add_edge(Transition(label='Status Check'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Forecast Update'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Scenario Sim'))
root.order.add_edge(Transition(label='Scenario Sim'), Transition(label='Model Run'))
root.order.add_edge(Transition(label='Model Run'), Transition(label='Option Select'))
root.order.add_edge(Transition(label='Option Select'), Transition(label='Team Review'))
root.order.add_edge(Transition(label='Team Review'), Transition(label='Plan Approve'))
root.order.add_edge(Transition(label='Plan Approve'), Transition(label='Procure Adjust'))
root.order.add_edge(Transition(label='Plan Approve'), Transition(label='Route Replan'))
root.order.add_edge(Transition(label='Plan Approve'), Transition(label='Inventory Shift'))
root.order.add_edge(Transition(label='Procure Adjust'), Transition(label='Execute Updates'))
root.order.add_edge(Transition(label='Route Replan'), Transition(label='Execute Updates'))
root.order.add_edge(Transition(label='Inventory Shift'), Transition(label='Execute Updates'))
root.order.add_edge(Transition(label='Execute Updates'), Transition(label='Monitor KPIs'))
root.order.add_edge(Transition(label='Monitor KPIs'), Transition(label='Feedback Loop'))