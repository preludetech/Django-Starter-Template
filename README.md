# Modern Frontend Django template repo 

There are many excellent Django templates out there. They all have different priorities and opinions. 

This template repo is different from the rest in that it's primary focus is frontend development. 

## Using the template

You could simply use this repo as a starting point for your own work - download it however you choose, and start adding your own code to the mix. 

Or you can poke around and use this as a learning resource. Make sure you understand how everything was wired up and why certain decisions were made.  

The latter is the best bet if you want to grow your own skills - it's likely that you will have different preferences, you might want to lay out your project in different ways and use different tools. That's perfectly normal. 

## Learning about the tools 

This template was brought to you by [Prelude](https://prelude.tech).

Prelude offers well crafted, expert supported learning experiences designed to set you up for long term success.

We take a different approach to teaching. Rather than relying on traditional, one-size-fits-all methods, we design our programs using years of experience, evidence-based practices, and real learner feedback.

Our learning experiences are immersive, self-paced, supported by experts, and deeply human. We’re committed to your long-term success and growth—not just short-term outcomes.

Education is not the filling of a pail, but the [planting of a seed].

## Honorary mentions  

Here are a few other Django templates that are worth learning from

- https://github.com/lincolnloop/django-layout/blob/main/pyproject.toml 
- https://github.com/jefftriplett/django-startproject 
- https://github.com/wsvincent/lithium/blob/main/pyproject.toml

## Installation 

To get everything running:

... 

## Components, features and decisions 

This section will give an explanation of the major tools used and the decisions made. 

The code itself is a bit contrived - it is a very basic content management system. The main idea here is to demonstrate a few tools and get them to play nicely together.

Here is what the project does:

- Administrators can log into the admin panel to edit the content
- Regular users can sign up or sign in, either using email addresses and passwords, or through Github
- Users can view content. Some content is only visible to logged in users 
- Users can chat to each other about any piece of content. Every piece of content has a real time chat window

### The `config` directory 

The first decision is to do with project layout. The `config` directory contains all our project configuration. 

### Custom User Model 

### Package management with `uv` 

### Installing Tailwind using npm

### Crispy tailwind 

### AllAuth 

- Email/pass authentication
- Basic email template in place for comms 
- Login with Github enabled

### Django Admin customisation with Unfold

- Using Unfold instead of the default admin
- Added custom pages and dashboards
- Minor customisations

### HTMX 

### Django template partials 

### Cotton 

### Django debug toolbar 

### Browser reload 

### Fancy markdown rendering 

This makes use of Cotton components

### AlpineJS 


### Playwright

### Environmental variables 

### Postgres development database 


### Environmental variables  


### Django Compressor 

https://django-compressor.readthedocs.io/en/latest/



## TODO:

- Document all the things 
- Install HTMX etc using npm rather than using a CDN 
- Tidy up code 
- Make GUI prettier