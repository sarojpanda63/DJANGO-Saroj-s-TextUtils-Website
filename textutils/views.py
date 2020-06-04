#My File - SAROJ
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')
def saroj_analyze(request):
	djtext	=request.POST.get('saroj_text', 'Default')
	s_removepunc =request.POST.get('saroj_removepunc','off ')
	s_fullcaps =request.POST.get('saroj_fullcaps','off ')
	s_newlineremover =request.POST.get('saroj_newlineremover','off ')
	s_extraspaceremover =request.POST.get('saroj_extraspaceremover','off ')	
	analyzed=""
	params={'purpose':'', 'analyzed_text':analyzed}
	if s_removepunc == "on":
		analyzed=""
		Punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		for char in djtext:
			if char not in Punctuations:
				analyzed+=char
		params={'purpose':params['purpose']+',Removed Punctuations', 'analyzed_text':analyzed}
		djtext=analyzed
	if(s_fullcaps=='on'):
		analyzed=""
		for char in djtext:
			analyzed = analyzed + char.upper()
		params={'purpose':params['purpose']+',Changed to Uppercase', 'analyzed_text':analyzed}
		djtext=analyzed
	if(s_newlineremover=='on'):
		analyzed=""
		for char in djtext:
			if char != "\n" and char !="\r":
				analyzed = analyzed + char
		params={'purpose':params['purpose']+',New Line Removed', 'analyzed_text':analyzed}
		djtext=analyzed
	if(s_extraspaceremover=='on'):
		analyzed=""
		for index, char in enumerate(djtext):
			if index < (len(djtext)-1):
				if not(djtext[index] == " " and djtext[index+1]==" "):
					analyzed = analyzed + char
			else:
				analyzed = analyzed + char
		params={'purpose':params['purpose']+',ExtraSpaceRemoved', 'analyzed_text':analyzed}
	if (s_removepunc!="on" and s_fullcaps!="on" and s_newlineremover!="on" and s_extraspaceremover!="on"):
		return HttpResponse("Please select atleast one operation")
	return render(request, 'analyze.html', params)