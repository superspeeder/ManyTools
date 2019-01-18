
format_ = """
list = "name {
<data>
}"

data = "
'- name'
'[data-type]' 
'- name (<attribs>)'
"
comments = "//comment"

attribs = "key:<value>"

value = "
'number<unit>'
'"percentage%"'
'reference'
'"string"'
'<flag>|<flag2>'.....
'<flag>'
"

flag = "
'flag-name'
'variable-flag< <input> >'
'variable-flag< <input> >&<condition>'
'variable-flag< <input> >%<method>'
'variable-flag< <input> >%<method>
"

flag -> input = "
* Remove variable-flags
'reference'
"

method = "
'method-name< <input> >'
'method-name< <input> >$<special-input>'
"

special-input = "method-name< <input> >"

condition = "condition-name< <input> >"

"""

test_data = """
// Parser Test Data

types {
- Item
- Character
- Enemy
- Enviroment
- Material
- Weapon
}

units {
[weight]
Pounds, Pound = lb, lbs
Grams, Gram = g
Kilograms, Kilogram = kg
Milligrams, Milligram = mg

[distance]
Yards, Yard = yd, yds
Feet, Foot = ft
Inches, Inch = in
Meters, Meter = m
Kilometers, Kilometer = km
Centimeters, Centimeter = cm
Millimeters, Millimeter = mm
Nanometers, Nanometer = nm

[liquidvolume]
Liters, Liter = l
Kiloliters, Kiloliter = kl
Milliliters, Milliliter = ml
Ounce, Ounces = oz
}

materials {
- wood (strength:"15%",durability:"22%")
}

flags {
- can-be-used-as-weapon (#ITEM_TO_WEAPON TRUE;#WEAPON_TO_ITEM TRUE)
- picked-up-off-ground (#ITEM_IS_COLLECTABLE TRUE;#ITEM_IS_DROPPABLE TRUE)
}

methods {
- cut-off *RESTRICT_INPUT(MUST_BE_TYPE ITEM|ENVIROMENT) *ACTIONS(SELECT $INPUT;MALFORM REMOVE $ITEM_IN;GIVE_PLAYER $ITEM_IN) *ALLOW_RUN_CONDITIONS(TRUE) *ACTION_RESULT_AFFETORS(lowerstat <- DOWNGRADE_STATISTIC $AFFECTOR_INPUT [$SPECIAL_INPUT])
- percent *RESTRICT_INPUT(FITFORMAT NUMBER%)
}

objects {
[Item]
- branch (weight:4lbs,length:10ft,width:4in,material:wood,flags:can-be-used-as-weapon,collection-methods:picked-up-off-ground|cut-off<tree>&using<axe|saw>|broken-off<tree>%lowerstat<durability>$percent<15>)
- twig!branch (weight
