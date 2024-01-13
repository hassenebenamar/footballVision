# Documentation - Football Vision App 

## Table des matières

- [Introduction](#introduction)
- [Partie FootAndBall](#Partie FootAndBall)
- [Partie Django](#Partie Django)

## Introduction

Football Vision App est une application de vision par ordinateur basée sur le travail de Jac99 (https://github.com/jac99/FootAndBall). Elle utilise Pytorch et OpenCV pour effectuer la détection d'objets dans des vidéos. Notre projet vise à étendre les fonctionnalités de cette application et à l'intégrer à une interface web via un cadre architectural, en utilisant Django.

<img src="https://cdn.discordapp.com/attachments/1183508687923453956/1193901735861829713/homepage.png?ex=65ae66a3&is=659bf1a3&hm=8c8cd34d4ff13ff30957fef89cfe21f6db9d5c6734e1a46966cd440ded5d1a26&" alt="homepage">

## Partie FootAndBall

L'application FootAndBall permet de détecter les joueurs et le ballon de football dans une vidéo, par exemple un replay de match. Le résultat est une vidéo annotée avec des boîtes indiquant l'emplacement des objets détectés. 

Voici l'architecture de l'application :

<img src="https://cdn.discordapp.com/attachments/1183508687923453956/1195769999344812062/Image2.jpg?ex=65b53298&is=65a2bd98&hm=b0875bba66a4e296f5cb19a0cae088e7ef57b6a7895b17f84be5e58d25c51ad8&" alt="archiFootAndBall">

```python
run_detector(model, args) #main function, runs the detector
# model is the FootAndBall model already defined in the python file
# args is of type argparse :
    #'--path', help='path to video', type=str, required=True)
    #'--model', help='model name', type=str, default='fb1')
    #'--weights', help='path to model weights', type=str, required=True)
    #'--ball_threshold', help='ball confidence detection threshold', type=float, default=0.7)
    #'--player_threshold', help='player confidence detection threshold', type=float, default=0.7)
    #'--out_video', help='path to video with detection results', type=str, required=True,
    #                    default=None)
    #'--device', help='device (CPU or CUDA)', type=str, default='cuda:0')
numpy2tensor(image) #converts OPENCV image to tensor (with normalization)
# image is an OPENCV image
draw_bboxes(image, detections) #draw the detected boxes on the image
# image is an OPENCV image
# detections : array containing boxes, labels and scores.
```

## Partie Django

Football Vision App offre une interface web permettant aux utilisateurs de se connecter à leur tableau de bord et d'envoyer une vidéo pour traitement par FootAndBall, cela sans avoir à installer l'application de base sur la machine.
Cette interface a été développée en Django.

Voici l'architecture de l'application :

<img src="https://cdn.discordapp.com/attachments/1183508687923453956/1195773028282421278/Image3.jpg?ex=65b5356a&is=65a2c06a&hm=0cdf53a4b105edbbf5a1147e0623674203d1e567bf66505dc2ae8c6c38a1464c&" alt="archiDjango">

```python
# views.py

- loginView(request) # This function returns the render of the login page.
- logoutView(request) # This function returns the render for the logout button.
- registerView(request) # This function returns the render for the register page.
- dashboard(request) # This function returns the render for the dashboard page.
- uploadpage(request) # This function returns the render for the upload page, the page defines the form for the treatment of the input video)
- uploadpageML(request) # This function returns the render for the upload page ML (defines the form for the treatment of other types of data)

# models.py

class inputFile(models.Model) # This class defines where the input file will be saved.

class CustomUserManager(BaseUserManager) # This class defines a custom user manager for the app.
    
    def create_user(self, username, email, password, **extra_fields):
        # username : str, email : str, password : str
        # This function returns the user after saving it in the SQLite database.
    def create_superuser(self, username, email, password, **extra_fields):
        # username : str, email : str, password : str
        # This function calls the create_user function (with staff, superuser and active tags as extra fields).

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # This class defines the user of this app with :
        # email : str
        # username : str
        # is_staff : boolean
        # is_active : boolean
        # date_joined : DateTimeField
```
