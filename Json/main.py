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
    "Meja 3: Area lesehan depan, sirkulasi udara segar.",
    "Meja 4: Dekat dispenser, gampang ambil minum.",
    "Meja 5: Meja kayu besar buat kumpul organisasi.",
    "Meja 6: Pojok adem dengan fasilitas kipas angin sendiri.",
    "Meja 7: Dekat jendela, pemandangan ke arah jalan.",
    "Meja 8: Lesehan pojok dalam, nyaman buat santai.",
    "Me_ja 9: Dekat rak koran, cocok buat makan sambil baca.",
    "Meja 10: Dekat tempat cuci tangan (wastafel)."
]

desc_mpo_lines = [
    "Meja 1: Area depan banget, cocok buat yang buru-buru.",
    "Meja 2: Tengah ruangan, dekat dengan tempat kerupuk.",
    "Me_ja 3: Pojok kanan, ada colokan listrik tersembunyi.",
    "Meja 4: Area lesehan paling belakang, sangat tenang.",
    "Meja 5: Meja bundar unik, asik buat ngobrol melingkar.",
    "Meja 6: Dekat rak gorengan, tinggal comot (jangan lupa bayar).",
    "Meja 7: Lesehan dinding, sandarannya empuk.",
    "Meja 8: Meja standar dekat kipas angin dinding.",
    "Meja 9: Dekat speaker musik, suasananya asik.",
    "Meja 10: Dekat pintu dapur, aroma masakan menggoda."
]

desc_ma_sin = [
    "Meja 1: Dekat pintu masuk, sirkulasi udara paling mantap.",
    "Meja 2: Meja standar dengan stop kontak di bawah meja.",
    "Meja 3: Meja tengah, posisi paling strategis.",
    "Meja 4: Dekat pantry, bisa liat proses masak Indomie.",
    "Meja 5: Meja pojok dengan pencahayaan warm putih.",
    "Meja 6: Tepat di depan TV besar, pas jadwal bola.",
    "Meja 7: Lesehan samping, suasana kayu yang hangat.",
    "Meja 8: Lesehan belakang, area khusus dilarang merokok.",
    "Meja 9: Meja kecil, pas banget buat yang makan sendirian.",
    "Meja 10: Pojok paling adem, kipas anginnya kenceng."
]

# --- DATA PENJUAL UTUH ---
data_penjual = [
    {
        "id": "12052601", "nama": "Burjo Desi", "meja": "2", 
        "desc": desc_desi, "lat": -7.0517063, "lng": 110.4403961
    },
    {
        "id": "12052602", "nama": "Burjo Pa Weka", "meja": "6", 
        "desc": desc_pa_weka, "lat": -7.0512984, "lng": 110.4391414
    },
    {
        "id": "12052603", "nama": "Burjo Mpo Lines", "meja": "1", 
        "desc": desc_mpo_lines, "lat": -7.0518414, "lng": 110.4337752
    },
    {
        "id": "12052604", "nama": "Burjo Ma Sin", "meja": "9", 
        "desc": desc_ma_sin, "lat": -7.0502177, "lng": 110.4417592
    }
]

def update_database():
    print("⏳ Menghapus data lama dan mengunggah data baru...")
    for p in data_penjual:
        doc_ref = db.collection('penjual').document(p['id'])
        
        # Simpan Data Utama
        doc_ref.set({
            "nama_burjo": p['nama'],
            "status_meja": p['meja'],
            "deskripsi_meja": p['desc'],
            "lokasi": firestore.GeoPoint(p['lat'], p['lng'])
        })
        
        # Reset & Simpan Menu (Opsional jika ingin update menu juga)
        menu_ref = doc_ref.collection('katalog_menu')
        for m_old in menu_ref.list_documents(): m_old.delete()
        
        menu_ref.add({"nama": "Nasi Ayam Bali", "harga": 15000, "kategori": "Makanan", "is_active": True})
        menu_ref.add({"nama": "Indomie Tante", "harga": 10000, "kategori": "Makanan", "is_active": True})
        menu_ref.add({"nama": "Es Teh Manis", "harga": 4000, "kategori": "Minuman", "is_active": True})
        menu_ref.add({"nama": "Kopi Susu", "harga": 5000, "kategori": "Minuman", "is_active": True})

    print("✅ Database MyBurjo SIAP! Semua deskripsi meja sudah unik.")

update_database()