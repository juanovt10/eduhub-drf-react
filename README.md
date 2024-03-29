# Eduhub Learning Platform - API

Eduhub is a learning platform design for people that want to master knowledge by teaching others. The platform allows them to create courses and interact with other users throught reviews. This seciton of the project with the REST API powered by the Django Rest Framework to support the ReactJS front end. 

- Here you can find the [backendAPI render]
- Here you can find the front end live site
- Here you can find the front end repository

## Table of contents

+ [User stories](#user-stories)
+ [Database](#database)
+ [Testing](#testing)
+ [Technologies used](#technologies-used)
+ [Deployment](#deployment)
+ [Credits](#credits)

## User Stories

To be filled

## Database

The database schema is composed by five models: user profile, course, ratings, enrollments and wish lists. 

When a new user signs up on the website, a user profile instance is automatically generated, utilizing a One-to-One Field with the username. Subsequently, the user is requested complete their profile information with the EditProfileForm to finalize the profile details.

The course model contains the owner as foregin key, representing the username who created the posts, followed by character and text fields. 

The rating model contains the owner and course as foreign keys, then followed by the rating value and review content. 

Finally, the enrollments and wish lists models are only related to the timing where they are created and related to the course and owner. This are key for each user to review which courses do htey have in their enrollment lists and wish list. 

![databseSchema](/static//readme-images/databaseSchema.png)

## Testing

All fi