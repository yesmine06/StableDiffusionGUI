import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import torch
from diffusers import StableDiffusionPipeline
import time
from authtoken import auth_token  

# Initialisation de l'application
app = tk.Tk()
app.geometry("532x622")
app.title("Stable Diff")
ctk.set_appearance_mode("dark")

# Champ de texte pour le prompt
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="blue", fg_color="white")
prompt.place(x=10, y=10)

# Label pour l'image générée
lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=110)

# Barre de progression
progress_bar = ctk.CTkProgressBar(master=app, width=500)
progress_bar.place(x=10, y=550)

# Label pour le temps de génération
time_label = ctk.CTkLabel(master=app, text="", font=("Arial", 12),text_color="blue")
time_label.place(x=10, y=580)

# Détection du périphérique (CPU forcé)
device = "cpu"
print(f"Using device: {device}")

# Chargement du modèle
modelid = "CompVis/stable-diffusion-v1-4"
try:
    pipe = StableDiffusionPipeline.from_pretrained(modelid, use_auth_token=auth_token)
    pipe.to(device)
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")
    exit()

# Fonction pour générer une image
def Generate():
    user_prompt = prompt.get()
    progress_bar.set(0.1)
    app.update_idletasks()

    start_time = time.time()
    try:
        # Génération de l'image sur CPU
        image = pipe(user_prompt, guidance_scale=7.5).images[0]

        # Sauvegarde et affichage de l'image générée
        image.save('generatedimage.png')
        img = ImageTk.PhotoImage(image)
        lmain.configure(image=img)
        lmain.image = img

        # Affichage du temps de génération
        time_label.configure(text=f"Time taken: {time.time() - start_time:.2f} seconds")

        # Mise à jour de la barre de progression
        progress_bar.set(1.0)
        app.update_idletasks()

    except Exception as e:
        error_msg = f"Erreur lors de la génération : {e}"
        print(error_msg)
        time_label.configure(text=error_msg)

# Bouton pour lancer la génération
trigger = ctk.CTkButton(
    master=app, 
    height=40, 
    width=120, 
    font=("Arial", 20),  
    text_color="white", 
    fg_color="blue", 
    text="Generate", 
    command=Generate
)
trigger.place(x=206, y=60)

# Lancement de l'application
app.mainloop()
