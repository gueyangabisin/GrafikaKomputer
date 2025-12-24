import matplotlib.pyplot as plt
from draw_engine import dda_line, midpoint_circle

# Koordinat awal Matahari
sun_center = [20, 90]
sun_radius = 10

def draw_scene():
    """Fungsi untuk menggambar ulang seluruh objek di canvas"""
    plt.clf() # Bersihkan canvas
    
    # --- GAMBAR RUMAH (Statis) ---
    # Kita definisikan garis-garis rumah di sini
    lines = [
        ((30, 20), (70, 20)), ((70, 20), (70, 60)), ((70, 60), (30, 60)), ((30, 60), (30, 20)), # Dinding
        ((30, 60), (50, 80)), ((50, 80), (70, 60)), # Atap
        ((45, 20), (45, 40)), ((55, 20), (55, 40)), ((45, 40), (55, 40)) # Pintu
    ]
    
    for start, end in lines:
        lx, ly = dda_line(start[0], start[1], end[0], end[1])
        plt.scatter(lx, ly, color='black', s=2, marker='s')

    # --- GAMBAR MATAHARI (Dinamis) ---
    sx, sy = midpoint_circle(sun_center[0], sun_center[1], sun_radius)
    plt.scatter(sx, sy, color='orange', s=5, marker='s')

    # Setting Canvas
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Gunakan tombol PANAH untuk menggeser Matahari")
    plt.draw()

def on_press(event):
    """Fungsi yang dipanggil setiap kali tombol keyboard ditekan"""
    step = 3 # Besarnya pergeseran (Translasi)
    
    if event.key == 'up':
        sun_center[1] += step
    elif event.key == 'down':
        sun_center[1] -= step
    elif event.key == 'left':
        sun_center[0] -= step
    elif event.key == 'right':
        sun_center[0] += step
    
    draw_scene() # Gambar ulang setelah koordinat berubah

# Inisialisasi Window
fig, ax = plt.subplots(figsize=(6, 6))

# Hubungkan event keyboard ke fungsi on_press
fig.canvas.mpl_connect('key_press_event', on_press)

# Gambar scene pertama kali
draw_scene()

plt.show()
