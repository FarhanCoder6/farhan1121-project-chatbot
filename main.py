# Step 1: Install libraries
!pip install transformers
!pip install ipywidgets
# Step 2: Import required modules
from transformers import pipeline
import ipywidgets as widgets
from IPython.display import display

# Step 3: Load GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Step 4: Create UI elements
input_box = widgets.Text(
    value='',
    placeholder='Apna prompt yahan likhein...',
    description='Input:',
    layout=widgets.Layout(width='80%')
)

output_box = widgets.Textarea(
    value='',
    placeholder='Generated text yahan dikhega...',
    description='Output:',
    layout=widgets.Layout(width='80%', height='150px')
)

submit_button = widgets.Button(
    description='Submit',
    button_style='success',
    tooltip='Click to generate text'
)

clear_button = widgets.Button(
    description='Clear',
    button_style='warning',
    tooltip='Click to clear text'
)

# Step 5: Define the function to run on button click
def on_button_click(b):
    prompt = input_box.value
    if prompt.strip() == "":
        output_box.value = "⚠️ Please enter a prompt."
        return
    output_box.value = "Generating text..."
    result = generator(prompt, max_length=100, num_return_sequences=1)
    output_box.value = result[0]['generated_text']

# Step 6: Define the function to clear text
def on_clear_button_click(b):
    input_box.value = ""
    output_box.value = ""

# Step 7: Link buttons to functions
submit_button.on_click(on_button_click)
clear_button.on_click(on_clear_button_click)

# Step 8: Display the UI
display(input_box, submit_button, clear_button, output_box)
