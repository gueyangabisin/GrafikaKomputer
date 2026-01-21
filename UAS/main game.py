from ursina import *
from ursina.shaders import lit_with_shadows_shader
import random

app = Ursina()

# --- 1. SETUP LAYAR ---
window.size = (1500, 800)
window.center_on_screen()
window.title = "Simulator Mobil Rizal - Camera Follow"
window.color = color.gray

# --- 2. ILUSI KEDALAMAN ---
pivot = Entity()
matahari = DirectionalLight(parent=pivot, y=20, z=10, shadows=True)
matahari.look_at(Vec3(0, 0, 0))

Sky(texture='sky_default')
scene.fog_density = 0.015
scene.fog_color = color.light_gray

# --- 3. ARENA ---
batas_arena = 95 
lantai = Entity(
    model='plane', texture='grass',
    scale=(200, 1, 200),
    color=color.rgb(50, 150, 50),
    collider='box',
    shader=lit_with_shadows_shader
)

# --- 4. DATA POSISI ---
# Gunakan Rotasi yang menurutmu pas tadi (misal 1079, 180, 0)
# Kalau di snippet kamu pakai rotation_y=180, saya pakai itu dulu.
# Tapi sebaiknya pakai angka kalibrasi 1079 jika mobil terlihat miring.
POSISI_AWAL = Vec3(0, 1, 0)
ROTASI_AWAL = (0, 180, 0) # Ganti ke (1079, 180, 0) jika perlu

mobil = Entity(
    model='mobil_fix',          
    texture='Zombie_Atlas',     
    scale=0.5,
    position=POSISI_AWAL,
    rotation=ROTASI_AWAL,
    # Hapus collider fisik, kita pakai logika jarak manual
    shader=lit_with_shadows_shader
)

# --- 5. RINTANGAN ---
kotak_rintangan = [] 
for i in range(30):
    box = Entity(
        model='cube',
        color=color.red,
        scale=(2, 2, 2),
        position=(random.randint(-80, 80), 1, random.randint(-80, 80)),
        texture='white_cube',
        shader=lit_with_shadows_shader
    )
    if distance(box, mobil) < 20:
        box.x += 40
    kotak_rintangan.append(box)

# Dinding Batas
Entity(model='cube', scale=(200, 5, 1), position=(0, 2.5, 100), color=color.rgba(255,0,0,50))
Entity(model='cube', scale=(200, 5, 1), position=(0, 2.5, -100), color=color.rgba(255,0,0,50))
Entity(model='cube', scale=(1, 5, 200), position=(100, 2.5, 0), color=color.rgba(255,0,0,50))
Entity(model='cube', scale=(1, 5, 200), position=(-100, 2.5, 0), color=color.rgba(255,0,0,50))


# --- LOGIKA GAME ---
def update():
    kecepatan_maju = 30
    kecepatan_putar = 100

    # 1. GERAKAN
    if held_keys['w']:
        mobil.position += mobil.forward * time.dt * kecepatan_maju
    if held_keys['s']:
        mobil.position -= mobil.forward * time.dt * kecepatan_maju
    if held_keys['a']:
        mobil.rotation_y -= time.dt * kecepatan_putar
    if held_keys['d']:
        mobil.rotation_y += time.dt * kecepatan_putar

    # 2. BATAS WILAYAH
    mobil.x = clamp(mobil.x, -batas_arena, batas_arena)
    mobil.z = clamp(mobil.z, -batas_arena, batas_arena)

    # 3. TABRAKAN (Logika Jarak)
    for box in kotak_rintangan:
        if distance(mobil, box) < 2.5:
            print("DUAR!")
            mobil.color = color.red
            mobil.position = POSISI_AWAL
            mobil.rotation = ROTASI_AWAL # Reset rotasi biar kamera ga bingung
            invoke(pulihkan_warna, delay=0.5)
            break 

    # --- 4. PERBAIKAN KAMERA (FOLLOW CAM) ---
    # Logika Lama: mobil.position + (0, 10, 18) -> Ini salah karena arahnya tetap (Global)
    
    # Logika Baru: Gunakan 'mobil.back'
    # Artinya: "Ambil posisi di BELAKANG bokong mobil, kemanapun dia menghadap"
    offset_belakang = mobil.back * 18  # 18 meter di belakang mobil
    offset_atas     = mobil.up * 8     # 8 meter di atas mobil
    
    target_posisi_kamera = mobil.position + offset_belakang + offset_atas
    
    # Lerp biar pergerakan kamera halus (semakin kecil angka 5, semakin lambat/smooth)
    camera.position = lerp(camera.position, target_posisi_kamera, time.dt * 5)
    
    # Kamera selalu menatap mobil
    camera.look_at(mobil.position)

def pulihkan_warna():
    mobil.color = color.white

app.run()