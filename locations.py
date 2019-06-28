
#location information
locations = [
{
'name' : 'Starting Platform',
'description' : 'You are at the main train station platform.',
'options' : 
"""--Option-- north: Ticket booth
--Option-- south: Go sit on a bench
--Option-- wait: Wait awhile
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Ticket Booth',
'description' : "You walk up to the ticket booth. Lucky you, there isn't a line.",
'options' : 
"""--Option-- buy: Buy a ticket
--Option-- south: Starting area towards the bench
--Option-- wait: Wait awhile
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Bench',
'description' : "Nice. There's an open bench you can sit on.",
'options' : 
"""--Option-- sit: Walk to the bench and sit on it
--Option-- north: Head back to the starting area
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 1',
'description' : """You enter train car 1 and you see a sword.
It beckons you to pick it up.
You are the chosen one""",
'options' : 
"""--Option-- sword: Fulfill your destiny and pick up the sword!
--Option-- south: Move back to next train down
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 2',
'description' : "You enter train car 2 and it stinks.",
'options' : 
"""--Option-- north: Move to the next train up
--Option-- south: Head back to next train down
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 3',
'description' : "You try to enter train car 3 and squeeze in. It's full so try to move to another car because this is uncomfortable!",
'options' : 
"""--Option-- north: Move to the next train up
--Option-- south: Head back to next train down
--Option-- wait: Wait awhile standing and being annoyed
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 4',
'description' : "You enter train car 4 and hear screaming from the next car southward. You are very curious!",
'options' : 
"""--Option-- north: Move to the next train up
--Option-- south: Investigate the car southward
--Option-- wait: Wait awhile standing and ignoring the screams
--Option-- bag: Check your bag inventory
""",
},
{
'name' : 'Train Car 5',
'description' : """You enter train car 5 and immediately see carnage.
In the middle of the car, the thing is staring at you""",
'options' : 
"""--Option-- fight: Fight the monster
--Option-- north: RUN back to next train up
--Option-- wait: Wait awhile standing
--Option-- bag: Check your bag inventory
""",

},
]
