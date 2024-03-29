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

All files passed the [PEP8 valdator] with no issues except by the more than 79 characters per line recomended by PEP 8. 

![pep8validator](/static//readme-images/PEP8Validator.png)

### Manual testing: 

Testing can be found in [other repo link]

### Fixed bugs

When adding the image specifications to the profile and course serializers I omited the return value for the profile serializer validated image method. This was leading to a big problem in the front end. The missing of the return value was then returning a null value for the image, making in unacceptable for the database. Therefore, if the user was not delete it straight away it could lock the application. 

To unlock the applicaiton and refresh the JWTs I had to multople times change the secret key and redeployed. Then after various attempts, the application was throwing a 500 error in the course resourse. Unable to pinpoint where was the issue, I decided, in conjunction with Code institue tutors, to reset the database and try again. This situation did unlocked the application and API but the issue was just addressed when I added the return statement in the validate image method in the profile serializer. 

### Unfixed bugs
- None

## Technologies used

### Programming Languages:

- Python

### Frameworks, Libraries & Programs Used: 

- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers

## Deployment 

ADD deployment steps 

## Credits 

ADD credits 


