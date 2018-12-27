from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
# Create your views here.
def hihi(request):
	hi = Comment.objects.all()
	comment = request.POST.get('comment',False)
	Comment.objects.create(comment=comment)
	overall = Comment.objects.all()

	return render(request,'index_t.html',{'hi':hi,'comment':comment,'overall':overall})