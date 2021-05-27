
from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

style = style_from_dict({
	Token.Separator: '#f7f7f7',
	Token.QuestionMark: '#673ab7 bold',
	Token.Selected: '#cc5454',
	Token.Pointer: '#673ab7 bold',
	Token.Instruction: '',
	Token.Answer: '#f44336 bold',
	Token.Question: '',
})

questions = [
	{
		'type': 'checkbox',
		'message': 'Select Toppings',
		'name': 'toppings',
		'choices': [
			Separator('=== The Meats ==='),
			{'name': 'Ham'},
			{'name': 'Ground Meat'},
			{'name': 'Bacon'},
			Separator('=== The Cheeses ==='),
			{'name': 'Mozzarella', 'checked': True},
			{'name': 'Cheddar'},
			{'name': 'Parmesan'},
			Separator('=== The Usual ==='),
			{'name': 'Mushrooms'},
			{'name': 'Tomato'},
			{'name': 'Spinach'}
		],
		'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True
	}
]

answers = prompt(questions, style=style)
pprint(answers)
