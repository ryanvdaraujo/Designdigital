from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def sobre():
    textosobre = "Hey, how do you do? Welcome to my portfolio. My name is Ryan, I'm 18 years old, and I am currently studying Software Development at Fatec in SJC. I developed an interest in programming in 2022 when I was studying Industrial Automation and programming microcontrollers using C and C++ (nowadays, I've embraced the world of Python and I'm more familiar with it, haha). It was an important experience that led me to discover the world of scripting, as I've always had a liking for logic. Apart from programming, I enjoy playing soccer/futsal. I have trained and played for a few teams over the years."
    return render_template("sobre.html", textosobre = textosobre )

@app.route("/projects")
def projetos():
    textovanmisterio = "Van Mistério (Clébinho) - A project developed by me and some friends that involved the use of a microcontroller programmed in C++. Its proposal was to use the Bluetooth connection of a cellphone to control the car. We used an Arduino, a DC mini motor, a battery, a Bluetooth module, and some other materials. With it, we achieved third place in the race that took place at ETEC - SJC."
    textoplacar = "That was the project developed as my final thesis. The idea was to have an automated scoreboard for the robot soccer matches (an annual event at ETEC), so that everyone could know the score of the game without the need for hand counting. We initially created a prototype in online simulators and then proceeded with assembly and programming. Afterwards, we integrated it into the field (the table in the photo)."
    textodatasars = "Data-Sars is the project I recently developed with my API group in the 1st semester at Fatec. It aims to facilitate the analysis of data related to the consequences of COVID-19 by providing graphs on various topics, enabling a wide and easy visualization of the facts."
    return render_template("projetos.html", textovanmisterio = textovanmisterio, textoplacar = textoplacar, textodatasars = textodatasars)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")