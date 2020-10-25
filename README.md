# Lab Explorer
Weclome judges (and others) to our ukfast hackathon submission

## What it does
Lab Explorer is a way to map, ping, bring up and identify machines in your lab, with a top-down lab view and per-rack view, all in the comfort of your terminal.

## Demonstration
- Please play '2020-10-25 16-55-15.mkv' for demonstration of functionality
- Please play 'WIN_2010-25_16_28_3_pro.mp4' for demonstation IPMI locator functionality

## How to run it
Suggested OS: GNU/Linux
- Install python3 and pip from your favorite package manager
- Run $ pip install getmac
- Clone this repository
- In the repository, start the program with either $ python main.py or just $ ./main.py

## How to use it
- Upon initial launch, the software will ask you whether you want to scan your network for known computers
- Pressing 'y' will run a quick scan across the network for online computers, and create a list for you to choose what you want to add to your lab
- A new lab will be created, fill out the details such as name 
- Pick the number of the machines you want to configure
- A lab will be created with your machines. 

- Any subsequent runs of the program will ask you which lab you wish to use (usually there is only one)
- Punch in the number of the lab that you would like to use
- A top-down view of the labs is now presented
- Press enter or type in h to view your options
- Select which rack you want by punching in v, <RETURN>, followed by the rack number
- A rack view is now displayed, here you can get information and actions about existing systems.
