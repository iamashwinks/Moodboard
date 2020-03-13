from django.shortcuts import render, redirect

from moodlog.models import Mood, Action, MoodLog

# Create your views here.

def dashboard(request):
	user = request.user

	moods = Mood.objects.all()
	actions = Action.objects.all()

	moodlogs = MoodLog.objects.filter(user=user).order_by("-timestamp")

	return render(request, "dashboard.html", {
			"moods":moods, 
			"actions":actions,
			"moodlogs":moodlogs
		})

def create_moodlog(request):
	if request.method == "POST":
		mood_id = request.POST["user_mood"]
		action_id = request.POST["user_action"]
		note = request.POST["user_note"]

		mood_instance = Mood.objects.get(pk=mood_id)
		action_instance = Action.objects.get(pk=action_id)

		moodlog = MoodLog.objects.create(
				mood=mood_instance,
				action = action_instance, 
				note = note,
				user = request.user
			)

		return redirect("/dashboard/")