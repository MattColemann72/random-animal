# Random Animal Generator

## Brief & Requirements

You are required to create a service-oriented architecture for your application. This application must be composed of at least 4 services that work together.

<br>

## Planning

<br>

### Trello Board
![Trello Board Day 1](https://github.com/MattColemann72/random-animal/blob/dev/misc/Trello-board.jpg)
[Trello Link](https://trello.com/b/WSZJLkvZ/animal-generator)

<br>

The Trello board has helped me to manage what I've done and what I have needed to do. I've kept it really basic so that I can't confuse myself or anyone who wants to view it.
I've also used my trello board to store my user stories. 

<br>

### User Stories
![User Stories](https://github.com/MattColemann72/random-animal/blob/dev/misc/User-stories.jpg)<br>
My user stories describe what my webapp should do. This has been useful for me when I was programming the app so that I knew exactly what I wanted to achieve.
The user needs to be able to what animals they are merging together, the animal that has been created and finally the last 5 animal names that were generated.<br>With the briefness of the user stories I know that I need to generate 2 random animal names then merge the two of them into one name. Once this is done I know that I need to store the newly created names in a database so that I can show the previous 5 of them, then I can print the two names of the animals to the screen along with the made up animal name.

<br>

### Entity Diagram
![ERD](https://github.com/MattColemann72/random-animal/blob/dev/misc/erd-proj2.jpg)<br>
The entity diagram for this project is very simple with it being just the one table with no relationships. All I wanted to store was the made up name generated from the two animal names given. Like I have previously stated, I will then be able to grab the stored names to show them to the user.

<br>

### Risk Assessment

For my risk assessment I started with putting as many things down that I could think about before I started the project. As with anything though I ran into risks during the project and this can be seen in the image below. For example, I rand into a problem where I was constantly running out of space on my VM so I couldn't do any more builds. This therefore, went into the risk assessment as it would cause the application to not be able to run any future updates. Luckily this was a quick fix being able to purge all of the previous builds, but the first thing I did was setup a new VM before I knew you could do this.
![Risk Assessment](https://github.com/MattColemann72/random-animal/blob/dev/misc/Riskassessment-proj2.jpg)<br>

<br>

### Continuous Deployment & Integration Pipeline
The CI-CD pipeline shown in the image below is how I have set up my project. I've used it to automate the majority of processes which in the long run saves a lot of time in development.
![CI/CD](https://github.com/MattColemann72/random-animal/blob/dev/misc/CI-CD_Pipeline-proj2.jpg)<br>

<br>

### Jenkins
Jenkins is used to manage my CI-CD pipeline and plays a major role in automation. For example without Jenkins, I would have to build the project manually each time. But by using a webhook linked with my GitHub account Jenkins automatically builds the webapp after each push to a specified branch. During development I used the dev branch for this. But after development I will be using my main branch. This is so that only the fully completed features are pushed to the live application rather than features still in development.<br>In the future I could setup another Jenkins server so that I could run a development server alongside the live server, to test out features properly before going live. 
![Jenkins Screenshot](https://github.com/MattColemann72/random-animal/blob/dev/misc/Riskassessment-proj2.jpg)<br>
As can be seen in the image above there are various stages for my pipeline, in particular, testing, building, pushing, config management and deployment. 

<br>

## Architecture

### Docker-Compose
I used Docker-Compose to create multiple containers which allowed me to run 4 services at a time on the same IP address whilst being able to communicate with each other. This allowed me to use my main service (service-1) to talk to each of the other 3 to get information or post information, to then be displayed in the HTML web page. I used Dockerfiles to create the images which, in turn, create the containers. There is a different Dockerfile for each of the four services.

<br>

### Docker-Swarm
Docker-Swarm(DS) is a container orchestration tool, which allowed me to manage the multipe containers across a host of machines(Manager(s) & Worker(s)). The benefits of this is that if I were to send an update out to the webapp, users could still use the application as DS balances the roll-out of the update over the hosts(VMs)

<br>

### NGINX
I used NGINX as a load balancer and reverse proxy. NGINX uses the DS hosts to balance the load equally across each of the VMs. The NGINX VM is the only url a user needs since the reverse proxy being used. This has additional security benefits.

<br>

### Ansible
Ansible is great for configuration. For example, I can use Ansible to setup groups such as the worker and manager hosts, which I brefly talked about in DS, and give them roles so that I don't need to go into each individual VM to change the same configuration files over and over again. This obviosly adds to the automation pipeline and saves so much time in the long and short term.

<br>

## Front-End
![WebApp Screenshot](https://github.com/MattColemann72/random-animal/blob/dev/misc/front-end-design.jpg)<br>
[Animal Generator](http://34.105.185.232)
