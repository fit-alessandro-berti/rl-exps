from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Milk Sourcing'),
        Transition(label='Quality Testing'),
        Transition(label='Starter Culture'),
        Transition(label='Milk Fermentation'),
        Transition(label='Curd Cutting'),
        Transition(label='Whey Draining'),
        Transition(label='Pressing Cheese'),
        Transition(label='Cave Aging'),
        Transition(label='Sample Tasting'),
        Transition(label='Flavor Profiling'),
        Transition(label='Packaging Design'),
        Transition(label='Cold Storage'),
        Transition(label='Logistics Planning'),
        Transition(label='Pop-up Sales'),
        Transition(label='Customer Feedback'),
        Transition(label='Recipe Adjusting')
    ],
    order=[
        ('Milk Sourcing', 'Quality Testing'),
        ('Quality Testing', 'Starter Culture'),
        ('Starter Culture', 'Milk Fermentation'),
        ('Milk Fermentation', 'Curd Cutting'),
        ('Curd Cutting', 'Whey Draining'),
        ('Whey Draining', 'Pressing Cheese'),
        ('Pressing Cheese', 'Cave Aging'),
        ('Cave Aging', 'Sample Tasting'),
        ('Sample Tasting', 'Flavor Profiling'),
        ('Flavor Profiling', 'Packaging Design'),
        ('Packaging Design', 'Cold Storage'),
        ('Cold Storage', 'Logistics Planning'),
        ('Logistics Planning', 'Pop-up Sales'),
        ('Pop-up Sales', 'Customer Feedback'),
        ('Customer Feedback', 'Recipe Adjusting')
    ]
)

print(root)