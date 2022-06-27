 <h1>Text Player</h1>

## That's a simple CLI to read texts word by word
<br>

Unfortunately, reading large texts takes time. This CLI assumes that a person can read much faster if they don't have to "navigate" the text with their eyes. The first few times it may take you a little longer to read some texts clearly but with a few tries, you will be able to read much faster than usual and you will have more focus on what you are reading.

## NOTE: Currently, it can open just pdf files
<br>

## Installation

    pip install pynput pypdf2

    git clone https://github.com/RadinhoDePilha/TextPlayer

    cd TextPlayer

## Usage 

On the project folder:

    python TextPlayer.py file.pdf

You can add the argument -p or --page with the number of the page that you wanna start
<br>
<h3>Controls in the CLI</h3>
<br>

- **Right/Left:** Change the speed of the words displayed 
<br>

- **Space:** Pause/Run the displayer
<br>

- **Enter:** Go to the next page

- **Esc:** Exit the CLI
<br>

- **i:** Hide/Show the information about the controls