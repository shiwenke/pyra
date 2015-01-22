from pyramid.view import view_config
import os
import subprocess,shlex
@view_config(route_name='home', renderer='templates/ui.pt')
def my_view(request):
   
    myvar=request.params.get('command',None)
    arg=shlex.split(myvar)

    #this runs the subprocess
    #run runr un
    #run
    myy=subprocess.check_output(arg,shell=True)
    #please tun

    return {'myvar': myy}

