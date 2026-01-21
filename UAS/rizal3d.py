from ursina import *
from ursina.shaders import lit_with_shadows_shader 

import random

# Inisialisasi Aplikasi
app = Ursina()

# --- 1. SETUP LAYAR & VISUAL ---
window.size = (1500, 800)
window.center_on_screen()
window.title = "Simulator Mobil Rizal - Final Fix"
window.color = color.gray

# --- 2. ILUSI KEDALAMAN ---
matahari = DirectionalLight()
matahari.look_at(Vec3(1, -1, -1))
matahari.shadows = True 

Sky(texture='sky_default')

scene.fog_density = 0.01
scene.fog_color = color.light_gray

# --- 3. ARENA ---
batas_arena = 95 

lantai = Entity(
    model='plane',
    texture='grass',
    scale=(200, 1, 200),
    color=color.rgb(50, 150, 50),
    collider='box',
    shader=lit_with_shadows_shader
)

# --- 4. MOBIL ---
mobil = Entity(
    model='mobil_fix',          
    texture='Zombie_Atlas',     
    scale=0.5,
    position=(0, 1, 0),
    collider='box',             
    rotation_y=180,
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
        collider='box',
        texture='white_cube',
        shader=lit_with_shadows_shader
    )
    if distance(box, mobil) < 15:
        box.x += 30
    kotak_rintangan.append(box)

# --- 6. DINDING BATAS ---
Entity(model='cube', scale=(200, 5, 1), position=(0, 2.5, 100), color=color.rgba(255,0,0,50), collider=None)
Entity(model='cube', scale=(200, 5, 1), position=(0, 2.5, -100), color=color.rgba(255,0,0,50), collider=None)
Entity(model='cube', scale=(1, 5, 200), position=(100, 2.5, 0), color=color.rgba(255,0,0,50), collider=None)
Entity(model='cube', scale=(1, 5, 200), position=(-100, 2.5, 0), color=color.rgba(255,0,0,50), collider=None)


# --- LOGIKA GAME ---
def update():
    kecepatan_maju = 25
    kecepatan_putar = 120

    if held_keys['w']:
        mobil.position += mobil.forward * time.dt * kecepatan_maju
    if held_keys['s']:
        mobil.position -= mobil.forward * time.dt * kecepatan_maju
    if held_keys['a']:
        mobil.rotation_y -= time.dt * kecepatan_putar
    if held_keys['d']:
        mobil.rotation_y += time.dt * kecepatan_putar

    mobil.x = clamp(mobil.x, -batas_arena, batas_arena)
    mobil.z = clamp(mobil.z, -batas_arena, batas_arena)

    hit_info = mobil.intersects()
    if hit_info.hit and hit_info.entity != lantai:
        mobil.color = color.red
        mobil.position = (0, 0.5, 0)
        mobil.rotation = (0, 180, 0)
        invoke(pulihkan_warna, delay=0.5)

    # --- PERBAIKAN KAMERA DI SINI ---
    # Tadinya -18 (di depan mobil), sekarang kita ubah jadi +18 (di belakang mobil)
    # Offset: (Kanan, Atas, Belakang)
    target_posisi_kamera = mobil.position + (0, 10, 18) 
    
    camera.position = lerp(camera.position, target_posisi_kamera, time.dt * 5)
    camera.look_at(mobil.position)

def pulihkan_warna():
    mobil.color = color.white

app.run()
