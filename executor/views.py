import paramiko
from django.http import JsonResponse
import json

def execute_script(request):
    # Get the token and other parameters from the request
    token = request.GET.get('token')
    server_name = request.GET.get('server_name')
    # script_location = request.GET.get('script_location')
    f=open('./cred/data.json')
    data= json.load(f)
    # Authenticate the token (you can use Django's built-in authentication or a custom implementation)
    try:
        if token != data[server_name][1]:
            return JsonResponse({'error': 'Invalid token'})
    except:
        return JsonResponse({"error":"Invalid server"})

    print(server_name)
    # private_key = paramiko.RSAKey.from_private_key_file("./cred/Sonarqube.pem")
    # Create an SSH client to connect to the server
    # k = paramiko.RSAKey.from_private_key_file("./cred/Sonarqube.pem")
    ssh_client = paramiko.SSHClient()
    # ssh_client=ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_name, username="sonarqube", key_filename="./cred/id_rsa")

    # Execute the script on the server
    script_location=data[server_name][0]
    stdin, stdout, stderr = ssh_client.exec_command(script_location)

    # Get the output and error messages
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    # Close the SSH client
    ssh_client.close()

    # Return the output and error messages as a JSON response
    return JsonResponse({'output': output, 'error': error})
