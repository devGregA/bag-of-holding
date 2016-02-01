from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from boh.core.applications.models import Application


@login_required
def list(request):
    applications = Application.objects.all()

    return render(request, 'frontend/applications/list.html', {
        'applications': applications
    })


@login_required
def overview(request, application_id):
    application = get_object_or_404(Application, pk=application_id)

    # Experimental
    from boh.core.activities.models import Event
    Event.objects.create_event(request.user, 'viewed', target=application, public=False)

    #is_following = application.is_following(request.user)
    #print('following: ' + str(is_following))
    #print(application.is_following(user=request.user))

    activity_feed = application.activity_feed()

    return render(request, 'frontend/applications/detail/overview.html', {
        'application': application,
        'activity_feed': activity_feed,
        'tab': 'overview'
    })


@login_required
def engagements(request, application_id):
    pass


@login_required
def benchmarks(request, application_id):
    application = get_object_or_404(Application, pk=application_id)

    return render(request, 'frontend/applications/detail/benchmarks.html', {
        'application': application,
        'tab': 'benchmarks'
    })
