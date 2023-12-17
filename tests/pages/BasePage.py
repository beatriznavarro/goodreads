class BasePage:
    def __init__(self, driver):
        self.driver = driver

    
    def swipe_down(self):
        # Obter tamanho da tela
        size = self.driver.get_window_size()

        # Coordenadas iniciais e finais para o gesto de swipe
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)

        # Realizar o gesto de swipe
        self.driver.swipe(size['width'] // 2, start_y, size['width'] // 2, end_y, duration=800)