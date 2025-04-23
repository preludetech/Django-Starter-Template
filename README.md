# Modern Frontend Django template repo 

There are many excellent Django templates out there. They all have different priorities and opinions. 

This template repo is different from the rest in that it's primary focus is frontend development, and frontend testing.

You could simply use this repo as a starting point for your own work - download it however you choose, and start adding your own code to the mix. 

Or you can poke around and use this as a learning resource. Make sure you understand how everything was wired up and why certain decisions were made.  

The latter is the best bet if you want to grow your own skills - it's likely that you will have different preferences, you might want to lay out your project in different ways and use different tools. That's perfectly normal. In fact, creating your own opinionated template repo is a useful learning experience :) 

## Brought to you by...

This template was brought to you by [Prelude](https://prelude.tech).

Prelude offers well crafted, expert supported learning experiences designed to set you up for long term success. 

We take a different approach to teaching. Rather than relying on traditional, one-size-fits-all methods, we design our programs using years of experience, evidence-based practices, and real learner feedback.

Our learning experiences are immersive, self-paced, supported by experts, and deeply human. We’re committed to your long-term success and growth — not just short-term outcomes.

Education is not the filling of a pail, but the planting of a seed.

## Honorary mentions  

Here are a few other Django templates that are worth learning from

- https://github.com/lincolnloop/django-layout/blob/main/pyproject.toml 
- https://github.com/jefftriplett/django-startproject 
- https://github.com/wsvincent/lithium/blob/main/pyproject.toml

## Work in progress 

This template repo is not a complete and final masterpiece, it's a work in progress and has a few rough edges. If you see a todo somewhere in the code and you want to fix it, PRs are welcome. 

## Installation 

This is a Django application so we'll be going through how to get things set up to allow you to run `runserver` and the tests. 

### 1. Postgres 

The first thing to know is that this project relies on Postgresql. In order to run the application or the tests, you need to have Postgres up and running. So we'll start there.

Postgres is run using a docker composition in the `dev_db` directory. It is set up in a way that just works with the development settings. 

To run the database:

```
cd dev_db
docker compose up
```

There is also a README inside the dev_db directory with more information.

This docker composition needs to be running whenever your Django application needs to interact with the development database. Eg while testing, migrating or running the server. Best to keep it open and running in a terminal.

### 2. Install Django and dependencies

We are using `uv` as a package manager. Follow the instructions [here](https://github.com/astral-sh/uv) to install it. 

Then run `uv sync` - this will set up a virtual environment in a directory called `.venv`. This environment works in the usual way.

Going forward, if you need to run a command using this environment you have the option of activating the environment or using the `uv run` command. Eg `uv run pytest`

### 3. Tailwind 

This website used the tailwind command-line client. Install it like so:

```
npm i
```

Once installed, you will have access to these two commands:

```
npm run tailwind_build
npm run tailwind_watch
```

`tailwind_build` executes the tailwind build process once. This is useful as a part of a deployment process.

`tailwind_watch` is more useful for development as it rebuilds the tailwind output css automatically as you make changes to your html or tailwind input file. 

If you are not planning to make visual changes, run `tailwind_build` once and then move on with your life. 

If you are going to be doing frontend work, it is useful to have `tailwind_watch` running in it's own terminal.

### 4. Run the development server 

Now you can run a few perfectly normal Django commands to get your local development server up and running:

```
# create the database tables
python manage.py migrate

# make some fake data inside the database tables so you have something to look at
python manage.py fake_news

# Run the server
python manage.py runserver
```

### 5. Running the tests 

We are using [Playwright](https://playwright.dev/python/) for browser automation tests. When you used `uv` installed all the dependencies, it installed Playwright, but we need to do one extra step.

```
playwright install
```

This will install all the necessary browsers. 

Once that is done, you can run the tests using `pytest`.

You can see a demonstration and tour of Playwright [here](https://www.youtube.com/watch?v=SmW8p3sDhzM). You'll get to see all the major features. 

## Application description

The code in this repo is a bit contrived - it is a very basic content management system. The main idea here is to demonstrate a few tools and get them to play nicely together.

Here is what the project does:

- Administrators can log into the admin panel to edit the content
- Regular users can sign up or sign in, either using email addresses and passwords, or through Github
- Users can view content
- Users can chat to each other about any piece of content. Every piece of content has a real time chat window. This is only available to logged in users

## Components, features and decisions 

What follows below is a description of the structure of the project - how it is built and what tools are being used. 

### The `config` directory 

The first decision is to do with project layout. The `config` directory contains all our project configuration. 

### Custom User Model 

The `accounts` app implements a custom user model. If you are ever likely to need a custom user model, make one up front.

### Package management with `uv` 

We already spoke about this earlier. 

### Installing Tailwind using npm 

There are tools such as [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) that try to take the complexity out of installing Tailwind. But this project uses plain ol' `npm` instead.

Reasons:

- We can choose what version of Tailwind we want to run (eg: the latest one)
- We have full control over the configuration 
- It's not very complicated once you have done it once

### Crispy tailwind 

Django forms are not pretty by default, [Crispy Tailwind](https://github.com/django-crispy-forms/crispy-tailwind) provides an opinionated solution. 

It's a useful starting point if you want good looking forms. It's very easy to install and use.

Downsides:

- It is very opinionated and might not match your style
- There doesn't seem to be any way to change those opinions, eg by providing your own classes
- It doesn't have a dark-mode (afaik)
- Newer versions of Tailwind do contain breaking changes so hard-coded opinions can potentially lead to frontend styling issues

**Watch this space** We'll be doing some work to find some alternatives that overcome these downsides

### AllAuth 

[Django AllAuth](https://docs.allauth.org/en/latest/) is used to provide the following:

- Email/pass registration and authentication 
- Email address validation
- Basic email template in place for comms 
- Login with Github

**Note:** If you want Github login to work, you will need to provide your own github client id and secret.  The approach to secret management will be explained later in this document.

You can see a demo of AllAuth's functionality in [this video](https://www.youtube.com/watch?v=sV7hNyhYCYA).

### Django Admin customisation with Unfold

[Unfold](https://github.com/unfoldadmin/django-unfold) is a Django admin theme that is beautiful by default, and very customizable. 

Features used:

- changed heading
- changed left hand navigation 
- added a custom dashboard page 

Take a look at the `UNFOLD` settings inside settings.py to see some of what we are doing. This barely scratches the surface.

### HTMX 

If you want an introduction to [HTMX](https://htmx.org/) and why it is awesome:

- [Why HTMX makes good business sense](https://www.youtube.com/watch?v=iP0XX9xkEGw)
- [HTMX versus React demo](https://www.youtube.com/watch?v=kYV8K71pY64)
- [Mother of all HTMX demos](https://www.youtube.com/watch?v=3GObi93tjZI)
- [Experience of porting from a React app to an HTMX app](https://www.sheenaoc.com/articles/2024-06-30-htmx)

TODO: Currently we are using the HTMX CDN. Rather NPM install it

### Django template partials 

One of the challenges with HTMX is that you can end up with a lot of templates. 

[Django Template Partials](https://github.com/carltongibson/django-template-partials) makes it a lot easier to organise your work.

### Cotton 

[Cotton](https://django-cotton.com/) is useful in conjunction with template partials. Cotton is used to create individual reusable components.

### Fancy markdown rendering 

Our news app defines an `Article` model, the content of the `Article` is a text field that gets rendered as markdown. 

The cool thing is that the markdown is rendered in a way that is aware of Django template syntax. This means you can use cotton components right in the article text.

Note that this is fairly experimental. It works by creating temporary template files in the `/tmp/` directory. This might not be a good idea. But it is interesting.

You can turn this functionality on or off using the `MARKDOWN_TEMPLATE_RENDER_ON` setting. It is off by default.

### AlpineJS 

We use [Alpine](https://alpinejs.dev/) to add minimal state management to our frontends. 

### Django Channels 

Real time 2 way chat is implemented using [Django Channels](https://channels.readthedocs.io/en/latest/)

### Playwright

We use [playwright](https://playwright.dev/python/) for frontend testing. 

Playwright was also used to test the 2 way chat application. This is not a simple thing to get right. If you need to test anything to do with Django Channels using a `live_server` fixture, then take a look at how the `channels_live_server` fixture is used.

### Postgres development database 

This was already explained in the Installation section of this document.

### Environmental variables  

We are using [django-environ](https://django-environ.readthedocs.io/en/latest/) and a `.env` file to handle environmental variables.

**Note** This is definately going to change in a future version of this template.

### Django Compressor 

[Django Compressor](https://django-compressor.readthedocs.io/en/latest/) is used to compress static css and js files.

### Click

[Click](https://pypi.org/project/django-click/) makes writing management commands nice and friendly.

### Django debug toolbar 

[This](https://django-debug-toolbar.readthedocs.io/en/latest/) is incredibly helpful. 

### Browser reload 

If you are working on Django frontend code, you often need to keep refreshing the page manually to see the effects of the changes you make. This is a pain.

[Django Browser Reload](https://github.com/adamchainz/django-browser-reload) makes life easier.
