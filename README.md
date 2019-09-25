
*****
*****
*
*  FOLLOW THESE INSTRUCTIONS BEFORE EXTRACTING THE ARCHIVE IN THIS PROJECT!
*
*****
*****

Before you can use the sample provided here you MUST install the AWS IOT SDK for Javascript on your machine first. The instructions here can also be found at:

https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-sdk-node.html

If you don't have node and npm installed on your machine, you will need to do so. If you are using a Windows machine, you might want to consider enabling the Windows Subsystem for Linux and working from the shell (I find things work better that way)



    To add the Node repository, open a terminal and run the following command:

    curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -

    To install Node and npm, run the following command:

    sudo apt-get install -y nodejs

    To verify the installation of Node and npm, run the following commands:

    node -v

    and

    npm -v

    If a version number is displayed by these commands, node and npm are installed correctly.

Once you've got node and npm installed, you need to download the AWS IoT Device SDK for Javascript. Follow these steps for installing the SDK.

1. Make a directory ~/deviceSDK using the command

	mkdir ~/deviceSDK

2. Change the curreht directory to the deviceSDK directory using the command

	cd ~/deviceSDK

3. Install the AWS IOT Device SDK for Javascript using the command

	npm install aws-iot-device-sdk

4. When the download is complete, you should have a directory name node_modules in your ~/deviceSDK directory. If you look in the node_modules directory, you should see a directory named aws-iot-device-sdk. Change to this directory using the command

	cd ~/deviceSDK/node_modules/awt-iot-device-sdk

5. Now you can extract the contents of the tar file iot-sdk-sample.tar.gz into the current directory. This will overwrite the README.md file and the contents of the examples directory. This is why you need to install the SDK BEFORE extracting the the tar file. Use this command to extract the tarfile.

	tar -xvzf iot-sdk-sample.tar.gz

At this point, you should be able to run the sample code.

  node device-example -k "../certs/f89d719c91-private-key.pem" -c "../certs/f89d719c91-cert.pem" -H ajj0dtxgspdpk-ats.iot.us-east-2.amazonaws.com -p 8883 -T vas-demo-gpg1 --test-mode 1 -a "../certs/root-CA.crt"
