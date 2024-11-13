### 1. Navigate to your squish installations ```etc``` directory, create a file named ```squishserverrc```, and add the line ```ALLOWED_HOSTS=\*```

![Screenshot 2024-11-12 170240](https://github.com/user-attachments/assets/c6d3cb1e-2749-466b-a764-bc511e36c2d1)

### 2. Navigate to your squish installations ```bin``` driectory and add an attachable aut to the server using ```./squishserver --config addAttachableAUT <aut_name> localhost:<aut_port>``` 

![Screenshot 2024-11-12 170810](https://github.com/user-attachments/assets/dd5a18bb-d702-4d86-80d4-56229c4be8eb)

### 3. Start the server using ```./squishserver --port <server_port>``` (port is optional and the default is 4322) and keep this window open

![Screenshot 2024-11-12 171016](https://github.com/user-attachments/assets/0aff68e3-277e-4a5a-966c-780de9e6eb3a)

### 4. Open a new terminal window, navigate to the ```bin``` directory again, run the attachable aut using ```./startaut --port=<aut_port> <aut_path>```, and keep this window open

![Screenshot 2024-11-12 172550](https://github.com/user-attachments/assets/4d18ca3e-0ce2-44f8-ba46-9da37d88d0c8)

### 5. Open the Squish IDE on the device that will be controlling the tests, then click Edit->Preferences->Squish->Servers->Add->Remote server. Enter a name for the server, then the ip address of the machine running the server(enter ```localhost``` if ide and server are running on the same device), and then the port number used when starting the server(default is 4322). Then click Add, select the new server, and click Set as Default->Apply and Close

![Recording 2024-11-12 182527 (2)](https://github.com/user-attachments/assets/e7403aa0-c717-42aa-9a78-b60cdef7058b)

### 6. In your test script, change ```startApplication("<aut_name">)``` to ```attachToApplication("<aut_name>")```

![Screenshot 2024-11-12 183438](https://github.com/user-attachments/assets/0574e2e3-680e-4aff-a123-1168c1a8ccab)

### 7. You can now run/record tests on the already running application.

![Recording 2024-11-12 185034](https://github.com/user-attachments/assets/4637bbb4-ba6d-49b7-b099-5c6ce42680df)
