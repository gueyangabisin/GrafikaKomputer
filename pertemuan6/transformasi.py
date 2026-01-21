import pygame
import sys

pygame.init()

# Warna (R, G, B)
WHITE = (255, 255, 255)
BLUE  = (50, 150, 255)
BLACK = (0, 0, 0)
RED   = (255, 50, 50)

# Ukuran Layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulasi Transformasi 2D (T=Rotasi, W/S=Translasi, R=Reset)")

# --- Variabel Transformasi (State) ---
# Posisi awal (Tengah layar)
start_x, start_y = WIDTH // 2, HEIGHT // 2
x, y = start_x, start_y
angle = 0  # Sudut rotasi dalam derajat

# Kecepatan perubahan
translation_speed = 5
rotation_speed = 5

# Membuat Objek (Sebuah Kotak)
rect_size = 100
# Surface asli (tidak pernah diputar langsung agar tidak hancur/distorsi)
original_surface = pygame.Surface((rect_size, rect_size), pygame.SRCALPHA)
original_surface.fill(BLUE)
# Gambar garis pinggir agar rotasi terlihat jelas
pygame.draw.rect(original_surface, BLACK, (0, 0, rect_size, rect_size), 4)
# Gambar tanda 'Atas' untuk orientasi
pygame.draw.line(original_surface, RED, (rect_size//2, rect_size//2), (rect_size//2, 0), 4)

# --- Loop Utama Program ---
running = True
clock = pygame.time.Clock()

while running:
    # 1. Cek Input (Event Handling)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Logika tombol (Single press trigger)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("Posisi di-RESET")
                x, y = start_x, start_y
                angle = 0

    # Logika tombol (Continuous hold) - Agar gerakan lebih halus
    keys = pygame.key.get_pressed()
    
    # t = Rotasi (melawan arah jarum jam)
    if keys[pygame.K_t]:
        angle += rotation_speed
        
    # w = Translasi Sumbu Y (Gerak ke atas - Y berkurang)
    if keys[pygame.K_w]:
        y -= translation_speed 
        
    # s = Translasi Sumbu X (Gerak ke kanan - X bertambah)
    if keys[pygame.K_s]:
        x += translation_speed

    # 2. Proses Matematika & Rendering
    screen.fill(WHITE) # Bersihkan layar
    
    # --- LOGIKA ROTASI ---
    # Kita memutar gambar asli. pygame.transform.rotate memutar berlawanan jarum jam.
    rotated_surface = pygame.transform.rotate(original_surface, angle)
    
    # --- LOGIKA TRANSLASI & PUSAT ROTASI ---
    # Agar berputar di poros tengah, kita harus mengambil 'rect' dari gambar yang sudah diputar
    # dan mengatur titik tengahnya (center) ke posisi x, y saat ini.
    rect = rotated_surface.get_rect(center=(x, y))

    # 3. Gambar ke Layar
    screen.blit(rotated_surface, rect)
    
    # Tampilkan Info Koordinat
    font = pygame.font.Font(None, 24)
    info_text = f"Posisi X: {x}, Y: {y} | Sudut: {angle % 360}°"
    text_surf = font.render(info_text, True, BLACK)
    screen.blit(text_surf, (10, 10))

    pygame.display.flip()
    clock.tick(60) # Batasi 60 FPS

pygame.quit()
sys.exit()
      
