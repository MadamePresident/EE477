# EE477
Mini Course on Robotic Simulation

# ROS Package: my_topics
	This ROS package publishes the count to the topic counter, increments the count, sleeps until it needs to iterate again adaptively (publisher), subscribes to what is being published, and prints the counter (subscriber). This continues until told to stop. The package is useful for keeping track of counts. 

## Requirements
	This will work on Linux Ubuntu Bionic 64 bit with ROS Melodic Morenia. This can be run on any operating system by using a virtual machine equipted with the above. Python is the coding language. 

## Installation and Configuration
	Install package by cloning or forking from GitHub to your own repository. Change package names to reflect your own. In the text files within each package, change the import "from" to reflect your own package name instead of "from my_topics".

## Getting Started
	To use the package, navigate to the directory containing your "my_topics" and launch using the command "roslaunch my_topics my_topics.launch". This will launch the package through its launch file and display a summary of the package, then start printing the counter. To stop execution, press "CTRL+C" on the keypad. 

## Usage
	Use as directed in "Getting Started" section. Package is fairly simple to use. There are several files inside of package that can be changed or updated to enhance usage. Keep track of these files and your changes in order to troubleshoot any issues that may occur. 

# ROS Package: my_services
	This package takes a string of input from the user and counts how many words it contains. This is useful for determining a word count. It could be especially useful in the case of long papers with word limits or requirements. 

## Requirements
	This will work on Linux Ubuntu Bionic 64 bit with ROS Melodic Morenia. This can be run on any operating system by using a virtual machine equipted with the above. Python is the coding language. 

## Installation and Configuration
	Install package by cloning or forking from GitHub to your own repository. Change package names to reflect your own. In the text files within each package, change the import "from" to reflect your own package name instead of "from my_services".

## Getting Started
	To use the package, navigate to the directory containing your "my_services" and launch using the command "roslaunch my_services my_services.launch input:="some string of words to be counted". This will launch the package through its launch file and display a summary of the package, then display your string and how many words it contains. To stop execution, press "CTRL+C" on the keypad. 

## Usage
	Use as directed in "Getting Started" section. Package is fairly simple to use. There are several files inside of package that can be changed or updated to enhance usage. Keep track of these files and your changes in order to troubleshoot any issues that may occur. 

# ROS Package: my_actions
	This package keeps track of the time that it takes for the package to launch as well as its state, status, and the updates sent. This is useful for determining how quickly the system is operating. Tracking this over time could reveal processor efficiency and/or aging. 

## Requirements
	This will work on Linux Ubuntu Bionic 64 bit with ROS Melodic Morenia. This can be run on any operating system by using a virtual machine equipted with the above. Python is the coding language. 

## Installation and Configuration
	Install package by cloning or forking from GitHub to your own repository. Change package names to reflect your own. In the text files within each package, change the import "from" to reflect your own package name instead of "from my_actions".

## Getting Started
	To use the package, navigate to the directory containing your "my_actions" and launch using the command "roslaunch my_actions fancy_action.launch". This will launch the package through its launch file and display a summary of the package, then the state, status, the time elapsed to complete, and the updates sent. The process should finish cleanly. Press "CTRL+C" to stop execution. 

## Usage
	Use as directed in "Getting Started" section. Package is fairly simple to use. There are several files inside of package that can be changed or updated to enhance usage. Keep track of these files and your changes in order to troubleshoot any issues that may occur. 
