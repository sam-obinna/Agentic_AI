# Use a lightweight Python image
FROM python:3.11-slim

# Set environment variables explicitly
ENV HOME=/app
ENV PATH="$HOME/.local/bin:$PATH"
ENV HF_HOME=/app/.cache  # Ensures Hugging Face models cache correctly

WORKDIR $HOME

# Copy requirements and install dependencies
COPY backend/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend files
COPY backend ./backend
COPY templates ./templates

# Ensure cache directories exist explicitly
RUN mkdir -p $HOME/.cache && chmod -R 777 $HOME/.cache

# Expose the port FastAPI will run on (Render requires a public port)
EXPOSE 10000

# Run the FastAPI app explicitly
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "10000"]
