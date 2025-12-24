# --- draw_engine.py ---

# File ini berisi implementasi murni dari algoritma grafika dasar.

def dda_line(x1, y1, x2, y2):
    """
    Menggambar garis lurus menggunakan Algoritma DDA.
    Mengembalikan list koordinat x dan y dari piksel-piksel garis.
    """
    dx = x2 - x1
    dy = y2 - y1
    # Tentukan jumlah langkah berdasarkan perubahan terbesar
    steps = int(max(abs(dx), abs(dy)))
    
    # Tangani kasus titik awal dan akhir sama
    if steps == 0:
        return [round(x1)], [round(y1)]

    # Hitung pertambahan (increment) per langkah
    x_inc = dx / steps
    y_inc = dy / steps
    
    x_points, y_points = [], []
    x, y = x1, y1
    
    # Iterasi dan bulatkan koordinat di setiap langkah
    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc
    return x_points, y_points

def midpoint_circle(xc, yc, r):
    """
    Menggambar lingkaran menggunakan Algoritma Midpoint Circle.
    Mengembalikan list koordinat x dan y dari piksel-piksel lingkaran.
    """
    x_points, y_points = [], []
    x = 0
    y = r
    # Parameter keputusan awal
    d = 1 - r 
    
    # Fungsi bantuan internal untuk mencerminkan titik ke 8 oktan (simetri)
    def plot_circle_points(xc, yc, x, y):
        xs = [xc+x, xc-x, xc+x, xc-x, xc+y, xc-y, xc+y, xc-y]
        ys = [yc+y, yc+y, yc-y, yc-y, yc+x, yc+x, yc-x, yc-x]
        x_points.extend(xs)
        y_points.extend(ys)

    # Plot titik awal
    plot_circle_points(xc, yc, x, y)

    # Loop hanya untuk 1/8 lingkaran (dari atas ke kanan bawah)
    while x < y:
        x += 1
        if d < 0:
            # Pilih piksel Timur (E)
            d = d + 2*x + 1
        else:
            # Pilih piksel Tenggara (SE)
            y -= 1
            d = d + 2*x - 2*y + 1
        # Cerminkan titik yang baru didapat
        plot_circle_points(xc, yc, x, y)
        
    return x_points, y_points
