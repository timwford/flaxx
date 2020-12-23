# Flaxx

A unified platform for data transmission and expression on the async Python stack and common mobile platforms for rapid, seamless, no-compromise development.

## Intro

Say something...

## Project Structure

So that everything can be found and named what is expected, let's get our project set up with the correct structure. 

```
repository_name
- app
-- app.py
-- models.py
-- schemas.py
-- enums.py
-- database.py
-- android/
-- ios/
```

You will have whatever your repository is called as your main directory and an `app` folder will be located directly inside that repository folder.
Everything else will be stored in there. Here's what "everything else" is:

#### app.py

This is where your [FastAPI](https://fastapi.tiangolo.com/) web app will live.
While this is a good start, refer to the FastAPI docs for how to appropriately scale a FastAPI project's size using routers.

#### models.py

This is where your [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/index.html) models are stored. Everything from this point out will be largely taken care of, so write these once and see them manifest themselves everywhere!

#### schemas.py

This is where the [Pydantic](https://pydantic-docs.helpmanual.io/) models that are used by FastApi for JSON serialization and type validation. This file will be populated automatically for you by Flax.

#### enums.py

You can declare any helpful enums in Python in this file and they will be converted to their Swift and Kotlin counterparts. TODO: If the name of the enum matches the name of a model in the `models.py` file and the model does not have a description provided, the description will be a string reprentation of the enum. This follows from the unified data language theory. Everything in your platform should be written, documented, and expressed once.

#### database.py

This is where your database configuration information is.

#### android/

This folder contains anything that is generated for the Android/Java/Kotlin platform

#### ios/

This folder contains anything that is generated for the iOS/Swift platform.

## Python Setup

Probably Python 3.9 with like some stuff about Venv and like install my package a specific way and it will install the entire stack's dependency list and maybe some other stuff.

## Tortoise ORM Setup

The model in the ORM is the source of all of your data. 
This is the single source of truth for data transmission across the entire platform.
This write once, see it everywhere paradigm allows for incredibly fast development. 
Add anything you need and it shows up everywhere! 
Let's see how we can use it.

### Basics

What an ORM does, what Tortoise is and does, and whatever else you want to add.

### Defining a model

The basics of making a model, probably follow a real life example.

### Getting Pickier about what's allowed

How Tortoise can restrict certain things about a field.

### Documenting your Data

All the different ways your data can be documented.
Descriptions, maybe the enum thing, whatever.

### Best Practices

Something about string overrides and whatever other cool shit you find

## Pydantic Model Conversion

### Basics

What a Pydantic model is, why it's necessary, how it's used in FastAPI, and the bare miniumum about how it's generated.

### What's going on

A more in depth discussion about what's going on underneath the hood of the generation.

## Migrations with Aerich

### The Basics

Explain what database migration is, why its necessary, and how to use it.

### Database Setup

Mention how SQLlite is broken or fix it, I haven't tested MySQL, buy postgres is blazing fast and works incredibly well.

### Initizalizing

How to set up Aerich in your project.

### Migrating

How migrations work in Aerich

### Best practices

Maybe some of the shell scripts that you create that ease the process of migration and other things that you learn that make this faster and easier.

## FastAPI Web App

### The Basics

What FastAPI does, is, and uses and what it offers you.
A link to it's docs.
Whatever else you find fascinating about FastAPI.

### A FastAPI App

Basic app setup and stuff.

### A GET Endpoint

A basic GET endpoint that get's the example schema.

### A POST Endpoint

A basic POST endpoint that creates the example schema.

### Next Steps

## Mobile Model Generation

### The Basics

Explain what this is used for and the capability it has

### Android

Explain all Android capabilities

### iOS

Explain all iOS capabilities
