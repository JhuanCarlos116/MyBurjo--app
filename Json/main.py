import firebase_admin
from firebase_admin import credentials, firestore

# 1. Inisialisasi Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- DAFTAR DESKRIPSI MEJA ---
desc_desi = [
    "Meja 1: Dekat colokan listrik, pas buat nugas lama.",
    "Meja 2: Area lesehan pojok, lebih tenang dan privat.",
    "Meja 3: Meja kayu standar tepat di bawah kipas angin.",
    "Meja 4: Dekat pintu masuk, akses cepat dan sirkulasi oke.",
    "Meja 5: Lesehan tengah, cocok buat makan bareng temen.",
    "Meja 6: Meja panjang kapasitas 4-6 orang.",
    "Meja 7: Area semi-outdoor, cocok buat yang merokok.",
    "Meja 8: Dekat TV, pas banget buat nonton bareng.",
    "Meja 9: Meja favorit, pencahayaan paling terang di sini.",
    "Meja 10: Pojok belakang, area paling sepi dan adem."
]

desc_pa_weka = [
    "Meja 1: Dekat kasir, gampang kalau mau nambah pesanan.",
    "Meja 2: Meja tengah dengan akses stop kontak di dinding.",
    "Meja 3: Area lesehan depan, sirkulasi udara bagus.",
    "Meja 4: Meja panjang, bisa untuk kelompok belajar.",
    "Meja 5: Pojok ruangan, tempat favorit buat nugas.",
    "Meja 6: Dekat jendela, pencahayaan alami terang.",
    "Meja 7: Meja bundar kecil, cocok untuk berdua.",
    "Meja 8: Area agak masuk ke dalam, lebih tenang.",
    "Meja 9: Dekat area dapur, wangi makanan bikin laper.",
    "Meja 10: Lesehan luas di bagian belakang."
]

desc_mpo_lines = [
    "Meja 1: Meja paling depan, bisa lihat jalanan.",
    "Meja 2: Dekat meja kasir.",
    "Meja 3: Meja standar kapasitas 4 orang.",
    "Meja 4: Lesehan nyaman dengan bantal duduk.",
    "Meja 5: Meja kayu jati tebal.",
    "Meja 6: Area tengah yang cukup luas.",
    "Meja 7: Dekat colokan listrik.",
    "Meja 8: Pojokan yang nyaman.",
    "Meja 9: Meja untuk rombongan besar.",
    "Meja 10: Area khusus yang lebih privat."
]

desc_ma_sin = [
    "Meja 1: Meja dekat pintu.",
    "Meja 2: Lesehan dekat jendela.",
    "Meja 3: Meja tengah.",
    "Meja 4: Meja dengan kursi sofa.",
    "Meja 5: Area favorit pengunjung.",
    "Meja 6: Dekat rak majalah/buku.",
    "Meja 7: Meja panjang.",
    "Meja 8: Lesehan belakang.",
    "Meja 9: Meja paling terang.",
    "Meja 10: Pojok sepi."
]

# --- DAFTAR DATA PENJUAL ---
data_penjual = [
    {
        "id": "12052601", "nama": "Burjo Desi", "meja": "2", 
        "pin": "1234", 
        "desc": desc_desi, "lat": -7.052062, "lng": 110.437145
    },
    {
        "id": "12052602", "nama": "Burjo Pa Weka", "meja": "5", 
        "pin": "6339", 
        "desc": desc_pa_weka, "lat": -7.0512984, "lng": 110.4391414
    },
    {
        "id": "12052603", "nama": "Burjo Mpo Lines", "meja": "1", 
        "pin": "", 
        "desc": desc_mpo_lines, "lat": -7.0518414, "lng": 110.4337752
    },
    {
        "id": "12052604", "nama": "Burjo Ma Sin", "meja": "9", 
        "pin": "1111", 
        "desc": desc_ma_sin, "lat": -7.0502177, "lng": 110.4417592
    }
]

def update_database():
    print("⏳ Sedang menyinkronkan data ke Firebase...")
    for p in data_penjual:
        doc_ref = db.collection('penjual').document(p['id'])
        
        doc_ref.set({
            "nama_burjo": p['nama'],
            "status_meja": p['meja'],
            "deskripsi_meja": p['desc'],
            "lokasi": firestore.GeoPoint(p['lat'], p['lng']),
            "pin": str(p['pin'])
        }, merge=True)
        
    print("✅ Selesai! Data dan PIN sekarang sudah tersimpan di Firebase.")

if __name__ == "__main__":
    update_database()