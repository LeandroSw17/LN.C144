import cv2
import numpy as np

# Anexe a câmera indexada como 0
camera = cv2.VideoCapture(0)

# Definindo a largura do quadro e a altura do quadro como 640 X 480
camera.set(3, 640)
camera.set(4, 480)

# Carregando a imagem da montanha
mountain = cv2.imread('mount_everest.jpg')

# Redimensionando a imagem da montanha como 640 X 480
mountain = cv2.resize(mountain, (640, 480))

while True:
    # Ler um quadro da câmera conectada
    status, frame = camera.read()

    # Se obtivermos o quadro com sucesso
    if status:
        # Inverta-o
        frame = cv2.flip(frame, 1)

        # Convertendo a imagem em RGB para facilitar o processamento
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Definindo os limites de cor (ajuste conforme necessário)
        lower_bound = np.array([0, 50, 0], dtype=np.uint8)
        upper_bound = np.array([50, 255, 50], dtype=np.uint8)

        # Criando a máscara
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # Invertendo a máscara
        inverted_mask = cv2.bitwise_not(mask)

        # Bitwise_and - operação para extrair o primeiro plano/pessoa
        result = cv2.bitwise_and(frame, frame, mask=inverted_mask)

        # Exiba a imagem final
        cv2.imshow('Resultado', result)

        # Aguarde 1ms antes de exibir outro quadro
        code = cv2.waitKey(1)
        if code == 32:  # Código ASCII para a tecla de espaço
            break

# Libere a câmera e feche todas as janelas abertas
camera.release()
cv2.destroyAllWindows()
