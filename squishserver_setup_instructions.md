## Option 1
Follow these steps if you want tests to start and stop the application each time they are run.
1. Navigate to your squish installations ***bin*** directory and add an aut to server using ***./squishserver --config addAUT <aut_name> <aut_path>***

    ![Screenshot 2024-11-12 145355](https://github.com/user-attachments/assets/51034937-e44f-49d1-835f-59c76f8e8360)

2. Navigate to your squish installations ***etc*** directory, create a file named ***squishserverrc***, and add the line ***ALLOWED_HOSTS=\****

    ![Screenshot 2024-11-12 145943](https://github.com/user-attachments/assets/c28a673a-b6db-4b8a-8aac-64b56eb36615)

3. Navigate back to the ***bin*** directory and start the server ***./squishserver --port \<port>*** (port is optional and the default is 4322).

    ![Screenshot 2024-11-12 150241](https://github.com/user-attachments/assets/fae78efd-07bd-462e-9ae6-081aa7a91805)

4. Now open your squish ide and click edit, preferences, squish, servers, add, remote server. Then enter any name for the server, the ip address of host machine(use ***localhost*** if ide and server are running on same machine), and the port number you used when starting the server(default is 4322). Then click add and also set the server as default.

    ![Screenshot 2024-11-12 152334](https://github.com/user-attachments/assets/1126ec9f-2e5a-4ded-a68b-9282bece0676)

5. Now you can run tests through the ide on a local or remote machine through that remote server.
