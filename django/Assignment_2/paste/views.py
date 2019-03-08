from django.shortcuts import render

posts = [
	{
	'user':'Barry McKockinner',
	'title':'Code Upload 1',
	'content':'pastebin.code(<virus></virus>)',
	'date_posted':'June 5th, 2020'
	},
	{
	'user':'Snowden',
	'title':'Code Upload 2',
	'content':'pastebin.code(<virus></virus>)',
	'date_posted':'June 5th, 2020'
	}

]



def home(request):
	return render(request, 'paste/home.html')

def about(request):
	return render(request, 'paste/about.html')

