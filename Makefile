# Nome do arquivo objeto gerado
TARGET = mandelbrot.so

# Compilador e flags
CC = gcc
CFLAGS = -fPIC -shared

# Arquivos fonte
SRC = mandelbrot.c

# Arquivo Python principal
PYTHON_SCRIPT = main.py

# Default target: compilar a biblioteca compartilhada
all: $(TARGET)

# Compilar o arquivo .so
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Executar o script Python
run: $(TARGET)
	python3 $(PYTHON_SCRIPT)

# Limpar os arquivos gerados
clean:
	rm -f $(TARGET)

.PHONY: all clean run
