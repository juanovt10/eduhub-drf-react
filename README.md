# Eduhub Learning Platform - API

Eduhub is a learning platform designed for individuals who want to deepen their knowledge by teaching others. The platform enables users to create courses and interact with others through reviews. This section of the project utilizes a REST API powered by Django Rest Framework to support the ReactJS frontend.

- Here you can find the [backend API render](https://eduhub-drf-api-8e84adf897cc.herokuapp.com/)
- Here you can find the [front end live site](https://eduhub-react-f1c98786bec1.herokuapp.com/)
- Here you can find the [front end repository](https://github.com/juanovt10/eduhub)

## Table of contents

+ [Database](#database)
+ [Testing](#testing)
+ [Technologies used](#technologies-used)
+ [Deployment](#deployment)
+ [Credits](#credits)

## Database

The database schema consists of five models: user profile, course, ratings, enrollments, and wish lists.

When a new user registers on the website, a user profile instance is automatically created, linked to the user's account through a One-to-One Field with the username. The user is then prompted to complete their profile information using the EditProfileForm to finalize the profile details.

The course model includes the owner as a foreign key, representing the user who created the course, along with various character and text fields for course details.

The ratings model includes owner and course as foreign keys, in addition to fields for the rating value and review content.

Lastly, the enrollments and wish lists models are associated with the time they were created and are linked to both the course and owner. These models are crucial for users to manage which courses they have enrolled in and added to their wish lists.

![databseSchema](/static//readme-images/databaseSchema.png)

## Testing

All files passed the [PEP8 valdator](https://pep8ci.herokuapp.com/) with no issues except by the more than 79 characters per line recomended by PEP 8. 

![pep8validator](/static//readme-images/PEP8Validator.png)

### Manual testing: 

Testing can be found in [Eduhub front end repository.](https://github.com/juanovt10/eduhub)

### Fixed bugs

While adding image specifications to the profile and course serializers, I omitted the return value in the profile serializer's validated image method. This omission led to a significant problem in the frontend: the absence of a return value resulted in a null image value, which the database could not accept. Consequently, if not promptly removed, it could lock the application.

To unlock the application and refresh the JWTs, I repeatedly changed the secret key and redeployed it. After several attempts, the application encountered a 500 error related to the course resource. Unable to identify the exact problem, I decided, with advice from Code Institute tutors, to reset the database and try again. This action unlocked the application and API, but the issue was fully resolved only when I added the missing return statement in the validate image method of the profile serializer.

### Unfixed bugs
- None so far

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

### Running the project locally

1. Go to [Eduhub DRF API repository](https://github.com/juanovt10/eduhub-drf-react)
2. Clock on the "Code" button.
3. Choose one of the following three options and click copy.
    - HTTPS
    - SSH
    - Github CLI
4. Open the termial in your IDE.
5. Type `Git clone` and paste the url that was copied in step 3.
6. Press enter and the local clone will be created.

### Deploying with Heroku

The following steps were taken from the Django "Django Rest" walkthrough project provided by [Code Institute](https://codeinstitute.net/global/).

1. Login or create an account in [Heroku](https://id.heroku.com/login). 
2. Go to your dashboard on the top right and click the `New` dropdown button and select `Create New App`.
3. Enter a name of the project (must be unique).
4. Select the region your are working in. 

### External database set up

I used [ElephantSQL](https://www.elephantsql.com/) as my database. 

1. Login or create an account. 
2. In dashboard on the right top corner click `Create New Instance`
3. You will be forward to a `Select a plan and name`:
    - `Name` should be the name of the project
    - `Plan` should be the type of subscription you have with ElephantSQL, in my case I used the `Tiny Turtle (Free)` plan.
    - `Tags` can be left in blank

    Then click on `Select Region`.

4. Here selecte your `Data center`. This is hosted with AWS. In my case due to my location I used `AP-East-1 (Hong Kong)`. Then click `Review`.

5. Here you will check the name, cloud provider and region where the application will be hosted. If, everything is correct, click `Create instance`.
6. Go to dashboard and your instance will be there. Click in the name and under `Details` copy the `URL`, this will be values that will be needed for the [Heroku variables setup](#heroku-settings) and the [env.py](#envpy-file-set-up) file.

#### env.py file set up

1. In the root directory of your project create a new file called `env.py`.
2. Add this `env.py` file to your `.gitignore` file so the confidential information in the file is not push to Github.
3. In the `env.py` file import the `os` module and add the [database URL](#external-database-set-up).

```
os.environ["DATABASE_URL"]="<copiedURL>"
```

4. Then, using the same process create a `SECRET_KEY`. This can be anything, I used [RandomKeygen](https://randomkeygen.com/) to create a complicated key. 

```
os.environ["SECRET_KEY"]="<copiedGeneratedKEY>"
```

5.  Then add the development enviroment variable. Please note that this line needs to be connected out when setting up the external database to test that the database is connected.

```
os.environ['DEV'] = '1'
```

6. Then, using the same process, in the `env.py` file import the `os` module and add the [storageURL](#external-storage-set-up).

```
os.environ["CLOUDINARY_URL"]="<copiedCloudinaryURL>"
```

7. Save the file.

#### Heroku settings 

After the application is created in Heroku. Got to your dashboard and you will see the application name, click on it and then follow the following: 

1. Go to the settings tab and go to `ConfigVars` and click on `Reveal Config Vars` and set the following variables: 
    - Key: `ALLOWED_HOST`, Value: `front end deployed url`
    - Key: `DATABASE_URL`, Value: [databaseURL](#external-database-set-up)
    - Key: `CLOUDINARY_URL`, Value [storageURL](#external-storage-set-up)
    - Key: `SECRET_KEY`, Value: [randomKey](#envpy-file-set-up)
    - Key: `CLIENT_ORIGIN`, Value: `front end deployed url`
    - Key: `CLIENT_ORIGIN_DEV`, Value: `front end local url`
    - Key: `DISABLE_COLLECTSTATIC`, Value: `1`

2. After setting up the variables, go to `Buildpacks` and select `Python`.

#### Heroku deployment 

1. Go to `Deploy` tab and under `Deployment method` connect to the Github repository.
2. Then there can be two options: manual or automatic deployment. 
    - Manual deployment means that it will be necessary to go to Heroku and deploy the application each time that changes are made. 
    - Automatic deployment will re-deploy the application each time new code is pushed to Github. 
3. After selecting the deployment method, under `Manual Deployment` click `Deploy branch`. 

## Credits 

### Content 

- Modifications were made to the 'Profile' model, while I created the remaining four data models, serializers, and views.
- Rebecca from Code Institute Tutor Support helped me reset my database and guided me on the path to identifying the bug causing issues in my application.

### Media
- Default profile image was provided by [Code Institute](https://codeinstitute.net/global/) in their DRF-API project. 
- Default course image was sourced from [Freepik.](https://www.freepik.com/)


