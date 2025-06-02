Download and install Ollama from the official website:

https://ollama.com/download

Open VS Code and Create a Python Virtual Environment (Optional but Recommended)
In your project folder:

python -m venv venv
venv\Scripts\activate  # Activates the virtual environment

Install Python Dependencies
In your activated terminal:

pip install streamlit ollama pillow
pillow is needed for working with images (PIL.Image)

Pull the LLaMA 3.2 Vision Model
Now, open a separate terminal (outside VS Code) and run:

ollama run llama3.2-vision

Run Your Streamlit App
streamlit run your_script.py