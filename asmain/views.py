from django.shortcuts import render

def pIndex(req):
	return render(req, 'asmain/index.html')